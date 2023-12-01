# Maintainer Meeting (19 Aug 2023)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 19 Aug 2023 18:00 UTC

**Attendees:**
- Visne
- ElectroSR
- Metalgearsloth
- ShadowCommander
- PJB
- DrSmugleaf
- Julian
- Mirrorcult
- Notafet
- TheQuietOne
- Faint
- Jezithyr
- EmoGarbage

![](https://hackmd.io/_uploads/SJ_QSYAhh.png) omg miku

## Namespace changes in content | metalgearsloth
- https://github.com/space-wizards/space-station-14/pull/18869#issuecomment-1672388772
- client and server end with s but shared doesn't so it was updated
- PR is also making component changes
- IMO no because it's cleaning up code so it's actually consistent
- **Do it in standalone PRs unless the PR is very small**
    * Better for reviewing and forks
- **Post breaking changes in #codebase-changes AND THE GITHUB DISCUSSIONS ANNOUNCEMENTS**

## Conventions for locale strings | EmoGarbage
- there is literally no rhyme or reason anywhere
- there isn't a guideline for what the locale key is supposed to look like
- the file structure is a literal hellhole of a million folders with a single file inside of them
- it doesn't even mirror Prototypes or the c# code file structure
- "Does anybody even use the file tree?" - Smug
- Mirror idea: what if they're top-level popup/, verb/, prototype/, etc.
    - Would make future rewriting easier.
    - **Just always have `verb-` or `popup-` or `ui` in the key for that purpose.**
- **Mirror C# structure**
    - Mostly used from C#: popups, verbs, etc..
    - C# structure is *fine*, could be better but ah well.

## How do we handle reagents with extra data | ElectroSR
- IMO we should extend solutions to also be able to store non-prototype / complex reagents that aren't simply an ID string.
- How would complex reagents store data? Would it just be an instance of some class per solution or would they point to some shared instance/entity?
- If its a shared entity, how do we handle:
- PVS
- Deleting the entity when all solutions are gone.
- Cloning an entity if one of several solutions gets modified (e.g., dna damage).
---
Comments:
- IMO it would probably be easiest to just have complex reagents be instances of some class that defines special behaviour in C#. Allowing them to be entities probably just overcomplicates this?
- this has definitely been brought up before, but I don't remember what the conclusions were
- if there even were any

---

- ![](https://hackmd.io/_uploads/SJOE9tR2h.png)
- **(Make it some base type other than object, figure out how to do automatic merging behavior)**
- Idea is this data object would be copied

## Don't speedmerge large content PRs | metalgearsloth
- specifically [c#18840] and [c#18136] (TEG and borgs)
- I know they're both maintainers but at a glance I can see a lot of standards not being applied
- there's a lot of older prs that still need reviewing
- having a maint get their 5k line pr get merged while your small pr is still sitting there is a kick in the guts
---
- personally:
- I'd rather playtest after someone's reviewed it thoroughly so if there's no major issues we can keep it rather than expect every time for it to get reverted. This is to avoid stuff like the ninja pr which sat in review hell for months
- There's a risk that some big, really not up-to-standards code gets merged and then people get unhappy when it needs reverting, or the bigger risk that it just stays there.
- **Have it be moderately ready for test merges**
- **Remember test merges**
- **Try to notify game admins for roles and gamerules (events)**

## IMPROMPTU TOPIC: Contributor survey | Mirrorcult
- Do it sometime soon™

## Derailment
OH MY GOD WE HAVE 700 MERGED PRs LAST MONTH ALMOST TWICE OTHER CODEBASES.

## Change how we do !logging | Visne
- !logging tells you to dm a random maintainer who may not know how it works and may have to message someone else
- Logs may have PII
- **Remove PII from logs so they can be posted in public channels**
    - **Edit the !logging command**
- **Eventually have some ticketing system that lets every maintainer look at it**
- Ticket system is a massive pipe dream lmao wyci

## Net entities | metalgearsloth
- how do we handle commands for migration (I'm just assuming they should all take NetEntity atm)
- anything else that may come up
- **Write a migration guide for forks**

## Arch migration | metalgearsloth
- after the initial arch port to swap out internals what else do we want to take advantage of / how in terms of what I think is priority e.g.:
- queries (and how we prefer to structure it content side) https://github.com/genaray/Arch/wiki/Query-techniques
- command buffer (to replace RemCompDeferred / other stuff editing in loops), would we just expose this directly, do we flush it after every update, do we store one on EntityManager and flush it at the end of ticks etc. https://github.com/genaray/Arch/wiki/Utility-Features
- eventbus
- job scheduling (replace my shitty parallel.for everywhere)
- relations
- **its good**

## Named args enforcement | metalgearsloth
- so emote sounds broke and it turns out adding an extra arg to the emotes method shifted everything and broke it.
- should we enforce this in review, even just past a certain point (e.g. 3 args) to avoid bools suddenly being mixed up or is this just a skill issue.
    - **Enforce it in review when we decide the guidelines.**
- alternatively chat system is so fucking bad this was bound to happen (freeze until refactor PLEASE).
- **Maybe write an analyzer for it**
- **Also figure out how long it takes to run analyzers**

## Default values in component C# definitions | PJB
- HAS THIS HAPPENED TO YOU?
- You define a component in C#. You only need it for one thing right now. Instead of putting the value in the YAML, you put it in the C#
- Should we put this as a no-no in the conventions?
- **Do it case-by-case**

## Additional changelog categories/types for codebase changes and pretty/lore versions | ShadowCommander
- **Do it for codebase and game admin changes that can be filtered.**
```
**Changelog**

:cl: PJB3005
[Gameplay]
- add: Nanotrasen finally decided to give engineering departments something to do, and has finalized the schematics for the thermo-electric generator (TEG).
- add: The TEG creates power by exchanging energy between a hot and cold gas on its two sides. 
- tweak: You can turn on gas heaters/freezers with alt-click now.
- tweak: You can open air alarm and pump menus with activate (E) now.
```
- **Have separate files and ids for any channels (admin/fork) so forks can also have their own.**

## Early Access Roadmap
- gamemodes/antags
    - dynamic [c#16548](https://github.com/space-wizards/space-station-14/pull/16548)
        - lings? [c#16513](https://github.com/space-wizards/space-station-14/pull/16513) (closed)
            - needs DNA
        - blob
        - revolutionaries [c#18477](https://github.com/space-wizards/space-station-14/pull/18477)
            - we want a generic antag overlay system
            - loyalty implant
            - faction system
        - clock cult | keronshb
            - waiting for mind rework
- EL BODY SYSTEM | jez ![](https://cdn.discordapp.com/emojis/933790288860815380.webp =40x)
    - some refactors were done by mirror, still some left
    - surgery died in the war of 1992
        - Mirror died in the war of 1993
    - limb damage.....
- body system but again
- body system
    - Maybe if we hold the VRChat maintainer meeting
- __***ENGINE EDITOR***__
    - could benefit from full state reload
- movement refactor
    - Client side movement?
        - a smidgen
            - as a treat
            - acruid pls com bak
                - What does this even mean anymore?
                    - what is an 'acruid'?
- ghostrole/antag bans
    - for ghost roles make taking them not valid if role-banned
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
    - "Uh" | PJB 19/03/2023
    - "Smugleaf to answer the literal question posed, because its better than Byond I hope" | PJB 01/04/2023
    - "Well I have a sample size of 1 myself and I do believe people do not in fact play the game" | PJB 15/04/2023
    - "Well I mean well ok we are somewhat close to being able to play the game, I still haven't played the game however" | PJB 20/05/2023
    - "It still runs pretty bad however I do understand how people play it" | PJB 10/06/2023
    - "Still does" | PJB 19/08/2023
- A trailer for Steam
    - Also the >>>>**screenshots**<<<< for steam and the website
        - DO WE HAVE SELF GHOST HIDING
    - holy shit we have **replays** now


Crashes / Critical bugs: (when are we moving these to GitHub)
=> till next time
like and subscribe
smash that button
did you know only 6% of contribs join this meeting?
