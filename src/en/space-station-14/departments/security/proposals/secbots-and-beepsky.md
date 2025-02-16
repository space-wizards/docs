# Secbots and Beepsky

| Designers | Implemented | GitHub Links |
|---|---|---|
| PotentiallyTom | :x: No | TBD |

## Overview

Secbots are NPC security officers. They patrol the halls and other public areas looking for criminals. When they see one, they attempt to detain them and hold them for sec to arrive. Officer Beepsky is a unqiue Secbot. They have improved abilities, more complex behaviour, and a personality to their statements. 

## Background

Secbots, and Beepsky in particlar have been in SS13 for longer than I've known about it and players and maintainers have both expressed a desire for them to be added. Beyond being a cool feature people have wanted for a while

## Features to be added

### Generic Secbots

### Officer Beepsky

## Game Design Rationale

## Roundflow & Player interaction

## Administrative & Server Rule Impact (if applicable)

# Technical Considerations

## Patrol Route

The obvious blocker to implementing this is the routing. Specifically how does it move around the station when patrolling, and what needs to be added from a code and mapping standpoint to faciliate that? **Station beacons** are the obvious choice for points of interest, but patrolling secbots should be sticking to public areas and corridors, which typically don't have any. 

TODO - image demos

So how do we define the areas that we want the secbots to patrol. There seem to be 3 main possibilites (and since this seems to be the most debated part of the proposal, would appreciate more):

1. Defined by a player in-game.

2. Defined by a mapper during the map creation process.

3. Defined automatically, using stuff existing in the map.