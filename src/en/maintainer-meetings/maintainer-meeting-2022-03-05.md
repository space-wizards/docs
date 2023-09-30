# Maintainer Meeting (5 March 2022)
===
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 5 March 2022 16:00 UTC

**Attendees:**  
Paul  
PJB  
ShadowCommander  
ElectroSr  
moony  
Silver

## should we stop storing entity uids inside entity systems to denote entities to update in favor of special components for this? | Vera
for example: basically instead of this field on a system
```csharp
HashSet<EntityUid> ActiveWelders
```
You'd just assign the `ActiveWelderComponent` and use an EntityQuery
- ye this is probably a good idea, but we'd have to take effort to make it efficiently.
- make binary components efficient

## Deprecate EntitySystem.Get | Vera
it's a shitty static method that does an IoCManager resolve and its misused everywhere
- sgtm

## benchmark metrics | paul
already decided on, just announcing: action piping data into db, grafana reading db
- YES
- gh actions will produce inconsistent results
- where to run benchmarks

## docfx | paul
bugging pj or vera to set it up
- silver will do it

## Soundsystem API revamp | Mirror
the current api leads to easy errors which cause sounds to be played globally, not uid-specific
example: https://github.com/space-wizards/space-station-14/pull/6982/files
- remove overloads

## Rename Server Role Ban to Role Ban | ShadowCommander
sgtm

## Early Access Roadmap
[Previous Roadmap](https://docs.spacestation14.io/en/maintainer-meetups/secret/2022-01-22-meetup)

- emergency shuttle
    - auto shuttle movement
- gamemodes/antags
    - dynamic | mirror
        - nuke ops
            - the nuke is done, nuke ops isn't yet
            - does not work outside dynamic
        - lings?
        - blob | Remie
        - cult?
            - make it as good as vg for pjb
        - revs
- EL BODY SYSTEM | mirror
    - some refactors were done by mirror, still some left
    - surgery died in the war of 1992
- Salvage proc gen | moony
    - [Cargo Commander](https://www.youtube.com/watch?v=H0LPWuTt2o4)
- Radiation refactor
    - Singularity rebalance
- body system but again
- body system (get smug to code it)
    - Species
        - we need to do non human body parts
- __***ENGINE EDITOR***__
    - could benefit from full state reload
- movement refactor
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
- oldchat + ui refactor
- explosion refactor | electrosr
- combat refactor
- ghostrole bans
- pulling refactor
- admin notes | drsmugleaf
- Admin traitor/role menu
    - Assign people roles
- Job playtime requirements
    - Playtime tracking
    - Per role playtime tracking
- experimental science
- action ui refactor, [like ss13 maybe](https://i.ytimg.com/vi/iFf_T31C-iU/maxresdefault.jpg)
- change pvs to p/invoke zstd
- Prototype composition | Paul
- Map poll at round end
- Round Statistics
    - Log votes, which maps are played the most…

Crashes / Critical bugs: (when are we moving these to GitHub)
- grid disappears on reconnect
  => till next time
