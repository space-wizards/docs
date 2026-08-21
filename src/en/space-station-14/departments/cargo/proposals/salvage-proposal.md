# Salvage

```admonish warning "Retracted"
This content was requested to be retracted by its authors due to the following:
- Majority of authors no longer work on upstream
- Majority of authors no longer believe salvage can work upstream
- No current plants to implement this doc
```

| Designers                      | Implemented | GitHub Links |
|--------------------------------|---|---|
| EmoGarbage, Emisse, Mirrorcult | :warning: Partially | TBD |

_Most of these concepts are from emisse and mirror, emo is just chronicling them all down._

## Overview

This proposal serves to clarify and set in a stone the design goal for the salvage subdepartment.
Primarily, this involves the restructuring of the various gameloops they have (asteroids, wrecks, expeditions) and the modification of related systems such as ore processing, their shuttle, and other elements of the role.

## Background

[Mirrorcult's original salvage proposal](https://hackmd.io/@mirrorcult/salbidge)

Salvage right now is in a bit of a weird spot.
They have a decent amount of content, with a variety of tools, equipment, locations, ores, and various other things to work with.
Cargo has a legitimate gameplay loop that salvage can integrate with and theoretically aid the station greatly.

However, while all these elements _do_ exist, they aren't tied together in a way that best realizes their combined potential and lots of minor elements or issues consistently detract from the quality of the gameplay.

I don't think that there's one inherent element which is terrible and ruins all of salvage.
On the whole, there's a lot of stuff to work with and it just needs a steady hand to pull it together to deal with common issues like an excess of overly-powerful loot and being too disconnected from the station.

## Round Progression

Salvagers will have a soft 'progression' throughout the round in terms of the types of things they can do.
This serves to give them more structure while also allowing them to balance the risk-reward of what they want to do.

At the beginning, salvagers won't have anything beyond basic tools and will be relegated to the magnet for gathering materials.
This is the low-skill and low-risk end of the scale, where they can get accustomed to space and basic resource collection.

After salvage gets a decent amount of equipment and has enough equipment to allow them to navigate deeper into space, they can reach the mining asteroid.
The mining asteroid has larger depots of ores as well as rare ruins and dungeons on it.
However, it also has a greater number of threats that make it uninviting until salvage has gotten enough equipment to be able to deal with it properly.

From the asteroid, in various ruins and dungeons, salvagers can retrieve **expedition disks** which enable going on individual expeditions.
These serve as the final stage of salvaging content, with the entire team working together for an extended period of time.
There's the most danger here but also the greatest possible reward with large dungeons and tons of ores and natural resources.

## Magnet & Wrecks

The salvage magnet will function basically identically to how it works in mirror's original document and how it has worked ever since [the recent major rework](https://github.com/space-wizards/space-station-14/pull/23119).
The magnet allows salvagers to pick from a few different selections of wrecks and asteroids, giving them an overview of the general loot on them.

Asteroids serve as just a way to get needed resources.
They aren't particularly complex or difficult and can be thought of as the "chill" part of salvage.
Wrecks on the other hand have more unique loot, including scrap and deconstructable objects as well as some weak equipment that can serve to start getting salvage on the progression to the mining asteroid.
Wrecks may have low-level threats like weak mobs or non-fatal traps but are otherwise similar in danger to asteroids.

Grids pulled from the magnet should be fairly close to it.
Unaided by a jetpack, a salvager should be able to launch themselves from the magnet all the way to the grid.
The only requirement for doing magnet salvage should be a suit and oxygen.

The magnet should also be strictly bound to the station so as to reduce the potential for someone taking it and making it impossible for this base level work to be done.
This is accomplished by having the magnet, if attached to a small grid like a shuttle, physically pull the shuttle towards the grid at a strength that prevents it from moving and causing damage to the hull from colliding with the asteroid/wreck.

## Mining Asteroid

The mining asteroid serves as the step up in difficulty from the magnet.

Simply reaching the asteroid itself requires some kind of advanced transportation.
You could use the cargo shuttle but obviously this locks up cargo orders for an extended period of time and leaves you vulnerable to getting stranded.
Alternatively, you could build a custom small shuttle for salvage and use that to fly over to the asteroid.
As a final resort, you could get a jetpack (optionally a handheld mass scanner as well) and just fly all the way to the asteroid.

These options give salvagers a lot of variety in how they choose to get to the asteroid both in terms of speed and reliability.
They're also not exclusive to one another and can be done at any point during the round so as to not lock them out of all options.

The mining asteroid itself is significantly more dangerous than anything on the magnet.
There are significantly more mobs which are both more numerous and dangerous as well as more traps and environmental hazards that can quickly kill unsuspecting salvagers.
Larger structures embedded in the asteroid could also potentially contain minibosses or catastrophic threats.

However, the potential for resources is significantly higher as well.
The ore density of the mining asteroid is higher than of those pulled in from the magnet and the larger structures contain more loot than traditional wrecks.

This entire package offers up a greater reward for preparing and becoming skilled enough to best the challenges on the asteroid and collect the resources on there.
It provides variety and a bit of dangerous separation from the station while not being wholly disconnected due to the general impossibility of safety on the asteroid.

Structures on the asteroid also have the potential to contain expedition disks, which leads to the final section:

## Expeditions

Expeditions serve as a capstone salvaging event and are only meant to appear infrequently throughout rounds.
To gain access to an expedition, you must first locate an expedition disk somewhere on the mining asteroid, most likely gated in a dungeon or by some kind of bossfight.
Whatever the methodology is, they should be extremely limited in number and difficult to obtain.

Once the disk is obtained, the salvagers must return to the station and place it inside of the expedition console, enabling the expedition to be ran.
Expeditions are timed planet-side operations facilitated through a large central gateway near the vault.  

This allows non-salvage members and potentially the whole station to participate in the expedition, allowing for a more unique gameplay opportunity than the more solo-oriented salvaging.

The focus on the expedition is on the large dungeon full of goodies as well as threats and enemies.
You can also mine and harvest from the environment, but not nearly to the same scale as wrecks/asteorids/mining asteroid in order to balance in the infinite size.

Much like current wrecks, after a specified time limit (likely about 15 to 20 minutes) a final track will begin to play and players will need to make their way to the gateway in order to not be marooned on the planet.

## Loot and Rewards

The specific loot the salvagers retrieve has long been a contentious issue so this section seeks to clarify what exactly they'll be collecting.
The goal is to remove problematic items and giving them greater opportunity to benefit others while still retaining the 'upgrades' of better and better equipment.

### Mining and Ores

Mining ores is a relatively basic thing for salvage and has a lot benefits.
Lots of departments can use materials and rare materials are serve as progression for better equipment for salvagers.

They can be harvested plentifully via magnet salvage and the mining asteroid and less commonly on expeditions.

The rarity of ores is thus:
- Iron
- Quartz
- Coal
- Silver
- Gold
- Plasma
- Uranium
- Bananium

**Ore processing** will also be a slightly more involved process.

The goal of this is to reduce a common issue with the ore processor: utilizing it as diet infinite storage.
People commonly bring it onto a shuttle or similar structure as it can hold an infinite amount of materials invalidating proper storage methods. 
It also enables salvagers to get processed resources for themselves while on the go and incentivizes them to take the processor with them, leading Cargo to often be without materials.

My suggested solution is to make the ore processor unfeasible to run without a significantly resource intensive setup.
The power supply alone should be impossible to manage on portable generators, requiring at least a station-level power supply.
Furthermore, the ore processor will need a constant supply of nitrogen gas to in order to process ores into a refined state.

While this is trivial to supply on-station, shuttles will have a hard time gathering enough nitrogen to produce a constant flow for the processor. 

### Treasure

Treasure is pretty simple: it refers to any item that possesses a significant monetary value without any useful mechanical application.
Consider fantasy crowns and jewels and gold chalices.
These can be an exciting way to show off your wealth (who doesn't love walking around with a literal crown) while not actually affecting balance in a meaningful way.

As these are solely useful for selling directly in cargo, they also serve as an incentive to return and deposit treasure in order to enrich cargo.

The broad goal is just to have cool shinies that people can ogle at while not majorly disrupting any kind of balance and being useful to cargo.

### Scrap

Scrap refers to objects which are essentially condensed pieces of materials.

These can take the form of a few different things:
- Holdable scrap objects that can be processed into materials via a material processor inside of salvage
- Large destroyed machinery that can be deconstructed on-site
- Unpowered or disused on-station machines

Scrap serves as a diagetic way of acquiring materials and basic parts in bulk without having to resort to just dumping a crate of steel onto the map.
A destroyed thruster can deconstruct into 10 or 15 steel; a few of those can add up to a typical crate while also requiring more engagement in order to harvest.

This is generally more important in wrecks and dungeons where filling space and interaction is an important goal.
This is the kind of stuff that feels like actual _salvaging_.

Scrap that needs to be returned to a dedicated machine to process also serves as a reason to return to the department.
Dropping off scrap and processing it into relevant materials can be a nice source of downtime for salvagers and even cargo techs.

### Department Resources

Another major area for salvage is getting equipment for other departments.
A main issue in the past is that this loot was generally more useful to salvage than to the department and thus they would often keep it rather than ever returning it to the station.
The way to work around this is limiting items to things that don't have direct utility to salvage.

Medical can receive plants and minerals that can be synthesized into batches of chemicals.
Note that these should likely be precursor chems and not just direct omnizine or something.

The bar and kitchen can receive unique flora and fauna that can be made into special drinks and meals.

Science can get tech disks, research point disks, or even artifacts / artifact fragments.

This isn't all encompassing: the idea is that basically everyone should be able to get something minor of value out of salvage's wrecks.
It serves as an encouragement to return to the station and offload these items as well as fosters cooperation and relationships between different departments.

## Salvager Equipment

_The contentious one._

Salvagers should be able to find equipment to help them better deal with threats while they are exploring wrecks and dungeons.
In the beginning, salvagers only have the most basic equipment of a suit, belt of tools, a pickaxe, and maybe a few other basic items.

### Salvage Weapons.

This broadly includes the PKA, the combat knife, the dagger, the crusher, and the glaive.
None of these would be available in the starting salvage vendor and would all have to be acquired through searching wrecks.

The combat knife would be the most common with the dagger, PKA, crusher, and glaive following behind respectively.
These items should be defined by their relative utility in the environment--mild healing, reach against mobs, or light sources--not by damage numbers.

**No salvage weapon, even the most powerful ones you can find, should out-damage the captain's saber or the fireaxe.**

### General Utility

This just refers to equipment that grants useful abilities that salvagers would want to have.
These can be items that can be acquired traditionally in alternative or slightly modified versions of existing items to make them more or less lucrative.

It generally includes jetpacks (with and without extra capacity), large mobile light sources, gear like welding gas masks or mesons, and other various items that can serve to aid in surviving dangerous environments and moving around.
There can also be more mild rewards like high-capacity power cells and extra oxygen tanks.

The goal is just to add small rewards that help salvage either upgrade or replenish their pre-existing basic equipment without doing much else.

### Blueprints

Blueprints are a uncommon find on salvage wrecks that enable players to print new items off of lathes.
Unlike tech disks or similar items that sci uses, blueprints are restricted to a singular lathe and generally focus on consumables that salvage uses regularly.

This means things like mining charges, fultons, flares, etc.

The intent for blueprints is to give salvage a reward in being able to replenish their own stockpiles of consumables quickly.
It also adds variation between rounds as certain items become far more available than others as salvage unlocks blueprints at different times.
