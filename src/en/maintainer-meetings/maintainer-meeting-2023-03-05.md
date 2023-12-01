# Maintainer Meeting (5 March 2023)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

> **Time:** 5 March 2023 19:00 UTC
>
> **Attendees:**
> - Wrexbe
> - Jezithyr
> - Visne
> - ElectroSR
> - PJB
> - DrSmugleaf
> - Paul
> - moony
> - keronshb

## Re-enabling GitHub discussions | PJB
- Open them up to ideaguysing?
- We originally closed them because bot doesn't track them
- We disabled it because MoMMI doesn't post GitHub discussions in the github channel
    - **If we agree that it's good PJB codes it**
- Verdict: **Yes**

## YAML Prototype Editor | DrSmugleaf
- In-game or out-of-game
    - If it's in-game it doesn't need to be downloaded separately but it can't be used if the branch doesn't build (can be solved by not using latest)
    - Out of game means having to use avalonia :death:
    - In-game means having to use robust's UI :death:
    - In-game means it could live reload, and show it
    - If the editor was good enough, we could store the data in a better format for machines
- Could be used by admins when uploading prototypes?
- Exporting to Resources/Prototypes when in local development
- Being able to view prototypes that have been uploaded through uploadfile in an UI? imagine
- **Don't do it out of game with Avalonia**
- **Do it in-game and maybe later move it to be inside a RobustToolbox editor**


## What to do about delta comp states | metalgearsloth
- Make comps track it themselves? https://discord.com/channels/310555209753690112/310555209753690112/1080275438913470564
- Just use smaller components? (in the above case per-chunk ents but then that likely requires pvssystem changes and maybe archetypes)
- Pre-empting "do we need this" fixtures were split out from physics as grid movement was making the game unplayable for slow connections
- **Look into supporting chunk entities**
    - **For bounds, chunks are multiples of 4 so it's not a problem** (i regard to chunk entities sitting at the corner of chunks)
- **Archetypes when**
- hampter, buncake


## Turning off settings requiring reviews to be approved | metalgearsloth
- It's just a placebo
- You can just dismiss it anyway. It doesn't need to remind me comments exist.
- I have already vibechecked the pr by that point even if I wasn't the reviewer.
- About as useful as protecting engine master
- Assuming it takes 5-10 seconds per PR this wastes 40+minutes a month
- Take a survey of active maints or smth idklol
- **Just use Bors you don't need to dismiss the reviews and Bors will fail if you merge something while it's working**
    - **Ok don't do it yet until we fix the changelog bot**


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
- EL BODY SYSTEM | jez ![](https://cdn.discordapp.com/emojis/933790288860815380.webp =40x)
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
- State mandated Xonotic matches | PJB
    - Please I have severe withdrawal symptoms
    - Replaced by private SS14 playtests
    - Woman down
    - She added Miku to her server (real) now you can play as miku pls play with her
    - Implement Xonotic as a plugin to ss14
- The game runs like shit how do people play this
    - still does | PJB 28/05/2022
    - people like shitty games
        - "how do people play this game" (high pitched scream) | PJB 28/05/2022
        - ex: SCREEEEEEEEE
    - Slightly better | PJB 11/06/2022
    - It's better but still not as good as I'd like it to be | PJB 25/06/2022
    - I haven't played the game since | PJB 16/07/2022
    - "Please read the last line of that subsection" | PJB 30/07/2022
    - "Please unread the last line of the previous subsection" | PJB 07/01/2023
    - "I spent the last two weeks coding Rain World" | PJB 21/01/2023
    - "I should've tried to run it from the AirBNB that I was staying over in my skiing trip but I didn't" | PJB 11/02/2023
    - "It still runs like shit" | PJB 05/03/2023
- A trailer for Steam
    - Liltenhead made one

Crashes / Critical bugs: (when are we moving these to GitHub)
- role timers not counting properly (pjb added a thing to check if its a db issue) (epico)
    - the web ui just chops off after 24 hours haha
      => till next time
      like and subscribe
      smash that button
      did you know only 6% of contribs join this meeting?
