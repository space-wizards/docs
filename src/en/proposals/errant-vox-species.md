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

- There will be some system indication/display at Character Creation to inform the player what to expect (presumably, this system will also serve to provide basic info about other playable species)
  - Should use (or be integrated into) the Guidebook

- Vox breathe nitrogen, and oxygen is very toxic to them (crit in 2 minutes)
- They exhale Ammonia
- All vox will start with a full-size nitrogen tank and breathing mask equipped. Internals will start active.
  - At current capacities they will have to swap/refill the tank every 31 minutes, so at least 3 times during an average round
  - If they did not get some sort of outerClothing from their job spawn gear, a stock vest/tank harness will be provided so they have a suitStorage slot for the tank to spawn into
- They will have to build a nitrogen room (or go to one built by someone else) to be able to safely eat/drink.
  -  Alternatively, they will have to hold their breath (new feature, manual activation)
  - Holding their breath actually causes asphyxiation damage faster than the oxygen deals toxin damage (crit in 40 sec) but asphyxiation damage automatically recovers over time once they start breathing again, potentially making it a preferable choice

- They can't be cloned (they can still be normally resuscitated with defibrillators)
- They take 3x as long to rot
- They are immune to some specific toxic substances (See Diet)

- Vox blood should be incompatible with other blood (apparently this is getting implemented independent of them anyway)
- Their brain is a cortical stack
  - They don't remain "conscious" the way a positronic brain/MMI is. They can't speak and aren't supposed to learn/remember things until they are put in a body. Just like any other species' extracted brains
  - Cortical stacks, however, can be slotted directly into a cyborg, and will work/behave like any other cyborg, save for the fact that the cortical stack will again be dead/inert while removed from the cyborg

They are small/fragile beings
- Ideally their sprite should be about kobold size (the entire sprite situation will likely be their last blocker anyway)
  - Scaled down, if allowed?
  - Different sprite?
  - Displacement map to chop a few rows of pixels out of their legs?
- They take +25% Blunt damage, +15% Piercing, and +5% Slash
  - (The logic being that they take bonus brute damage because of their smaller size, and even more bonus because fragile bones, but the bonus to slashing is less because their fuzz/feathers resists that better)
- They have lower Density, making them ~~easier to shove and~~ worse at pulling heavy things
- They get drunk easier, but not off Ethanol. (See Diet)
- They run 10% faster (unless Sad)
  - Not sure if players would be able to even feel this in a blind test

They are small but also vicious when needed
- Their claws deal only 4 damage, but can attack 1.66 times per second.
  - Their rapid attacks create a threatening onslaught, but it's not nearly as dangerous as it appears, being outshined even by a shiv
  - In unarmed vs unarmed, their 20% higher base DPS is generally evened out by them also taking more damage. The most common unarmed damage type is Blunt
  - Other than species flavor or crew disputes/RP, unarmed damage is kind of irrelevant. Virtually any improvised weapon is an upgrade

### Diet
The idea is that they have a robust digestive system but it's not tuned to a modern, sophisticated palate. Historically they haven't been into agriculture and are not known for their cuisine

- Can butcher without any tools, using their claws.
- Can eat raw meat without ill effects
- Can eat spoiled food, immune to Gastrotoxin
- Immune to INGESTED Carpotoxin (might not currently be possible. In that case, immune to all carpotoxin until distinction possible)
- Reduced damage from ingested Toxin (might not currently be possible. In that case, no resistance until distinction possible)
- Welding fuel is harmless and quenches thirst efficiently (Basically their Water)
- Ethanol is harmless and mildly quenches thirst
- Water does not satiate them, intoxicates them and can make them throw up. (Basically their Ethanol. Ideally with faster onset from lower dosage, without becoming much more severe at higher dosage)
- Milk and cheese disagrees with them like Water, but WORSE. It is also psychedelic and causes hallucinations. Terrible idea. Keep it away from them.
- Processed foods should be less filling (might not currently be possible)
- Fruits might be intoxicating due to water content? But fruits don't typically have an actual water reagent configured
  - Give fruits a little water reagent (this seems like a reasonable change for the other species too, make fruits quench a bit of thirst)

### Scream
Vox have evolved to interpret information from their sophisticated vocalisations (which others describe as a horrible screech). This analysis also works on screams of other species.
While the information from this system can cheat line of sight, it's fairly short in range and only ever shows anything if someone screams, which is only really incentivized for vox players so it can't exactly be counted on.

- Vox can pinpoint screams within 10 tiles, even in unseen locations.
- The screams create a stationary indicator over the exact location, and fade out after 5-10 seconds
  - 10 tiles away is off the screen vertically, but the player could have been moving in that direction, making it come into view.
- Indicator shares basic info about the mob ("young diona", "middle-aged human")
  - I kinda wanted it to show Voice Identity names but I think that might be too much
- Indicator shows a snapshot of rough health state (Good, Okay, Poor, Bad, Danger)
  - If this is too powerful, maybe only show health data within a shorter range and/or within line of sight
- If the screamer was a Vox in the Sad state, the health data lies and shows Poor Health (if the actual health is better than that) to indicate "distress"
  - Would be funny if sometimes other vox came running to see whats wrong only to have to cheer you up
- The Vox Player also sees and hears that MGS-style ! popup when they pick up a low health scream (or a sad-vox scream)

Possible concern: screams can be spammed using @, although it seems unlikely that this ability alone would be enough to cause OTHER players to start abusing that capability. If it actually becomes a problem, could be changed to only hear screams signaled via the ability, which does have a cooldown


### Mood System

An abstract representation of how much the vox feels like it's "part of the group". Feeling like they are "on their own" in a cold cruel world has a tangible negative physiological impact on them. The penalties are not significant but the idea is that most players should still want to avoid them

- They have an inner "mood countdown". When it reaches 0, they enter the Sad state
- Sad state is indicated by a HUD alert. This is a psychological attack on the player to want to make their character not sad.
- Sad state also confers the following penalties:
   - 10% Run Speed Bonus becomes 10% Run Speed Penalty
   - Hunger decreases 50% faster (Goes through a full Hunger stage in 33 minutes instead of 50)
   - Scream cooldown increased to 20 seconds
- Hitting an "allied" player with a melee attack could take off a few seconds per hit
   - Might be a lot of trouble to code for not much gain
- Being in restraints could progress the mood countdown faster

Recovering Mood
- Getting hugged bumps the countdown to 6 minutes
- Screaming and having someone else scream in response within 5 tiles bumps the countdown to 3 minutes

# When Vox?
I have every intention to work on the actual implementation of the species and will create a roadmap for getting to roundstart vox once the design direction is settled
