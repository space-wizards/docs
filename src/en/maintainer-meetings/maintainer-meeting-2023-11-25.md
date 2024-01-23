# Maintainer Meeting (25 Nov 2023)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 25 Nov 2023 18:00 UTC

**Attendees:**
- DrSmugleaf
- PJB
- EmoGarbage
- Faint
- Lank
- Jezithyr
- Chief Engineer
- KeronshBB

## Faster get/tryget methods for engine with arch | metalgearsloth
- Might not be safe with multiple threads from content
- Also check unsafe code in Arch
- **Arch should not cause unsafe-type bugs if incorrectly accessed through multithreaded code**


## Atmos method events | ElectroSR
- Remove them, they are private.
- **If downstreams need them, they can revert the change (or whatever subset they need for their features)**


## Early Access Roadmap
- **nothing on this roadmap matters except early access trailer.**
- A trailer for Steam
    - ask enrico about the trailer
- gamemodes/antags
    - dynamic [c#16548](https://github.com/space-wizards/space-station-14/pull/16548)
    - wizard
- The game runs like shit how do people play this
    - "IDK but maybe when I fix the watchdog you can figure it out easier" | 09/09/2023
    - "I only played VRChat since last time and VRChat runs like shit so I don't know how people play this" | 23/09/2023
    - "" | 21/10/2023


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
