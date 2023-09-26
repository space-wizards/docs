# Hunger/Thirst [Carbonhell, Unapproved]

# Current system

The current hunger and thirst system, as of right now (2022-11-30) is based on a penalty given if players do not remember to replenish themself with food and drinks.
This can imply some social gameplay such as a crewmember going to the kitchen and asking the chef for food, same for the bartender, but in practice it negates any social behaviour due to the amount of vending machines available on all station maps.
There is zero benefit on the chef doing his job versus just using said vending machines, or even just drinking water from water tanks or sinks. This causes the system to become a chore for the player, rather than something that increases interaction and fun between the players.

# Proposed system
The proposed system shifts the basic principle behind hunger and thirst from penalizing players ignoring it, to incentivizing players playing along with it in a social way.
The system is based on the currently existing flavor mechanic, where eating or drinking a certain consumable notifies the player of the consumable's flavor ("Tastes like bread" and so on). A specific player will have his own preferred flavors cycle multiple times in a round. Satisfying your own preferred flavor awards you with a small bonus, in the form of a boost of a certain statistic for example (movement speed, melee damage, armor and so on). Ignoring the system altogether does not penalize the player in any way, other than possibly being at a disvantage in certain situations (combat for example, if you're against someone who's well fed and has some combat related bonuses).
The system also favors the production of specific, single consumable types for player, instead of mass producing food to give players enough nutriments. This has the small benefit of reducing entities (instead of having 50 pizza slices hanging around for the random passing greytider to hoard, you'd probably cook specific requests and deliver them to the requester).
The document will analyze food in detail but the same exact idea can be applied to drinks with no specific implementation.

# Subsystems
## Flavors - food
Food items, code wise, already have flavors implemented for them through the FlavorProfile component. The idea is to reuse that, perhaps by expanding so to add more granular flavors to the various existing ingredients.
Basic food items such as ones that require little to no crafting would usually have one or at most two flavors. An example of this could be meat (meat flavor), botany plants ("banana" for banana, and so on...).
Any crafted food item will inherit the flavors of all the base ingredients used during crafting.

## Flavors - players
Players spawn initially with multiple sets of preferred flavors, > 1 to allow the system to be slightly more flexible by giving the chef some freedom.
The preferred flavors have a timer attached to them, which should last long enough to give the chef more than enough time to prepare the food that fits the criteria, but it should also give some sense of urgency to both make the social interaction between players and the chef more frequent, and to also lower powergaming by avoiding players stockpiling their preferred food to use in specific situations. This timer should only be hinted to the player, for example one minute before it runs out by notifying something along the lines of "You're growing tired of \<insert flavor here\>..."
Satisfying a flavor should grant a bonus and mark the flavors as "satisfied". This means the player still has to wait for the timer for the preferred flavors to refresh and to gain another bonus again. This can have interesting implications ingame, such as players considering which might be the best time to consume food (before a dangerous/combat situation perhaps?).
To entice the chefs/bartenders to craft more complex food/drinks, the system should only grant the bonus if the player consumes a food type that satisfies all the flavors of one of his preferred flavor sets.

### Example
- Player John spawns with the following flavor sets:
```
{
    {
        bun,
        leafy,
        metallic
    },
    {
        oily,
        cheesy,
        bread
    }
}
```

- John probably has no clue about how the system works. He goes to the kitchen and notifies the chef he would like something with bun, leafy and metallic flavor.
He also notifies that he might like something with the flavors of eggplant, corn, tomato, oily, cheesy, and bread.
- The chef collects the order, along with the others. After deciding which of the set he can fulfill based on ingredient availability, complexity and time, he decides to go with the second set.
- Thanks to ~~the wiki~~ ~~some manual he found in the back of the freezer~~ his immense knowledge of all types of food, he realizes any pizza will fit the required criteria.
- The chef thus decides to cook a simple margherita for the customer. The customer eats the pizza and gets a random bonus.
- After X minutes, regardless of whether he actually satisfied his preferred flavors or not, the flavors refresh and the flow restarts.

## Flavors - bonuses
Consuming a food which fits the flavors the player wishes for should grant a random bonus, picked from a pool of bonuses. The bonuses chosen should be good enough to warrant the players being aware of it, therefore they should also be generic enough to apply for any activity the player may do during a round. It would also be nice for critical roles to be even more aware about this system, for example the security team or the heads of staff.
Possible bonuses (arbitrary and most likely subject to change) could be:
- Movement boost (random on gain 2% - 5%).
- Armor up (+2-+5 armor points for a random damage type).
- Quickness up (reduce the time to do doafters, this might be complex to do codewise though?)
- Damage up (+1-+3 damage points when damaging something)
Since only one set of preferred flavors can be satisfied at once, only one bonus can be active at a time. To allow both the chefs and the bartenders to engage with players, though, the system should allow players to satisfy food-related flavors and drink-related flavors separately.

# Possible improvements
Here we list ideas that could futher improve the system but which would better be implemented after the initial idea is confirmed to work in game.

## Different difficulty for flavor sets
Instead of treating the various random flavor sets equally, a difficulty value can be assigned to them. This can either be explicit (calculated by some mean) or implicit (for example, simply the number of flavors in the set). A higher difficulty would imply a better bonus, so that the player would actually need to think twice about which flavor set to ask the chef to fulfill.

## Specific flavors for complex consumables
Instead of simply having complex consumables inherit the flavors of their ingredients, they could also add special ones. An example would be pizzas having a "pizza" flavor, to slightly limit the freedom of the chef to ensure more complex food is used every once in a while.
This might not be needed if the flavor set generator and the flavors of each food item are carefully picked though.
