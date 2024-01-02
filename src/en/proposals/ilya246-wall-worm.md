# Wall Worm

| Designers | Implemented | GitHub Links |
|---|---|---|
| Ilya246 | :x: No | TBD |

## Overview

A new midround antagonist that is a worm that travels through walls. Eats people like a dragon and grows new segments depending on how many it ate. Its objective is growing as big as possible.

## Background

Relevant Discord discussion: https://discord.com/channels/310555209753690112/1008709214006427689/1191795809587576922

## Gameplay

### Core gameplay

Initially, the wall worm spawns in any non-transparent wall on the station as a ghost role.
It may only move through walls, airlocks, and full windows, using smooth tile movement.
The worm has no FOV and can see everything regardless of sight blockers.
Worm movement is audible in a low to moderate range. Silent if moving slowly.
Damaging the worm directly or the walls the worm is in damages the segment hit.
Sufficiently damaged segments are disabled.
Damaging a disabled segment leaks damage to neighbouring segments.
If all segments are destroyed, or the head is destroyed, the worm dies.
The head has high health.
It may, through the usage of an ability, temporarily go out of walls to grab people, after which it must go back into a wall.
Being outside of walls rapidly asphyxiates the worm, so it must go back in as soon as it can.
Dragging people inside walls deals damage to them. If the person is dead or dies, they get eaten by the worm.
Eating people heals the worm.

### Abilities

Scream - Scream loudly. Audible in a high range. Doesn't do anything besides scaring people.

Grab - Passive ability. Makes the worm grab the first person the mouth collides with. The worm is slowed while having grabbed someone. Disabling the ability will release the person. May be disabled inside walls.

Charge - Can only be used while in walls. Makes the worm rapidly dash from inside the wall to the target location, possibly arriving at another wall in the way. May grab people while dashing.

### Growth

Eating people lets the worm gain additional body segments.
As a downside, additional segments make the worm's movement slower and louder and give the crew more area to hurt it.
As an upside, they grant it additional health and make Grab deal more damage and incur less slowdown.
The worm may choose to specialise new segments.
Disabled segments do not provide their function.

#### Segment specialisation

Upon gaining a new segment, the worm gets an option to choose an organ to grow in that segment. Said specialisations may include:

Stomach - Lets the worm regain more health from devoured people.

Heart - Makes the worm slightly faster.

Liver - Makes the worm slowly regenerate health.

Acid gland - Makes Grab deal considerably more damage.

Wing - Increases the range of Charge and makes it faster.

Armor - High health. Aborbs damage taken by neighbouring segments.

Brain - Low health. Prevents death by head destruction. May sacrifice its health to slightly repair a disabled head.
