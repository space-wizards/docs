Space stations are both big floating metal structures which you can stand on ("grids") and places of habitation with hallways, maintenance tunnels, departments, offices, and so on.

In Engineering, it's useful to think about a station, be it a static one or a shuttle, as "zones" - an area provided atmosphere that is airtight is one zone, or maybe an area serviced by one substation is one zone. Security and Command can think about the station as being broken up into areas based on access. But every department and every agent on the station can agree that the station is _definitely_ broken up into rooms.

This document discusses how to define rooms, what their impact on parts of the game are, and how they can be modelled to build features on. It'll explore some ideas for features that could use rooms.

# Foundations

## Definitions

A grid is a set of tiles that together are connected together as the "floor". 
A wall is a usually-impassable, usually-airtight object that is bolted onto a grid.
A room is a set of tiles in a grid that are contiguous and surrounded completely by walls.

```
Key: 

# is a wall, 
, is a floor tile
. is empty space
+ is a door
```

```
The below is just empty space:

.....
.....
.....
.....
.....
```

```
A 3x3 grid floating in some space:

.....
.,,,.
.,,,.
.,,,.
.....
```

```
A square of walls measuring 3x3, floating in space. It's not a room.

.....
.###.
.#.#.
.###.
.....
```

```
A room with no doors.

.....
.###.
.#,#.
.###.
.....
```

```
A room with two doors. It doesn't matter if the doors are bolted open or non-functional; it's still a room.

.....
.###.
.+,+.
.###.
.....
```

```
A bigger room with a hole in the centre. Even though it's not airtight, it's still a room.

#####
#,,,#
+,.,+
#,,,#
#####
```

## Impacts

### Department/Role access

Rooms are almost-always scoped to some general or departmental access. For example, all the rooms on the Bridge will be "Command" rooms. Some rooms are scoped to individual roles - The Head of Security's office can only be accessed by the HoS. Walls getting destroyed allows people in who shouldn't be in that room. Doors are hacked.

Rooms contain items and goodies. The walls keep the goodies inside and the tiders outside.
### Engineering 

Generally speaking people want the walls of their rooms to remain there and be re-attached when they're not there. Rooms are an important part of the atmospherics and power zones the station is distributed into; the edges of a zone line up to the rooms.

### Orientation

Players find there way around the map via room structure; corridors lead them around the station, the station map is defined by room structure on the station map, and so on.

Corridors are either named as such or function as maintenance tunnels, but they're still there as spaces used to get elsewhere. They're also still rooms, even if they're not often referred to as such.

Rooms are also labelled - e.g. the "AI room" is the room the AI core is inside.

### Work Division

Rooms are how work is divided. Generally speaking mixed-role rooms are really uncommon; the Warden has their office, science's different disciplines have their own rooms, and the botanists and chefs don't share a workspace.

Rooms are important to contain what a job should be doing. When a room is mixed-use, like the bar, it indicates that it's a room that's used to collaborate between different roles.

### Spawn Logic

Spawners are always mapped to some "room" or other - "the Energy Shotgun is always in the Warden's office". Likewise, job spawners are mapped to rooms - "Pun Pun always starts in the Bartender's office, near the bar."

# Design Proposal

Rooms as explained above are pretty obvious; they map closely to the real world. However, they don't really exist inside the game's design and its codebase. Mappers create rooms, and create beacons that label the rooms, but that doesn't mean that rooms actually exist in the game.

This leads to a few problems that can be solved by making a technical system that supports **dynamically being able to recognize rooms on a grid, get information about them, and use that information to do things.**

The following are examples of why we should make this  system and what we could then bolt on to it.
## Mapping Help

At the moment mapping doesn't have any assistance inside the editor. Standards are kept externally and often drift from reality. It's hard to assert a map is acceptable automatically.

As an example: "the Warden has an energy shotgun in their office". How can this be tested? A human tester can look for a room that matches what they'd expect a warden's office to look like and look for the energy shotgun in that room. But if we know a map has a warden's office, and we could detect that office is on the map, we could programmatically detect if an energy shotgun is inside that room.

This would allow for a mapping system that would mirror games like Dwarf Fortress or Prison Architect, where a room can be specified by the mapper, but the room won't be valid unless it fulfils some checks.

This would obviously be possible to over-engineer  to become dangerously inflexible. But the advantage would exist even if these were just hints; the ability to decorate a map with markup that can be shown via an overlay would allow someone who is unfamiliar with the map to understand its layout, making both design, maintenance and review easier.

## Station Map Improvements

The station map at the moment is a generated UI that shows off the walls, doors, floors and beacons that make up the station. It relies on the beacons to decorate what part of the station is where. This is hard to read sometimes.

