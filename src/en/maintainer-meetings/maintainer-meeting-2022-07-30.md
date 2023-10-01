# Maintainer Meeting (30 July 2022)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 30 July 2022 18:00 UTC

**Attendees:**
- DrSmugleaf
- ShadowCommander
- ElectroSR
- Wrexbe
- moony
- PJB
- Visne

## Are we The Upstream or our own server | moony
- Will there be a separate repo
    - **No**
- Don't hold game design back because we're "upstream"
    - If a feature needs to be killed to make the game better, don't keep it because downstreams might want it
- Can we trust project managers with SSH:
    - Yes, assuming Silver doesn't object.
- Change server configs in the repo instead of Ansible.
    - Is this worse for downstreams
    - Downstreams can change it promptly in the config file
    - **Put all the default configs in the TOML config file so upstream changes don't change downstream**
- Do we make different CVars changeable by different permission groups? (Game admin, moderator)
    - **Yes**


## Remove game settings from server config | PJB
- We basically ended up discussing this in the previous point
- "Thank you for the bullet point" - Smugleaf


## Hud refactor ready for review | Jezithyr
- AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


## Early Access Roadmap
- gamemodes/antags
    - dynamic | mirror
        - lings?
            - needs DNA
        - blob | Remie
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
                - ![](https://cdn.discordapp.com/emojis/933790288860815380.webp =40x)
- oldchat + ui refactor READY FOR REVIEW | Jezithyr, DrSmugleaf
    - we did it
    - lost in the canadian wilds
    - found in the canadian wilds
- combat rework (needs to be bikeshedded)
    - https://github.com/space-wizards/space-station-14/issues/3378
- ghostrole/antag bans
    - unify ghost roles prototype
- Job playtime requirements | metalgearsloth, Veritius [c#9384](https://github.com/space-wizards/space-station-14/pull/9384)
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
- State mandated Xonotic matches | PJB
    - Please I have severe withdrawal symptoms
    - Replaced by private SS14 playtests
    - Man down
- The game runs like shit how do people play this
    - still does | PJB 28/05/2022
        - "how do people play this game" (high pitched scream) | PJB 28/05/2022
    - Slightly better | PJB 11/06/2022
    - It's better but still not as good as I'd like it to be | PJB 25/06/2022
    - I haven't played the game since | PJB 16/07/2022
    - "Please read the last line of that subsection" | PJB 30/07/2022
- A trailer for Steam

Crashes / Critical bugs: (when are we moving these to GitHub)
=> till next time
