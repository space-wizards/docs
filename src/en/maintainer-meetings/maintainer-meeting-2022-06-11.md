# Maintainer Meeting (11 June 2022)
===
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 11 June 2022 18:00 UTC

**Attendees:**
- Electro
- Vera
- Remie
- Visne
- PJB
- Moony

## I'm stuck in Quebec for 5 more hours | DrSmugleaf
- I'm about to baguettify
- The destination is even worse (Spain)
- Smug gets a Canadian gf character arc (multiple maintainer meetings long, episode 2: Attack of the Quebecoise)
    - Jez isn't even awake to help me cope with the French please send help

Agreement:
- Quebec bad
- "Discord leave lasting damage" - smugleaf

## Click to wide attack was a mistake | Remie
- [link](https://discord.com/channels/310555209753690112/900426319433728030/980204271385604106)

Agreement:
- Mirrorcult on break, move it to next meeting


## Lobby songs take up half the game download what the fuck | All of us, enranged
- seriously??
- "enranged" means all of the maintainers are so distant from SS14
- 16 lobby songs... 40mb total. The resources folder is 133mb total.
- This is probably fucking terrible for git clone, etc

Agreement:
- Turn the PR icon red
- Should we do on-packaging compression?
    - Probably yes but how

## How do release packaging of assets | PJB monologues in the maintainer meeting
- Most engines work with raw high quality assets in repo, game finalized has compressed and lower qualtiy assets on publish.
    - Probably a terrible fit for our development: Git
    - Audio compression etc is gonna require dedicated heavy tools like ffmpeg and be slow
    - Doing audio compression live means results potentially inconsistent across publishes =
    - Too slow performance for ACZ, will require asset cache
        - Goes against current engine model where resources have 0 importing/caching/etc...
- Still a good choice we should do this:
    - Audio too large
    - RSI packing
    - more

Conclusion:
- Generate a good idea
- Audio files too heavy, put sources in separate repo. Main repo contains pre-downsampled assets.
- RSI packing etc is a good idea and should be fine.
    - Move packaging logic to C#, expose it to ACZ.
        - FINALLY. Also please put it in engine thanks.
- Probably still gonna need an asset processing cache either way, :salute:
    - SQLite it up
    - Please refrain from fucking this up this could go really bad.
    - No commitment only experiment for now

## Asset Manifests | PJB monologues in the maintainer meeting
- Manifest files (not for delta updates) client can load to pre-load all lengths of audio files etc
- Potentially very useful and avoids expensive loading
- May not be necessary
- Annoying on development builds
- Ick for ACZ again, see above.
- Reasons like async loading probably not good enough?
- Vera just got me activated so sloth could show up, how nice of her.

## Discord emote for all in-game plushies | Wrexbe
- uhhhh
- Only the good ones
- We already snivy what more do you need
    - Slime plushie
        - Slushie
        - PJB throws BASED ACCUSSATIONS of me being a slime girl... lawsuit ensues
        - SS14 in shambles

## Optional tile movement in SS14 | Vera
- Make mob movement modular
- How much effort
- We have to sucker in SS13 codebases
- How to implement?

Conclusion:
- Ship it, kind of half-ass it for SS14.
- Keep doing distance measurements for interactions, avoid
    - Simpler physics for it? Only hard vs non-hard, no "proper" shapes.
        - Have support for things such as windoors, etc.
            - This logic is not trivial at all, will require in-depth understanding of how SS13 works.
- Forks can improve it further if they want.
    - Perhaps upstream/merge good changes?
    - as long as it doesn't diverge the code too much??
- OpenDream needs more sophisticated implementation.
    - Needs separate visual/simulation transform
        - Wanted to pass this by sloth but rip
        - I talked about this with Acruid once
        - Gonna be kinks to work out
            - Probably have shared transform system func that gets render position, returns sim pos during sim.
- Sorry, Sloth. (Listen I tried to delay this topic until you showed up ;_;)

## No more new maps until better tools | Sloth
- [message there's a lot of details](https://discord.com/channels/310555209753690112/900426319433728030/980517246390644777)
- didn't we discuss this last meeting wtf
- drama

Conclusion:
- Even if we had better tools, more maps isn't a good idea
    - Still allow new maps but remove old ones.
        - Don't increase the total map count
- Make maps unique
    - Don't gimmick with a layout, gimmick with a story/theme
    - Maps should have unique assets where possible (Sprites, Objects, Jobs)
        - Yes this takes effort, git gud
            - Who knew that making a good game requires effort
- Port the fucking map that's like 6 spaceships amalgamated together.
    - I don't know what it's called (Ask in coderbus)

## Update server every commit again | Mirror
- [message](https://discord.com/channels/310555209753690112/900426319433728030/982571963316863038)
    - Damn 9 this tbh
- We have deltas + redial
- Moony mentioned still reduction in pop even through redial.

Conclusion:
- PJB has anxiety, this will kill her
- Just don't shy away from manual publish when :eyes:
- Keep as is

## can I get maintainer review of my design docs because you guys don't look at ideaguys | Mirror
- Well uhhhh

Conclusion
- She is not here...
- Sorry mirror
- Easiest maintainer meeting topic of my life

## RobustGenericAttribution Standard: yay or nay? | Vera
- https://github.com/space-wizards/RobustToolboxSpecifications/pull/3
- don't bikeshed the name
    - RobustGenericAttribution (Name Subject to chance)
        - it's the choice of steins;gate
            - based ref

Conclusion
- Good idea
    - Reviews left to be handled
- Not sure about the name!
    - Hehehehehe

## Matrix3 -> System.Numerics.Matrix3x2 | Electro
Conclusion:
- Probably wanna switch to System.Numerics in general
    - Even if it's not great for hot loop SIMD, it's still a bit of savings.
- Differences in API needs to be evaluated, massive breaking change.
    - Can we/should we use extension methods to help with this?
    - Misses stuff like my tuple cast so sad

## Early Access Roadmap
- emergency shuttle
    - auto shuttle movement
- gamemodes/antags
    - dynamic | mirror
        - ~~!!nuke ops | Paul~~
        - lings?
            - needs DNA
        - blob | Remie
        - cult?
            - make it as good as vg for pjb
        - revs | Vera
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
- Diagonal tiles | sloth
    - we have diagonal walls, tiles are harder
- __***ENGINE EDITOR***__ | PJB
    - could benefit from full state reload
- movement refactor
    - Client side movement?
        - a smidgen
            - as a treat
            - acruid pls com bak
    - TILE MOVEMENT
- Tutorial
    - In game guides
        - Yes
        - Waiting on pretty labels
        - books/ebooks in pda
            - ebooks preloaded on pda for selected job
            - when rich text gets merged
                - ![](https://cdn.discordapp.com/emojis/933790288860815380.webp =40x)
- oldchat + ui refactor | Jezithyr, DrSmugleaf
    - we did it
    - lost in the canadian wilds
- combat rework (needs to be bikeshedded)
    - https://github.com/space-wizards/space-station-14/issues/3378
- ghostrole bans | ShadowCommander
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
- State mandated Xonotic matches
    - Please I have severe withdrawal symptoms
    - Replaced by private SS14 playtests
    - Man down
- The game runs like shit how do people play this
    - still does | PJB 28/05/2022
        - "how do people play this game" (high pitched scream) | PJB 28/05/2022
    - Slightly better | PJB 11/06/2022

Crashes / Critical bugs: (when are we moving these to GitHub)
=> till next time
