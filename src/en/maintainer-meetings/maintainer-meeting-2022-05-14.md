# Maintainer Meeting (14 May 2022)
===
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 14 May 2022 18:00 UTC

**Attendees:**  
DrSmugleaf  
Remie  
Visne  
moony  
ShadowCommander  
PJB  
ElectroSR  
mirrorcult

## Launcher server announcements | moony
- The launcher listens to an RSS feed if you opt-in **per server (or server group)**.
    - Works for any server that has such a feed setup.
    - **It can be transient (truncated)**
- For both automated and manual announcements.
    - **Can be categorized.**
- Can announce a new round starting, or mandatory server restarts.
- Separate restart notifications from other notifications?
    - **Needs high poll rate**
    - **Don't have a websocket per server**
    - **Run a news aggregator as part of the hub?**
        - What happens to servers off the hub?
    - Just keep it simple no websocket stuff for now just RSS all the way baby.
    - **Push notifications for restarts**
- **Hook up changelog to RSS updates**


## Automerging PRs when approved and CI passes | metalgearsloth
- Refined GitHub supports this but it doesn't work properly.
- Allegedly exists in GitHub by default but the button doesn't exist.
    - You can only enable it if you enable only being able to merge PRs when CI passes
        - Simply disable push to master --moony
- What if the servers DIDN'T autoupdate to broken builds??
    - check em before we wreck em
- **Use a bot (when you code it)**
    - **We can use the `workflow_run` workflow event to do this.**


## getFlatIcon() AKA handling capture of appearance data (photography, scoreboard, Remie bait) | PJB
- No BYOND-like server CPU rendering
- Send the visual information to the client (appearance components)
    - Move complex stuff like item rendering on mobs to be 100% visualizer data
- Just take a screenshot on the client? (photography) (Remie vindicated)
    - Easy to do
- How do we render multi-entity entities?
    - e.g. eris walls
    - **follow child entities and collect em all?**
- **Replace appearance visualizers with entity systems**
    - Already agreed on this in another meeting
    - Use component states to send the data?


## ABI vs API backwards compatibility on engine | PJB
- ABI: code keeps working dynamic linking against newer versions of the engine
- API: code keeps working if you recompile against newer versions of the engine
- **ABI stability**
- There might be GitHub analyzers to check this
    - May or may not be worth setting up
- **Aim for ABI, when you have to break it, increase major version**
```cs
// What you have:
void Foo(int x) => ...

// What you want:
void Foo(int x, int y = 0) => ...

// What you need to do to preserve ABI compat:
void Foo(int x) => Foo(x, 0); //method NOT removed
void Foo(int x, int y) => ...
```


## Private playtest/actual QA sessions | mirrorcult
- Making the maintainers, senior contributors and game admins play their game
- (Suspicion on Space Station)
- Whitelisted server on EUW2 or USW?
    - Maybe USW for the Australians.
    - **Put another server instance on USW ez clap**
- Schedule
    - **After the maintainer meeting (afterparty)**
- **The whitelist needs to be per server**


## Auto-ignore unknown components on the client and remove client IgnoredComponents | mirrorcult
Cases:
- server side component spelled correctly--ignored by client, no error on server
- server side component spelled incorrectly--ignored by client, server errors
- client side component spelled correctly--no error on client, server needs it in the ignore list
- client side component spelled incorrectly--ignored by client, server errors since it's no longer in the ignore list
- shared component spelled correctly--no error on client, no error on server
- shared component spelled incorrectly--ignored by client, server errors
- **Fund it**


## Early Access Roadmap
- emergency shuttle
    - auto shuttle movement
- gamemodes/antags
    - dynamic | mirror
        - nuke ops | Paul
            - the nuke is done
            - does not work outside dynamic
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
- Salvage proc gen | moony
    - [Cargo Commander](https://www.youtube.com/watch?v=H0LPWuTt2o4)
    - **Coded on outer-rim, just needs porting to upstream**
        - moony's entirely rewriting it anyways so don't do that
- body system but again
- body system
- Grid merging
- Diagonal tiles | sloth
    - we have diagonal walls, tiles are harder
- __***ENGINE EDITOR***__ | PJB
    - could benefit from full state reload
- movement refactor
    - Client side movement?
        - a smidgen
            - as a treat
            - acruid pls com bak
- Tutorial
    - In game guides
        - Yes
        - Waiting on pretty labels
        - books/ebooks in pda
            - ebooks preloaded on pda for selected job
            - when rich text gets merged
- oldchat + ui refactor | Jezithyr, DrSmugleaf
    - we did it
- combat rework (needs to be bikeshedded)
    - https://github.com/space-wizards/space-station-14/issues/3378
- ghostrole bans | ShadowCommander
    - unify ghost roles prototype
- Admin traitor/role menu
    - Assign people roles
    - Objectives UI
- Job playtime requirements
    - Playtime tracking
    - Per role playtime tracking
- experimental science
    - artifacts??!?!?
- action ui refactor, [like ss13 maybe](https://i.ytimg.com/vi/iFf_T31C-iU/maxresdefault.jpg) | Jezithyr
- any% maintainer | Jezithyr
- Prototype composition | Paul
    - https://github.com/space-wizards/RobustToolbox/pull/2678
    - https://github.com/space-wizards/space-station-14/pull/7403
- Server polls
- Round Statistics
    - Log votes, which maps are played the most…
- State mandated Xonotic matches
    - Please I have severe withdrawal symptoms
    - Replaced by private SS14 playtests
    - Man down
- The game runs like shit how do people play this

Crashes / Critical bugs: (when are we moving these to GitHub)
=> till next time
