# Chemistry
> _Medical's bartender, and sometimes an arms or drug dealer._

## Concept

Chemistry is to medical what service is to the rest of the station: a means of producing goods on-station for the benefit of others.

First and foremost, Chemistry is interacted with through the Chemists that reside in medical, who primarily focus on producing medicinal items for the rest of the department.
Their central challenge revolves around balancing their supply of chemicals with the demands of the medical department, as well as the skills to turn their raw resources into usable items in a timely manner.

Secondarily, Chemistry is interacted with by anyone that wants to manufacture drugs and produce effects that cannot come from elsewhere.
It is a complement to Construction in that it focuses around the transformation of raw things into new results, often for antagonistic means when done outside the bounds of its designated department---steel into secret walls, plants into performance-enhancing drugs.

## Design Pillars

### Pillar 1: Chemistry is for everyone

Chemistry, applied both within Medical and outside of it, should not be fundamentally isolated from the rest of the game---the basic elements of temperature, resources, storage, and others are equally shared between the Chemist making medicine, the Passenger making gunpowder, and the Chef making a cake.
Nothing should be fundamentally gatekept behind any one job---a Chemist might have a thermobath, a Passenger might have a welding tool or a fire, and the Chef might have a grill, but these all interact with the same mechanic of _temperature_ in their own ways.

Mechanics that appear in chemistry should be shared with other parts of the game where possible, as part of making the world overall feel more interactive.

Chemistry can also rely on mechanics from other parts of the game to build up its own layers, instead of requiring unique-to-Chemistry mechanics that present a learning curve.

> Do not: The Chemist lab in medical has the only means of processing two reagents into a new thing, and someone wanting to do something to a pill and some goop they have has to convince them that it's worth their time, otherwise they are completely shut down.

> Do: An antagonist on the run ducks into a closet to combine a pill and some goop they found into something useful by holding up a welding tool to a half-pint glass a few times to heat it up enough, but a medical Chemist would've been able to do this easier if they were the antagonist or the antagonist asked them.

> Do not: The only way to electrolyse chemicals is to use a machine in the chemistry lab.

> Do: The elctrolysis machine in the chemistry lab is the safest way to electrolyse chemicals, but you can use a makeshift stunprod in a pinch, or just put a wire from the station's power network into the beaker, at the cost of efficiency and safety.

### Pillar 2: Chemistry is not a loner task

How Chemistry fits into the game loop of players interacting with it should not fundamentally isolate them from interacting with other players---past basic round-start chores, Chemistry should be focused on the journey of putting something together as it brings players into contact with each other and the environment, rather than focusing on making an intricate minigame with little interaction with the outside world.

> Do not: A Chemist, wanting to make a specialty request, primarily fulfills this by spending 15 minutes crafting an intricate recipe tree in the lab, without being able or incentivised to interact with others. All of their time is spent actively juggling equipment or pressing buttons. They don't have any long-form-but-unsupervised processes to start and go check on something else. They have no need to check with others, or others outright cannot help them with their task.

> Do: A Chemist, wanting to make a specialty request, has to tackle the choice of how they're going to get the prerequisites---can they cooperate with a Botanist to get precursors from plants, should they see if Atmospherics has anything to spare, or should they tank the cost of synthesizing from raw and have to order some cartridges from Cargo to replace the cost?

> Do: A Passenger wants to synthesize gunpowder without asking the Chemist to make an obviously suspicious request. They have to scrounge for the ingredients in maintenance, either directly, or indirectly in forms that can be broken down with equipment given to various jobs. They also have to source something from Botany and convince the Chemist to give them 10u of something, or perhaps they can convince Cargo to fill an order for a cartridge of it.

### Pillar 3: Resource management reigns supreme

Resources and accesss to them is the main pillar that forces players together on Space Station 14---and Chemistry is no different.
Anyone working with Chemistry should expect to have to manage resources and balance competing concerns to decide what they're prioritizing, what they're doing after they get something, and what they aren't doing.
Players interacting with Chemistry from different angles should have different resources to interact with it, and they should be incentivized to have these resources flowing between different players.
Nobody should be able to have a full supply of everything, and players should not be so inundated with resources that storage becomes the primary concern over availability.

At the same time, resources should be flexible in terms of how they are acquired, with different pros and cons to consider.
Cargo may be able to get you a cartridge of pure carbon, but that requires that you have money _and_ that Cargo is operational.
You might consider processing some wood from the Botanist or maintenance to get carbon instead in a pinch.

Storage itself is also a resource, for both a Chemist and for anyone carrying chemicals---available options to carry and distribute medicine should differ from passenger, to traitor, to physician, to nuclear operative.

Storage should be balanced based on ease/speed of the chemical being given to someone---cartridges are unwieldy outside of the ChemDispenser on multiple levels, beakers and bottles require force drinking, pills require a force feed and have a delay, and syringes, hyposprays, and autoinjectors are generally smaller than anything meant to carry chemicals.

There should be no "best storage" for reagents.

> Do not: A nuclear operative corpsman has an entire medbay's worth of chemicals in their bag which allows them to account for every situation for an entire mission without ever having to worry about conserving or running out of chemicals.

> Do not: A Chemist has all the resources they will need for the round at the start of it to produce every medicine Medical might need that round, and then some. If they run out, they can order a ChemVend to get another set of roundstart chemicals.

> Do: A Chemist has access to a limited set of chemicals that can be used with discretion, and if they run out, they have various means of replenishing various chemicals, but there is no one-size-fits-all solution to get everything.

> Do: A traitor chemist has access to the chemicals they need to prolong their fights, but not enough to keep them fighting forever. They will eventually need to step back and replenish their supplies after a couple of fights.

### Pillar 4: Chemistry is not required

