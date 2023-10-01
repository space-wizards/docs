# Maintainer Meeting (10 Jun 2023)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 10 Jun 2023 19:00 UTC

**Attendees:**
- DrSmugleaf
- PJB
- ElectroSR
- KeronSHB

## Target round length | ShadowCommander
- How long?
    - Citadel is too long at 2 sometimes not
    - Really depends on what's going on in the round
    - **60/90 minutes and give admins permissions to extend the shift**
- **Not hard-forced mechanically**
    - i.e. no forced un-recallable shuttle at 90 minute mark
    - If someone holds the round hostage others AHelp it
- **If we want to end the round, start ramping up events and disaster on the round**
    - Overridable by admins
    - Maybe override with player vote?
    - Obviously tune for MRP
    - Should take state of round into account
- Add a TF2 payload cart to SS14

## Formatting for log sawmills | metalgearsloth
- Options:
    - name
    - name.othername
    - name_name
    - Name
    - Name.Name
    - Name_Name

- **Decision**:
    - snake case elements
    - example: `foo_bar.baz`

## Obsolete freeze | PJB
![](https://hackmd.io/_uploads/B17h1SMP2.png)

- Fucking fix the code reeee
- **"Just don't obsolete anything that's on the tier of `.Owner` for now probably"**
- **No content freezes or anything like that, it doesn't work**

## IoCManager resolves in UI code | PJB
- UI controls currently rely on `IoCManager.Resolve<IUserInterfaceManagerInternal>()` in current
- **Option 1: constructor parameter**
    - `new Control(UI)`
    - First parameter becomes `IUserInterfaceManager`
    - Must be passed through manually when creating new controls
    - XamlUI does it automatically, only relevant for dynamic control creation.
    - Hopefully not too inconvenient, have a `UI` property you can pass through easily.
    - Add `IDependencyCollection` property to `IUserInterfaceManager` to link it through.

- ~~Option 2~~:
    - UI manager gets passed through on tree attach (when you add control as child of another one).
    - Means no needing to pass constructor parameter manually.
    - Fetching dependencies like sawmills must be done from `EnteredTree()` instead.
    - Add `IDependencyCollection` property to `IUserInterfaceManager` to link it through.

## How do we make PRs easier to review
- **We don't know**

## Early Access Roadmap
- gamemodes/antags
    - dynamic [c#16548](https://github.com/space-wizards/space-station-14/pull/16548)
        - lings? [c#16513](https://github.com/space-wizards/space-station-14/pull/16513)
            - needs DNA
        - blob
        - revolutionaries
            - we want a generic antag overlay system
            - loyalty implant
            - faction system
        - clock cult | keronshb
            - waiting for mind rework
- EL BODY SYSTEM | jez (sloth?) ![](https://cdn.discordapp.com/emojis/933790288860815380.webp =40x)
    - some refactors were done by mirror, still some left
    - surgery died in the war of 1992
        - Mirror died in the war of 1993
    - limb damage.....
- body system but again
- body system
- __***ENGINE EDITOR***__
    - could benefit from full state reload
- movement refactor
    - Client side movement?
        - a smidgen
            - as a treat
            - acruid pls com bak
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
    - "Uh" | PJB 19/03/2023
    - "Smugleaf to answer the literal question posed, because its better than Byond I hope" | PJB 01/04/2023
    - "Well I have a sample size of 1 myself and I do believe people do not in fact play the game" | PJB 15/04/2023
    - "Well I mean well ok we are somewhat close to being able to play the game, I still haven't played the game however" | PJB 20/05/2023
    - "It still runs pretty bad however I do understand how people play it" | PJB 10/06/2023
- A trailer for Steam
    - Also the screenshots for steam and the website

Crashes / Critical bugs: (when are we moving these to GitHub)
=> till next time
like and subscribe
smash that button
did you know only 6% of contribs join this meeting?
