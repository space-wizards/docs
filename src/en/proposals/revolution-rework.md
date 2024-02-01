# Revolution Rework

| Designers | Implemented | GitHub Links |
|---|---|---|
| illdoodle | :x: No | TBD |

## Overview
***THIS CONCEPT IS TRANSLATED WITH “DEEPL TRANSLATE”, there is maybe translation errors***

Also it worth noting, that this is just _concept_. Unfortunately, i don't know C#

As many people know at the moment revolution gamemode is actually a legalized LRP slashing, which for many players for obvious reasons causes resentment, 
unwillingness to play the mode and even thoughts of its complete removal from the game.
upd: it’s already deleted :pepefrog:

On some SS13 servers for exactly the same reasons the mode is simply taken out of rotation and we should not exclude that in time the same fate awaits it in SS14, when people will get tired of the mess as it is now. 
For these reasons it is necessary for the mode to conduct a complete revamp of mechanics (code), rules, lore.

Also worth noting are the current flashes, which are a definite meta, because the player even by sound becomes aware of the game mode, which can affect his future decisions, which the admins obviously can't track. 
Also flashes are an easy excuse to choke the headrevs and ruin the round.
The forced conversion mech itself is stupid. People won't even have a choice of which side to step on, which will narrow the RP process in the mode and just turn it into a prototype of cultists, 
getting rid of any meaning and mood of the rebellion itself.

Anyways the goal of this concept is to not treat revolution as a LRP mode, thereby increasing its RP level and lowering player carelessness. 
It's also worth considering revolution as a major mode rather than a minor mode.

### Concept Abstracts
- unique scoring system
- voluntary entry into the revolution
- rev icon replacement
- additional avenues for recruitment
- rev uplink 
- various rebel paraphernalia
- cult-like alert

## Background
**You can read a more comfortable and beautiful version here --->** <https://docs.google.com/document/d/1KaitkDoAZFSBrNIc78K522gtLkDHlZaMzH9vNMe9Oz4/edit?usp=sharing>

It's contains additional comments, illustatrations, images and other MAYBE useful information.

**RUS VERSION --->** <https://docs.google.com/document/d/11Lpip1kL9xyVAVoQn-PVuqBHv-stovz8ZaweRDGwxtE/edit?usp=sharing>

## 1. GENERAL MECHANICS
### 1.1 Rev Uplink
- Headrevs have another distinctive feature, the rev **uplink implant**. It contains a variety of often decrepit, rusty and makeshift equipment.
- For **one recruited** it gives **1 Rebel Telecrystal** (RTC) to headrev’s uplink.
> A full list of gear is being worked on.
Approximately:
Soviet-made pistols, Mosinky, PPSh, Kalashnikovs, RGDs, various body armor, clothing, riot posters, homemade war makings, ammunition and other paraphernalia

**FOR WHAT:** These things will make the headrev stand out from the crowd or help him in some minor actions for later climax (like raiding an security patrol).

### 1.2 Holographic Armband
- In exchange for the icons, the revolutionary will be given the **ability "make intentions known"** which will create a red or blue-red **armband** on his shoulder for the headrevs.
- The **ability is one-time** and there is no way to remove this bandage once activated.
- To know the player's affiliation before activation requires examining the character - it will answer it in examine window (being a revolutionary).
- Once alerted _(1.6)_, all armbands automatically appear on the shoulders of the rebels.

**FOR WHAT:** To get rid of stealthy revolutions, add "rebel entourage" and replace trivial meta icons.

### 1.3 Mindshield
Has no effect on revolutionaries, but prevents further recruitment _(1.8)_.

### 1.4 Goldstein Books 
- There is a **free** item in headrev uplink _(1.1)_ - a **“brainwash book”.**
- Initially there is no books in the uplink _(1.1)_, but for every **[headrev count * 2]** revolutionary, the copy will be replenished by one piece. **[Maximum books = 6]**.
- When read **(by pressing Z)**, the character becomes a revolutionary. If a loyalist or rebel does it, nothing happens.
>Hereinafter, a loyalist is a character with a mindshield implant. In the points system, a loyalist and a head are different people.

**FOR WHAT:** Diversify the method of recruitment, allow simple revolutionaries to recruit, and make a reference to 1984.

