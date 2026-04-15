# Shipbreaker Salvage Proposal (Implementation & Design)

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| SlamBamActionman, Princess Cheeseballz | SlamBamActionman et al. | :x: No | TBD |

## Overview

Shipbreak Salvage (or BreakSalv) is a new primary gameplay loop for the Salvage Specialist job, focusing on pulling in shuttle wrecks to the station and manually disassembling them for valuable resources, before sending the remaining structure into a vast industrial furnace to extract base materials. It challenges Salvagers to perform these tasks efficiently in hazardous environments, appealing to players looking for problem-solving gameplay and PvE combat. BreakSalv emphasizes EVA work on the outside of (but still on!) the station with a sci-fi industrial aesthetic mixed with extra-terrestrial discovery unique to the department.

## Background

### Previous Salvage iterations

Throughout the years of SS13 and SS14, there have been multiple types of "Salvage Specialist"-type jobs and mechanics, far too many to list exhaustively here. In SS13, the main ones were Shaft Miner, Lavaland, and Bitrunner. For SS14, it's been Magnet Pulls, Space Debris, Expeditions, and Vgroid. A longer post-mortem describing the issues of the past implementation of Salvage can be found [here](https://docs.spacestation14.com/en/space-station-14/departments/cargo/proposals/salvage-postmortem.html).

Salvage has always been positioned as a "resource generator" job. A resource generator is a role that creates new resources for other roles to use. Cargo and Botany are two jobs strongly featuring this aspect. Salvage in SS14 has primarily focused on lathe materials, with some being soft- or hard-locked behind the job, such as silver or uranium. BreakSalv intends to continue this specialization because it fills a niche that other resource generators do not; providing high volumes of basic materials, and rare items that are difficult to acquire elsewhere.

A recurring pattern in both SS13 and SS14 implementations of Salvage is their unavailability. Whether it is Lavaland, Expeditions, or Vgroid, there has been a strong focus on having Salvage leave the station for a highly challenging environment. This gave Salvage an identity of being something hardcore PvE players engage with, but also came with the downside that said players effectively "disappeared" from the round, not caring about station events and being difficult to reach for antagonists. Or, if one of the Salvagers were antagonists, having a straightforward system to dispose of their fellow Salvagers. This has been felt potently in SS14, with periods of the game where Salvage used shuttle gameplay to leave the station for effectively the entire duration of the round. They would create their own medical treatment and lathes, getting antagonist-level loot, and using Cargo's purchase mechanic to bypass interacting with the rest of the station completely. 

That said, Salvage has elements that allow unique gameplay, themes, and mechanics to shine through. PvE-focused combat, variation via mapped magnet pulls, mining, dungeon/world generation, and shuttle building are some gameplay features that Salvage has showcased. Not all of these were conducive to station-aligned gameplay (dungeon/world generation being part of Expeditions is one such example), but it shows Salvage affords ample design space that would be inaccessible through other jobs.

BreakSalv will not attempt to capture all aspects of previous Salvage iterations. It does draw on what has come before as inspiration and as a launchpad for its new design. As you read this document, you will note mechanical similarities to *some* previous implementations of Salvage (most notably Magnet Pulls). That is a result of those systems being a good fit for the ideas that are core to BreakSalv, rather than BreakSalv building upon them simply because they exist.

