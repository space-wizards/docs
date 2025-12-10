# Department Vending Machines

## Overview

Department vending machines are access-locked vendors located somewhere inside their respective department. They contain items specific to that department, for use by that department, and players need to share the gear inside. Departments typically have two types of vending machines: equipment and clothing. They can be restocked through a purchase from cargo mid-round.

## Requirements

A deparment vendor should have enough stock to supply two naked players with the neccesary gear to work the job. An untouched pair of vending machines should have two complete sets of spare tools and uniforms.

### Equipment Vendor

Equipment vendors contain expendable equipment, spare tools, and optional tools. Gear they provide should be regularly useful and sought by players. They should not have gear that is easily available (such as in an autolathe), even if those items would be useful to the job. Nor should they have gear in excess for the purpose of distributing it to non-department players (such as an Engi-Vend with 8 crowbars).

Items in an equipment vendor should never be clothing. This includes all eyewear and gloves, even if such items are important tools for the job. They should instead be found in the department's respective clothing vendor. There are two exceptions: an item which can be worn but isn't clothing - such as a whistle - and clothing that is not worn by the player themselves - such as a medical gown to give to patients.

```admonish success "Good:"
 - Compressed matter
 - Syringe
 - Riot shield
```

```admonish failure "Bad:"
 - Flashlight
 - Hand labeler
 - Welding mask
```

The order of gear in a vendor should loosely follow the importance of the item. Spare tools should be at the top, followed by expendable equipment, and lastly stituational and optional gear.

### Clothing Vendor

Clothing vendors (typically called "Drobes") should spawn with clothing typical of a department's colors or aesthetic qualities. Clothes should reflect the standard uniform of a department employee and include anything available in a loadout (excluding prestige rewards). Every item in a Drobe must be equippable. Particularly powerful clothing should instead be found in department lockers.

```admonish success "Good:"
 - Jumpsuit
 - Jackboots
 - Hardhat
```

```admonish failure "Bad:"
 - Hand labeler
 - Galoshes
 - Hardsuit
```

The order of clothing in a Drobe from top to bottom should go: `Head -> Eyes -> Mask -> Ears -> Back -> Belt -> InnerClothing -> OuterClothing -> Neck -> Gloves -> Feet`.

### Combined Vendors

Certain individual roles on the station have a dedicated vending machine due to the specific nature of that role. Unlike other vendors these only need enough stock to resupply one player. If they contain non-clothing items, they should not use "Drobe" as part of their name.