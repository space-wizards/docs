# Secbots and Beepsky

| Designers | Implemented | GitHub Links |
|---|---|---|
| PotentiallyTom | :x: No | TBD |

## Overview

Secbots are NPC security officers. They patrol the halls and other public areas looking for criminals. When they see one, they attempt to detain them and hold them for sec to arrive. They can be produced in a similar fashion to cleanbots or medibots. Officer Beepsky is a unqiue secbot. They have improved abilities, more complex behaviour, and a personality to their statements. Officer Beepsky is also the only secbot that spawns at the start of the round.

## Background

Secbots, and Beepsky in particlar have been in SS13 for longer than I've known about it and players and maintainers have both expressed a desire for them to be added. Beyond being a cool feature people have wanted for a while, secbots provide a baseline level of security to the station. It is not uncommon to see rounds start with only a single person in the security team and having NPC security helps mitiage that. 

I consider the criminal records computer to be a good addition to the game, but there's a lack of consensus with some security teams as to what each mark should be used for, and very few reasons to use the paroled or released marks. Having secbots interact with players differently based on their criminal records (such as wanted causing an instant arrest, or paroled making secbots quicker to arrest you) would add some mechanical consequences to using the system.

When griefers, "shitters", or raiders join the game, it usually falls on sec to remove them. In rounds with few, or unrobust security officers, this can be difficult. Beyond just adding a baseline level of competance to the security team, wasting a secbot's time is less rewarding than wasting a player's time. This is unlikely to have a major impact on the number of times it happens, but someone leaving the game when they get arrested will likely leave the game regardless of whether it was a player that got them, or a secbot. 

An often brought up rule is that "Command and Security should not be using contraband". There is no mechanical enforcement for this. Having secbots arrest even command and security with contraband visable (wearing or holding, not including pockets) would provide this. Obviously some leeway should exist for officers and command carrying stuff back to the brig.

## Features to be added

### Navigation

The most discussed part of this is how a secbot should navigate around the station. The details for this, and why this method was chosen are in a [later section](#patrol-routing). As far as a player needs to know, the secbots patrol with the following system:

1. Maps have a set of "Patrol Beacons" under the tiles in major locations. This would include places like the bar, the outside of security, and the corridor containing the vault. Importantly these locations should all be public access. TODO - example. Beacons can be unanchored, moved, and destroyed, but not built. A navigation table contains data for travelling between nodes down to the exact tiles a secbot should traverse.

2. A Secbot is at a beacon. It is currently in the `Patrolling` state. It chooses another beacon at random on the same grid as it, not including it's current or previous location. It starts moving towards the new beacon using the path laid out in the navigation table. 

3. If it gets to the beacon successfully, it will stay in the area for a short duration, then pick a new beacon and begin moving towards it.

3. If it encounters an obstacle on its path (locked firelocks, anomaly rocks, walls, etc) it enters a `Returning` state where it follows the path back to the previous beacon and choose a new node. An "Attempts" score gains +1 for that path.

4. If the number of attempts for a given path it deletes the path in the navigation table and enters an `Explore` state, where it uses a TODO - algorithm to generate a new path which is added to the navigation table if it works. If it spends more than 2 minutes in the `Explore` state, it enters the `Returning` state.

5. If it encounters an obstacle in the `Returning` state, enter 



### Generic Secbots

### Controlling Secbots

### Officer Beepsky

### As a Thief Objective

### Producing More

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