As the name suggests, Shipbreaker Salvage is also inspired by the game [Hardspace: Shipbreaker](https://store.steampowered.com/app/1161580/Hardspace_Shipbreaker/). It does not try to recreate the game's mechanics in SS14; instead, it aims to emulate the feeling of engagement and fulfilment that breaking apart a spaceship provides, much like the game does. The game provides a good aesthetic and emotional goalpost for what BreakSalv attempts to be (and it's a pretty good game!).

## Core Gameplay Description

*This section deals with the mechanical content introduced by BreakSalv. It is intended to assist developers in what to implement for BreakSalv's base gameplay. To read how this aligns with the Salvage game design document, jump to the [Game Design Rationale](#game-design-rationale) section.*

### Summary

BreakSalv is the primary gameplay loop for the _Salvage Specialist_ job. The purpose of the job is to produce resources for distribution to the rest of the station.

These resources are:
- High volumes of basic raw materials (e.g. steel, glass, plastic).
- Rare and unique materials (e.g. plasma, uranium).
- Certain equipment that may be costly or otherwise difficult for other departments to procure.
- Fully unique items exclusively available through Salvage.

This is achieved by spawning in wrecks of derelict shuttles, extracting rare materials and objects from them by hand, and then smelting the remainder of the shuttle for basic materials. These wrecks feature hazards and challenges that Salvagers must contend with; a proficient Salvage player has both the knowledge and execution to efficiently extract materials while navigating the dangers the wrecks bring.

Salvager work takes place in the _Salvage Bay_. It is a public location exposed to space on the outside of the station, near the Cargo department. Most EVA Salvage work occurs in the Salvage Bay due to the station-locked machinery there. Salvagers should also have a locker room in Cargo for suiting up, with easy access to the rest of the Cargo department to facilitate material transfers.

BreakSalv's gameplay loop consists of four primary parts: retrieval, extraction, processing, and questing. 

### Retrieval

**Retrieval** is the process of spawning wrecks and transporting them to the station so their resources can be extracted.

Wrecks are pre-made grids themed around being decommissioned shuttles, destroyed station sections or similar. Salvage has a unique console in the Salvage Bay called the _Salvage Magnet_ used to spawn and track wrecks. 

#### Salvage Magnet

The Salvage Magnet provides an interface where Salvagers can select from a small set of wrecks to work on. Each entry lists the wreck name, condition and the resources expected to be found on it.

A key pieces of information listed in a magnet entry is the _wreck condition_. Wreck conditions describe environmental hazards or properties that Salvagers can expect to encounter on the wreck. 

Some examples of wreck conditions:

- **Superheated:** Contains compartments with superheated plasma actively on fire. These must be vented into space before being accessed.
- **Infested:** Contains a large number of space mobs that will attack the Salvagers. These mobs are resistant to piercing damage, making ballistic weapons ineffective.
- **Overgrown:** Kudzu covers the wreck, along with trees blocking pathways.
- **Mineralized:** The wreck has chunks of ore and rock in it, which need to be cleared.
- **Radioactive:** Contains a large number of radioactive objects that require quick removal.
- **Defended:** Contains dangerous turrets (ballistic and/or laser) and mines that must be disposed of.
- **Shadowy:** Covered in the visually obscuring shadow anomaly fog that has to be navigated or removed via flashes.
- **Electrified:** Features electrical grilles and shocked airlocks that require either insulated gloves or strategic turning off of APCs.
- **Fortified:** Contains powered access-locked and high-security airlocks with strong walls. These must be hacked or destroyed to reach the resources inside.
- **Anchored:** Has a mini-station anchor inside of it that must be manually turned off before the wreck can be moved.
- **Distant:** Spawns at a further distance away from the station than normal. Jetpack recommended.
- **More!** The idea is that these wreck types can be expanded upon for more variety. 

The wrecks should clearly communicate their danger before being selected so that salvage can prepare beforehand. They do not need to be more specific than what is necessary to communicate which tools a salvager should attempt to acquire. 

- **DO:** Salvage sees a wreck has the "Overgrown" modifier, so they go to Botany to get some Plant-B-Gone to easily get rid of the kudzu.
- **DO:** Salvage sees a wreck has the "Mineralized" modifier, so they go to Science to get drills for the rocks.
- **DON'T:** Salvage jumps onto a wreck and finds out that it's protected by high voltage cables, so they have to leave the Salvage Bay to get insuls after pulling in the wreck.
- **DON'T:** Salvage sees that a wreck has 3 carp, 2 goliaths, and a turret before pulling it in, so they decide to pull in the wreck that instead has 2 carp, 1 goliath, and no turrets.

Only one wreck may be active with the magnet at any given time. Once a wreck has been selected, the interface changes to a new view as described in the [Magnet Evaluation](#magnet-evaluation) section.

Wrecks have the possibility to be aligned with a faction in the game (e.g bloodcult, NanoTrasen, alien etc.). Visuals and contents on the wreck may change to reflect the faction's design. This ties into the [Questing](#questing) section and associated safes. 

#### License Upgrades

At the start of a round, Salvage only have access to fairly simple and small wrecks. Salvage are rewarded for doing their work properly with more complex wrecks through the Salvage Magnet's _license upgrades_. This is tracked on the Salvage Magnet. Through correct handling of wrecks and the resources that can be found on it, Salvage may unlock wrecks that are of larger size and have more wreck conditions, and consequently contain better loot. Safes (as described in the [Questing](#questing) section) are the primary way to gain license upgrades. 

#### Towing

Spawned wrecks will appear in nearby space in proximity to the Salvage Bay. If the wreck is not within the player's viewing distance, Salvage may use a _Mass Scanner_ console in the Bay to locate it. 

Salvage will have tools to move the wreck closer to the Salvage Bay after spawning. This is known as _towing_. Doing so will make it easier to transport resources off the wreck, and having the wreck in the Bay is necessary to complete the later Processing step. Salvagers should not have to step off the station to perform the towing process, though they may need to stand on the extremes of the edge.

An example of this would be using _grappling hooks_ and _magboots_. Magboots provide a strong grounding force and could together with the rope of the grappling hook allow players to reel grids towards themselves. 

Other options such as towing ropes and harpoon turrets could serve a similar purpose. Science has an opportunity to create intra-departmental collaboration via tool upgrades in this area.

### Extraction

**Extraction** is the process of manually retrieving rare materials from wrecks.

Wrecks will contain resources that Salvage wants to move to the station for manual processing. In its simplest form this may be a stack of material, but where the extraction process becomes more interesting are the unique _wreck resources_ and _safes_ that spawn. 

#### Wreck Resources

Wreck resources are ship parts, technology gadgets and hazardous containers made up of rare materials. To extract these materials, the item must be processed via a _recycler_. Every Salvage Bay should be mapped with at least one. 

The scarcity of the material determines how common a wreck resource is. Wreck resources should generally _not_ focus on basic materials, since those are primarily obtained through the Processing step.

Wreck resources often come with some complexity to them to make moving them more challenging:

- **Two-handed:** Requires two hands to pick up. 
- **Large:** Big enough to require dragging and can't be held or put in containers.
- **Fragile:** Yields fewer materials if thrown.
- **Mounted:** Attached to a wall or integrated into some machinery that requires deconstruction.
- **Radioactive:** Emits radiation.
- **Electrically Unstable:** If destroyed or processed incorrectly, will emit an EMP pulse.
- **Explosive:** If destroyed or processed incorrectly, will explode.
- **Pulsating:** Occasionally emits a gravity pulse that pushes away other objects around it.
- **More!** The idea is that these wreck resources can be expanded upon for more variety. 

It's key that wreck resources can be easily identified as such; Salvagers shouldn't need to wonder if a resource should be recycled or if it can be left on the wreck as scrap. 

#### Safes

For the purposes of extraction, safes are unique wreck resources that are not recycled into materials. As they relate to Salvage's progression and on-station tasks, they are desirable to retrieve. Safes are described in more detail in the [Questing](#questing) section.

### Processing

**Processing** is the clean-up process of a salvage operation, performed by grinding up the wreck grid into base materials.

Once all valuable wreck resources have been extracted, it is time to dispose of the wreck itself. For this, the Salvage Bay has a large wall of _industrial smelters_, and _separation charges_.

#### Industrial Smelters

Industrial smelters destroy any tile and structure that comes into contact with the machine. It is essentially a recycler specializing in grids. 

Because wrecks are mostly composed of metal and glass, this is the primary method Salvage uses to produce these materials. To prevent Salvage from simply sending a fresh wreck directly into the smelters and skip the extraction step entirely, they provide a substantially lower yield for wreck resources and items that can already be recycled. Some wreck resources may also damage the smelters if inserted (e.g. ship fuel tanks).

Each smelter acts as a conveyor belt that is only able to push items perpendicular to its opening. Since each Salvage Bay is meant to have a line of smelter (known as a "smelter wall"), this means the material end up in one place. In the event that a smelter gets damaged (because of meteors or misconduct) it should be repairable, e.g. via welding. 

Smelters should by default *only* be able to destroy wrecks spawned by the salvage magnet. Realistically there wouldn't be a distinction, but the antagonistic and griefing impact would be too considerable otherwise. It would also allow crew to easily weaponize the smelter wall against shuttle-based antagonists. It may be possible to remove this limitation (e.g. as an EMAG interaction); however, this would likely need extra precautions if implemented, such as being accompanied by a station-wide announcement.

#### Separation Charges

Some wrecks will simply be too large to fit into the Salvage Bay and the smelter wall. Salvage will be tasked to split these wrecks into smaller parts using a new tool called _separation charges_. These would operate similarly to cables but mounted along tile edges and, when activated, split the grid in two, much like an RCD. Large wrecks should be designed with this functionality in mind and have ideal spots to put down the charged. 

Separation charges can enable strong antagonistic plays, such as disconnecting vital station sections. Placing a single separation charge should therefore have a reasonably long do-after. 

#### Magnet Evaluation

The final part of the Processing step is Salvage returning to the magnet and getting an evaluation of their work.

While a wreck is being worked on, the magnet interface displays a view with the following information:

- **Wreck Percentage:** Percentage of how much of the spawned wreck grid has been processed.
- **Processing Efficiency:** Percentage of wreck resources that were processed correctly, i.e. not inserted into the smelters.
- **Wreck Timer:** Time since magnet pull started.

After some time has passed (short enough not to feel restrictive, but long enough that Salvage can't just cycle wrecks), Salvagers may choose to despawn any remaining grids of their wreck. The magnet interface returns to the wreck selection view, with a timer showing when the next selection of wrecks are available.

The wreck percentage and processing efficiency are used to evaluate how well the Salvage team is correctly dealing with the wrecks. A high processing efficiency means the Salvagers are extracting valuables and not just immediately smelting the wreck, and a high wreck percentage means the Salvagers aren't just despawning the wreck after looting it. These stats can be used to affect various parts of the work to encourage proper handling of the wrecks, such as introducing a delay on pulling in new wrecks if the percentage is too low or lowering the license upgrade progress.

Each wreck should be of one time use. Once Salvage has finished extracting from a wreck, the magnet cannot pull that wreck in a second time and players must choose from a new selection of wrecks. 

### Questing

**Questing** is the final part of the BreakSalv gameplay loop, involving the _safes_ found on the wrecks. Between wreck pulls from the magnet, there will be downtime that Salvagers are encouraged to use for this. 

#### Safes

As mentioned in the [Extraction](#extraction) section, some items Salvage acquire are intended to be used during the Questing step. These are known as Safes.

Safes are impenetrable containers unable to be brute-forced into by normal means. They contain beneficial or interesting _safe loot_ for both Salvage and station crew. To retrieve them from the safe, it must be unlocked via an _unlock condition_.

Unlock conditions require input or cooperation of other departments or crewmembers outside Salvage. They may be more or less detrimental and should require an investment of resources, attention and/or time. The potential benefit of the loot should be potent enough that the crewmember assisting would want to make the investment (even if it is not always guaranteed/risks having a dangerous loot!). The loot also needs to be specific enough to the job/individual such that Salvage does not feel the need to keep all the loot for themselves. 

The safes should be numerous enough that salvage is encouraged to split them up as a team, but not so numerous that one Salvager can't do all the work within a reasonable timeframe. In addition, Salvage should only need to unlock a majority of the safes they find rather than every single one, as there's no guarantees that all of the conditions will be completable due to factors outside of their control. 

In addition to the loot found in the safes, every safe also contains _magnet chips_. These can be inserted into the Salvage Magnet for a large increase in license upgrade progress.

#### The implementation of Safes

Safe design must follow these three rules:

1. Safe unlocking must not be reasonably achievable by Salvage on their own.
2. The unlock condition must result in meaningful gameplay; preferably related to the core gameplay of the person/department intended to unlock it.
3. The loot must benefit the person/department unlocking it, to discourage Salv from unlocking it on their own.

Unlock conditions should ideally not be able to be circumvented using purchases from the cargo request computer. The process of unlocking safes should also be intuitive to an experienced Cargo Technician, acting as an evolution of simple bounties and mail with far more possibilities and danger. 

Keeping with Salvage's themes, these safes should range from mundane to outright bizzare or even dangerous, but they should never be so esoteric in their completion as to confuse the player. It should always be obvious where Salvage needs to go in order to unlock a safe, and what needs to be done. 

Safes also provide an opportunity to bring much of Salvage's unique content onto the station itself. For example, a boss or treasure that was once intended for the VGRoid or Lavaland may instead be accessed through a safe that is activated on station. 

### Salvage Progression

Salvage's equipment progression should primarily come from Science and what can be found/crafted from resources found on wrecks. As the better wrecks are only available through unlocking safes, this ties Salvage to the station and encourages crew interactivity as part of the core gameplay loop.

#### Salvage Specialist equipment

From the start of the round, Salvagers should have access to:

- A salvage hardsuit. Necessary for working in the Salvage Bay.
- Basic tools and toolbelt. For navigating and deconstructing the wreck during the Extraction step.
- A survival knife and a portable kinetic accelerator. Used to deal with hostile mobs on wrecks, and as tools against environmental hazards.
- A grappling hook and separation charges. Necessary to complete the Retrieval and Processing step.

Salvage's upgrades should consist of improvements to these options, with a mix of mundane and not so mundane options. Some examples could include:

- Improved space faring armor.
    - Better defense or better mobility.
- Better deconstruction tools.
    - Welding goggles, insulated gloves, power tools, mining drills, explosives.
- Better space mobility.
    - Jetpacks, grappling hook+, forklifts.
- Better grid dragging tools.
    - Harpoons, forklifts, tether guns.
- Better weaponry
    - Laser weapons, crusher melee weapons.

The options listed above are very mundane. Fantastical options should be available, though the shape and balance of them are best determined via playtesting. Fantastical options should at best be equal to the best mundane options listed as examples above. 

### Aesthetic choices & inspirations

A large part of Salvage's appeal is the aesthetics. Salvage should feel like a tough and cool job to do, regardless of what they're doing. 

Aesthetically and tone wise, Salvage should lean more on the dark comedy and horror of the game's tone. Space is vast, endless, and full of threats both rational and irrational. The wrecks salvagers pull in should reflect this, enhancing the tone of the job and ensuring gameplay variety. 

Wrecks should never feel completely mundane. There's a story to how this once functional ship, outpost or machine beyond understanding became a wreck. The environment in the wreck should reflect this, and ideally tie into whatever safe is contained within. 

#### Mundane realities of fantasy star-systems 

An important aspect to enhance tone is to have the actual interactions be extremely mundane. Salvagers are people accustomed to manual labor, regardless of what they are working with. A wreck may be an abomination of flesh-consuming metal as Salvage works inside the belly of some cosmic beast, but mechanically they're treating its arteries the same way they would treat pipes, and its vital organs as obstacles or valuables. 

Salvage's progression should reflect this. Armor upgrades being the result of stripping the tough hides off of alien monsters. Medicine being taken from self replicating cosmic beasts. Weapons having sci-fi tech so advanced as to appear magical, stealing the life force from their slain enemies. 

Salvage is practical, and the world around them is irrational. This should be reflected as much aesthetically as it is mechanically. The aesthetics that a Salvager takes on should be shaped by the wrecks and situations they encounter. 

## Game Design Rationale

This section addresses specific design choices with the various features BreakSalv aims to implement.

### Salvage in space

Previous iterations of Salvage had a problem with Salvage "fucking off into space" and not engaging with the station for the majority of the round. This has less been the fault of space itself and rather caused by Salvage mechanics that encouraged leaving the station. Shuttle building and space debris encouraged hopping from debris to debris to gather resources. The VGRoid asteroid was the epitome of encouraging Salvage to leave for extended durations and make "mini-stations" replacing the need to return to the station altogether. Expeditions disconnected Salvage from the station map entirely, and fultons meant Salvagers didn't need to return to the station to hand over materials. 

BreakSalv locks Salvage to the station in four ways: 
- Industrial smelters are large machinery difficult to reposition.
- The salvage magnet only works on-station, and wrecks are spawned close to the station.
- Wreck conditions necessitates equipment Salvage have a hard time accessing themselves.
- Safes require collaboration with station crew to unlock.

This has major knock-on effects for Salvage's independence and accessability. There are no parts of Salvage's gameplay loop that require extended periods off the station. By being in so close proximity to the station, there isn't a strong incentive to set up station-replacing equipment. Salvage will always be available to react to station events and become easier to locate, e.g. for antagonists. 

The Salvage Bay is proposed to be publicly accessible to crew. Salvage would end up being relatively accessible compared to other jobs on the station, with the caveat that an EVA-capable suit is necessary. Emergency EVA softsuits should work for visitors though won't allow long-term stays. This is a vast improvement to their previous iterations, and would position them better than enclosed subdepartments like Atmospherics or Xenoarcheology.

### The Retrieval Part & Towing

The purpose of the Retrieval part of the gameplay loop is to involve players with the game's space movement mechanics. It's the primary way that Salvage engages with the *space* part of the space station. Movement through zero-g is different enough to regular movement that players develop it as a skill. With the additional task of moving magnet wrecks, Salvage are encouraged to learn the ways their character and tools have physical characteristics in a space environment.

Towing ends up serving both as a power fantasy mechanic and as a puzzle mechanic. Pulling wrecks by hand, with the slow lumbering movement as you gradually accelerate it, feels empowering. The puzzle aspect comes into play when you need to position the wreck to fit within the Salvage Bay, encouraging an understanding of the physics and how the Bay itself can be reshaped to move it into place.

Towing as a game mechanic will likely not be relevant to other roles. It will be a general mechanic, but the use case for it is largely limited to Salvagers and the grids they pull. There may be more use for it in the future depending on how shuttle and Engineering mechanics develop.

### The Salvage Magnet and Wrecks

Wrecks are implemented as Salvage's instanced locations and utilization of random generation.

Wreck conditions is a way to add further variation independent of grid layout. The ability to foresee these modifiers in the salvage magnet gives players a sense of agency and planning. Players are able to (somewhat) control what challenges they want to tackle based on their preference and equipment.

All wrecks should ideally have some "lore" behind them. It does not necessarily have to be hand-crafted environmental storytelling, and may instead be the result of wreck layout, conditions, contents and factions allowing players to imagine a story. This enhances the world-building for the game and immerses players more. Random generation should be balanced with this in mind. While variation is important, it should not cause situations where immersion is broken.

Wrecks should ideally not have just a single way that they can play out. Salvagers should feel like they can make meaningful choices in how they approach a wreck. This makes them more accessible to novice players, and gives experienced players an opportunity for skill expression in determining the most optimal path based on the circumstances.

As mentioned in the previously, the salvage magnet becomes part of what ties Salvagers to the station. It is a critical part of ensuring that BreakSalv flows smoothly, and a lot of care and consideration needs to be taken to ensure that its presentation and mechanics don't encourage gameplay going against Salvage's design. 

#### Wreck contents

Wrecks should ideally refrain from having certain items. This is primarily medical supplies, food, and hard cash. Salvagers shouldn't be able to loot wrecks and set up their own medical facilities, sustain themselves completely on wreck food, or find large stacks of money invalidating the work Cargo Technicians put in. However, Salvage should be able to supply these departments with resources, and may be a core part of completing certain bounties for Cargo.

Salvage has had a tradition of getting "gamer loot" via wrecks, i.e., equipment that would be very strong in the hands of an antagonist (or worse, used to validhunt/shut down antagonists) when they return to the station. Some wrecks, especially those that become available after the magnet upgrade, may contain some stronger equipment and fun cosmetics (drip) are encouraged. Syndicate equipment should be heavily restricted from the wrecks.

### Smelters and Wreck resources

The main motivation behind wreck resources is to encourage Salvage to engage with the inside of wrecks. They should be something that Salvagers *want* to seek out, via distinct visuals and containing rare materials. This should play into the aesthetics of Salvage. Players should feel that the valuable things they find are contextualized as such in-universe, instead of "scrap".

Salvagers are punished in multiple ways when ignoring the wreck resources. Smelters provide an immensely lower yield for wreck resources and may even take damage from explosions. The salvage magnet also tracks improperly smelting resources. This further encourages Salvagers to engage with the challenges posed by the wreck, instead of simply sending the entire grid straight into the smelters.

#### Station resources

This document primarily cites rare materials and specialized equipment in the form of safes as content Salvage can uniquely provide the station. With the content currently available, this can negatively impact gameplay for other departments (e.g., Science) where Salvage is _required_ to provide materials to enable core gameplay and rewards. 

BreakSalv's design is more accessible than previous iterations of Salvage and it should be easier for non-Salvage crew to assist in the work should there be heavy demand for a resource. However, this may not be sufficient to cover resource shortage, such as when the Salvage Bay is irrepairably damaged.

The solution for this would necessitate more gameplay mechanics that allow generating the materials that are necessary for other departments, or a redesign of their consumption. Reworking the game's resource dependencies is considered out of scope for this document as it is not relevant to BreakSalv's core gameplay loop.

### Questing & Safe Design Motivation

Questing provides the necessary motivation for Salvage to not constantly throw themselves at dangerous wrecks over and over. Working in space is always going to have a base level of tension to it higher than being inside the station, and with the challenges wrecks provide this is only pushed further. Safes allow Salvagers to take a break and gives them an excuse to socialize with the rest of the station without feeling like they are skipping out on work. It integrates crew interaction into Salvage's gameplay loop and allows it to feed back into the resource gathering via the license upgrades.

License upgrades being core to Salvage's progression, and therefore magnet chips being a key component, is critical to ensure Salvagers are the ones engaging with station interaction. Securing chips should be a strong motivator for Salvagers to make sure they are the ones doing the delivery of the safes (rather than pawning it off to a Cargo Technician) and pushes them into interactions with the crew. 

#### Safes & Station collaboration

The unlock conditions, loot and magnet chips are how safes are motivated to be brought onto the station. As previously mentioned, unlock conditions should ideally not be solved by Salvage and instead involve other departments. 

The easiest way to achieve collaboration is to make the unlock condition require some station-bound equipment. Salvage will generally not have access to certain things, such as Science's APEs or Engineering's Particle Accelerator. They would then be required to interact with the roles that do. However, this method of unlocking safes may result in uninteresting interactions if not designed properly.

Another way to achieve collaboration is to have conditions that demand something beyond Salvage's capabilities. As examples, Salvage may have *some* medical or combat capabilities, but Medical and Security have core gameplay that make them more proficient. By having the unlock condition require more than Salvage could themselves handle, such as causing major injury to a player or an overwhelming combat scenario, they are pushed into asking the station for assistance. This should be the preferred way that safes are unlocked, though they do run a greater risk of expert Salvagers being able to complete the challenges themselves.

The greatest difficulty in this is ensuring that that the loot is unique and interesting, and that the unlock conditions truly do require crew interactions. A safe design has failed if crew are unwilling to help Salvagers, or if Salvagers don't feel the delivery is worth the effort.

## Administrative & Server Rule Impact (if applicable)

Given the safety locks on the industrial smelters, the only moderation issue is an antagonist using them for DAGD-level destruction by mounting them on a shuttle and trying to bulldoze the station. This is not possible by default and while it could be opened up via requiring an EMAG to "bypass the lock", it would be limited to antagonists only and may not even be enabled depending on playtesting.

## Technical Considerations

### New features

#### Grid dragging

Grid dragging has been implemented in a prototype. The main issue encountered is that grid mass is currently not very accurate. This would cause problems when determining pull strength and also how the grids should pull towards each other if neither grid on either end of the grappling hook is anchored. The prototype accounts for this, but other systems (such as shuttle power) would require refining to match these new values.

There would need to be some sanity checks so that a Salvager can't just stand on the station and keep a moving shuttle in place with just their equipment.

#### Separation charges

Splitting grids is already a thing that can be done with the RCD, but that operates on the principle of removing tiles entirely. There would need to be a solid system in place that not only deals with separation charges being capable of sitting on the edge between two tiles, but also that it can accurately split the grids in two. There may also be a desire to have "welding charges" that allow two grids to be connected, though that isn't vital to BreakSalv itself.

The main motivation for why they should be implemented is to give mappers more freedom when designing the sizes of Salvage Bays and wrecks.

#### Wreck Resources and Safes

There would be a fairly substantial amount of new sprites for both wreck resources and safes, as the whole point of them is to stand out from what currently exists in the game. There will likely be changes and additions to many different systems to support their behavior, though reusing assets and components where possible is greatly preferred.

### Modified features

#### Station map considerations

Station maps would need to accommodate the new "smelter wall" concept. After testing, it seems that a width of 9 tiles (the width of a singularity containment field) is around the ideal size to deal with pulling in wrecks for smelting. Most stations seem to have room to fit them without issue (except possibly Reach, though there is room for a smaller version).

All maps would need to implement a new Salvage Bay to be able to support BreakSalv. The new Salvage Bay should have access via a Cargo airlock and a public airlock; only the Salvager locker room needs to be job-locked.

#### Wreck map considerations

All existing wreck maps would likely need to be removed entirely. They are not balanced with BreakSalv in mind and have wild variation in things that can spawn on them. Some may be able to be repurposed and their designs reused, but they are not compatible as-is. 

This document does not make a _definitive_ statement on how the wrecks and wreck types should be implemented technically. There are many options here (some better than others), from handcrafted prefabs to fully randomly generated, and it may not be fully evident which method is best until implementation is started.

The suggested way to implement the wrecks would be to have standardized wrecks with sophisticated random spawners, conditional rules that apply visuals and wreck conditions to the grid, and randomized room layouts. This would ideally strike a balance between deliberate design choices a mapper may make in terms of environmental storytelling and challenges, and the maintainability and variation that random elements provide. 

#### Salvage Magnet

The salvage magnet would require a major re-design with its UI to support the new functionality. Some of what exists could probably be repurposed for BreakSalv however.

The magnet must also be able to properly track how much of a spawned grid remains, which includes whether the grid is split off into multiple parts. This has been implemented in a prototype.

### Further Embodiments

There are a few ways that BreakSalv can be expanded upon. These are not necessarily part of the base implementation but may be worth exploring in the future:
- A stationary "spear gun" turret stationed in the Salvage Bay that Salvagers manually control to hook into wrecks that are too far for their grappling hooks.
- Industrial smelters being a Science research technology. I fear what the Passengers will do with this.
- More elaborate wreck mechanics inspired by Hardspace: Shipbreaker. Examples would be reactors that start a timer before needing to be processed or else explode, or heating/cooling pipes that could harm you if cut before being drained.
