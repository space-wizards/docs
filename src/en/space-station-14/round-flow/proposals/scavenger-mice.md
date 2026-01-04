# Scavenger Mice
<!-- Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar. -->

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| DigitalThaumaturge | DigitalThaumaturge | :x: No | TBD |

<!--
`Designers` should be the names that you use on GitHub and/or Discord. This is optional but strongly recommended, since:

- This acknowledges credit where it is due
- People who are confused about the written intent can use this information to contact the authors

`Implemented` is the status of the feature.

Github links can include multiple PRs, if relevant.
-->

## Overview

New minor antagonist ghost-role that steals station resources in order to evolve and gain functional hands.

<!-- A very short, maybe three sentence summary of what this proposal is about. A high level "overview" or "what this adds". -->

## Background

Mostly based upon the concept of the "loot goblin," enemies in video games (especially RPGs) that exist to steal valuable items, but drop everything they've stolen and then some if they are killed.

Currently, in SS14, players are desperate for more interesting ghost roles. That's a major reason why getting round removed is such a problem: there's just not enough unique ghost roles to go around.

In addition, none of the round-start antagonists currently in the game tend to cause trouble within the first 15 minutes of a round; they always end up being too busy planning, or are gathering resources to make their attack later. A small-scale antagonist that inconveniences the crew by depriving them of generic but valuable resources and running away would be a low-stakes way to add some spice to roundstart.

<!--
Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game.

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.
-->

## Features to be added
A new minor antagonist mob, the Scavenger.

Scavengers are large mice about the same size as an ancestor species, but smaller than a Rat King. However, they share some traits with a Rat King: the ability to scurry under doors, the ability to talk (with a similar accent), the Rat King's Domain ability (allowing them to recover injuries), and similar amounts of health. However, they are slightly slower than normal crew, and have all the combat incapability of a normal mouse.

Unlike most ghost roles, a scavenger ghost role has a chance of opening on roundstart, allowing them to be a very early round "threat."

Scavengers visibly carry around a large sack, hinting at both their modus operandi, and the reward for killing them.

Scavengers have a simple objective: steal enough materials, spesos, and/or food to evolve. Interacting with these objects stores them inside the Scavenger, and awards the scavenger with points toward evolution. When enough combined materials, spesos, and/or food has been collected, the Scavenger automatically evolves.
- Spesos: 10,000 spesos alone would be enough for the scavenger to evolve.
- Materials: The scavenger would have to collect about 10 full stacks of materials to evolve. Points would not be based on rarity (Diamonds being no better than steel).
- Food: Does not provide much points. Mostly used to supplement the other point sources.

Scavengers do not have hands, having a similar interaction range as cyborgs, meaning they can use lathes, computers, and vending machines. They have a unique interaction with request computers, however, as interacting with a request computer will make it withdraw 250 spesos, with a short cooldown between withdrawals.

When a Scavenger evolves, it immediately loses the ability to steal, but gains hands, pockets, and storage slots equivalent to a normal crewmember. It also gains clothing slots equivalent to an ancestor species. After evolving, Scavengers become free agents.

If a Scavenger is killed and butchered, they drop:
- Three pieces of raw rat meat
- All stolen items
- Additional spesos and materials
- A few pieces of random loot, such as toys or maintenance loot
- A Scavenger Sack

### Scavenger Sack
Scavenger Sacks are storage items with slightly more grid space than a dufflebag, but no movement penalty. These are the main loot for killing a scavenger. Upon evolving, a Scavenger Sack is put into the Scavenger's backpack slot, and it cannot be removed without butchering the Scavenger.

<!-- Give a description of what game mechanics you would like to add or change. This should be a general overview, with enough details on critical design points that someone can directly implement the feature from this design document. Exact numbers for game balance however are not necessary, as these can be adjusted later either during development or after it has been implemented, but mention *what* will have to be balanced and what needs to be considered when doing so. -->

## Game Design Rationale

The Scavenger is a classic "loot goblin:" able to steal valauble resources and run away with them, but can't fight, is instantly valid to kill, and gives back everything it stole (and more) if killed, with a nicer dufflebag as an additional reward.

However, if a Scavenger does manage to survive and thrive long enough to evolve (which should be hard, considering how much the crew hates regular mice) it becomes a fearsome free agent, as it now has hands AND the ability to scurry under doors. Much like a Rat King, many will be easily dealt with early on, but the ones that don't can become a real menance.

<!--
Consider addressing:
- How does the feature align with our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosphy?
- What makes this feature enjoyable or rewarding for players?
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- How does it enhance player cooperation, competition, or emergent gameplay?
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?
-->

## Roundflow & Player interaction

Scavengers are a minor antagonist, but with the unique distinction of sometimes spawning roundstart. This should allow them to serve as a "warm-up" for more dangerous threats.

Scavengers should play like an extreme version of the mouse: having similar tools and goals, but with a much greater risk of having angry crewmembers chase you down. Seeing as they are not protected in any form by space law, and give useful rewards when butchered, they will likely be beaten to death on sight if they do not play carefully. 

Scavengers would likely be able to interact with any department they wish: every department has a request computer that a Scavenger might try to target and a lathe (or store of food, in Service's case) that can be stolen from. Given their pest mobility, they might feasibly end up interacting with the whole station.

<!--
Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
- Which department will interact with the feature? How does the feature fit into the [design document](../space-station-14/departments.md) for that department?
-->

## Administrative & Server Rule Impact (if applicable)

Scavengers should have no more impact than that of the other free agents currently in the game. There is nothing a Scavenger could do that a Skeleton could not do with a little more effort.

<!--
- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
- How are the rules enforced mechanically by way the feature will be implemented?
-->

# Technical Considerations

Some C# will likely be required for tracking evolution points, as well as allowing scavengers to store steal objectives and directly withdraw from request computers. Everything else can probably be done through YAML. 

<!--
- Are there any anticipated performance impacts?
- Does the feature require new systems, UI elements, or refactors of existing ones?
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
-->