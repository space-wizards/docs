# XenoArch Redux [3MOArch]

| Designers       | Implemented | GitHub Links |
|-----------------|---|---|
| Thee EmoGarbage | :x: No | TBD |

## Overview

This proposal aims to re-imagine the science subdepartment of XenoArch and Artifacts in general in an effort to give them more depth, and utility.
This will be accomplished by changing node traversal to add more player agency, improving in-game tools for categorizing and understanding artifact structure, and adding additional equipment that makes manipulation more interesting.

The ultimate goal is to redesign the system so players can better understand how artifacts work and to allow greater utility and mechanics to arise out of artifacts.
XenoArch should feel like unlocking the sprawling secrets of an artifact while additionally gaining points as a secondary reward for the research.

_This redesign lends partial inspiration to Goon's artlab as well as Noita's customizable wands._

## Background
As it is now, artifacts consist of interconnected nodes, each one carrying an effect and a trigger. 
The effect is just some crazy behavior that happens in response to the trigger, which is just some kind of generic action taken upon the artifact.

These nodes form a tree, wherein each individual node's depth within this tree determines the craziness of the its effect and trigger.
An artifact has a single node which is active, which is what determines the current effect and trigger which must be done.

Moving to another node requires the completion of the current node's trigger and is semi-random in nature.

While the core concept of XenoArch is interesting and has decent integration with salvage and cooperation for collecting tools for triggers, there are also many situations where players feel as if they lose the ability to meaningfully interact with them.

I'll outline some of the core issues here:

### Randomness
Artifact generation is completely random, but so is the activation of effects.
Players cannot meaningfully control which effects they activate and even the limited tools they have like the traversal distorter are extremely esoteric and don't actually provide meaningful control.

The result of this is that while many effects could potentially be extremely useful and provide players interesting means of interacting with their environments, there's no way to actually harness of control the randomness to produce those interesting outcomes.
At best, you simply re-trigger a beneficial effect several times and reap the rewards in that way.

### Lack of Complexity
Artifacts are primarily dictated by a single effect with the occasional mix-up of having permanent effects (many of which are underwhelming).
Activation stimuli are similar: the only sliding scale to adjust with how difficult something is to activate is just how hard it is to do that singular trigger.

Since these triggers are always placed in isolation, unless the effect is having some pronounced impact on the crew's ability to trigger the artifact, triggers mostly devolve into incredibly simple and routine tasks.

A water trigger should have lots of depth, but it instead is mostly just walking in with a cup of water and splashing it, which is really the most boring way to engage with something like that.

### Lack of Progression
Artifacts have an innate progression in the form of the scaling of nodes, which is mostly built around increasingly difficult triggers and more dangerous and wacky effects.
This is a good start for a system like this, but the unfortunate reality of it is that the scaling isn't pronounced enough to often feel like a deviation from the early-depth nodes.

Especially when taken in with randomization of artifacts, you can oftentimes just get subpar generation that flounders in weak effects that don't feel like a progression in research.

## Artifacts
I'll use the element of a [tech tree](https://en.wikipedia.org/wiki/Technology_tree) as a reference to explain the new generation.

Each node is essentially an upgrade in a tech tree.
The structure can be described as a typical tech tree structure (a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph)) but without the presence of the first element in the graph.

Just like the current system, all of these nodes have a trigger and an effect associated with them.
However, you do not 'move' to a node like the current system, but you instead permanently unlock it like a tech tree.

And just like a tech tree, unlocking a node has a cost associated with it.
The 'cost' is the activation of all of the triggers of the nodes in that path--that is, all of the nodes that needed to be unlocked in order for the current node to become available.

In this situation, the 'active' nodes are the nodes in each path that have the highest tier.
These are the nodes that will produce effects when they are activated.
The remaining nodes are classified as 'latent'--unlocked but not creating any effects when the artifact is activated.

All remaining nodes are simply locked and have no behavior.

### Activation and Unlocking Nodes
The activation of an artifact is now something that is distinct from simply triggering a node in the old system.

Activating an artifact is simply achieved by using it in hand, clicking on something, or other context interactions.
Doing this simply causes all the effects of the active nodes simultaneously.

By making many effects happen at once, they can combine in novel ways and increase the utility and chaos of the artifact, greatly improving on the current system where lackluster nodes can seem to have 0 effect at all.

As a balancing factor, each node of the artifact now has a durability.
Activating an artifact degrades the durability of all of the active nodes.
When the node is fully degraded, it no longer produces any effect when activated.

The durability can be repaired using special equipment (which will be elaborated on further later).

In exchange easier activation, unlocking nodes is now more complex.
To unlock a node, you must provide the stimulus for that node as well as the the stimuli for every node below it in its path (the path being all of the nodes that had to be unlocked in order to reach the current node).

