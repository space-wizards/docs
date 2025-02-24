# Secbots and Beepsky

| Designers | Implemented | GitHub Links |
|---|---|---|
| PotentiallyTom | :x: No | TBD |

## Overview

Secbots are NPC security officers. They patrol the halls and other public areas looking for criminals. When they see one, they attempt to detain them and hold them for sec to arrive. They can be produced in a similar fashion to cleanbots or medibots. Officer Beepsky is a unqiue secbot. They have improved abilities, a personality to their statements, and serve as a potential target for thieves and syndicate agents. Officer Beepsky is also the only secbot that spawns at the start of the round.

## Background

Secbots, and Beepsky in particlar have been in SS13 for longer than I've known about it and players and maintainers have both expressed a desire for them to be added. Beyond being a cool feature people have wanted for a while, secbots provide a baseline level of security to the station. It is rare but not unheard of to see rounds start with only a single person in the security team and having NPC security helps mitiage that. 

I consider the criminal records computer to be a good addition to the game, but there's a lack of consensus with some security teams as to what each mark should be used for, and very few reasons to use the paroled or released marks. Having secbots interact with players differently based on their criminal records (such as wanted causing an instant arrest, or parolled making secbots quicker to arrest you) would add some mechanical consequences to using the system.

When griefers, "shitters", or raiders join the game, it usually falls on sec to remove them. In rounds with few, or unrobust security officers, this can be difficult. Beyond just adding a baseline level of competance to the security team, wasting a secbot's time is less rewarding than wasting a player's time. This is unlikely to have a major impact on the number of times it happens, but someone leaving the game when they get arrested will likely leave the game regardless of whether it was a player that got them, or a secbot. 

An often brought up rule is that "Command and Security should not be using contraband". There is no mechanical enforcement for this. Having secbots arrest even command and security with contraband visable (wearing or holding, not including pockets) would provide this. Obviously some leeway should exist for officers and command carrying stuff back to the brig.

## Features to be added

### Secbot AI

The secbot uses a 4-state-machine to control it's behaviour. The states are `Patrolling`, `Chasing`, `Exploring`, and `Reorienting`. Secbots will move slightly slower than a player (~90%). They will have basic department access - HoP access without the actual HoP room.

![The secbot state machine (Patent Pending)]()


#### Patrolling

