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

This is for The Wizard antagonist - which is to help answer any frequently asked questions for the Wizard and to help others understand what the Wizard is about.

The Wizard in short is a highly disruptive/chaotic antagonist that does anything to their whim.
A lot about the Wizard is that it doesn't conform to standard rules so it very much is the
embodiment of "a wizard did it."

Players will be encouraged to come up with their own gimmick, while still being an antagonist to the station.

## Background

<!--
Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game.

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.
-->

The Wizard is already added but the document is needed to help clarify certain roundflow and even frequently asked questions about the wizard design.

It's an extremely rare, high-chaos, high-impact, and highly disruptive lone antagonist. Its existence is a culmination of the chaotic and goofy nature of the game and has existed as an implementation in SS13 for over a decade.

Their general goal is to "show off" their magical talent to the station.  They have spells and magical items that they can purchase to help them with these goals. Compared to other antagonists they're relatively powerful due to not only the rarity of the game mode, but also the nature of the Wizard being a glass cannon.
Compared to Traitors, this allows Wizards to be given powerful spells and some with reality-warping effects (like animating tons of objects, changing walls into doors, making the floor lava, etc).

### SS13 History
It's a port of the longstanding SS13 antagonist. Mainly it's based off of it's /tg/ server derivatives, but it's planned to be based off of multiple codebase implementations and a celebration of all things magic from SS13.
The Wizard was added relatively early in SS13's history, sometime between 2008-2011. By comparison Nukies and Revolutionaries were added sometime in 2004-2005. 
The /tg/ (and also Goon) implementation is a high-chaos lone antagonist. Sometime in their lore they were sent from the Space Wizards Federation to go mess with the station for some petty reason, or just for fun.

Generally their main goal was relatively freeform - teach the station a lesson they'll never forget. And they may have had some objectives mixed in, similar to that of Traitors but more open ended (eg. Take over the station, Kill X, Do Y to Z amount of crew, etc).

### SS13 Issues
One of the issues that some servers faced was that the spell upgrades fell somewhat flat. Mostly they were just cooldown reductions. Now not every spell's going to need an upgrade, but one thing to strive for will be meaningful spell upgrades.

Another was anti-magic. A relatively lazy way to counter Wizards (and other magical based antagonists) was the introduction of null rods and holy melons. At their conception they 100% shut down magic and while some adjustments were made to be more fair, 
the inclusion of antimagic changed per server due to its nature of being too much of a hard counter. This also gave the Chaplain (and Botany) too much focus on a handful of game modes,
which they ended up as departments you had to permakill ASAP.

As with SS14, a Wizard being a friendly antagonist was also an issue in SS13. Even with Traitor-like objectives, it didn't stop Wizards from joining up with the station for no good reason. See Friendly Wizards later on in this doc for the exact definition.

## Features to be added

<!-- Give a description of what game mechanics you would like to add or change. This should be a general overview, with enough details on critical design points that someone can directly implement the feature from this design document. Exact numbers for game balance however are not necessary, as these can be adjusted later either during development or after it has been implemented, but mention *what* will have to be balanced and what needs to be considered when doing so. -->

Wizard is already implemented but this would be in hopes of reintroducing it into Roundstart and as a subgame mode.

Currently their spell list is limited to some projectiles, very few events, teleportation spells, and a few different rods and staves, which gives them a little to work with but overall limits their capabilities and creativity. But once more spells and features are added to the Wizard that'll solve itself relatively quickly.

The plan is to overall add more spells that better help this, and backend mechanics to go with it such as an advanced targeting system and shifting some spells to game rules.

An advanced targeting system/spawning system will need to be added to not only make more creative spells, but to make it easier for contributors to just
add the parameters that they want to do while cutting down on custom logic. Custom logic won't be avoided but there can be a point where a lot is cut down.
- Advanced targeting/spawning as an actual working example is something like the force wall, where it targets a certain set of tiles in front of it.
- Another example would be having an instant spell with the targeting parameter to target all in sight, and another targeting parameter to spawn something underneath the wizard.

