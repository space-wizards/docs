# Paradox Clone

| Designers | Implemented | GitHub Links |
|---|---|---|
| Slartibartfast | :warning: Partially | TBD |

Based on the [original design](https://github.com/tgstation/tgstation/pull/71141) from Shadyyy66 for Space Station 13.

## Overview
The paradox clone is a mid-round ghost role antagonist that is spawned due to a space-time anomaly as a random event. The clone has the appearance, name, outfit, ID, DNA, fingerprints and other traits of a random person on the station. Its only other equipment is a toolbox to get out of locked rooms and a nitrogen supply in case the clone is a vox.
The objective for the clone is to silently kill and replace their original to fix the time flow and blend in until the end of the shift to escape to CentCom.

## Goals
- The paradox clone is supposed to be a less destructive, roleplay-focused way to cause chaos on the station and sow distrust among the crew.
- Reward good communication between crewmembers: A clone is easily identified if you can ask them about previous interactions you had with them or if someone is spotted at two places at once.
- A chance for players to get creative to fulfill the objective: You will have to use your access and ability to blend in to silently follow your original without being seen by them and then find an opportunity for the kill. If someone catches you you can still try to convince others that you are in fact the original.
- Lower the potential for metagaming for the changeling (once it is implemented): Seeing a copy a crewmember does no longer directly lead to the conclusion that a changeling is on the station.

The paradox clone can also serve as a replacement for the terminator. This antagonist was particularly problematic as its superiority in combat encouraged players to go on a murder spree. The clone solves this problem both meachanically and from a lore perspective:
- You are a normal crewmember, not a violent murder machine. You only kill so you can survive the time paradox yourself and return back to a normal life once your objectives of replacing the original and escaping to CentCom are fulfilled.
- You don't have any special equipment or powers, so you will have to use stealth for your advantage.

## Implementation details
Cloning code will be refactored to properly copy traits, DNA, fingerprints and any other relevant details from the original.
The clone will get a copy of the outfit and basic equipment (e.g. toolbelts or goggles) the original is currently wearing, restricted by a whitelist. If this causes any problems from a code perspective alternatively the original's roundstart loadout can be used. However, this would be less ideal since many players customize their character during the round.

### Ghost role information:

A freak space-time anomaly has teleported you into another reality! Now you have to find your counterpart and kill and replace them.

### Objectives:
- Kill and replace  \<target\>, \<job\> to fix the time paradox. Remember, your mission is to blend in, do not kill anyone else unless you have to!
- Escape to CentCom alive and unrestrained.

## Possible optional additions
- Give the paradox clone a chance to be friendly instead of an antagonist for more roleplay opportunities and to prevent clones from being seen as 'valid' to kill.
- If the original is an antagonist, additionally give the clone the original's objectives as well. This makes them an even more perfect copy and may lead to some interesting interactions between traitors where you first cooperatere and then inevitably betray each other.
