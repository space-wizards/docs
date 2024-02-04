# Vox Species

| Designers | Implemented | GitHub Links |
|---|---|---|
| Errant |  :x: No | None yet |

## Overview

Vox are a species of superficially bird/raptor-like creatures who are highly allergic to oxygen.
I propose that their ongoing design direction be based on three core points: they are weird, they offer a more difficult gameplay experience, and their hardship is intended to encourage cooperation.

(More specific details at the end)


## Background

They are from Space Station 13 and there has always been some interest to bring them over. This is evidenced by the fact that our codebase had vox assets ported more than two years ago. They also come up on Discord every now and then ~~when I start talking about them~~. While there are some unresolved technical issues with implementing them right now, I think the lack of a clear design target is similarly in the way of getting closer to implementing them.

"*I know for a fact that one of the things keeping a lot of the vox players on 13 is that we dont have any*"

"*I would absolutely play vox in SS14 lol*"

"*i think i have been voxpilled*"

[A vox discussion that I did not start I swear ](https://discord.com/channels/310555209753690112/310555209753690112/1200361375856332830)

[A vox discussion](https://discord.com/channels/310555209753690112/310555209753690112/1200411180779438081)

[Discord thread where we are attempting to contain the vox talk](https://discord.com/channels/310555209753690112/1200498334587179018)


## Design Pillars

Disclaimer, all my info is secondhand. If you have any input, feel free to nitpick about the details.

My best attempt to boil down (or am I re-interpreting?) what the vox are about, are these three pillars: Weird, Difficult, and Cooperative.
Everything designed about/for them should aim to channel or at the very least not contradict these three ideas.


#### Weird
They are a weird species, which is perhaps a strange thing to specify in a scifi setting with moth people and space carps, but even so. They are probably cybernetic and their biology is particularly alien I mean who dies from oxygen?! They scream, dammit why do they scream?? Why are they drinking the welder fluid??? While care should be taken that their features are not (encouraging to be) annoying, it's fine if they are a little Weird.

#### Difficult
They are not intended to be perfectly balanced, or even necessarily what you might call "on par". Their main "feature" is in itself very punishing. If they overall fall towards the weaker side of the meta, that's just the cost of being vox. While they can and should have some positives, they should not be given big buffs just to "balance out" their shortcomings. They should not be prohibitively difficult, but if they are a less popular choice, that fits just fine into Difficult.

#### Cooperative
Historically, due to the difficulty of surviving a round as a vox, they had a tendency to rely on each other to get by in a world that was just not built for them. When no one else "got it", vox players turned for support to those who did. (Or so I'm told). It is the position of this design that this cooperative aspect of them is something to be preserved, and it being species specific is not something that should either be encouraged or discouraged mechanically, leaving it to the players to decide.
Obviously, "just designating" how a species is supposed to play like is an impossible, lofty goal, but nevertheless their features could be designed in a way to help with that
This was the hardest pillar to phrase and will be the hardest to come up with ideas for. But if a feature works better with other players, does something for other players rather than you, or is a flaw that is more easily counteracted with external help rather than just having the right tool in your pocket, then that feature is Cooperative.


## Specific Features and Ideas 
(All subject to further review during the actual implementation, of course. Especially towards the end of the list. They are mostly just intended as a showcase of ideas to start out with)

  - There should be some sort of warning or confirmation when selecting them, so players, especially new players, don't end up unwittingly picking a choice that will kill their character for the wrong click. 

  - They breathe nitrogen, but oxygen hurts them badly (tentative number is, they crit in 2 minutes in normal air. Afaik this is actually more lenient than in Spess13)  - they will start with a large nitrogen tank and breathing mask equipped
    - because taking their mask off is BAD, eating and drinking is challenging. They need a nitrogen room, and someone needs to have made that room
    - possible alternative to a nitrogen room is the as-yet uncoded feature to hold their breath, taking asphyxiation damage instead of poison (at an even faster rate). They can regenerate that automatically (assuming they don't miscalculate and go crit)
    - their emergency food and water could be replaced with injectable reagents
  
 - They can't be cloned
 - They take longer to rot (2x? 3x?)
 - They have 50% poison resistance (oxygen bypasses this. poison is generally not a very common damage type/not a very useful resistance to have, so I feel 50 is fine)
 
 - They have their own blood type, and when that system is expanded, it should be incompatible with "normal blood"
 - Possibly their brain, (it actually being a piece of tech), is automatically ready to be placed into a borg chassis

  - They are small/unassuming/fragile.
    - Possibly a dwarf-sized sprite? (when you sprite it)
    - They take ~ +25% damage from all Bruise
    - They get drunk more easily
    - Maybe they are worse at pulling things?
    - They are easier to shove
    - I thought they would deal sub-par damage but there have been some fairly strong feelings on Discord that their claws should be vicious claws. Maybe an exception can be made here, if they take more brute damage they won't really have an advantage in a brawl anyway. Unarmed damage probably isn't really all that important in a real fight anyway)
  
- They should have some actual mechanic involving screams (any such ability should consider that the hotbar cooldown does not apply to emoted screams. They might need to be an actual ability that also does a scream, rather than apply on any scream)
  - they could have the ability to discern the positions of screams within a range, even through walls
  - they could discern some information from screams, such as the coarse Health state of the person? (Good, Okay, Poor, Bad, Danger)
  - their screams could apply a ! popup on nearby people with no additional effect?

- They have a weird dietary range.
  - It has been suggested that they be able to butcher without any tools. Very messily.
  - Their thirst can only be satiated with welding fuel?
  - Water makes them drunk
  - Maybe "normal food" is less satiating to them than the weird stuff (if that can be categorized in some way)
  
- This was just an idea I toyed around with but they could have a mechanic based on hugs. However we want to explain it, from a deep psychological need based on their pack hunter ancestry, to them actually sapping small amounts of bioelectrical energy from others with surface contact (and reducing the other person's life expectancy by 1 to 3 seconds. Don't worry you'll be fiiiine it hardly matters.). The point is that they can't hug themselves and this will make them either hug every single crewmember they see (in hopes of reciprocation) and become known as having no concept of personal space, or threaten you with a fireaxe for hugs. Both of these outcomes are weird which is good.
  - They get a sad vox face debuff on the alert HUD after going X minutes without getting a hug. What a terrible fate 
  - Their bruise regeneration (that all organics have at low damage levels) could stop?
  - Maybe their hunger meter depletes faster when debuffed

# When Vox?
I have every intention to work on the actual implementation of the species and will create a roadmap for getting to roundstart vox once the design direction is settled
