# Traitor Reputation System

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| Princess Cheeseballs | coder names here | :white_check_mark: Yes or :warning: Partially or :information_source: Open PR or :x: No | PR Links or TBD |

`Designers` should be the names that you, the authors of this document, use on GitHub and/or Discord. This is optional but strongly recommended, since:

- This acknowledges credit where it is due
- People who are confused about the written intent can use this information to contact the authors

`Coders` should be the names of the contributors who plan on implementing this feature. To get a design doc approved you will need either
- have the technical knowledge to be able to implement the proposed feature yourself.
- have someone else who agreed to do this for you.
- already have an existing implementation elsewhere that just needs to be ported.

In either case you will have to write an outline on how you plan to implement this feature in the **Technical Considerations** section to show that is technically sound and feasible.

`Implemented` is the status of the feature.

Github links can include multiple PRs, if relevant.

## Overview

Traitor Reputation is a system which would enhance the roundflow of the traitors gamemode as well as adequately managing the threat level of traitors. 
It aims to lower the power floor of the average traitor to more predictable and less chaotic levels while increasing the threat ceiling of the average traitor. 
In addition, it aims to provide a balanced way to allow traitors to either ignore or go above and beyond their objectives to make the gamemode less predictable.

## Background

Traitors in its current form sucks. There's a lot people want out of the gamemode and the vast majority of it is conflicting and contradictory. Balance sucks in a way that can't be fully addressed by small balance changes and patches.
There have been plenty of controversial PRs and Discord discussions in regards to Security and Traitor balance and what to do about it, with few being the perfect solution anyone is looking for (if one were to even exist).
The way I see it, the issue with traitors is that it should be a gamemode that promotes creativity and skill and should show off the depth the game has to offer in terms of content and possibilities. 
However, this fails due to how the gamemode is structured. Objectives are usually extremely direct and binary which curbs creativity, and ignoring your objectives and doing your own thing opens the floodgates for unfun murderbone and round griefing which requires a heavy hand to regulate also dissuading creativity and lowering the skill ceiling. 
I believe that if traitor balance is to be fixed, the gamemode needs some genuine depth to facillitate skillful play that supports players being able to choose how they want to play their traitor. 

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.

## Features to be added

Traitor Reputation is a loose "Street Cred" value which allows you to unlock more parts of your uplink as you raise it.
Your traitor rep is visible in a new tab of your uplink dedicated to "Blood Red Bounties" a gig economy mercenary work app for all your evil needs.

Blood Red Bounties will offer a variety of jobs which can be used to increase your reputation, with harder jobs giving you more rep. Some difficult jobs can also give extra TC or items as well.
Syndicate Agents can also choose to offer up some of their TC to place bounties in the app, these bounties cost a minimum of 1 TC to place and are extremely modular allowing you to request anything from "Complete my objectives" to "Cook me up 200u of Meth"

Traitor Rep starts at 0 and can go up to 100, at different levels it allows you to unlock stronger and more expensive items from your uplink.

#### =<10 Basic Uplink (Extremely basic items that can get the job done if you plan well)

Most stealth items, Cheap 3TC or less weapons, Ammo, Smoke Grenades

#### 11-20 Expanded Gadgets (Items that help you execute a plan with little hic-ups)

Thieving gloves, Lobbying Bundle, C4, Cobra, Python, Chemical Synthesis Kit, Whiteholes

#### 21-30 Extra-Lethal Weapons (Items that are meant to give you an explicit combat edge)

Webbed Vest, Energy Sword, Combat Medkit, Syndicat, Reinforcements, Grenade Penguins

#### 30-40 Excessively Lethal Weapons (Items that are way more lethal and bigger guns enough to be a budget nukie)

Hristov, C-20, Bulldog, Hardsuits, Holoparasites, Shrapnel Grenades, Hyperzine

#### 41-50 Items of Excessive Destruction (Items that destroy entire departments, enough to be a real nukie)

China Lake, L6, All explosives

#### 51-100 Unlocks Station Destroying Items and Victory Assurance Items (Items that are basically DAGD only, and items that can make your victory assured)

