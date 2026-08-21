# Maintainer Meeting (30 April 2022)
===
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 30 April 2022 18:00 UTC

**Attendees:**  
Vera  
Silver  
ShadowCommander  
PJB  
Sloth  
moony  
mirrorcult  
Acruid  
DrSmugleaf

## Removing RobustUnitTest or RobustServerSim | metalgearsloth
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/966291335785095239)
- Actual unit tests shouldn't be inheriting, everything else should be an integration test
- If prototype loading was faster we could remove both
- Is Acruid in the meeting

Answer:
- We have like four ways to start engine and run tests.
- We have NO CLUE what each of these do, we should probably gather some info and list it out so we can make a more informed decision?
- Come back to this after we actually know what each does
- Acruid came:
    - Server simulation can spawn entities
    - It's the bare minimum required for that, any extras such as prototypes, components and systems need to be added automatically.


## Long term map maintenance tools | moony
![entitychange.png](../assets/images/maintainer-meetings/2022-04-30/entitychange.png)
- Fixing the mapping merge driver
    - Rewrite it atop the testing framework?
- Automated YAML and entity migrations

Answer:
- when someone codes it
- BYOND is better than us
    - BYOND's map editor asks you for new paths (like entity prototype IDs) for missing things
    - tbh this goes for a lot of things about mapping rn
- Entity UID consistency system on map is broken right now, needs fixing
    - 1 entity getting changed -> ![entitychange.png](../assets/images/maintainer-meetings/2022-04-30/entitychange.png) ungabunga change go brr SO TRUE BESTEI
- Migrations are like scripts more than like prototypes. Does it make sense to keep them in the prototypes folder?
    - For complex C# based ones it'd be necessary for them to remain compiled in?

## Write down the main purpose of each interaction hotkey | ShadowCommander
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/966591327494086706)
- For contributors to decide on which hotkey to use when implementing a feature.
- Remove overlap between left click/E | PJB


Answer:
- Tooltip show alt uses
    - Somewhat unusual for 2D games?
        - Starbound apparently has it though
    - Show icons and
- Remove overlap between left click/E. Force people to learn E
    - Give indication that you can use E to click on the thing. Otherwise people will not realize it exists.
        - Candidate: https://youtu.be/d6GtGbI-now keyboard spritesheet
            - Has no Cyrillic support
                - Can add ourselves
        - Other links:
            - https://thoseawesomeguys.com/prompts/
            - https://www.gameuidatabase.com/index.php?&scrn=907
            - https://kenney.nl/assets/input-prompts-pixel-16
- Forced Tutorial™ to teach interactions
- Show the thing you're looking at too, optionally.

### Hotkeys:
- Use(Left click)
    - Interaction involving hands
- ActivateItemInWorld(E)
    - Open UI
        - If there's a secondary activate, then put that in the UI
- AltActivateItemInWorld(Alt)
    - Specify which interaction it should run instead of automatically picking the first verb
- ActivateItemInHand(Z)


## Guidelines for balance discussions and code of conduct | moony
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/966843069515329586)
- Emag nerf (18291 comments)

Results
- GitHub discussions usually get bad.
- They spam the #github channel reee.
- Should we move those discussions to somewhere else?
    - The official forums aren't great for that.
    - Discord threads are an option, but they're not great for week-long discussions.
        - discord community server forums someday
        - Some people don't want to join the Discord for these discussions, they might be put off by that.
    - Moderate GitHub better?
    - Use GitHub discussions? (Although they suck)


## Planet maps, should maps be able to be grids | Vera
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/966984856863113217)
- It would allow for tiles to be placed anywhere (needs refactors)
- This would be sane opt-in default grids
- Allows for planet maps if changes are made to:
    - Parallax
    - Default atmos empty tile behavior (being worked on)
    - Adding a component for a map to handle gravity.
- Probably useful for other games, including OpenDream.

