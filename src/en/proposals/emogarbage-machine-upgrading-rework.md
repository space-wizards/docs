# Machine Upgrading Rework

| Designers | Implemented           | GitHub Links                                                                                                                                   |
|---|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| EmoGarbage | :warning: Partially | [#23202](https://github.com/space-wizards/space-station-14/pull/23202), [#22233](https://github.com/space-wizards/space-station-14/pull/22233) |

## Overview

Upgrades as a whole are somewhat integral to science as a department. 
They basically exist to produce upgraded versions of various items and tools.
However, when it comes to upgrading the machines around the station, there are some issues.

It's not a stretch to say that machine upgrading is in a state of constant irrelevancy.
Even after a slew of additions and support added for close to 20 different machines, the system failed to become the science subdepartment I had hoped, rather becoming a strange task that would occasionally be done by a select few players.

The system suffers from a few core issues, which I will highlight briefly.
#### RND Integration
Machine parts predate the new discipline system that RND now functions on. 
While in the past, getting higher tier parts was really trivial, now, with the heavy randomization implicit in the system, it's pretty common to go a long time before receiving even one part upgrade.

It also means that all machine part upgrades, which can affect machines between every department in the game, are relegated to a single discipline.
This not only makes that single discipline (experimental) significantly better than most others, but it also means that other disciplines that could have new upgrades get snubbed by the machine part upgrades.

#### Discoverability
By the nature of machine parts, it's really difficult to tell when and where they'll have an effect. 
Of course, if you have already built the machine, you can physically examine it to determine if it has upgrade potential, but this knowledge isn't readily available at all when you unlock the parts.
Additionally, the line between a machine and not a machine is very much a technical one that players are unlikely to intuit.

Previously, the methodology for making upgrades discoverable was a tactic of complete coverage: every machine _must_ have an upgrade. 
Otherwise, using higher tier parts to upgrade a machine could result in no difference at all, which would be frustrating for players.
This is obviously not ideal however, since some machines really just don't need upgrades.

A perfect system would make players instantly aware of what machine they can improve the moment they are able to, rather than requiring a ton of trial and error discovery.

#### Balancing
Machine parts exist as simply numerical values. 
Each tier is basically just a number that goes up with little else to distinguish it.
This means that, to implement an upgrade, the simplest and most logical way of doing it is simply increasing some value on a component.

This is not to say that it is impossible to do anything deeper, but the system as a whole has absolutely no support for that, and adding support for it is really not feasible due to the nature of being to swap parts so trivially.
This makes having additional 'side-grade' features (which can be integral to balance) very difficult to implement. 

Furthermore, having 4 distinct levels of upgrades makes balancing this very difficult, with a lot of things getting absurdly strong in the later tiers.
This is very prominent with a lot of machines that have 'useless' upgrades (the blender blending things instantly comes to mind) but it's also tough to balance a numerical value that is simultaneously worthwhile when in the 2-3 range, but not overpowered in the 3-4.

## Discrete Upgrades
My proposed solution to this issue is **discrete upgrades**. 
This isn't really a formalized system but rather a guideline for how to better make "upgrades" without machine parts and the like.

Discrete upgrades are, quite plainly, machines that look and have similar names to existing ones while performing their task better.
A discrete upgrade to a microwave might simply be a 'macrowave' that has a glossy black finish and an absurd radiation sound while cooking food twice as fast.

These machines would simply be unlocked like any other science machine: via unlocking the corresponding technology in the appropriate discipline.
This helps with discoverability, integration, and balancing, since now these upgrades can be in disciplines relevant to them while also being able to have custom unlock prices and tier restrictions.
Furthermore, before you even unlock the tech, you are made aware of what upgrades you are getting via the descriptions of what is unlocked.

Additionally, these new entities, since they are completely different than their base counterparts, can easily have new components added to them in YAML to allow for new functionality such as emitting radiation, heat, or any other behavior.
This is a powerful tool for adding downsides to balance potentially strong upsides.

Unlocking **Geiger's Food Prep Science** and being able to build the **macrowave**, which instantly cooks your ramen while dousing you in lethal radiation, is a far more engaging and discoverable system than simply getting **Super Parts** and waddling over to the kitchen to allow the same old microwave to cook your food instantly.
Just simply having different audio/visual stimuli makes the upgrades more unique and recognizable to players.

## Machine Parts
Tier 1 machine parts, that being the capacitor, matter bin, and manipulator, will most likely remain in the game. 
It might even be worthwhile to bring back the laser and scanning module if we so please.

These parts won't have any unique functionality. 
They'll simply remain as a small item used in various constructions for variety, which is always nice.

The RPED, being a somewhat core concept of machine-part-based upgrading, will likely just be removed.
It doesn't really fit in with the way discrete machines work and the functionality of placing in machine parts into a frame is really not enough to justify it existing. 

Likewise, the technologies for higher tier parts as well as the parts themselves will also be removed.
There's not really a purpose to them and, as we saw before upgrades had implementation, they were frequently a source of confusion as to what their higher tier actually did.

## Flatpacks and the Flatpacker
A common concern that has been voiced about the removal of machine parts is that it makes these upgrades harder to access for the average player.
This is a pretty fair criticism: building new machines is a fairly intensive process, requiring a variety of tools, parts, and materials.
It's a fair to expect that the average service worker or cargo tech may not have the means to build upgrades in scale.

The solution to this is a concept already used in the game: **flatpacks**.

You may be familiar with these from station beacons or the AME shielding: these are small boxes that can be unpacked via a multitool, turning into a full-sized machine.
These are an ideal way to allow non-technical roles to build machines easier, since they require very little skill to use.

The way that flatpacks will be constructed is through a new science machine, called the **flatpacker**. 
The flatpacker simply takes in a machine board and an amount of materials equal to the construction cost (with a small addition in exchange for the convenience) and creates a flatpack for that machine, leaving the board.

This makes the flatpacker the ideal way to make compact machines that can be set up trivially as well as making a large amount of machines in bulk that can be transferred easily.
This is good for scenarios like bringing over a bunch of hydroponics trays to botany, or making a bunch of recharging stations and setting them up around the station quickly.