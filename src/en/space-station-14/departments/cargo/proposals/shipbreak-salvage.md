# Shipbreak Salvage Proposal

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| SlamBamActionman | SlamBamActionman et al. | :x: No | TBD |

## Overview

Shipbreak Salvage (or BreakSalv) is a new primary gameplay loop intended to act as Salvage's main method  Salvage focusing on physically pulling in wrecks of old shuttles to the station with the goal to extract unique resources and large volumes of common materials. 

## Background

Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game.

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.

## Features to be added

Give a description of what game mechanics you would like to add or change. This should be a general overview, with enough details on critical design points that someone can directly implement the feature from this design document. Exact numbers for game balance however are not necessary, as these can be adjusted later either during development or after it has been implemented, but mention *what* will have to be balanced and what needs to be considered when doing so.

BreakSalv is intended to take place on the outside rim of the space station, leveraging the free empty space to spawn in shuttles for resource extraction.  with station-bound machinery in a way that is unique to the department. 

BreakSalv has a gameplay loop that can be broken up in three primary parts: retrieval, extraction and shredding. 

### Retrieval

**Retrieval** is the process of spawning and getting wrecks to the station so that their resources can be extracted.

Wrecks are pre-made grids themed around being a decommissioned shuttle or destroyed station section. To get access to wrecks, Salvage has access to a unique console called the _Salvage Magnet_. 

#### Salvage Magnet

The Salvage Magnet (or just magnet) provides an interface where Salvagers can select one of a small selection of wrecks that they want to work on called the "Wreck Selection" view. Each entry lists information of what type of wreck it is and what resources are expected to be found on it.

One of the key pieces of information listed in a magnet entry is the _wreck type_ the wreck is. Types describe some sort of environmental hazard or property of the wreck, providing challenges unique to the wreck type and gives Salvagers variety and choice in the wreck they want work on.

Some examples of wreck types:

- **Superheated:** Contains compartments with superheated plasma actively on fire. These must be vented into space before being accessed.
- **Infested:** Contains a large number of space mobs that will attack the Salvagers.
- **Overgrown:** Kudzu covers the wreck, along with trees blocking pathways.
- **Radioactive:** Contains a large number of radioactive objects that require quick removal.
- **Defended:** Contains dangerous turrets (ballistic and/or laser) and mines that must be disposed of.
- **Shadowy:** Covered in the visually obscuring shadow anomaly fog that has to be navigated or removed via flashes.
- **Fortified:** Contains powered access-locked and high-security airlocks with strong walls. These must be hacked or destroyed to reach the resources inside.
- **Distant:** Spawns at a further distance away from the station than normal. Jetpack recommended.

