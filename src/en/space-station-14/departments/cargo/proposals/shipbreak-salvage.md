# Shipbreaker Salvage Proposal

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| SlamBamActionman, Princess Cheeseballz | SlamBamActionman et al. | :x: No | TBD |

## Overview

Shipbreak Salvage (or BreakSalv) is a new primary gameplay loop for the Salvage Specialist job, focusing on pulling in shuttle wrecks to the station and manually disassembling them for valuable resources, before sending the remaining structure into a vast industrial furnace to extract base materials. It challenges Salvagers to perform these tasks efficiently in hazardous environments, appealing to players looking for problem-solving gameplay and PvE combat. BreakSalv emphasizes EVA work on the outside of (but still on!) the station with a sci-fi industrial aesthetic mixed with extra-terrestrial discovery unique to the department.

## Background

### Previous Salvage iterations

Throughout the years of SS13 and SS14, there have been multiple types of "Salvage Specialist"-type jobs and mechanics, far too many to list exhaustively here. In SS13, the main ones were Shaft Miner, Lavaland, and Bitrunner. For SS14, it's been Magnet Pulls, Space Debris, Expeditions, and Vgroid. A longer post-mortem describing the issues of the past implementation of Salvage can be found [here](en/space-station-14/departments/cargo/proposals/salvage-postmortem.html).

At its core, Salvage is meant to be a "resource generator" job. A resource generator is a role that creates new resources for other roles to use; Cargo is an obvious one, with its bounties and cash (turning into purchased products and some materials), and another is Botany, with its produce (turning into reagents and some materials). There is an inherent sense of accomplishment in this kind of gameplay, as other players appreciate the resources created, and the supply can influence the round in notable ways. Salvage in SS14 has primarily focused on lathe materials, with some being soft- or hard-locked behind the job, such as silver or uranium. BreakSalv intends to continue this specialization because it fills a niche that other resource generators do not, providing high volumes of basic and rare materials that are difficult to acquire elsewhere.

A recurring pattern in both SS13 and SS14 implementations of Salvage is their unavailability. Whether it is Lavaland, Expeditions, or Vgroid, there has been a strong focus on having Salvage leave the station for a highly challenging environment. This has given Salvage a bit of an identity as being something hardcore PvE players engage with, but also came with the downside that said players effectively "disappeared" from the round, not caring about station events and being difficult to reach for antagonists, or if one of the Salvagers were antagonists, having a straightforward system to dispose of their fellow Salvagers. This has been felt potently in SS14, where there were periods of the game where Salvage used shuttle gameplay to leave the station for effectively the entire duration of the round, creating their own medical treatment and lathes, getting antagonist-level loot, and using Cargo's purchase mechanic to bypass interacting with the rest of the station completely. 

That said, Salvage has elements that allow unique gameplay, themes, and mechanics to shine through. PvE-focused combat, variation via mapped magnet pulls, mining, dungeon/world generation, and shuttle building are some of the things that Salvage has showcased. Not all of these were necessarily conducive to station-aligned gameplay (dungeon/world generation being part of Expeditions is one such example), but it shows Salvage affords a rather ample design space that would otherwise be inaccessible through other jobs.

Accordingly, BreakSalv will not attempt to capture all aspects of previous Salvage iterations. Still, it does draw on what has come before as inspiration and as a launchpad for its new design. As you read this document, you will note mechanical similarities to *some* previous implementations of Salvage (most notably Magnet Pulls). That is a result of those systems being a good fit for the ideas that are core to BreakSalv, rather than BreakSalv building upon them simply because they exist.

