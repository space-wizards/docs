# Maintainer Meeting (02 April 2022)
===
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 02 April 2022 18:00 UTC

**Attendees:**  
Smug  
Silver  
Shadow  
Paul  
moony  
Jezithyr  
ElectroSR  
PJB  
metalgearsloth

## Not pushing to master to make it easier for downstreams | moony
- Using PRs it's easier for downstreams to selectively pick what they want from upstream.
- This would mean making master (and stable if it happens) a protected branch so people can't push to it.
- [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- We already don't push features to master
- Should we push hotfixes/submodule updates to master?
    - We can commit hotfixes to master
        - I'm still PRing them
    - Push submodule updates directly if we can fix bots
- Current bots don't handle direct commits well, someone needs to fix/create a new bot that does


## Getting a CDN and setting up region serving | Silver
- Our resident Argentinian has been getting slow downloads.
    - complaints from argentinian resident are through the roof
- silver spinning up free aws instances with s3 and cloudfront with na, sa and eu, maybe au
    - we barely push 100gigs a month
        - we can use the free plan
        - if not, its not very expensive
- apparently we cant use S3, builds arent cached (nono)


## Migrating to a point-release model | moony
- To help avoid disrupting our active playerbase and help mitigate download times.
    - Delta downloads when.
    - Reconnecting automatically without going back to the launcher when.
    - background download
    - point release
- One update per day?
- Point release is the easiest to do fast
    - **Do it**
    - 10 am every day
- Delta downloads when PJB codes it


## Document and improve content/engine publish workflows and the watchdog | moony
- Open-source content and engine publish workflows.
- Server hosting is painful at the moment, has undocumented error messages.
- The system to publish builds like the main servers isn't public, you need to ask for the powershell scripts.
- **Improve the docs** and the tools god damn
    - Specially the watchdog (proper error output)


## Engine changelog | ike709
- Document engine changes so breaking changes are not a surprise.
- This has already been a problem multiple times for Opendream.
- also proper major/minor versions x.y -> major -> .z minor
    - X Major Y Minor?
- **GitHub action for changelog**, similar to how content does it
- Show the changelog somewhere


## Removing drag and drop interactions | moony
- Uncommon interaction and unintuitive for new players.
    - We can assign a keybind instead, like alt+click currently
- How do we do it for dragging others into disposals for example
- **We should write a design doc and decide how interactions work in general**


## Multi-Z | Vera
- How does one (sanely) do it
- what needs it
    - movement
    - atmos
    - explosions
    - rendering
- Special case maps
- needs more discussion.


## Improving dev UX for mappers, maintaining maps | moony
- We need to maintain our soon to be 7 playable maps and other salvage maps.
- Onboarding new mappers to help maintain them
- Automated map maintenance?
    - Migrations
        - Renaming, replacing and removing
        - With YAML
- Seeing pipes through walls / Being able to hide walls
    - filter/toggle by walls/floors/doors/windows/wire/pipe/tubes etc.
- Being able to see the color of floors
- Area copy and paste with preview
- Picker copy and paste (middle click to copy what's under your mouse)
- Improving mapping UI in general (spawn windows)
- Improving docking when mapping
- Teleporting to error messages
- Unreal engine retargets
- Placement ghost for salvage that shows where it will spawn, how big the maximum salvage size is
    - To know if the salvage will spawn inside the map


## Splitting UI code from simulation code, UI hot reloading and framework | Jezithyr
- **Split UI code from simulation code**
- **Splitting into a separate assembly to be decided**
- Apply this to rendering and user input as well.
- This can be done at the engine level without breaking downstreams (Opendream) while we transition SS14.
- Removing UI dependencies from sim makes it possible to run the game without an UI.
    - It also makes it possible to develop UI without getting cancer.
- Hot reloading UI
    - **Yes when you code it**
    - Visual editor?
        - **No, visual preview yes**
- Using a established UI framework?
    - [Avalonia](https://avaloniaui.net/)
    - [qmlnet](https://github.com/qmlnet/qmlnet)
    - **Not at the moment**


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
- body system (get smug to code it)
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
                - ![](https://cdn.discordapp.com/emojis/933790288860815380.webp =40x)
- oldchat + ui refactor | Jezithyr
    - we did it
- combat rework
    - hard to hit someone
    - wide attacks might be broken
        - prediction issue
- ghostrole bans | ShadowCommander
    - unify ghost roles prototype
- pulling refactor
- admin notes | DrSmugleaf
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
- change pvs to p/invoke zstd
    - compression too slow
    - we're using (Q's) C# library for zstd
- Prototype composition | Paul
- Server polls
- Round Statistics
    - Log votes, which maps are played the most…
- suit storage

Crashes / Critical bugs: (when are we moving these to GitHub)
- Round restart fails sometimes (may be a physics issue)
  => till next time
