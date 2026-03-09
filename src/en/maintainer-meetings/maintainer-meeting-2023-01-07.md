# Maintainer Meeting (07 January 2023)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 07 January 2023 19:00 UTC

**Attendees:**
- Moony
- Visne
- ElectroSR
- Remie
- Flipp
- ShadowCommander
- DrSmugleaf
- Vera
- PJB

## Using source generators for (de)serialization | DrSmugleaf
- Expression trees were a mistake
- **sounds good**


## Enforce AccessAttribute and better documentation on new PRs | metalgearsloth
- [Discord link](https://discord.com/channels/310555209753690112/900426319433728030/1060739900758044792)
- **yes**
- may not work for shared components
- check if it works with implementations of the whitelisted type for shared systems
    - If it doesn't, make [Access] take an optional list of strings for types in server/client
- ping Vera if something goes terribly wrong


##  Minify meta.json files | metalgearsloth
- [Discord link](https://discord.com/channels/310555209753690112/900426319433728030/1060432256092618753)
- [GitHub PR](https://github.com/space-wizards/space-station-14/pull/13035)
- Do we minify them
    - **no**
- If not change the editorconfig to match the current style (2 space indents)
    - **yes**
- Apparently some people copypaste existing meta.jsons to create new ones, which has caused many errors in multiple RSIs
- Reasons not to:
    - harder to edit
    - harder to review
    - ?
- Reasons to:
    - there's editor plugins that minify and unminify automatically for you
        - this isnt a reason
    - ~~saves 1.5 MB~~ not important? it's compressed when game is packaged, etc
    - ?


##  Require all public fields and methods to include xmldoc comments | moony
- [Discord link](https://discord.com/channels/310555209753690112/900426319433728030/1055341182248558623)
- Make sure every method is documented
- Document every field
- **Put this in the PR guidelines**
- https://docs.spacestation14.io/en/getting-started/pr-guideline


##  Rename entityquery to componentquery | metalgearsloth
- [Discord link](https://discord.com/channels/310555209753690112/900426319433728030/1030122281462136862)
- **Yes**
- Wait for archetypes to rename them


##  Should Helpers and Extensions be moved to EntitySystems | ShadowCommander
- [Discord link](https://discord.com/channels/310555209753690112/900426319433728030/1018323213517856838)
- **Yes, if it refers to any manager, system or entity**
- **If it's a random helper to save code it doesn't need to be**


## Resolve pattern | DrSmugleaf
- **Add call site to arguments of resolve with the new .NET 6 arguments so it can log the file and line if a warning happens.**


##  Turn IPlayerSession into an entity | moony
- [Discord link](https://discord.com/channels/310555209753690112/900426319433728030/1015187820752683021)
- **Yes**
- This would let us modularize the entire thing and allow us to use events on players directly, letting us get rid of many player-indexed dicts in favor of storing it on the player
- Should this be done at an engine level, or at a content level?
- **Engine**
- **Keep player session, then have an entity field on the session for its data**
- **Mind would still be separate since player session is transient**
- **You can have multiple minds for the lifetime of a single player session**


##  Replace BUI state handling with normal component state handling for BUI prediction | ElectroSR
- [Discord link](https://discord.com/channels/310555209753690112/900426319433728030/1012164293816483870)
- Laggy interfaces suck
- Everyone is actively avoiding BUI atm
- **Prefer component states to BUI states**
- **Someone refactor BUI please**
- **Have the client manage the UI, the server needs to know if its open**


## Component references | PJB
- **Try to remove them**
- How do we have client-only or server-only data on a component without it
- Use different components for that data?


## Archetypes | DrSmugleaf
- B O N U S T O P I C
- Need to be made faster before we implement them outside of Robust.Benchmarks
- Do archetype chunking to optimize for CPU cache hits
- Check startup time specially for the JIT when creating all the archetypes
- [Flecs benchmarks](https://github.com/SanderMertens/ecs_benchmark)


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
- EL BODY SYSTEM | mirror
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
- Tutorial
    - In game
        - we have a pr open
- combat rework (needs to be bikeshedded)
    - https://github.com/space-wizards/space-station-14/issues/3378
- ghostrole/antag bans
    - unify ghost roles prototype (mind refactor)
- experimental science
    - "Science is still a piece of shit" - Vera 28/05/2022
    - "I haven't played the game in 2 years" - Vera 07/01/2023
- any% maintainer | Jezithyr
    - Stuck in canada
        - soon tm
- State mandated Xonotic matches | PJB
    - Please I have severe withdrawal symptoms
    - Replaced by private SS14 playtests
    - Woman down
- The game runs like shit how do people play this
    - still does | PJB 28/05/2022
        - "how do people play this game" (high pitched scream) | PJB 28/05/2022
    - Slightly better | PJB 11/06/2022
    - It's better but still not as good as I'd like it to be | PJB 25/06/2022
    - I haven't played the game since | PJB 16/07/2022
    - "Please read the last line of that subsection" | PJB 30/07/2022
    - "Please unread the last line of the previous subsection" | PJB 07/01/2023
- A trailer for Steam

Crashes / Critical bugs: (when are we moving these to GitHub)
- role timers not counting properly
  => till next time
