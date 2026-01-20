# Maintainer Meeting (16 April 2022)
===
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 16 April 2022 18:00 UTC

**Attendees:**  
Acruid  
metalgearsloth  
DrSmugleaf  
moony  
Vera  
ShadowCommander  
Visne  
Paul  
ElectroSR  
PJB

## We hit 250 players in one server. What's next? | moony
- What is our goal for optimizations
    - What can we do better
    - What should we do now that the game is very performant
- Is this when we finally code content
- We need to fix stuttering, pvs pop-in, rubberband issues and make network smoothing default to 2 | mirrorcult
- **Server side performance is fine, need to fix client side performance and bugs**


## Diagonal tiles | metalgearsloth
- The engine technology is there
- What do about anchoring and stuff on content
- Atmos will just treat them as space, still have diagonal walls be airtight
- **Needs to be fleshed out more**


## Make VV read/write by default | mirrorcult
- Everyone forgets to make properties read/write
- We still have to refactor VV for ECS
- **Make all VV properties writable if you have +HOST**
- **The default should be read**
- **Attribute to make all properties on a class VV**


## Review and PR guidelines | mirrorcult
- https://docs.spacestation14.io/en/maintainer-info/review-guidelines
- https://docs.spacestation14.io/en/getting-started/pr-guideline
- **We are missing file name conventions on the conventions page**
- **We need better automated tooling**


## Early Access Roadmap
[Previous Roadmap](https://docs.spacestation14.io/en/maintainer-meetups/secret/2022-01-22-meetup)

- emergency shuttle
    - auto shuttle movement
- gamemodes/antags
    - dynamic | mirror
        - nuke ops
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
- Radiation refactor
- body system but again
- body system
- Grid splitting
    - finish when sloth comes out as a furry
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
- Tutorial
    - In game guides
        - Yes
        - Waiting on pretty labels
        - books/ebooks in pda
            - ebooks preloaded on pda for selected job
            - when rich text gets merged
- oldchat + ui refactor | Jezithyr
    - we did it
- combat rework
- ghostrole bans | ShadowCommander
    - unify ghost roles prototype
- pulling refactor | bobda
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
- Server polls
- Round Statistics
    - Log votes, which maps are played the most…

Crashes / Critical bugs: (when are we moving these to GitHub)
=> till next time
