# Xenobiology (Mutant Lab)

| Designers     | Implemented | GitHub Links |
|---------------|-------------|--------------|
| EmoGarbage404 | :x: No      | TBD          |

## Overview

**Xenobiology** is a """new""" Science subdepartment. 
The subdepartment comes with no roles but instead a variety of machinery that allows scientists to harvest and splice genomes from various flora both on and off station.
These splices can then be grown into living mutants, who must be contained, cared for, and grown until they can be dissected and studied in order to gain research.

## Background

Science's current methods for point generation consist entirely of just XenoArcheology and Anomalies. 
Both of these subdepartments have perfectly fine gameplay loops that integrate well with the game, but leave a gap in gameplay that serves to be filled.

XenoArch is very reliant on other departments for supplies and artifacts yet the threat of the artifacts is largely contained within science.
Anomalies are the opposite: they require very little input from outside of science to generate points but create a large threat that exists entirely outside of the science department itself. 

This iteration of Xenobio serves to fill the gap between these two while also introducing some generally well liked thematic ideas--aliens and gene modification--in a way that integrates well with the current design of the science department.

## Genome Collection

Collecting DNA samples from creatures across the station is the primary 'resource' of Xenobio.
This concept takes loose inspiration from /tg/'s cytology.
Scientists are equipped with a set **biopsy punches**, which are single use tools that deal a small amount of damage to the mob they're used on and produce a **biopsy sample**.

Biopsy samples can then be taken to science, where the **DNA Sequencer** can be used to collect the genome from the biopsy, automatically adding them into the **Genetic Database**.

Not all genomes are created equal, however. 
For the purpose of Xenobio, the part of genomes that matter is their instability.
This is essentially a scaling factor that affects the extent of mutations.

Common genomes, like rats, dogs, or other on-station animals, have a low instability and will only have one or two mutations associated with the genome.
More rare creatures, like space animals, have a higher instability which results in more mutations of more serious degrees.
Even still, finding something exceptionally rare, like a blob or a xenomorph, can yield extremely unstable DNA that contains lots of mutations.

This basically means that while you can have a basic set of genes from just looting animals from the station, any more exotic combinations will require collaboration with cargo, botany, or other jobs in order to get access to rarer creatures or the closely-guarded head pets.
Ian makes a fine DNA source.

## DNA Splicing
Once you've collected a reasonable stockpile of genomes in the Genetic Database, you can use the **Mutagen Synthesizer** to combine genomes and create a **mutation injector**.
DNA splicing is a relatively simple procedure that mostly just involves selecting two distinct genomes and combining them. 

This splice can then be further combined with more individual genomes or simply turned into a mutation injector.
Splicing genomes carries a small plasma cost as well as a failure chance.

The chance to fail as well as the cost is dependent on a few factors:
- The amount of times the genome has already been spliced
- The instability of the genome (uses the higher value)
- The difference in stability between two genomes

This overall encourages people to try a variety of simple combinations and not tacking on endless small modifications to create super beasts.
It can still theoretically be done, but it's much more expensive and resource intensive.

## Mutant Creation
Once you have finished splicing a satisfactory genome, you can create a mutation injector at the mutagen synthesizer.
This is how you're going to deliver your payload to your lucky test subject.

By default, you'll be supplied with a crate of monkeys and some N2O. Knock a monkey out, inject it with the cocktail, and then stick it inside one of the various **Growing Vats** scattered inside of the xenobio lab.
Once inside, you simply need to wait for the mutant to grow, watching from afar.
When finished growing, use a plunger to pull it out.

If you pull it out prematurely, you may simply get an unmutated monkey or just a pile of slop. If you leave it in too long, the mutant may wake up and become angry, destroying the vat as it escapes.

Growing Vats must be stocked with a decent level of nutriment and saline in order to facilitate the mutation process. 
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

Research is awarded based on the instability of the creature as well as the number of splices in the genome.
However, the research is only rewarded for a unique genome.
Attempting to perform autopsies on a creature with the same genome multiple times will not result in additional points.