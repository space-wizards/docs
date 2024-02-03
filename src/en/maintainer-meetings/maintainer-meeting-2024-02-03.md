# Maintainer Meeting (03 Feb 2024)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 03 Feb 2024 18:00 UTC

**Attendees:**
- DrSmugleaf
- ShadowCommander
- Lank
- Chief_Engineer
- Jezithyr
- faint
- EmoGarbage
- notafet
- Julian
- Ed

## Singleton entities | metalgearsloth
- I've had to use these before so stuff serializes properly (e.g. arrivals map, centcomm map)
- Do we add engine support (atm I have been using AllEntityQuery\<T> and returns but would be nice to reduce duplication)
    - **Sure WYCI**
- Gamerules are doing something similar as well (e.g. making nukeops exclusive or whatever if it's a nukeops round)
    - **Game rules shouldn't all be singletons, but it's fine if someone codes one that is.**

## Freezing pet clothing | metalgearsloth
- Copy-paste pngs and shift pixels everywhere
- Massive code debt
- Just use displacement maps dear god
- **We freeze new sprites (gas tank sprites are still allowed)**

## Handling deleted entities on datafields for refs | metalgearsloth
- So for example device networks don't cleanup data and have a bunch of invalid entity references which maploader prunes but this is mid
- There's other instances of this too where you need to do bi-directional entity termination handling
- Do we just add some way to subscribe to a particular entity deleting as an easier way to handle this E.G
- **Yes WYCI, but also when any disconnection not just deletion**
    - >EntityA references EntityB
    - >EntityB has no practical reason to reference EntityA besides cleanup
    - >EntityA subscribes to EntityB termination (like a dictionary or something) and cleans itself up, meaning you don't need to add any extra handling on EntityB and the datafield stays clean
- This would also handle cases where it might be EntityA + EntityC + EntityD referencing EntityB and you don't need to add some list to bloat out EntityB
- Alternative we just keep storing references in components ig

## Design docs | Lank
- **We allow docs that won't be implemented by the author as long as either the design doc is good or someone else wants to implement it.**
    - If a design doc is left accepted but not implemented for a long time we can remove it later.
    - This gives a list of things to implement for contributors and maintainers.

## Current freezes
- Vehicles are restricted.
- New pet clothing is frozen (except for gas tanks).

## Current admin issues
- Ahelp relay does not tell you whether the player has disconnected or not. [23716]
- Ahelp window should tp you to the last character if the player is disconnected [20189]
- Specific admin actions can only be performed on logged in players(e.g. Erase) [23796]

## Early Access Roadmap
- **nothing on this roadmap matters except early access trailer and admin issues.**
- A trailer for Steam
    - ask enrico about the trailer
- [**game admin items**](https://github.com/space-wizards/space-station-14/issues/23246) [c#23985](https://github.com/space-wizards/space-station-14/pull/23985)
- gamemodes/antags
    - dynamic [c#16548](https://github.com/space-wizards/space-station-14/pull/16548)
    - wizard (keron)
- Steam account linking
- The game runs like shit how do people play this
    - "IDK but maybe when I fix the watchdog you can figure it out easier" | 09/09/2023
    - "I only played VRChat since last time and VRChat runs like shit so I don't know how people play this" | 23/09/2023
    - "" | 21/10/2023
    - Miros runs fine | 16/12/2023
        - I am 5 parallel universes ahead of you
    - We have a new Minecraft server it runs fine now (SS14 runs fine, really)
    - Here lies Minecraft long live Satisfactory
    - PJB is skiing

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

## PJB personal roadmap
- Audio rework DONE NO WAY
- Fix infra
- Watchdog rework: testmerges, **better way to get traces from game servers**
- Fix perf oh god
- PJB is reading about window scaling