As the name suggests, Shipbreaker Salvage is also inspired by the game [Hardspace: Shipbreaker](https://store.steampowered.com/app/1161580/Hardspace_Shipbreaker/). It does not try to recreate the game's mechanics in SS14; instead, it aims to emulate the feeling of engagement and fulfilment that breaking apart a spaceship provides, much like the game does. The game provides a good aesthetic and emotional goalpost for what BreakSalv attempts to be (and it's a pretty good game!).

## Motivation for Salvage

This Salvage design is grounded in using the unique opportunities provided by having a resource generator working on the outside of the station. Open space, and the environments that can be put in it, lends itself well to randomized elements that wouldn't be possible inside the static layout of a station. In addition, the inherent dangers of space suits a role defined by hazardous work, which should appeal to risk-seeking players that are either looking for a thrilling experience, or that wish to optimize their performance in spite of the dangers. This type of gameplay is currently only really offered via Security (which has a strong focus on PvP combat and unexpected bursts of danger) or Science (as part of artifact/anomaly research), leaving room for Salvage to fulfill a niche as a reliable source of PvE combat, environment navigation challenges and space movement mechanics, while being a primary resource generator.

Salvage should aim to provide the following experience:
- Hard work not for the faint of heart under a sci-fi megacorp industrial aesthetic. Salvagers should feel like they are cool by braving the dangers and efforts inherent to their job.
- Visible results from their work. Seeing a huge pile of materials that can be delivered should make the Salvagers feel like they are contributing to the station.
- Completionism and optimization. Salvagers will want to aim for high efficiency while working speedily, with experience allowing players to tackle more difficult scenarios while still keeping up a high pace. 
- Moments of rest. Since all Salvage work requires constant manual effort, Salvagers shouldn't be pressured to work continuously. The game should naturally have breakpoints where Salvagers disengage from the resource-gathering loop to ensure they aren't constantly in a monotonous "workmode". 

Salvage should avoid the following:
- Isolationism. While Salvage operates on the outside of the station, they should not by any means be unreachable to the rest of the station crew. There may be small moments where a Salvager and their team are positioned in an awkward location but this should be brief and temporary. In addition, Salvage should be encouraged to interact with station crew directly as part of its gameplay, either utilizing services (rather than being self-reliant) or through enabling aspects of their work.
- Easy sabotage/round removal features. By working in space, Salvage has some inherent advantages to the job for antagonistic activities (e.g. EVA, tools, space movement). Tools and equipment must be evaluated in the context of antagonists/griefers getting their hands on them and be appropriately balanced. 
- Overabundance of materials. All wrecks should follow guidelines for how many resources may be on them and what loot may be found, such that a competent Salvage team can't make Cargo completely redundant. Similarly, Cargo itself shouldn't make Salvage's work redundant to the station. Said guidelines should be constructed through playtesting to find the sweetspots and aren't covered in this proposal.
- Single point of failure for core gameloops. While the lack of Salvage should be felt by the station, Cargo and other departments should not rely on the output of Salvage's work to the extent where their core gameloops are unable to progress in case Salvage is unable to perform. In the event that Salvagers are dead/missing, it should be possible for Cargo/other crew to take over performing Salvage work without too much difficulty.
- Harvesting gamerloot. While Salvagers should be able to find fun and interesting things as part of their work, this should be achieved through properly interacting with the gameplay loop and ensuring the job is done well. Speeding through content to reach specific "loot" should be discouraged via mechanics, to prevent forgoing station-supporting gameplay for selfish rewards. 

## Core Gameplay Description

*This section deals with the content introduced by BreakSalv and to assist developers in what to implement to achieve the desired gameplay. To read motivations for the content, jump to the [Game Design Rationale](#game-design-rationale) section.*

BreakSalv is the primary gameplay loop for the _Salvage Specialist_ job belonging to the Salvage subdepartment of the Cargo department. The job's purpose on the station is to produce resources for distribution to the rest of the station, including high volumes of basic raw materials (e.g. steel, glass, plastic), rare and unique materials (e.g. plasma, uranium), certain equipment that may be costly or otherwise difficult to procure for departments, and fully unique items exclusively available through Salvage. This is achieved by spawning in wrecks of old derelict shuttles, extracting rare materials and objects from them by hand, and then smelting the remainder of the shuttle for basic materials. These wrecks feature hazards that Salvagers must contend with; a proficient Salvage player has both the knowledge and execution to quickly and efficiently extract materials while navigating the dangers the wrecks bring.

The work of a Salvager takes place in the _Salvage Bay_, a location exposed to space on the outside of the station, near the Cargo department. While most Salvage work occurs in the Salvage Bay due to the station-locked machinery there, they should have a small locker room in Cargo for suiting up, with easy access to the rest of the Cargo department to facilitate material transfers.

BreakSalv's gameplay loop consists of four primary parts: retrieval, extraction, processing, and questing. 

### Retrieval

**Retrieval** is the process of spawning wrecks and transporting them to the station so their resources can be extracted.

Wrecks are pre-made grids themed around being decommissioned shuttles, destroyed station sections or similar. To access wrecks, Salvage has a unique console in the Salvage Bay called the _Salvage Magnet_. 

#### Salvage Magnet

The Salvage Magnet (or just magnet) provides an interface where Salvagers can select from a small set of wrecks to work on, called the "Wreck Selection" view. Each entry lists the wreck type and the resources expected to be found on it.

One of the key pieces of information listed in a magnet entry is the _wreck type_ the wreck is. Wreck types describe environmental hazards or wreck properties that pose challenges unique to each type, giving Salvagers variety and choice in the wreck they want to work on. 

Some examples of wreck types:

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

The wrecks should clearly communicate before being selected their dangers and difficulties such that salvage can prepare beforehand. They do not need to be more specific than what is necessary to communicate which tools a salvager should attempt to acquire. 

- DO: Salvage sees a wreck has the "Overgrown" modifier, so they go to Botany to get some Plant-B-Gone to easily get rid of the kudzu.
- DO: Salvage sees a wreck has the "Mineralized" modifier, so they go to Science to get drills for the rocks.
- DON'T: Salvage jumps onto a wreck and finds out that it's protected by high voltage cables, so they have to leave the Salvage Bay to get insuls after pulling in the wreck.
- DON'T: Salvage sees that a wreck has 3 carp, 2 goliaths, and a turret before pulling it in, so they decide to pull in the wreck that instead has 2 carp, 1 goliath, and no turrets.

Only one wreck may be active with the magnet at any given time. Once a wreck has been selected, the interface changes to a new view as described in the [Magnet Evaluation](#magnet-evaluation) section.

Wrecks have the possibility to be aligned with a faction in the game (e.g bloodcult, NanoTrasen, alien etc.), which has some implications on visuals of the wreck, as well as possibly flavoring some of the contents found. This ties into the [Questing](#questing) section and associated relics. 

#### Towing

Once a wreck has been spawned, it will be located somewhere in nearby space in proximity to the Salvage Bay. If the wreck is not within the player's viewing distance, Salvage may use a _Mass Scanner_ mapped in the Bay to locate it. Compared with previous iterations of Salvage, the wrecks are meant to spawn much closer to the station. Regardless, Salvage will want to move the wreck closer to the Salvage Bay, as it will make it easier to extract materials and is necessary to complete the later steps. This is known as _towing_.

To tow the wreck, Salvage will have access to certain tools to drag grids. An example of this would be using _grappling hooks_ and _magboots_. While grappling hooks on their own simply drag the user towards the hook, when combined with the grounding force of the magboots, Salvagers could pull grids towards each other (or, in the case of one with a station anchor, only the one without is pulled). Ideally, Salvage would be able to stand on the outer rim of the station and use their grappling hooks to drag the wreck into working distance and proceed to the next step. Other options, such as towing ropes or harpoon turrets, could serve a similar purpose. There is an opportunity for intra-department collaboration where Science could provide tool upgrades for easier towing.

### Extraction

**Extraction** is the process of manually retrieving rare materials from wrecks.

On the wrecks, there will be various resources Salvage will want to move off the wreck and onto the station by going onto the wreck and picking them up by hand. In its simplest form, this may be a stack of material, but where the extraction process becomes more interesting is the unique _wreck resources_ and _quest items_ that may spawn on wrecks. 

#### Wreck Resources

Wreck resources are ship parts, technology gadgets and hazardous containers made up of rare materials. Salvage will want to remove these to ensure a high material yield and/or prevent damage to the Salvage Bay. No one wreck will contain all types of wreck resources, and wrecks could specialize in a specific resource to be extracted (such as a radioactive wreck type containing many radioactive wreck resources that provide uranium).

Wreck resources cannot be used directly as materials; they must be processed first. The _recycler_ is a good option for this, as it is a station-mounted machine, and Salvage can easily have their own. As a rule, wreck resources should _not_ focus on basic materials, since those are primarily obtained through the processing step.  

- **Two-handed:** Requires two hands to pick up. 
- **Large:** Big enough to require dragging and can't be held or put in containers.
- **Fragile:** Easily broken if thrown around recklessly.
- **Mounted:** Attached to a wall or integrated into some machinery that requires partial deconstruction.
- **Radioactive:** Emits radiation.
- **Electrically Unstable:** If destroyed or processed incorrectly, will emit an EMP pulse.
- **Explosive:** If destroyed or processed incorrectly, will explode.
- **Pulsating:** Occasionally emits a gravity pulse that pushes away other objects around it.
- **More!** The idea is that these wreck resource types can be expanded upon for more variety. 

It's key that wreck resources can be easily identified as such; Salvagers shouldn't need to wonder if a resource should be recycled or if it can be left on the wreck as scrap. 

#### Relics

Relics are described in more detail in the [Questing](#questing) section, but for the purposes of extraction they are unique wreck resources that are not recycled into resources. These items become important to Salvage's progression through the round, and are therefore desirable to retrieve. 

### Processing

**Processing** is the process of finalizing a salvage operation by grinding up the remains of a wreck into base materials.

Once all valuable wreck resources have been extracted and the Salvagers are finished with the wreck, it is time to dispose of the wreck itself. For this, the Salvage Bay has a large wall of _industrial smelters_, and _separation charges_.

#### Industrial Smelters

Industrial smelters operate by grinding any tile that comes into contact with the machine's open front, destroying it and any attached structures. It is essentially a recycler specializing in grids. Because wrecks are mostly composed of metal and glass, this is the primary method Salvage uses to produce steel and glass sheets. To prevent Salvage from simply sending a fresh wreck directly into the smelters and skip the extraction step entirely, they provide a substantially lower yield for wreck resources and items that can already be recycled, and some wreck resources may damage the smelters if inserted into them (e.g. fuel tanks).

Since some individual grid tiles could feasibly be made with less than one sheet of steel material, those tiles only have a percentage chance to produce a sheet. E.g., a lattice, which is made of 1 steel rod (equivalent to 0.5 steel sheet), has at most a 50% chance of producing a sheet.

Each smelter acts as a conveyor belt that is only able to push items perpendicular to its opening; since each Salvage Bay is meant to have a line of smelter (known as the "smelter wall"), this means the material can travel along the line to a pick-up location (either in the Bay or in Cargo proper). In the event that a smelter gets damaged (because of meteors or misconduct) it should be repairable, e.g. via welding. 

Smelters should by default *only* be able to destroy wrecks spawned by the salvage magnet. While realistically there wouldn't be a limit, this is an instance where moderation efforts need to be made as having them able to smelt any grid would make major griefing and self-antagonism too easy to perform, and also allow crew to easily weaponize the smelter wall against shuttle-based antagonists (despite how awesome it sounds, we do not want crew to mount smelters to a Cargo shuttle to bulldoze the Xenoborg Mothership). It may be possible to remove this limitation (e.g. as an EMAG interaction); however, this would likely need extra precautions if implemented, such as being accompanied by a station-wide announcement.

#### Separation Charges

Some wrecks will simply be too large to fit into the Salvage Bay and the smelter wall. Salvage will be tasked to split these wrecks into smaller parts using a new tool called _separation charges_. These would operate similarly to cables but are mounted along tile edges and, when activated, split the grid in two, much like an RCD. This split is accompanied by a small spark (not an explosion!) and a small push force separating the grids. Large wrecks should be designed with this functionality and, in most cases, include predefined ideal spots for placing charges.

Since separation charges can enable strong antagonistic plays, such as disconnecting vital station sections, placing a single separation charge should have a reasonably long do-after. 

#### Magnet Evaluation

The final part of the BreakSalv loop is Salvage returning to the magnet and getting an evaluation of their work.

While a wreck is being worked on, the magnet interface displays a "Magnet Evaluation" view with the following information:

- **Wreck Percentage:** Percentage of how much of the spawned wreck grid has been processed; 0% means all grid tiles remain, 100% means no grid tiles remain.
- **Processing Efficiency:** Percentage of valuable entities on the wreck that were processed correctly. This is calculated based on whether the smelters have processed any wreck resources.
- **Wreck Time:** Time since magnet pull started.

After some time has passed (short enough not to feel restrictive, but long enough that Salvage can't just cycle wrecks), Salvagers may choose to despawn any remaining grids of their wreck using an "End Salvage Operation" button on the magnet. Once the button is pressed, the magnet interface returns to the wreck selection view, with a timer showing when the next selection of wrecks are available.

The wreck percentage and processing efficiency are used to evaluate how well the Salvage team is correctly dealing with the wrecks; a high processing efficiency means the Salvagers are extracting valuables and not just immediately smelting the wreck, and a high wreck percentage means the Salvagers aren't just despawning the wreck after looting it. These stats can then be used to affect various parts of the work to encourage proper handling of the wrecks, such as introducing a delay on pulling in new wrecks if the percentage is too low. 

Each wreck should be of one time use. Once Salvage has finished extracting from a wreck, the magnet cannot pull that wreck in a second time and players must choose from a new selection of wrecks. 

### Questing

The final part of the BreakSalv gameplay loop is handling delivery of materials and _relics_ found on the wrecks. Between wreck pulls from the magnet, there will be downtime that Salvagers are encouraged to use for this. 

### Relics & Quests

As mentioned in [Extraction](#extraction), some items salvage acquires will specifically be designed to be used during the Questing phase. These relics contain beneficial or interesting _effects_, but must be unlocked first through some action. They should be designed such that their _unlock condition_ require the input or cooperation of other departments or crewmembers. This unlock condition may be more or less detrimental and should require an investment of resources, attention and/or time. The potential benefit of the effect should be such that the crewmember helping unlock it wishes to pursue it (even if it is not always guaranteed/risks having a negative effect!), but the effect also needs to be specific enough to the job/individual such that Salvage does not feel the need to keep the relic for themselves. 

Unlocking relics is tracked as "quests", and progress can be viewed in a computer in the Salvage Bay.

- DO: Salvage finds a lost coffer on a wreck that they need to deliver to a person on the station. This coffer is known to contain something valuable so there's incentive for the person to open it. Once it's delivered, the quest is marked as completed. 
- DO: Salvage finds some kind of alien tablet that seems to be pourous and demands bicaridine. Salvage goes to the medical bay and gives it to chemistry, who splashes some bicaridine causing it to transform into another reagent entirely. Chemistry can use this device to perform limited chemical transmutation, and the quest is marked as completed.
- DO: Salvage finds an encrypted tech disk that needs to be unencrypted by science and inserted into the R&D computer. This provides an option for Science to research an additional T3 technology for a greater cost. Once inserted, the quest is marked as completed.
- DON'T: Salvage finds an alien artifact that needs to be hit for 300 damage to progress, so they beat it with crowbars in space until their quest completes.
- DON'T: Salvage finds a locked data-tablet without any function requires Captain access to complete the quest. The captain opens it without thought and the quest is marked as completed without any further interaction or benefit.
- DON'T: Salvage finds a relic with an effect of instant full self-healing. Instead of going to Medical to help with its unlock, Salvagers brute-force unlocking it themselves, to save the trip and also keep the relic for themselves.

If Salvage wants to unlock better wrecks, they should have to complete these quests. Ideally much of the upgraded equipment and unlockables salvage wants should be locked behind wrecks which can only be pulled if Salvage completes these quests. 

Keeping with Salvage's themes, these quests should range from mundane to outright bizzare or even dangerous, but they should never be so esoteric in their completion as to confuse the player. It should always be obvious where salvage needs to go, in order to complete their quests, and what needs to be done. These quests ideally should not be able to be circumvented using purchases from the cargo request computer. 

Once salvage has completed a majority of these quests, they will be rewarded with a "license upgrade" which gives them access to a new selection of wrecks (or wreck singular) with higher complexity but also higher rewards.

These quests should be numerous enough that salvage is encouraged to split them up as a team, but not so numerous that one salvager can't do all the work within a reasonable timeframe. In addition, salvage should only need to complete a majority of these quests rather than every single one, as there's no guarantees that all of the quests will be completable due to factors outside of their control. 

## Game Design Rationale

This section addresses specific design choices with the various features BreakSalv aims to implement.

### Salvage in space

Previous iterations of Salvage have had a problem with Salvage "fucking off into space" and not engaging with the station for the majority of the round. This has less been the fault of space itself and rather the Salvage mechanics that encouraged leaving the station; shuttle building and space debris encouraged hopping from debris to debris to gather resources, with the vrgoid asteroid being the epitome of encouraging Salvage to leave for extended durations and make "mini-stations" with medical capabilities and even their own lathes replacing the need for the station altogether. Expeditions disconnected Salvage from the station map entirely, and fultons meant Salvagers didn't need to return to the station to hand over the materials. 

BreakSalv locks Salvage to the station grid by making heavy use of the magnet and the industrial smelters. There is little to no reason to engage in gameplay away from the station, and by being in so close proximity to the station, there isn't a strong incentive to set up station-replacing equipment. This means that Salvage will always be accessible to react to station events and become easier to locate, e.g., for antagonists. 

The purpose of the Retrieval part of the gameplay loop is to provide players with a good opportunity to engage with the game's space movement mechanics, from basic leaps to jetpacks (real or improvised) to grappling hooks. It's the primary way that Salvage engages with the *space* part of the space station. This makes the role fairly unique in the game; while there are other jobs that work in space at times (primarily Engineering) they do not utilize movement through it as a core aspect of the job. Of course this relies on that the base mechanics themselves provide interesting gameplay, but considering how integral space is to the identity of the game, that should be a given.

There are still some cons to working outside the station. It limits crew interactions, as there is no Salvage "front desk" and the Salvage Bays would not be by any high-traffic area (unless a station specifically designs its layout around it). On the other hand, tying Salvage's work to the Salvage Bay will make it massively more accessible compared to previous iterations. Paramedics will have an easier time accessing Salvagers in case of lethal explosions, Cargo & QM will generally know where Salvagers are while working, Engineers can pass by Salvagers when traversing the outside of the station, and there is a much lower barrier of entry for Passengers to help out by virtue of the Salvage Bay being more open.

The Salvage Bay also offers a good spot for holopads, and since the Wreck Timer is purely cosmetic, there is no penalty for Salvagers to pause their work to engage in conversation or complete station tasks.

### The Salvage Magnet and Wrecks

Wrecks provide variety to the round, both in the selection of available wrecks and in the contents they may provide. Having wreck types as modifiers is a useful way to add gameplay breadth, and giving the ability to foresee which wreck types are available gives players some control in what challenge they want to tackle based on preference and equipment. They are also excellent opportunities for environmental storytelling; all wrecks should have some sort of "lore" behind them that ties into their wreck type and what they depict. Wrecks do serve as an opportunity to use randomly generated layouts, possibly being entirely algorithmically generated, but care needs to be taken to ensure that this does not come at the expense of immersion and interesting exploration. Wrecks should ideally not have just a single way that they can play out to create emergent gameplay, and Salvagers should feel they can make meaningful choices with what wrecks they spawn in, and also in how they approach them.

As mentioned in the previous section, the salvage magnet becomes part of what ties Salvagers to the station. Despite its unassuming appearance, it is a critical part of ensuring that BreakSalv flows smoothly, and a lot of care and consideration needs to be taken to ensure that its presentation and mechanics (such as delays) don't encourage bad or unfun gameplay. 

#### Wreck contents

Wrecks should ideally refrain from having certain items. This is primarily medical supplies, food, and hard cash; Salvagers shouldn't be able to loot wrecks and set up their own medical facilities or sustain themselves completely on wreck food to prevent them from becoming independent from the station, and finding large stacks of money invalidates the work Cargo Technicians put in with their own work. Salvage should, however, be able to supply Medical and Service with resources, and may be a core part of completing specific bounties for Cargo and providing items for Cargo Technicians to sell.

Salvage has had a tradition of getting "gamer loot" via wrecks, i.e., equipment that would be very strong in the hands of an antagonist (or worse, used to validhunt/shut down antagonists) when they return to the station. Some wrecks, especially those that become available after the magnet upgrade, may contain some stronger equipment and especially cosmetics, but to prevent undesirable gamer loot, Syndicate equipment should be heavily restricted from the wrecks.

#### Towing

pulling grids is fun idk what else to say yippee pew pew i'm so strong pulling shottle weee

### Smelters and Wreck resources

The main motivation behind wreck resources is to encourage Salvage to enter the wreck and loot it properly by hand. By making them have distinct visuals and contain rare materials, they also become something Salvagers will want to seek out (which will be a positive experience), rather than "scrap" for basic materials, which the processing step is already responsible for. 

By making the wreck resources designed specifically for this, we can also avoid Salvagers simply mashing a shuttle straight into the smelter wall, as they can be set to give little to no resources from this. Wreck resources that damage the smelters also strongly discourage Salvagers from sending the wrecks directly into the smelter walls. This does allow for some flexibility as experienced Salvagers may be able to partially smelt a shuttle to open a section that would otherwise be difficult to access, but Salvage should not be able to properly progress without stepping foot on and successfully defusing threats on the wreck. 

#### Salvage and station resources

Regarding the resources Salvage can uniquely supply to the station, this document primarily cites rare materials. With the content currently available, this can negatively impact gameplay for other departments (e.g., Science) where Salvage is _required_ to provide materials to enable core gameplay and rewards. The BreakSalv design allows new materials and equipment to be introduced as new wreck resources instead of existing materials, reducing the blocking effect of Salvage on other roles. However, as this would require a broader rework of the game's resource system and supporting content, and it does not affect BreakSalv's core gameplay loop, it is excluded from this design proposal.

### Aesthetic choices & inspirations

A large part of salvage's appeal is the aesthetics. Salvage should feel like a tough and cool job to do regardless of what they're doing. 

Aesthetically and tone wise, salvage should lean more on the dark comedy and horror of the game's tone. Space is vast, endless, and full of threats both rational and irrational. The wrecks salvagers pull in should reflect this, enhancing the tone of the job and ensuring gameplay variety. 

Wrecks should never feel completely mundane. There's a story to how this once functional ship, outpost or machine beyond understanding became a wreck.

#### Mundane realities of fantasy star-systems 

A big aspect to enhance tone is to have the actual interactions be extremely mundane. A wreck may be an abomination of flesh consuming metal as salvage literally dives into the belly of some cosmic beast, but mechanically they're treating its arteries the same way they would treat pipes, and its vital organs as obstacles or valuables. 

Salvage's progression should reflect this, armor upgrades being the result of stripping the tough hides off of alien monsters. Medicine being taken from self replicating cosmic beasts. Weapons being magical in some way, stealing the life force from their slain enemies. 

Salvage is practical, and the world around them is irrational, and this should be reflected as much aesthetically as it is mechanically. The aesthetics that a Salvager takes on should be shaped by the wrecks and situation they encounter. 


### Salvage progression

Salvage's equipment progression should primarily come from Science and what can be found/crafted from resources found on wrecks. As the better wrecks are only available through the completion of quests, this ties Salvage to the station and encourages crew interactivity as part of the core gameplay loop.

#### Salvage Specialist equipment

From the start of the round, Salvagers should have access to:

- A salvage hardsuit. Necessary for working in the Salvage Bay.
- Basic tools and toolbelt. For navigating and deconstructing the wreck during the extraction step.
- A survival knife and a portable kinetic accelerator. Used to deal with hostile mobs on wrecks, and as tools against environmental hazards.
- A grappling hook and separation charges. Necessary to complete the retrieval and processing step.

Salvage's upgrades should consist of improvements to these options, with a mix of mundane and not so mundane options. Some examples could include:

- Improved space faring armor 
    - Better defense or better mobility
- Better deconstruction tools
    - Welding goggles, insulated gloves, power tools, mining drills, explosives
- Better space mobility
    - Jetpacks, grappling hook+, forklifts
- Better grid dragging tools
    - Harpoons, forklifts, tether guns
- Better weaponry
    - Laser weapons, crusher melee weapons

Of note, the options listed above are very mundane, but fantastical options should be available they are just far more difficult to balance and as such have been excluded as examples in this design doc. Fantastical options should at best be equal to the best mundane options listed as examples above. 

### Relics & Theme Design

Both the wrecks salvage pulls and their quests should be consistent in theme and story. If Salvage pulls a wreck with a wizard relic for example, the wreck should ideally have signs that wizards were once there to enhance the immersion and mood of salvaging. In addition relics should always feel thematically in universe and should be designed as being owned by a faction with consistent themes. Regardless, these items should be distinct to salvage to give extra weight to the wrecks being pulled. These aren't just any old pieces of debris floating around, Nanotrasen has an interest in these scrap heaps. 

One key aspect of relics is ensuring the design is consistent. Making unique relics with unique effects and unlock conditions can easily bloat the scope of what Salvage provides, and such handcrafted specificity is to be avoided. This document proposes that relics have a _type_ and _faction_. The type informs what kind of object the relic is (e.g. a coffer, a sacrificial dagger, an encrypted disk) and the unlock condition associated with the relic. The faction gives the visual identity of the relic, and also provides a secondary effect to the unlock condition/effect. 

This design is not *as* economical as Science artifacts (which mix up *any* trigger and effect), but it does provide useful design handrails when adding new relics.

- Examples:
  - Relics of blood cult origin should be colored red and brown, and their unlock condition should involve the expenditure of blood in some way. 
  - Coffers should always require delivery to a specific individual on the station, but the unlock method and what is inside the coffer is dependent on the faction.
  - Relics of clock cult origin should be metallic and gold colored, their unlock condition should generally involve the bar or engineering. Additional effect can result in construction of useful machines and devices (e.g a perpetual motion generator).

This type of design is very useful in making players develop an understanding of the relic system; once they discover a relic of a specific faction, they will understand the theme implications for any future relic of that faction they find. Similarly, if they find a relic of a specific type, they will now know how any faction variation works with the base unlock condition.

The greatest difficulty in this is ensuring that that the effect is unique and interesting, and that the unlock conditions truly do require crew interactions. This is something that can be explored further in playtesting to find the components that work well for this purpose.

## Administrative & Server Rule Impact (if applicable)

Given the safety locks on the industrial smelters, the only moderation issue I could see is that an antagonist uses them for DAGD-level destruction by mounting them on a shuttle and trying to bulldoze the station. It would require the EMAG, which means it's limited to antagonists only, so the risk for self-antag griefing is fairly minor. 

## Technical Considerations

### New features

#### Grid dragging

Grid dragging has been implemented in a prototype. The main issue encountered is that grid mass is currently not very accurate. This would cause problems when determining pull strength and also how the grids should pull towards each other if neither grid on either end of the grappling hook is anchored. The prototype accounts for this, but other systems (such as shuttle power) would require refining to match these new values.

There would need to be some sanity checks such that a Salvager can't just stand on the station and keep a moving shuttle in place with just their equipment.

#### Separation charges

Splitting grids is already a thing that can be done with the RCD, but that operates on the principle of removing tiles entirely. There would need to be a solid system in place that not only deals with separation charges being capable of sitting on the edge between two tiles, but also that it can accurately split the grids in two. There may also be a desire to have "welding charges" that allow two grids to be connected, though that isn't vital to BreakSalv itself.

They main reason they should be implemented is to give mappers more freedom when designing the sizes of Salvage Bays and wrecks.

#### Wreck Resources and Relics

There would be a fairly substantial amount of new sprites for both wreck resources and relics, as the whole point of them is to stand out from what currently exists in the game. Furthermore, there will likely be changes and additions to systems to support their behavior, though reusing assets and components where possible is greatly preferred.

### Modified features

#### Station map considerations

Station maps would need to accommodate the new "smelter wall" concept. After briefly testing, it seems that a width of 9 tiles (the width of a singularity containment field) is around the ideal size to deal with pulling in wrecks for smelting. Most stations seem to have room to fit them without issue (except possibly Reach, though even there, there is room for a smaller version).

Still, all maps would need to implement a new Salvage Bay to be able to support BreakSalv. The new Salvage Bay should be accessible to Cargo Technician access; only the Salvager locker room needs to be job-locked.

#### Wreck map considerations

Many, if not all, of the existing wreck maps would likely need to be redesigned to comply with the wreck type system and provide an engaging wreck for Salvage to process in the manner that BreakSalv requires. The magnet must also be able to properly track how much of a spawned grid remains, which includes whether the grid is split off into multiple parts. This has been implemented in a prototype.

This document does not make a definitive statement on how the wrecks and wreck types should be implemented technically. There are many options here (some better than others), from handcrafted prefabs to fully randomly generated. To ensure there is appropriate environmental storytelling as well as the design intent of a mapper it may be desirable to use a combination of standardized layouts with sophisticated spawners, conditional rules depending on wreck type, and randomized room layouts, but this is ultimately a question to be answered during implementation.

#### Salvage Magnet

The salvage magnet would require a major re-design with its UI to support the new functionality. Some of what exists could probably be repurposed for BreakSalv however.

### Further Embodiments

There are a few ways that BreakSalv can be expanded upon. These are not necessarily part of the base implementation but may be worth exploring in the future:
- A stationary "spear gun" turret stationed in the Salvage Bay that Salvagers manually control to hook into wrecks that are too far for their grappling hooks.
- Industrial smelters being a Science research technology. I fear what the Passengers will do with this.
- More elaborate wreck mechanics inspired by Hardspace: Shipbreaker. Examples would be reactors that start a timer before needing to be processed or else explode, or heating/cooling pipes that could harm you if cut before being drained.
