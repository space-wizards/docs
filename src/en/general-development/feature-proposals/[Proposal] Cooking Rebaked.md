# Cooking Rebaked


| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---| 
| SyaoranFox | T.T | TBD |

## Overview

This is an overhaul to the cooking system and chef role. This includes recipes, methods of cooking, incentive to both cook and eat various foods, and mechanisms for antagonist play.

## Background

Cooking currently only uses a microwave to create dishes. Dishes are aestetic, and chefs need to go out of their way to create new and interesting ways to perform the role. Often times this leads to chefs creating the same menu each shift, and for the only deviation to occur within roleplay. This means that after 30-40 minutes in the kitchen, the chef will abandon their post either because cooking has gotten stale, or, ingredients have dried up to the point where they cannot continue to cook.

Chefs also lack the antagonist zest present in the SS13 counterpart. Food cannot be poisoned, food instills nothing except to satisfy hunger. Technically the chef can make food that is poisonous, but once the crew has learned what these dishes are, they can just avoid them. Further, there is no insentive for players to see the chef, as the food from vending machines and mail satisfy the slowdown state given by hunger.

## Features to be added

1. Change recipes that require heat to trigger when all ingredients are present, at the correct temperature
1. Change recipes that require chilling to trigger when all ingredients are present, at the correct temperature (ice cream, ice, jelly etc.)
1. Add oven to replace microwave as the main means of cooking hot food.
1. Change microwave to be a faster, but less capacity version of the oven. Can also be limited in what recipes work.
1. Change cooking to follow a component system that have a base, sauce, and topping.
1. Add bases that act similar to how "fundamental" ingredients work already such as noodles, buns, bagels.
1. Create functionality that allows for many items to be "diced" or "grated" to then be sprinkled on top of food.
1. Create functionality that allows for many items to be heated/melted to become liquids to be added to food bases.
1. Allow for most liquids to be used as part of food dishes. This can be both very functional, and horrific. 
1. Add buffs to more complex meals/components.
1. Add a saucepan that allows the chef to create sauces that can go with their food
1. Add jars to allow for the storage of sauces with a lid that can prevent spilling
1. Add a kitchen lathe that can create utensils, crockery, and glass items useful to the kitchen
1. ~~Add allergies to crew~~
1. ~~Add the ability for HoP and/or CMO to generate a report on the crew's list of food requirements~~
1. ~~Add histamine generation for those with allergies that can be treated by medical if they metabolise the allergen.~~
1. Add food processor that can allow for chefs to prepare food ingredients in bulk, and to allow chefs to "reclaim" rolled out dough back into "normal" dough.
1. Increase the consequences for hunger and thirst
1. Allow for food to carry the attributes of its ingredients, both beneficial and detrimental
2. Menu system for chefs to make a menu
1. Give chefs the innate ability to know what is contained in food by examination
1. Add a bookshelf with cookbooks to supliment the ingame help system
1. Change the name of "cornmeal dough" to "cornbread dough" and "tortilla dough" to "cornmeal dough"
1. Cake starter should remain a liquid, and be pourable into a cake pan/sheet pan

## Game Design Rationale

![Cooking Ecosystem](Cooking_Rebaked.svg)

The changes are intended to increase interactions with chef and the kitchen in general. Those with food allergies are required to be more careful about what they eat, thus needing a chef to create dishes that fit their diet. More over, increasing these interactions allows for an antag chef to have more opportunities to perform their required tasks without just running around the station in disguise. The diagram is meant to demonstrate how the chef role and food affects the ecosystem of the station. There are changes proposed that are not listed here, as it was intended to give the overall flow on effect.

## Roundflow & Player interaction

Allergies and increased danger from hunger, by design, requires players to interact with a chef. It also means that a shift that is missing a chef will require significant roleplay, and adjustment, from the other players in the same way that a crew needs to adjust to a lack of engineers. At the start of shift, HoP (or maybe CMO) can generate a report for the chef to ensure that allergies are considered because a menu is created. The menu will in turn determine what kind of buffs will be available to the crew that eat those meals. If, for example, the threat to the station appears to be zombies, it may be beneficial for the chef to change course, and make food that allows crew to run faster rather than have more maximum stamina.

## Administrative & Server Rule Impact (if applicable)

- There needs to be guidelines for what is considered "massive damage" to the station when it comes to purposeful food poisoning, or trying to just kill everyone with an allergy rather than a specific target.

# Technical Considerations

I am still learning the source of SS14. I can look through and offer suggestions, but if I were to implement everything it will take years. A lot of the suggested changes can be added in pieces at various skill levels. I am happy to put up issues for these so people can find the required tasks.

- From what I can tell, we can continue to piggy-back the chemistry system still. Currently dough is made a reagent reaction when present in a container. When we do the food recipes, we just ensure that there is a heating component to the recipe, so that when the oven imparts the heat, the food is created. The item can be spawned on top of the oven at first, but ultimately should spawn inside the container to be retrieved from the oven. E.g. you put a sheet pan of brownie batter in, and you take a sheet pan of brownies out.
- Ovens will need to impart heat like how Hyper Convection Lathes do to the ambient air, but to the food containers itself. Maybe it should also impart radiant heat as well.
- Microwaves would be similar to the above, but the heat transfer is raised, while the maximum heat is lower.
- Saucepans will act like a blender, but is heated on a hotplate/oven top
- Buffs already exist in the game in the form of chemical reagents. Given that food is digested, it could use that system as well. An issue that might arise is hitting the maximum reagent ceiling for each race.
- Recipes will need to be tweaked to use heat, but this is already a part of how chemistry works.
