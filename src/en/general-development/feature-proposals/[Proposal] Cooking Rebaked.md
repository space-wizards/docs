# Cooking Rebaked


| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---| 
| SyaoranFox | T.T | TBD |

## Overview

This is an overhall to the cooking system and chef role. This includes recipes, methods of cooking, incentive to both cook and eat various foods, and mechanisms for antagonist play.

## Background

Cooking currently only uses a microwave to create dishes. Dishes are aestetic, and chefs need to go out of their way to create new and interesting ways to perform the role. Often times this leads to chefs creating the same menu each shift, and for the only deviation to occur within roleplay. This means that after 30-40 minutes in the kitchen, the chef will abandon their post either because cooking has gotten stale, or, ingredients have dried up to the point where they cannot continue to cook.

Chefs also lack the antagonist zest present in the SS13 counterpart. Food cannot be poisoned, food instills nothing except to satisfy hunger. Technically the chef can make food that is poisonous, but once the crew has learned what these dishes are, they can just avoid them. Further, there is no insentive for players to see the chef, as the food from vending machines and mail satisfy the slowdown state given by hunger.

## Features to be added

1. Change recipes that require heat to trigger when all ingredients are present, at the correct temperature
2. Change recipes that require chilling to trigger when all ingredients are present, at the correct temperature (ice cream, ice, jelly etc.)
3. Add oven to replace microwave as the main means of cooking hot food.
4. Change microwave to be a faster, but less capacity version of the oven. Can also be limited in what recipes work.
5. Change cooking to follow a component system that have a base, sauce, and topping.
6. Add bases that act similar to how "fundamental" ingredients work already such as noodles, buns, bagels.
7. Create functionality that allows for many items to be "diced" or "grated" to then be sprinkled ontop of food.
8. Create functionality that allows for many items to be heated/melted to become liquids to be added to food bases.
9. Allow for most liquids to be used as part of food dishes. This can be both very functional, and horrific. 
10. Add buffs to more complex meals/components.
11. Add a saucepan that allows the chef to create sauces that can go with their food
12. Add jars to allow for the storage of sauces with a lid that can prevent spilling
13. Add a kitchen lathe that can create utencils, crockery, and glass items useful to the kitchen
14. Add alergies to crew
15. Add the ability for HoP and/or CMO to generate a report on the crew's list of food requirements
16. Add histamine generation for those with alergies that can be treated by medical if they metabolise the alergen.
17. Add food processor that can allow for chefs to prepare food ingredients in bulk, and to allow chefs to "reclaim" rolled out dough back into "normal" dough.
18. Increase the consiquences for hunger and thirst
19. Allow for food to carry the attributes of its ingredients, both beneficial and detrimental
20. Menu system for chefs to make a menu
21. Give chefs the innate ability to know what is contained in food by examination
22. Add a bookshelf with cookbooks to supliment the ingame help system

## Game Design Rationale

Consider addressing:
- How does the feature align with our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosphy?
- What makes this feature enjoyable or rewarding for players?
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- How does it enhance player cooperation, competition, or emergent gameplay?
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?

## Roundflow & Player interaction

Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
- Which department will interact with the feature? How does the feature fit into the [design document](../space-station-14/departments.md) for that department?

## Administrative & Server Rule Impact (if applicable)

- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
- How are the rules enforced mechanically by way the feature will be implemented?

# Technical Considerations

- Does the feature require new systems, UI elements, or refactors of existing ones? Give a short technical outline on how they will be implemented.
- Are there any anticipated performance impacts?
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
