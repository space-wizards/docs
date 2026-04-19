# Maintainer Meeting (8 Jan 2022)
===
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 8 Jan 2022 16:00 UTC

**Attendees:**  
DrSmugleaf  
Vera  
metalgearsloth  
Paul  
ElectroSR  
PJB  
Visne  
ShadowCommander

# Automatic component names | wrexbe, metalgearsloth
- [Current PR link](https://github.com/space-wizards/RobustToolbox/pull/2389)
- Previous PR got some objections which got addressed.
- RenderingTreeComponent gets RenderingTree as name automatically

ok epin merge

# Reduce movement speed | metalgearsloth
- Current movement speed:
    - Walk = 4
    - Sprint = 7
- Reduce it to 5 for sprint?
- Change it in code 5 sounds good

# Comment and changelog typing conventions | ShadowCommander, metalgearsloth
- Capitalization
- Punctuation
- They are very inconsistent at the moment
- Code comment consistency does not matter
- Changelog consistency matters

# Improving CODEOWNERS | Vera
- Maintainers should actually codeown stuff they're in charge of.
- Make it so nobody gets notified for absolutely everything (like me and PJB currently-)
- Doing this should help with reviews!
- Maybe don't merge PRs if the codeowners haven't approved it?
- Current CODEOWNERS:
    - All: PJB, Vera
    - Localization files: Remie
- Change it to:
    - Atmos: Vera
    - Body system: Mirror and Smug
    - Clyde/ClydeAudio: PJB
    - Construction: Vera
    - Database: PJB and Smug
    - Integration tests: Smug
    - How about just everything except physics in engine: PJB <!-- thistbh -->
        - thistbhn't, I'd rather not have anyone receive notifs for everything :blobsweat:
    - Map renderer: Smug
    - Networking/prediction (not pvs): PJB/Acruid?
    - Pow3r: PJB
    - PVS: Paul
    - Resources: PJB
    - Physics: Sloth
    - Serialization: Paul and Smug
    - UI: PJB
    - YAML Linter: Paul and Smug

# Audio attribution | Paul
- Do we enforce it
- Paul says we figured out how to do out but I can't find where
    - audiofile.ogg -> audiofile.ogg.yml
- Which metadata should audiofiles have?
    - license identifier like rsis, copyrightstring

# Event naming | Paul
- Unified way to name them
- TWO EVENTS
- Equip attempt event has two viewpoints:
    - Equipee (GotEquipped?)
    - Equipment (IsBeingEquipped?)
    - talk in text chat to decide the funny
    - just @ Remie simple

# Port, protocol and IANA | PJB
- IANA is the list of "which applications use which ports"
- Port 5514 is free.
- Current status: `ss14://` is HTTP port 1212/tcp, `ss14s://` is HTTPS port 443/tcp
    - Problem: leaving out URI scheme can make address fail to work
        - Most people used to playing on game servers are probably *not* used to URI schemes in their server address.
    - Problem: 443 is HTTPS port. This means `ss14s://` servers need to put their stuff behind a subpath or subdomain, which is ugly. Or use a port I guess.
- Do we want an IANA port assignment?
    - Yes
    - Port: 5514
- Only HTTP for connections
- Drop the code for connecting over HTTPs
    - It makes the code simpler (Launcher, watchdog, hub)
    - Figure out a fallback path for the other servers

# Reverting policy for untested/unreviewed buggy PRs | ShadowCommander
- Should we revert them?
    - We did so for rich text
- Revert if server is broken and we can't fix it in one line code change (quickly)
- Objective: For a round to be playable, we can do it case by case.
- If we revert we can reopen the original pr

# YAML bloat prevention rules | Vera
- What to do about the many useless prototypes?
    - Do we clean them?
- Only allow YAML additions that would be immediately useful to mappers, admins or straight up obtainable in-game
    - New salvage wreck, new playable station, new chemical that can be mixed and has effects, new food item that can be cooked in-game or is obtainable in some other way, new fun badmin toy...
- Do we want to be a bit more strict with new machines having, for example, construct/deconstruct steps?
- every yaml addition should be either:
    - for admins
    - for mappers
    - obtainable
        - with cooking recipe & construction steps
- be more strict in general

# Full server snapshot/reload | PJB
- The workflow:
    - Press a button
    - Restart server
    - Enter server
    - Same state
- What's the current status
    - not good
- What can we do (conventions, best practices) to make this more doable
    - event serialization
    - new save format & logic: gamestatesave
        - saves all maps
        - entitysystem should get a way to read/write into that
- sidenote: this would be very beneficial for my persistence server fork plans

# Species | Paul
- This is going to take 30 minutes to talk through
- Do we allow them at roundstart?
    - Current stance:
        - Q. Will the main SS14 servers have round-start playable races other than humans?
        - A. No, but the functionality will be there for other servers. (Click spoiler to see the long answer to this question).
        - Thoughts (from PJB) are that it would be too much effort to make them interesting enough.
        - See [the FAQ for the full explanation](https://forum.spacestation14.io/index.php?/topic/48-information-faq/)
    - Is PJB a furry?
        - >looks at own avatar on discord
          - ![walterwhite.png](../assets/images/maintainer-meetings/2022-01-08/walterwhite.png)
- We support species.
- We support species at roundstart (when moony PRs it)
- Review species case by case, same as everything else.

# Roadmap
[Previous Roadmap](https://docs.spacestation14.io/en/maintainer-meetups/secret/2021-12-11-meetup)
AKA What do we want to move from playtest to early access

- emergency shuttle
    - auto shuttle movement
- gamemodes/antags
    - dynamic
        - mirror pls write the doc for it I will code it I swear on my life
        - nuke ops
            - the nuke is done, nuke ops isn't yet
            - does not work outside dynamic
        - lings?
        - blob?
            - vera loves blob
        - cult?
            - make it as good as vg for pjb
- EL BODY SYSTEM
    - some refactors were done by mirror, still some left
    - surgery died in the war of 1992
- Salvage
    - it is done
    - upstream moony asteroid/wreck generator for procgen salvage
    - https://www.youtube.com/watch?v=H0LPWuTt2o4
- Teleporters (Beam me up (Scotty))
    - telescience
    - its complicated we need to talk about it
- Singularity needs to ACTUALLY WORK
- body system but again
- body system (get smug to code it)
    - Species????
- __***ENGINE EDITOR***__
    - could benefit from full state reload
- Tutorial
    - In game guides
        - Yes
        - Or at least a link to the wiki ingame
            - Link it RN JESUS
        - Waiting on pretty labels
        - books/ebooks in pda
            - ebooks preloaded on pda for selected job
            - when rich text gets merged

# Bloons TD 6 | Vera, DrSmugleaf
- Bloons TD 6 gaming
    - this
