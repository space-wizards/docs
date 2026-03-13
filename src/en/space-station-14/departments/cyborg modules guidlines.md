||VERY WIP||  
||I'm not sure how to write comments so i might be just doing those lines||  
||It currently contains the info i think should be put in to this doc, and later it shall be discussed with #silicon maintainers||  
||TODO:||
- Module clusters - how many slots should be in each modules, how to split all the items/slots for a borg for each module, how many modules slots borg should have
- Evil modules - Antag modules: xenoborg, syndiborg modules
- what items can be whitelisted
- when to use a hand slot and alternativly make it an item
- unique borg items and when you should add them/ make them

||Ideas and drafts:||  
||
- If a slot allows for carrying a lot of diverse materials, it should be whitelisted (produce, materials, tiles, yada yada)
- If a slot holds unique borg tooling (upgraded buckets, stronger versions of items that are not possible to acquire by crew) it should be a unremovable
- a small amount of whitelisted hands for things like tools may be allowed, but only if having hand-per-tool would cause the amount of hands to be unreasonably big
- Any whitelisted hand should only allow for items from a single category, a whitelist hand cannot for example hold materials AND tiles, those would have to be 2 seperate hands  

||

||Actualy start of the document:||

# Cyborg modules guideline

This document is about guidelines on how to create or modify borg modules
It was created because of the lack of consistency and quality between borg modules
Those guidelines are to help figuring out how to structure singular modules or structure whole specialized borg modules.  

## Cyborg modules
Cybrog modules are an item that is designed to inserted in to a cyborg that grants them items or slots they can use.
Most modules are already build into a borg when selecting a chasie or spawning in in casees of direlects, xenoborgs and
syndiborgs. Some modules have to be fabricated in exosuit fabricator usually located in robotics/science department, 
fabricated in xenoborg core or bought through an uplink. Cyborgs drop all their modules on the floor when destroyed.
Modules can be looked at, added or removed from a cyborg if their mentaince panel is open.

### Module slots
Modules have slots compared to humanoid hands, but are much more restricted, but there are many more of them ||better wording needed||   


There are 2 types of slots in a module:
- An item slot which is an item permanently attached to that slot and cannot be removed from it
- A hand slot which is often an empty slot in which only whitelisted items can be picked up in to it and removed  

Here are the things you should think about when deciding what slot to add.  
For items:
- Tool that don't require to be placed on the floor, and is reusable
- ||add more examples||

For hands:
- Cyborgs should never have unrestricted hand slots ||specify why||
- Item is removable on use (it is usually better to create a regenerating item or a tool that uses that item) ||might want to split this||
- If there are many items of similar usage and are interchangeable (like instruments)
- ||Add more examples||

### Normal and Specialized modules
Normal modules, often depicted as gray, fit in to any chasie as long as there is an empty slot ||is it true with syndi modules?||
Specialized modules are modules that are only designed to fit in to one type of borg chasie.   
Overall normal modules should usually contain items that a passager could get without added acess and 
specialized modules should contain items usually found in their chosen department.

Normal modules:
- They should be universal and not specialized in to any department
- ||add more examples||

Specailized modules:
- Should fit the theme of the department in which they are specialized in
- Should include the tools that department usually use ||maybe add examples||
- ||add more examples||

### Upgrade modules
Some research unlocks an upgraded version of modules. Those modules are only specialized and that is the only upgrade 
to them.  
Upgraded modules should do everything that previous module could or more. It can also contain items that can be better
than a humanoid counterpart

### Module slots and how to slice them
Borg usually have all their items seperated in to groups which are then put in to modules.  
Each module should contain 6 or less items, otherwise the slots are put on top of each other, exeption to this rule
might be hand slots for storing things.  
Each module should fallow a theme ||might want to rewrite this||