# Shipbreak Salvage Proposal

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| SlamBamActionman | SlamBamActionman et al. | :x: No | TBD |

## Overview

Shipbreak Salvage (or BreakSalv) is a new primary gameplay loop for the Salvage Specialist job, focusing on pulling in shuttle wrecks to the station and manually disassembling them for valuable resources before sending the remaining structure into a huge industrial shredder for even more materials. It challenges Salvagers in how to deal with a variety of environments, types of hazards and ways to extract materials in an expedient manner, rewarding thorough work with a high resource yield for the station, tool upgrades and bragging rights. BreakSalv emphasizes EVA work on the outside of (but still on!) the station with a sci-fi industrial aesthetic unique to the department.

## Background

### Previous Salvage iterations

Throughout the years of SS13 and SS14 there have been multiple types of "Salvage Specialist"-type jobs and mechanics, far too many to list exhaustively here. In SS13 the main ones were Shaft Miner, Lavaland and Bitrunner. For SS14, it's been Magnet Pulls, Space Debris, Expeditions and Vgroid. 

At its core, Salvage is meant to be a "resource generator" job. A resource generator describes a role that creates new resources for other roles to take advantage of; Cargo is an obvious one with its bounties and cash (turning into purchased products and some materials), and another is Botany with its produce (turning into reagents and some materials). Salvage in SS14 has primarily focused on lathe materials, with some being soft- or hard-locked behind the job such as silver or uranium. BreakSalv intends to continue with this specialization as it fills a niche that other resource generators do not, providing high volumes of basic materials and rare materials difficult to acquire elsewhere.

Something that has been a recurring pattern with both SS13 and SS14 implementations of Salvage is their unavailability. Whether it is Lavaland, Expeditions or Vgroid, there has been a strong focus of having Salvage leave the station in favor of a highly challenging environment. This has given Salvage a bit of an identity as being something hardcore PvE players engage with, but also came with the downside that said players effectively "disappeared" from the round, not caring about station events and being difficult to reach for antagonists - or if one of the Salvagers were antagonists, having an extremely easy system to dispose of their fellow Salvagers. This has been felt potently in SS14 where there were periods of the game where Salvage used shuttle gameplay to effectively leave the station for the entire duration of the round, creating their own medical treatment and lathes, getting antagonist-level loot and using Cargo's purchase mechanic to completely bypass interacting with the rest of the station. 

That being said, there have been elements of Salvage that allow unique gameplay, themes and game mechanics to shine through. PvE-focused combat, variation via mapped magnet pulls, mining, dungeon/world generation and shuttle building are some of the things that Salvage has showcased. Not all of these were necessarily conducive to station-aligned gameplay (dungeon/world generation being part of Expeditions is one such example) but it shows Salvage affords a rather large design space that would otherwise be inaccessible through other jobs.

Because of this, BreakSalv will not attempt to capture all the aspects of previous Salvage iterations, but it does use what has come before as an inspiration and launchpad for its new design. As you read this document you will note mechanical similarities to *some* previous implementations of Salvage (most notably Magnet Pulls). That is a result of those systems being a good fit for the ideas core to BreakSalv, rather than BreakSalv building upon them just because they exist.

