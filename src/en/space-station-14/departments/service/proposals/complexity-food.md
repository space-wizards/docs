# Complexity Food

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| Killerqu00 | Killerqu00 | :x: No | TBD |

## Overview

This proposal aims to describe a score-based system for food items - aiming to set a solid base for hunger/eating/satiation/interact-with-kitchen mechanics. This score-based system is used to grant people buffs and determine food nutrition.

## Background

After looking into food rates in [#39637](https://github.com/space-wizards/space-station-14/pull/39637), I have noticed that hunger system is extremely bare-bones and unbalanceable in the current form - effectively, it is on the same level of development as the Minecraft hunger system (or even lower). This is not very good for an in-depth game as SS14.

Simply slapping a specific "+10% damage for 10 minutes by eating a bacon burger" will result in a meta revolving around specific food recipes. Also, it doesn't support any potential dynamic food recipes, meaning dynamic food recipes will always be worse than specific ones.

### Note

The following parts of the doc go in-depth about the mechanic. Some sort of TLDR can be found starting at "Features to be added" part.

## Food Complexity and Food Groups

Nutrition, vitamin and other food-related reagents are no longer manually added to the food prototype - instead, they are based on food complexity.
Food complexity is a "grade" - how complex is this food in terms of difficulty to make and nutritional balance/fulfillment.
Food type/group is the dietary group of a food item - this already partially exists in a form of tags. This is used to prevent people from spamming the same type of ingredient.
For example, food types can be meat, fruit, vegetable, dairy, grain and sugar. Some misc items (like plasma in the empowered burger) may have special food groups.
Food complexity for base-level ingredients (like raw meat and standard plant produce) is equal to 1. For anything else, it's determined either by manual override in the prototype, or calculated using food complexity of ingredients, food types used, and method of cooking.

### Example, Part 1

Let's take a big bite burger as an example. Big bite is made of:
- 1 bun: complexity is 2, since it consists of flour and water.
- 2 raw meat: complexity is 2.
- 1 cheese wedge: complexity is 2 (while creating cheese via enzyme counts as complexity increase, cutting a cheese wheel doesn't).
- 1 tomato: complexity is 1, since it's standard plant produce.
- 2 onion slice: complexity is 2.

Finally, simply microwaving the food doesn't add any complexity.

## Food Complexity Calculation

In order to calculate food complexity for a dish, simply add up all complexities of ingredients, rounded up. For 4th and 5th ingredient from the same food group, add only half of the complexity. Ingredients beyond 5th from the same food group only add 25% of the complexity.

### Example, Part 2

Let's take a look at the big bite burger again:
- Bun has a group of Grain.
- Raw meat is Meat.
- Cheese wedge is Dairy.
- Tomato is Vegetable.
- Onion slice is also Vegetable.

Since each food group doesn't have more than 3 entries, we can simply add up all the complexity values, resulting in a complexity of big bite burger being 7.

### Example, Part 3

Let's say that we use a custom burger system and put 1000 lettuce into it. Bun has a complexity of 2, and lettuce has a complexity of 1. Only first 3 lettuce add full complexity, only 2 lettuce add half the complexity, and the rest adds 25% of the complexity. This means that the doomstack lettuce burger will only have 2 + 3x1 + 2x0.5 + 995x0.25 = 255 complexity. 

## Nutrition and Food Buffs

Upon consuming food, you gain a buff based on complexity. It isn't tied to a specific timer - instead, it will disappear once you become peckish. The strength of the buff depends on the maximum complexity value of the food you have ate. It should not be a big buff, and it should have a cap on the maximum level to avoid doomstacking. There is no specific buff that satiation provides; instead, it depends on the dish food groups, meaning that by mixing different food groups, you may receive buffs such as (for example):
- Increase in doafter speed for simple, non-harmful actions like crafting and constructing;
- Small buff for regular nutrition/vitamin regeneration;
- Small out-of-combat speed buff (goes away as soon as damage is dealt to/by person);
- Increase in stamina regeneration speed.

Finally, nutrition of the dish is also determined by complexity.

## Features to be added

- All base ingredients get a food group - some of them already exist via tags.
- All food gets a complexity value based on the amount/complexity of ingredients; this complexity value can be scanned by a tool called Nutritional Analyzer.
- By eating complex foods, you gain "Satiated" buff - this buff goes away when you become peckish, and its strength depends on the most nutritious dish you've ate.

## Game Design Rationale

Q: How does the feature align with our Core Design Principles and game philosophy?

A: It's seriously silly - while it's pretty much close to how cooking works in real life, it still allows for "showing off" - for example, making a doomstack lattuce burger with 255 complexity. It doesn't break the balance, though. It is intuitive: healthy diet grants you benefits, feeding on snacks gets you by, but doesn't reward you. It encourages player agency - there are no wrong choices when it comes to cooking, as long as the meal is sufficiently complex. You also don't have any meta dishes.

Q: What makes this feature enjoyable or rewarding for players?

A: Satiated buff gives some nice bonuses for interacting with the chef. Chef is also rewarded for cooking complex dishes. Species' dietary restrictions introduce a challenge for the cook - making a complex dish that utilizes specific food groups and avoids others. These limitations also force the chef to cook a variety of dishes instead of being a one-dish factory.

Q: Does it introduce meaningful choices, risk vs. reward, or new strategies?

A: While cooking is currently not exactly a risky profession, you can have meaningful choices - by making different dishes, you can achieve different micro-buffs in different ratios. You also can't really stick to making the same food due to dietary restrictions - if desired, this variety can be increased using other mechanics - allergies, species' dietary restrictions, specific requests from players, cargo bounties and so on.

Q: How does it enhance player cooperation, competition, or emergent gameplay?

A: Since chef is encouraged to make complex dishes with different types of ingredients, this encourages chefs to cooperate more with botany - different dishes need different ingredients.

## Roundflow & Player interaction

Q: At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?

A: This feature sets the base "round goals" for the chef: provide crew with complex meals. Since it is a base mechanic for cooking, it occurs every round.

Q: How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?

A: The intended behaviour is to encourage chef players to make different complex dishes, and to encourage regular players to interact with the kitchen to satisfy hunger and get useful buffs. Since the snacks are not a complex dish, they have low complexity, resulting in low nutrition and a lack of buffs, meaning they can be used to satisfy hunger if there is no other choice. However, going to the kitchen and getting a complex meal is encouraged via more nutrition and nutrition buffs.

Q: Which department will interact with the feature? How does the feature fit into the design document for that department?

A: This proposal is for service, chef role specifically. With some modifications, this system can also be applied to bartender. This also indirectly brings a small impact to the botany roundflow, since chef now hsa interest in a wider variety of ingredients. There is no design doc for service as of writing this.

## Administrative & Server Rule Impact (if applicable)

Q: Does this feature introduce any new rule enforcement challenges or additional workload for admins?

A: The only thing I can think about is powergaming buffs - however, since buff system is very generic and does not result in a specific-dish-meta, it doesn't seem like a problem to me.

Q: Could this feature increase the likelihood of griefing, rule-breaking, or player disputes? How are the rules enforced mechanically by way the feature will be implemented?

A: I don't see how food influences rules in any capacity.

# Technical Considerations

Q: Does the feature require new systems, UI elements, or refactors of existing ones? Give a short technical outline on how they will be implemented.

A: Step 1: implement food groups and assign them to edible items. Food groups are stored as a list of IDs; then, they are "inherited" via cooking recipes by merging the lists of all ingredients into one - similar to what AlwaysPushInheritanceAttribute does, but specifically for recipes.
Step 2: migrate tags like "Fruit" and such to food groups.
Step 3: implement food complexity calculations - most likely, adding a partial to IngestionSystem. Food complexity (and nutriments) get added to the food item on entity creation.
Step 4: finally, implement the food buffs.

Q: Are there any anticipated performance impacts?

A: No, spamming tons of low-quality food (which increases the entity count) is discouraged.
