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

To find out where these problems lie, [I created a thread on the Discord](https://discord.com/channels/310555209753690112/1227226189358174209) to gather feedback from the playerbase where they have percieved metaknowledge abuse. This feedback is used as a basis for the changes and will be cited throughout the proposal.

The proposal will contain both mechanical design changes as well as rule changes. The rule changes are necessary as the goal of the PR is to reduce admin workload, and where it's not possible to eliminate them the goal will be to make them more clear and reduce grayzones. 

## The PDA / Uplink problem