### 1.5 Rebel Flag
- There is another free item in headrev uplink _(1.1)_ - rebel flag, which **can be placed** in different departments.
- Used exclusively for the points system _(3.2)_.
- If the department contains **[number of loyalists / 5]**, it is **automatically removed** after a minute.
- Normal crew can remove it manually activating the process for 1 minute (can't move). Can't be moved.
- **Can't be staged after** the evacuation shuttle has been dispatched.

**FOR WHAT:** to get rid of stealthy revolutions, diversify the strategic part of the mode, and supplement the points system.

### 1.6 Alert
> Automatic station notification:
“Attention! According to automatic internal sensors, there is crew misconduct on the station. There is a threat of a full-scale mutiny. 
We ask the station heads to take measures according to the SOP and common sense. If necessary, send a fax to the CC regarding the current situation.”

#### This announcement comes after the fact:
- **over 40%** of the crew have been turned to the revolutionary side 
- **over 80%** of the rebels have exposed their holographic armband
- **more than 2 heads or 50%** of the loyal crew are in a neutralized state within 5 minutes
- **more than 30%** of the crew has dangerous items (homemade, contraband, explosives) in their inventory
- **there are 3 or more rebel flags** on the station

**One minute before the announcement itself, a message will be given to all headrevs that they have been revealed.**

**FOR WHAT:** to get rid of covert revolutions. 

### 1.7 Headrev
**When a headrev dies**, revolutionaries are **not deconverted**, but there will be no new headrev. Calculation of the number of hedrevs is the same as before.

### 1.8 Recruitment
- Upon headrev ability, the victim will be presented with a **dialog box** with the options "YES" (join the revolution and convert) or "NO" (refuse the revolution)
- In order to recruit a person it is necessary for them **to be free and not implanted with a mindshield**. The outcome of the recruitment process is a handshake. 
- **[1 converted = 1 RTK]** to the revolutionary's uplink _(1.1)_.
- The ability has a 1.5 minute **cooldown**.
- Only the headrev himself or Goldstein's book _(1.4)_ can recruit.

> Will create as a partial necessity for meetings and speeches. Dialogue (RP process) - as a recruitment tool.

**FOR WHAT:** Completely abandon the violent conversion mechanic, diversify the RP process.

## 3. GREENTEXT
Due to the fact that normal programmatic determination of winners in the mode requires a large and intricate game code/mechanics, everything can be reduced to two simple things: 
the conditions of the greentext and the points system that will be displayed in it.
Let's start with the former.

_**all figures are based on a hundred players**_
_//imbalanced numbers are possible, analytics are needed_

### 3.1 Greentext Conditions
> in this chapter there is a difference between a loyalist _(mindshield person)_ and a head _(station command)_.

After 5 minutes, after the following possible combinations the greentext _(neutralized - dead/chained/out of station)_ will be displayed:
- **All station heads or headrevs** have been neutralized.
- **85% of the maximum number** of loyalists have been neutralized.
- **Revolution points are close to 65%** of the maximum or minimum number.

### 3.2 Revolutionary Points
**show up in the revolutionary's interface**

**MAX AMOUNT = [ [max heads * 7] + [max loyalists * 3] + 54 ]**

**MIN AMOUNT = [ - [max heads * 12] - [max rebels * 1.5] - 54 ]**

**+ 1** for a dead loyalist 

**+ 3** for an chained loyalist

**+ 4** for a dead head 

**+ 7** for an chained head 

**+** for a rebel flag _(1.5)_ if it stands in a 
 - **5** in Medical or R&D 
 - **9** in Eng or Cargo 
 - **13** in Bridge or Brig.
___
**- 0.5** for dead rebel 

**- 1.5** for chained rebel 

**- 7** for a dead headrev

**- 9** for a burned/thrown into space goldstein book _(1.4)_

**- 12** for chained headrev

**If none of the conditions are met for a long period of time, there should be admin intervention (ERT/DS), or an attempt to fulfill the station goal.**

## 4. CONCLUSION
In this near-concept, I tried to balance the partial simplicity of SS14 with its RP component. In general, there are not many mechanics, but their relative casualness gives ample room 
for roleplay and adequate wagering. Of course, as many will say everything will end in a massacre, but this massacre will be accompanied by a semblance of conflict escalation 
and the very spirit of rebellion, which is so lacking in the current mode.

The concept is open for criticism, I will be glad to argue, listen to opinions, finalise some points. 

P.S. This is my first attempt to add design doc and work with md files.
