# R-ANGL Tokamak Fusion Reactor

| Designers      | Implemented | GitHub Links |
|----------------|-------------|--------------|
| ArtisticRoomba | :x: No      | nuh uh       |

## Background
Currently, Upstream Atmospherics is lacking in interesting engine design or gas-based mechanics.

The Thermo-Electric Generator (TEG) is a great example of this, suffering from monotony.
While multiple interesting solutions exist to the TEG's problem due to the emergence of atmospherics devices, these solutions often result in an engine that rarely offers any interesting or emergent gameplay post-setup, especially with other departments. The standard gameloop is to pray that someone knows how to set up the engine and just wait until the shift ends - rarely does the chamber need to be refilled and a burn re-lit for more hot gas.

Note that even with the recent changes to the TEG encouraging dual-loop designs and punishing extremely basic single-loop designs, the TEG's core problems still remain.

A large component of the TEG's problem is the lack of interesting gases and the means to synthesize them. Tritium is synthesized as a by-product of burning plasma at specific conditions, leading to a free large heat boost that invalidates any sort of care for efficiency or optimization - the most people are worried about in that sense are making sure they didn't invert their burn chamber ratio.

Gas synthesis gameplay is generally boring. Frezon setups are largely copied from external sources or reconstructed from memory - there is no intuitive way for players to discover frezon synthesis. Additionally, the only two relevant gas reactions (tritium and frezon)

## Proposal
This proposal plans to introduce the R-ANGL Tokamak Fusion Reactor, a machine that gives engineers a relaxed pressure and temperature constraint environment in which the fusing of new gases can take place. Atmos techs have to manage new and interesting constraints associated with maintaining the environment, which happens entirely in the tile space, just like a standard burn chamber.

As an effect, Upstream would be more motivated to add more gases with more interesting/unique synthesis requirements. This would shift the roundflow focus more on the Tokamak and synthesizing gases for the station and the TEG, rather than just setting up the TEG and forgetting about it.

### Inspiration
The fusion reactor concept is largely inspired from SS13 Baystation's R-UST Fusion Reactor, which is an alternative method of generating power for the SEV Torch. The reactor has a magnetic confinement field that must be powered and brought online. Fuel is inserted and a massive laser is fired to start the reaction and keep it going.

The thing that was most attractive about the R-UST was the fact that it was a machine with reactions and operations happening in the tile space. This is much different from the currently available downstream Hypertorus Fusion Reactor (HFR). The HFR is extremely cool, however it is more akin to a black box where gasses go in an out with not much player interaction apart from changing settings.

## Core Mechanics
### Magnetic Confinement
Gas is confined magnetically by a set of extremely powerful electromagnets located in a ring around the chamber as well as in the center.
This forms a donut in the chamber where only gas can reside, preventing it from touching the walls and interacting with them. Gases will flow naturally from unconfined to confined areas, allowing pressure and heat to build beyond the regular pressure limit of most atmospherics devices.

Gases can be extracted from the chamber via any extraction device residing in the confined section of the chamber, and inserted via any non-confined area in the chamber.
This allows any high temperature or pressure reaction to take place in the reactor, with Atmospherics Technicians left with the tasks of maintaining reactor confinement as well as the requirements of the desired reaction.

#### Pipe Pressure Limits
In the future, pipe pressure limits may be added, which make pipes burst when they exceed a high pressure.
There are multiple upsides and downsides when considering how pipe bursting may interact with the Tokamak:
- Atmospheric Technicians will be limited in how fast they can vent the chamber, as any piping that bridges the gap between the containment area needs to be limited to its maximum safe pressure.
  - This puts a cap on how fast engineers can pull from the chamber for both reaction throughput and emergency venting.
- Emergency cooling loops for the Tokamak may overpressure unless designed in a way that alleviates overpressure.

Overall, pipe bursting may add an element of complexity that may be too frustrating - it depends on how interactive and "fair" pipe bursting's implementation is.

### Confinement Operation
As mentioned previously, confinement is generated and maintained by a series of electromagnets.

