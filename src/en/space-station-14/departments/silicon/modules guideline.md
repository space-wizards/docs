||VERY WIP||  
||I'm not sure how to write comments so i might be just doing those lines||  
||It currently contains the info i think should be put in to this doc, and later it shall be discussed with #silicon maintainers||  
||TODO:||
- Specialized modules - what they are and what is specialization
- Modules philosophy - just what borgs modules should do and shouldn't
- Module clusters - how many slots should be in each modules, how to split all the items/slots for a borg for each module, how many modules slots borg should have
-
||Ideas and drafts:||  
||
- If a slot allows for carrying a lot of diverse materials, it should be whitelisted (produce, materials, tiles, yada yada)
- If a slot holds unique borg tooling (upgraded buckets, stronger versions of items that are not possible to acquire by crew) it should be a unremovable
- a small amount of whitelisted hands for things like tools may be allowed, but only if having hand-per-tool would cause the amount of hands to be unreasonably big
- Any whitelisted hand should only allow for items from a single category, a whitelist hand cannot for example hold materials AND tiles, those would have to be 2 seperate hands  

explain what the doc is about
explain why the doc is needed and what issues it is meant to solve
present the solution
how the solution addresses the problems
borg hand whitelisted
the doc is written because borg hand whitelisting currently has no guidelines which leads to a lot of microbalancing with no way to properly continue forward
the solution is whatever i wrote above
it allows borgs to have whitelisted hands without being overwhelming and dealing with microbalancing yada yada  
||

||Actualy start of the document:||

# Cyborg modules guideline

This document is about guidelines on how to create or modify borg modules
It was created because of the lack of consistency and quality between borg modules
Those guidelines are to help figuring out how to structure singular modules or structure whole specialized borg modules.  

## Module slots

Modules slot ||explain what module slots are?||
There are 2 types of slots in a module:
- An item slot which is an item permanently attached to that slot and cannot be removed from it
- A hand slot which is often an empty slot in which only whitelisted items can be picked up in to it and removed  

Here are the things you should think about when deciding what slot to add.  
For items:
- If it is a tool that doesn't require to be placed on the floor, is reusable it should be 
- ||add more examples||

For hands:
- If an item is removed on use (it is usually better to create a regenerating item or a tool that uses that item)
- ||Add more examples||

## Module clusters