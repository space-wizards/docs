# Avali Species Document


| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| NoreUhh | NoreUhh + TBD | :x: No | TBD |

## Overview

This proposal document aims to cover the Avali as a playable round-start species.

The Avali are a small, bird-like, "silly"- looking alien species. With their four big ears, large feathered arms/wings, and feathered tails, they stand out from other species easily at a glance. While the Avali don't have any unique "abilities", they still have many traits that help them stand out from other species, which leads to unique interactions among players.

## Background

The Avali is a widespread, round-start species on many downstream forks. As a result, the Avali have become a popular species choice for many players. This has led to repeated discussions about adding them to upstream time and time again.

The Avali is available on many popular forks, including Starlight, RMC-14, and Harmony. However, each fork's iteration of Avali can differ slightly from the others. The goal of this document is to incorporate unique additions to Avali across different forks and combine them, and to implement some of our own additions, aiming to strengthen upstream by providing new and interesting player interactions with a new species that players can enjoy thematically.

## Features/Design

The Avali stand out as a mostly unique species. While they do share similar "avian" features to the Vox, they differ drastically enough to be a completely separate species from them, especially regarding their mechanics differing vastly from one another.

### Core Visual Elements

Avali are fuzzy, bipedal creatures. The main identifying features of Avali are their four giant ears, large feathered wings, and tails. Avali stand digitigrade and communicate with others using their unique squeaky voices. Like other species with tails, they protrude from their jumpsuits/hardsuits, making them easy to identify. The same can be said of their large, winged feathers, which make them hard to miss. Avali are normally small-statured, but the size of their wings and feathers makes them seem larger than they really are, like an animal with a puffy coat of fur.

### Naming Convention

Avali have straightforward naming conventions. Avali most commonly have singular "exotic" names. However, any naming scheme can be applied to their species.

Some examples of Avali names include: Narodi, Kalomi, Eijuli, Eilan, and Maaka.

### Features Of The Species

#### Preference To Cold

Due to their origins, the Avali have a naturally lower body temperature compared to other species. In addition to their lower body temperature, Avali have razor sharp claws on their feet. This allows them to gain traction on slippery surfaces such as ice or meat flooring, but does not prevent them from slipping from other sources. 

#### Unique Bloodstream

The Avali, like Vox, have anaerobic blood (blue blood). However, unique to Avali, they do not use saline to recover this. Instead, Avali are poisoned by saline and require ammonia as a replacement.

This creates a new interaction with the medbay on every shift, as chemists are now required to make ammonia to treat Avali patients. It also requires medical doctors and anyone who decides to treat an Avali patient to consider this. This doesn't destroy the use of topicals, however, as blood packs will still heal an Avali's blood loss. Not only does this affect crew-sided gameplay, but it also affects antagonistic gameplay. For example, nuclear operatives will now have to take this into account when their corpsman creates medication. Instead of bringing only saline as a cure-all for blood loss, they will have to potentially make ammonia as well and decide who gets what injection.

#### Faster Metabolism

One of the more unique differences between Avali and other species is the speed of their metabolism. In contrast to Arachnids, their metabolism is slightly faster instead of slightly slower. This creates a "double-edged sword" situation for Avali players and those who interact with them. For example, Avali will now heal faster from injected medicines, meaning they could potentially recover more quickly from a fight than other species. However, this comes with its downsides...

Avali are more susceptible to poisoning, as any injected poison is metabolized faster than in the average species. Not only are poisons faster acting on Avali, but overdoses can easily be more lethal. Beneficial chemicals such as Hyperzine/Stimulants will be less effective in Avali patients, as they only produce effects while the user is metabolizing those reagents. The faster a stimulant metabolizes, the less "effective time" the user gets from those chemicals.

When treating Avali patients, medical staff should account for Avali's faster metabolism, as they currently do for Arachnids.

#### Hollow Bones

Avali, like many bird-like creatures, have hollow bones. This makes them slightly more susceptible to brute damage. More specifically, piercing and blunt damage. It also means Avali tend to weigh less than other species. Similar to Dwarves, Avali will not shatter glass tables when vaulting onto them and can also be dragged more easily.

Just like Dwarves, this creates a new antagonist and crew-sided interaction. Being easier to drag means Avali could be kidnapped more easily, or potentially saved by a passerby, due to their lighter weight.

#### Feather Preening

The Avali have a bountiful amount of feathers across their body. This comes to relevance in different scenarios through either combat, detective work, or just as a cosmetic.

When struck in combat with a brute weapon, whether it be getting shot, stabbed, or bludgeoned, the Avali can lose a feather or two. It is not guaranteed, but it is highly likely that during a scuffle with another player, the Avali will emit an audible "squawk" in pain, indicating that they have dropped a feather on the ground. The color of the feather is dependent on the player themselves. These feathers can come into play during detective work, whether it be helping support/corroborate a story or it being used to frame someone else for a supposed "assault". These feathers leave DNA evidence when scanned, which can easily connect the feather to its owner. If not used in detective work, they can be worn as a cosmetic item, similar to the hair flower and other such cosmetics.

When it comes to detective/security work, dropped feathers can either help confirm you are innocent or potentially serve as a piece of evidence and help prove you are guilty of a crime. If you are an antagonist that has recently gotten into a fight, it can be quite important to ensure you leave behind no evidence, lest you want security to use it against you.

Avali players can also choose to preen themselves every few minutes, allowing them to pluck off a feather from their body for them to use. This helps to ensure that finding feathers isn't always a guaranteed connection in crimes and allows for some wiggle room with sec.

# Technical Considerations

There are some considerations to keep in mind when importing Avali from downstream.

#### Licensing

When porting Avali from downstream forks, licensing, permissions, and attributions must be considered.

Issues with permissions, attributions, and licensing are highly unlikely to arise during the actual implementation of the species. Code owners and asset owners will be contacted regarding their current downstream implementations and the request to move them upstream.

Features not shown from downstream can be implemented easily and should cause no performance or moderation/admin issues.