More reality-effecting spells will be also added to help vary up the Wizards gameplay and solidify it as an actual round-shifter.
- ex). A spell that forces tile movement to all in sight.

## Game Design Rationale

<!--
Consider addressing:
- How does the feature align with our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosphy?
- What makes this feature enjoyable or rewarding for players?
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- How does it enhance player cooperation, competition, or emergent gameplay?
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?
-->

One of the unique things about the Wizard is that by its existence it does potentially violate some of the antagonist pillars, but that's intended (and previously approved).

Potential antagonist pillars that it violates:
- Just a Spark
  - Wizards are 100% meant to disrupt a round, they are a major force of chaos after-all.
  - In ways it can help spark interaction too! 
    - By giving the entire living playerbase guns or magic, it could help tip the scales in a crew vs nukie fight.
    - They could punish a crew member by turning them into a cluwne, which should turn their fellow crewmates against them and also fear the Wizard so they too don't get cluwned.
    - A lot of the possibility are endless once the options are available to add sparks to the round!

- Escalation
  - As above, the Wizards are like Nukies and have their full potential right off the bat. This is so they can combine spells in a unique and creative way to make a more interesting round.

- Discoverability
  - Like Nukies, the Wizard can announce itself so it's relatively easily discovered. The Wizard has relatively low armor and healing access, easy to slip, and no stun or stamina resistance. It's very much the definition of a glass cannon, so counterplay comes from smacking the wizard.

Despite it potentially violating some antagonist pillars, it does help highlight the core design principles, mainly:
- Chaos (not carnage)
  - The Wizard is the embodiment of this pillar. You know you're in for a wild ride when a wizard is around. The potential they have for introducing chaos is pretty high.
    They may give everyone in existence a gun and turn the station into a standoff. Or the captain might be turned into a cluwne as punishment.
    The Wizard may even just summon a dance floor and make people dance their stamina away. By being able to shift reality, the choices are basically as creative as the contributors can get.
  - Spells can have a wide range of abilities, using weaponizing different features and game mechanics across the codebase. By combining them through freeform selection the wizard is able to have these features interact in emergent gameplay with wildly unexpected or rare results. The creativity of the wizard player is the tool that drives the round.
  - It can get old doing the same old thing all the other wizards are doing. Try out some new and creative combination to really spice up the round!
- Seriously Silly
  - There's almost nothing more unhinged than a Wizard and their antics. A well timed fireball or a smite may end up being hilarious in a story told later.
- Dynamic Environment
  - Wizards being reality benders can easily shift the environment around them, depending on what they're feeling.
    - The floor could in fact, be lava.
    - Maybe they feel like the captain's quarters really needed a back door so they just use a wand to turn a wall into a door.

The Wizard is an entire force of chaos. It's meant to have a lot of reality bending/shifting, powerful spells to enable its gimmicks.

- Want to trap a bunch of people in lockers with the Staff of Locker and then animate said lockers to make it a challenge for the 
crew to get out? Go for it.

- Want to swap bodies and pretend to be the captain/security to not only sow distrust, but also punish anyone who disobeys you with a smite?
100% fine.

- Want to summon a dance floor and force everyone to dance until they run out of stamina? Sure.

The world is your oyster, you're literally a wizard in space.

### Spell/Equipment breakdown:

Now not all spells are going to be straightforward. If you try to fireball someone in the face, you're going to die too unless you put some distance. 
Some spells having drawbacks (long cooldown, dangerous to use up close, long after-effect, hard to control, a Slaughter Demon not being your friend, etc) makes more interesting conflict.

Some magic may be locked to using an item, which means you'd need to risk losing the item or also buy a recharge spell to compensate. A Wizard being slipped just to have their equipment used against them is a classic moment.
And it's even funnier when the Wizard yoinks it right back with a different spell.

Or some magic may require robes, which means you'll be relatively unprotected and the definition of a glass cannon and reserved for some of the more powerful spells.

Most of this is based on vibes and themeatics. Does it make much sense for a Wizard to shoot lockers out of their hands? It's funny conceptually but it makes more sense that some piece of equipment is doing it instead.

