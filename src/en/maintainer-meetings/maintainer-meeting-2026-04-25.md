# Maintainer Meeting (2026-04-25)

:::info
**Attendees:**
- ArtisticRoomba
- Slarti
- Princess
- Scarky
- Ada
- Slam
:::

This meeting was recorded:

{% embed youtube id="meow meow :3" loading="lazy" %}

## Space Law its Future and its Purpose (Princess)
Relevant internal discourse thread: [Space Law, Its Purpose and Future](https://forum.spacestation14.com/t/space-law-its-purpose-and-future/27179/8)
Overall space law sucks and needs to be fixed. It's one of those things that gets kicked around without action being taken so I made a discourse thread to discuss what to do about it.
After this meeting I'll make a PR to make the changes discussed as per the thread and this meeting, although anything out of scope (such as locker BUI) I'll make an issue for.
In addition I'm going to leave much of the microdiscussion about crime stacking to the actual PR. 
- Why does space law exist?
- Are there any laws which don't help fufill the purpose of space law, or are counter-intuitive to why it exists.

## Free Agents and what to do about them? (Princess)
Relevant internal discourse thread: [The Future of Free Agents](https://forum.spacestation14.com/t/the-future-of-free-agents/27253)
Free Agents have always been a mild pain rules wise, but that pain mostly comes as a result of rules like 2.9 and such.
This was especially an issue when we had roundstart Wizard who made the entire station into free agents resulting in an absolute slugfest. 
Free Agents aren't something we can just remove, as many roles rely on having freedom to choose how they approach their role. In addition having a role whos round impact is entirely dictated based on how players choose to play them is generally good.
I see the survivor issue as being more of a "You give the entire station guns and a pass to shoot whoever" and expect the round to not end literally immediately. 
- What are the expectations and limitations of free agents, and should we have the same expectations for every role?
    - If different free agent roles have different expectations is that something we should account for in rules or in design? 

## Slowing down the Release Schedule (Princess)
Relevant internal discourse thread: [Slowing down the release schedule](https://forum.spacestation14.com/t/slowing-down-the-release-schedule/27131)
Release Schedule is being slowed down from bi-weekly to the fourth week of every month. It would've been every 4 weeks but Discord doesn't let us set it as that so this is close enough :^) 
- We need to construct a message for announcements about this, or designate someone to construct one.
    - We also need someone (likely Zoldorf) to send the message.
    - `Slarti`: Probably does not need Zoldorf, any PM can do a small announcement. And we need to adjust the docs page.

TODO: Adjust docs pages mentioning the bi-weekly release.

Notes for the announcement:
- "include an emphasis about the sustainability and health of the team"
- "we are slowing down updates due to staff restructuring and in order to keep those who are not on break from becoming burnt out"

## Some Misc Hotfixes (Princess)
Discussing a couple misc hotfixes we should try and get into this stable if we can.
- [43654 - Fix AI Holopads from breaking the client](https://github.com/space-wizards/space-station-14/pull/43654) 
    - Was supposed to get into this staging but the max cap heisentest prevented it from being merged
- [Revert #39173](https://github.com/space-wizards/space-station-14/pull/43729)
    - Linked Issue [43698](https://github.com/space-wizards/space-station-14/issues/43698)
- No PR currently, fix the heat shader overlay to have the correct gamma

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- Princess
- aada
- SlamBamActionman
- Slarti
:::

- [43492](https://github.com/space-wizards/space-station-14/pull/43492) New janibelt/janicart ItemMapper and trash bag equipped sprites
- [43537](https://github.com/space-wizards/space-station-14/pull/43537) Wire brush can scrub away webs and posters
- [43385](https://github.com/space-wizards/space-station-14/pull/43385) Move Kudzu Removal from Shared Seed Shenanigans to Plant-B-Gone
- [43500](https://github.com/space-wizards/space-station-14/pull/43500) Cool down surroundings
- [43444](https://github.com/space-wizards/space-station-14/pull/43444) Add FleetingClothingComponent
- [43615](https://github.com/space-wizards/space-station-14/pull/43615) Elite webvest has pockets again
- [43629](https://github.com/space-wizards/space-station-14/pull/43629) Lower amount of wirebrushes
- [43641](https://github.com/space-wizards/space-station-14/pull/43641) Add BreakOnAccessBreaker check for the Knock spell
- [37983](https://github.com/space-wizards/space-station-14/pull/37983) Monkeys can now put people into disposal bins
- [43281](https://github.com/space-wizards/space-station-14/pull/43281) The Grand Max Cap Rewrite
- [43590](https://github.com/space-wizards/space-station-14/pull/43590) Add changeling flesh clothing transformation
- [43098](https://github.com/space-wizards/space-station-14/pull/43098) Container toolshed commands
- [40900](https://github.com/space-wizards/space-station-14/pull/40900) NPCs combat improvements
- [43560](https://github.com/space-wizards/space-station-14/pull/43560) Mail Fraud [Traitor Objective]
- [43558](https://github.com/space-wizards/space-station-14/pull/43558) Tile gun starts filled
