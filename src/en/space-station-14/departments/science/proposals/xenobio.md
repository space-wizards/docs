# Xenobiology (Mutant Lab)

| Designers     | Implemented | GitHub Links |
|---------------|-------------|--------------|
| EmoGarbage404 | :x: No      | TBD          |

## Overview

**Xenobiology** is a """new""" Science subdepartment. 
The subdepartment comes with no roles but instead a variety of machinery that allows scientists to harvest and fuse cell samples from various flora both on and off station.
These splices can then be grown into living mutants, who must be contained, cared for, and grown until they can be dissected and studied in order to gain research.

## Background

Science's current methods for point generation consist entirely of just XenoArcheology and Anomalies. 
Both of these subdepartments have perfectly fine gameplay loops that integrate well with the game, but leave a gap in gameplay that serves to be filled.

XenoArch is very reliant on other departments for supplies and artifacts yet the threat of the artifacts is largely contained within science.
Anomalies are the opposite: they require very little input from outside of science to generate points but create a large threat that exists entirely outside of the science department itself. 

This iteration of Xenobio serves to fill the gap between these two while also introducing some generally well liked thematic ideas--aliens and gene modification--in a way that integrates well with the current design of the science department.

## Cell Collection

Collecting cell samples from creatures across the station is the primary 'resource' of Xenobio.
This concept takes loose inspiration from /tg/'s cytology.
Scientists are equipped with a set **biopsy punches**, which are single use tools that deal a small amount of damage to the mob they're used on and produce a **biopsy sample**.

Biopsy samples can then be taken to science, where the **Cellular Sequencer** can be used to collect add the sample into the **Cellular Database**.
Cell samples from the database can be printed at the cost of biomatter (scaling with rarity of the cell sample).

Not all xells are created equal, however. 
For the purpose of Xenobio, the part of cells that matter is their instability.
This is essentially a scaling factor that affects the extent of mutations.

Common creatures, like rats, dogs, or other on-station animals, have a low instability and will only have one or two mutations associated with the cells.
More rare creatures, like space animals, have a higher instability which results in more mutations of more serious degrees.
Even still, finding something exceptionally rare, like a blob or a xenomorph, can yield extremely unstable cells that can cause lots of mutations.

This basically means that while you can have a basic set of cell samples from just looting animals from the station, any more exotic combinations will require collaboration with cargo, botany, or other jobs in order to get access to rarer creatures or the closely-guarded head pets (Ian makes a fine DNA source).

## Cellular Fusion
Once you've collected a reasonable stockpile of cell samples, you can use the **Cellular Fusion Chamber** to fuse cell samples.
Cell fusion is a relatively simple procedure that mostly just involves selecting two distinct samples and fusing them.
Fusing samples carries a small plasma cost as well as a failure chance.

The chance to fail as well as the cost is dependent on a few factors:
- The amount of times the current sample has already been spliced
- The instability of the cells used (uses the higher value)
- The difference in stability between two samples

This sample can then be further fused with more samples, creating a more and more complex and unstable sample.
One completely finished, the sample is loaded into a **Mutagenic Cell Injector** (MCI) and is ready to be used.

This overall encourages people to try a variety of simple combinations and not tacking on endless small modifications to create super beasts.
It can still theoretically be done, but it's much more resource intensive.

## Mutant Creation
Once you have acquired a loaded MCI, you're now ready to deliver your payload to your lucky test subject.

By default, you'll be supplied with a box of monkey cubes and some N2O. 
Knock a monkey out, inject it with the MCI, and then stick it inside one of the various **Growing Vats** scattered inside of the xenobio lab.
Once inside, you simply need to wait for the mutant to grow.
When finished growing, use a plunger to pull it out.

If you pull it out prematurely, you may simply get a regular monkey or (in an unfortunate case) just a pile of bloody slop and goo. 
If you leave it in too long, the mutant may wake up and become angry, destroying the vat as it escapes.

Growing Vats must be stocked with a decent level of nutriment and saline in order to facilitate the mutation process. 
You'll need to monitor the levels and replenish it as they deplete.
Failure to do so may lead to your mutant coming out dead.

Whatever the case may be: you've now grown a mutant.
Get it inside of a chamber and start experimenting.

## Mutant Care and Growth
You have a disgusting mutant in a cage: now what?

Your main goal is to care for the mutant in order to help it grow.
This requires satisfying certain conditions for it. Primarily:
- Food: vegetables, meat, live animals, etc.
- Temperature: Average, cold, warm, boiling
- Pressure: Average, low, or high
- Enrichment: Toys, playmates, prey, entertainment.

When you satisfy these conditions, the mutant slowly grows.
Making sure that these conditions stay constant is important, as mutants will react more strongly when they have a condition satisfied and then it goes away.

But what happens when you don't satisfy these conditions?
In short: bad things.
Improper diet and environment may cause the mutant to weaken and slowly die, preventing you from researching it properly.
Uncomfortable or unsatisfied mutants may additionally grow aggressive, lashing out at their cage and researchers.

This may cause them to break out and escape their cages, at which point they may ravage all of science or even escape out into the station.
Keeping them happy should (mostly) prevent this, however, so it's essential to do so.

## Research
Once a mutant has finished its growth, it's appearance will change and scientists will be able to conduct research.
This is when points are generated.

First, the scientists must figure out how to kill the mutant.
Gassing the chamber with N2O is a smart bet but it may come down to lasers or even good ol' fashioned hand-to-hand combat.
Whatever the case, it must be dead.

Then the corpse can be taken to the autopsy station and a post-mortem analysis can be done.
This is simply done with a large scanner machine while surgery isn't implemented. 
After the machine finishes the post-mortem, research will be added to the server and the corpse can be disposed of.

Research is awarded based on the instability of the creature as well as the number of fusions in the original sample.
However, sequences with minimal variation compared to previous ones will be penalized and give reduced research.

The goal is to encourage experimentation with different base cell combinations, pushing players to find lots of different creatures to experiment.
This lends a huge cooperation and discovery factor to the subdepartment.