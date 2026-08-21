# Maintainer Meeting (20 May 2023)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 20 May 2023 19:00 UTC

**Attendees:**
- DrSmugleaf
- flipp
- metalgearsloth
- ShadowCommander
- PJB
- Visne
- keronshb
- ElectroSR
- Jezithyr
- mirrorcult

## Component shutdown events | ElectroSR
- Should we combine ComponentShutdown and ComponentRemove events?
    - Yes, but also remove the separation between component Add and Init (and Startup)
    - Also remove component enabling/disabling
- Should we add a new event that only gets raised when a component is explicitly removed, rather than due to entity deletion. Standard removal events would still get raised.
    - Context: removal logic that is a waste of time if the entity is just getting deleted anyways.
    - Components shouldn't do complex work in removal/deletion. Deletion should just get rid of things as aggressively as possible, only keeping the game state consistent.
    - Removal of components should be private to systems rather than a public API. Systems should do "on removal" logic themselves in a public function that removes components for you.
        - Make it opt in (Access attribute).
    - Keep a deletion event if the entity is deleted altogether, but don't fire it if individual component is removed.
        - Combined with the earlier point, this means that if you ABSOLUTELY MUST run code on all component removals, you need to explicitly call it from both your public removal function AND on deletione event.
    - Keep a component removal event in case some use case really needs it.
- If we have a separate explicit removal event, can we eventually remove InSafeOrder() & just enforce that component removal doesn't require querying other components on that entity?
    - **YES**

Edit with bonus questions:
- If the events are merged, what do we do with deffered component removal. Currently it raises a shutdown event, but defers the remove event & actual removal.
    - idk
- Also: should events be raised for components that are deferred for removal (i.e., should the subscription enumerator check the component's lifestage?)
    - idk 2


## UI stylesheets and themes | ElectroSR
- Meeting topic/discussion: Stylesheets & themes.
- How do we make them better? Stylesheets and rich text should probably use themes when possible.

- Decision:
    - Combine stylesheets and themes, move it to YAML
        - Context: stylesheets are originally C# because they need to be able to describe C# objects like style boxes, and `.css` can't do that.
        - Whoever makes the YAML syntax has to figure out how to implement constants for re-use in the stylesheet.
    - Make it easy to extend stylesheets (edits of simple properties, colors etc).
    - For complex animations/styling of controls, content should inherit engine controls and implement logic there.
        - We will not be implementing more complex styling functions from CSS like built-in transitions, aniamtions, descendant selector.


## Arch | DrSmugleaf
- Smug giving status updates on Arch
    - She's ranting I love it when she has this energy.
    - She's explaining it again


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
- EL BODY SYSTEM | jez (sloth?)
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
- A trailer for Steam
    - Also the screenshots for steam and the website

Crashes / Critical bugs: (when are we moving these to GitHub)ç
=> till next time
like and subscribe
smash that button
did you know only 6% of contribs join this meeting?