#### Spells (Actions)

- These can be a wide variety of execution and power.
  - Execution examples:
      - Projectile, touch, event, area-effecting.
  - Power examples:
    - Summoning smoke which creates a thick smokescreen, and causing people to cough which forces item drop (themself included)
    - Shooting a fireball and blowing people up in an area of effect
    - Touching someone and they get knocked back.
    - An event trigger that temporary makes the floor lava.

#### Wands

- Like spells they can have a variety of effects. Never event-level effects.
- Wands are limited by charges and have a relatively higher power than staves.
- Can be given to allies to help assist you.
- Also meant to be used as combo pieces with other Spells or Equipment
  - Examples:
    - Wand of Animation + Flesh2Stone Touch Spell
    - Wand of Animation + Staff of Locker
    - Polymorphing your PAI or Wizard Apprentices

#### Staves
- Similar to Wands, Staves can have a variety of effects but nothing as powerful as event-level.
- Staves are also limited by charges, but have a lower power level compared to wands.
- They can self-recharge due to this, which also enforces them being combo pieces with other Spells or Equipment
- Can also be given to allies to help assist you
  - Examples:
    - A staff that turns walls into doors
    - A staff that polymorphs someone into a random creature
    - A staff that fires a random bolt of magic

#### Other Equipment
- This is for a variety of equipment that doesn't fit into the above three categories, these can be low-medium power.
- Examples
  - An orb of scrying to turn yourself into a ghost (temporarily) to observe others
  - An orb of pondering to look at the stations cameras
  - A deck of cards to give yourself a Holoparasite/Guardian
  - A magical contract to summon a predefined Wizard Apprentice
  - A magical item that summons a Slaughter Demon
  - A hammer that pulls everyone and everything towards you
  - A hammer that stuns and also knocks people away

### Wizcoin breakdown:

And with the wizard only being stuck to 10 currency, compared to other antagonists that may have more spending power, they need to make a choice of what they'd like to build.
Generally the higher the cost of a spell/item the more impact it has. That being said, some spells are planned on being upgradeable so they may cost 3 at base price, but further purchases of the spell (at the same or lower cost) may give you stronger effects.
- 1 Cost - Relatively low risk low reward (something like teleport spells, smoke, etc).
- 2 Cost - Standard. Higher power or unique utility.
- 3 Cost - Powerful. May have a lot of power (instant gibbing) or a profound effect (summoning guns)
- 4 Cost and above - Should be reserved for something that's 100% dominating because this is 40% of your budget.

## Roundflow & Player interaction

<!--
Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
- Which department will interact with the feature? How does the feature fit into the [design document](../space-station-14/departments.md) for that department?
-->

The Wizard is a _rare_ antagonist, but one that could show up absolutely **anywhere**. They're meant to be unfairly strong and weave chaos into any roundtype.
And because of this they should never be common. Maybe they should be seen only a few times a day if not less.

Since they can appear anywhere you could see them in the start or the middle of a round.

The Wizard will be given different tools and spells to help influence the chaos they have on the round. Some may be purely offensive or defensive,
but they also dip into the realm of goofy and wacky.

For example they could have a wand of polymorph which will turn a player into a random creature. That player would still have their own agency but also the positive (or negative) attributes with becoming
the creature. The wand could easily backfire on the wizard and the other player could be turned into something fearsome like a syndicate borg.

The Wizard being quite strong will be limited by the amount of spells they can buy. The ideal situation is to _avoid_ making "the game winning build" but instead
allowing the creativeness of the player to mix and match different spell & equipment combinations to make something interesting.
That being said, timestop and fireball is a classic combination for a reason, but giving players way more interesting options will help cut down on pure offensive Wizards.

### Friendly Wizards
This will be the only definition and rules of what is considered a friendly wizard. A **friendly wizard** is a wizard who will either refuse to use spells on crew OR will help out the station against other threats without an iron-clad reason.

