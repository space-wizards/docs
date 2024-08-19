# Botany Rework Plans

| Designers | Implemented | GitHub Links |
|---|---|---|
| Cerol | No | [Pt 1: Mutations](https://github.com/space-wizards/space-station-14/pull/31163) |

## Overview

This is a proposal to improve Botany (The system involving plants growing in-game) by making it support the ECS code pattern better than it currently does. This is a large task, but can be broken into 5 or so pieces to make the upgrade manageable. This is not a proposal to change Hydroponics (The department where people do the growing of plants), though most ideas for reworking Hydroponics require a more flexible Botany system.

## Background

Botany isn't awful, but it's not very expandable. It's locked down to essentially what SS13 Botany was, including being a single function with a lot of checks, with a few parts of it commented out for reasons. It should get updated to use components as modularly as possible, so that each part of the Botany system becomes extremely flexible and gives us much more room to create interesting plants and scenarios involving them. This requires breaking the current Update() call into several pieces, and making lots of components that can reference systems for those pieces separately per plant. Ideally, this also means that much more can be done to seeds in YAML.

This isn't the first time this idea has been brought up, but this should be the most complete writeup so far. This write-up does not assume any previously discussed PR that was cancelled due to requiring Plant ECS will be implemented after these changes, or be implemented in the same way the original author envisioned. I am also not an expert on RobustToolbox, so some of the expectations below might not be the best way to do things or I may have missed some details.

## Summarized Proposed Changes:

When a Botany system tick happens, all Plants go through their Update process in the following steps:
* All attached GrowthComponents are run through the appropriate system. Plants may not all have the same GrowthComponents. 
* Health or status changes will be handled by the Botany system with the results of the GrowthSystem calls.
* All MutationComponents are checked by the system. These are a global list that applies to all plants. The back-end logic for mutations will be simplified for performance and clarity.
    * Simple random rolls with low (< 0.01f) probabilities will replace the multi-bits-as-genes current setup that obscures how rare and potent a mutation actually is. Bits-as-genes can be re-added when someone makes a Botany Genetics system, which is out of scope for this proposal.
    * MutationComponents themselves will determine their requirements, thresholds, probability, and effects.

Seeds and Plants also gain an OnInteract component check, and Harvest actions are also handled by a system and component(s) as well, to allow other things.

## Out of Scope:

* Kudzu: Not directly relevant to Botany code beyond being a possible mutation. 
* Hydroponics: Department changes will depend on these changes being implemented, and be done after all of these.
* Additional Mutations: Existing mutations will be ported to the updated system. New ones will be future PRs.
* Balance: This is a system port. Any numbers that aren't obviously a bug should be ported over as-is. Some math may be simplified for human convenience. Hydroponics shouldn't change in popularity only due to the backend changes proposed.
* Guidebook: This will be it's own PRs worth of work, if the guidebook should automatically detail out plants or mutations they way that Chemistry details out recipes. The written behaviors for Botanists should not change.

## Technical Details 

* An earlier proposal said plants should just be entities in a container. This is the ideal goal, but that's probably better done after each other step in the process has been compartmentalized out from PlantHolder.Update(). Step 1 is making all the SeedData values become components and systems, then step 2 is moving those to the new entity.
    * Alternately, step 1 is to make a Plant entity with the SeedData variable info, and work on converting everything to components from there. Seed components should just be copied from the prototype to the plant.
* BotanySystem should do all the actual checking for plants that's done in PlantHolder right now. PlantHolder should just be the interface used to interact with plants most of the time. In current state, PlantHolder is effectively the 'plant' for interactions with SeedData being the plant's core stats, and we want the plant to be a new entity instead of a component when this is done. 
* Plantholder should remain, but it will mostly be limited to managing the lights on the grow trays instead of the plant's lifecycle and holding the resources the Plant consumes.
* GrowthComponents / GrowthSystems should be added, so that Botany isn't checking a fixed set of values to handle plant growth. This replaces the water/nutrient/gas/light/heat checks currently present, and lets plants do stuff when they would grow besides 'health/age go up'. This also means plants only check for what they care about, and don't process needs they don't have. It also allows the addition or removal of these components to be a mutation.
* Mutations become components that get checked by their own requirements. This way, some mutations could have specific circumstances to make them show up, and others can remain purely random rolls. On that note, the existing mutation system's bit-gene checks will be replaced with 2 random rolls: 1 to check the odds of the mutation happening this tick (easy to scale to the current odds), and a second check if the first passes to see how much the value changes by for non-boolean mutations. This will help performance and human understanding of mutation odds. I see this as a global list of available mutations, and each plant will check the entries on the global list when it's eligible to mutate. Individual plants could have specific mutation effects added to them that only possibly occur on them, but I think this is a future change. 
    * Mutations become EntityEffects that run on the plant. This might be easier than what I was thinking before.
* Harvesting gets a component/system that run on harvest. This allows plants to do more than just drop produce when they're picked. The 2 existing behaviors become Components here, for one-shot or repeatable harvests. Worth pointing out that auto-harvest would be a GrowthComponent that fires off the Harvest action, because the plant picks itself when its grown enough.
* A new component type for onInteract hooks could be added to seeds and plants, to make them responsive to things before planting them and for doing more than just harvesting them. A plant that has utility while it's alive instead of just at harvest time is a thing we cannot currently do, and might motivate people to keep a plant around as long as possible instead of just aiming for maximum Potency.
* The Plant entity should take the visuals of the plant itself from PlantHolder, and store components for growing on itself. SeedData, if any fields aren't handled after all this, should become a proper component applied to the plant.
* Seeds may still end up storing some data, like a list of components to be applied to the plant, but it should be significantly smaller than the current set of values on SeedData.

## Work Split

This should be multiple PRs, so that incremental improvements can be made and work potentially divided among multiple contributors. This is roughly what I expect the order to be:
* Mutation System rework (minus stat mutations and harvest type)
    * This should probably be a bunch of EntityEffects and components to fire them off.
    * Mutations should be defined in YAML similar to how chemicals are. 
    * Simplify this system down to just be low percentage rolls instead of the fake-gene-bit setup it is now. The conversion math for those is (1 / totalBits(275 today) / bitCount), so a 5-bit mutation would just be Prob(0.00072 * severity)
* HarvestComponents rework
    * 2 EventEffects that fire off and create the actual produce. Copies all the mutation components active on the plant to the produce. One destroys the plant, the other reverts it to the previous growth stage.
* GrowthComponent/System and seed prototype rework.
    * Most of the current checks in PlantHolder.Update() should get split out into their own component (EntityEffect derived? Or new components with a new system that runs on its own?)
    * Auto-harvest becomes one of these, since it runs at Update() and not OnHarvest().
    * I am not sure how much of SeedData remains after this. I suspect it does still exist, but mostly for which prototype the seed creates at harvest and which species it can mutate into.
* Update Mutation System to include mutations for GrowthComonents and HarvestComponents
    * This must be delayed until both the new Mutation system and new Components are in place, because this is where those systems touch.
* Plant entity replaces PlantHolder/SeedData
    * Update PlantHolder, ideally by moving much of its logic to Plant and what can't be moved should reference the Plant entity instead.
    * Update other Botany systems to use Plant instead of Plantholder where appropriate. 
    * Ensure tools work on Plant entities. PlantHolders may redirect clicks to a Plant in them for conveneince.
    * Update ReactPlant() in Chemistry to use Plant instead of PlantHolder
    * While we're at it, update the SolutionContainerSystem to the new version that doesn't have an Obsolete warning.
* add OnInteract component hooks for seeds and plants
    * This PR would be optional since its technically not part of the current system code, but it will allow for more options in the future.

In addition, this would mean that people could contribute new content to the updated parts before the full system update is implemented. New mutations could be added once that system is reworked without causing extra work for the other step in the process (Mostly).

## Future Potential (Ideaguys dump)

This is a list of stuff that should be possible with the new Botany system that is hard/impossible in its current state, and what it would prove. This is not a proposal to make any of these ideas available in-game after this is implemented, but these should be done to prove the system meets its goals and left in as debug/admin stuff if possible or removed if not. If nothing else, let these serve to inspire additional future changes.

* Decorative plants become actual plants with no GrowthComponents, but can have mutations applied to them. [Proves GrowthSystem isn't hard-coded to any specific requirement]
* Hellfruit: A new flex goal for Botanists to show off their skills. Requires extreme growing conditions, and harvesting it is dangerous. Uses more water and nutrients than most plants, requires plasma gas to grow, heats up the air around it, and hurts when picked without botanist gloves. You'd want to mutate this into something safer. [Proves GrowthComponents can be stacked, and the new Mutation system can add or remove GrowthComponents instead of just changing numbers]
* Pitcher Plants: These can be harvested to collect Plant Beakers, which will have a maximum capacity based on Potency. They otherwise work like normal beakers. [Proves HarvestComponents can be customized to handle the extra work on setting capacity for the container]
* Giving Tree Seed: Rub this seed on an item, and that item becomes the prototype that the tree produces at harvest. Mutations that affect produce such as Bioluminescent can be applied to the harvested item. [Proves OnInteract effects are possible for seeds, and that mutations aren't locked to Produce prototypes]
* Spanish Cherry tree: A plant that makes bullets when you feed it steel sheets is a reason for Security to actually come to Hydroponics, and provides a reason to maximize lifespan of a plant over Potency. [Proves OnInteract for plants are properly implemented]

Looking farther forward, what could this system enable for the Hydroponics job? None of these are implementable in this proposal, but should be doable once it's complete as part of a future Hydroponics rework.
* Botany Genetics Analzyer: Put produce in this machine to analyze it, which destroys the item and takes a couple seconds. It will show the plant's type, components, values, mutations, etc. in full detail. You may pick 1 of those to save into the machine, and can create one-use mutators to apply that component or value to another growing plant. [Proves nothing, but provides a way for Hydroponics to reliably make super-plants with time and luck.]
* New Mini-Antag: Mad Scientist. Starts with unique/rare seeds, and has ways to manipulate plants into dangerous products. Has plant-related goals. May not necessarily start as a Botanist. [Proves Hydroponics is a source of chaos and danger if constantly ignored, and not just for growing big fruit or space weed.]
