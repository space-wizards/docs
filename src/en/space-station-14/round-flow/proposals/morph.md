# The Morph Antagonist

| Designers            | Implemented | GitHub Links |
|----------------------|-------------|--------------|
| Goldminermac    | :x: No      | TBD          |

## Overview

The Morph is a failed bioweapons experiment. It is able to mimic the appearance of any creature or object, but is extremely unstable. Despite being dumped by its creators for being uncontrollable, a small part of its original programming still remains - the urge to absorb genes and remain hidden.

## Background

Currently, the antagonist variety in SS14 is pretty low, especially non-human ones. The Morph's focus on stealth instead of overwhelming brute force like the Rat King would make it a fun role to both play and play against.

This implementation of The Morph is inspired by, but not directly based on any specific Morph version from SS13.

## Spawning
The Morph is a minor antagonist and does not spawn at round start.

### Random Event
A random event can occur that spawns a ghost-role Morph floating outside of the station.

### Morphing Serum
A new item called the Morphing Serum could be used to transform a player into a Morph by injecting it. It is uncraftable, but could be found in some salvage ruins.

## Mechanics

### Surviving Space
The Morph does not need to breathe, is immune to low pressure, and comfortable in any temperature. This makes the Morph incredibly robust (pun intended) and able to survive in the vacuum of space, or spaced areas.

### Hunger
The Morph is ravenously hungry and must constantly eat to not starve to death. It can eat any food item along with consuming corpses.

### Genes
The Morph's original purpose was to collect the genes of specific targets by consuming and absorbing them. Genes are a resource the Morph can collect by consuming the corpses of living creatures, proportional to the size of the corpses.

### Speech
The Morph is able to speak, but their speech is noticibly degenerated which makes it difficult to communicate and will likely give them away as a Morph.

### Combat
The Morph has a powerful melee attack, but is slow enough to be easily evaded. Along with this, the Morph is not very durable and can be easily defeated by a group of attackers or someone heavily armed.

### Navigation
When in its natural form, The Morph can move under door, granting it a large freedom of movement. The need to be untransformed to do so does mean it needs to drop its disguise in order to enter secure areas however.

## Abilities

### Imitation
The Morph can use the imitation ability at any time to transform. The player can click on any object on screen and change their sprite to match it after a short delay. This includes inanimate objects, structures, and living creatures.

The Morph cannot use any abilities while transformed, and will need to de-transform in order to do so. The Morph is able to move while transformed, even while disguised as inanimate objects which will likely reveal their true nature to any observers.

Mimicking an object is purely visual, The Morph does not gain any abilities or properties from the things it imitates, even living creatures with equipment.

### Immobilizing Spit
For a small genes cost, The Morph has the ability to spawn a projectile. Anyone hit by the spit will be greatly slower for a short time, allowing The Morph to catch up to them. It has a very long cooldown which means it must be used sparingly and cautiously.

### Calcify
For a moderate genes cost, The Morph can harden its body for a short time, greatly reducing incoming piercing damage. This ability is intended as a panic button to stop a Morph from dying immediately when attacked by security or other other armed opponents. The hardening only gives resistance against piercing damage, The Morph can still be easily killed by melee or other damage methods, encouraging creativity on the crew's part in dealing with it.

### Mitosis
For a high genes cost, The Morph can create a Morph Cocoon structure. This structure can be occupied by a ghost player who will have the ability to hatch at any time to become another Morph. This Morph will have the exact same abilities as the original.

## Core Gameplay Loop

As a minor antagonist, The Morph does not have any real objectives. Its ultimate goal however is to survive until the end of the round and escape on the shuttle.

The hunger mechanic means that a Morph player must constantly hunt down sustenance to not starve to death in order to even survive for that long. A passive player can decide to survive without harming anyone however, and may even be able to co-exist with the crew if found out, like the many friendly Rat Kings seen online.

If a Morph player wishes to take an active role as an antagonist their abilities give them lots of options. The Morph is specialized to ambush lone targets, so it is right at home stalking through the maintenance tunnels and abandoned parts of the station, picking off patrolling secoffs, antags, and greytiders.

An extremely effective Morph player can even achieve a win condition of sorts by using the mitosis ability to spawn more Morphs, infesting the station. This will take a lot of time and effort to accomplish however, and will make the round more engaging as every new Morph will give a dead player something to do.

## Adjacent Features

### Vent Crawling
When a vent crawling system is added, the Morph will greatly benefit from being able to do so.

### Genetics
When the Genetics Department of science is implemented, a way to create the Morphing Serum through it should be added.
