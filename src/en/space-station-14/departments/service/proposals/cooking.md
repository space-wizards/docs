# New Cooking System 

| Designers     | Coders        | Implemented | GitHub Links |
| ------------- | ------------- | ----------- | ------------ |
| TheShuEd      | No            | No          | No           |

# Background

I am not fond of the current design of the microwave and cooking systems. When developing my fork, I decided to attempt to create my own cooking system, drawing inspiration from Don't Starve Together and The Legend of Zelda: Breath of the Wild.
The result of my efforts was a system that received a lot of positive feedback. When discussing the possibility of porting the system to Wizden, 
the main task was to structure and describe the game design approach of the new cooking system, which is what this document is intended to do.

# System Overview

## Food

In ss14, “food” has always been simply a container of nutritional reagents, combined with a set of flavors, tags for separating diets, and garbage left over after eating.
This is not enough to, for example, implement the pouring of meat soup from a cauldron into plates. We need “Food” to store more information. 

In addition to reagents, flavors, and waste, “Food” in this system also stores:
- Information about its appearance, in the form of a separate link to a sprite.
- Supported “Food Container” type (e.g., soup)

## Food Container
Food Container - An entity with a container for reagents, such as a pot, plate, or pan. It has a specific type that limits the types of food that can be moved into this container:
- Soups
- Plate dishes
- Skewers
- Pies

It has a number of restrictions that prevent unsuitable types of food from being moved into this container to avoid visualization problems.
It has a number of displacement maps that allow the sprite of the food placed in the container to be displayed correctly, with different levels of fullness. (1 dish sprite will automatically adapt to the level of fullness of the plate)
<img width="484" height="234" alt="image" src="https://github.com/user-attachments/assets/0b92837a-8c0b-41ff-bb61-f1f4a3d1cca3" />

## Cooking process

There is a special type of entity that I call FoodCooker, which is simultaneously:
- An item storage (grid inv)
- A liquid storage
- A food container

For example: a pot, a pan, a pie tin.
The task of such entities is to transform the reagents and items placed inside into “Food” by fulfilling certain recipe conditions. (e.g., heat treatment over a long period of time)
When the conditions are met:
- All items inside are removed, and the inventory becomes inaccessible.
- All reagents, diet tags, trash, and flavors from the removed items are added to the “Food.”
- All reagents added manually are also added to the “Food.”

When all food is either eaten or transferred to other food containers, the inventory becomes available again.

## Fractality of recipes

An important factor in the new cooking system is the ability to experiment and mix anything: in any case, the player will get something.

Each recipe has:
- Food type (Soup)
- Appearance (Link to soup sprite)
- Name, description LocId (Meat broth)
- List of requirements

Requirements are checks that are performed on the FoodCooker entity. They can be of different types:
- From 0 to 20 units of the “Water” reagent
- Presence of an item with the “Meat” tag
- Absence of an item with the “Cheese” tag

Each requirement also has a function for calculating **complexity** based on its own parameters.

The final recipe contains X requirements and automatically calculates the complexity of the recipe based on the number and settings of these requirements.

Example recipes from CrystallEdge:

```yml
- type: CP14CookingRecipe
  id: InedibleSoup
  foodType: Soup
  foodData:
    name: cp14-soup-recipe-trash-name
    desc: cp14-soup-recipe-trash-desc
    visuals:
    - sprite: _CP14/Objects/Consumable/Food/Soups/misc.rsi
      state: trash
  requirements:
  - !type:AlwaysMet

- type: CP14CookingRecipe
  id: MonsterBrew
  foodType: Soup
  foodData:
    name: cp14-soup-recipe-monster-brew-name
    desc: cp14-soup-recipe-monster-brew-desc
    visuals:
    - sprite: _CP14/Objects/Consumable/Food/Soups/misc.rsi
      state: mole
  requirements:
  - !type:ReagentRequired
    amount: 20
    reagents:
    - Water
  - !type:TagRequired
    tags:
    - CP14MeatMonster
  - !type:TagRequired
    tags:
    - CP14Egg
```

All recipes are logically sorted by complexity, from the most complex to the simplest in the game code.

The most complex recipes require precise ingredient ratios and potentially complex conditions, such as 
“12+ units of carpotoxin + at least 2 pieces of dragon meat +  at least 5 units of salt + 5 to 10 units of ichor + cook in a vacuum + no cheese” = Legendary Dragon Soup

Simple recipes, on the other hand, can be prepared in many different ways:
“10+ units of water + any meat” = Meat Soup

The simplest recipe is always “Inedible Slop”, which must be an existing recipe in every food category and has no conditions.

When a player throws random items into a pot and tries to cook soup, the system iterates through all soup recipes from the most complex to the simplest.
The first recipe whose conditions are met is selected and used as the result of cooking. If no conditions are met, there is a fallback to “inedible slop,” which has no conditions.

<img width="858" height="323" alt="image" src="https://github.com/user-attachments/assets/c568c52e-ea1b-4233-87d2-dff47784239d" />

This system has enormous potential for expanding recipes while remaining interesting to play at every stage and encouraging experimentation with ingredients, and as a result of experimentation, different dishes will always be produced.
At the same time, only the appearance and name of the recipes are transferred to the final dish, while the original reagents of all ingredients are used as the filling for the dish: Players can use a poisoned apple to make a fruit salad and get a poisoned salad.
Similarly, in the future, the complexity of a recipe could be used to determine the beneficial properties of a dish, rewarding players with special bonuses for preparing complex dishes.

## Example of implementation

This system has already been successfully implemented in CrystallEdge, and you can download the latest build to check out the system's gameplay cycle and try cooking something.
You can find videos with examples at the links below. All code for these systems is under MIT and is free to port.
https://github.com/crystallpunk-14/crystall-punk-14/pull/1529
https://github.com/crystallpunk-14/crystall-punk-14/pull/1535
https://github.com/crystallpunk-14/crystall-punk-14/pull/1540

The implementation is not perfect and has some bugs.
