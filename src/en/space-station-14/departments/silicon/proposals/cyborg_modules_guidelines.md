# Cyborg modules guideline

This document has been created in hopes of explaining what a Cyborg module is, what their contents should be, and how they should be implemented in the context of the whole game. 

It was written in response to a large influx of microbalance pull requests following the implementation of whitelisted Cyborg 'hands', leading to designs that would infringe on a Cyborg's desired limitations or inadvertently obsolete existing modules. 

## Cyborg modules
Cyborg modules are items that grant a variety of unique abilities to Cyborgs.

A majority of modules are given to a Cyborg when they choose a model. The rest are obtained through fabrication at various workstations or purchased through Syndicate up-links. 

To install a module into a Cyborg, it must be unlocked via an assigned access or damaged into a state beyond movement. After it has been unlocked, its maintenance panel can be opened with a screwdriver. In the case of forced maintenance, a prying tool may be used once the Cyborg has been damaged sufficiently.

With the panel open, modules may be freely removed or added, as long as the chassis has space for the slotted module.
- For embedded modules, they can not be removed through the maintenance panel.

Upon a Cyborg's destruction, it will drop all their installed modules, allowing for a reinstallation into a new chassis, dependent on its model specifications.

A Cyborg may only be installed with a limited amount of modules, this is to prevent a Cyborg from becoming an all-in-one solution.

## Module slots
Module slots are the primary way Cyborgs interact with their environment.

Slots are the Cyborg equivalent of humanoid hands, but unlike hands, they are an array of slots that the Cyborg must cycle through to use. Since Cyborgs lack conventional equipment slots for additional inventories like humanoids, this is the main way they "store" items for them to use around their environment. 

A module should rarely ever be one slot, exceptions may apply for certain modules such as the martyr module, but to prevent modules from being too one-off in their scope, it should be avoided. A low slot count is fine, as long as the items in it are powerful enough to warrant it.

There are two types of slots in a module:
- An embedded tool that cannot be removed from the module.
- A whitelisted 'hand' slot in which only specific items can be picked up and dropped.

When making slots, a few precautions must be taken:

### For embedded slots:
- Do not use items that require deployment to function, the point of the tool is that it integrated into the Cyborg, if it must be detachable, a whitelisted 'hand' is better suited for it.
- Do not use items that are consumable or have limited use, if the item gets exhausted, the slot would be rendered useless for the remainder of the slot's installation.
- If an existing exhaustable item is a perfect candidate for a slot, make a new self-sufficient or renewable variant for Cyborg exclusive use.

### For whitelisted 'hands':
- Ensure the 'hand' slots are restricted in what they can hold, if a hand lacks any restriction, it bypasses limitations that Cyborgs are designed around.
- Do not use categories that are too broad, having a "medical" 'hand' is too vague and involves whitelisting many functionally unrelated items.
- Use narrow item categories that have too many options to be embedded in a reasonable amount of slots, like instruments, topical medicine, and construction materials.
- Never put Cyborg exclusive technology in a whitelisted 'hand', even if a superior version of it exists, Cyborg exclusive items are meant to stay in the modules.

## Generic modules
Generic modules are all-around helpful modules that can fit into any chassis, regardless of model.

Most generic modules can be manufactured at an Exosuit fabricator found in Science's robotics branch, while others may need to be purchased by a Syndicate up-link. Items in these modules are generally helpful to have on any chassis they are installed on, not favoring any specific chassis should it be installed.

Generic modules should contain:
- Items that are not departmentally locked contraband, if an item is exclusive to a department, it does not belong in a generic module.
- Items that have a wide variety of applications, a set of basic tools such as a crowbar, wrench, screwdriver, wire cutters, welder and a multitool have universal utility in many areas of the game.
- A set of specific items that would not be role altering, items like art supplies, or navigational equipment are narrow in category, but do not fundamentally alter a Cyborg's primary specialty.

## Specialized modules:
Specialized modules are chassis specific modules that grant Cyborgs powerful abilities.

Most specialized modules are integrated into their respective chassis, they provide powerful, themed, utilities to a Cyborg and are the primary tools that make the specialized chassis exceed at their purpose. These should be the primary draw when playing a specific chassis, meaning their contents should have exclusive and powerful technology.

Specialized modules should contain:
- Items that are heavily themed around the chassis' chosen specialization, the more synonymous, the better.
- Items that have specific use cases, it does not matter how narrow the category may seem, the chassis the module will occupy has one area of expertise, it should exceed at it.
- Powerful, Cyborg exclusive technology. These should be the reason someone will choose a certain chassis, and are one of the primary perks to playing a Cyborg over a humanoid.

### Upgrade modules
Upgrade modules are a way to further improve a Cyborg's abilities.

Much like the rest of the station, Cyborgs can be improved in various ways such as research done through the Science department or through resource investments. As the name implies, they are upgrades to existing versions of modules that should surpass the capabilities of the original.
- Upgraded modules should do everything that its predecessor could do and more.
- If there is no way to improve a contents of a module, it may be given new equipment as long as it improves upon the theme in some form.
- Upgraded modules are fabricated, and should come at a slightly premium price such as costing gold, bananium, a fair amount of common material or some other uncommon material.

### Passive modules
Passive modules are modules that grant Cyborgs passive abilities.

As the name suggests, passive modules grants persistant abilities to a Cyborg for having them installed. Because of this persistence, passive abilities should be relatively tame in their capabilities.

### Module slot management
Cyborgs have their equipment separated into reasonably-sized, themed, groups of items.

For ease of access, a Cyborg's tool kit is split into groups that the Cyborg can swap between. One module could be filled with every item in a Cyborg's tool kit, however this would be at the detriment to the Cyborg. Due to the slots being listed and how a Cyborg swaps between them, larger modules become tedious to swap through. So limiting how many items can be in one module helps keep the 'inventory' of the Cyborg organized and usable.

Slots should follow these guidelines:
- On average, a module should contain 6 or fewer items, if they have more, additional slots are placed above the existing 6 slots on the UI. Exceptions may be made in which six slots would be too few for a module, common reasons being categories that are too large such as material sheets allow for this. (Steel, glass, plastic, wood, uranium, gold, silver, etc.)
- Ensure the slot is thematically related to the module it is a part of, filling a "gardening module" with a crowbar does not make sense as the crowbar has no gardening functionality.

