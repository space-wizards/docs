# Onsite Mining
## Overview
Onsite Mining is a redesign of the mining department that focuses on these things:

* Fun gameplay
* Sandboxy solutions
* Integration with the station

The core game mechanic here is the **Megadrill**: A machine that miners build on meteors on appropriate resource nodes ("Wellsprings") to extract ores. While the Megadrill is powered, it **produces resources in waves**. Also, while it's powered, **monsters spawn continuously**, attempting to destroy the drill and the miners. This turns mining into, in essense, a **tower defense subgame.**

## Round flow
In the intended gameplay loop, the mining team follows this flow:

1. The miners prospect meteors to find the best candidate. They want a meteor with good Wellsprings (preferably multiple for efficiency), good enemy spawn locations (easy to plan around), and overall a good shape for building on.
2. The miners relocate the meteor to the salvage bay for easy construction, medical safety, etc. (optional but highly suggested)
3. The miners prepare and plan for fighting. (They would clearly benefit for help from other departments like Engineering, Medical, Security etc. if available) (optional)
4. The miners build the Megadrill and related machines. (In the proof-of-concept screenshot, they use a SUPERPACMAN, but other ideas will be listed later). The drill is connected to the monster spawn nodes via something like pipes or wires, and only function if at least one spawn location is connected to the drill via an uncovered network of those pipes, to ensure a continuous pathing from the spawn to the drill. With multiple monster spawn nodes connected, the resource generation is faster or higher quality.
6. The miners pray (optional) and start the machine, beginning the first extraction wave.
7. Monsters spawn at the connected monster spawn nodes, which are predictable locations based off the meteor's shape, properties, difficulty and such (see step 1)
8. Monsters keep spawning while the drill is in operation. After a certain amount of time has elapsed, it starts to spew out resources.

**Successful outcome:**
The miners stop (spin-down) the drill when they have enough stuff, or when they give up and need to flee, or the drilling node is exhausted (~10 to 30 minutes, depending on Wellspring generation and Drill upgrades). They can turn it back on, but stopping the drill and starting again is less efficient than leaving it running - it needs to ramp up to 100% before producing any resources.

The miners should then take their loot inside, visit Medical, feed Sci, beg Sec for guns, get a drink or such -- because they moved the meteor to the salvage bay, this is not as far a trip as it would be otherwise. They can work with Sci to upgrade the drill machine to higher difficulties and more efficient, more challenging waves; they can also reconstruct or deconstruct the operation, and start back at 1 if they want.

**Bad outcome:**
The miners are overwhelmed and they quickly know it. They shut the drill down early, getting only enough ore to feed sci briefly, and clean up the last few monsters from a safe distance. They pop by medical to heal, ask the CE to borrow an emitter, reconstruct their defenses, and try to start the machine up again.

**Worse outcome:**
The miners get overwhelmed. They flee, calling over radio that the drill monsters are taking it; the monsters knock one miner out and the other drags it away. Then, the monsters attack the drill; when it's destroyed, kaboom. The drill was only on level 1 difficulty, so the explosion only takes out most of the meteor it's on.

**Traitorous outcome:**
Right before starting the drill, one of the miners swipes an emag into the drill, unlocking greater intensities. They prepared for this, of course -- the drill takes much more power at higher difficulties and they ensured proper power flow -- and their cohort doesn't notice the drill machine's sprite is now sparking until the spawn points start putting out goliaths instead of ore crabs. The other miners are quickly overwhelmed, and the traitor pockets the singlets telecrystal that the drill spits out before it explodes like a syndicate hardbomb.

# Game Design Rationale
### What this design does
This doc **imagines a new subdepartment that covers the resource acquisition needs of the station ("mining")**. This is currently part of salvage, but a relatively unpopular one because the gameplay loop for resource gathering has these problems which Onsite Mining avoids:
1. **Current Mining Isn't Fun**. This is the big one; for most people, hitting rocks and dragging a bag of rocks to station is not fun. The salvaging aspects (see below) are fun, therefore people do the fun gameplay loop instead. Furthermore, this is an *intrinsic* gameplay problem, meaning that regardless of the reward, the gameplay isn't fun; good gameplay is ideally *fun* to do even if you don't have any gain from it.
2. **People don't do mining** (because it's not fun), which makes the station suffer, because everyone needs materials; Cargo can provide materials, maybe, but again this wouldn't be particularly fun.
3. **Current mining distances people from the station in a way that undermines the rest of the game**. This is to be avoided, because it limits interaction and impact both on the miner and on the station. The miner doesn't care the station is on plasmafire. The miner isn't at the bar because they are 1000m away. The miner isn't getting maints slashed, they are in space. The miner isn't getting rescued by the paramedic. etc.

