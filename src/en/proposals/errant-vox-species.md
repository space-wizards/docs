# Vox Species

| Designers | Implemented | GitHub Links |
|---|---|---|
| Errant |  :x: No | None yet |

## Overview

Who Vox?

Add Vox as a roundstart species. They are an uncommon species of superficially bird/raptor-like creatures who dwell in the far reaches of space and typically do their own thing, but some of them end up working for NT.  The most well known thing about them is that they die if they breathe what we call air. That this is about the only thing known about them is the reason this document exists.


## Background

Why Vox?

#### "I know for a fact that one of the things keeping a lot of the vox players on 13 is that we dont have any"

They are from Space Station 13 and there has always been some interest to bring them over. This is evidenced by the fact that our codebase had vox assets ported more than two years ago. They also come up on Discord every now and then ~~when I start talking about them~~. The way I see it, there are two main reasons they are still just assets lying in the depths of the Entity Spawn panel: code limitations (aka wyci) and lack of a design goal.

The only thing I'll say about code limitations here is that great improvements are currently being made, but even so it will eventually be stalled by the other issue: there is no clear idea or common agreement what they should be as a playable species apart from "they should scream and die from oxygen". So this is my idea to improve on that front.


[A vox discussion that I did not start I swear ](https://discord.com/channels/310555209753690112/310555209753690112/1200361375856332830)

[A vox discussion](https://discord.com/channels/310555209753690112/310555209753690112/1200411180779438081)

[Discord thread where we are attempting to contain the vox talk](https://discord.com/channels/310555209753690112/1200498334587179018)


## Why Roundstart Vox?
There are three options they could be playable: Admin Spawn Only, Midround Event, and Round Start

##### Admin Spawn Only
Let's say that they are already playable (technically they even are). At that point, getting them greenlit to be a midround event or roundstart would just be a matter of agreeing what features and themes they should have. So let's do that now and ignore this option even exists.

##### Midround Event
I could be wrong but afaik it's more common for them to be a midround presence in 13. As far as I know they usually spawn as "traders wink wink" who are a type of minor antagonist? 

While "space scoundrels" is a well-established sci-fi trope, that does not automatically make it a good idea, and even then, directly tying that idea to a specific species is the sort of detail we should leave to rot in the past. 

Even if space scoundrels are an idea we want in the game, it would be both less chafing against the intentions of our server rules and more interesting to play/face if they were a mix of the available species. That way when a player spots a vox on the station they won't automatically think "Oh great, it's here to steal". They will have to somehow realise that this vox is not a member of the crew.

##### Round Start
Yes.

## What Vox?
Before we proceed, a quick disclaimer (that I randomly put in the middle instead of at the beginning. Thank you for reading this far!). Naturally, everything here is just my interpretation and obviously subject to change especially before, but even after this design is finalized. I don't have much of a history with Spess13 and have never played or seen vox. All I know is secondhand information. So in that respect, I should perhaps not be the one trying to establish what they should be like? And yet, I haven't seen anyone else really try to do so, or at least not where it would be accessible. So if you think I'm off the mark, or you can do a better job, great! That's exactly the kind of input needed here. There is a persistent place for it now.

## What Vox? (But actually)
So. My best attempt to boil down (or am I re-interpreting?) what the vox are about, is these three pillars: Weird, Difficult, and Flock.

Everything designed about/for them should aim to channel or at the very least not contradict these three ideas.


#### Weird Birds
They are a weird species, which is perhaps a strange thing to specify in a scifi setting with moth people and space carps, but even so. They are probably cybernetic and their biology is particularly alien I mean who dies from oxygen?! They scream, dammit why do they scream?? Why are they drinking the welder fluid??? While care should be taken that they are not specifically encouraged to just be annoying, it's fine if they are a little Weird.

#### A Difficult Life
They are not intended to be perfectly balanced, or even necessarily what you might call "on par". Their main "feature" is in itself very punishing. If they overall fall towards the weaker side of the meta, that's just the cost of being vox. While they can and should have some positives, they should not be given big buffs just to "balance out" their shortcomings. They should not be prohibitively difficult, but if they are a less popular choice, that fits just fine into Difficult.

#### Flock Together
Historically, due to the difficulty of getting through a round as a vox, they had a tendency to rely on each other to get by in a world that was just not built for them. When no one else "got it", you turned to those who did. Or so I'm told.

I feel it necessary to say that how they were is not necessarily something to directly emulate. I'm not sure it would be a good long-term plan to encourage them to be insular (if it were even actually possible to just "design" how people will play in this roleplaying game). Nevertheless I think it's an interesting idea that they should be designed with some features that specifically encourage relying on each other, if that's somehow possible? Whether that each other is other players in general or just other vox will be something to be decided by the individual players. If we find that our implementation of vox aren't flocking maybe we didn't make it hard enough >_>

This was the hardest pillar to phrase and will be the hardest to come up with ideas for, assuming it stays as a pillar. But if a feature works better with other players, does something for other players rather than you, or is a flaw that is more easily counteracted with external help than just having the right piece of gear, that feature encourages Flock.


## What Vox? (But specifically)
WIP:
This will be the list of features. We can then go and make them a reality
Only somewhat important for this discussion is "what is currently possible". Let's settle on what we want, what's good, and what's allowed. and work out afterwards how to make it happen
They do not need to be exactly finalised or perfectly specific, we can settle on the exact numbers on the Vox PR once we get there, but when we are done here this should be the concrete list of coding goals (at least for kicking it off. I'm sure things will change down the line, but first the line needs to start somewhere)


#### Fairly Well Established:

- They breathe nitrogen, but oxygen hurts them badly (tentative number is, they crit in 2 minutes in normal air. Afaik this is actually more lenient than in Spess13)
  - their time to die from crit is the same as for other species, since you don't breathe while in crit
  - they start with a large nitrogen tank equipped and their mask should turn itself on at spawn
  - because taking their mask off is BAD, eating and drinking is challenging. You need a nitrogen room, and someone needs to have made that room
  - possibly a feature to hold their breath, taking asphyxiation damage instead of poison. You can regenerate that automatically (assuming you don't make a mistake and black out)
  - emergency food and water could be replaced with injectable reagents
  - MAYBE they should be able to get nutrients in general via injection?
- They can't be cloned
- They rot much more slowly
- They have their own blood type, and when that system is expanded, it should be incompatible with "normal blood"
- Possibly their brain, (it actually being a piece of tech), is automatically ready to be put into a borg chassis

#### Possible Ideas:
This is the part where things deteriorate and why this is a draft

- They should have some actual mechanic involving screams
  - their scream indicates their direction to other players in range? Maybe just other vox?
    - ((this is intended to both encourage and discourage screaming on their part. If you constantly scream, no other vox will eventually care?))
      - Or maybe have this on a specific cooldown?
    - caution: this does not encourage mixed-species flocking
  - their screams heal a small (symbolic) amount of damage. Something something positive resonance or whatever
    - only heals other nearby players, but not them?


- They are small/unassuming/fragile.
  - Possibly a dwarf-sized sprite? (when you sprite it)
  - More vulnerable to all brute damage
  - Maybe they are worse at pulling things?
  - They are easier to shove
  - Maybe they deal subpar unarmed damage?

- They are more resistant to poison damage (oxygen will bypass resistance)
  - 50%? It's not unprecedented to have that level of resistance and poison is often not a hugely useful resistance to have
  - If they can eat lots of poisonous stuff, this will dampen the damage
    - should it, though?

- They have a weird dietary range.
  - Can drink welding fuel with no ill effects?
  - They should get drunk from said welding fuel, or maybe from just plain water. It's funny.
  - Can eat some inorganic items?
  - In general they should be able to eat and drink a very wide range, and at worst be poisoned a bit (which they are resistant against)
  - Maybe "normal food" is less satiating to them though

- They get drunk more easily? I think crew trying to keep the water away from vox to prevent drunkness-induced screamsinging is perfection.


# When Vox?
Once this doc is settled we can create a specific roadmap of things that need to be coded or specified, on the way to roundstart vox.
