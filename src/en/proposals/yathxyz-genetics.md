# Genetics

| Designers | Implemented | GitHub Links |
|---|---|---|
| yathxyz | :x: No | TBD |

```admonish warning "Attention: WIP!"
This section is actively under development! Everything and I mean *everything in this document* is subject to change. You are more than welcome to help with this proposal.
```


```admonish warning "Disambiguation"
Not to be confused with the [proposal regarding plant genetics](./deltanedas-plant-genetics.md).
```

## Overview

This proposal covers the implementation of genetics, including the job role and its interactions with other departments. It outlines the principles of genetics to be implemented as well.

## Design Pillars

### Accessible yet limitless

Genetics should have small workflows that will let even a new player with a guidebook to help with the station. At the same time, a skilled geneticist should have a differential impact to the station's robustness or destruction.

### Multidisciplinary

Genetics as a job should be synergistic with medical, science, security and **botany**. Genetics (although typically a medbay role) interfaces with each of the first three departments in terms of diagnostics and cloning, genomics, and forensics respectively. As for botany; botanists can essentially be geneticists strictly for plant groups. This should already make the implementation applicable for pre-existing maps.

*A robust geneticist should not be a hermit, but instead interact with many departments that reasonably depend on it and vice versa. This respects the Player Interaction/Agency Core Design Pillar*

### Non-deterministic

The natural history of living things should be different in each round. A new genetic schema has to be generated that makes the use of investigative workflows necessary.

## Implementation

### Principle

Genetics should appreciate and fully exploit the benefits of ECS and specifically prototypes. The current genetics implementation that is restricted to plants involves a string of binary values with positions of that string allocated for hard-coded traits, with mutation flipping values at different positions of the string.

Genetics should be implemented in reverse. Any arbitrary trait can be made heritable with the attachment of a heritable component. This component specifies the genetic schema that includes rules that it needs to satisfy so that the emergent model of the genome during the investigation makes sense. *This does not mean that an active trait need be heritable. We can also declare junk DNA itself to be heritable that can be used in identification.*

It goes without saying that all generated information about traits is to remain server-side.

This helps in three ways:

1. Genetic traits can be extended through the use of prototypes without changing the underlying logic. This allows the declaration of heritable traits can be *Chaotic* and *Seriously Silly*.
2. Observable phenomena akin to real genetics such as Mendelian inheritance (with actual modes of inheritance that can be observed).
3. Penentrance can be variable without complicating the codebase. We can mutate any organism that has heritable traits and let the traits show in the next generation.

*There will be multiple solutions to how the YAML code should look like. The principle allows us to be flexible regardless.*

### Schema

*This will require further elaboration.*

Properties generated for a heritable trait that decide things like mode of inheritance must follow a declared schema. For example, in terms of chromosomes, fruit flies only have 3 autosomal pairs and 1 sex-linked. A trait that has a locus (chromosomal/genetic linkage map location) "subcomponent" would be based on that schema.

### Model organisms and homology

*The actual genetics-ness in genetics.*. All organisms share a common ancestor, thus making homology a core mechanic in creating genetic modifications through forward genetics.

Model organisms are organisms used in a controlled setting to answer biological questions. Taxa that are closer to our species would have a higher degree of similarity, thus there is a higher chance that a given trait has homology to ours.

This elegantly transfers to a effort/risk-reward mechanic. Fruitflies for example are part of a taxa that is a lot more distant from our in comparison to a species like mice. Isolating mutations (explained in the forward genetics workflow) would be easier since fruitflies have a short reproductive cycle, however homology would be restricted to genes of a more universal function. On the other hand, something like a monkey has a high degree of genetic similarity and would have more complex traits that can be implanted to humans. However, mammals have a long reproductive cycle and sample sizes would remain small, thus might be restricted to just backwards genetics (sequencing).

See [this article](https://en.wikipedia.org/wiki/Homology_(biology)) for a satisfactory explanation.

## Gameplay

### Workflows

As discussed above, in genetics there are multiple workflows. Each of them can interface with a different department.

#### Forensics

- Key item: RLFP test kit.

This is a tool used by the detective for conducting forensic analysis on crime scenes. Based on a real life method [(1)](https://en.wikipedia.org/wiki/Restriction_fragment_length_polymorphism). Each player would have a junk DNA component that is used for identification. The test kit will produce a different pattern of polymorphic bands based on the junk DNA value. In a scene involving the bodily fluids of multiple people, the test kit would produce an image of overlapping bands suggesting the presence of multiple people in a crime scene.

#### Forward genetics

- Key items: BioSonica Breedstation™, NanoTrasen Vectorizer™.

The classical genetics simulator (2) is the primary if not the sole inspiration for this entire workflow. Although a lot of explaining is required to describe the depth of this workflow, it is recommended that everyone interested in the genetics implementation try this simulator in order to gain an intuitive understanding of what is being proposed here.

Succintly describing the workflow, the geneticist;

1. Exposes a generation of fruitflies to unstable mutagen resulting in a progeny with different traits that are potentially desirable.
2. Cross-breeds mutated fruitflies with other fruit flies of fully documented genotype and phenotype. Finds the locus of the desired mutated gene based on recombination frequencies alone.
3. Upon knowing the locus of the desired trait, the geneticist will use the vectorizer to isolate the relevant chromatin. The vectorizer will essentially "attach" the trait to a virus (a vector). A substance will be outputted that can be injected to the person allowing for genetic modification.

*The vectorizer will be useful to the botanist as well. This forward genetics process can be done through successive rounds of cross-pollination. See the issues section.*

#### Backwards genetics

- Key items: Luxdyne Sequencer™, NanoTrasen Vectorizer™.

Considered a more direct approach, the sequence will take in a sample from an organism and directly output information about the heritable traits. For balancing, sequencing should be a long passive process that can be left in the background while the geneticist is focused on other tasks. This will naturally limit its use to model organisms that have more homologous traits such as monkeys and mice.

With the information provided by the sequencer, the geneticist can use the vectorizer to isolate the desired trait.

## Issues *actively looked into*

Although we could make lizards fit into the natural history of Earth, more thought will have to be put on how slimepeople can be treated.

With plant genetics, other things will have to be considered such as polyploidy, vegetables, *and the fact that realistically that botanists can only allocate a few trays for such a workflow.*

## Inspirations, related

- (1) https://en.wikipedia.org/wiki/Restriction_fragment_length_polymorphism
- (2) https://cgslab.com/

