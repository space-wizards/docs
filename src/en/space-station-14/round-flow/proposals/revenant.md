# Revenant V2

| Designers | Implemented | GitHub Links |
|---|---|---|
| Warpzoned, Doru991 | :x: | TBD |

Heavy inspiration from EmoGarbage404's [Specter antagonist](https://github.com/space-wizards/docs/pull/262), as well as SS13's [Wraith antagonist](https://wiki.ss13.co/Wraith).

[Holy Damage PR](https://github.com/space-wizards/space-station-14/pull/32755)

## Overview

With this proposal we aim to add more self-sufficiency to the Revenant, as well as make it more fleshed out.</p>
<p>Some existing abilities have been reworked to better fit with how this new Revenant plays out on top of having the shop expanded, and not all abilities reveal the Revenant now. The Revenant is now extra susceptible to holy damage as per SlamBamActionman's PR, as well as being able to possess harvest-prone players, taking over their body completely. Lastly, it can upgrade some of it's abilities in exchange of souls.</p>
<p>Player souls are ranked differently.

## Background

Currently, the Revenant is a mediocre mid-round antag ghost role, due to it's dependence on crew deaths, which are entirely beyond the Revenant's control, the present gameplay loop usually consists of the Revenant having to visit med at least once in order to attain Stolen Essence, or pray for major disasters, which isn't fun at all, and even after having unlocked all abilities, there's not much going for the Revenant besides being a mild and repetitive annoyance.</p>
<p>What we bring you is a major re-design of the Revenant, which not only makes getting 'fun' abilities less of a grind, but tries to make it actually interact with the crew.

## MHP (Metaphysical Hitpoints)

The Revenant's HP will now be completely separate of the Soul Essence harvested.</p>
<p>MHP does not passively regenerate, making the only way to get it back through Soul Essence conversion, the Revenant starts with below average HP, similarly to the existing version, however, there will be ways to upgrade the Revenant's MHP up to double its base amount.

### Vulnerabilities

The Revenant is intangible towards nearly all kinds of damage when metaphysical, the one exception being holy damage.</p>
<p>When possessing someone, the Revenant will not be able to pick up the Bible, nor any container with one within, as they will burn similarly to how you do when touching a light fixture without insulated gloves.</p>
<p>If the Revenant passes/steps through salt that is poured on the ground, they will be revealed for a short while.

## Soul Essence

(Stolen Essence has been renamed to Soul Essence as to not make it feel like the Revenant's a complete kleptomaniac)</p>
<p>Soul Essence is the Revenant's universal currency, almost everything revolves around it's usage, you can obtain it solely via Harvesting.

### Soul ranking

Souls are now divided into 3 different grades: **Low-value**, **Medium-value**, and **High-value.**
 - **Low-value** souls will be that of 'normal' personnel (Civillians, common Engineers, common Medics, et cetera)
 - **Medium-value** souls will be that of 'special' personnel (ie. Security Officers and Cadets, most of Command)
 - **High-value** souls will be that of 'unique' personnel (ie. Captain, Head of Security, Antagonists)</p>
Your soul's essence will be dependent on it's grade, Low-value having the least base amount, and High-value having the most. Players may rise through the rankings via killing other player-controlled characters.

## Objectives

 - **Claim % souls**
 - **Survive**

## Abilities

Abilities aren't tiered, contrary to EmoGarbage404's proposal, but rather, will use the same shop format the current Revenant possesses.

### Universal Abilities

Abilities under this category can be used by the Revenant whenever.

 - **Harvest** - Unlock Cost: Free - Use Cost: Free - Cooldown: None - Use Duration: Short - Reveal Time: Short - Harvests the soul of a deceased crew member, dealing high cold damage if successful.
 - **Defile** - Unlock Cost: Low - Use Cost: Low - Cooldown: Average - Use Duration: Instant - Defiles the surrounding area, ripping up floors, damaging windows, and opening most containers.
 - **Overload** - Unlock Cost: Medium - Use Cost: Medium - Cooldown: Average - Use Duration: Short - Overloads all nearby lights, causing light fixtures to pulse and flash-stun people as they break.
 - **Malfunction** - Unlock Cost: Very High - Use Cost: High - Cooldown: Long - Use Duration: Short - Ions every silicon in the vicinity, and has an added chance of granting other machines close-by sentience!
 - **Mistify** - Unlock Cost: Medium - Use Cost: Low - Cooldown: Average - Use Duration: Instant - Enshrouds the Revenant in a shadowy mist that obscurs vision to everyone but the caster, similarly to the shadow anomaly's.
 - **Command** - Unlock Cost: High - Use Cost: Low - Cooldown: Average - Use Duration: Instant - Gives the selected object the ability to be telekinetically controlled by the Revenant, an ability similar to that of a tether gun's, but slightly stronger.

### Metaphysical Abilities

Abilities under this category can only be used when the Revenant is in it's metaphysical form.

 - **Flicker** - Unlock Cost: Free - Use Cost: Very Low - Cooldown: Short - Use Duration: Short - Causes lights around the Revenant to flicker ominously, an ability innate to ghosts.
 - **Whisper** - Unlock Cost: Very Low - Use Cost: Very Low - Cooldown: Near-Instant - Use Duration: Instant - Sends an otherworldly message to the selected target, spooky!
 - **Slip** - Unlock Cost: Very Low - Use Cost: Very Low - Cooldown: Short - Use Duration: Instant - Makes the selected target slip. stun duration similar to that of normal soap.
 - **Hallucinate** - Unlock Cost: Low - Use Cost: Low - Cooldown: Average - Use Duration: Instant - Makes the selected target start hearing things.
 - **Deafen** - Unlock Cost: Medium - Use Cost: Low - Cooldown: Average - Use Duration: Instant - Makes the selected target progressively more deaf until they can't hear anything but their own footsteps.
 - **Disorient** - Unlock Cost: Medium - Use Cost: Medium - Cooldown: Long - Use Duration: Instant - Makes the selected target's controls go haywire, so that they're either completely inverted, stuck in walking one direction, or inputting late.
 - **Mark** - Unlock Cost: High - Use Cost: Medium - Cooldown: Very Long - Use Duration: Short - Marks the targeted crew member with an effect that periodically drains them of their energy, making them experience drowsiness, an effect similar to that of being drunk, in which after a while they'll forcefully enter an asleep state.
 - **Possess** - Unlock Cost: Very High - Use Cost: High - Cooldown: Long - Use Duration: Medium - Reveal Time: Medium - The Revenant may possess recently deceased personnel, upon entering their body, they will be brought back to the Poor state, and any kind of DoT will be immediately and completely halted (ie. poison, bleeding). If the Revenant uses any ability on the mortal plane they emit a dim purple haze around them. Possessed bodies will be frighteningly cold and upon examining them they will apear pale. If the possessed body dies the Revenant is kicked from it and will be unable to gather Soul Essence for a while.

### Post-possession Abilities

Abilities under this category can only be used when the Revenant is possessing someone.

 - **Dispossess** - Unlock Cost: *Free (comes with Possess) - Use Cost: Free - Cooldown: None - Use Duration: Short - Allows the Revenant to leave the physical body at any point in time.
 - **Unshackle** - Unlock Cost: Medium - Use Cost: Medium - Cooldown: Average - Use Duration: Instant - Frees the Revenant of any binds.
 - **Adhere** - Unlock Cost: High - Use Cost: Free - Cooldown: Near-Instant - Use Duration: Toggleable - Grants the possessed body no-slip capabilities.
 - **Filch** - Unlock Cost: Very High - Use Cost: Free - Cooldown: Near-Instant - Use Duration: Toggleable - Makes it so that when stealing something from someone there's no visible action bar, similarly to thieving gloves.

### Ability Upgrades

Items listed under this category are upgrades to existing abilities.

 - **Sleep Paralysis** - Unlock Cost: Very High - Affects: Harvest, Possess - SSD and asleep personnel are now susceptible to having their Soul Essence reaped by the Revenant, as well as being possessed. The Revenant will take slightly longer to harvest and possess crew members if they are in a slumbering state.
 - **Hyperload** - Unlock Cost: High - Affects: Overload - Overload's flashes now penetrate through sun glasses, welding masks, and any other kinds of flash protection.
 - **Mist Empowerment** - Unlock Cost: Medium - Affects: Mistify - Mistify's mist size now increases with each purchase. (every additional acquisition of this upgrade costs more than previously)
 - **Domain** - Unlock Cost: Very High - Affects: Mistify - Bodies within the Revenant's shadowy mist decompose considerably slower, as well as any Harvest or Possess used on said targets will have their Use Duration cut.
 - **Super Slip** - Unlock Cost: Medium - Affects: Slip - Slip's slips now stun for longer, duration similar to that of syndie soap.
