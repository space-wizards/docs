# How to get rid of microwaves

| Designers | Implemented | GitHub Links |
| --------- | ----------- | ------------ |
| EWanderer | None        | TBD          |

## Overview

The process of making food is largely centered on a microwave, which serves as a sort of compiler. This is very much undesired, for it removes much of the magic of producing different dishes and comes with it’s own caveats on what you can or cannot do as a chef. Finally the code has been said to be very messy. In this document we shall take stock of why the microwave system exists and how one might be able to circumvent it, while maintaining or even expanding existing meal variety and recipes.

## Background

Lets first take stock of broad meal categories. There are some outliers like the “chèvre chaud”, but there no trouble to see where they would fit into the system at the end.

- Dough Based (also Tortilla/Cotton)
  - Bagel
  - Croissant
  - Dumplings
  - Sandwich
  - Bread
  - Nachos
  - Pizza
  - Taco
- Liquid Solutions
  - Cookie
  - Brownie
  - Muffin
  - Pancake
  - Waffles
  - Baguette
  - Cake
  - Spaghetti
  - Oatmeal
  - Pie
  - Soup
  - Stews
  - Sauce
- Other
  - Fries
  - Skewer
  - Rice
  - Salad
  - Steak
  - Grilled Meats

Overall there are three main take aways:

1. Intent. As we can see there is in theory a lot we can already do from dough by marking out intent between slicing, rolling and combining pieces together (dumplings). Simply by recording the actions done with the dough.
2. Burgers are also a fascinating case of being sort of open ended when it comes to putting items into them. Their actual type is eventually determined by what is placed in them.
3. Grilled items track their heat status to see how far along they are to be considered well done / burnt.

But one might also see two problems:

1. Many Solution Based Recipes share Ingredients. A simple mix reaction would often mess with a players intent.
2. Aside from dough, many solution meals go straight to their output. Naively grinding solids into the solution on the other hand would lose track of player intend if someone tried something like: Cooking Tomato Filled Dumplings in a Tomato Sauce.  

## Introducing the MealContainer (Name Pending)

A Meal container is a simple thing. It holds a solution, describing the hull of the meal (like pancake batter or dough) and other Meal Container. Each container has one type identifier like: RawApple, AppleSlice, AppleJuice, PancakeBatter, Dough. They also have a maximum volume for the sum of the hull+Child Containers. You simply put a meal container into another. Raw Food and Solutions will be converted on the spot into appropriate containers (with raw foods being ground to solution and assigned a container type matching the food).

Finally a container tracks any heat imparted on it either directly or as a child of a larger MealContainer-Tree, which is put against the solution / container type to determine how well cooked the container is.

Evaluating now a meal is done by checking all possible types of output food for that containers hull type + types of the child containers. With containers being able to have a fuzzy list of output types, which only gets cut down as we search for the best possible match to our recipe database until the whole tree is evaluated.

Eating from a meal container gives pieces from each solution equally for base nutritional value + other metabolism effects. While actual meal type might incur additional benefits.

## Whisking Reactions and Baking Solutions

This takes care of the aforementioned issue of tracking player intend when it comes to the many very similar baking bases. To signal the engine that a player wants to make waffles rather than pancakes, they whisk the solution now, much like a bartender uses shake or stir action for some reactions. In this case creating a specific baking solution. Now to add some freedom to making batter, pie dough, etc. I propose to have each whisking reacting have a bit of fuzziness to the ratios. If you make a more dry dough it may be able to hold more items, but loose some taste. While liquids allow ingredients to shine through at the cost of capacity. Now since someone might want to adjust their baking solution by adding more flour after whisking or otherwise mess with the liquid somehow, we track for a baking solution its makeup as ReagentData. Only once we create the MealContainer is this meta-data turned into the necessary parameter for the Meal Container.

## Kitchenware

While from a technical standpoint nothing stands in the way of using a bowl or plate sufficiently setup to hold a meal container (and be setup from pancake batter solution to create one in the first place), it should be much more enjoyable to have proper pans and pots. If enforcing some rules about how you can make a pancake not in a pie tin are necessary, I would propose Metamorphic Kitchenware. Basically you pour in a solution or put something like a dough slice in and based of its type it becomes a pie tin, muffin tin, pan, pot or any other kitchenware with a ready made initial meal container each with appropriate allowed volume and all. This allows us to clearly delineate the type of food being made from its base (pancake, soup, muffin, cookie) for both the engine (evaluation) and player (visual cue).

## Tangent: Making a Salad and other Weird Interactions.

