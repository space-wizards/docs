# Engine Containment Safeties

| Designers | Implemented | GitHub Links |
|---|---|---|
| Flareguy, CptJeanLuc |:x: No | TBD |

## Overview

This proposal aims to make sabotaging the primary engines (the singularity and tesla) much, *much* harder - possibly to the point of even being able to be theoretically considered an IC issue, provided you set aside the fact that it is one of the most antagonistic things you could possibly do.

## Background

[This is mainly based on a brainstorming session held in discord,](https://discord.com/channels/310555209753690112/1008709214006427689/1201664586512871435) with some additional things added as I went along.

Despite the round-ending damage these engines can cause, the amount of effort needed in comparison to make them break containment is minimal. By cutting a single wire or turning the PA's particle strength above 1, you can instantly force a shuttle call.

This not only makes it a pretty unbalanced & simplistic interaction for antagonists, but also makes it extremely potent for griefing. It's practically just a "kill station" button with no real safegaurds other then needing engineering access.

## The Safegaurds in Question

- **Particle accelerators are now simplified to on/off instead of having strength.**

In SS13, instead of being a "make the singularity break containment" button, higher particle strengths meant that the singularity would sustain itself at a certain stage. There's not really much value in this, though - you're practically just choosing between "do I want more power or do I want less power," as the added danger of a bigger singularity is incredibly negligible.

This includes the emag behaviors's removal. If you want to loose the engine, you're going to have to put in real effort.

- **Wire Power Monitoring Thingamaob**

A device that mounts to a power network, and monitors if it loses power or is otherwise disconnected from the network. If it does, the object will make a chat message over the engineering channel informing them of the disconnected terminal.

This also helps curb mass-wirecutting (another very easy-to-abuse mechanic.) Engineering can install these in other places and try to cooperate with security to catch a criminal, or just respond to the alarm and repair it when it happens.

People looking to mess with wire nets with the monitor installed will need to get creative - either by using explosives to detonate the wire monitor to prevent it from sending a signal, stopping power from being generated entirely as a coverup, or just by stealing the monitor itself and getting the hell out of there before you can be found.

- **Containment Field Alarms**

The containment fields in the engine room now come with a pre-installed upgrade that lets them broadcast if they are losing power. This would function similarly to the the supermatter alarm from /tg/station; once the containment field starts losing power it will broadcast a message over the engineering channel, and once it's under a certain threshold (say, 2 minutes left of power out of a total of 5,) it'll start broadcasting over common. This is to give the crew a fighting chance to stop whoever is messing with the singularity, and cannot be prevented unless you get a radio jammer in range of all of the containment fields.

To reiterate further, this is a feature that not all containment fields will have. Upgrading a regular containment field with a special upgrade chip should be possible.

- **The Generators Themselves**

This wasn't discussed in the inital discord conversation, but is probably nessecarry, since you can trivially just move a generator in front of the PA and have it instantly loose without having to deal with any containment proceedures. The only reason this probably isn't utilized more often is because raising the PA strength is easier.

When being fired at with a particle accelerator, the generators will broadcast a message over engineering communications:

`A (singularity/tesla) generator is being initalized at (coordinates!)`

Initializing the generators should take approximately 40 seconds or so, to give people time to respond.
