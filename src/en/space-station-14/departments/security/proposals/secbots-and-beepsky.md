# Secbots and Beepsky

| Designers | Implemented | GitHub Links |
|---|---|---|
| PotentiallyTom | :x: No | TBD |

## Overview

Secbots are NPC security officers. They patrol the halls and other public areas looking for criminals. When they see one, they attempt to detain them and hold them for sec to arrive. They can be produced in a similar fashion to cleanbots or medibots. Officer Beepsky is a unique secbot. They have improved abilities, a personality to their statements, and serve as a potential target for thieves and syndicate agents. Officer Beepsky is also the only secbot that spawns at the start of the round.

## Background

Secbots, and Beepsky in particular have been in SS13 for longer than I've known about it and players and maintainers have both expressed a desire for them to be added. Beyond being a cool feature people have wanted for a while, secbots provide a baseline level of security to the station. It is rare but not unheard of to see rounds start with only a single person in the security team: having NPC security helps mitigate that. 

I consider the criminal records computer to be a good addition to the game, but there's a lack of consensus with some security teams as to what each mark should be used for, and very few reasons to use the paroled or released marks. Having secbots interact with players differently based on their criminal records (such as wanted causing an instant arrest, or paroled making secbots quicker to arrest you) would add some mechanical consequences to using the system.

When griefers, "shitters", or raiders join the game, it usually falls on sec to remove them. In rounds with few, or unrobust security officers, this can be difficult. Beyond just adding a baseline level of competence to the security team, wasting a secbot's time is less rewarding than wasting a player's time. This is unlikely to have a major impact on the number of times it happens, but someone leaving the game when they get arrested will likely leave the game regardless of whether it was a player that got them, or a secbot. 

An often brought up rule is that "Command and Security should not be using contraband". There is no mechanical enforcement for this. Having secbots arrest even command and security with contraband visible (wearing or holding, not including pockets) would provide this. Obviously some leeway should exist for officers carrying stuff back to the brig.

## Features to be added

### Secbot AI

The secbot uses a 4-state-machine to control it's behaviour. The states are `Patrolling`, `Chasing`, `Exploring`, and `Reorienting`. Secbots will move slightly slower than a player (~90%). They will have basic department access (HoP access without the actual HoP room). In my exeperience state machines are good for NPC AI, and are easy to extend with states for more complex behaviour in the future.

![The secbot state machine (Patent Pending)](..\..\..\..\assets\images\proposals\secbots\SecbotNavState.png)

