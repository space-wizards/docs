# The Space VVitch

| Designers | Implemented | GitHub Links |
|---|---|---|
| 2013HORSEMEATSCANDAL | :x: No | TBD |

## Overview

A stealthier and trickier counterpart to the wizard, the witch has little in the department of flashy spells but has access to a variety of curses, rituals and potions. Her objective is to be respected/feared and curse those who disrespect her. She also spawns in the wizard's den.

## Goals
- A stealthier variant of the wizard, the witch has little offensive magic, instead having to curse her victims.
- Open-ended goals allow for creative approaches.
- RP potential, the witch may decide to open a potion shop or let crewmembers order a hex on someone else.

## Original Mechanics

### Witches's Brew
The witch has a cauldron in her den, which starts furnished with various rare ingredients (Eye of newt, 4-leaf clovers, orichalcum, etc.) which she can use to brew potions, reagents with strange and unique properties such as :

- Potion of Feline Eyes (see in the dark)
- Potion of Astral Projection (briefly become a ghost, without access to deadchat)
- Potion of Wild Growth (Instantly mutates a fully grown plant) 

Some potions may have alternative ingredients the witch can find on the station, encouraging her to explore and forage.

### The Curse

The witch has access to a special type of spells called Curses (or hexes). A curse may only be cast in the witch's ritual circle, which spawns in her den. Casting a curse requires a catalyst, an item with the target's DNA or fingerprints. The witch then selects a curse from her grimoire, using the same currency the wizard uses to buy spells, she then selects a target from a list of DNA on the catalyst. The catalyst then turns into mana dust.
Exemples of curses:

- Curse of Damocles : Makes a sword (or piano/anvil) appear above the target, it has a random chance to fall every minute.

- Curse of Weaponizing : When the targeting spell is cast on someone, the Curse Target will automatically start running towards the victim, no matter where they may be, and attempt to gib them, breaking anything in their way. They regain control upon success or death.

- Curse of Babel : The target no longer understands Galactic Common ! All messages' letters are jumbled!

- Curse of Dust : Target turns food and drink they grab or try to consume into a pile of ash

- Curse of the Dream Demon: Target gains the narcoleptic trait if they don't already have it and a monster spawns whenever they fall asleep.

- Curse of the Martyr : Target takes 25% of all damage inflicted to others around them in their stead.

- Curse of Eternal Darkness : All lightsources the target can see turn themselves off automatically.

A person may only have one curse on them at a time. Only someone who has cast a curse may lift it.

### Burn the Witch !

If the witch dies, she may point to a nearby player and curse them, provided her body is not burned within 5 minutes of her death, which cancels the curse. If this happens, the witch's body explodes into a murder of crows.

## Implementation details

The potion system is basically a reskinned chemistry system. Adding new reagents is all that is needed.

The cursing ritual would have to be coded, although both the DNA and spellcasting systems already exist.

### Ghost role information

The moon is right ! Show these insolent fools the true power of a witch !

### Objectives
- Ensure you are feared and respected.
- Punish those who disrespect you.