Bowls have a default Meal Container which can be filled with all sorts of items. If a knives is applied, it will turn said container type from something like EmptyBowl to SaladBowl. Similiar actions can happen to make Stuffed Pizza, Multi-Layer Pies by executing a specific combine between a tool or two meal containers.

## How to Finish A Meal (Evaluation)

A meal is never really done. The only exception are specific actions such as slicing cake or pizza into pieces. Whenever adding a new container or heating it, its content get evaluated over again:

1. As heat is added to containers they flag themselves (not their children) as either burned, well done or raw. When evaluating a tree, and we find a burned child, the whole tree is usually considered burned as well. For raw this is more tricky since salads are usually raw.
2. Each nodes possible outcomes are tracked using the hull type.
3. We do a wave form collapse from the top down by locking down the best possible actual allowed top node type (if we considered the possible child node types and each combination including their state of cooked-ness), collapsing the children in the process, who then collapse down.
4. From this we can now derive description like: This pizza is topped with a deep fried salad containing a skwered xeno meat and pineapple with pancake slices dipped in apple sause.
5. Calculate taste store by traveling through the tree checking the base flavor score of the hull type, modified by the ratio to the ideal hull composition and factor in each child container’s value based on the actual types rules.
6. This decides sprite and layer configuration, taste and bonus benefits. As far as possible.

## Making a Pancake (With a look under the hood)

1. Put 5 Flour, 5 Milk, 5 Raw Egg into Solution.
2. Whisk to turn into Pancake Batter (missing 1u of Egg we reduce both volume and taste)
3. Pour Batter in Metamorphic Kitchenware.
4. Here we swap to a pan and setup a meal container with the batter as the solution and a volume of 12 (from the ideal 15).
5. Add heat, the container slowly adds cooking points to itself based on the temperature. (watch the sprite to get an idea how the cooking process is coming along)
6. After a while add blueberries. They get turned into juice and put into a container labeled RawBerry, which is added of the pancake container. Here we could add any other ingredient
7. Continue to heat until both the container and the blueberries are well done. The container now changes its appearance and name to blueberry pancake.
8. Now if you want to top it, wait for it to cool and add a non cooked apple sauce to it. In our recipes we can track a cooked pancake with cooked contents and uncooked toppings. This would change the item again. Though for best results, first serving the pancake and then add the topic would allow the multiple layers of food containers and thus is advised, because a recipe could then say: PlateContainer:With Any Pancake + Any Topping → [Best Actual Pancake] Topped with [Best Actual Topping] → Blueberry Pancake topped with Apple Sauce and Cinamon.
9. From here either eat from the pan, transfer to a plate or use Spatula to receive pancake item.
10. The removed blueberry pancake could also be added to another meal.

As we can see here, the process of making a pancake, while a bit more involved than simply pouring everything into a microwave, it now feels more natural? How to make a pancake from batter should be perfectly clear, so aside from teaching the player the particular recipe to make the batter, they should be good to go, learning the rest through trial and error. And this should go for basically all foods. You merely teach how to get a particular meal type started and have the player then free to experiment using two very clear rules: 

1. Manage the Cooking Process to not burn food.
2. You may add food until the meal container is full.

## Some Considerations

* Recipes. Aside from the basics (starters to a meal so to speak), it is unclear how much auto-generated recipes one might want. So additional recipe ideas could be distributed as random literature.
* No Food Microwave Recipes. A lot of them just need the heat which can be tracked separately.

## Implementation Details (Rough Outlines)

* MealContainer. Solution + Child Containers + Cooking Status + Type + Actual Type + Tastiness. 
* MealContainerComponent. Holds a meal container.
* MealContainerSystem. Transfer heat data to containers.
* WhiskerComponent. Flags an item to be able to whisk solutions.
* WhiskingSystem. Applies WhiskingReactions and tracks whisker use.
* WhiskingReaction. Chemical Reaction with fuzzyness
* Baking Reagents. Just a list of new reagents to reflect batter for pancakes and other non solid food starter
* BakingReagentData. Reagent Data to track a baking solutions content, for further reactions or seutp into a meal container.
* MealType + MealRecipes. The typing for containers and how to determine container type from its contents + cooked flag. Also how to represent a meal in description and appearance.
* CookCore. API to handle all meal container aspects.
  * Baking. Extracting container data from a baking reagent data.
  * Setup. Making Meal Containers for doughs or solutions added to kitchenware.
  * Evaluation. Logic to eval a meal container tree for actual type of top item.
  * Serving. Handling meal container splitting into bites/slices.

