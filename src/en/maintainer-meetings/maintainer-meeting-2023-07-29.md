# Maintainer Meeting (29 Jul 2023)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 29 Jul 2023 19:00 UTC

**Attendees:**
- EmoGarbage
- Visne
- Wrexbe
- ElectroSR
- PJB
- Chief_Engineer
- Moony
- Notafet

## Ambiguity of rule-relevant information in-game - Chief Engineer
* Certain rules are unclear at least partially because the game doesn't do a great job of presenting certain types of information to the player. This can result in confusion around certain rules, particularly for players who don't spend a significant amount of time in the game.

* This is the information I can think of that should be clearly presented in-game:
* Antag status, including for ghost roles
    * Example: Slimes clearly™️ communicate their antag status in their role description, but this is inconsistent with other ghost roles which also have ghost role rules saying that they are an antag.
        * **On spawn (regular jobs & ghost roles), the character window should always open.**
        * **Character menu gets far more info such as antag status, job expectation, etc... Actually make it useful!**
        * **For ghost roles, add lottery, so people have time to read the role's description.**
        * **This should provide people unmissable info what's expected of them (e.g. if they're antag), if people still wanna be friendly in an RP game we can't stop them.**
    * What is contraband, specifically what is non-stealth contraband
        * This is info for the antag player (in the item status box), so people realize what they're buying is contraband.
        * **Silly stuff like syndicate balloon isn't really contraband: security can't assume you're a traitor.**
        * ![](https://hackmd.io/_uploads/HJFTnRMjh.png)
        * **No explicit indication for obvious crap like emag, power sink, etc. Players should use their brain, but do have good descriptions for it.**
    * What are high value items, things that shouldn't be given away by heads
        * People don't realize you can't *just* give the hypospray away.
        * **Put a list of high-value items in the guidebook.**
    * Which bodies can be returned to [#8495](https://github.com/space-wizards/space-station-14/issues/8495).
        * **Make sure it's clearly explained in the guidebook.**
        * **Make sure it makes sense.**
        * **Doesn't need to be 100% obvious whether a corpse is revivable or not just from examine text, minimum should be health analyzer.**

> What is the best way to present this information to players in-game? Many players miss that xenos, whose description includes "kill all crewmembers", are antags. Is this just a skill issue, or can it be mitigated with game changes?
How do you communicate what is a high value item without encouraging/justifying things like throwing it in the vault round start
What's the best way to ensure that contributors are aware that this information needs to be presented to players?
Is there a way the contraband status of stealth items can be communicated without ruining their stealth?

mucho texto

**See bullet points above**

## Salvage Design Direction maintainer meeting topic - Emisse
(what's the opposite of mucho) texto
* tstalker says it's poco.

According to EmoGarbage: Used to just have magnet salvage. Pull shit in, mine it. Now we have expeditions (~10min): fly to length, procgen dungeon. These are very different and it's not clear how this shit fit into gameplay.

* **Make expeditions shorter & faster**
    * **~5 min max time limit**
    * **Corpse recovery if left behind**
    * **stuff to make looting faster: mark items to be teleported, no inventory management**
    * **Just make it more gamey**
    * **Force a cooldown between expeditions. People can do magnet salvage if they want, but it's not required**

## Spawn coordinates naming - ElectroSR
* Should we rename the entity spawn variant that takes in entity coordinates to clarify that it spawns-then-attaches or something like that
* **Yes, make more clear naming.**
* **A lot of helper functions.**
* **We need explicit helpers for common scenarios like "spawn next to player" (accounting for containers).**

## What kinds of gamemodes are acceptable upstream? - EmoGarbage
* What kinds of gamemodes are acceptable upstream?
* Current gamemodes are all on-station regular stuff. People have jobs, antags happen.
* Some idea for more devious game modes:
    * Planet tower defense
    * Team deathmatch
    * STATIONWARE
* Do we run total conversion and NRP modes (TDM, etc)
* What kinds of modes should be opt-in vs. part of secret
* **People can vote for alt gamemodes, within population ranges (e.g. 20 players max for TDM).
* **Alt gamemodes are WYCI**

## Antags: to midround or not? - EmoGarbage
* What modes should be roundstart / in secret
* What modes/antagonists should remain as midrounds
* **We're just bikeshedding dynamic/game director. I think we're all in agreement there's nothing special to decide here**

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
    - Maybe if we hold the VRChat maintainer meeting
- __***ENGINE EDITOR***__
    - could benefit from full state reload
- movement refactor
    - Client side movement?
        - a smidgen
            - as a treat
            - acruid pls com bak
                - What does this even mean anymore?
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
    - holy shit we have replays now


Crashes / Critical bugs: (when are we moving these to GitHub)
=> till next time
like and subscribe
smash that button
did you know only 6% of contribs join this meeting?