Singularity Beacon, ~~Storage Implant~~

Traitor Rep will increase slowly over time if you've completed some of your objectives already but it will not increase if you haven't done any of your objectives. 
Every minute where at least one of your objectives is green, your reputation will increase by 1. (Note this means keep a fellow traitor alive will either have to be reworked or removed)

Traitor rep can also be increased by doing contracts, contracts are gig jobs that are available first come first serve to whoever claims them. You will have a limited amount of time to complete them and failure will result in adequate punishment.
Every 5 minutes any unclaimed jobs are refreshed for new jobs. Jobs that are claimed are visible to everyone once claimed giving the opportunity for someone to poach your job. 
There are three types of contracts:
- Syndicate Contracts
- Corporate Contracts
- Agent Contracts

#### Syndicate Contracts
Syndicate Contracts are job contracts that are available to any traitor, appear for a limited amount of time and dissapear once completed. 
These have a varying difficulty but offer the best rewards and reputation. There is always at least three available at a time. 

#### Corporate Contracts
Corportate Contracts are more stable but less flexible, only one of them appears at a time but every traitor gets an exclusive corporate contract straight from their employer.
Due to the internal nature of these contracts, they offer less reputation and never give you bonus TC (you're already getting paid) but sometimes offer a reward item.

#### Agent Contracts
Agent contracts are unpredictable. Another agent has to put them up so they wont refresh if unclaimed and there's no guaratees the agent who put it up won't screw you over even if you succeed. 
However, if you need TC these can be a great way to get TC, and if you don't want to do your objectives, these are a great way to offload them onto someone else. 

In addition to the three types, contracts vary in difficulty and the reputation reward is dependant on difficulty.

#### Easy
These jobs won't raise much heat but also won't increase your rep by that much. If you do get caught, you're likely not spending more than 5 minutes in jail.

+5-10 Rep

Commit minor sabatoge to your department, Waste station resources, Make a mess

#### Normal
These jobs require you to commit 


## Game Design Rationale

I wanted to ensure that Traitor Reputation allows and facillitates more interesting syndicate strategies while allowing looser rules. I also wanted to give security some things to latch onto with traitors that way they can appropriately react and try to prevent a traitor from snowballing into a massive threat. 
A big issue with traitors I've seen is security is often caught completely by surprise without really anything they could do. Oftentime security just has someone walk in with a webbed vest and an e-sword and they don't even have time to open the armory. This makes that scenario far more of a security skill issue since they will have ample time to figure out someone is a traitor and hopefully stop them from snowballing through good detective work and contraband confiscations. 
This also has the doubled effect of giving security things to do during a quiet syndie game. There's some clues to follow, some minor crimes being comitted, always something to chase and do.

Lastly, I wanted to nerf the traitor strategy of blitzing your objectives. It's very strong and can also be very not fun as it often leads to one of three things:
- Important command member dies so captain calls evac early  (lame)
- You do your objectives and no one catches you so you just have to wait for the round to end with nothing else to do (lame)
- You get round removed early on because you were a kill target and your game is over before it even began (lame)

This doesn't prevent traitors from doing these things, but it means it requires more skill, either from getting makeshift weapons or blitzing a number of syndicate objectives, both of which are more interesting than spawning a thieves gloves minibomb combo in your hand.

In addition, I didn't want traitor rep to just be a "number that ticks up to prevent you from getting the best gear" I felt it was important to reward traitors for interacting with this system and enable more types of traitor playstyles.

Consider addressing:
- How does the feature align with our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosphy?
- What makes this feature enjoyable or rewarding for players?
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- How does it enhance player cooperation, competition, or emergent gameplay?
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?

## Roundflow & Player interaction

Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
- Which department will interact with the feature? How does the feature fit into the [design document](../space-station-14/departments.md) for that department?

## Administrative & Server Rule Impact (if applicable)

- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
- How are the rules enforced mechanically by way the feature will be implemented?

# Technical Considerations

- Does the feature require new systems, UI elements, or refactors of existing ones? Give a short technical outline on how they will be implemented.
- Are there any anticipated performance impacts?
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