Only one wreck may be active with the magnet at any given time. Once a wreck has been selected the interface changes to a new view as described in the [Magnet Evaluation](#magnet-evaluation) section.

#### Towing

Once a wreck has been spawned, it will be located somewhere in nearby space in close proximity to the Salvage Bay. If the wreck is not within the player's viewing distance, Salvage may use a _Mass Scanner_ mapped in the Bay to locate it. Regardless, Salvage will want to move the wreck closer to the station as it will make it faster to extract materials from it and is a necessity to complete later steps. This is known as _towing_.

To tow the wreck, Salvage will have access to _grappling hooks_ and _magboots_. While grappling hooks on their own simply drag the user towards the hook, when combined with the grounding force of the magboots Salvagers are able to pull grids towards each other (or in the case one has a station anchor, only the one without gets pulled). Ideally Salvage will be able to stand on the outer rim of the station and use their grappling hooks to drag the wreck until it is within working distance; once it is, they can proceed with the next step.

### Extraction

**Extraction** is the process of manually retrieving rare materials from wrecks.

On the wrecks there will be resources of various kinds that Salvage will want to move off the wreck and onto the station by going onto the wreck and picking them up by hand. In its simplest form this may be a stack of material, but where the extraction process becomes more interesting is the unique _wreck resources_ that may spawn on wrecks. 

#### Wreck Resources

No one wreck will contain all types of wreck resources and generally these should be flavored around the wreck. The Salvage magnet may indicate that a wreck will be specialized in a type of wreck resource.
TODO: Move above to the magnet section.

Wreck resources are scraps, technology gadgets, structures and hazardous containers containing rare materials. Salvage will want to remove these from the wrecks before the scrunching step takes place to ensure a high material yield and/or prevent damage to the Salvage Bay. 

Wreck resources can not directly be used as materials but need to be processed first. The _recycler_ is a good option for this as it is a station-mounted machine and Salvage can easily have their own. As a rule, wreck resources should _not_ focus on steel or glass materials, since those are primarily obtained through the scrunching step.  

- **Two-handed:** Requires two hands to pick up. 
- **Large:** Big enough to require dragging and can't be held or put in containers.
- **Fragile:** Easily broken if thrown around recklessly.
- **Radioactive:** Emits radiation.
- **Mounted:** Attached to a wall or integrated into some machinery that requires partial deconstruction.
- **Electrically Unstable:** If destroyed or processed incorrectly, will emit an EMP pulse.
- **Explosive:** If destroyed or processed incorrectly, will explode.
- TODO: More!!

### Shredding

**Shredding** is the process of finalizing a salvage operation by grinding up the remains of a wreck into base materials.

Once all valuable wreck resources have been extracted and the Salvagers feel finished with the wreck, it is time to get rid of the wreck itself. For this, the Salvage Bay has a large wall of _industrial shredders_ and _separation charges_.

#### Industrial Shredders

Industrial shredders work by grinding up any tile that comes in contact with the open front of the machine, destroying it and any structure attached. It is essentially a recycler but specializing in grids. As wrecks are mostly made up of metal and glass parts, this becomes the main method Salvage produces steel and glass sheets. To prevent Salvage from simply sending a fresh wreck straight into the industrial shredders they provide a remarkably lower yield for wreck resources and items that can already be recycled, and some wreck resources may harm the shredders if inserted into them.

Since some individual grid tiles could feasibly be made with less than one sheet of steel material, those tiles only have a percentage chance to produce a sheet. E.g. lattice, which is made of 1 steel rod (equivalent to 0.5 steel sheet) has a 50% to produce a sheet.

Each shredder acts as a conveyor belt that is only able to push items perpendicular to its opening; since each Salvage Bay is meant to have a line of shredders this means the material can travel along the line to a pick-up location (either in the Bay or in Cargo proper). *Shredders are only active* when there is an active wreck being worked on via the magnet and turn on/off via device linking to it.

Shredders do not have the safety mechanism of recyclers which means they deal contact damage, but the damage is low enough that it isn't an efficient method of murder. You wouldn't want to stand or walk through a shredder for a long duration but just touching it for a few seconds won't be lethal.

#### Separation Charges

Some wrecks will simply be too large to fit into the Salvage Bay and the shredder wall. Salvage will be tasked to split these wrecks into smaller parts using a new tool called separation charges. These act similar to cables but are placed on the edges of tiles and when activated split the grid into two parts, similar to how an RCD can separate grids. This split is accompanied by a small spark (not an explosion!) and a small push force separating the grids. Large wrecks should be designed with this functionality and in some places have pre-defined ideal spots to place charges.

Separation charges will only activate if the line they create fully separates the two parts of the grid from each other. If the charges do not form a full cut across the grid or there are other sections still connecting the parts together, the charges fail to activate. Since separation charges have potential for some pretty strong antagonistic plays, such as disconnecting vital station sections, placing a single separation charge has a fairly lengthy do-after. 

It's recommended (but not required) that _weld charges_ are implemented as well, that act opposite to separation charges and give the ability to attach grids together. These would work well as an Engineering tool and/or part of the RCD.

#### Magnet Evaluation

The final part of the BreakSalv loop is Salvage returning to the magnet and getting an evaluation of their work.

While a wreck is being worked on the magnet interface displays a "Magnet Evaluation" view with the following information:

- **Wreck Percentage:** Percentage of how much of the spawned wreck grid has been processed; 0% means all grid tiles remain, 100% means no grid tiles remain.
- **Shredder Efficiency:** Efficiency of connected industrial shredders. This is calculated based on whether the shredders have processed any entities that they give lower yield for, such as wreck resources.
- **Wreck Time:** Time since magnet pull started.

After some time has passed (short enough to not feel restrictive, but long enough that Salvage can't just cycle wrecks), Salvagers may choose to despawn any remaining grids of their wreck using a "Despawn Wreck" button on the magnet, but there is an incentive to fully shred the wreck. If the Wreck Percentage is at 100% a previously greyed out button "Claim Processing Reward" becomes available. Clicking this button rewards Cargo with a monetary boost and announces in the Supply channel that Salvage finished processing the wreck along with the Shredder Efficiency and Wreck Time. 

Once either button has been pressed the magnet interface returns to the wreck selection view (after a short delay to give a moment to breathe) and Salvage is free to select a new wreck to work on.

### Salvage Progression

As some wrecks will contain useful tools and equipment to better deal with the three core parts of BreakSalv, there should be a natural progression inherent to Salvage's gameplay. Science may also provide upgraded tools through research and usage of Salvage's materials. Some wrecks will likely be discouraged by being too dangerous or slow to process without these upgrades, lending to a sense of becoming more powerful over the round.

As a way to add further progression and provide some breathing room for Salvage, BreakSalv also features an upgrade to the salvage magnet's capabilities. This unlocks after Salvage has a certain number of 100% Wreck Percentage completions in the form of a greyed out "Magnet Upgrade" button in the wreck selection view becoming available. Pressing this starts a fairly lenghty progress bar during which no new wrecks can be selected. Salvagers are encouraged to spend this time taking a break on the station and/or visiting the other departments for upgrades.

Once the progress bar has completed the Salvagers are rewarded with a new wreck option in the wreck selection view that features a higher tier of wreck. These higher tiers are intended to be more challenging by featuring multiple wreck types, more resources and are generally larger.

## Game Design Rationale

BreakSalv is intends to position Salvage as a primary resource generator for the station by utilizing the unique game mechanics opportunities afforded by working on the outside of the station. 

BreakSalv intends to provide the following experience:
- Hard work not for the faint of heart under a sci-fi megacorp industrial aesthetic. Salvagers should feel like they are cool by braving the dangers and efforts inherent to their job.
- Visible results from their work. Seeing a huge pile of materials come out of the shredders should make the Salvagers feel like they are contributing to the station.
- Completionism and optimization. Salvagers will want to hit 100% on the Wreck Percentage with high Shredder Efficiency and low Wreck Time, but may situationally forgo it for a faster, lower reward. Good Salvagers can brag about how fast they completed a wreck.
- Moments of rest. Since all Salvage work consists of constant manual effort, salvagers shouldn't be stressed into continuously working by always having high-value work available.

There are a few things that BreakSalv is intentionally trying to avoid:
- Isolationism. While Salvage operates on the outside of the station, since the focus is on magnet wrecks and the shredders Salvagers do not have much reason to leave the station proper. At worst a Salvage team may occasionally need to leave the station grid to retrieve a wreck that has spawned further out, but this is only intended to be a temporary excursion lasting for the duration to get out there and towing it back. Salvage should be expected to be found in the Salvage Bay for the majority of the round. 
-  Easy sabotage/round removal features. BreakSalv doesn't intend to solve the strategy of just yeeting a dying body into space, but otherwise the equipment used for BreakSalv shouldn't be highly efficient antagonist/griefing strategies. The industrial shredders can damage things but aren't as useful as just stabbing someone with a Syndicate weapon, and the separation charges should be as easy to interupt as trying to disconnect a grid using an RCD. 

Consider addressing:
- How does the feature align with our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosphy?
- What makes this feature enjoyable or rewarding for players?
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- How does it enhance player cooperation, competition, or emergent gameplay?
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?

## Roundflow & Player interaction

Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
- Which department will interact with the feature? How does the feature fit into the [design document](../space-station-14/departments.md) for that department?

## Administrative & Server Rule Impact (if applicable)

- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
- How are the rules enforced mechanically by way the feature will be implemented?

# Technical Considerations

- Does the feature require new systems, UI elements, or refactors of existing ones? Give a short technical outline on how they will be implemented.
- Are there any anticipated performance impacts?
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)

## Further Embodiments

There are a few ways that BreakSalv can be expanded upon. These are not necessarily part of the base implementation but may be worth exploring in the future:
- A stationary "spear gun" turret stationed in the Salvage Bay that Salvagers manually control to hook into wrecks that are too far for their grappling hooks.