The current strength of the confinement is known as the _tesla field strength_ and is an all-around quantifiable value for the current health of the reactor's containment field.
Engineers can see this value, with UI elements detailing minimum safe values and how this can increase or decrease depending on the actions that can be taken by the player.

The confinement electromagnets require power and cooling. Their power requirements are proportional to the temperature of the electromagnet, with higher temperatures requiring greater power to maintain the same tesla field strength. This leads to the following:
- Engineers are encouraged to set up cooling for their electromagnets using standard space cooling loops or powered equipment.
- Batteries can be used to help compensate for a magnet whose cooling system has failed, keeping the field strength high before engineers take measures to lower the field strength (whether it be venting off pressure, bleeding off heat for use in the TEG or wasting into space, or decreasing the size of containment).

Higher chamber pressures require a higher tesla field strength in order to contain.
The size of the confinement can also be controlled by engineers, with larger confinements requiring a greater field strength.
This encourages engineers to seek better methods of cooling (whether it be spamming high-wattage thermomachines or taking advantage of the frezon decomposition reaction) in order to sustain high-pressure, high-volume reactors.

All-in-all, this leads to a balancing game where engineers are encouraged to toy with their reactor, enabling faster and hotter reactions.
It's important that the tesla field strength balancing game should be intuitive and follow the player's expectations, with proper feedback given as to what the player can do in order to raise or lower the field strength.

### Upsets & Failure States
The reactor's destructive power is not always tied to the reactor itself, but rather the gas that is currently reacting inside the containment field.
Gases can now deal Delta-Pressure damage, where structures like windows take damage and shatter due to differences in pressure across the sides of the object.
Since the reactor can contain reactions that require extreme pressures in a small volume, this could prove very problematic if the reactor's containment was breached and the gas was allowed to spread throughout the station.

Gas reactions may also have environmental effects, like radiation, which would require engineers to set up proper precautions when synthesizing gases of that nature.

#### Upsets
Upsets are small events that occur that might disrupt or effect the regular operation of the reactor, causing it to deviate temporarily.
These upsets should not be targeted random chance events. Instead, they should disrupt other mechanics that, by interconnected simulation, effect the Tokamak in some way.

For example, an event should not simply turn off power to the electromagnets, causing a drop in tesla field strength. Instead, random or antagonist-caused power outages should affect the power supply to the electromagnets. Note that in this instance, engineers can counter this to some extent by setting up emergency power generation, however the power requirements will likely be more than what can be produced by a single mini PACMAN. Also note that the electromagnets require proper cooling, which will likely take a lot of power!

Upsets can also be beneficial. For example, a cool benefit would be the ion storm temporarily increasing the tesla field strength. Having more events tie into the Tokamak mechanically makes it feel more fun to get it under control, and rewards players for learning the various ways the reactor can be affected, which adds to the depth of the system.

#### Failure States
The Tokamak can suffer from critical failure of its systems, causing a confinement loss and invoking whatever consequences arise from an uncontained exotic gas reaction.

In any critical failure state, the reactor should not fail instantly, with no chance for any engineer to recover the stability of the reactor. Instead, a prolonged sequence of events should occur. This leads to the following:
- **It gives new engineers messing around with the system a final chance to get the reactor back in control.** Accidents happen, and incompetence is a part of SS14! If you royally screw up, well, you had your chance, and it's probably a bit late in the round by now. Whatever happens next is (hopefully) going to be a fun ride and moment of chaos/catastrophe that the crew gets to survive.
- **It makes sabotaging the reactor a huge "playing point" in a round.** Much like the nuclear bomb in the Nuclear Operatives gamemode is a very large playing point, the tokamak should behave the same way. The capture and subsequent sabotage of it is a big point in the round, and the crew would be encouraged to fight to get it under control.

The secondary electromagnets (the ones on the edges) cannot be destroyed barring extremely specific circumstances - they can only take enough damage to trigger a **critical damage** state. In this state, the reactor is on a timer and the containment slowly starts to fail. The entire station is alerted that containment is about to be breached and sets the alert level to yellow.

Restoring containment involves performing a complex repair procedure on the damaged element. This can be anything interactive, but it shouldn't be a simple doafter or construction steps - a UI that has players playing some sort of minigame or fixing some sort of element inside the system should be the repair action.

