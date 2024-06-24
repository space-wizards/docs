# PAI Expansion Slots

| Designers | Implemented | GitHub Links |
|---|---|---|
| deltanedas | :warning: wip | TBD |

## Overview

This proposal adds an expansion slot to pAIs.
Certain computer boards can be inserted as expansions which let the pAI (but not anyone else) interact with the world.
Once a pai has an expansion installed **it cannot be removed** so you cannot hotswap boards to let a single pAI do everything.

## Background

Right now pAIs don't have much to do, especially if they have no midi library built up.

With this pais can do more interesting things like:
- Detective's pai watching over cams
- Scientist's pai unlocking techs on the go
- Captain's pai making announcements about who is valid

However since the pAI on its own is not special the user has to go and find a board to use, creating RP scenarios.

This creates more depth to a glorified jukebox, and owners can now choose an expansion wisely.

## Implementation

PAIs get a maintenance panel which will allow inserting an expansion board.

A PaiExpansionComponent has a comp registry of things to add to the pAI once installed.

This would also allow implementing things like a protolathe pai that you insert materials into then ask to make things, or an id console pai that copies accesses itself. It would "just" be itemslots and the component but without ActivatableUI.