As the name suggests Shipbreaker Salvage is also inspired by the game [Hardspace: Shipbreaker](https://store.steampowered.com/app/1161580/Hardspace_Shipbreaker/). It does not try to recreate the game's mechanics in SS14, but rather attempts to emulate the feeling of engagement and fulfilment that breaking apart a spaceship provides in the same manner as the game does. The game provides a good aesthetic and emotional goalpost for what BreakSalv attempts to be (and it's a pretty good game!).

## Features to be added

BreakSalv is the primary gameplay loop for the _Salvage Specialist_ job belonging to the Salvage subdepartment of the Cargo department. The goal is to produce resources for distribution to the rest of the station in the form of high volumes of basic materials and rare, unique materials and equipment that are otherwise difficult to procure. This is achieved by spawning in wrecks of old derelict shuttles, extracting rare materials from them by hand and then shredding the remainder of the shuttle for basic materials.

The work of a Salvager takes place in the _Salvage Bay_, a location exposed to space on the outside of the station in close proximity to the Cargo department. While the majority of work Salvage performs happens inside of the Salvage Bay due to the station-locked machinery there, they should have a small locker room inside of Cargo for suiting up and easy access to the rest of the Cargo department to ease the transfer of materials.

BreakSalv has a gameplay loop that can be broken up in three primary parts: retrieval, extraction and shredding. 

### Retrieval

**Retrieval** is the process of spawning and getting wrecks to the station so that their resources can be extracted.

Wrecks are pre-made grids themed around being decommissioned shuttles or destroyed station sections. To get access to wrecks, Salvage has a unique console in the Salvage Bay called the _Salvage Magnet_. 

#### Salvage Magnet

The Salvage Magnet (or just magnet) provides an interface where Salvagers can select one of a small selection of wrecks that they want to work on called the "Wreck Selection" view. Each entry lists information of what type of wreck it is and what resources are expected to be found on it.

One of the key pieces of information listed in a magnet entry is the _wreck type_ the wreck is. Types describe some sort of environmental hazard or property of the wreck, providing challenges unique to the wreck type and gives Salvagers variety and choice in the wreck they want work on.

Some examples of wreck types:

- **Superheated:** Contains compartments with superheated plasma actively on fire. These must be vented into space before being accessed.
- **Infested:** Contains a large number of space mobs that will attack the Salvagers. These mobs are resistant to piercing damage, making ballistic weapons ineffective.
- **Overgrown:** Kudzu covers the wreck, along with trees blocking pathways.
- **Radioactive:** Contains a large number of radioactive objects that require quick removal.
- **Defended:** Contains dangerous turrets (ballistic and/or laser) and mines that must be disposed of.
- **Shadowy:** Covered in the visually obscuring shadow anomaly fog that has to be navigated or removed via flashes.
- **Electrified:** Features electrical grilles and shocked airlocks that require either insulated gloves or strategic turning off of APCs.
- **Fortified:** Contains powered access-locked and high-security airlocks with strong walls. These must be hacked or destroyed to reach the resources inside.
- **Anchored:** Has a mini-station anchor inside of it that must be manually turned off before the wreck can be moved.
- **Distant:** Spawns at a further distance away from the station than normal. Jetpack recommended.
- **More!** The idea is that these wreck types can be expanded upon for more variety. 

Only one wreck may be active with the magnet at any given time. Once a wreck has been selected the interface changes to a new view as described in the [Magnet Evaluation](#magnet-evaluation) section.

#### Towing

Once a wreck has been spawned, it will be located somewhere in nearby space in close proximity to the Salvage Bay. If the wreck is not within the player's viewing distance, Salvage may use a _Mass Scanner_ mapped in the Bay to locate it. When compared to previous iterations of Salvage, the wrecks are meant to spawn much closer to the station. Regardless, Salvage will want to move the wreck closer to the Salvage Bay as it will make it faster to extract materials from it and is a necessity to complete later steps. This is known as _towing_.

To tow the wreck, Salvage will have access to _grappling hooks_ and _magboots_. While grappling hooks on their own simply drag the user towards the hook, when combined with the grounding force of the magboots Salvagers are able to pull grids towards each other (or in the case one has a station anchor, only the one without gets pulled). Ideally Salvage will be able to stand on the outer rim of the station and use their grappling hooks to drag the wreck until it is within working distance; once it is, they can proceed with the next step.

### Extraction

**Extraction** is the process of manually retrieving rare materials from wrecks.

On the wrecks there will be resources of various kinds that Salvage will want to move off the wreck and onto the station by going onto the wreck and picking them up by hand. In its simplest form this may be a stack of material, but where the extraction process becomes more interesting is the unique _wreck resources_ that may spawn on wrecks. 

#### Wreck Resources

Wreck resources are scraps, technology gadgets, structures and hazardous containers containing rare materials. Salvage will want to remove these from the wrecks before the shredding step takes place to ensure a high material yield and/or prevent damage to the Salvage Bay. No one wreck will contain all types of wreck resources, and ideally wrecks should specialize in a specific resource that can be extracted (such as a radioactive wreck containing many radioactive wreck resources that provide uranium).

Wreck resources can not directly be used as materials but need to be processed first. The _recycler_ is a good option for this as it is a station-mounted machine and Salvage can easily have their own. As a rule, wreck resources should _not_ focus on steel or glass materials, since those are primarily obtained through the shredding step.  

- **Two-handed:** Requires two hands to pick up. 
- **Large:** Big enough to require dragging and can't be held or put in containers.
- **Fragile:** Easily broken if thrown around recklessly.
- **Mounted:** Attached to a wall or integrated into some machinery that requires partial deconstruction.
- **Radioactive:** Emits radiation.
- **Electrically Unstable:** If destroyed or processed incorrectly, will emit an EMP pulse.
- **Explosive:** If destroyed or processed incorrectly, will explode.
- **Pulsating:** Occasionally emits a gravity pulse that pushes away other objects around it.
- **More!** The idea is that these wreck resource types can be expanded upon for more variety. 

### Shredding

**Shredding** is the process of finalizing a salvage operation by grinding up the remains of a wreck into base materials.

Once all valuable wreck resources have been extracted and the Salvagers feel finished with the wreck, it is time to get rid of the wreck itself. For this, the Salvage Bay has a large wall of _industrial shredders_, and _separation charges_.

#### Industrial Shredders

Industrial shredders work by grinding up any tile that comes in contact with the open front of the machine, destroying it and any structure attached. It is essentially a recycler specializing in grids. As wrecks are mostly made up of metal and glass parts, this becomes the main method Salvage produces steel and glass sheets. To prevent Salvage from simply sending a fresh wreck straight into the industrial shredders they provide a remarkably lower yield for wreck resources and items that can already be recycled, and some wreck resources may harm the shredders if inserted into them.

Since some individual grid tiles could feasibly be made with less than one sheet of steel material, those tiles only have a percentage chance to produce a sheet. E.g. lattice, which is made of 1 steel rod (equivalent to 0.5 steel sheet) has at most a 50% to produce a sheet.

Each shredder acts as a conveyor belt that is only able to push items perpendicular to its opening; since each Salvage Bay is meant to have a line of shredders (known as the "shredder wall") this means the material can travel along the line to a pick-up location (either in the Bay or in Cargo proper). Shredders are *only active* when there is an active wreck being worked on via the magnet and turn on/off via device linking to it. In the event that a shredder gets damaged (because of meteors or misconduct) it should be repairable, e.g. via welding. 

Shredders do not have the safety mechanism of recyclers which means they deal contact damage, but the damage is low enough that it isn't an efficient method of murder. You wouldn't want to stand or walk through a shredder for a long duration but just touching it for a few seconds won't be lethal.

Shredders are *only* able to shred wrecks attached to the linked salvage magnet. While realistically there shouldn't be a limit, this is an instance where moderation efforts need to be made as having them able to shred any grid would make major griefing and self-antagonism too easy to perform, and also allow crew to easily weaponize the shredder wall against shuttle-based antagonists (despite how awesome it sounds, we do not want crew to mount shredders to a Cargo shuttle to bulldoze the Xenoborg Mothership). There is the possibility to remove this limitation as an EMAG interaction for the salvage magnet however, though if that is to be implemented it should come with a station-wide announcement to alert crew to the impending danger.

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

After some time has passed (short enough to not feel restrictive, but long enough that Salvage can't just cycle wrecks), Salvagers may choose to despawn any remaining grids of their wreck using a "Despawn Wreck" button on the magnet. There is an incentive to fully shred the wreck however. If the Wreck Percentage is at 100% a previously greyed out button "Claim Processing Reward" becomes available. Clicking this button rewards Cargo with a monetary boost and announces in the Supply channel that Salvage finished processing the wreck along with the Shredder Efficiency and Wreck Time. 

Once either button has been pressed the magnet interface returns to the wreck selection view (after a short delay to give a moment to breathe) and Salvage is free to select a new wreck to work on.

### Salvage Progression & Magnet Upgrade

As some wrecks will contain useful tools and equipment to better deal with the three core parts of BreakSalv, there will be a natural progression inherent to Salvage's gameplay. Science may also provide upgraded tools through research and usage of Salvage's materials. Some wrecks will likely be discouraged by being too dangerous or slow to process without these upgrades, lending to a sense of becoming more powerful over the round.

As a way to add further progression and provide some breathing room for Salvage, BreakSalv also features an upgrade to the salvage magnet's capabilities. This unlocks after Salvage has a certain number of 100% Wreck Percentage completions in the form of a greyed out "Magnet Upgrade" button in the wreck selection view becoming available. Pressing this starts a fairly lenghty progress bar during which no new wrecks can be selected. Salvagers are encouraged to spend this time taking a break on the station and/or visiting the other departments for upgrades.

Once the progress bar has completed the Salvagers are rewarded with a new wreck option in the wreck selection view that features a higher tier of wreck. This higher tier is intended to be more challenging by featuring multiple wreck types at once, more resources and are generally larger.

#### Salvage Specialist equipment

From the start of the round, Salvagers should have access to:

- A salvage hardsuit. Necessary for working in the Salvage Bay.
- Basic tools and toolbelt. For navigating and deconstructing the wreck during the extraction step.
- A survival knife and a portable kinetic accelerator. Used to deal with hostile mobs on wrecks during the extraction step.
- A grappling hook and separation charges. Necessary to complete the retrieval and shredding step.

Upgrades to the Salvager's arsenal could be:

- Improved hardsuit with higher movement speed/defense.
- Welding goggles/gas mask, insulated gloves, improved welding equipment.
- Jaws of life and power drill.
- Simple laser weapons.

## Game Design Rationale

BreakSalv is intends to position Salvage as a primary resource generator for the station by utilizing the unique game mechanics opportunities afforded by working on the outside of the station. 

BreakSalv intends to provide the following experience:
- Hard work not for the faint of heart under a sci-fi megacorp industrial aesthetic. Salvagers should feel like they are cool by braving the dangers and efforts inherent to their job.
- Visible results from their work. Seeing a huge pile of materials come out of the shredders should make the Salvagers feel like they are contributing to the station.
- Completionism and optimization. Salvagers will want to hit 100% on the Wreck Percentage with high Shredder Efficiency and low Wreck Time, but may situationally forgo it for a faster, lower reward. Good Salvagers can brag about how fast they completed a wreck.
- Moments of rest. Since all Salvage work consists of constant manual effort, salvagers shouldn't be stressed into continuously working. Not having a time limit and forcing small delays between wrecks (and a longer for the Magnet Upgrade) are meant to encourage this.

There are a few things that BreakSalv is intentionally trying to avoid:
- Isolationism. While Salvage operates on the outside of the station, since the focus is on magnet wrecks and the shredders Salvagers do not have much reason to leave the station proper. At worst a Salvage team may occasionally need to leave the station grid to retrieve a wreck that has spawned further out, but this is only intended to be a temporary excursion lasting for the duration to get out there and towing it back. Salvage should be expected to be found in the Salvage Bay at a level similar to Botany and Xenoarch.
- Easy sabotage/round removal features. BreakSalv doesn't intend to solve the strategy of just yeeting a dying body into space, but otherwise the equipment used for BreakSalv shouldn't be highly efficient antagonist/griefing strategies. The industrial shredders can damage things but aren't as fast as just stabbing someone with a Syndicate weapon, and the separation charges should be as easy to interupt as trying to disconnect a grid using an RCD. 
- Overabundance of materials. All wrecks should follow guidelines for how many resources may be on them and what loot may be found such that a competent Salvage team can't make Cargo completely redundant. Similarly, Cargo itself shouldn't make Salvage's work redundant to the station. Said guidelines should be constructed through playtesting to find the sweetspots and aren't covered in this proposal.
- Spawning in wrecks, grabbing loot and de-spawning them: That's not to say a wreck can't have a _little_ bit of "loot", i.e. equipment/cosmetics only benefitting Salvage. But the wrecks and the rewards should be balanced such that it's not desirable for Salvagers to just spawn in a wreck and not actually work on or shred it.

### BreakSalv in detail

This section addresses specific design choices with the various features BreakSalv aims to implement.

#### Salvage in space

Previous iterations of Salvage have had a problem with Salvage "fucking off into space" and not engaging with the station for the majority of the round. This has less been the fault of space itself and rather the Salvage mechanics that encouraged leaving the station; shuttle building and space debris encouraged hopping from debris to debris to gather resources, with the vrgoid asteroid being the epitome of encouraging Salvage to leave for extended durations and make "mini-stations" with medical capabilities and even their own lathes replacing the need for the station altogether. Expeditions disconnected Salvage from the station map entirely and fultons meant Salvagers didn't need to return to the station to hand over the materials. 

BreakSalv locks Salvage to the station grid by making heavy use of the magnet and the industrial shredders. There is little to no reason to engage in gameplay away from the station and by being in so close proximity to the station there isn't a strong incentive to set up station-replacing equipment. This means that Salvage will always be accessible to react to station events and become easier to locate e.g. for antagonists. 

There are still some pros and cons with working on the outside of the station. EVA work is a very unique mechanic to the space setting that otherwise only really Engineering deals with as part of their primary gameplay loop, is aesthetically cool and leverages the open space afforded by it. This does limit crew-job interactions however, as there is no Salvage "front desk" and the Salvage Bays would not be by any high-traffic area (unless a station specifically designs its layout around it). On the other hand, tying Salvage's work to the Salvage Bay will make them massively more accessible compared to previous iterations. Paramedics will have an easier time accessing Salvagers in case of lethal explosions, Cargo & QM will generally know where Salvagers are while working, Engineers can pass by Salvagers when traversing the outside of the station and there is a much lower barrier of entry for Passengers to help out by virtue of the Salvage Bay being more open.

The Salvage Bay also affords a good point for holopads, and with the Wreck Timer being purely cosmetic there is no penalty for Salvagers to pause their work to engage in conversation or do tasks for the station.

#### The Salvage Magnet and Wrecks

Wrecks provide variety to the round, both in the selection of available wrecks but also what contents they may provide. They are also excellent opportunities for environmental story-telling; all wrecks should have some sort of "lore" behind it that ties into its wreck type and what the wreck depicts. Wrecks should not be created through pure random generation but be hand-crafted grids by our talented mappers. Wrecks should ideally not have just a single way that they can play out to create emergent gameplay, and Salvagers should feel they can make meaningful choices with what wrecks they spawn in and also in how they approach them.

As mentioned in the previous section, the salvage magnet becomes part of what ties Salvagers to the station. Despite its unassuming appearance it is a critical part of ensuring that BreakSalv flows smoothly and a lot of care and consideration needs to be taken to ensure that its presentation and mechanics (such as delays) don't encourage bad or unfun gameplay. 

A potentially contentious part is the Upgrade Magnet button. Forcing Salvagers to not engage with their primary gameplay loop may be seen as killing the momentum, however considering that it is optional and up to the Salvagers when it should be activated (in case Salvage just wants to do more wrecks right this moment) and that it only unlocks after Salvage has done some wrecks already should hopefully place it at a point where Salvagers are looking for an excuse to take a break. Ideally it will be implemented such that Salvagers can go "We'll do one more wreck and then hit the bar while the magnet upgrades".

#### Grappling Hooks

pulling grids is fun idk what else to say yippee pew pew i'm so strong pulling shottle weee

#### Shredders and Wreck resources

The main motivation behind wreck resources is to encourage Salvage to enter the wreck and loot it properly by hand. By making them focus on containing rare materials they also become something Salvagers will want to seek out (which will be a positive experience), rather than "scrap" for basic materials which the shredding step is already responsible for. 

By making the wreck resources designed specifically for this we can also avoid Salvagers simply mashing a shuttle straight into the shredder wall, as they can be set to give little to no resources from this. Wreck resources that damage the shredders also strongly discourage Salvagers from sending the wrecks into the shredders, though experienced Salvagers may be able to partially shred a shuttle to open up a section that would be otherwise difficult to get to. 

## Roundflow & Player interaction

As previously mentioned, Salvage will have some inherent progression through what is found on the wrecks, but may also be assisted by upgrades from Science in the form of useful equipment. There isn't as much of an endgoal for Salvage as there is an escalation of stakes to match the stronger equipment, with larger volumes of rarer materials and more challenging environments becoming available/feasible as the round progresses.

Wrecks should ideally refrain from having certain items. This is primarily medical supplies, food and hard cash; Salvagers shouldn't be able to loot wrecks and set up their own medical facilities or sustain themselves completely on wreck food to prevent them becoming independent from the station, and finding large stacks of money invalidates the work Cargo Technicians put in with completing bounties. Salvage should however be able to supply Medical and Service with resources, and may be a core part of completing certain bounties for Cargo and providing items for Cargo Technicians to sell.

Salvage has had a tradition of getting "gamer loot" via wrecks, i.e. equipment that would be very strong in the hands of an antagonist (or worse, used to validhunt/shut down antagonists) when they return to the station. Some wrecks, especially those that become available after the magnet upgrade, may contain some stronger equipment and especially cosmetics, but to prevent undesirable gamer loot Syndicate equipment should be heavily restricted from the wrecks.

In terms of what resources Salvage should focus on, this document focuses primarily cites rare materials as what Salvage can deliver uniquely to the station. With the content currently available this can negatively impact gameplay for other departments such as Science where _requiring_ Salvage to supply materials to enable core gameplay and rewards. The design of BreakSalv is such that new materials and equipment could be introduced as wreck resources to make poor/non-existent Salvage work less blocking for other roles and good results only enhance the station's gameplay. As this would involve a larger rework of the overall resource system in the game with supportive content and not impact BreakSalv's gameplay loop, it is left out of this design proposal.

## Administrative & Server Rule Impact (if applicable)

Due to the safety locks on the industrial shredders, the only moderation issue I could see is that an antagonist uses the shredders for DAGD-level destruction by mounting them on a shuttle and trying to bulldoze the station. It does require the EMAG which means it's limited to antagonists only so the risk for self-antag griefing is fairly minor. 

# Technical Considerations

## New features

### Grid dragging

Before writing this document I had a short sync with Slartibartfast who has experience with grid movement. He said it was likely feasible to implement something like a grappling hook pulling, though it depends on how well Box2D supports continuous forces being applied to a grid. A `DistanceJoint` on the hook may be sufficient however so signs point towards this not being a difficult thing to implement.

The main issue likely encountered is that grid mass is currently not very accurate. This would cause problems when determining pull strength and also how the grids should pull towards each other if neither grid on either end of the grappling hook is anchored. If this becomes an issue, grid mass calculations would need a pass to ensure it's more accurate.

There would need to be some sanity checks such that a Salvager can't just stand on the station and keep a moving shuttle in place with just a grappling hook and magboots.

### Separation charges

Splitting grids is already a thing that can be done with the RCD, but that operates on the principle of removing tiles entirely. There would need to be a solid system in place that not only deals with separation charges being capable of sitting on the edge between two tiles, but also that it can accurately split the grids in two. 

In terms of testing BreakSalv, separation charges aren't necessary. They main reason they should be implemented is to give mappers freedom when designing the sizes of Salvage Bays and wrecks.

## Modified features

### Station map considerations

Station maps would need to accommodate the new "shredder wall" concept. After briefly testing it seems that a width of 9 tiles (the width of a singularity containment field) is around the ideal size to deal with pulling in wrecks for shredding and most stations seem to have room to fit them with no problem (except possibly Reach, but even then there is room for a smaller version).

Still, all maps would need to implement a new Salvage Bay to be able to support BreakSalv. 

### Wreck map considerations

Many if not all of the existing wreck maps would likely need to be redesigned to comply with the wreck type system and provide an engaging wreck for Salvage to process in the manner that BreakSalv requires. The magnet must also be able to properly track how much of a spawned grid remains, which includes if the grid is split off into multiple parts. This should be doable via a simple tracking component, hopefully.

### Salvage Magnet

The salvage magnet would require a partial re-design with its UI to support the new functionality. Most of what exists could probably be repurposed for BreakSalv however.

## Further Embodiments

There are a few ways that BreakSalv can be expanded upon. These are not necessarily part of the base implementation but may be worth exploring in the future:
- A stationary "spear gun" turret stationed in the Salvage Bay that Salvagers manually control to hook into wrecks that are too far for their grappling hooks.
- Industrial shredders being a Science research technology. I fear what the Passengers will do with this.
- More elaborate wreck mechanics inspired by Hardspace: Shipbreaker. Examples would be reactors that start a timer before needing to be processed or else explodes, or heating/cooling pipes that could harm you if cut before being drained.