Multiple pylons can be damaged, decreasing the time before a confinement loss. It's important to note that a force like Nuclear Operatives shouldn't be able to damage all pylons and guarantee a fast containment loss or doomed state cheaply - this type of action would need to cost a significant portion of the team's telecrystal.

A critical failure state can also occur when the containment field is failing due to being overloaded. This will not cause the epic Doomed State, only a confinement loss, which Atmospherics will feel the consequences of.

#### Doomed State
Because all engines need a really cool explosion mechanic at the end of the day.

The Tokamak can enter a Doomed State, where the reactor is critically damaged and is about to explode. This is meant to mark the climax in the reactor's failure sequence. Having a reactor's destruction warm up to an epic moment instills fear in players, similar to the nuke explosion in Nuclear Operatives.

This state is reached automatically during the following:
- The reactor has 30 seconds remaining until confinement fails due to one or multiple damaged secondary electromagnets.
  - A doomed state does NOT trigger if the containment is simply fizzling out due to a confinement loss caused by a tesla field strength decrease. Magnet damage is required to facilitate a doomed state.
- The center electromagnet receives a large amount of instantaneous damage. This is supposed to seldom occur and is more so a way of fulfilling the butterfly principle for absurd moments - for example an immovable rod nailing the center electromagnet dead-on.
  - This shouldn't be able to be caused by regular antagonists or crew outside extremely absurd events like the immovable rod. Anyone attempting to trigger this themselves should have to spend 20 TC on minibombs, on top of getting ashed instantly by the plasma field in the reactor.

When Doomed State triggers, station alert level is set to Delta.
If Doomed State persists and the reactor is not fixed in time, the reactor triggers a station-wide impacting effect at the end of its life. Either the entire station gets EMP'd, a radius the size of Engineering is vaporized, or it creates a point-fusion event and instantly vaporizes any entity that's in a star pattern centered on the Tokamak. This can be anything, but the destruction should fulfill the following requirements:
- It should match the ante that we're building up. Nobody's going to want to feel scared from Delta alert if they know the explosion is just the size of a small burn chamber in a part of the station they don't care about.
- It should leave a decent chunk of the station alive in order for them to survive the aftermath and facilitate post-apocalypse survival Evac gameplay.

## Roundflow and Gameplay
### Startup
In the beginning, the Tokamak will be cold and sleeping silently.
Engineering, if they choose to accept it, can power up the Tokamak by following a set of procedures listed in the UI of the tokamak control computer.

The UI will present a series of conditions that the reactor and its elements must be at in order to start up the containment field.
For example:
- The chamber is a valid structure (square) with pylons placed in all 4 corners of the square. This will usually be already fulfilled as it is likely that the Tokamak will have its elements pre-mapped to enable Engineers to get started making gases.
- Primary and secondary electromagnets need to be connected to power and need to be cooled to below a certain temperature.
- A priming sequence needs to be completed on each pylon.
  - This slows down startup gameplay, increasing the chances that every engineer is "in the know" of the engine being brought online.
  - This should be an interactive UI minigame of some sort, and should line up a little well with the repairing process that would be done if the pylon enters a critical damage state, so players know what to expect.

Afterward, the reactor starts up and the containment field is active.

### Operation
During operation, engineers will have to monitor and ensure that the Tokamak can contain whatever reaction is occuring inside the reactor.
The operation of the Tokamak is a balancing act, and engineers will naturally want to see how far they can push their reactor, and see what type of interesting reactions they can perform.

It should be noted that the products of gas synthesis should benefit the station in its entirety, and not just Atmospherics.
Gases should see more use, either being included in crafting recipes for better productivity, usage in cooling critical AI servers, usage in medicine, or otherwise. 

### Shutdown
Safe shutdown is accomplished by depressurizing the confinement area to the point where any gas that was in the field would not cause any harm if allowed to contact the edges of the enclosure. Any attempt to shut down the reactor while the confinement is still holding gas that is considered dangerous (ex. ongoing reaction or gas pressure above a setpoint) would trigger a critical state warning and alert the station.