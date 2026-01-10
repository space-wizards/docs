# Round Start Player Equipment

## Overview

This page provides an outline for what types of items and machines are expected to be available to players at the start of their shift. It's particularly concerned with tools needed for regular department jobs. Antagonists have different needs for starting equipment which are covered elsewhere in their respective design documents.

This follows the discussion in [Maintainer Meeting (27 September 2025)](../../maintainer-meetings/maintainer-meeting-2025-09-27.md). PRs changing round start equipment are very common and represent a high workload due to subjective and unclear definitions. Round start equipment affects every round, so design standards need to be established for where players get what equipment.

There's five main locations where crew obtain their equipment at the begining of the shift: 
	- [Loadouts](#Loadouts)
    - [Job Lockers](#Lockers)
	- [Vending Machines](#Vending-Machines)
	- [Lathes](#Lathes)
	- [Mapped](#Mapped)
	
Of these only the loadout is unavailable for mid-round players receiving promotions or stealing gear. Therefore important items and essential job equipment should **not** be given in loadouts. This ensures these items are present in rounds regardless of player role selection. It also pushes players to visit their department / personal area at least once, connecting them to their department and to their coworkers before inevitably disappearing.

In summary players spawn with clothing and RP props from loadouts, collect essential equipment from lockers they spawn next to, claim optional equipment in nearby vending machines, and find generic equipment in lathes and mapped.

## Definitions

### Essential Equipment

A role's esssential equipment are tools which have an often irreplaceable function, and can be recognized as thematically "belonging" to the role. A Research Director's stamp is essential equipment because it plays an irreplaceable RP function, and has the role's name on it. Epinephrine, a stun baton, the nuke disk, or a bike horn are examples of essential items. These are consequently the items least likely to be in the hands of a different role, and most likely for an antagonist to want to steal. Essential equipment is often department contraband.

Sometimes essential equipment is a set of several items at once, such a a toolbelt or a foolbox. Even if the contents of a toolbelt are generic, having a tool for every situation is essential engineering.

### Optional Equipment

Optional equipment are items that serve an uncommon need to a role, but still recognizably belonging to that role. The CMO's beret is optional because it has the role's name on it, but doesn't do anything. A ballistic shield or inflatable walls are examples. Unique RP props like a stethoscope and clothing often fall in this category.

### Generic Equipment

Items that are widely available, easily crafted, or aren't strongly connected to a role's identity are generic. Hand labelers, flashlights, and many RP props are examples of generic equipment.

### Expendable Equipment

Rather self explanatory: Expendable equipment is finite. It's something you need either time or resources to replace. These can be essential like welding fuel, optional like grenades, and generic like steel.

## Locations

### Loadouts

todo

Loadouts are the items given to a player when they first spawn. Loadouts are different for each role, and loadouts for station jobs give players a selection of options for all of them. These items are never essential, and typically clothing.

Station role loadouts should spawn with department-identifying clothing. At minimum players should spawn with a PDA, a backpack (or variant), a headset with their department's coms channel, and a jumpsuit. Loadouts should **not** contain job-essential equipment that allows a player to do their job without ever visiting their department.

### Lockers

At round-start every role spawn near one (1) complete set of their role's essential equipment. Typically this is some sort of locked container (a locker) but might rarely be items scattered around their starting room. They spend a few moments sorting through and equipping these items, getting familiar with them, and preparing themselves for the shift ahead. Mid-round players - either through late joining or getting promoted - will seek out an unclaimed locker to get their gear due to the simplicity. Antagonists will similarly seek out these lockers, knowing that they will contain everything a person needs to do some specific job. The number of lockers that need to be mapped should be at or barely exceed the roundstart + latejoin capacity of the station (learner jobs included).

A player should want most items found in their locker or have a clear picture of why they would want them. Optional equipment can be included with a chance to appear (as long as it's not selectable in a loadout), and generic equipment shouldn't appear unless it's **really** funny. Expendable items in a locker should have adequate availability outside of lockers to discourage raiding multiple lockers for loot and leaving the next player with a half full locker.

Lockers for specialized jobs in a department (including department heads) should include any equipment present in a "lesser" locker, unless that job has better equipment equivalent to the "lesser" equipment. For example a toolbelt can be replaced by a toolbelt with more space, but a submachine gun can't be replaced by a shotgun. This is another measure meant to prevent players from raiding multiple lockers for gear. A player shouldn't want anything from a locker they have access to that wasn't provided in their own locker.

In addition to their own specialized gear, there are several items present in all command lockers.
 - A personal stamp.
 - A headset with encryption keys for their department and for command.
 - A door remote controlling their department's airlocks.
 - A box containing spare department encryption keys.
 - A box containing spare circuit boards for vital machines and computers.

### Vending Machines

Vending machines are the main source of optional and expendable equipment for departments, and are a common source of generic equipment in public spaces. They create resource competition that isn't difficult to resolve (a restock from Cargo is always available) and serve as a consistent, well-known location for sets of items. A player can trust that if they need snacks, a snack dispenser will be a strong choice.

Each full department contains (at least) two (2) vending machines responsible for restocking players and providing extra supplies. The wardrobe (or "Drobe") consists of clothing while the second supplies non-clothing. Together they should supply at least two naked players with the neccesary gear to work the job (two complete sets of spare tools and uniforms).

#### Department Tool Vendor

Department tool vendors contain (in order) two (2) full sets of essential equipment, followed by extra expendable equipment, then optional equipment. They should never have generic equipment. Non-essential items should be stocked to have supplies for roughly four (4) players. Clothing items typically belong in the wardrobe, but a few exceptions exist:

 - Filled Container Clothing
  - - This typically means belts. While the belt itself is a clothing item, the items inside it are not and should not be available inside a wardrobe.
 - Worn items that aren't clothing
 - - Items like whistles or a backpack water tank. While they can be worn, they aren't "clothing" in a visual sense. They are more tool than garb.
 - Clothing not worn by the player themselves
 - - These are things like a muzzle or a hospital gown. They're akin to tools in how they are used on others, rather than used for yourself.

#### Department Clothing Vendor

Department clothing vendors (typically called "Drobes") should spawn with two (2) sets of any essential clothing not present in a tool vendor and 2 sets of optional clothing. Stock should be split for items that are effectively identical (such as headset variants). Clothes should reflect the standard uniform and aesthetics of a department employee and include anything available in a loadout (excluding prestige rewards). Every item in a Drobe must be equippable. The order of clothing in a Drobe should have essential equipment listed first, followed by: `Head -> Eyes -> Mask -> Ears -> Back -> Belt -> InnerClothing -> OuterClothing -> Neck -> Gloves -> Feet`.

#### Combined Vendors

Certain individual roles on the station have a dedicated vending machine due to some specific nature of that role. Unlike other vendors these only need enough stock to supply one player of essential equipment and clothing. If they contain any non-clothing items, they should not use "Drobe" as part of their name.

Sometimes there's so little non-essential equipment for a role that even a combined vending machine is overkill. In these cases (like with command), optional equipment is mapped near their spawn such as clothes in a dresser.

### Lathes

Lathes serve as the primary source for generic equipment in a round. They provide a quick, expensive way to gear players with (large amounts of) common items and expendables. They supply an even more consistently and wider selection of items compared to vending machines, but with a high cost as tradeoff for the lack of scarcity. Later in a round lathes also serve as the reward vector for the science department's research.

Each lathe should be specialized with a clear theme for the items it has available. Autolathes are specialized in the most generic of items crew are expected to have in abundance, while department specific lathes are specialized in items for that department. Initial offerings from lathes should feel cheaper and lower quality than items available from other sources like cargo or vending machines. The more specialized equipment - including some essential equipment - should not be immediately available, and in some cases might never become available (requiring alternative sources).

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

Maps often contain gear scattered around a department for players to take. These are typically generic equipment like materials, but can be anything appropriate to the department. Well commented spawners should exist for standardized collections of equipment to guide mappers on what should be included, additionally enabling balancing through YAML.

#### Armory

The armory is a special location on maps which belongs to the security department. It's similar to a vending machine in how it's a primary source for much of the department's optional gear; Except instead of a cheery pre-recorded message, you have a very serious warden demanding paperwork for losing your service weapon.

The station's supply of lethal weapons are held in the armory, as well as its combat grade protective gear and armor. There should be no more than one (1) `reflective vest` as part of an armory's stock.

#### Maintenance

The scary unlit sections of a station, maintenance contains random generic items and (rarely) viable weapons. The random selection and spooky hallways cater to players seeking danger, uncertainty, and variety in their equipment.