# Revenant V2

| Designers | Implemented | GitHub Links |
|---|---|---|
| Warpzoned, Doru991 | :x: | TBD |

Heavy inspiration from EmoGarbage404's [Specter antagonist](https://github.com/space-wizards/docs/pull/262), as well as SS13's [Wraith antagonist](https://wiki.ss13.co/Wraith).

## Overview

This proposal aims to solidify the Revenant as a support antagonist whilst still leaving it to be a threat of its own accord.</p>
<p>Its gameplay loop has been reworked for this matter, making it much more of a singular threat in the long-run (akin to Space Dragons) instead of the current mid-round annoyance that it is, for a quick sum-up of what this document entails:

 - The Revenant has a proper presence in-game from both a roleplaying and mechanical aspect. (flavour & "specialized" abilities, both active and passive)
 - The Revenant has been given new vulnerabilities and thinks to look out for, consequentially making it so the crew also has things to counter the Revenant with. (eg. Salt) [SlamBamActionman's Holy Damage PR](https://github.com/space-wizards/space-station-14/pull/32755)
 - The Revenant may possess players at a time.
 - Player souls are ranked differently.

I have also deemed it appropriate to rename "Stolen Essence" to "Soul Essence" so that it's more on theme.

## Background

As it stands, the Revenant is a very lacking antag ghost role, primarily due to the fact that it nigh completely relies on other antagonists and/or accidents to actually start progressing, and seeing as those are entirely beyond the Revenant's control it ends up offering a very stale (and undesirable) gameplay loop of:

1. Visitting medbay to check for bodies (morgue or otherwise, though the latter would require the Revenant to have obtained the Defile ability, which, for being the Revenant's capstone of soul-sucking, it falls very flat (and is very varied)

2. Sitting around and being a mild and repetitive annoyance.

What we then bring you is a partial re-thinking of the Revenant both mechanically and aesthethically, which not only makes getting 'fun' abilities a more realizable dream, but also tries to mitigate current round-flow issues for the player themself (such as the aforementioned "Sitting around")

## Metaphysical Hitpoints (MHP)

The Revenant's HP will now be completely separate of the Soul Essence harvested.</p>
<p>MHP does not passively regenerate, making the only way to get it back through Soul Essence conversion, the Revenant starts with below average HP, similarly to the existing version.
 
However, there will be ways to upgrade the Revenant's MHP using the harvested Soul Essence, unlimited, with scaling, or otherwise.

## Vulnerabilities

The Revenant is intangible towards nearly all kinds of damage when metaphysical, the singular exception being holy damage. This characteristic may be made use of by the crew by, for example:
- Having the Chaplain bless certain things with their Holy Bible (take a spear, where, if thrown at the revenant even whilst they're metaphysical, will hurt and stick to them for a short while)</p>
- Spiking anything and everything with Holy Water so as to have it running through as many players' bloodstreams as possible (hindering possessions, perhaps?)

When possessing someone, the Revenant will not be able to pick up/pull the Bible, nor any container with one within, as they will burn similarly to how you do when touching a light fixture without gloves.

The crew may pour salt on a tile, preventing the (metaphysical) Revenant from passing through (akin to the mime's invisible wall ability), or, if they are possessing someone as they pass, they could either be revealed for a short while (maybe an effect similar to anomaly infections' for a bit/a dim purple glow), get hurt from it (holy damage), or even get forcefully shunted from that person to their original form.

## Soul Essence

Soul Essence is the Revenant's universal currency, almost everything revolves around its usage and consumption (buying and using abilities, upgrading passives, healing, etc..), you can obtain it solely via Harvesting.

### Soul Ranking

Souls are now divided into 3 different grades: **low**, **medium**, and **high value**.
 - **Low value** souls will be that of 'normal' personnel (ie. Civillians, Department Staff)
 - **Medium value** souls will be that of 'special' personnel (ie. Security Officers/Cadets, most of Command)
 - **High value** souls will be that of 'unique' personnel (ie. Captain, Head of Security, Antagonists)
 
Your soul's essence will be dependent on its grade, low value having the least base amount, and high value having the most. Players may, however, rise through the rankings via killing other player-controlled (take a would-be low value tider killing 3 Nuclear Operatives), excluding critters.

## Objectives

I have decided to keep the Revenant's objectives moderately simple, since I think malleability is very helpful for an adaptable antagonist such as this.

 - **Claim [X] (dependent on crew size) Souls** / **Claim [X] (also dependent on crew size) Soul Essence**
 - **Survive**

## Abilities - Everything below has not yet been updated as of 04/05/2025 (DD/MM/YY)

Abilities aren't tiered, contrary to EmoGarbage404's proposal, but rather, will use the same shop format the current Revenant possesses.

### Universal Abilities

Abilities under this category can be used by the Revenant whenever.

 - **Harvest** - Harvests the soul of a deceased/slumbering (ie. asleep or SSD) crew member, dealing high unholy damage if successful.
 - **Defile** - Defiles the surrounding area, ripping up floors, damaging windows, and opening most containers.
 - **Overload** - Overloads all nearby lights, causing light fixtures to pulse and flash-stun people as they break. (Short)
 - **Malfunction** - Ions every silicon in the vicinity, and has an added chance of granting other machines close-by sentience! (Medium)
 - **Mistify** - Enshrouds the Revenant in a shadowy mist that obscurs vision to everyone but the caster, similarly to the shadow anomaly's. (Instant)
 - **Command** - Gives the selected object the ability to be telekinetically controlled by the Revenant, an ability similar to that of a tether gun's, but slightly stronger. (Instant)

### Metaphysical Abilities

Abilities under this category can only be used when the Revenant is in its metaphysical form.

 - **Flicker** - Causes lights around the Revenant to flicker ominously, an ability innate to ghosts.
 - **Whisper** - Sends an otherworldly message to the selected target, spooky!
 - **Slip** - Makes the selected target slip. stun duration similar to that of normal soap.
 - **Hallucinate** - Makes the selected target start hearing things. (ie. Hallucination Event but for one person)
 - **Deafen** - Makes the selected target progressively more deaf until they can't hear anything but their own footsteps, dissipates after a while.
 - **Disorient** - Makes the selected target's controls go haywire, so that they're either completely inverted, stuck in walking one direction, or inputting late.
 - **Mark** - Marks the targeted crew member with an effect that periodically drains them of their energy, making them experience drowsiness, an effect similar to that of being drunk, in which after a while they'll forcefully enter an asleep state.
 - **Possess** - The Revenant may possess recently deceased/slumbering personnel, upon entering their body, they will be brought back to the Poor state, and any kind of DoT will be immediately and completely halted (ie. poison, bleeding). If the Revenant uses any ability on the mortal plane they emit a dim purple haze around them. Possessed bodies will be frighteningly cold and upon examining them they will appear pale. If the possessed body dies the Revenant is kicked from it and will be unable to gather Soul Essence for a while.

### Post-possession Abilities

Abilities under this category can only be used when the Revenant is possessing someone.

 - **Dispossess** - Allows the Revenant to leave the physical body at any point in time.
 - **Unshackle** - Frees the Revenant of any binds.
 - **Adhere** - Grants the possessed body no-slip capabilities. (Toggleable)
 - **Filch** - Makes it so that when stealing something from someone there's no visible action bar, similarly to thieving gloves. (Toggleable)

### Ability Upgrades

Items listed under this category are upgrades to existing abilities.

 - **Sleep Paralysis** - Affects: **Harvest/Possess** - Anyone the Revenant attempts to use Harvest/Possess on while in a slumbering state will be temporarily paralyzed as they wake up, a time in which the Revenant's abilities still take effect.
 - **Hyperload** - Affects: **Overload** - Overload's flashes now penetrate through any and all kinds of flash protection (sun glasses, welding masks, etc.).
 - **Mist Empowerment** - Affects: **Mistify** - Mistify's mist size now increases with each purchase. (every additional acquisition of this upgrade costs more than the previous one)
 - **Domain** - Affects: **Mistify** - Bodies within the Revenant's shadowy mist decompose considerably slower, as well as any Harvest or Possess used on said targets will have their Use Duration cut.
 - **Super Slip** - Affects: **Slip** - Slip's slips now stun for longer, duration similar to that of syndie soap.
