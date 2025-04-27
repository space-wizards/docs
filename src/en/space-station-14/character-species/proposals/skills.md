# Skills System

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| Killerqu00 | Killerqu00 | :x: No | TBD |

## Overview

Skills System is an abstract system of labels that describes knowledge an entity possesses, enabling this entity to have certain abilities. It can be used in a variety of ways both by forks and upstream. This doc will focus on upstream usages.

## Background

In general, skill system was described as a method of mechanically enforcing meta-knowledge and preventing others from doing others' jobs. Here's one of the discussions about this: [Link](https://discord.com/channels/310555209753690112/1008709214006427689/1298684771504754791)

## Features to be added

Skill System is a new tab in character menu. It displays the list of all currently learned skills, as well as some skills that are being learned. A player only has the skill once it has been fully learned, however.

Some of the possible skills to be added are:
- "Chameleon Technology Knowledge", given to syndicate agents and those who have opened an uplink. Prevents checking stealth items by security.
- "Machine Assembling", given to engineers roundstart. Allows to see exact components needed for a console/machine assembly.
- "Stargate", given to those who have learned it from the library - see (Librarian Proposal)[src/en/space-station-14/departments/service/proposals/theshued-librarian-gameplay.md].

## Game Design Rationale

This mechanic is both intuitive, realistic and dynamic. Skills can be learned, meaning having no people with a needed skill an inconvenience rathen than an unsolveable problem. It is realistic and intuitive - you have to learn about something before being able to do something. It is also rewarding - some advanced skills may allow to gate certain mechanics behind something that is not yet another science research they will never do.

This is also a core mechanic for the (Librarian Proposal)[src/en/space-station-14/departments/service/proposals/theshued-librarian-gameplay.md] - effectively, it implements the knowledge from encrypted books. This actually makes librarian a useful role. Also, it allows for new strategies - for example, antagonists could learn some forbidden knowledge by interacting with a library in order to outplay security later on.

## Roundflow & Player interaction

Skills are mostly related to service, in specific - librarian, where they serve as the source of skill learning. Certain skills can be granted roundstart, like those needed for department jobs. This also introduces some extra "switching jobs" roleplay - you actually learn your new job instead of just switching to it.

## Administrative & Server Rule Impact (if applicable)

Q: Does this feature introduce any new rule enforcement challenges or additional workload for admins?
A: No. It is partially created to enforce rules mechanically.

Q: Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
A: Theoretically people could break into the library and research the skills, bypassing the librarian, but this is out of the scope of this proposal - this is more of a librarian gameplay problem.

Q: How are the rules enforced mechanically by way the feature will be implemented?
A: Let's take the "Chameleon Technology Knowledge" from above. If the conditions for learning this skill are set to the exact ones that qualify as revealing in the rules, then the rule has just been reinforced mechanically.

# Technical Considerations

Q: Does the feature require new systems, UI elements, or refactors of existing ones? Give a short technical outline on how they will be implemented.
A: It is a new tab in the Character Menu (C key by default). It would require a small refactor to it. Otherwise, it's just a matter of adding the system.

Q: Are there any anticipated performance impacts?
A: Given that the skill check would run only when the action is being performed, no.

Q: For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
A: ![Here is an example of the similar UI element in C:DDA, called "Proficiencies".](src/en/assets/images/proposals/cdda-proficiencies.png)