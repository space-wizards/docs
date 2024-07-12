# Low Power Handling (Pow3r)

This doc is for bikeshedding what should happen to station equipment under low-power and power-spike scenarios. 

## TL;DR

Power is no longer buffered to shit with big batteries that can keep the station running for hours. The station is vulnerable to large-scale grid fluctuations if they happen. Batteries are in place but need time to "ramp up" to meet demand if power cuts out suddenly.

## High level

### How Equipment Responds to power shortages
When the full amount of power is provided to a machine, it will operate as normal. When power is not available, the machine will completely turn off (should machines have power switches?) This unpowered state is the same state as an unanchored consumer.

When a brownout occurs, the machine will respond depending on it's consumer type. Each machine has a power draw, a brownout only occurs for a machine if the power available to it is less than the draw amount. This is an independent event for every machine on the network.

* If the consumer is an analogue device like a motor/battery charger, it will reduce its speed (each machine will define what that means), but still operate as normal. Usually these types of consumers will have no electronics on them.

* If the consumer is a digital device (most machines/terminals on the station, anything you can network to) it will have a built-in feature where it goes into a power cycle. It will turn itself off for ~5 seconds and then check to see if it can turn itself back on, repeating until power is restored.

* If the consumer is a incandescent light bulb, then it will reduce it's light range, basically dimming. This is a linear relationship with the power deficit, it does not flicker.

* If the consumer is a fluorescent lamp (most lighting in station, they use tubes) then it will flicker off/on with the frequency based on the deficit. When implementing this you probably want some randomness, and don't make it flicker too fast, this isn't a strobe.

* Advanced machines like the particle accelerator/emitters could have reduced fire rate depending on input power (the idea being that they need to charge internal capacitors). Should probably should have some form of curve here so that 50% power results in 25% firing speed or similar. Or actually accumulate charge inside of themselves to fire (invisible built-in capacitors), which would respond more realistically to frequent fluctuations, and prevent power pulsing metagame (see ONI exploits).

Some machines will have an internal battery entity that can store/provide power, which can mitigate these effects.

### Power storage on the station
Because of the size of the station and the number of high-power consumers on it, large power demand fluctuations are to be expected. Because most generators cannot respond quickly to this, power needs to be stored to provide consistent service to the rest of the station.

The main storage device is the SMES. It is expected that engineering will have a group of these to buffer power into for the entire station. Other critical departments may have a single SMES nearby in maintenance, so that in the event of a power shortage they can still operate. Hallways and other low-priority areas will not have a dedicated SMES, so in the event of a power shortage they will turn off.

We want to avoid the overuse of this, so that power fluctuations on the station have a realtime effect on lights and machines. A nice balance will have to be struck here.

### Power supply wind up/down

Power supply equipment (batteries or generation) has to match power load of their network, Barotrauma style. If a new load gets attached to a circuit, supply equipment has to "wind up" to match the demand (assuming it has the ability to match the demand, of course). This takes time during which the grid will be under-supplied, resulting in brownout effects described above. There should also be a "burst" power windup to deal with small fluctuations.

Generally, batteries will be able to match this change in demand more quickly than actual generation equipment. This means that the APC batteries, substation batteries (if we decide to have them) and SMES all add "filtering" against sudden power fluctuations. They are not wizardry though: if engine power cuts off completely, everybody on the station will see the lights flicker hard for a few moments while the SMES and APCs ramp up to fill the sudden hole in power supply.

It should be noted that batteries are considered to be "passing through" all power that isn't going through internal storage. So if you have 10 kW load, 10 kW supply, and full battery: when the supply cuts off the battery is considered as supplying 0 W and has to wind up from there.

Due to the hierarchical power grid, if science does something funny and suddenly need an extra megawatt they'll probably only cause their own lights to really go blinky blinky before the engine/SMES can ramp up. 

Currently, I have no ideas for "problems" caused from overvoltage (in Barotrauma, over/undervoltage results in junction boxes wearing and requiring repair). Undervoltage is obvious. Just have the power monitor blink angrily at engineers for the time being, I guess.

### Power Limit at Substations

