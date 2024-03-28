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
Artifacts in their current iteration have a few shortcomings that drastically reduce the potential complexity of the system.
While the core concept is interesting and they have decent integration with things like salvage and collecting tools for activations, there are also many situations where players feel as if they lose the ability to meaningfully interact with them.

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
The primary changes to generation are fairly simple. 
While all the nodes still generate in an interconnected structure, they will have more connections to lower depths, resembling a tech web more than a basic tree.

All nodes can have one of 3 basic states:
- Active
- Latent
- Locked

**Locked** nodes are the basic state of all nodes on an artifact.
All nodes start as locked and they have no effects.
The primary goal is to unlock these nodes.

Once all of the necessary triggers are activated (will be elaborated on later), a locked node can become a **latent** node.
Latent nodes do not inherently have any effects when the artifact is activated but they do increase the research value of an artifact.

Any latent node at the end of it's path is an **active** node. The effects of active nodes are what is seen when an artifact is activated.

```admonish info "Paths"
A "path" can be conceived of as a string of connected nodes that is increasing in depths.
A path would be formed from a depth 1 node that leads to depth 2 to depth 3 and so on.

The end of a path is the node with the highest depth.
This means that node either has no connections to higher depth nodes or the higher depth nodes are still locked.

The end of a path is variable and can change when higher depth nodes are activated.
```

### Activation and Triggering Nodes
A distinct departure from the previous version of artifacts, the activation of an artifact is now something that is distinct from simply triggering a node.

Activating an artifact is simply achieved by using it in hand, clicking on something, or other context interactions based on the active nodes.
This simply does all the effects of the active nodes all at once.
By stacking the effects and allowing them to happen on queue, artifacts are given much more utility than they have prior but the simultaneous activation of multiple nodes makes them even more chaotic and interesting.

As a balancing factor, artifacts now have a durability, with over-use of direct activation potentially "breaking" nodes and preventing them from being used.
They can be repaired using specialized equipment (which will be elaborated on further later).

In exchange for this much easier activation, triggering nodes is now significantly more complex.
To trigger a locked node and make it become latent, you must not only provide the stimulus for that node, but for every node underneath it in the structure.

```admonish info "Node Children"
The nodes 'underneath' a given node can be thought of conceptually as every node attached to the current node with a lower depth.
This is the extended recursively to every additional node.

For example, if Node A has 2 lower nodes connected--called Node B and C--and node B has 1 lower node connected called Node D, then to activate Node A, you need to have the combined stimuli of Nodes A, B, C, and D.
```

Once the first stimuli is provided, an "activation period" (roughly 10 seconds) will begin wherein all the stimuli activations will be recorded. 
At the end of the period, if the stimuli recorded _exactly match_ the locked node, it will become a latent node.

Note that if you need stimuli A, B, and C but you instead provide A, B, C, and X, the node will not become latent.
It must be the exact match and not simply a superset.

When a node is unlocked via this method, its effect will occur once.
Future activations of the effect will only happen through the regular activation method highlighted above.

## Artifact Equipment
With these new mechanics, existing artifact equipment will be reimagined and new equipment will be added to fill in the existing niches.

The artifact analyzer and analysis console gets the most immediate and useful changes.
It will now visually show all nodes in the correct structure, using lines to connect nodes.
All latent and activated nodes will have basic information such as stimuli, effects, depth, and the latent/activated state.
Clicking on a node in the UI will bring up a small window with additional information.

Locked nodes that are connected to latent or activated nodes will be given a limited information display, showing only the stimuli and the effect.

The handheld node scanner will be used to harvest more precise information on any active nodes.
This will give info such as the research value and the current durability.
Using the scanner to check up on the status of an artifact is an important factor in using their active abilities to make sure you don't accidentally break it.

Artifexium, which previously activated artifacts, will now serve as a "dummy" stimuli when applied during an activation period.
For example, if stimuli A, B, and C are needed, but only A and B are provided, spraying artifexium will substitute the non-existent C stimuli and cause the activation.

The traversal distorter will be plainly removed since it is fucking esoteric garbage that no one knows how to use and has no place in the new system.

### Artifact Fragments
Fragments are gonna work almost completely differently in this iteration. 
They are kinda neat in their current existence, but they are pretty boring and could serve to be a lot more interesting.

Artifact fragments will no longer simply just be a random collection that's spit out after an artifact is crushed.
Instead, each distinct path of the artifact's structure will be turned into a fragment.

These fragments, instead of being crafted into a new artifact, will be combined with existing artifacts at an **Splicer**, which will combine the nodes of the fragment into the existing artifact.
This provides interesting gameplay where you can combine artifacts in order to make more useful equipment which allows for something interesting min-maxing.

The fragments will also scale their artifexium values in relation to the amount research they provide. 

### New Equipment
New equipment (besides the splicer) will focus mostly on manipulating the active nodes of an artifact and interacting with the new mechanics.

**Artifact Glue** is a reagent made from artifexium and when applied to an artifact will repair the durability of nodes on it. 
This provides additional uses for artifexium and ways to extend an artifact's lifespan in the case of beneficial effects that players are using often.

The **Resequencer** simply takes the existing nodes and shuffles them, creating new connections.
This can completely flip the effects of an artifact and enable new wacky combinations.
It can also help reach particularly hard to get nodes and allow science to 100% complete and artifact.

The **Arti-nUKer** is a special device that obliterates all active nodes on an artifact. 
The severed connections are automatically merged, fixing any holes created in the structure.
This is basically a free re-roll of effects paired with easier to activate high-depth nodes.

The Resequencer and Arti-nUKer can both serve as mid-tier research to provide optional depth for the truly engaged archeologists.

## Artifact Reports
The original version of research generation from artifacts simply came from destroying the artifact in exchange for points.
This has been gutted significantly and now it is basically just a risk-free button you press.
This proposal aims to reintroduce that interest.

Research is generated at the new **reliquary console** through **artifact reports**.
The data for the reliquary console can be sent via the analysis console, which sends a copy of the current state of the artifact.
Players can then choose which copy of the artifact to use for a report, allowing for backups to be made if someone horrifically obliterates an artifact.

The research value for an artifact is calculated similarly to how it is now:
- Latent nodes give value based on the effect/trigger/depth of a node.
- Nodes that have been scanned via the handheld node scanner give additional research.
- An artifact with no locked nodes has an additional bonus.

However, there are factors which can damage the research value of an artifact:
- Missing nodes, such as those from the effect of the Arti-nUKer
- Nodes with destroyed durability, such as from the effects of the repeated activation. Glued artifacts do not suffer from this loss in value.
- Extra/non-original nodes, such as from the effects of the Splicer or any future machines.

When a report is submitted, players will receive research based on all these factors.
A single artifact can have multiple reports submitted, however, more research points are only given for the increase in value between the two reports (100 value report -> 250 value report yields only 150 points).

The combination of these mechanics provides a risk-reward for modifying artifacts, introducing strategy around whether or not the modifications are worth the loss in value.
Perhaps you can make a epic exploding teleport gun artifact, but it isn't worth much to the scientific community.
