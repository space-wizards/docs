# Maintainer Meeting (11 February 2023)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 11 February 2023 19:00 UTC

**Attendees:**
- Remie
- keronshb
- ElectroSR
- DrSmugleaf
- Vera
- PJB
- moony
- Visne
- Jezithyr
- flipp
- Zoldorf
- Wrexbe

## Standardize and document naming for (system) dependencies | Vera
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/1070066968419381320)
- [Original discussion](https://discord.com/channels/310555209753690112/770682801607278632/1070064771761709076)
- **Remove the prefix and suffix.**
- What about UIControllers, where there is SharedHandsSystem, HandsGUI, HandsUIController.
- Keep it explicit with `_handsSystem`.
- **Make a maintainer vote for whether or not we enforce this (either an analyzer or as part of review.)**

## Debug vs DebugOpt vs Release vs ReleaseTools build configurations | PJB
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/1072637756955693067)
- **Yes**
- Release (closest to the launcher version) would be closer to what we have for the downloadable public build (FULL_RELEASE).
    - Can't be compiled easily because of filepath changes.
- Current release configuration (debug tools available) can become DebugOpt.
- Current debug configuration is the new Debug configuration.
- Tools (for mapping) is release with checks disabled and optimizations/tools enabled (tools is the launcher connect command).
- to summarize:
    - `Debug`: optimizations disabled, asserts enabled, tools enabled.
    - `DebugOpt`: optimizations enabled, asserts enabled, tools enabled.
    - `Tools`: optimizations enabled, asserts disabled, tools enabled.
    - `Release`: optimizations, asserts and tools disabled. As close to the launcher builds as you're gonna get while it stills runs from your repo.
- **Don't disable exception tolerance in debug.**

## Medical refactor | Jezithyr
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/1073932941878636624)
- This is basically old baymed (+ rimworld ~~+ EFT~~)
- Take notes on brainmed
- Don't make it overly complex
- Make cloning lategame/not a solution to everything
    - And implement speedcloning where releasing someone too soon makes them miss body parts

## Game admin tooling | DrSmugleaf
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/1073933000204619807) (mistake)
- LOGS BAD (kind of)
- Not being able to search by username (have to correlate with the player list)
    - Same in the player list
- Replays will help
- Add more buttons to the player panel (following players is ass)
- Make admin logs clickable (we have rich text now)
- Add UI for role bans
- Whitelist UI
- Admin wishlist [#13270](https://github.com/space-wizards/space-station-14/issues/13270)
- [Admin wishlist 2](https://github.com/space-wizards/space-station-14/issues?q=is%3Aopen+is%3Aissue+author%3A%40me+wishlist)
- [Admin wishlist 3](https://github.com/space-wizards/space-station-14/issues/13269)
- Fix not being able to use role ban and role time commands with offline players
- Add month and year to notes
- Greyscale/Grey out older notes
- Add UI to see a player's inventory including pocket items
- Admins can't see whispers
- Antag/ghost role bans
- Add categories to admin logs (groups of types) (not in the database, do it filtering on the frontend)
- Add a cvar to delete old admin logs

## Server pop with the new large map | Pancake
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/1073935104176562236)
- [Admin chat Discord message](https://discord.com/channels/310555209753690112/811324338099585036/1073934949633237092)
- Do we increase player cap
    - idk
    - **make a vote**
    - **mirror take the wheel**
- Do we change the player cap based on the map
    - probably not
- Do we make an US East server
    - **yes**

## Early Access Roadmap
- gamemodes/antags
    - dynamic | mirror
        - lings?
            - needs DNA
        - blob | Remie
        - revolutionaries
            - we want a generic antag overlay system
            - loyalty implant
            - faction system
- EL BODY SYSTEM | jez
    - some refactors were done by mirror, still some left
    - surgery died in the war of 1992
        - Mirror died in the war of 1993
    - limb damage.....
- Salvage proc gen | moony
    - she did it go port it https://github.com/Citadel-Station-13/space-station-14/tree/master/Content.Server/_Citadel/Worldgen
- body system but again
- body system
- __***ENGINE EDITOR***__ | PJB
    - could benefit from full state reload
- movement refactor
    - Client side movement?
        - a smidgen
            - as a treat
            - acruid pls com bak
- combat rework (needs to be bikeshedded)
    - https://github.com/space-wizards/space-station-14/issues/3378
- ghostrole/antag bans
- experimental science
    - "Science is still a piece of shit" - Vera 28/05/2022
    - "I haven't played the game in 2 years" - Vera 07/01/2023
    - "Uhhhhhhhhhhhhhhhhh I'm sorry EmoGarbage" - Vera 11/02/2023
- State mandated Xonotic matches | PJB
    - Please I have severe withdrawal symptoms
    - Replaced by private SS14 playtests
    - Woman down
    - She added Miku to her server (real) now you can play as miku pls play with her
- The game runs like shit how do people play this
    - still does | PJB 28/05/2022
        - "how do people play this game" (high pitched scream) | PJB 28/05/2022
    - Slightly better | PJB 11/06/2022
    - It's better but still not as good as I'd like it to be | PJB 25/06/2022
    - I haven't played the game since | PJB 16/07/2022
    - "Please read the last line of that subsection" | PJB 30/07/2022
    - "Please unread the last line of the previous subsection" | PJB 07/01/2023
    - "I spent the last two weeks coding Rain World" | PJB 21/01/2023
    - "I should've tried to run it from the AirBNB that I was staying over in my skiing trip but I didn't" | PJB 11/02/2023
- A trailer for Steam

Crashes / Critical bugs: (when are we moving these to GitHub)
- role timers not counting properly (pjb added a thing to check if its a db issue) (epico)
  => till next time