Substations will be able to limit power. So if science puts down a machine that needs 100 MW they'll just fuck only themselves. ~~let's just hope they don't hack the thing to turn the current limit off~~. We could even implement a ramp up/down for passthrough power on a substation such that science *can* use the 10 MW the engine has spare, but no quicker than the engine can ramp up to get there. This way science can get their 10 extra MW, but without causing negative effects for the rest of the station.

### APCs

APCs manage multiple power channels that default to being toggled depending on charge% of the internal battery. In SS13 these channels are equipment (computers, fabrication machines, etc...), lighting, environmental (doors/vents). Equipment cuts out at 30% APC charge, lighting at 15%.

Ideally the grid would self regulate to have lighting turn off (but nothing else) if power is sufficient to just barely run everything except lighting. Not sure how well this would work out in practice.

I do propose swapping lighting and equipment though for spook vibes.

My current idea is that APCs distribute power to all enabled channels evenly, so if there's only 50% of required grid power available, all channels will get 50% evenly instead of environ getting 100% and equipment like, 10%. APCs would still cut out channels based on their battery percentage, which I suppose could cause some funny oscillating behavior on low-power grids. Let's see how it works out. 

### Glossary for Swept

Brownout: light wants power, only gets some = light only kinda works. but instead of a light, everything.

## Power solving strategies

Actually implementing this model requires a bit more nuance than the simple electrical model in SS13/MC mods, where batteries are perfect buffers that have instantly varying supply rates.

There are two strategies I came up with to calculate, or "solve", power grids for this:
1. `GraphWalkSolver`: My first idea, it tries to treat the electrical grid as a tree (\*) and tries to walk it up/down to calculate grid loads upwards and push supply downwards. It is relatively quite complicated to implement and does not handle non-tree grids (possible) well. Would be consistent and predictable (\*) mostly, however.
2. `BatteryRampPegSolver`: My second idea. At a high level, basically does the SS13/MC model but puts the floor of a battery power ramp at its input rate. While this does generate some more wacky/inconsistent/spiky behavior on power graphs, it is extremely easy to implement. And honestly that wackiness may be desirable.

Currently, `BatteryRampPegSolver` is probably what's gonna be implemented because it's more simple in all aspects, but should do the job very well.

## `BatteryRampPegSolver`

Solves the power grid by considering each network, and the input/output rates of said networks' batteries, individually. The "floor" for the supply ramp on batteries is the input *to* that same battery, so that power can "pass through" without "going through the battery storage". This means that if power supply to a battery gets cut off, said battery's output *also* cuts off until it ramps up.

Furthermore, we set the demand of batteries on their *loading* side to that of their supplying network's unmet demand (after non-battery supplies). The idea here is that this will propagate demand upwards in the "tree" implicitly (note that this is to improve evenness of power distribution across loads. The system works before this but batteries get very uneven power satisfaction). Sort of like `GraphWalkSolver` does explicitly.

There are various inconsistencies with this model, such as really spiky graph behavior on large grid fluctuations. This is all emergent though and it seems to self-regulate *extremely* well so I am *extremely* pleased. I did notice some bi-stable configurations in testing but call it a feature.

This is O(n) because each network is passed one 

I'm serious when I said this model is simpler than `GraphWalkSolver`. These four paragraphs above compared to the entire other half of this document. Pick one.

## `GraphWalkSolver`

