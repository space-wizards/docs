# Cyborg Whitelisted 'Hands'

| Designers  | Implemented | GitHub Links                                                              |
|------------|-------------|---------------------------------------------------------------------------|
| ThatGuyUSA | YES         | [PR #38668](https://github.com/space-wizards/space-station-14/pull/38668) |

## What are whitelisted Cyborg 'hand' slots?

Whitelisted hand slots are the solution to future proofing Cyborg inventories.

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

## What a whitelisted 'hand' slot IS:

- A way to compliment and empower Cyborg's embedded toolkit.

- A way to condense cluttered modules by merging redundant slots together.

## What a whitelisted 'hand' slot ISN'T:

- A fully identical, normal hand but on a Cyborg instead.

- A shortcut to alleviate or negate a Cyborg's inventory restrictions.