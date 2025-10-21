# The Wizard
<!-- Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar. -->

| Designers                                                                         | Implemented     | GitHub Links |
|-----------------------------------------------------------------------------------|-----------------|--|
| /tg/station, Citadel Station, and other various SS13 forks, Keron, ActiveMammmoth | :white_check_mark: Yes | https://github.com/space-wizards/space-station-14/pull/35406 |

<!--
`Designers` should be the names that you use on GitHub and/or Discord. This is optional but strongly recommended, since:

- This acknowledges credit where it is due
- People who are confused about the written intent can use this information to contact the authors

`Implemented` is the status of the feature.

Github links can include multiple PRs, if relevant.
-->

## Overview

<!-- A very short, maybe three sentence summary of what this proposal is about. A high level "overview" or "what this adds". -->

This is for The Wizard antagonist - which is to help answer any frequently asked questions for the Wizard and to help 
others understand what the Wizard is about. The Wizard in short is a highly disruptive/chaotic antagonist that does
anything to their whim. A lot about the Wizard is that it doesn't conform to standard rules so it very much is the
embodiment of "a wizard did it." Players will be encouraged to come up with their own gimmick, while still being an
antagonist to the station.

## Background

<!--
Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game.

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.
-->

## Features to be added

<!-- Give a description of what game mechanics you would like to add or change. This should be a general overview, with enough details on critical design points that someone can directly implement the feature from this design document. Exact numbers for game balance however are not necessary, as these can be adjusted later either during development or after it has been implemented, but mention *what* will have to be balanced and what needs to be considered when doing so. -->

## Game Design Rationale

<!--
Consider addressing:
- How does the feature align with our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosphy?
- What makes this feature enjoyable or rewarding for players?
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- How does it enhance player cooperation, competition, or emergent gameplay?
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?
-->

One of the unique things about the Wizard is that by its existence it does violate some of the antagonist pillars, but that's intended (and previously approved).
The Wizard is an entire force of chaos. It's meant to have a lot of reality bending/shifting, powerful spells to enable its gimmicks.

- Want to trap a bunch of people in lockers with the Staff of Locker and then animate said lockers to make it a challenge for the 
crew to get out? Go for it.

- Want to swap bodies and pretend to be the captain/security to not only sow distrust, but also punish anyone who disobeys you with a smite?
100% fine.

- Want to summon a dance floor and force everyone to dance until they run out of stamina? Sure.

The world is your oyster, you're literally a wizard in space.

Now not all spells are going to be straightforward. If you try to fireball someone in the face, you're going to die too unless you put some distance.

Some magic may be locked to using an item, which means you'd need to risk losing the item or also buy a recharge spell to compensate.

Or some magic may require robes, which means you'll be relatively unprotected and the definition of a glass cannon.

And with the wizard only being stuck to 10 currency, compared to other antagonists that may have more spending power, they need to make a choice of what they'd like to build.

Despite it potentially violating some antagonist pillars, it does help highlight the core design principles, mainly:
- Chaos
  - The Wizard is the embodiment of this pillar. You know you're in for a wild ride when a wizard is around. The potential they have for introducing chaos is pretty high. 
    They may give everyone in existence a gun and turn the station into a standoff. Or the captain might be turned into a cluwne as punishment. 
    The Wizard may even just summon a dance floor and make people dance their stamina away. By being able to shift reality, the choices are basically as creative as the contributors can get.
- Seriously Silly
  - There's almost nothing more unhinged than a Wizard and their antics. A well timed fireball or a smite may end up being hilarious in a story told later.
- Dynamic Environment
  - Wizards being reality benders can easily shift the environment around them, depending on what they're feeling.
    - The floor could in fact, be lava.
    - Maybe they feel like the captain's quarters really needed a back door so they just use a wand to turn a wall into a door.

## Roundflow & Player interaction

<!--
Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
- Which department will interact with the feature? How does the feature fit into the [design document](../space-station-14/departments.md) for that department?
-->

## Administrative & Server Rule Impact (if applicable)

<!--
- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
- How are the rules enforced mechanically by way the feature will be implemented?
-->

The Chaos the Wizard brings may introduce challenges to the admin team. 
Some things like mass event spells (when reworked) will considerably lower the amount of free agents it makes which in turn reduces admin headache.

Furthermore, some optional challenge purchases may be introduced to give the wizard more drive. So people who aren't as creative, but crave a challenge, will have some guidance on what to do which may reduce friendly wizards. There's not too much that can be done mechanically to truly prevent any friendly antag.

# Technical Considerations

<!--
- Are there any anticipated performance impacts?
- Does the feature require new systems, UI elements, or refactors of existing ones?
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
-->

Since Wizard's been out there's refactors that need to happen to get Wizard fully back in and those include (but aren't limited to:)
- Actions
  - A generic way to spawn sprite effects is needed (ie. Void's Applause)
  - Magic Comp (which is just a fancy named requirements comp) needs to be converted to ActionRequirements and expanded on
  - Targeting and Spawning behaviors need to be added as either presets or overrides
    - ex) An instant action may have the targeting logic to target X amount of people in sight
    - ex) A world action might have targeting logic to target 3x3 tiles from where it was clicked
  - Event Spells (actions) also need to be converted to gamerules and work more as a 1 purchase and done kind of thing.
- Event Spells
  - As above, the event spells need to be reworked to launch gamerules instead of just events.
  - For the more dangerous event spells (Summon Guns/Magic), the Wizard should be forced to teleport back onto the station if we detect they're not. To make it fair that they commit to the bit
  - And for Summon Guns/Magic specifically the free agent rate is going to be turned down considerably so it has X chance to turn someone into a survivor instead of it being guaranteed.
- Polymorph
  - The polymorph system itself needs an overhaul, as there were some issues with entity references and the like. The Rod Polymorph would get the biggest benefit from this.
- Rods/Brute Damage Gibbing
  - Wizard Rods need to be changed to not delete people and objects. Even setting gib to no gets bypassed by the deletion that Rods inheretly have and it's extremely easy to gib with enough brute damage so both things also need to be changed.
- Cameras working off grid
  - Cameras need to work off grid so the Wizard can use its pondering orb effectively
  - This would also open up oppertunities for other antags (Nukies, Listening Outpost, Abductors, Clock Cult, etc)