### What this design DOES NOT do
**Does not replace Salvage.**
Salvage is the gameplay loop where you focus on *exploration and discovery,* with typical rewards being rare items and technology that can't be acquired elsewhere. This is currently vgroid or expeditions or space wrecks or such. This design doesn't cover that category of gameplay, but it does separate out the resource extraction loop so that salvage can be something else without *also* having to be resource extraction. Salvaging is already *intrinsically fun*, in the sense that exploring wrecks, fighting mobs, and navigating a dungeon is fun just on its own even without loot; the loot is an additional extrinsic reward. For example, salvagers still have a reasonable amount of fun even when they die on a godforsaken rock and are round removed.

### Why do a Tower Defense 
Space Station 14 supports a substantial amount of constructions, machines, mounted weapons, and triggerable / linkable devices, all of which could see more use (especially ship weapons); this design encourages creative use of constructions and, as a direct result of intrinsic gameplay, cooperation between departments to see those constructions made. This will improve the health of the supply department by enabling more ways for other departments to support them both with expertise and mechanics.

###  Inspirations
This design draws primarily on certain **Deep Rock Galactic** missions where the main characters defend their machines from alien bugs while extracting materials.

## Questions

* What if a 500 Mothroaches situation happens and too many monsters spawn?
If the drill spawns exceed a certain count (let's say 15 to be safe?), spawning pauses and the mobs become stronger (essentially, gain structural damage until they can break out). If that doesn't solve it within a certain timer, the drill starts to failsafe (:godo:) and lose durability, eventually exploding (which _should_ solve the problem). The DragonRiftComponent is already configurable in this way, as an example of a spawner.

* What if someone creates a nifty setup that routes the monsters to the station instead, using, say, conveyor belts and the hand teleporter? 
That's cool, I hope they're an antagonist. The drill failsafe will still trigger and the monsters will start being a problem for everyone else to deal with.

* What if the Drill Team is bad at their job and can't even beat a level 1 crab rave?
Awesome! Ask the engineering team for help and ideas, they'll probably have a few! If it's REALLY tough, maybe Sec will send a cadet to just shoot the crabs for you? More people can help with resource extraction and take a cut.

* What if I create a perfect design that fully solves the tower defense puzzle forever, huh smart guy? What if my perfect meta design undoes your tower and I stand triumphant on my grand laser-throne?
This is not a design problem so long as the puzzling is still fun for the players. If a strong meta forms, we can add new monsters or other complications to ensure continued variety.

## Items that need to be implemented
* **Drilling machines and connection pipes**: These will need sprites and programming work - construction nodes, new components, UI work for the drill.
* **Changed magnet, new debris**: These grids should be summoned by a new version of the existing salvage magnet, but allowing for persistent grids (or allowing for the grids to be persistent if anchored -- see docking pitons)
* **Grid-moving devices**: Machines that miners use to position the Wellspring to dock to the station. This could be anything from a harpoon gun to a tractor beam, or possibly an attractor that fires a projectile that impulses the grid towards the shooter. This is potentially cool for ship-to-ship combat or other applications (like a shipbreaker). This is also optional (shuttles are the alternative to moving grids).
* **Docking pitons**: a construction that docks a loose grid to another grid when activated, allowing it to secure the Wellspring and secure it to the station for use; it could potentially also be part of channeling power through to the drill. This is technically optional given enough willingness to extract in space and provide the drill with power (and changes to the magnet). The clamp is probably
the most technically challenging piece of this, but would go a long way towards making the Drill Operators station-adjacent and station-impactful. This could *also* be useful in ship-to-ship combat. 
* More monster AI: This is probably a good thing to have and may not need much changes — the NPCs should attempt to fight their way to the drill. Ideally we also take a look at optimizing for enemy groups.

Later work could expand to more monster types, more interactions with other systems (the same system could be used for Mega-Artifacts instead), and more antag interactions (what should the emag do to the drill? what should it do to the tractor beam?)
