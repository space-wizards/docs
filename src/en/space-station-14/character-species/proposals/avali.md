# Avali Species Document


| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| NoreUhh | NoreUhh + TBD | :x: No | TBD |

## Overview

This proposal document aims to cover the Avali as a playable round-start species.

The Avali are a small-statured, "silly" bird-like alien species with a very distinctive look. With their 4 big ears, large feathered arms/wings, and feathered tails, they stand out from other species easily at a glance. While the Avali don't have any unique "abilities", the Avali still have many traits that help them stand out easily from other species, and that causes unique interactions to happen amongst players.

## Background

The Avali are a very common round-start species on many downstream forks. As a result, the Avali have become a popular species choice for many players. This has led to the discussion of them being added to upstream time and time again.

The Avali can be found on many popular forks such as Starlight, RMC-14, and Harmony, just to name a few. However, each fork's iteration of Avali can differ slightly from the others. The goal of this document is to incorporate unique additions to Avali across different forks and combine them, as well as implement some of our own unique additions, aiming to strengthen upstream by providing new and interesting interactions between players and a new species that players can enjoy thematically.

## Features/Design

The Avali stand out as a mostly unique species. While they do share similar "avian" features to the Vox, they differ drastically enough to be a completely separate species from them, especially in regard to their mechanics differing greatly from one another.

### Core Visual Elements

Avali are fuzzy, bipedal creatures. The main identifying features of Avali are their 4 giant ears, large feathered wings, and tails. Avali stand digitigrade and communicate with others using their unique squeaky voices. Like other species with tails, they protrude from their jumpsuits/hardsuits, making them easy to identify. The same can be said of their large, winged feathers, which make them hard to miss. Avali are normally small-statured, but the size of their wings and feathers makes them seem larger than they really are, like an animal with a puffy coat of fur.

### Naming Convention

Avali have very simple naming conventions. Avali most commonly have singular "exotic" names. However any naming schematic can fit their species.

Some examples of Avali names include: Narodi, Kalomi, Eijuli, Eilan, and Maaka

### Features Of The Species

#### Preference To Cold

The Avali have a naturally lower body temperature compared to other species. This means they prefer colder environments, giving them slight resistance to cold, and that their acceptable temperature range is lower than that of other species. This, along with the fuzz on their bodies, makes them more susceptible to heat damage.

#### Unique Bloodstream

The Avali, like Vox and Arachnids, have anaerobic blood (blue blood). This means their blood is copper-based, not iron-based, requiring copper to replenish blood levels as opposed to iron. However, unique to Avali, they do not use saline to recover this. Instead, Avali are poisoned by saline and require ammonia as a replacement.

This creates a new interaction with the medbay on every shift, as chemists are now required to make ammonia to treat Avali patients. It also requires medical doctors and whoever decides to heal an Avali patient to consider this. This doesn't destroy the use of topicals, however, as blood packs will still heal an Avali's blood loss. Not only does this affect crew-sided gameplay, but it also affects antagonistic gameplay. For example, nuclear operatives will now have to take this into account when their corpsman creates medication. Instead of bringing only saline as a cure-all for blood loss, they will have to potentially make ammonia as well and decide who gets what injection.

#### Faster Metabolism

One of the more unique differences between Avali and other species is the speed of their metabolism. In contrast to Arachnids, their metabolism is slightly faster instead of slightly slower. This creates a "double-edged sword" situation for Avali players and those who interact with them. For example, Avali will now heal faster from injected medicines, meaning they could potentially recover more quickly from a fight than other species. However, this comes with its downsides...

Avali are more susceptible to poisoning, as any poison injected into them will be metabolized faster than in the average species. Not only are poisons faster acting on Avali, but overdoses can easily be more lethal. Beneficial chemicals such as Hyperzine/Stimulants will be less effective in Avali patients, as they only produce effects while the user is metabolizing those reagents. The faster a stimulant metabolizes, the less "effective time" the user gets from those chemicals.

When treating Avali patients, medical staff should take into account the faster metabolism of Avali, as they currently do with Arachnids.

#### Hollow Bones

Avali, like many bird-like creatures, have hollow bones. This makes them slightly more susceptible to brute damage. More specifically, piercing and blunt damage. It also means Avali tend to weigh less than other species. Similar to Dwarves, Avali will not shatter glass tables when vaulting onto them and can also be dragged more easily.

Just like Dwarves, this creates a new antagonist and crew-sided interaction. Being easier to drag means Avali could be kidnapped more easily or potentially saved by a passerby more easily due to their lighter weight.

# Technical Considerations

There are some considerations to make when importing Avali from downstream.

#### Licensing

When porting Avali from downstream forks, licensing, permissions, and attributions must be considered.

Issues with permissions, attributions, and licensing are highly unlikely to arise during the actual implementation of the species. Code owners and asset owners will be contacted regarding their current downstream implementations and how they are requested to be moved upstream as well.

Features not shown from downstream can be implemented easily and should cause no performance or moderation/admin issues.