This is not trivial to implement for various reasons. I will now brain dump our [extensive discussions on Discord](https://discord.com/channels/310555209753690112/310555209753690112/817164553401401414).

The first problem is that this model is very easy to implement if the power network is a tree. In practice, however, the station really forms a *polytree* in the best scenario, a full directed acyclic graph (DAG) in the worst scenario.

As far as we can tell, "properly" solving the power network basically devolves into electric network analysis with resistors and such, which requires complex matrix solvers and is not easy (both because it's a ton of complex stuff I know nothing about, AND computationally). Also Acruid mentioned it might be a wave function collapse problem. So yes, quantum physics.

It seems like the best method to solve this is to just have some strict rules in how the graph is traversed by loads/sources/batteries. If implemented correctly and optimized well it should be possible to calculate efficiently at station-scale.

### Network nodes

The current model I am imagining assumes four types of nodes:

1. Suppliers: generate power on a network
2. Loads: demand power on a network
3. Diodes: connect between two networks to pass power in one direction, potentially limited in throughput.
    1. Batteries: subset of diodes that provides backup-battery functionality (think APCs)
4. Networks: groups of power devices (supplies, loads) that are interconnected via diodes.

For the purposes of all calculations, supplies and loads inside networks can be added up so that each network is one supplier and one load. This is one easy form of grouping so that we don't have to care about individual loads on the network. We could also group multiple batteries that connect the same two networks, to allow them to discharge evenly (parallel SMES in SS13, for example).

Really all this means is that you have a pass at the start of a power tick to sum power devices up, and a pass at the end to divide demand/supply up between them.

If I mention "supplier" or "load" later on in this doc, I mean "supplying network" and "loading network". We're never working with individual supply and load devices barring the two passes described above. 

When I put diagrams in this doc, `+` refers to a supply, `-` refers to a load, `-|>` refers to a diode (standard electrical symbol) and `X` refers to a battery. Some old diagrams didn't keep a distinction between diode and battery because until I wrote this section I kept them one and the same so keep that in mind. Also yes diodes/batteries are one-directional but in some old diagrams I didn't bother specifying the direction so figure it out on your own.

Batteries and diodes are connected to two networks. To distinguish these I refer to them as "supplying" and "loading". The "supplying" network is the network that the diode supplies power TO. The "loading" network is the network that the diode loads power from.

### Basic model

At a high level, supplies find all loads below them, add them up, and then evenly distribute power across those loads. A naive brute-force approach would be pretty easy to break to have exponential behavior and as such not be desirable. We can do better.

### "Proper" proportional distribution

Pow3r is not meant to simulate real electrical networks where power moves across paths proportional to resistance or anything like that. We're trying to come up with a system that mostly works in a predictable way and is easy to calculate. That means that things are very susceptible to ordering of execution, by design.

This does mean that the grid is susceptible to inconsistency in iteration order when, for example, walking down a tree (which subgrid do we evaluate first). Different behavior by sorting supplies based on tree depth (as described below) is easy to grasp. Different behavior because "the left node is first in the child list" is not. I am not sure what can be done here.

### Cycle handling

This implementation is designed assuming that cycles cannot exist. I'm planning on just having electrical equipment report a "cycle detected" error and shut off if a cycle comes up.

There is no real valid use of cycles in a correct power grid in pow3r anyways since the only logical outcome is that the batteries on the network empty themselves on losses. It's not worth trying to make work and it makes the problem significantly more hard.

### Supply ordering

Because we cannot solve real electrical simulations where electricity takes a path proportional to resistance, we have to decide on a strict ordering in which power is "delivered".

Supplies will be evaluated in order of their tree height, ascending. This means that if you put a generator on a local APC network, the generator will process before the rest of the station grid.

This has two desirable properties:

1. If you put a generator on a local APC network, it will actually take the load off the main station grid, instead of only being able to fill in brown/blackouts.
2. It avoids upwards hierarchy walks as described below. It does not make these impossible, but it does make them basically nonexistent unless you actively go set up weird networks to trigger the behavior.

### Hierarchical power distribution

As stated before, supplies add up demand then distribute their power. The trick is grouping across multiple networks to avoid large tree navigations.

If operating under the assumption that power grids are a tree (not anything fancier), the process is quite easy. We go through the tree bottom-to-top, adding up unmet demand and adding *met* demand whenever a network has a supplier. We make ancestors inherit the unmet demand of their children. Then when we've navigated the whole tree, navigate top-to-bottom breadth-first, distributing the met demand of suppliers downwards evenly.

When the power grid forms a polytree instead, we need a little bit more effort. First of all, the first tree walk is initiated by suppliers, and suppliers are iterated in the previously discussed order. It is done recursively, top-to-bottom. When a network's unmet demand gets inherited by its ancestor(s), a "reservation flag" is set on the network. If, while traversing the polytree downwards from another supplier, we come across a network that has this reservation flag set, we need to navigate the graph upwards. We navigate up the tree of reservation flags and immediately apply the met demand of supplies on the hierarchy, clearing the reservation flag along the way. Then set the reservation flag again to reserve for our own calculations. This probably requires more complex book keeping and a per-connection "power already sent" to keep track of the power that's been "immediately collapsed". Just clearing flags upwards and specifying "power already sent" on connections may be enough here.

This upwards walk is a bit of a sore spot but luckily should not happen unless you actively set up wacky networks to create it. The worst case scenario, I suppose, is setting up two long lines of networks such that they take turns taking over each other's reservation flag and causing exponential tree walking. Maybe have a check to avoid this?

This behavior would only happen on grids like this, which don't happen frequently on the real station:
![](https://i.imgur.com/aOquNMN.png)
*X: battery, -: load, +: supply*

The #2 supply is artificially "weighed down" with extra batteries to increase its tree height, so that it is processed after #1.

These tree traversals can keep current limiting of substations and such into account by simply limiting the amount of unmet demand that can go through a link between two networks.

This still isn't sufficient for full-DAG scenarios like this, however:

![](https://i.imgur.com/sOHe7OY.png)

This case cannot be transparently handled: the previously discussed model would try to solve this by "collapsing" the power hierarchy to immediately calculate the unmet demand of the sub-network. But we can't do that yet because we're still *calculating* the demand of the network in the first place.

First of all, this case is only really complicated when handling current-limited connections. When the path to such a "joiner" network is through a current-unlimited connection then obviously there is no problem since you can just have all the power go through the unlimited connection, and you won't have to evaluate the network the second time you encounter it.
For current-limited connections, of course, it isn't that easy.

![](https://i.imgur.com/vAjGd2J.png)

One idea I had is to evaluate the total current limit of the joiner network, so far. Then we can say "the first connection passed 2 kW we'll pass the remaining the subnet needs". Keep in mind that this would have to evaluate the total demand of the network up until the current limiting diode and then assign the ratio, not just a `min(min_of_current_limits, subnet.demand)`. This is a "collapse the network" but a different kind. We'd be collapsing the network for distribution inside the grid only, not actually walking up to the supply to instantly hand out power. I need to do more concrete thinkwork to figure this out.

Basically uhhhhh if you encounter the network the second time, calculate "what is the max amount of demand that can be filled thanks to current limiting" and then take the *remaining* unmet demand for the network instead of the total. We can basically keep doing this. We *aren't* calculating power distribution here but *distribution ratios*. 

The important distinction is that this grid collapse happens internally during the calculation of a single push. This means that the power grid will be internally consistent at the end and a "some nerd hooked a weighed-down supply into it randomly" and it has to collapse power distribution, it can just collapse it. The logic will be more complex however.

### Distribution priorities

I am currently thinking of having ~~three~~ four passes of power distribution across the power grids, in this order:

1. Supply -> load
2. Battery -> load
3. Supply -> battery
4. Battery -> battery

Batteries can effectively be modelled as pass-throughs (always), supplies (when discharging) and loads (when charging). Ordering distribution like this means that supplies always get maxed out before batteries get used, and batteries do not take power away from machines when recharging.

...Except that's the initial idea. Another idea I had is that EVERYTHING is processed in one pass. This means that batteries will basically always be outputting (e.g. APCs always discharging into their own network) BUT we'll let direct input charge of the battery deduct for the purposes of ramp calculation. 

This way a battery might supply 1 kW (base ramp tolerance) to its supplying network, but it'll GAIN an immediate 1 kW of demand itself, for the parent network to handle. If this 1 kW gets filled we'll avoid increasing the ramp position so the battery won't ramp up. You effectively couldn't tell that this was happening. This is possible because we know that a battery always processes before anything that can feed into it (bottom-up supply ordering). Does make calculating network grouping more complex though since we'll only be able to calculate network groups once the loading batteries of the network have processed their power distribution. It'll make the code less elegant but it shouldn't be a problem.

The only edge case I can immediately see is that this means that weighted-down hierarchy situations (described above) will behave differently. If you have a scenario like this:

![](https://i.imgur.com/3nhQZnv.png)

The order in which the supplies (batteries and plain supplies) are evaluated could be as described. In that case #1 will discharge instead of letting #4 take over. I'd say this edge case isn't worth the added complexity and overhead created by needing 4 power distribution passes.
