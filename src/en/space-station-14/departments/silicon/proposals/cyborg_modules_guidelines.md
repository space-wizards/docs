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
- Any whitelisted hand should only allow for items from a single category, a whitelist hand cannot for example hold materials AND tiles, those would have to be 2 separate hands  

||

||Actual start of the document:||

# Cyborg modules guideline

This document is about guidelines on how to create or modify Cyborg modules
It was created because of the lack of consistency and quality between Cyborg modules
Those guidelines are to help figuring out how to structure singular modules or structure whole specialized Cyborg modules.  

## Cyborg modules
Cyborg modules are an item that is designed to inserted in to a cyborg that grants them items or slots they can use.
Most modules are already build into a Cyborg when selecting a chassis or spawning in, in cases of derelicts, Xenoborgs and
Syndicate Cyborgs. Some modules have to be fabricated in exosuit fabricator usually located in robotics/science department, 
fabricated in Xenoborg core or bought through an uplink. Cyborgs drop all their modules on the floor when destroyed.
Modules can be looked at or added from a cyborg if their maintenance panel is open, but not always remove them  
Some modules provide items that are strictly better than humanoid counterpart and usually have infinite uses with regenerative delay

## Module slots
Module slots are the primary way Cyborgs interact with their environment.

Slots are the Cyborg equivalent of humanoid hands, but unlike hands, they are fixed loadouts that the Cyborg must cycle through to use. Since Cyborgs lack conventional equipment slots for additional inventories like humanoids, this is the main way they "store" items for them to use around their environment. 

There are two types of slots in a module:
- An embedded tool that cannot be removed from the module.
- A whitelisted 'hand' slot in which only specific items can be picked up and dropped.

When making slots, a few precautions must be taken:

### For embedded slots:
- Ensure the item is thematically related to the module it is a part of, filling a "gardening module" with a crowbar does not make sense as the crowbar has no gardening functionality.
- Do not use items that require deployment to function, the point of the tool is that it integrated into the Cyborg, if it must be detachable, a whitelisted 'hand' is better suited for it.
- Do not use items that are consumable or have limited use, if the item gets exhausted, the slot would be rendered useless for the remainder of the slot's installation.
- If an existing exhaustable item is a perfect candidate for a slot, make a new self-sufficient or renewable variant for Cyborg exclusive use.

### For 'hands':
- Ensure the 'hand' slots are restricted in what they can hold, if a hand lacks any restriction, it bypasses limitations that Cyborgs are designed around.
- Do not use categories that are too broad, having a "medical" 'hand' is too vague and involves whitelisting many functionally unrelated items.
- Use narrow item categories that have too many options to be embedded in a reasonable amount of slots, like instruments, topical medicine, and construction materials.
- Never put Cyborg exclusive technology in a whitelisted 'hand', even if a superior version of it exists, Cyborg exclusive items are meant to stay in the modules.

## Generic modules
Generic modules are modules that can fit into any chassis, regardless of model.

A generic module can be fit into any Cyborg and come in a variety of designs, 
(tools, jet modules for space movement, module for carrying materials without an ability to use them)  
Specialized modules are modules that are only designed to fit in to one type of Cyborg chassis.

Generic modules:
- should contain item/slots that aren't department locked and are of general use ||what is general use|| to cyborgs. (tools, jet modules for space movement)
- ||add more examples||

Specialized modules:
- Should fit the theme of the department in which they are specialized in
- Should include the tools that department usually use ||maybe add examples||
- ||add more examples||

### Upgrade modules
Some research unlocks an upgraded version of modules. Those modules are only specialized and that is the only upgrade 
to them.  
- Upgraded modules should do everything that its predecessor could do or more.

### Module slots and how to slice them
Borg usually have all their items separated in to groups, which are then put in to modules.  
- Each module should contain 6 or fewer items, otherwise the slots are put on top of each other, exception to this rule
might be hand slots for storing things. ||might want to rewrite this||
- Every module should have a theme it tries to achieve, and shouldn't try to fit several themes at once 
(gardening module over a module that has both gardening tools and chemistry tools)

