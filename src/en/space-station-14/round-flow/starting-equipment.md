# Round Start Player Equipment

## Overview

This page provides an outline for what types of items are expected to be available to players at the start of their shift. It's particularly concerned with tools needed for regular station jobs.

This follows the decision made in [Maintainer Meeting (27 September 2025)](../../maintainer-meetings/maintainer-meeting-2025-09-27.md). In summary, PRs changing round start equipment are very common and represent a high workload due to subjective and unclear definitions of what should be available. Round start equipment affects every round, so definitions need to be established for where players get what equipment.

## Forward

There's five main locations where crew can obtain equipment for their role. The items they spawn with in their [Loadout](#Loadouts), items the player spawns next to in [Job Lockers](#Lockers), available nearby in [Department Vending Machines](#Department-Vending-Machines), printed from [Lathes](#Lathes), and items [Mapped](#Mapped) by the map creator.

Of these, only the loadout is unavailable for mid-round players receiving a promotion or looking to steal gear. Therefore important items and essential job equipment should **not** be given in loadouts. This pushes players to visit their department / personal room to collect the gear needed to properly do their jobs, connecting them to their department and to their coworkers before they inevitably disappear into maintenance.

## Definitions

### Essential Equipment
A role's esssential equipment are tools which have an irreplaceable function, and can be recognized as thematically "belonging" to the role. A Research Director's stamp is essential equipment because it plays an irreplaceable RP function, and has the role's name on it. Epinephrine, a stun baton, the nuke disk, or a bike horn are examples of essential items. These are consequently the items least likely to be in the hands of a different role, and most likely for an antagonist to want to steal. Essential equipment is often department contraband.

Sometimes essential equipment is a set of several items at once, such a a toolbelt or a foolbox. A t-ray might be too common to be considered thematic, but a belt filled with a tool for every situation is thematic for engineers.

### Optional Equipment
Optional equipment are items that serve an uncommon need to a role, but are still recognizably belonging to that role. The CMO's beret is optional because while it has the role's name on it, it doesn't do anything. A ballistic shield or inflatable walls are examples. Unique RP props like a stethoscope and clothing often fall in this category.

### Generic Equipment
Items that are widely available, easily crafted, or aren't strongly connected to a role's identity are generic. Hand labelers, flashlights, and many RP props are examples of generic equipment.

### Expendable Equipment
Rather self explanatory: Expendable equipment is finite. It's something you need either time or resources to replace. These can be essential like fuel, optional like grenades, and generic like steel.

## Locations

### Loadouts

todo

Loadouts are the items given to a player when they first spawn. Loadouts are different for each role, and loadouts for station jobs give players a small set of options. These items are never essential, and typically clothing.

Station role loadouts should spawn with department-identifying clothing. At minimum players should spawn with a PDA, a backpack (or variant), a headset with their department's coms channel, and a jumpsuit. Loadouts should **not** contain job-essential equipment that allows a player to do their job without ever visiting their department.

### Lockers

At round-start every role spawn near 1 complete set of their role's essential equipment. Typically this is some sort of locked container (a locker) but might rarely be items scattered around their starting room. They spend a few moments sorting through and equipping these items, getting familiar with them, and preparing for their shift. Mid-round players - either through late joining or getting promoted - will seek out an unclaimed locker to get their gear. Antagonists will similarly seek out these lockers, knowing that they will contain everything a person needs to do some specific job. The number of lockers that need to be mapped should be at or barely exceed the roundstart + latejoin capacity of the station.

A player should want most items found in their locker or have a clear picture of why they would want them. Optional tools can be included with a chance to appear, and generic equipment shouldn't appear unless it's **really** funny. Expendable items in a locker should have adequate availability outside of lockers to discourage raiding multiple lockers for loot and leaving the next player with a half full locker.

Lockers for specialized jobs in a department (including department heads) should include any equipment present in a "lesser" locker, unless that job has specialized equipment that is equal to or better than the "lesser" equipment. For example, a toolbelt can be replaced by a toolbelt with more space, but a submachine gun can't be replaced by a shotgun. This is another measure meant to prevent players from raiding multiple lockers for gear. A player shouldn't want anything from a locker they have access to that wasn't provided in their own locker.

In addition to their own specialized gear, there are several items present in all command lockers.
 - A personal stamp.
 - A headset with encryption keys for their department and for command.
 - A door remote controlling their department's airlocks.
 - A box containing spare department encryption keys.
 - A box containing spare circuit boards for vital machines and computers.

### Department Vending Machines

Department vending machines are access-locked vendors located somewhere inside their respective department. They contain items specific to that department for use by that department, and players need to share the gear inside. Departments typically have two types of vending machines: equipment and clothing. They can be restocked through a purchase from cargo mid-round. Together they should supply at least two naked players with the neccesary gear to work the job (two complete sets of spare tools and uniforms).

#### Equipment Vendor

Equipment vendors contain (in order) 2 sets of locker gear, followed by extra expendable equipment, then optional gear. They should never have generic gear. Clothing (including eyewear and gloves) should instead be found in the department's respective clothing vendor. There are two exceptions: an item which can be worn but isn't clothing - such as a whistle - and clothing that is not worn by the player themselves - such as a muzzle.

#### Clothing Vendor

Clothing vendors (typically called "Drobes") should spawn with 2 sets of any essential clothing and 2 sets of optional clothing. Clothes should reflect the standard uniform and aesthetics of a department employee and include anything available in a loadout (excluding prestige rewards). Every item in a Drobe must be equippable. The order of clothing in a Drobe should have essential equipment listed first, followed by: `Head -> Eyes -> Mask -> Ears -> Back -> Belt -> InnerClothing -> OuterClothing -> Neck -> Gloves -> Feet`.

#### Combined Vendors

Certain individual roles on the station have a dedicated vending machine due to some specific nature of that role. Unlike other vendors these only need enough stock to supply one player of essential equipment and clothing. If they contain any non-clothing items, they should not use "Drobe" as part of their name.

### Lathes

Most departments can print additional gear from a machine using shared resources. At minimum a department's mapped lathe should be capable of equipping a player with the most basic gear needed for their job. Certain specialized equipment - including some essential equipment - should not be immediately available in lathes. They might become available later as a result of science research or from finding a blueprint. Even still some equipment might never be available in a lathe and must be aquired somewhere else, such as cargo.

Lathes are the primary source for generic equipment a player might want. Autolathes are solely capable of printing generic items, while department specific lathes can print anything from generic to essential. Department lathes should be primarily focused on producing items useful to the employees in that department.

| Location | Round Start Lathe |
| --- | --- |
| Hydroponics | biogenerator |
| Cargo | autolate, ore processor |
| Engineering | autolathe |
| HoP Office | uniform printer |
| Medical | medical techfab |
| Armory | security techfab |
| Science | autolathe, protolathe, circuit imprinter, exosuit fabricator |

### Mapped

Maps often contain gear scattered around a department for players to take. These are typically generic items like materials, but can be also be spare tools and expendables. Spawners should exist for a standardized collection of items to guide mappers should they choose to use it. Examples would include a spawner for one random essential tool, or at the extreme a spawner for generic engineering materials on a 30 pop station.