The act of Chemistry can be a boon to a round, but just like other mechanics, explicit player interaction with it should not be outright required for basic function of any department it participates in.

**That is not to say that Chemistry's absence shouldn't be felt.**

Construction is a good reference point---it is not required until destruction happens, and e.g. air starts leaking out of the station.
Someone that can do Construction can properly seal the patch and re-air the room, but firelocks will drop on their own and prevent the situation from worsening.

Likewise, for Medical, Chemistry should be able to help with properly fully healing someone, but Medical should not be reliant on Chemistry to get a patient stable and going on their way.

## A Design Hypothesis

This design hypothesis is meant to be a sketch of what the Chemist job and Medical's relation to it should look like in practice in order to fulfill the prior pillars, and is explicitly meant to be tested and refined to better fulfill the stated goals as well as overall player enjoyment.

### Medical Supply
Rather than the current status quo of Chemistry getting an entire warehouse's worth of raw chemicals (against Pillar 3) and Medical being wholly reliant on them to turn those into usable medicines (against Pillar 4), I posit the alternative setup of roundstart supplies:

Medical should have a plentiful supply of basic precursor chemicals available to the whole department. For Offmed, this set would be Inaprovaline, Dexalin, Paracetamol, Dylovene, Hyronalin, and Kelotane. These chemicals should be worth using in their own right, and should be able to let Medical operate at a workable capacity without a Chemist (Pillar 4).

Chemist's job at the round start should be transformed from synthesizing medicines wholly from scratch, to transforming the roundstart supply of medicines into something better. Given that this eliminates a lot of the need for raw materials at the start of the round, we can correspondingly cut Chemist's access to raw resources _substantially_, outright killing the ChemVend in favour of the ChemDispenser having slightly more chemicals per type, as well as some intermediates (Pillar 3).

The availability basic medications also contributes to more interesting resource considerations---should a Chemist track down more Kelotane from e.g. Botany, or should they use their limited supply of Carbon and Silicon to put it together? (Pillar 2, 3)

If a Chemist needs more of a raw resource, they can opt to break it down from something they can get their hands on, or order an individual cartridge from Cargo for a non-trivial price. (Pillar 3)

### The Lab

Synthesis of chemicals should largely be straightforward---the availability of resources should be the main constraint, not players' abilities to memorize or reference a guidebook/spreadsheet/etc. and press buttons correctly. (Pillar 3)

The machines themselves as-is are mostly fine and would have their positive traits emphasized by resource constriction.

In particular, electrolysis, centrifugation, and grinding take center stage once the ready supply of raw materials is tightened up---their ease of use should be brought up to the same standard as the more readily available machines.

The ChemDispenser becomes the main source of raw chemicals roundstart, given the absence of the ChemVend---it should operate on cartridges that can only be used by the ChemDispenser, and these cartridges can be found roundstart, or ordered individually from Cargo at great price.

To avoid these cartridges becoming the undisputed best container, they should not be refillable, or at the very least, not refillable with arbitrary chemicals.
Being able to re-insert carbon into a carbon cartridge _may_ be acceptable, but ideally, the UI should be such that experienced players make few mistakes that would demand re-inserting raw resources into them.

Given the tighter constraints on resources, the ChemMaster's infinity storage/lavabeaker behaviour can be removed outright, and the machine refocused on packaging chemicals.

Overall, there should not be an "all-in-one" machine for chemistry.

The dispenser dispenses, the master packs, the electrolysis unit electrolyses, so on and so forth.
And of course, the various machines should have various budget equivalents, i.e. just pouring things, handmade pill press, putting a stunprod in a beaker, using a microwave, etc.

### What Medicines Are There?

A recipe tree that focuses on depth of synthesizing over getting resources tends to cause Chemistry to isolate for a long time (against Pillar 2), and is only really facilitated by a large roundstart supply of raw materials and the triviality of getting more of everything (against Pillar 3).

The set of available chemicals needs to be trimmed heavily.
A new medical system as planned will permit the burden of interestingness be moved from overcomplicated chemical trees and choices to be more equally shared by Medical overall.

#### Basic/Precursor Medicines

As outlined above, these should be decently available to Medical roundstart and fairly easily able to be reacquired if the roundstart supply depletes.
These are your kelotanes, your dexalins, and your hyronalins.
Medicines that can do their job, but not particularly well.

#### Chemist Medicines

Some medications can be synthesized without too much hassle given the presence of a Chemist, and are fine being straight upgrades to the precursors, given that a lot of them will be consumed in the process of synthesizing them, and resource constraints should prevent them from being more bountiful than their precursors in a round.
These are your dermalines, your bicaridines, your dexalin plusses, your arithrazines.
Medicines that are the bread and butter of a well-supplied medical department.

Basic toxins may also find their way here, with the usual resource constraints in mind---if you spend all your raw resources on turning medicine into toxins, you're going to have to explain yourself to the CMO raising an eyebrow at you.

#### Specialty Drugs

Once a chemist has gotten the basic medical supply out, the results of further synthesis should change from being a straight upgrade that simply needs time to do, to medicines with unique effects that don't overlap with other medicines, and that require unique things to make happen. (Pillar 2, 3)

The general balance here should be that they _could_ be synthesized directly from raw, but that would heavily tank the limited supply of raw elements.

The Chemist should seek to find precursors, from e.g. maintenance, Botany, Salvage, et cetera. (Pillar 2, 3) over always opting to deplete their supply of raw elements.

These would include drugs such as leporazine (for its effect on temperature), narcotics, performance enhancing drugs, and specific cures like oculine.

This is also the category where antagonist-specific drugs can be introduced, such as Vestine or Lead to let antagonists make a limited supply of something unique to them.

More potent toxins usually end up here, either requiring substantially unique materials or outright antagonist-gated ones to synthesize.