Once the first stimulus is provided, an activation period (roughly 10 seconds) begins wherein all the stimuli activations will be recorded. 
At the end of that period, if the stimuli recorded _exactly match_ a node's required stimuli, it will be unlocked.

```admonish info
Note that if you need stimuli A, B, and C but you instead provide A, B, C, and X, the node will not be unlocked.
It must be an exact match and not simply a superset.
```

Once unlocked, the node's effect will occur while a small animation and sound effect playing, giving feedback to the players that something has occured.

## Equipment

### Analysis Console
The artifact analyzer and analysis console will be improved to no longer have any kind of delay and to show significantly more information

The console UI will now visually draw all the nodes in the structure, using lines to connect them.
All unlocked nodes will have basic information such as stimuli, effects, depth, research value, durability, and whether or not the node is active.
This info can be accessed by clicking on the node in the UI, which will show a small window.

Locked nodes that are connected to unlocked nodes will be given a limited information display, showing only the stimuli and the effect.
This allows players to have a limited strategy for the nodes they want to unlock. 

### Handheld Scanner
The handheld node scanner will be used to check information on the current active nodes of the artifact.

Clicking on an artifact with the handheld scanner will take a "snapshot" of it which can be viewed in a UI.
This gives similar info as the analysis console but is limited to the active nodes of the artifact.

The scanner now gains a lot of utility as being able to quickly assess the state of an artifact without needing to bring it to science.
Being able to check the durability also helps when actively using the effects on the go.

The scanner also has the ability to view the node structure of artifact fragments, which can be useful for sifting through them when trying to splice artifacts.

### Artifexium
Artifexium, which previously activated artifacts, will now serve as a "dummy" stimuli when applied during an activation period.

For example, if stimuli A, B, and C are needed, but only A and B are provided, spraying artifexium will substitute the non-existent C stimulus and unlock the node.

If there are multiple nodes which could be unlocked by a the artifexium (say, a node needing stimuli ABC and one needing stimuli ABD), one will simply be unlocked at random.

### Artifact Fragments
Artifact fragments will no longer simply just be a random chunk that's spit out after an artifact is crushed.
Instead, each distinct path of the artifact's structure will be turned into a fragment which stores the nodes and connections from that path.

These fragments, instead of being crafted into a new artifact, will be combined with existing artifacts at a **Splicer**.
This provides interesting gameplay where you can combine artifacts to create more tactically useful artifacts with beneficial or dangerous effects.

The fragments will also scale their artifexium values in relation to the amount research they provide. 

### New Equipment
New equipment (besides the splicer) will focus mostly on manipulating the active nodes of an artifact and interacting with the new mechanics.

**Artifact Glue** is a reagent made from artifexium and when applied to an artifact will repair the durability of nodes on it. 
This provides additional uses for artifexium and ways to extend an artifact's lifespan in the case of beneficial effects that players are using often.

The **Resequencer** simply takes the existing nodes and shuffles them, creating new connections.
This can completely flip the effects of an artifact and enable new wacky combinations.
It can also help reach particularly hard to get nodes and allow science to fully unlock the artifact.

The **Arti-nUKer** is a special device that obliterates all active nodes on an artifact. 
The severed connections are automatically merged, fixing any holes created in the structure.
This is basically a free re-roll of effects paired with easier to activate high-depth nodes.

The Resequencer and Arti-nUKer both serve as mid-tier research to provide optional depth for the truly engaged archeologists, without the boring technical complexity of the traversal distorter.

## Research Generation
The analysis console UI will show the current research value of the artifact as well as the value it needs to exceed to generate more research.

This will also show the calculation for how the research value is achieved, providing more info and transparency to players.

The research value for an artifact is calculated similarly to how it is now:
- Unlocked nodes give research based on their effect, stimulus, and depth.
- Artifacts with no locked nodes grant an additional bonus.

However, there are factors which can damage the research value of an artifact:
- Nodes with completely degraded durability (gluing the artifact to repair it does not incur this penalty)
- Missing nodes, such as those from the effect of the Arti-nUKer.
- Additional nodes, such as from the effects of the Splicer. 

Note that the calculation for the last two points is based on the total number of nodes in the original vs. the current artifact.
If you destroy 2 nodes and then repair it by splicing 2 nodes onto it, you incur 0 penalty.

To actually gain research from the artifact, you must place it on an analyzer and begin the 'research' task in the analysis console UI.
This begins a 30 second countdown where the artifact must remain on the analyzer, cannot be activated, cannot have any stimuli trigger, and the analyzer must remain powered.

This provides an interesting window wherein sabotage and other such measures can be taken to steal the artifact or otherwise interrupt science.

At the end of this countdown, the research is added into the server and a glorious sound effect plays.