# Round Start Player Equipment

## Overview

This page provides an outline for what types of items and machines are expected to be available to players at the start of their shift. It's particularly concerned with regular department jobs. Antagonists have different needs for starting equipment, which are covered elsewhere in their respective design documents.

This follows the discussion in [Maintainer Meeting (27 September 2025)](../../maintainer-meetings/maintainer-meeting-2025-09-27.md). PRs changing round start equipment are very common and represent a high workload due to subjective and unclear definitions. Round start equipment affects every round, so design standards need to be established for where players get what equipment.

There are five main locations where crew obtain their equipment at the beginning of the shift: 
	- [Loadouts](#Loadouts)
    - [Job Lockers](#Lockers)
	- [Vending Machines](#Vending-Machines)
	- [Lathes](#Lathes)
	- [Mapped](#Mapped)
	
Of these, only the loadout is unavailable for mid-round players receiving promotions or stealing gear. Therefore important items and essential job equipment should **not** be given in loadouts. This ensures these items are present in rounds regardless of player role selection. It also pushes players to visit their department / personal area at least once, connecting them to their department and to their coworkers before inevitably disappearing.

In summary: Players spawn with clothing and RP props from loadouts, collect essential equipment from lockers they spawn next to, claim optional equipment in nearby vending machines, and find generic items in lathes and mapped.

## Definitions

### Essential Equipment

A role's essential equipment are tools which have a nearly irreplaceable function, and can be recognized as thematically "belonging" to the role. A Research Director's stamp is essential equipment because it plays a unique RP function, and has the role's name on it. Epinephrine, a stun baton, the nuke disk, or a bike horn are examples of essential items. These are consequently the items least likely to be in the hands of a different role, and most likely for an antagonist to want to steal. Essential equipment is often department contraband.

Sometimes essential equipment is a set of several items at once, such a a toolbelt or a foolbox. Even if the contents of a toolbelt are generic, having a tool for every situation is essential engineering.

### Optional Equipment

Optional equipment are items that serve an uncommon need to a role, but still recognizably belong to that role. The CMO's beret is optional because it has the role's name on it, but doesn't do anything. A ballistic shield, a substation machine board, or a rolling pin are examples. Unique RP props like a stethoscope and clothing often fall in this category.

### Generic Items

Items that are widely available, easily crafted, and aren't strongly connected to any role's identity. Hand labelers, flashlights, and water are generic.

## Locations

### Loadouts

Loadouts are the items a player has on them when they first spawn. Nearly every station job allows players to customize these loadouts as part of character creation. The loadout is part of creating your unique space alien and so is focused primarily on cosmetics, mainly clothing. But it's also used to limit options as part of the crushing conformity of working under space capitalism.

Every role should spawn wearing department-identifying colors and clothing, with your options existing between different kinds of uniform. At minimum players should spawn with a PDA, a backpack (or variant), a headset with their department's comms channel, and a jumpsuit. Optional categories can exist for any other kind of clothing, but gloves in a loadout **must not** disguise fingerprints to give more intentionality to someone choosing to hide them.

Trinkets are the non-clothing items available in a loadout. These are RP props used to establish a unique character. They should not be used to shortcut finding readily available and common items (like cigarettes) or to give yourself an advantage with some special functionality. Trinkets should be scarce and say something about the personality of your character.

Players should **not** spawn with job-essential equipment, nor any other tool. This includes essential clothing like armor and insulated gloves. Loadouts don't allow a player to do their job without ever visiting their department.

#### Role Time Unlocks

Also called prestige awards, these loadout options are earned from playing a certain amount of time. These items are used for bragging rights and as a reward for being dedicated to your favorite job.

Care needs to be taken that the time asked for these unlocks is not excessive; We don't want to encourage players to hurt themselves by playing too much. Sixty (60) hours is the upper limit of an acceptable role time for a department.

### Lockers

At round-start every role spawns near one (1) complete set of their role's essential equipment. For most roles this gear is in a nearby locked container (a locker), but might rarely be items scattered around their starting room. Mid-round players - either through late joining or getting promoted - will seek out an unclaimed locker to quickly get all their needed items. Antagonists will similarly seek out these lockers, knowing that they will contain everything a person needs to do some specific job. The number of lockers that need to be mapped should be at or barely exceed the roundstart + latejoin capacity of the station (learner jobs included).

A player should want most items found in their locker or have a clear picture of why they would want them. Optional equipment can be included with a chance to appear (as long as it's not selectable in a loadout), and generic equipment shouldn't appear unless it's **really** funny. Expendable items in a locker should have adequate availability outside of lockers to discourage sourcing them from multiple lockers, leaving the next player with part of their gear missing.

Lockers for specialized jobs in a department (including department heads) should include any equipment present in a "lesser" locker, unless that job has an equivalent item.  For instance a toolbelt can be replaced by a toolbelt with more space, or a gun can be replaced by a cooler gun. This is also part of discouraging the raiding of secondary lockers as a source for your own gear. A player shouldn't need anything from a locker that they have access to which wasn't provided in their own locker.

In addition to their own specialized gear, there are several items present in all command lockers.

 - A personal stamp.
 - A headset with encryption keys for their department and for command.
 - A door remote controlling their department's airlocks.
 - A box containing spare department encryption keys.
 - A box containing spare circuit boards for vital machines and computers.

### Vending Machines

Vending machines are the main source of optional and expendable equipment for departments, and are a common source of generic equipment in public spaces. Vending machines are consistent, simple, and well-known locations for sets of items. Their limited stock creates resource scarcity, but their resources are never truly scarce with a restock from Cargo. 

Each full department contains (at least) two (2) vending machines responsible for restocking players and providing extra supplies. The wardrobe (or "Drobe") consists of clothing, while the second supplies non-clothing. Together they should supply at least two naked players with the necessary gear to work the job (two complete sets of spare tools and uniforms).

#### Department Tool Vendor

Department tool vendors contain (in order) two (2) full sets of essential equipment, followed by extra expendable equipment, then optional equipment. They should never have generic equipment. Non-essential items should be stocked to have supplies for roughly four (4) players. Clothing items typically belong in the wardrobe, but a few exceptions exist:

 - Filled Container Clothing
  - - This typically means belts. While the belt itself is a clothing item, the items inside it are not and should not be available inside a wardrobe.
 - Worn items that aren't clothing
 - - Items like whistles or a backpack water tank. While they can be worn, they aren't "clothing" in a visual sense. They are more tool than garb.
 - Clothing not worn by the player themselves
 - - These are things like a muzzle or a hospital gown. They're akin to tools in how they are used on others, rather than used for yourself.

#### Department Clothing Vendor

Department clothing vendors (typically called "Drobes") should spawn with two (2) sets of any essential clothing not present in a tool vendor and two (2) sets of optional clothing. Stock should be split for items that are effectively identical (such as headset variants). Clothes should reflect the standard uniform and aesthetics of a department employee and include anything available in a loadout (excluding prestige rewards). Every item in a Drobe must be equippable. The order of clothing in a Drobe should have essential equipment listed first, followed by: `Head -> Eyes -> Mask -> Ears -> Back -> Belt -> InnerClothing -> OuterClothing -> Neck -> Gloves -> Feet`.

#### Combined Vendors

Certain individual roles on the station have a dedicated vending machine due to some specific nature of that role. Unlike other vendors these only need enough stock to supply one player of essential equipment and clothing. If they contain any non-clothing items, they should not use "Drobe" as part of their name.

Sometimes there's so little non-essential equipment for a role that even a combined vending machine is overkill. In these cases (like with command), optional equipment is mapped near their spawn such as clothes in a dresser.

### Lathes

Lathes serve as the primary source for generic equipment in a round. They provide a quick, expensive way to gear players with (large amounts of) common items. They supply an even more consistently selection of more items compared to vending machines, but with a high cost as tradeoff for the lack of scarcity. Lathes also serve as the reward vector for the science department's research later in a round.

Each lathe should be specialized with a clear theme for the items it has available. Autolathes are specialized in the most generic of items crew are expected to have in abundance, while department specific lathes are specialized in items for that department. Initial offerings from lathes should feel cheaper and lower quality than items available from other sources like cargo or vending machines. The more specialized equipment - including some essential equipment - should not be immediately available, and in some cases might never become available (requiring alternative sources like Cargo).

### Mapped

The items that start mapped for a department are their initial source for generic equipment like materials, though these items can be anything appropriate for the access they are locked behind. Specifics are established in ( link mapping doc here ).

#### Armory

The armory is a special location on maps which belongs to the security department. Mapped inside is the station's supply of lethal weapons and protective armor. Similar to a vending machine, the armory is a primary source for much of the department's optional gear; Except instead of a machine you have a very serious warden demanding paperwork for losing your service weapon.

#### Maintenance

Maintenance contains the widest variety of items for players, but is stocked mostly randomly. The random selection and spooky hallways cater to players seeking danger, uncertainty, and variety in their equipment.