Results
- When sloth codes it
- We are supposed to be able to have maps as grids already but it's broken
- Allows for global grids from Byond
- Causes some crashes if you mix map and grid component


## Deprecate GridId and MapId in favor of EntityUid | Vera
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/966986023689129994)

Results:
- YES
- Ask Acruid, he has *a plan* :focus:


## Maps submodule | moony
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/967544877506236437)
- Keep only 4-5 core maps in the main repo
- Lets us introduce new maps without assuming that they will be in forever
- We can give mappers like Emisse write access to the repo
- Allows easier rotation of maps and possibly encouraging people to try out bolder things with map design

Results:
- Every submodule makes it harder for new people
- Requires keeping the main/map repo in sync with changes
    - If an item is changed then the maps need to be changed
- If someone needs map write access give them write access to content
- **No submodule for maps**


## Icon for the launcher | mirrorcult
- [Discord message and thread](https://discord.com/channels/310555209753690112/900426319433728030/967667307142860800)
- Probably needs to be different than the SS14 one
- PJB had a think in the thread above

Results:
- Maybe do it similar to the auth website
  https://central.spacestation14.io/web/
    - How does this fit into the icon in the task bar
        - Who knows
- When someone inkscapes it
- When one of us uses the Patreon money for it?
- Can be a modified SS14 logo
- YES BUT WE DO NOT KNOW THE DESIGN


## Making fake lag the default in local development | metalgearsloth
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/967779103023460352)
- Helps spot prediction issues
- Makes people other than just senior contributors consider it
- Prevents the game feeling like shit to play with high ping
- We can LARP as Australians or Argentinians during local development

Results:
- Yes
- Make it 150ms
    - With 20ms randomness, but the client might not handle it well yet
    - 0.01% packet loss
- We need to be able to diff component states


## Quickstart script for repo setup | moony
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/967988264818577488)
- Also attempts to open the repo in your IDE of choice
- Probably a Python script targeting only Windows users to allow people that have no interest in fully developing the game (mappers and spriters) to get the game up and running.

Results:
- Make a script to build without Visual Studio (Saves a few GB of disk space and RAM for mappers)
    - Script needs .NET 6
    - msbuild
- We need a tutorial on how to clone and build the project from command line for mappers
    - We can provide a script for this, to have an up-to-date build to map with


## Species/roles whitelist | metalgearsloth
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/968123789768552468)
- Would we ever actually have it on an official server
    - (no) | moony
- Generalize whitelists so it's easy to add new ones | moony
    - Specify in YAML which whitelist to use

Results:
- Implement it
- Generalize whitelists
- We won't have it on an official LRP server


## Issue templates and enforcing good issue writing | moony
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/968126891926122547)

Results:
- We need an issue template on engine
- Improve the content issue template
- Figure out a better template
    - Description:
    - Reproduction:
    - Screenshots:


## The identity / entity LOC problem | mirrorcult
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/968642553228460052)
- What did mirror mean by this
- Need to separate metadata name and display name

Results:
- Don't have it in engine, add a layer in content that gets used
- We can have an analyzer for people to not use EntitySystem.Name(EntityUid) where necessary


## What's necessary for MRP | moony
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/968872376370622495)
- [GitHub issue](https://github.com/space-wizards/space-station-14/issues/7809)

Results:
- BE ABLE TO CHANGE THE RULES


## What do we want out of in-game species | moony
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/969305610657087499)
- SS14 has made it a lot easier to add and maintain new playable species
    - The biggest hurdle is sprites, but humanoid ones are fine
- What should we do when for example someone wants to add a sentient cloud of bees:
    - What's acceptable for a round-start species?
    - What's acceptable for a mid-round species? (Events, something you can turn yourself into with enough work)
    - Situational/event species (skeletons on roundstart on Halloween)

