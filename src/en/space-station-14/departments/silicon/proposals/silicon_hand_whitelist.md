# Cyborg Whitelisted 'Hands'

| Designers  | Implemented | GitHub Links                                                              |
|------------|-------------|---------------------------------------------------------------------------|
| ThatGuyUSA | YES         | [PR #38668](https://github.com/space-wizards/space-station-14/pull/38668) |

## What are whitelisted Cyborg 'hand' slots?

Whitelisted 'hand' slots are the solution to future proofing Cyborg inventories.

Essentially it is a traditional 'hand' you would find on a humanoid, that can only hold items of the corresponding tag or component that we tell it to.

## Before its implementation

Cyborgs were given 'empty stack' prototypes that could exclusively hold the item assigned to it.

Before [PR #38668](https://github.com/space-wizards/space-station-14/pull/38668), Cyborgs were given slots that could only hold one specific item, indicated by a silhouette of that item. It had a shortcoming of scaling terribly, making for a poor user experience the more 'hands' someone had to interface with in a single module.

If a Cyborg wanted to hold reinforced uranium glass, a `reinforced uranium glass hand` would have been created to be placed into a module. While it accomplished what we needed, it would a huge commitment for an uncommon material that one might not even interact with in most rounds.

Due to how Cyborgs navigate their inventory, swapping between larger lists of slots and tools can become tedious quickly leading to a diminished user experience.

## Implementation

Whitelisted Cyborg 'hands' aim to generalize things a cyborg can hold utilizing Tags and Components, while still limiting their freedom.

Instead of having one slot each for gauze, bruise packs, and ointment, you have 3 slots that can hold any topical medication. If someone wants to exclusively stack up on gauze and blood packs, they may do so as they please.

This allows the Cyborg player to fill their inventory to better suit their needs, while maintaining the restrictions of whatever module the hand is part of.

## Empowering embedded tools

Embedded tools should not be obsoleted by 'hands', they should compliment each other's existence.

The centerpiece of a cyborg module should never be the 'hands', the embedded tools should be the main reason a Cyborg would want a certain module. It is important for keeping Cyborgs exclusive tools the reason a player would want to be a Cyborg.

If the 'hands' are too versatile, then it undermines the limitations of being a Cyborg. For this reason they must be limited in what they can carry. If a Cyborg needs to carry tools it is preferred they are made into embedded slots rather than whitelisted 'hands'.

## Broad categories

Whitelisted items for slots must be contextually related.

If there are too many options in a category to make into embedded slots, whitelisted slots may be used in place of them. However, the items must be related both functionally and contextually.

Giving a Cyborg a "machine construction" 'hand' that can hold machine parts, all cable types, batteries, igniters, and beakers may seem like a good idea as they are all related to constructing / upgrading machines. But giving the slot so much versatility has inadvertently made other modules redundant. 

That slot can pour drinks, splash people, lay cables, and replace batteries in devices. Some of which have entire modules centered around doing so, such as the wiring module. It is a common pitfall to make a 'hand' overly useful, so development should be done with extreme caution.

## Dos and Don'ts

### What whitelisted 'hands' should be:

- A slot that can hold produce and seeds.

- A slot that can only hold various types of glass.

- A slot that can exclusively hold gardening tools.

### What a whitelisted 'hand' SHOULDN'T be:

- A functionally identical, and nearly indistinguishable single humanoid hand.

- A slot that can hold all construction materials ranging from Wood to Uranium.

- A slot that can hold functionally similar but very unrelated things, such as both knives and swords.