The most discussed part of this is how a secbot should navigate around the station. The details for this, and why this method was chosen are in a [later section](#patrol-routing). As far as a player needs to know, the secbots patrol with the following system:

Maps have a set of "Patrol Beacons" under the tiles to encourage patrolling between major locations. This would include places like the bar, the outside of security, and the corridor containing the vault. Importantly these locations should all be public access. Beacons can be unanchored, moved, and destroyed. 

![Possible beacon layout for Meta Station](..\..\..\..\assets\images\proposals\secbots\Meta.png)

A navigation table is maintained for each grid with a patrol beacon on it. The table contains data for travelling between nodes down to the exact tiles a secbot should traverse. Because of the potential for O(n^2) growth of this table with regards to the number of beacons, they should not be constructable. 

#### Patrolling

A secbot in the `Patrolling` state will choose a random beacon and follow the tile-by-tile path laid out in the navigation table. If it arrives at its destination, it will linger in the area for a short time, before repeating the process - picking a beacon, pathing to it, and lingering in the area. If the path becomes blocked, such as a by a closed firelock or a broken tile, a weak attempt is made to get around the obstacle by pathfinding to the first unblocked tile. This should be effective enough to navigate a pillar in the middle of the corridor, but should not path down a different corridor. If this attempt fails, the secbots follows the path backwards to return to the closest beacon, marks that route as `Attempted`, and continues patrolling to a different beacon. If a route is successfully navigated, all `Attempted` marks on the route are removed. If a route has been `Attempted` and failed 3 times, the route is deleted from the navigation table. If the secbot's return path is blocked, it enters the `Reorienting` state.

If a secbot picks a beacon without a path from its current beacon in the navigation table, it enters the `Exploring` state.

At any point if a secbot sees someone that should be arrested, it enters the `Chasing` state.

#### Reorienting

When in the `Reorienting` state, a secbot attempts to path towards the nearest beacon. If that fails, it attempts to path towards the nearest beacon that it hasn't already attempted to path to. This repeats until it has attempted to path to every beacon in the navigation table, at which point it will pick random beacons. If it reaches a beacon, it will enter the `Patrolling` state.

The path to the nearest beacon should not be computed in a single tick - capping the search to some heuristically best point within X tiles, navigating to that tile, and repeating would prevent a situation in which a massive pathfinding call causes a lag spike. It also means adding an upper bound to memory usage.

Failing to reach a beacon could be defined in a few ways and could be tweaked through testing. A good starting point would be to take the current difference in x and y to the beacon, and saying the pathfinding attempt has failed if we have traversed twice as many tiles as the sum of the two.

At any point if a secbot sees someone that should be arrested, it enters the `Chasing` state. 

#### Exploring

The `Exploring` state is entered when the secbot attempts to travel between two beacons that don't have an entry in the navigation table. This can occur if a beacon is moved or destroyed, or if an existing route has been deleted through 3 failed attempts at navigating it. The secbot attempts to find a path from the first beacon to the second. If it succeeds, the generated path is added to the navigation table and the secbot is put into the `Patrolling` state. If a path already exists (because another secbot has already added one), the 2 paths are compared, and the shorter of the two is used. If exploring fails, the path is disregarded, and the secbot is put into the `Reorienting` state. 

Like with the `Reorienting` state, the entire path should not be computed in one tick. Some heuristically best point within X tiles is picked, and pathed towards, with a new point being picked once we get there. Failure is defined with the same process as `Reorienting`: taking the current differences in x and y, and failing if we traverse more than double the sum.

At any point if a secbot sees someone that should be arrested, it enters the `Chasing` state. 

#### Chasing

The `Chasing` state will inevitably need tweaking after implementation [1]: if a player is directly interacting with a secbot, they're probably being chased. When a chase starts, the secbot will pause in place for a short duration (somewhere around 0.5-1.5 seconds) to "charge up" and will say some statement: "Stop criminal scum", "Freeze", etc to give the target an opportunity to start running. After this it will gain a significant speed boost for a short duration (~130% of base player speed for ~5 seconds) and move towards the target. If it gets within melee range it will swing a stun baton at the target up to 3 times. 

If the target is stunned, the secbot will apply handcuffs to them, make an announcement to the sec radio "Secbot (1234) has detained a suspect near {nearest station beacon}", and pull the target without moving [2]. If a target escapes the handcuffs, the secbot will attempt to arrest them again, but it will not react to the target attempting to take the handcuffs off until they are off. 

[1] Every number here is a rough guideline and will probably need changing.

[2] There will have to be a special case to the "handcuffs prevent a change of puller" rule.

During the chase, if the secbot does not stun the target before the speed boost ends, it will repeat the process - charging up, then rapidly approaching the target to stun them, repeating this until it succeeds or the chase is lost. If the secbot looses sight of the target, it will move towards their last known point. If it reaches that point without seeing the target, it considers the chase lost, and moves to to the `Reorienting` state.

### When to Arrest?

There's a lot of space to make secbots "smart" with making arrests, and I would welcome additions once the basics are implemented. For the basic implementation, there will be 2 cases where a secbot will attempt to make an arrest.

1. Someone who is marked as Wanted

2. Someone who is seen carrying Syndicate Contraband. 

Obviously someone marked as wanted should be a target. The second case helps reinforce the idea that Syndicate contraband is *very* illegal, which doesn't always come across in-game. In this case "seen carrying" means anything that can be seen on the strip menu; things that are worn, and held in hands, but not including things that are in pockets.

Case 1 has no exceptions, For case 2, there are 2 exceptions:

1. If the target has armory access on a visible ID, they will never be targeted for contraband.

2. If the target has security access on a visible ID, they are given 3 chances; every time the secbot sees them with syndicate contraband they get a strike, every time they are seen without, they lose a strike. Strikes can only be gain or lost every 2 minutes. If someone gets a third strike, an arrest attempt is made. 

Someone needs to be able to reliably move contraband and having the HoS, Warden, and Captain able to do so is the simplest solution. The HoS or Warden can be expected to handle every piece of contraband that sec encounters. Armory access is arguably the most important single access on the station; someone trusted with that can be trusted not to misuse contraband. 

Secoffs need some leeway for handing stuff in; The HoS and Captain can't be expected to respond to every contraband call. Ideally we want officers to be able to transport large contraband, and potentially use it in emergency situations. This system gives at least 4 minutes of open usage, more than enough time to head to the armory, or deal with a life-or-death emergency. It will still arrest anyone abusing contraband, such as openly walking around with an esword "cos it looks cool". The strikes are shared between secbots.

Station contraband has deliberately not been included here: by the rules there are situations when someone can legally carry major and minor contraband. Allowing for this would mean implementing some form of permit system, which is beyond the scope of this doc.

### Producing More

Secbots can be constructed with a Security Helmet, Proximity Sensor, Cyborg arm, Stun Baton, and 2 LV wire. They require cooperation between security and robotics to produce. Having a roboticist make 30 secbots is a funny gimmick for the first few times, but would make any antags in the round miserable. With these materials, you need someone with armory access to mass-produce batons and helmets and you need someone in science for the sensors and arms. Mass-producing secbots therefore becomes a logistical issue - if a warden is handing a roboticist 30 batons, it's likely that a few of them will end up in the hands of an antagonist. Making a handful of secbots, or [repairing Beepksy](#officer-beepsky) will not be as big a logistical challenge and should be more viable.

### Officer Beepsky

Officer Beepsky is a unique secbot that spawns at roundstart. They have better numbers, different lines, and a unique "Beepsky personality chip" that serves as a steal objective, and a way to rebuild them if they are destroyed. 

For stats, Beepsky will have improved base movement speed (~95% of player movement speed), a shorter charge up time (~25% less than regular secbots), a longer speed boost (~25% longer than regular secbots), and be more resistant to damage. Ideally, Beepsky should be effective enough to reliably arrest someone unprepared, but be fairly easy to play around for someone planning to interact with them, and a non-issue for anyone with serious loud gear (DAGD or nukies). 

Beepsky will have different voicelines to regular secbots. The personality will be more aggressive than the regular "matter-of-fact" secbots. 

The thing making Officer Beepsky unique is a "Beepsky Personality Chip". It can be removed from Officer Beepsky by destroying them, or by unlocking them with Security access, and removing the chip. Removing the chip will turn them into a regular secbot. Inserting the chip into a secbot will turn that secbot into Officer Beepsky. This chip should not be obtainable outside of the roundstart Officer Beepsky. This makes it possible to "repair" them if they are destroyed. Stealing this chip will be a possible antagonist objective, encouraging players to interact with Beepsky, and make deliberate plans to subvert them. 

## Game Design Rationale

With regards to the core design principles, this mostly comes down to being a new system for players to interact with. It is a tool for security, but can also be a tool for antags if subverted. A ninja setting everyone to wanted is now a significant issue rather than being a minor annoyance for the warden, or a smart thief could use it to incapacitate someone by planting contraband on them. It also leans into being "Seriously Silly" - an antagonist having to quickly adapt a plan because they ran into a secbot, or an officer suddenly getting attacked because someone set them to wanted would make for good stories.

There is an argument to be made that having secbots would reduce the amount of chaos in the server by adding a baseline level of order to the station. Effort should be made when balancing to ensure that secbots aren't the be-all and end-all of security. 

For antagonists like syndicate agents, secbots would encourage teamwork. Secbots can only detain one person at a time, making it easy to destroy one by having one person get stunned while the other works to destroy it. For security it would encourage listening to the radio, since once somebody is detained, an officer is needed to actually bring the detainee to security for processing.

## Roundflow & Player interaction

Beepsky would spawn at the start of every round, generic secbots would be constructable. The majority of direct interactions would be people playing around the existence of Beepsky, getting chased/arrested by Beepsky, and security dealing with the people arrested by Beepsky. Secbots should not be making the majority of arrests except in rare specific rounds where people are mass-producing them. As mentioned, Beepsky should be effective enough to reliably arrest someone unprepared, but be fairly easy to play around for someone planning to interact with them, and a non-issue for anyone with serious loud gear (DAGD or nukies). Secbots would be weaker than this and serve more to put pressure on antagonists rather than reliably arrest them. This can be balanced by tweaking numbers for secbots and Beepsky.

## Administrative & Server Rule Impact (if applicable)

The headline here is mechanical enforcement of the "Command / Sec shouldn't be using contraband" rule. It also would help add a base level of robustness to security teams for dealing with griefers/raiders. Outside of that there is no major administrative or server rule impact.

# Technical Considerations

## Patrol Routing

The obvious blocker to implementing this is the routing. Specifically how does it move around the station when patrolling, and what needs to be added from a code and mapping standpoint to facilitate that? **Station beacons** are the obvious choice for points of interest, but patrolling secbots should be sticking to public areas and corridors, which typically don't have any. 

![The in-game map of Bagel station, with the areas we want secbots to patrol highlighted, Note that there typically aren't beacons in these areas.](..\..\..\..\assets\images\proposals\secbots\Bagel.png)

So how do we define the areas that we want the secbots to patrol? There seem to be 3 main possibilities:

1. Defined by a player in-game.

2. Defined by a mapper during the map creation process.

3. Defined automatically, using stuff existing on the map.

We can also store our areas in 2 ways:

1. Graph based (Define individual tiles as interesting, then move between those interesting tiles)

2. Area based (Define a contiguous area we want the secbots to be, then have the secbot move between random points, only stepping on those tiles).

This proposal uses a Mapper-defined, Graph-based system. I believe this has the best payoff of out-of-game factors (difficulty to implement and extend, space and time complexity, mapper overhead), and in-game factors (possibility for player interaction, feedback for players, general intuition for the system). 

The main argument against mapper-defined systems is maptainer overhead - mappers would be expected to place beacons in specific locations to allow secbots to move between them. The 2 alternatives are using something already on the maps to define it, or having it be entirely defined by players in-game. Looking at the first option, you would need a "thing" that only appears in these public areas, or appears everywhere except these public areas. Existing station beacons are the obvious choice, however have 2 main flaws. 1: any system exclusively using beacons wouldn't distinguish between maints and corridors, 2: it requires mappers to place station beacons in such a way to allow for secbot movement, which would be more effort than adding a handful of beacons. The same problems apply for anything else used to define it such as physical station maps or air alarms, except now you are coupling these things to the navigation system. 

A player controlled system would most easily take the form of a console in which someone (probably the HoS or Warden) can mark points or rooms the secbots should patrol through. I don't think having a player-controlled system is a bad idea; my main issue is that it makes secbots another command toy like the digi-board, and would make secbots too powerful too easily. With the current system, a clever antagonist could move the beacons to make secbots not patrol down a specific corridor, a player-controlled system doesn't allow for that. Having secbots patrol throughout the station also make them apply a more general pressure rather than a tool to completely lock down a specific area. A set of navigation beacons and paths between them could also be useful for other systems in the future, but a player-controlled system doesn't allow for that.

For graph based vs area based, either system could work, but a graph based system has better gameplay interactions, and fits the role of "Patrolling" better. A graph based system also has a much simpler dynamic update system (`Explore`). A graph based system has a handful of "key points" that can be interacted with to interact with the system; someone who wants to modify a path just needs to modify a beacon. With an area based system, the locations are more spread out, and invisible to the player. 

## The Navigation Table

The navigation table is used to tell a secbot how to get from a given beacon to another beacon via a list of tile-by-tile directions. It will be a part of the map file, and will be able to update itself through the in-game actions of players. Since a lot of routes between beacons will take it via another beacon, we have a chance to optimise memory usage. Take 3 beacons in a line, in a 1 block wide corridor.

```
A -- B -- C
```
We can define the path from A to C as being the path from A to B, and then B to C. By storing this in the table we half the amount of path data stored (since the A to C path is twice as long as the other two). With optimal placement of beacons, **this navigation table becomes a planar graph, which has a linear max on the number of edges**. We still have to either store the `A -- B -- C` path, or do a smaller pathfinding algorithm over the navigation table to find out that the path `A -- B -- C`. Since it will be the longer paths that are compressed this way, this should have a significant impact on memory usage. Of course this only works when beacons are placed specifically to allow for this; in game it would be possible for a player to make a layout of beacons where every beacon has an  extremely long, explicit path to every other beacon. We can optimise the amount of memory used for a path by packing multiple directions into single bytes. Specifically we can go to anywhere in the following pattern with half a byte of data (4 bits for 16 points). 

```
X X X
 XXX
XX@XX
 XXX
X X X
```

Taking the largest map (Fland) to be about 100x150 tiles. Placing 16 beacons in a circle of diameter 150 and generating a path between each gives a sum of ~22,000 path tiles. We can encode 2 tiles of a given direction per byte. That's ~10KB of data stored for a scenario in which someone is deliberately trying to maximise the amount of data stored. Even if they were to make some maze that increased the number of tiles traversed, the `Explore` state will not store paths double the length of the best-case scenario, so we have a worst-case scenario of ~20KB. In reality we need fewer than 16 beacons, will have shorter paths, and can take advantage of our the above-mentioned linear maximum for edges. Again going to Fland, here's an example of a beacon layout, and the expected edges.

![A possible layout of navigation beacons for Fland, note that 13 beacons and 18 edges cover the majority of the public areas.](..\..\..\..\assets\images\proposals\secbots\Fland_smaller.png)

When updating the navigation table with the `Explore` state, some system will have to be put in place to allow for these A-to-B-to-C paths to be generated. The simplest solution is probably to maintain a stack of visited beacons when trying to go between 2 beacons while exploring.

With the suggested system, it would be possible to precompute the navigation table as part of the mapping process. Some `generateNavTable <gridID>` command would be used as part of the mapping process, similar to how pipe networks are colored, or atmos is generated. It would be possible to give a warning if 2 paths overlap, as that suggests a more efficient layout of beacons could be used.

## Pathfinding

While pathfinding in `Explore`, we want the secbot to stay in public hallways, avoiding maints and departments if possible. The simplest way of doing this would be to block secbots from exploring through any access locked doors. This restriction will be removed while `Reorienting`. A smarter system could be implemented in the future, perhaps encouraging secbots to path over tiled floors, or lit up areas.