# Maintainer Meeting (19 March 2022)
===
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 19 March 2022 16:00 UTC

**Attendees:**  
DrSmugleaf  
ShadowCommander  
ElectroJR  
Remie  
Moony  
Silver  
Mirrorcult

## Weekly bug-sheriff to triage issues that come up | Paul
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/952880631514288148)
- Maybe also include triaging PRs that should/could be included in the progress report
    - **Use labels for project reports, is 3 too many?**
        - 3 is good, use Major for things that should be added
        - Minor for things that may be added/fine to miss
- We can shuffle maintainers around to this role depending on availability
    - Have a bot or something that displays how many issues are untagged?
    - **Whoever volunteers**


## Fixing/refactoring test pooling | DrSmugleaf
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/954006741568344084)
- Restarting the round is not a foolproof solution to reset the instance.
- Integration test client reconnection is faulty which is why pooling never applied for client instances.
- **We need functioning full state serialization, then reset the state.**


## How does one move the YAML Linter to engine | DrSmugleaf
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/954006885802049586)
- How do we have content have a way to specify IOC services to use if the YAML Linter is in the engine.
    - **Nobody knows**
- Currently all the YAML Linter project does is start up two integration instances and call a prototype manager method.
    - **Nobody knows an alternative**
    - **PLS HELP PJB**


## Where to draw the line on references to non-SS13 media | PJB
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/953952903964549130)

Examples of references to discuss:
* https://github.com/space-wizards/space-station-14/pull/6037/files many AI names from small names barely anybody knows to SHODAN to Siri.
    * I fucking added X.A.N.A. to the AI name list on /vg/ you can damn well bet your ass I'm gonna try to keep it there
        * Who added XANA I must know who here stans Code Lyoko
            * HERE WE ARE, GOING FAR, TO SAVE ALL THAT WE LOVE
* Kamina glasses & other Gurren Lagann items
    * Keep
* Hatsune Miku clothes
    * Keep it's CC
* Alien franchise (aliens duh but also Ripley mechs?)
    * No (we have replacements thank god)
    * RIP smug
* Duck game items on /vg/
    * VG items are direct asset rips, fuck that
* Portal gun on /vg/ (Terraria has one too!)
    * It's pixel should be fine. Valve allows a lot of usage from what I know.
* Red telephone
    - **This is fine until valve releases their Red Phone AU**
    - Yes this is fine

(Writing out thoroughly since I won't be here)

Some thoughts:
* Something like Siri or Windows might be ick since those are actively advertised trademarks and stuff. Something like SHODAN isn't as big of a deal?
    * **Agree**
* A simple name drop like SHODAN isn't as big of a deal as complete content-take like Aliens.
    * **Agree**
* Taking assets is never OK, obviously.
    * **Agree**
* Miku clothes are fine only because they allow nonprofit use, prob wouldn't be otherwise?
    * **Agree**

**Case-by-case, check what each owning company has policy-wise**

* **If the demand is very strict it may want us to remove the content from git hsitory, needing a rewrite, which is painful**


## Renaming/editing/hiding old rsi-editor | mirrorcult
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/950509187073470509)
- People are still trying to use it over RSIEdit
- Already archived
- **We are waiting on GitHub to detach the fork**
- **Edit the rsi-editor Readme to lead to RSIEdit**

RSIEdit
- It doesn't show up on the organization's project list because it's a fork
    - Ticket to detach it already open with GitHub Support


## Commission lobby art | mirrorcult
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/952756729295274034)
- We have lobby BG support now
- PJB's take: BG should take full screen at ~16:9 aspect ratio. Part will be covered up by lobby UI on the right frequently; art commissioned can put less important stuff there to avoid wasting effort.
    - Please no inset image like SS13 lobby. The lobby goes on top of the art.
- **Find an artist, get the price, use Patreon money.**
    - Artist for some of the stuff is aspev, steam art is waster of orange.
- **Try to add support for viewing a map through a viewport in the background.**
- **Make a transparent overlay to give to the artists to know what aspect ratio they have to work with**
    - **Overcompensate for a long server name**


## What extra servers do we want | mirrorcult
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/953039871587520512)
- We have EU West 1, EU West 2, US West and Oceania at the moment
- We can host more instances on our current hardware
- **Poll for MRP**
    - Discord poll, but we should implement game polls too
- **US East pls**
- Kill EU West 1 make 2 new 1
    - add US East


## Early Access Roadmap
[Previous Roadmap](https://docs.spacestation14.io/en/maintainer-meetups/secret/2022-01-22-meetup)

- emergency shuttle
    - auto shuttle movement
- gamemodes/antags
    - dynamic | mirror
        - nuke ops
            - the nuke is done, but it doesnt explode
                - large kaboom required
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
    - Species
        - we need to do non human body parts
            - needed to reenable lizard
- __***ENGINE EDITOR***__ | PJB
    - could benefit from full state reload
- movement refactor
    - Client side movement?
        - a smidgen
            - as a treat
- Tutorial
    - In game guides
        - Yes
        - Waiting on pretty labels
        - books/ebooks in pda
            - ebooks preloaded on pda for selected job
            - when rich text gets merged
- oldchat + ui refactor | Jezithyr
    - we did it
- explosion refactor | ElectroJR
    - under review
- combat rework
    - hard to hit someone
    - wide attacks might be broken
        - prediction issue
- ghostrole bans | ShadowCommander
    - unify ghost roles prototype
- pulling refactor | Sloth
- admin notes | DrSmugleaf
- Admin traitor/role menu
    - Assign people roles
    - Objectives UI
- Job playtime requirements
    - Playtime tracking
    - Per role playtime tracking
- experimental science
- action ui refactor, [like ss13 maybe](https://i.ytimg.com/vi/iFf_T31C-iU/maxresdefault.jpg)
- change pvs to p/invoke zstd
    - compression too slow
    - we're using (Q's) C# library for zstd
- Prototype composition | Paul
- Server polls
    - Map poll at round end
- Round Statistics
    - Log votes, which maps are played the most…
- suit storage

Crashes / Critical bugs: (when are we moving these to GitHub)
- Round restart fails sometimes (may be a physics issue)
  => till next time


## PJB isn't here so there's no Tetris after-meeting party
