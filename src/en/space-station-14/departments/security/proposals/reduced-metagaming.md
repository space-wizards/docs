# Reducing Metagaming

| Designers | Implemented | GitHub Links |
|---|---|---|
| SlamBamActionman | :x: No | TBD |

## Overview

This proposal contains a list of design changes and features aiming to reduce the impact of metaknowledge in the game. 

## Background

Right now there are several instances in the game where admins are expected to enforce rules related to metagaming. Some of these are related to the current round (e.g. using knowledge gained as a ghost after being revived), but there are also rules disallowing knowledge about the game in general. This mostly includes knowledge about antagonist items, behaviors and round events. This kind of "*metaknowledge*" rules are primarily restricted to Security and Command, and there are examples of metaknowledge that is allowed under the rules; knowing where maints loot spawns, secret Chemistry recipes and recognizing modifications to station layouts. 

There are two ways to reduce the impact of metaknowledge: allow it in the rules, or make it unviable to act upon it. Often this is done in combination; uplinks are an example of this. It's pretty much impossible to find out if a locked PDA is an uplink due to the high number of permutations in the lock. While it's technically possible for Security to confiscate every roundstart PDA and replace them with ones from the P-Tech vendor, it's simply not feasible in practice. This becomes more of an issue when a specific person has been suspected of being Syndicate (which is why we have stringent rules about PDA confiscating still) but it shows there are ways to design around metaknowledge.

The negative impact enforcement of metaknowledge is the following:
- Players need to self-assess what counts as abusing metaknowledge, possibly over-correcting as there's no ingame feedback.
- Disagreements about whether someone is abusing metaknowledge (e.g. a SecOff testing a pair of gloves for chameleon) can easily occur between players in a round, and is highly contextual.
- Admins need to put in time and resources enforcing these rules, which is always desirable to reduce.
- Players have to pretend they don't know about certain mechanics.

To find out where these problems lie, [I created a thread on the Discord](https://discord.com/channels/310555209753690112/1227226189358174209) to gather feedback from the playerbase where they have percieved metaknowledge abuse. This feedback is used as a basis for the changes and will be cited throughout the proposal.

The proposal will contain both mechanical design changes as well as rule changes. The rule changes are necessary as the goal of the PR is to reduce admin workload, and where it's not possible to eliminate them the goal will be to make them more clear and reduce grayzones. 

### Security & Resources

Other than explicit rules and Space Law, the main thing holding Security back is **time**, **materials**, **personnel** and **information**. Performing a search takes time, which holds up a SecOff that then becomes unable to respond or assist in other duties. Needing to utilize guns, stun batons and flashes means a SecOff must return to Sec to refill, and if materials are scarce this wait can be even longer. Similarly, health is a resource which will cause time and personnel loss from the SecOff needing to be treated.

Information helps mitigate these losses; knowing who to search, what materials to prepare and where to go. The more Security has of each resource the more effective it will be, and overabundance of one resource can make up for the lack of another. Some of these resources put strain on other departments however; materials may be necessary to craft or refill vital Security equipment, but those materials come from Cargo's work. Any rule change that relaxes the requirements on Security should instead impose a drain on its resources. For example, guessing uplink codes is usually too much of a timesink and takes up an officer's attention despite it being allowed by the rules, so it's rarely done.

## The Implant Problem

## The PDA / Uplink Problem

```admonish quote
Confiscating PDAs of anyone you suspect of being a traitor without proof.
```

Uplinks are in a kind of weird situation where it's one of the most powerful tools for a Traitor and in-universe a very well-hidden feature, but at the same time it's also one of the easiest metaknowledge items in the game. As soon as a player has been found using a traitor-exclusive item Security players have to pretend that the PDA isn't a high target to confiscate. The reason for this is because you generally want antags to be able to use all their TC during a round to make it interesting. As such, the PDA may only be confiscated for two reasons:
- Security finds an open uplink in the PDA.
- Security has previously found an open uplink in another PDA, and can thus pre-emptively confiscate any PDA they have reasonable suspicion of having an uplink.

Right now the rules are the main way of preventing overzealous Security confiscating PDAs. Traitors do have a gameplay option as well: The Uplink Implant. This implant does have the benefit of making PDA confiscating a non-issue, but the tradeoff is 2 less TC and with the stringent rules on PDA confiscating it's unlikely to get any benefit from it. There's no reason to keep the uplink open after the implant is used, so you only get value if another uplink has been found. Additionally it suffers from the vulnerability of implant checks.

### Proposal

The PDA is very easily the single point of failure with this problem, but it's also unique in its ringtone lock. 
