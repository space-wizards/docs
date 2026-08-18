# The Chosen

| Designers | Implemented | GitHub Links |
|---|---|---|
| Velken | :x: | TBD |

## Overview
The chosen are a late-round antag that gets activated when a Throngler appears, be it by random event or Cargo lottery. Once the Throngler spawns, it will teleport to a random location on the station.
A player may become a Chosen (also referenced as Worthy) by enabling the antag in character options. Except for roles that prevent being antag, or if they are already another antag, ALL Worthy gain the ability to wield the Throngler, the rest of players must destroy it.
The objective for the Worthy is to either be the last remaining Worthy alive or break the cycle and destroy the Throngler.

## Goals
- The chosen is a shift-ender role, should cargo get enough funds to get one from gambling or the shift be late enough for the event to spawn one.
- Mechanically enforce Throngler, to reduce admin workload.
- Provide memorable moments where the crew needs to make moral choices.
 
## Implementation details
The Throngler from the lottery will be changed to a version that requires being Worthy to wield it (as in, hold and being able to attack with it). Those that are Unworthy cannot attack with the Throngler (attempting so gives a popup saying you are Unworthy).
Once the Throngler is spawned (event, lottery or admin), an announcement is made and everyone gets the objective to destroy it and it gets teleported to a random location on the station. Those that are able to become The Chosen (non-sec/command, not already another antag, and is not 100% guaranteed) also get the objective to claim it.
The Worthy gain an action to toggle a [waypointer](https://github.com/space-wizards/space-station-14/pull/42459) that targets the Throngler. The Worthy are Free Agents, but if they are bound to the Thrognler, they become Solo Antagonist.
Destroying the Throngler takes a somewhat long doAfter, and binding it takes a very very long doAfter. If it is bound, the player gets an action to summon it back (like the Ninja Katana) and their waypointer changes from pointing to the Throngler to pointing to the other Worthy.
If there aren't enough alive players eligible for being The Chosen when the Throngler spawns, ghost roles are made, they spawn with Claymore swords.
There are alternative ways to destroy the Throngler, such as: Throwing it into the singularity (Cast it into the Singularity! Destroy it!) or selling it (good luck not getting it stolen all the way to the ATS).

### Objectives
- Claim the Throngler. Bind the Throngler to yourself, as its one true owner!
- Or destroy the Throngler, ending the cycle of death and violence... for now.

## End of round screen
- Who claimed/destroyed the Throngler
- Who held to the Throngler the longest
- How many lives were claimed by the Throngler
- List of players that were The Chosen