Results:
- **Round start:** have them be sufficiently different that you play different than a human
    - The goal is to make it different enough that LRP players play them differently.
    - Slimes should be made more interesting
    - Lizards aren't there
        - Make them cold-blooded
        - More carnivorous
    - Dwarves are a debug species, can be removed
    - Vox are good but effort
        - ok tbh vox would probably still need a bit more mechanically to set them apart imo
    - Can it be too different? (Plasmemes)
        - Pain in the ass
        - If the rest of the game needs to be designed around it (the map has to change) it is too different
- **Mid-round:** SKELETONS, needs to be unique, well-designed, the bar is lower than for round-start
- **Situational/event species:** Lower bar than mid-round, needs to be funny
    - Needs a way to prevent round start species after event


- Literally this entire answer has been "it has to be interesting" smh.

## Should we implement map standard tests | moony
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/969630546550489119)
- Examples:
- Enforcing a maximum light budget within an area.
- Making sure each job in the job list has a spawnpoint.
- Forbidding certain objects from being placed in a map (i.e. finally making sure nobody maps the cursed locker for a laugh)
- Ensuring that no spawnpoints will instantly kill you.
- Potentially abusing the pathfinder a bit to check that it's possible for each job to make it to their spawnpoint from arrivals? This might help avert "whoops you can't exit arrivals/your office" bugs. But I think the pathfinder's ability to understand access isn't functional atm.
- Duplicate structures (pipes, wires, and full-tile structures having more than one of themself on the same tile)
- Power continuity tests (mapper places test points and can either check in-game or have a test yell if there's a break)

Results:
- We need a better way to review maps.
    - Overlay to see wires and what's powered at round-start.
    - Access overlay for doors, green for accessible red for not, able to be used as a ghost to audit access
        - Or list access levels above doors
        - Easy way to change access level for this so you don't need to go back to the lobby
- Yes:
    - Enforcing a maximum light budget within an area.
    - Making sure each job in the job list has a spawnpoint.
    - Forbidding certain objects from being placed in a map (i.e. finally making sure nobody maps the cursed locker for a laugh)
        - Don't error, warning for relevant things
    - Duplicate structures (pipes, wires, and full-tile structures having more than one of themself on the same tile)
    - Seeing how fast power runs out on a map
    - Power continuity tests (mapper places test points and can either check in-game or have a test yell if there's a break)
        - Makes sure there are no breaks in power lines
- No:
    - Ensuring that no spawnpoints will instantly kill you.
        - Not automatic, we need to go through spawn points for quality control anyway
        - The arrivals shuttle fixes this.
        - Draw spawn points over everything
    - Potentially abusing the pathfinder a bit to check that it's possible for each job to make it to their spawnpoint from arrivals? This might help avert "whoops you can't exit arrivals/your office" bugs. But I think the pathfinder's ability to understand access isn't functional atm.
        - For access
        - Do it in manual review instead

- When you code

## Map quality control | PJB
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/969677010668507176)
- PJB says a bunch are bad
    - tremble
    - PJB ASMR (patreon exclusive)

Results:
- Don't rely on there not being player collisions when mapping
- Porting 1:1 is fine on some maps (Delta) not on others (Atlas)
- Common problems:
    - All staff halls were a mess, didn't have visibility into the department or no desks, almost all the offices had a bedroom crammed into the office (waste of space, we don't have enough for that on most maps).
    - Medbay lobby (except Pillar, where it was fine)
    - Too many lights (Pillar and Bagel specially)
- Make sure there are enough disposal chutes


## Do we keep asking question on maintainer meeting that end in "WYCI" | PJB
Results:
- Yes, when there's valuable input to be had, even if the result is WYCI we need to figure out if everyone wants it or if there are any downsides


## Early Access Roadmap
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
- oldchat + ui refactor | Jezithyr
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
    - https://github.com/space-wizards/space-station-14/pull/7403
- Server polls
- Round Statistics
    - Log votes, which maps are played the most…
- State mandated Xonotic matches
    - Please I have severe withdrawal symptoms

Crashes / Critical bugs: (when are we moving these to GitHub)
=> till next time