An iron-clad reason would be something like Nukies relentlessly pursuiting the Wizard or a conversion antagonist attempting to convert the Wizard. In no other circumstances should a Wizard act friendly towards the crew.

A Wizard forcibly taking over the station, whether it's through actual force or mind swapping, is not a friendly wizard.

On the same coin, a wizard not killing a person every second is also not a friendly wizard. As long as a wizard is using their spells in some way that effects the station, they're not friendly.

Like any friendly antag, an antag just joining up with the station with zero reason isn't fun for anyone. But an iron-clad reason as stated above helps make rounds more interesting and memorable.

### Hiding in Ship/Space (Beginning of Round Stalling)

Some Wizards may hide in their den or in space and do nothing but event spells. This isn't good because while the event spells may have some sort of large impact on the round, 
the wizard themselves are effectively removed from it.
- Event spells
  - The plan to prevent Wizards from sitting back and firing off events is that the event trigger will also automatically detect if the Wizard is either 
    on a space tile (a certain distance away from the station) or not on the station grid. If any of those are true, there will be a mechanic to automatically teleport
    the wizard back onto the station.
- Spacing Protection
  - This mostly applies to Hardsuits or Softsuits of some sort. There is a plan to either double cooldowns of spells for Wizards who wear spacing protection or disable spells entirely.

### Polymorphs

Being polymorphed by a Wizard does **not** convert you to their team, no matter the result of the polymorph! The only exception is if you were already on the Wizard's team to begin with (ex. Wizard Apprentice).

### End State

The Wizard game mode does not have a natural end state generally, as the antagonist is mainly encouraged to come up with some gimmick to terrorize the station enough for them to call the shuttle.

In part, a shuttle should be automatically called if a majority % of crew are dead regardless of game mode. The shuttle would be unrecallable so people cannot stall out the round.

As stated later in the doc, an optional buy in to do objectives up to a round-end state will also be implemented to give people who are less than creative some end goal to work towards while also getting bonuses along the way.

## Administrative & Server Rule Impact (if applicable)

<!--
- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
- How are the rules enforced mechanically by way the feature will be implemented?
-->

The Chaos the Wizard brings may introduce challenges to the admin team.
Furthermore, some optional challenge purchases may be introduced to give the wizard more drive. So people who aren't as creative, but crave a challenge, will have some guidance on what to do which may reduce friendly wizards. There's not too much that can be done mechanically to truly prevent any friendly antag.

### Current Issues

- Event Spells
  - These are spells like Summon Guns or Magic - which turns everyone into a free agent. This was added initially, as a request _by a wizard_, because it would be too much of a net positive for the crew to get a bunch of guns and magic for them to use against the Wizard without any intra-conflict. 
  - The current implementation turns all crew into a free agent, which has caused some admin headache. Instead of mass-changing crew, the new solutions is that a small group of players will be made into a free agent at a low percent based chance each time the event fires off (and the event will fire off automatically instead of manually).
Which will considerably lower the amount of free agents it makes which in turn reduces admin headache.


- Fast Greenshift
  - One issue is that a Roundstart Wizard has the potential to turn the rest of the round into a greenshift if they died too fast. One option _could_ be to end the round instantly when they die,
    however that has its own issues when we move to dynamic. So it could be implmented as a temporary bandaid. 
  - Other missing features such as Wizard Apprentices (a much lower power wizard), summoning Slaughter Demons, and a Lich power
    could help the roundflow continue if the wizard was to die early -- if they decide to purchase extra help
  - Additionally if a Wizard dies too fast, another one could be called in immediately.


- Obsurdly Powerful
  - This is part in due to some unintended effects (Rod deleting people and things) and some overtuned abilities. Abilities and equipment are planned on being adjusted, while still remaining strong.
    A Wizard will absolutely be a glass cannon and there will be times that a player may be hit by an unfair choice (ex. polymorphed into something simple, gibbed) but that is the will of the game.


- Choice of Spells
  - The Wizard has a relatively low choice of spells and some are overtuned, which means that people will gravitate towards those choices. So more spells are on the way to address this.

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