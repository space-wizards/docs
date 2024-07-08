# The Holodeck or the Holography Laboratory

| Designers | Implemented | GitHub Links |
|---|---|---|
| CptJeanLuc | :x: No | TBD |

## Overview

Imagine a room on a station or shuttle which, upon interacting with a computer console you can have instantly remapped into one of many pre-programmed, or in-round assembled structures.

## Background

Currently we have various systems which generate dungeons, place entities into a paused map with the ability to return them, and replace station and planet tiles at whim.
These are the core functionalities required for a holodeck.

## Gafaw! but how!?

The base principle, is that special holodeck walls and floor tiles can be placed and linked to from a holodeck computer console.
The holodeck should be required to be enclosed by special walls, airlocks, and floor tiles. Should the enclosure break it should cease functioning.
The computer console can select from a list of (a) premapped dungeon-like layouts, or (b) saved layouts that were constructed in round on the holodeck.
When the console selects a premapped layout, it builds the holodeck room, walls, tiles, and entities within. It also marks all of these with a relevant HoloDeckWallComponent, HoloDeckFloorComponent, or HoloDeckEntityComponent.
When the computer console is set to an empty state, the holodeck room should be returned to the state it was initially, comprised of the initial special walls and floors.
When walls/tiles/entities are removed from the holodeck, they should be moved and placed on a paused map, or easier retrieval, and continuity.
After the first time a premapped layout is selected, it should remain persistent via this method of moving the relevant entities to a paused map and back.
If for any reason the holodeck is rendered non-functional, either by power loss, selecting an empty state on the console, or breaking the enclosure, the holodeck should return to the initial state.
Entities with the HoloDeckEntityComponent should cease existing if they are removed from on top of a tile with an active HoloDeckFloorComponent. 

The console should not function, thereby preventing remapping, while a player is on top of a tile with a HoloDeckFloorComponent, active or not.

Preventing damage to players while on top of a tile with an active HoloDeckFloorComponent, unless the console is emagged, would be quite funny. Thats a stretch goal though.

Somehow allowing players to ask for items in local chat and have them spawn in the holodeck, marked with the HoloDeckEntityComponent. This is a stretch goal.

Either prevent construction within the holodeck, or make constructions made with any components having the HoloDeckEntityComponent also be marked with that component.

How to make it non-euclidean is left as an exercise for the reader. (joke)

## The rest?

This is the beginning of the bike shedding.
