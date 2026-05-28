||VERY WIP||  
||I'm not sure how to write comments, so I might be just doing those lines||  
||It currently contains the info I think should be put in to this doc, and later it shall be discussed with #silicon maintainers||  
||TODO:||
- Module clusters - how many slots should be in each module, how to split all the items/slots for a Cyborg for each module, how many modules slots Cyborg should have
- Evil modules - Antagonist exclusive modules: Xenoborg, Syndicate Cyborg modules
- what items can be whitelisted
- when to use a hand slot and alternatively make it an item
- unique Cyborg items and when you should add them/ make them

||Ideas and drafts:||  
||
- If a slot allows for carrying a lot of diverse materials, it should be whitelisted (produce, materials, tiles, etc.)
- If a slot holds unique Cyborg tooling (upgraded buckets, stronger versions of items that are not possible to acquire by crew) it should be an unremovable
- A small amount of whitelisted hands for things like tools may be allowed, but only if having hand-per-tool would cause the amount of hands to be unreasonably big
||

||Actual start of the document:||

# Cyborg modules guideline

This document is about guidelines on how to create or modify Cyborg modules
It was created because of the lack of consistency and quality between Cyborg modules
Those guidelines are to help figuring out how to structure singular modules or structure whole specialized Cyborg modules.  

## Cyborg modules
Cyborg modules are an item that is designed to inserted in to a cyborg that grants them items or slots they can use.
Most modules are already built into a Cyborg when selecting a chassis or spawning in, in cases of derelicts, Xenoborgs and
Syndicate Cyborgs. Some modules have to be fabricated in exosuit fabricator usually located in robotics/science department, 
fabricated in Xenoborg core or bought through an uplink. Cyborgs drop all their modules on the floor when destroyed.
Modules can be looked at or added from a cyborg if their maintenance panel is open, but not always remove them  
Some modules provide items that are strictly better than humanoid counterpart and usually have infinite uses with regenerative delay

## Module slots
Module slots are the primary way Cyborgs interact with their environment.

Slots are the Cyborg equivalent of humanoid hands, but unlike hands, they are an array of slots that the Cyborg must cycle through to use. Since Cyborgs lack conventional equipment slots for additional inventories like humanoids, this is the main way they "store" items for them to use around their environment. 

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

### Module slot management
Cyborgs have their equipment separated into reasonably-sized, themed, groups of items.

For ease of access, a Cyborg's tool kit is split into groups that the Cyborg can swap between. One module could be filled with every item in a Cyborg's tool kit, however this would be at the detriment to the Cyborg. Due to the slots being listed and how a Cyborg swaps between them, larger modules become tedious to swap through. So limiting how many items can be in one module helps keep the 'inventory' of the Cyborg organized and usable.

Slots should follow these guidelines:
- On average, a module should contain 6 or fewer items, if they have more, additional slots are placed above the existing 6 slots on the UI. Exceptions may be made in which six slots would be too few for a module, common reasons being categories that are too large such as material sheets allow for this. (Steel, glass, plastic, wood, uranium, gold, silver, etc.)
- Ensure the slot is thematically related to the module it is a part of, filling a "gardening module" with a crowbar does not make sense as the crowbar has no gardening functionality.

