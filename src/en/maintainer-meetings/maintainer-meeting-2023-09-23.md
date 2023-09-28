# Maintainer Meeting (23 Sep 2023)

**Time:** 23 Sep 2023 18:00 UTC

**Attendees:**
- EmoGarbage
- ElectroSR
- Visne
- DrSmugleaf
- notafet
- Lank
- Visne
- Julian
- Jezithyr
- Chief_Engineer
- PJB (hiiiiiiiiiiiiiiiiii)
- mirrorcult
- TheQuietOne
- miku
![miku](https://media.discordapp.net/attachments/813722892948733982/1155204273777422366/miku.png)
- moony
- Slava0135
- ShadowCommander

## Change ToString & Parse for EntityUid or NetEntity | ElectroSR
- Commands that take either are now ambiguous, how do we differentiate between them
- **All commands should take NetEntity**
- What do we do for command output
    - **NetEntities should be the one getting presented to the user most of the time**
    - **e for EntityUid**
    - **n for NetEntity**
    - **c for client-side**

## Remove transparent / non-occluding containers for sprites | ElectroSR
- Right now they can not occlude lights and not occlude sprites.
- **Force containers to always occlude sprites.**
- **Wish we could put containers in content instead.**

## DERAILMENT: Containers as entities, how do we do it?
- **Entities with ContainerComponent and ContainerSlotComponent.**

## Entity categories | ElectroSR
- **they are good**

## Early Access Roadmap
- **nothing on this roadmap matters except early access trailer.**
- A trailer for Steam
    - Also the >>>>**screenshots**<<<< for steam and the website
    - holy shit we have **replays** now
- gamemodes/antags
    - dynamic [c#16548](https://github.com/space-wizards/space-station-14/pull/16548)
    - revolutionaries [c#18477](https://github.com/space-wizards/space-station-14/pull/18477)
    - wizard
- The game runs like shit how do people play this
    - "I only played VRChat since last time and VRChat runs like shit so I don't know how people play this" | 23/09/2023


Crashes / Critical bugs: (when are we moving these to GitHub)
- Crashes the server reliably.
- Something that bricks your client often (needs a client restart).
    - Example: Blackscreens the client until you reconnect.
- If something ruins the round and is disabled because of it.
    - Example: Communal lung bug.
=> till next time
like and subscribe
smash that button
~~did you know only 6% of contribs join this meeting?~~ According to YouTube's statistics, 
