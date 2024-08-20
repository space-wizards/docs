# Hydroponics Rework Plans

| Designers | Implemented | GitHub Links |
|---|---|---|
| Cerol | No | TBD |

## Overview

This is a proposal to improve Hydroponics (The department where players go to grow plants for the station) by enabling it to be a source of useful plants, unexpected results, and occasionally massive amounts of danger. Many of the ideas below are expecting the [Botany system rework](https://github.com/space-wizards/space-station-14/pull/31163) to be in place to make these changes easier/possible. 

## Background
Botanist is a unusually slow and safe Nanotrasen career path. The worst that can happen due to the system right now is a small kudzu outbreak. The biggest threat to the actual player is getting smote by an admin because you grew too many glowing tomatoes and lag out anyone walking past Hydroponics. This doesn't stick real well to the game's design pillars, so we need to come back to the ideas of being chaotic, silly, and interconnected. 

## Summarized Proposed Changes:

Hydroponics needs the 3 I's to become a good job on the station:
* Interconnections with the other departments. More departments will find Hydroponics potentially has useful stuff for them, and should be asking for it. This mostly happens by giving Hydro more stuff, with only Chemistry getting something removed to add a dependency on Hydroponics.
* In-round job progress. Over the course of a calm round, you should be able to go from making plants with random effects to adding the specific traits you want onto a plant. The expectations of a Botanist having a calm round will be decreased due to the other factors involved in this rework.
* Internal danger. A botanist should be able to cause problems for the stations at various scales. Usually intentional by a bad actor, but with enough room for accidents, carelessness, and sabotage to bring this up without warning. 

To make those happen, the Botany system needs 1 significant change.

## The Second Mutation List
The main change to the Botany code that makes Hydroponics better is fairly simple. You have a 2nd list of high-risk/high-reward mutations. Plants do not automatically roll on this list when mutating. To get access to this list, a plant must first be exposed to and consume gaseous plasma, which will now count as a mutagen for plants. After one exposure, the exposed plants will roll on this high-risk table for the rest of their lifespan when doing mutation rolls. Seeds from that plant will need exposed again separately to use the high-risk table. Botanists should have a small greenhouse room (2x2) with a simple atmos setup(a connector port, a passive vent, possibly a heater and lights outside) and 2 growing trays to use for high-risk mutations. Randomly dumping plasma into the main Hydropnics room in an attempt to get more of the powerful mutations is a move done accidentally, in desperation, or as sabotage. 

### Odds revealed
The rarer/move powerful chemicals currently available on the mutation list can either be moved to the high-risk set, or added to it with much better odds. Here are the odds of getting one of the rarest chemicals (omnizine):
* Getting the 'new chemical' mutation is 0.018% per mutation severity
* Getting the rarest set of chemicals picked is 5%
* Getting the chemical you want on that set is 17%.
* For 1u of mutagen, your odds of getting Omnizine added to the produce is 0.000153%
* For a whole bottle of unstable mutagen (30u), which in the system ends up being 6 checks of x5 base chance, those odds jump to 0.0046% per bottle. You need about 200 whole bottles to have a 1% chance of getting your choice of the rarest chemical in the normal mutation list right now. You can expect to see it once every ~600,000u of mutagen used in botany.

The high-risk mutation path should certainly have better chances of rare/powerful chemicals that that.

And for reference, here's the odds of getting each possible current mutation if you dump 30u of unstable mutagen (6 checks at 5 severity) into one tray:
69.5% (stat changes, per stat)
43.2% (tolerance changes, per tolerance)
19.7% (change species and 'fun' mutations)
10.3% (consume gasses)
2.7% (exude gasses)
1.07% (ligneous, kudzu, screaming, harvest type)
0.53% (change chemicals)
0.36% (unviable)

I do not offer a suggestion on the 'correct' odds of what mutations should be on either the normal or high-risk table. But now we can actually discuss the odds since they are no longer hidden behind 2 steps of bit-thermometer logic.

## Interconnections

Currently, There are 4 C-roles that want to talk to Hydro. 
* Chef wants a bunch of different plants, but rarely as many as Hydroponics can crank out. 
* Clown may want bananas. 
* Chemist may want carrots or ambrosia. Hydro will want chemicals from them to keep progress going. 
* Cargo might have bounties on produce.
* Crud, I forgot everyone else might occasionally ask you to grow weed. That doesn't counts.

This is insufficient. 75% of the list is often a single player on smaller stations. Hydroponics simply needs more things that departments and players will want.

### Unfortunate Chemist nerf
However, The chemist does not NEED to talk to the botanist in any capacity, since they have every reagent they need and can make any medication on the list without Hydroponics except aloxadone (which is worse than the cryoxadone you use to make it). They can make Oculine from raw materials before a botanist can grow and grind a carrot. I hate to suggest nerfs to other jobs as improments, but the Chemist should be required to go to Hydroponics for SOMETHING. 

My proposal is simple: remove potassium from chem dispensers and refills. This blocks the chemist from making poison/rad treatment drugs (Dylovene, Tricordrazine, Arithrazine, Hyronalin) and the typical Botany chems (EZ Nutrient and Robust Harvest) without interdepartment interaction. The Botanist will also know on round-start that they have an immediate need they should fill: grow bananas for the Chemist. They will also have the clown asking for bananas since they're already being grown. And the chef might wants a few for food. Look, there's now 4 roles at round-start that want the same limited resource. This is already a huge improvement for potential RP and round drama. This can also push antags to look for new attack routes. If they know the station has a harder time recovering from poison damage, they may want to consider options beyond "which gun drops people fastest" and look at "how can I force medical to waste time so I can accomplish my goals while they're occupied and people are injured?". Finallly, this blocks mindbreaker/heartbreaker toxins from being made on roundstart, adding the potential paranoia that someone asking for bananas now is going to turn around and be a problem later in the round.

### New Demands from New Departments
Hydroponics should be able to make stuff that's useful for other people, and that means new content. 
* Atmos: Botanists will want to get Atmos to give them a can of plasma to start the high-risk rolls. Atmos may want them to make plants that generate gasses, or will take plants that do.
* Engineering: Engineering might want plants that reliably make materials they can use for construction, which will be possible once the BGM is present and self-harvesting regrowing tower-cap/steel-cap is a viable target. Some of the high-risk mutations are actually useful as well, like plants bright enough to act as room lighting.
* Security: With reliable results possible (see BGM below), Security will possibly come asking for fruit that can heal them up before going to fight antags. A couple units of pre-emptive medicine can make the difference on which side ends up in medbay. Assuming that only Security gets their hands on those, of course.
* Medical: Botany, in a pinch, could be a backup medbay. It would need time and notice to get up to full speed, but it should be able to handle light to moderate medical treatment with the right chemicals in harvests. Pod people could be added as a last-ditch cloning setup in case of brain loss, or for ghost roles. 
* Science: Some interaction between high-risk mutations and science anomalies should be possible. Current proposal is a high-risk mutation that turns a plant into an anomaly.
* Antags: Botany should be a source of sneaky weapony and tricks for antagonists that want to stay quiet for a while. It currently could do this if the dice rolled in their favor, but without a way to reliably get specific results it's better to just grab an e-sword than grow your heirloom breed of death nettle. 

## In-Round Job Progress
Current Hydroponics has very little job progress, because the only system beyond 'grow plants' is 'gamble on random mutations'. Cross-breeding provides minimal control over moving traits between plants at no cost to the plants themselves, and that will remain. For reliable results, the department needs a way to make plants have certain properties.

### Botany Genetics Machine (BGM)
Despite the name, this does not introduce any genetics puzzles or mini-games for the player. Put produce in the machine to analyze it. This destroys the item inserted and takes a couple seconds. It will show the plant's type, traits, values, mutations, etc in full detail. Once a plant with a trait or mutation has been analyzed, you can create Botany Mutators that apply one of those to another living plant, which updates/replaces existing components/values. You can only pull 1 trait out of an analyzed produce, so if you have a plant with 4 great things you want to transfer, you need to analyze 4 different produce, and you may want those produce to make seeds or to actually use for something. Tough decisions can start showing up this way. This logic applies to both normal and high-risk mutations, and high-risk mutators do not require their target plant to have been exposed to plasma to work.

The BGM can save multiple values for a single variable as long as you've analyzed something with each of those values. Binary mutations can also be used to create mutators that remove that mutation. 

EX 1: A normal lemon tree get mutated to glow and consume 0.4 water. You could pull the water consumtion of 0.4 out of that sample, or the Bioluminescent to make other plants glow the same color, or any of the other normal lemon values. You would need a 2nd lemon to save the other.
EX 2: A apple tree gets a lot of mutations on a lucky streak. It has water consumption of 0.3, and 2u of pax, and it also emits frezon gas. You could add the water consumption 0.3 to the BGM's list besides the 0.4 from the lemon. Or add a mutation that gives any plant 2u of pax on harvest. Or a mutatator that removes frezon from the emitted gas list. You could also make mutators that remove pax from produce or add frezon to the emitted list with these apples, if you really wanted to. 

Botany Mutators are one-use items that only work on plants. They set values or add/remove components and are spent. This may require consuming additional biomass or an additional cost to create the mutators. These will normally be made by the BGM, but pre-made ones with particular stuff could be available elsewhere. Traitor items come to mind, allowing an antag to spend a few TC to immediately get a specific high-risk mutation without the time and effort, or grow plants with a specific chemical that helps their goals. 

This lets Hydroponics end up with powerful, useful plants over time. It requires them to engage with the random mutation system, but once they've identified something they want, they can keep it for the rest of the round. The biggest limiter on this is luck and time, as it can take a while for the mutation you want to actually show up. Additional resource costs on making Botany Mutators may limit down things, but the primary one is waiting for plants to grow and getting lucky on mutations you want to find. This doesn't exclude new Botanists from the process, since you could feed normal produce into the BGM to mix and match traits on baseline plants and still get a desireable result. It just may not be particularly flashy. A mutation-free plant with the growing speed of tobacco, the lifespan of tower-cap, the yield of cocoa pods, containing dermaline and bicardine to heal common damage, becomes a great snack for Security to munch on while hunting down troublemakers. Experienced players willing to gamble and experiment can do even better things.

(UNLIKELY: As a potential additional 'cost', each mutator may require a produce with the trait you want to make or remove from another plant. This might limit how fast they can be made, or means you need to use some mutators on additional plants in order to have a source for that mutator. This keeps the botanist growing and tending to plants consistenly instead of making 1 and walking away from their job. This would just mean that once the botanist has a good mutation, they will grow 1 repeat-harvest plant with that mutator applies and use its produce to make more of them later. Peas are a likely candidate as a source for this. We want to minimize entity spam, but also increase how much work botanists do for big results. I think this plan isn't where the right balance is for those.)

## Internal Danger
Hydroponics doesn't pose much threat to the people doing it. It's not a department likely to be attacked or overtaken by antags. Kudzu is the biggest threat, and it's stopped with the hachet in your toolbelt. Tomato killers and death nettle are the only things that might actually hurt someone else. This must change.

### The High-Risk, High-Reward Process
The new process to get to the high-risk mutations mentioned earlier is easy: give plants plasma. This presents a little danger, as you'll need to understand the basics of the Atmos items involved. In Hydroponics, its mostly a connector port for a tank of gas and a passive vent in a 2x2 greenhouse room. Advanced setups will be left to advanced players.

New to the code is that plants always check for plasma gas when growing, and consume it if present. Doing this sets a flag on the plant that tells it to use the high-risk mutation table instead of the normal one. Plasma absorbed will increase the mutation factor like unstable mutagen and left4zed do, and cause an immediate roll on the new table. The safe strategy will be to use small amounts of plasma on one or two plants to enable the list, and use liquid mutagens like normal. The fast strategy will be to pump in plenty of plasma and let the dice fall where they may.

Risks added for botanists on duty:
* The usual plasma risks: They mess up handling plasma, and blow themselves up. Or they leak a bunch of plasma into their room, enabling more plants to become dangerous than intended. Or someone else vents plasma into their room, requiring you to uproot everything or risk some hazards you didn't plan for.
* The bad mutations on the normal list hurt the plant. The bad mutation on the high-risk list hurt you. Plants might make their surrounding very hot or cold, trip you for being nearby, attack when harvested, spit lots of plasma into the air when they're harvested, or other awful things.
* The nastier versions of kudzu can show up on high-risk mutation rolls.

But what you get out of this process is worth the danger. Some examples:
* More fun mutations. RGBioluminescent fruit is a biodegradable disco ball.
* More useful mutations. Sunglow produce would have a light radius of 8, able to act like a permanent flare. Well, permanent until someone eats it.
* New species worth getting. Steel-cap could mutate into Plastic-cap, and make plastic sheets.
* Silly results worth showing off. A Giving Pit found in an eaten fruit could be touched to an item to grow copies of anything. A shotgun tree. A vodka tree. A Captain's ID tree. An Ian tree? I hope that fruit was safe to eat.

## Content Expansion Ideas:

### New plant species:
* Hellfruit. A plant not normally found on the station. Grows better in additional light, needs lots of water and nutrients, requires plasma gas to grow, heats the air around it, hurts the botanist if harvested without gloves, has a Yield of 1. But the fruit is so delicious and rare, someone will pay big bucks to eat it.
* Pitcher plants. Grows Plant Beakers, which hold an amount of chemicals based on the plants potency and chemicals contained. Starts off with just water. Requires some effort and luck to make this bigger than Large Beakers, but should be possible.
* Cherry tree. Delicious fruit for pies.

### High-Risk mutations:
* Good/Fun:
	* Jumbo. Large plant sprites, but a huge (x5?) multiplier for the chemical contents of the produce.
	* RGBioluminescent. Disco plants! Light cycles through colors over time.
    * Storyfruit: The produce will connect into the system that makes random library books, and read it out loud a sentence at a time.
	* Perfect metabolism. An effect that removes growth components that use nutrients or water.
	* Giving pit: When eaten, leaves a Giving Seed. Touch that to an item and the seed will grow into a tree that lets you harvest copies of that item.
* Neutral/Situational
	* Sunglow: A high-power point light. Radius is ~8 tiles, higher intensity. Acts like a permanent flare you can also eat.
    * New species. Varies by parent species. These should be more varied in 'power level', both good and bad. 
        * Plastic-cap. Like Tower-cap or Steel-cap, but makes plastic. Mutates from one of those two.
        * Spanish Cherry Tree. Also called Bulletwood. Mutated from the Cherry tree, can be fed steel sheets to get back bullets. Everyone wants untraceable ammo, right?
	* New chemicals. A second list of chemicals that makes it more likely for exposed plants to acquire rare chemicals via high-risk mutations. May share some chemicals with the base list, but they'll be easier to get on this list. Some may be moved to this list.
* Bad/Chaotic:
	* Fragile: Produce breaks and spills its contents if thrown or stepped on.
	* Anomaly: plant turns into a plant anomaly, and needs Science to come handle it.
	* Thorned: Produce or plant damages user on touch. Might already be implemented by death nettle somewhere.
    * Hostile: Plant attacks you for some damage when you touch it. Scales with potency.
	* Dangerous Kudzu types. There's a few in the code that should become possible to acquire.
	* Furnace/Cooler: Starts dramatically increasing/decreasing the air temperature around it, and has extreme temperature tolerances.
	* Anti-Killer: weed killer heals this plant dramatically, possibly also de-aging it some. Really bad if this also get a roll for kudzu.
	* Big mob: Spawn an 'Audrey Jr' style monster that inherits all the EntityEffect mutations on the plant. Can break windows, attack people, and inject the plant's chemicals into them on attacks. If possible, eats people that are dead/crit. Signficantly more dangerous and durable than tomato killers. Possibly only available via pre-made mutator a traitor could buy with TC, and apply to a plant they crafted themselves, or specific to a mini-antag that wants to make a mean green mutha in outer space.