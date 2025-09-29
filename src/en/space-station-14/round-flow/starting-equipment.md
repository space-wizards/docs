# Round Start Player Equipment

## Overview
This document provides a general outline for what types of items are expected to be available to crew at the start of the round.

This document follows the decision made in [Maintainer Meeting (27 September 2025)](https://hedgedoc.spacestation14.com/Wtd4OwYZThqutLbR3y-e4g). There have been many PRs attempting to change what players get on round start. Round start equipment affects every player every round, so definitions need to be established for where players get what equipment. This way maintainers have a firmer base for evaluating these PRs.

## Locations
There's five main locations crew can obtain job equipment. The items they spawn with in their [Loadout](starting-equipment/loadouts.md), the items that spawn in department [Lockers], items available in department [Vendors], items printed from [Lathes], and items [Mapped] by the map creator. Of these only a loadout is unavailable mid-round to players receiving a promotion or looking to steal gear. Therefore important items and necessary job equipment should **not** be given in loadouts.

Mid-round a sixth location exists for aquring job equipment, that being purchases from cargo. There is currently no design document to link to establishing item availability from cargo.

### Player Loadouts

{{#template ../../../../templates/stub.md}}

Players spawn with these items and can possibly choose between a small set of options. These items are generally cosmetic and/or clothing.

Players should spawn with department-identifying clothing. Players should not spawn with job-essential equipment. All station roles - whether the player is round start, late join, or promoted - are expected to visit their department to collect the gear needed to properly do their job. This helps to connect a player to their department and their coworkers before they begin in earnest.

```admonish success "{Good:}"
 - Jumpsuit
 - Hardhat
 - Sterile mask
```

```admonish failure "{Bad:}"
 - Toolbelt
 - Insulated gloves
 - Nuke disk
```

```admonish question
Should gloves in loadouts be removed or replaced with fingerless versions? Gloves are widely available in-round, and starting with real gloves removes intentionality from antags trying to hide their prints.
```

### Lockers
Players spawn near these, and spend a few moments getting dressed and preparing for the shift. Lockers are intended to contain everything a player needs to do their job to a reasonable degree. Maps should have more lockers than job spawns.

Department lockers should spawn with all job-essential equipment. A player should generally want most items in their locker, or be able to conceive a situation where they would want them. Lockers should not spawn with cosmetic items or contain expendable equipment that another member of their department might want to raid.

```admonish success "{Good:}"
 - Toolbelt
 - Hardsuit
 - Disabler
```

```admonish failure "{Bad:}"
 - Compressed matter
 - Jumpsuit
 - Beer bottle
```


### Vendors
These spawn in departments and players can visit them to share additional gear. Departments typically have two types of vendors: equipment vendors and clothing vendors. They can be restocked through a purchase from cargo mid-round.

Equipment vendors should spawn with expendable equipment, spare tools, and optional tools. They should not spawn with non-department gear or gear that is easily available (such as in an autolathe), even if those items would be useful to the job.

```admonish success "{Good:}"
 - Medical topicals
 - Riot shield
 - RCD
```

```admonish failure "{Bad:}"
 - Flashlight
 - Hand labeler
 - Welding mask
```

```admonish question
Should department vendors contain items for the purpose of distributing them to crew? The EngiVend currently has 8 crowbars, and that's the only reason I can think why it would.
```

Clothing vendors should spawn with equipable items typical of a department's colors or aesthetic qualities. Items should reflect the standard uniform of a department employee at round start.

```admonish success "{Good:}"
 - Jumpsuit
 - Hardhat
 - Jackboots
```

```admonish failure "{Bad:}"
 - Anything that can't be equipped.
 - High-power items (hardsuits).
```

```admonish question
Should eyewear in general and insuls specifically be moved to the drobe? They're currently found in equipment vendors, but they're clothing and arguably break expectations.
```

### Lathes
Most departments can print additional gear from a machine using shared resources. Some have an autolathe to print spare gear, while others have department-specific lathes for this purpose.

Items available to be printed round start from lathes might be tools or expendables. In both cases the options available should be the basic, minimum gear to do the job. Better gear is often available later in the round as a result of science research.

```admonish success "{Good:}"
 - MV Cable
 - Syringe
 - Disabler
```

```admonish failure "{Bad:}"
 - RCD
 - Grenade
 - Grappling gun
```


### Mapped
Some tools or materials might be laid out around the department for players to share. A spawner should exist for these to control and standardize their use through YAML, should a mapper choose to use it.

Mapped items are shared department resources that every player has access to, and which a command member might try to ration. They are often consumable materials but can also include spare equipment.

```admonish success "{Good:}"
 - Glass
 - Handcuffs
 - Banana peel
```

```admonish failure "{Bad:}"
 - Powerful tools otherwise unavailable round start.
```

[Core Design Principles](../core-design/design-principles.md)