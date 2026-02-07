# Maintainer Meeting (25 June 2022)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 25 June 2022 18:00 UTC

**Attendees:**
- DrSmugleaf
- PJB
- Wrexbe
- ElectroSR
- Vera
- metalgearsloth (just got nitro)
- Shadowcommander (late)

## Making wide attack click-based was a mistake | Remie
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/980204271385604106)
- Too much friendly fire with Kudzu
    - **Kudzu needs to be fixed separately**
- Most weapons shouldn't have broad-angle wide attacks
    - **Spears should have spear-like attacks**
- Make it toggleable to let the user decide?
    - Need to pick a sane default
    - **Experiment with making it a hold attack, when you release left-mouse button**
    - Windup?
        - **Experiment with it too**


## Disbanding scheduled playtests for now | moony
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/986359940400680980)
- Letting in a select amount of users at a time
- High pop has design and game administration problems
- We set the cap to 65 recently (raised to 130 during playtests)
- Some SS13 servers have such high pop counts
- **We need high pop maps for this**
- **They are important to get players invested and check out new things**
- Turn them into proper feature tests?
    - No because features will be broken and it will look bad
- **Decision: Change playtests to be at the same time as progress reports**


## Tile damage kinds | moony
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/986384961718353951)
- RobustToolbox's tiles are too limited and don't have enough space
- Do we make a SS14-specific wrapper around tiles?
- Tile controllers?
    - **A separate system from normal ECS is not convenient**
- Make them use normal components and ECS?
    - **We need to make our ECS not shit and implement transformless entities**


## ECS refactor | Jezithyr
- Two-layer ECS, archetypical for perf and sparse for entity glut, similar to the concept of worlds in some ECS
- In archetypical ECS, the problem is that adding more components to an entity at runtime is slow
    - **We do this sometimes**
    - Iterating and filtering entities is very fast
- With worlds we can have replays with their own world and entities
    - Multithreading
- C# binds for FLECS exist
    - **Decision: Experiment with it**
- Rewrite our own ECS with the important parts in C# instead?
    - NIH my beloved
    - Less performance overhead with marshalling
    - More work to maintain
- Do we need to cut down on remo
- Flecs fixed my marriage
    - Me irl
    - Good for containers with child entities
- Is this the next engine rewrite
- Back to Godot
- Try to not cause an API breakage
- A - Vera


## Right-click for both entity menu and verb menu on entities is unintuitive | mirrorcult
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/988966819018707004)
- It's unintuitive because you have to right click twice
- There's no indication it's possible to open the verb menu
- How do we solve this
    - **Decision: Trigger on hover**
    - Properly handle moving diagonally onto submenu (don't make the submenu close instantly on hover leave)


## Expanding who can merge PRs | moony
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/988983179262189639)
- Junior maints / trusted reviewers?
- We need more people to get content PRs through
- Expanding triage perms?
- **Need more people to review**
- **Decision: Make review guidelines**
    - Add big/breaking code changes to the codebase changes channel


## Protect master branch | mirrorcult
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/989048858216636446)
- We are getting 500 PRs a month anyway help
- We need it to make downstreams have an easier time merging changes
- Prevents cringe pushes to master
- Too many commands to update the submodule
    - **Solution: make a script, you can make PRs from the CLI too**
- **Decision: protect master branch**


## Early Access Roadmap
- emergency shuttle | sloth
    - auto shuttle movement
- gamemodes/antags
    - dynamic | mirror
        - ~~!!nuke ops | Paul~~
        - lings?
            - needs DNA
        - blob | Remie
        - cult?
            - make it as good as vg for pjb
        - revs
            - we want a generic antag overlay system
            - loyalty implant
            - faction system
- EL BODY SYSTEM | mirror
    - some refactors were done by mirror, still some left
    - surgery died in the war of 1992
        - Mirror died in the war of 1993
    - limb damage.....
- Salvage proc gen | moony
    - [Cargo Commander](https://www.youtube.com/watch?v=H0LPWuTt2o4)
    - **Coded on outer-rim, just needs porting to upstream**
        - moony's entirely rewriting it anyways so **don't do that**
- body system but again
- body system
- Grid merging
- Diagonal tiles
    - we have diagonal walls, tiles are harder
- __***ENGINE EDITOR***__ | PJB
    - could benefit from full state reload
- movement refactor
    - Client side movement?
        - a smidgen
            - as a treat
            - acruid pls com bak
    - TILE MOVEMENT [c#5551](https://github.com/space-wizards/space-station-14/issues/5551)
- Tutorial
    - In game guides
        - Yes
        - Waiting on pretty labels
        - books/ebooks in pda
            - ebooks preloaded on pda for selected job
            - when rich text gets merged
- oldchat + ui refactor | Jezithyr, DrSmugleaf
    - we did it
    - lost in the canadian wilds
- combat rework (needs to be bikeshedded)
    - https://github.com/space-wizards/space-station-14/issues/3378
- ghostrole bans
    - unify ghost roles prototype
- Admin traitor/role menu
    - Assign people roles
    - Objectives UI
- Job playtime requirements | Veritius
    - Playtime tracking
    - Per role playtime tracking
- experimental science
    - artifacts??!?!?
    - "Science is still a piece of shit" - Vera 28/05/2022
- action ui refactor, [like ss13 maybe](https://i.ytimg.com/vi/iFf_T31C-iU/maxresdefault.jpg) | Jezithyr
    - stuck in canada
- any% maintainer | Jezithyr
    - Stuck in canada
        - soon tm
- Prototype composition | Paul
    - https://github.com/space-wizards/RobustToolbox/pull/2678
    - https://github.com/space-wizards/space-station-14/pull/7403
    - paul still not done with his thesis
- Server polls
- Round Statistics
    - Log votes, which maps are played the most…
- State mandated Xonotic matches | PJB
    - Please I have severe withdrawal symptoms
    - Replaced by private SS14 playtests
    - Man down
- The game runs like shit how do people play this
    - still does | PJB 28/05/2022
        - "how do people play this game" (high pitched scream) | PJB 28/05/2022
    - Slightly better | PJB 11/06/2022
    - It's better but still not as good as I'd like it to be | PJB 25/06/2022

Crashes / Critical bugs: (when are we moving these to GitHub)
      => till next time
