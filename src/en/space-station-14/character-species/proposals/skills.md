# Skills System

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| Killerqu00 | Killerqu00 | :x: No | TBD |

## Overview

Skills System is an abstract system of labels that describes knowledge an entity possesses, enabling this entity to have certain abilities. It can be used in a variety of ways both by forks and possibly upstream - this doc discusses only the technical applications of the system.

## Background

Currently, there are some abilities in the game locked behind your roundstart role (chaplain using the Bible, mime using Mime powers...), as well as other factors. Those abilities aren't directly visible currently.

## Features to be added

Skill System is a new tab in character menu. It displays the list of all currently learned skills, as well as some skills that are being learned. A player only has the skill once it has been fully learned, however.

### Examples
**None of those are actual feature suggestions - these are only things you could possibly implement using this system.**

Some of the possible skills to implement via this system are:
- "Chameleon Technology Knowledge", given to syndicate agents and those who have opened an uplink. You can only see the "Chameleon" verb if you have this skill.
- "Stargate", given to those who have learned it from the library - see (Librarian Proposal)[src/en/space-station-14/departments/service/proposals/theshued-librarian-gameplay.md].
- Roundstart skills for those picking a certain role. Probably more suitable for MRP+ servers, since those usually enforce some kind of "Don't do others' job" rule.
- Learnable martial arts, specific moves and such.

## Game Design Rationale

This is a core mechanic needed for the already accepted (Librarian Proposal)[src/en/space-station-14/departments/service/proposals/theshued-librarian-gameplay.md] - effectively, it implements the knowledge from encrypted books. This actually makes librarian a useful role. Also, it allows for new strategies - for example, antagonists could learn some forbidden knowledge by interacting with a library in order to outplay security later on.

## Roundflow & Player interaction

Out of scope - see librarian doc, since this is the only currently accepted application of this system.

## Administrative & Server Rule Impact (if applicable)

Q: Does this feature introduce any new rule enforcement challenges or additional workload for admins?
A: No, it regulates gameplay itself without any need for intervention.

Q: Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
A: Theoretically people could break into the library and research the skills, bypassing the librarian, but this is out of the scope of this proposal - this is more of a librarian gameplay problem.

Q: How are the rules enforced mechanically by way the feature will be implemented?
A: Let's take the "Chameleon Technology Knowledge" from above. If the conditions for learning this skill are set to the exact ones that qualify as revealing in the rules, then the rule has just been reinforced mechanically. Again, this is just an example of how this system can be used to regulate the rules - actual suggestions of the skills are out of scope.

# Technical Considerations

Q: Does the feature require new systems, UI elements, or refactors of existing ones? Give a short technical outline on how they will be implemented.
A: It is a new tab in the Character Menu (C key by default). It would require a small refactor to it. Otherwise, it's just a matter of adding the system.

Q: Are there any anticipated performance impacts?
A: Given that the skill check would run only when the action is being performed, no.

Q: For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)

A: Here is an example of the similar UI element in C:DDA, called "Proficiencies".
![C:DDA screenshot that shows a menu titled "Proficiencies". Proficiencies marked white are at the top, and not fully learned proficiencies with percentage near them are displayed in gray.](https://i.imgur.com/niPec94.png)