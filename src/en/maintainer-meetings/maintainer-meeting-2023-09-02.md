# Maintainer Meeting (02 Sep 2023)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 02 Sep 2023 18:00 UTC

**Attendees:**
- EmoGarbage
- Visne
- Julian
- ShadowCommander
- ElectroSR
- Lank
- Notafet
- PJB
- Faint

## "the github reviews murder case special"
- get rid of codeowners. do any of us actually use it, it just confuses people who think the codeowners need to review before its merged
    - **Remove all general ones and change to one or two folders deep, so that it actually goes to the relevant PRs
- review labels rn are half-automated which is good but its hard to tell when someone finishes a review. have people re-request a review on github to clear the ‘changes requested’ label and expect ppl to do this
    - Make the bot remove the "Awaiting changes" label when PR reviews are requested again
    - Just tell more people to press the re-request review button when reviewing.
        - Maybe make a copy paste that can be put as the instructions for new contributors
- have maintainers actually assign themselves to review PRs that they're going to review so we aren't just passing this along through word of mouth
- ok basically just actually make use of the GH review features instead of having to tell people ‘uhh just ignore that’
- side quest. can we ask github for GH enterprise again since we're big boys and open source

## "a killing at the github issues and labels page "
- get rid of all prio labels except for URGENT they dont rly matter
    - We probably wont sort by + or - Low Priority, so
    - **Yes only URGENT**
- maybe consolidate the difficulty labels too but theyre probably fine
    - **Keep difficulty labels**
    - Easy should be able to be done by a new contributor with 0-4 PRs within a few hours.
    - Beginner friendly should be clearly written out what the requirements and goals are for the PR
- mapping issue labels (one for every map? makes it easier for mappers to sort through)
    - Not needed
- some ‘possibly no longer relevant' label (like tgs ‘flagged cleanup’label), close really old issues with this if we aren't 100% sure
    - some other ideas for issue labels that are actually useful:
    - ‘oversight' (easy to fix random stuff that just wasnt caught)
    - ‘regression’ (previously working feature is broken)
    - combine cleanup/needs refactor into ‘code maintenance’
    - ‘requires resprite’for arttainer issues
- go back through and properly clean up and label old-old issues by god there are 2.2k open and they are definitely not all still relevant. let us start a united front here. give a bunch of people triage and go at it over the course of like a couple weeks. make github issues useful again
- allow user labeling of issues, at least for certain kinds like feature request and oversight. probably thru some gh action that just looks in the issue body or in comments. iirc someone tried this like 2 yrs ago but it didnt work and we never fixed it
    - Yes fix the bot
- think about giving out triage access more freely, maybe to all experienced contribs?
    - **Yes**
    - And some game admins
    - All staff

## New art
- ok can we actually commission artists for new lobby art with our five million dollars like we said we would a year ago
- Yes. We need an artist.
- Lobby art ideas:
    - One of every Antagonist
    - One of every species
    - One of every Job/Department
    - This is not one artwork per subject, one artwork can have more than one subject.

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