Being able to define a room as "engineering" or "service" would allow for that room to be colour-coded on the map. It might also allow for a reduction in the requirement for beacons to exist, because if the room exists itself, it can be given a colour and a label.

This would also have benefits for things like station cameras; a camera in a room would be automatically named after the room it's in. The AI might be able to warp to particular rooms.

## Access Control Improvements

Access controls are completely managed by doors at the moment; a room's access is only covered by what its doors think. This requires managing every single door access on the station by both mappers and the station's engineers.

In reality, access should be thought of more granularly - allowing movement from one room to another.

It's a very common problem where someone follows someone into a room, then cannot leave without being beeped out by someone with access. The game does have one-way doors (the rotating doors that genpop use), but these are very uncommon outside their niche.

Adding room logic would allow for access to be defined on a per-room basis, overwritten by doors on a per-door basis.

For example: the medical triage room might be connected to the foyer of the department, then connected to a general corridor. In some cases, it is preferable that movement between the foyer and the triage room is open. In most cases it isn't. In the case of a zombie outbreak, the foyer might be best off-limits to anyone without medical access.

At the moment this is all managed by editing individual doors. It would be much nicer to be able to set overall access rights for a given **room** using a computer terminal. Individual doors can still be overwritten, but their defaults would be updated by using this console. This access could then be shown on the station map, so all crew are aware where they can and cannot go.

This console could have a master terminal on the Bridge or in the Head Of Security's office, and individual terminals for each department inside its department lead's office.

#### To be clear: door access doesn't change

Door access controls are still the final layer of control, they just have their defaults set by the room. This means that if you fry a door's access, and this is repaired, the door can default back to the access rules the two rooms it exists in have. A door remote can still overwrite the defaults, a door can still be bolted, and so on.

Changing the defaults might be something that could be locked out of happening by snipping the AI wire.
## Improving Random Spawns

At the moment random spawning is tile-based, scanning for a good tile to try and put the spawned entity on. This tends to have annoying edge cases; a common scenario is accidentally spawning a Paradox Clone on the ATS.

With a dynamic room system, random spawning can be much more intelligent. For example, specific rooms could be searched for or excluded from consideration. Rooms could be searched for conditions - can the spawned entity be able to breathe the room's atmosphere? Does it have access to leave the room?

However, care should be taken to avoid the room system being gamed to manipulate where antagonists can spawn. For example, if an antagonist needs a particular situation in a room to allow it to spawn, it could be possible to create a room that guarantees the antag spawns there.

## Making Alerts Mean Something

With a room model with department designations and access rights, alerts can be connected so that rooms can have their access rights (or other properties) altered depending on the alert level. For example, in red alert, this could allow all rooms designated "maintenance" to become off-limits to passengers and make the armory unlocked to security personnel, with security gaining access rights to department areas they normally can't get into.
# Responding To The Round

The big challenge for rooms is responding to the round changes. A start-of-round, static, driven-by-mapping approach works until the first singuloose.

This means that the room structure needs to be configured in ways that players can also configure. This makes sense. If the players decide to build a really nice shuttle, you'd assume they'd want to define that shuttle's rooms. If a Head of Security decides to revise access to parts of the station, it would not be useful if rooms could be permanently deleted.

As such, we need a premade room model of the station, set at round start. If the station's walls and structure change, rooms should be marked as invalid in the model, and those rooms require maintenance. The game internally keeps a track of what rooms exist on the station, but converting those rooms into the model is first done by the mapper, and then left up to the station's crew to maintain.

This is a job that feels appropriate for the Station AI to keep on top of. Keeping an eye on new rooms bolted onto the hull and adding them to the room model, and fixing the model when the bar is remodelled, are tasks which can't, and shouldn't, be left to an automatic system running on some update loop. It would be always broken in annoying ways.

The impact of a broken room model is that the default access controls for the rooms that have been orphaned from the model stop updating. This means that the room's name, default access rights, department designation, etc, can't change until the room is tidied up in the model. This is not the end of the world (it just means the station falls back to how it works now).

This would also have the nice benefit of allowing a destroyed room to still appear on station maps (if you see a yellow transparent box on the station map where it should be solid yellow, you can assume engineering is gone).

Assuming that an access control terminal exists in each department, and a master one exists in a secure location, fixing the room model can be left to the master one, and maybe the AI's always-accessible windows.

## Summary

This system would allow mappers to set up SS14 maps a bit more intelligently with tooling, and then allow for players to maintain the station's organization during the round, making gameplay a bit more structured and dynamic, whilst providing game designers with a big win to fixing random spawning behaviour, by making spawning things be able to search for appropriate rooms to spawn into, rather than doing a tile-by-tile search which lacks the context of the station.