# Maintainer Meeting (22 Jan 2022)
=
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

DrSmugleaf  
Vera  
Visne  
ShadowCommander  
PJB  
ElectroSR  
metalgearsloth  
moony  
Remie  
mirrorcult

# Do we promote bigger over smaller maps | metalgearsloth
- We have a bunch of tiny maps but no large ones
- Small maps get played regularly
- Should we save mapvote stats?
    - **Yes, also track votes against to not skew results.**
- **Don't promote bigger maps, just merge them on a case-by-case quality basis.**


# Moving BUI to content | metalgearsloth
- Is this something that would be reused by other games
    - **No**
- **Move it**


# Proxy methods for is entity terminating / deleted / queued for deletion | metalgearsloth
- **Yes**
- Proxy methods in EntityManager and EntitySystem.
    - Maybe have an interface to standardise these?


# Standardising EntityManager generic and non-generic methods | metalgearsloth
- Some use the array indexing and some don't so assume there's more of a speed difference now
- **Standardise them (on generics)**


# Discord role for musicians | metalgearsloth
- We have a pingable role for spriter already
- **Add the role**


# Not raising transform events during initialization | metalgearsloth
- Raising them leads to lifestage checks everywhere
- Ties into DetachParentToNull which would be nice to remove.
- **Sloth looks at it**
- Make events for transform initialize/shutdown?
    - Current one can only be subscribed to once.


# Ergonomics of async code vs do_after events | metalgearsloth, mirrorcult
- Solution: [single event do-afters](https://github.com/space-wizards/space-station-14/issues/6132)
    - Replace the two do after events with one DoAfterEndedEvent with the status on it, and a wrapper for custom data
    - Also could put cancel tokens into the do_after system
- Events are more painful than async code to write
    - So painful I would rather code in Unity
- It's a necessary evil for full map serialization
- If we don't use it, do we keep async in for forks?
    - **No**
- Async do_after made interaction worse internally | metalgearsloth
    - If you want to make your tool do after you have to make it all async
- We could serialize member methods with much difficulty, pass in the method to run into the do_after like verbs | Paul
    - Needs to be a member method, not a lambda or anonymous
- **Async might be serializable, when PJB codes it**
- **Use single event do after meanwhile**


# Removing component start/shutdown events | PJB
- Instead have the few components that actually respect startup/shutdown implement it themselves.
- **Remove and replace it**
- We don't know how much legacy code require the OnAdd/Initialize/Startup functions.
    - This won't be trivial.
    - Probably nothing uses the Running property, which we can remove.
    - The point is to **Remove Running**


# Protocol-require UDP and TCP port to be the same | PJB
- Extension from the port assignment topic
- What did PJB mean by this
- It is very complex otherwise
- Querying the server list would be easier
- **Require both ports be the same**


# Do we accept translation contributions | Paul
- Can the admins deal with non-english speaking people?
    - Servers would still be English only, server hosts could change the locale with us as the upstream being the pool of translations for everyone.
        - Paul how do we handle different servers having different content to be translated
        - **We will only accept common content between the two repositories**
        - Linter when
- Not purely game-translation, also launcher, website, etc.
    - Launcher: **Yes**
    - Website: **Yes**
    - Game: If you can run a client with a different locale to the server **yes**
        - **This requires the giant FText refactor**
- There are tools for this ([Discord link](https://discord.com/channels/310555209753690112/675078881425752124/931645419598000238))
- [Weblate](https://github.com/WeblateOrg/weblate/)


# Wallmounts on the floor in front of the wall vs on/in the wall | ShadowCommander
- Interactability is easier if they're in front | PJB
- **They will go on the wall because otherwise you can't place wallmounts facing to space**
- Wall lights are complicated
    - **Simply offset the point light**
- PJB implements occlusion and we win


# Text input popup design | ShadowCommander
- Should it be a BaseWindow/Eui or pop out of the control like the confirmation pop out for verbs like delete?
- Example: the set-transfer-amount verb should use it. Currently it creates a little popup
- **Multiline text: window**
- **Verbs (Rename, Transfers): input box, with sizes**
- **Commands: box if possible, window if too big**


# Why are integration tests slow | mirrorcult
- Because someone broke the ShouldPool method by changing the amount of default cvars on tests or smth
    - Be my guest if you want to find a better way to do it
    - Also tests are now broken if you enable pooling again
        - I'm not fixing it | DrSmugleaf
- Next :clap: topic :clap:
- also 40% of tests is just reloading prototypes (last I profiledTM)


# Archive Python rsi.py and rsi-editor | mirrorcult
- **Decision: keep rsi.py because python scripts are convenient, archive rsi-editor**
  Old repositories in Python:
- [RSI.py](https://github.com/space-wizards/RSI.py)
- [RSI-editor](https://github.com/space-wizards/RSI-editor)

New repositories in C#:
- [RSIEdit](https://github.com/space-wizards/RSIEdit)
- [RSI.NET](https://github.com/space-wizards/RSI.NET)


# Mapping and adding escape pods | mirrorcult
- We now have multi-grid saving/loading and docking serialization
- **Decision: code it, map it**
- Mapping docking is really annoying right now
- **Add a console command/mapping utility to make this easier, while the map is paused**


# Upstreaming ship vs ship combat as a gamemode | moony, mirrorcult
- When mirrorcult upstreams it
- **Sounds good to everyone**


# Early Access Roadmap
[Previous Roadmap](https://docs.spacestation14.io/en/maintainer-meetups/secret/2022-01-08-meetup)

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
            - Remie already coding it, but got lazy
        - cult?
            - make it as good as vg for pjb
        - revs
- EL BODY SYSTEM
    - some refactors were done by mirror, still some left
    - surgery died in the war of 1992
- Salvage
    - it is done
    - upstream moony asteroid/wreck generator for procgen salvage!!!!!!!!!
    - https://www.youtube.com/watch?v=H0LPWuTt2o4
- Singularity
    - radiation needs to work
- body system but again
- body system (get smug to code it)
    - Species
        - we need to do non human body parts
- __***ENGINE EDITOR***__
    - could benefit from full state reload
- Client side movement?
    - a smidgen
- Tutorial
    - In game guides
        - Yes
        - Waiting on pretty labels
        - books/ebooks in pda
            - ebooks preloaded on pda for selected job
            - when rich text gets merged
                - :death:

Bugs:
- copy the Subnautica bug reporter for players to report bugs
- automatically log grafana exceptions
- being able to see inside containers
    - Need to change PVS to not send all container contents
    - Isn't this a separate issue anyway
        - Seems like PVS queue bugs?
        - Imagine if players could give steps to replicate, insanium
- hud disappearing