The most discussed part of this is how a secbot should navigate around the station. The details for this, and why this method was chosen are in a [later section](#patrol-routing). As far as a player needs to know, the secbots patrol with the following system:

Maps have a set of "Patrol Beacons" under the tiles in major locations. This would include places like the bar, the outside of security, and the corridor containing the vault. Importantly these locations should all be public access. TODO - example. Beacons can be unanchored, moved, and destroyed. 

A navigation table is maintained for each grid with a patrol beacon on it. The table contains data for travelling between nodes down to the exact tiles a secbot should traverse. Because of the potential for O(n^2) growth of this table with regards to the number of beacons, they should not be constructable. 

A secbot in the `Patrolling` state will choose a random beacon and follow the tile-by-tile path laid out in the navigation table. If it arrives at its destination, it will linger in the area for a short time, before repeating the process - picking a beacon, pathing to it, and lingering in the area. If the path becomes blocked, such as a by a closed firelock or a broken tile, a weak attempt is made to get around the obstacle by pathfinding to the first unblocked tile. This should be effective enough to navigate a pillar in the middle of the corridor, but should not be causing the secbot to path down a different corridor. If this attempt fails, the secbots follows the path backwards to return to the closest beacon, marks that route as `Attempted`, and continues patrolling to a different beacon. If a route is sucessfully navigated, all `Attempted` marks on the route are removed. If a route has been `Attempted` and failed 3 times, the route is deleted from the routing table. If the secbot's return path is blocked, it enters the `Reorienting` state.

If a secbot picks a beacon without a value in the routing table, it enters the `Exploring` state.

At any point if a secbot sees someone that should be arrested, it enters the `Chasing` state.

#### Reorienting

When in the `Reorienting` state, a secbot attempts to path towards the nearest beacon. If that fails, it attempts to path towards the nearest beacon that it hasn't already attempted to path to. This repeats until it has attempted to path to every beacon in the navigation table, at which point it will pick random beacons. If it reaches a beacon, it will enter the `Patrolling` state.

The path to the nearest beacon should not be computed in a single tick - capping the search to some heuristically "best" point within X tiles, navigating to that tile, and repeating would prevent a situation in which a massive pathfinding call causes a lag spike. It also means storing less memory.

Failing to reach a beacon could be defined in a few ways and could be tweaked through testing. A good starting point would be to take the current difference in x and y to the beacon, and saying the pathfinding attempt has failed if we have traversed twice as many tiles as the sum of the two.

At any point if a secbot sees someone that should be arrested, it enters the `Chasing` state. 

#### Exploring

The `Exploring` state is entered when the secbot attempts to travel between two beacons that don't have an entry in the navigation table. This can occur if a beacon is moved or destroyed, or if an existing route has been deleted through 3 failed attempts at navigating it. The 

At any point if a secbot sees someone that should be arrested, it enters the `Chasing` state. 

#### Chasing

The `Chasing` state will inevitably need tweaking after implementation [1]: if a player is directly interacting with a secbot, they're probably being chased. When a chase starts, the secbot will pause in place for a short duration (somewhere around 0.5-1.5 seconds) to "charge up" and will say some statement: "Stop criminal scum", "Freeze", etc to give the target an oppertunity to react. After this it will gain a significant speed boost for a short duration (~130% of base player speed for ~5 seconds) and move towards the target. If it gets within melee range it will swing a stun baton at the target up to 3 times. 

If the target is stunned, the secbot will apply handcuffs to them, make an announcement to the sec radio "Secbot (1234) has detained a suspect near {nearest beacon}", and pull the target without moving [2]. If a target escapes the handcuffs, the secbot will attempt to arrest them again, but it will not react to the target attempting to take the handcuffs off until they are off. 

[1] Every number here is a rough guideline and will probably need changing.

[2] There will have to be a special case to the "handcuffs prevent a change of puller" rule.

During the chase, if the secbot does not stun the target before the speed boost ends, it will repeat the process - charging up, then rapidly approaching the target to stun them, repeating this until it succeeds or the chase is lost. If the secbot looses sight of the target, it will move towards their last known point. If it reaches that point without seeing the target, it considers the chase lost, and moves to to the `Reorienting` state.

### When to Arrest?

There's a lot of space to make secbots "smart" with making arrests, and I would welcome additions once the basics are implemented. For the basic implementation, there will be 2 cases where a secbot will attempt to make an arrest.

1. Someone who is marked as Wanted

2. Someone who is seen carrying Syndicate Contraband. 

Obviously someone marked as wanted should be a target. The second case helps reinforce the idea that "Syndicate contraband is *very* illegal", which doesn't always come across in-game. In this case "seen carrying" means anything that can be seen on the strip menu; things that are worn, and held in hands, but not including things that are in pockets.

For case 2, there are 2 exceptions:

1. If the target has armory accesss on a visable ID, they will never be targeted for contraband.

2. If the target has security access on a visable ID, they are given 3 chances; every time the secbot sees them with syndicate contraband they get a strike, every time they are seen without, they lose a strike. Strikes can only be gain or lost every 2 minutes. If someone gets a third strike, an arrest attempt is made. 

Someone needs to be able to reliably move contraband and having the HoS, Warden, and Captain able to do so is the simplest solution. The HoS or Warden can be expected to handle every piece of contraband that sec encounters. Armory access is arguably the most important single access on the station; someone trusted with that can be trusted not to misuse contraband. 

Secoffs need some leeway for handing stuff in; The HoS and Captain can't be expected to respond to every contraband call. Ideally we want officers to be able to transport large contraband, and potentially use it in emergency situations. This system gives at least 4 minutes of open usage, more than enough time to head to the armory, or deal with a life-or-death emergency. It will still arrest anyone abusing contraband, such as openly walking around with an esword "cos it looks cool".

### Producing More

Secbots can be constructed with a Security Helmet, Proximity Sensor, Cyborg arm, Stun Baton, and 2 LV wire. They require cooperation between security and robotics to produce. TODO - justify

### Officer Beepsky

Officer Beepsky is a unique secbot that spawns at roundstart. He has better numbers, different lines, and a unique "Beepsky personality chip" that serves as a thief objective, and a way to rebuild him if he is destroyed. 

For stats, Beepsky will have improved base movement speed (~95% of player movement speed), a shorter charge up time (~25% less than regular secbots), a longer speed boost (~25% longer than regular secbots), and be more resistant to damage. Ideally, Beepsky should be effective enough to reliably arrest someone unprepared, but be fairly easy to play around for someone planning to interact with them, and a non-issue for anyone with serious loud gear (DAGD or nukies). 

Beepsky will have different voicelines to regular secbots. The personality will be more aggressive than the regular "matter-of-fact" secbots. 

The thing making Officer Beepsky unique is a "Beepsky Personality Chip". It can be removed from Officer Beepsky by destroying them, or by unlocking them with Security access, and removing the chip. Removing the chip will turn them into a regular secbot. Inserting the chip into a secbot will turn that secbot into Officer Beepsky. This chip should not be obtainable outside of the roundstart Officer Beepsky. This makes it possible to "repair" them if they are destroyed. Stealing this chip will be a possible antagonist objective, encouraging players to interact with Beepsky, and make deliberate plans to subvert them. 

## Game Design Rationale

## Roundflow & Player interaction

## Administrative & Server Rule Impact (if applicable)

# Technical Considerations

## Patrol Routing

The obvious blocker to implementing this is the routing. Specifically how does it move around the station when patrolling, and what needs to be added from a code and mapping standpoint to faciliate that? **Station beacons** are the obvious choice for points of interest, but patrolling secbots should be sticking to public areas and corridors, which typically don't have any. 

TODO - image demos

So how do we define the areas that we want the secbots to patrol. There seem to be 3 main possibilites (and since this seems to be the most debated part of the proposal, would appreciate more):

1. Defined by a player in-game.

2. Defined by a mapper during the map creation process.

3. Defined automatically, using stuff existing in the map.