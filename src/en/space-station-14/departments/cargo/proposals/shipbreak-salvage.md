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

BreakSalv has a gameplay loop that can be broken up in three primary parts: retrieval, extraction and scrunching. 

### Retrieval

**Retrieval** is the process of spawning and getting wrecks to the station so that their resources can be extracted.

To get access to wrecks, Salvage has access to a unique console called a _Salvage Magnet_. 

TODO: More sophisticated way of using the magnet than what we currently got.

Once a wreck has been spawned, it will be located somewhere in nearby space in close proximity to the Salvage Bay. If the wreck is not within the player's viewing distance, Salvage may use a _Mass Scanner_ mapped in the Bay to locate it. Regardless, Salvage will want to move the wreck closer to the station as it will make it faster to extract materials from it and is a necessity to complete later steps.

To move the wreck, Salvage will have access to _grappling hooks_ and _magboots_. While grappling hooks on their own simply drag the user towards the hook, when combined with the grounding force of the magboots Salvagers are able to pull grids towards each other (or in the case one has a station anchor, only the one without gets pulled). Ideally Salvage will be able to stand on the outer rim of the station and use their grappling hooks to drag the wreck until it is within working distance; once it is, they can proceed with the next step.

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

### Scrunching

**Scrunching** is the process of finalizing a salvage operation by grinding up the remains of a wreck into base materials.

Once all valuable wreck resources have been extracted and the Salvagers feel finished with the wreck, it is time to get rid of the wreck itself. For this, the Salvage Bay has a large wall of _industrial shredders_.

Industrial shredders work by grinding up any tile that comes in contact with the open front of the machine, destroying it and any structure attached. It is essentially a recycler but specializing in grids. As wrecks are mostly made up of metal and glass parts, this becomes the main method Salvage produces steel and glass sheets. To prevent Salvage from simply sending a fresh wreck straight into the industrial shredders they provide a remarkably lower yield for wreck resources and items that can already be recycled, and some wreck resources may harm the shredders if inserted into them.

## Game Design Rationale

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
