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

This is a design document for The Wizard antagonist - a highly disruptive/chaotic antagonist that does anything to their whim.

A lot about the Wizard's design philosophy can be summed up in that it doesn't conform to the standard rules of the game; very much the embodiment of "a wizard did it".
Players are encouraged to come up with their own gimmick using the many powers at the Wizard's disposal, while still being an antagonist to the station through the ensuing chaos.

## Background

<!--
Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game.

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.
-->
```admonish info
As of the writing of this document, the Wizard has already been in the game for several months, during which it was moved from being a roundstart antagonist and sub-gamerule into being a purely mid-round antagonist due to some design issues that this document intends to address. Even with this, it should feature as a comprehensive guide to the whole of the Wizard's design and its philosophy, for contributors to reference in future developments of the role.
```

The Wizard's existence is a culmination of the chaotic and goofy nature of the game, and has existed as an implementation in SS13 for over a decade. It's an extremely rare, high-chaos, high-impact, and highly disruptive solo antagonist. 

A Wizard's general goal is to "show off" their magical talent to the station. They have spells and magical items that they can purchase to help them with this goal. Compared to other antagonists they're relatively powerful due to not only the rarity of the gamemode justifying their potency, but also the nature of the Wizard being a "glass cannon" in terms of strengths and weaknesses.
This allows Wizards to be given powerful spells and some with reality-warping effects (like animating tons of objects, changing walls into doors, making the floor lava, etc) that would be seen as overpowered in the hands of other more common antagonists, such as Traitor or Nukies. See the Spells/Equipment section for a breakdown.

### SS13 History
The Wizard is a port of the longstanding SS13 antagonist of the same name. Mainly it's based off of it's /tg/ server derivatives, but it's intended to incorporate aspects of multiple codebase implementations and be a celebration of all things magic from SS13.
The Wizard was added relatively early in SS13's history, sometime between 2008-2011. By comparison Nukies and Revolutionaries were added sometime in 2004-2005. 
The /tg/ (and also Goon) implementation is a high-chaos lone antagonist. Sometime in their lore they were sent from the Space Wizards Federation to go mess with the station for some petty reason, or just for fun.

Generally their main goal was relatively freeform - teach the station a lesson they'll never forget. And they may have had some objectives mixed in, similar to that of Traitors, but more open-ended (eg. Take over the station, Kill X, Do Y to Z amount of crew, etc).

### SS13 Issues
One of the issues that some servers faced was that the spell upgrades fell somewhat flat; mostly they were just cooldown reductions. Now not every spell's going to need an upgrade, but one thing to strive for in SS14 will be meaningful spell upgrades that affect how the Wizard plays and helps with the gimmick the Wizard player is trying to perform.

Another issue was anti-magic. A relatively lazy way to counter Wizards (and other magic-based antagonists) was the introduction of null rods and holy melons. At their conception they 100% shut down magic and while some adjustments were made to be more fair, the inclusion of anti-magic changed per server due to its nature of being too much of a hard counter. This also gave the Chaplain (and Botany) too much focus on a handful of game modes, which they ended up as departments you as Wizard had to permakill ASAP.

As with SS14's first iteration, a Wizard being a friendly antagonist was also an issue in SS13. Even with Traitor-like objectives, it didn't stop Wizards from joining up with the station for no good reason. See Friendly Wizards later on in this doc for the exact definition and how it is being solved.

## Features to be added

<!-- Give a description of what game mechanics you would like to add or change. This should be a general overview, with enough details on critical design points that someone can directly implement the feature from this design document. Exact numbers for game balance however are not necessary, as these can be adjusted later either during development or after it has been implemented, but mention *what* will have to be balanced and what needs to be considered when doing so. -->

At the time of writing this document, Wizard exists in the game as a mid-round ghostrole antag. Its spell list is limited to some projectiles, very few event spells, teleportation spells, and a few different rods and staves, with some variation but not enough to embody a full roundstart or sub-gamemode antagonist, which it is intended to work as.

The plan is to overall add more spells that better help enable more creativity for the Wizard and/or increase how all-encompassing its impact is on the round. For this, the following backend mechanics are necessary:

The main feature necessary for the Wizard's development is an advanced targeting and spawning system, to make it easier for contributors to add new spells with various creative effects. Custom logic won't be avoided, but there can be a point where a lot of boilerplate is cut down. Example features of such a system would be:
- Target a certain set of tiles in front of the user, e.g. something like a force wall.
- Target all sentient entities in sight.
- Target the Wizard directly, or target the tile the Wizard is on.
- Target all sentient entities on the station.

Event spells especially would benefit from being gamerules, to make use of that system for role distribution and end-screen information.

### Wizard's Grimoire and Wizcoin breakdown

The main a Wizard gains these various effects and equipment is through the Wizard's Grimoire; effectively an uplink using a unique currency called Wizcoin. The cost of things should be such that the Wizard has to be mindful of what they purchase and leave certain spells on the table. 

Generally the higher the cost of a spell/item the more impact it has. That being said, some spells are planned on being upgradeable so they may cost 3 at base price, but further purchases of the spell (at the same or lower cost) may give you stronger effects. If the Wizard has access to 10 wizcoins:
- 1 Cost - Relatively low risk low reward (something like teleport spells, smoke, etc).
- 2 Cost - Standard. Higher power or unique utility.
- 3 Cost - Powerful. May have a lot of power (instant gibbing) or a profound effect (summoning guns)
- 4 Cost and above - Should be reserved for something that's 100% dominating because this is 40% of your budget.

### Spell/Equipment breakdown

As a glass cannon antagonist, not all spells are going to be straightforward, and part of navigating SS14's chaos is understanding the limitations certain mechanics put on you. If you try to fireball someone in the face, you're going to die too unless you put some distance. 

Some spells having drawbacks (long cooldown, dangerous to use up close, long after-effect, hard to control, a Slaughter Demon not being your friend, etc) makes more interesting conflict and allows for a range of skill expression, as long as safer alternatives are also supported.

Some magic may be locked to using an item, which means you'd need to risk losing the item or also buy a recharge spell to compensate. A Wizard being slipped just to have their equipment used against them is a classic moment from SS13.
And it's even funnier when the Wizard yoinks it right back with a different spell!

Or some magic may require robes, which means you'll be unprotected in terms of traditional armor, being the definition of a glass cannon. This is generally reserved for some of the most powerful spells.

Most of this is based on vibes and themeatics. Does it make much sense for a Wizard to shoot lockers out of their hands? Might be a bit funny conceptually, but it makes more "sense" that some piece of equipment is doing it instead.

### Spells (Actions)

The Wizard's bread and butter, inherent to the Wizard's mind. Without these, you're just an old grandpa who's about to become intimately familiar with the concept of a skull fracture. These can be a wide variety of execution and power.

- Execution examples:
    - Projectile, touch, event, area-effecting.
- Categories:
  - Offensive:
    - Any spell that excels at damage, destruction, killing, or restraining.
    - Generally spells you use to charge in.
    - Examples:
      - Fireball (explosion)
      - Rod Polymorph (piercing/knockdown)
      - El Nath (instant gib)
      - Mindswap (swaps the wizard's mind with another player)
  - Defensive:
    - Any spell that's good at area control.
    - Examples:
      - Force Wall (3x1 hallway control)
      - Smoke (drops a smoke screen, which could cause people to cough & drop weapons)
      - Trap Runes (summon trap runes to stun/slow down anyone who steps on them)
      - Jaunt (temporary ghost, limited movement through walls)
  - Utility/Support:
    - Any spell that can support the Wizard in some way.
    - Could help with escape, could be some sort of trickery, or maybe an ally.
    - Examples:
      - Void's Applause (swaps you and another person)
      - Knock (opens & unlocks all doors and locks in the area)
      - Wizard Apprentice Scroll (can summon a wizard apprentice with preset spells)
      - Recall (mark and recall an item)
  - Event:
    - Reality-bending spells that affect everyone in the world, whether it be station crew, invading Nukies and even the Wizard themself.
    - Examples:
      - A spell that forces tile movement to all in sight.
      - Summon Ghosts (a spell that allows ghosts to be seen)
      - Summon Guns/Magic (a spell that gives all living people guns or magical items, while also sowing chaos by making some crewmembers into antagonists)
      - A spell that makes the floor into lava for a short period.
    - See the Event section below for a better breakdown.
- Power examples:
  - Summoning smoke which creates a thick smokescreen, and causing people to cough which forces item drop (themself included)
  - Shooting a fireball and blowing people up in an area of effect
  - Touching someone and they get knocked back.
  - An event trigger that temporary makes the floor lava.

#### Event Spells

The defining feature of an Event Spell is that it affects everyone on the station. The effect itself should ideally be on either end of the power spectrum; cosmetic and "for fun", or highly disruptive through the chaos it causes. The latter type of event spell should be a high investment for the Wizard, and therefore encourage chaos such that the Wizard can revel in it on the station.

The motivation for cosmetic event spells is that they allow for some unique flavor and fun without being considered a major investment, contributing to the silly side of the Wizard's design. Since they affect all players they can also work as a fine way to herald the Wizard's arrival without taking resources the Wizard would've wanted to put towards other things.

Examples: 
- Summon Ghosts - This could both help and hurt the wizard or other antagonists, or the ghosts can just mess with the crew and put them on a wild goose chase.
- Forcing Tile Movement (temporary) - The concept of being forced to move from one tile to the next like the days of old is hilarious, and gives players a small taste of what the predecessor to SS14 was like.

The motivation for disruptive event spells is that they throw the station into mass-chaos, an aspect where SS14 shines thanks to its immersive sim gameplay and the limited confined area being on a space station provides. Since highly disruptive spells are just that, it's key that they are designed in such a way to:
- Not feel repetitive and lead to the same types of gameplay loops every time they are spawned.
- In the instance where equipment/powers are given out, some players are turned into antagonists.
  - This is so it's not a huge net positive for the crew and a net negative for other antagonists, and to encourage chaos permitted under server rules.
- Antagonists have the same amount of chance to get this equipment as much as the crew does, so it evens out.

Examples:
- Summon Guns/Magic - Two spells with similar base functionality but way different flavors. Summom Guns gives every player one of the many guns in the game, possibly terrible, possibly overpowered. Summon Magic gives every player a random wand or staff. As some of the crew turn into antagonists with the explicit goal to cause chaos, the remaining non-antagonist crew will have to subdue the new antagonists with their new equipment, with all the collateral and misunderstanding that may happen as a result.

### Equipment Spells

Anything that is not inherent to the Wizard's mind, i.e. an item in the world. As they are not inherently available to the Wizard, they should be slightly stronger than regular spells on average.

#### Wands

- Like spells they can have a variety of effects. Never event-level effects, but can otherwise draw from the pool of spell effects.
- Wands are defined by having limited by charges that once depleted stay depleted.
  - Because of this, they tend to be on the more powerful end of the spell spectrum.
- Can be given to allies to help assist you.
- Also meant to be used as combo pieces with other Spells or Equipment.
- Examples:
  - A wand of animation that turns inanimate objects into strong mobs hostile to your enemies.
  - A wand that turns someone into a horrifying "cluwne" abomination and can only be reverted in death.
  - Polymorphing your PAI or Wizard Apprentices

#### Staves

- Similar to Wands, Staves can have a variety of effects but nothing as powerful as event-level. 
- Staves are also limited by charges, but they are unique to wands by being self-recharging.
  - Because of this, they should be considered weaker than Wands. This should reinforce them being combo pieces with other Spells or Equipment
- Can also be given to allies to help assist you.
- Examples:
  - A staff that turns walls into doors.
  - A staff that polymorphs someone into bread, which can be eaten to free them.
  - A staff that fires a random bolt of magic

#### Other Equipment

- This is for a variety of equipment that doesn't fit into the above three categories, often used for effects that don't involve targetting or have other unique properties.
- Examples:
  - An orb of scrying to turn yourself into a ghost (temporarily) to observe others.
  - An orb of pondering to look at the stations cameras.
  - A deck of cards to give yourself a Holoparasite/Guardian.
  - A magical contract to summon a predefined Wizard Apprentice.
  - A magical item that summons a Slaughter Demon.
  - A hammer that pulls everyone and everything towards you.
  - A hammer that stuns and also knocks people away.

### The Wizard's Den

Hey, it's our server's namesake!

The Wizard's Den is the spawning location for the Wizard and acts as a staging location before teleporting to the station. Some of the Wizard's equipment can be found in the Den, along with some opportunities to practice certain spells. 

It's important that the Wizard is not encouraged to just stay in their Den for the round - the Den is made for leaving. Other players (other than those the Wizard may have summoned, such as an Apprentice) should not have access to the Den and the Wizard shouldn't be able to return to it once they have left it.

## Game Design Rationale

<!--
Consider addressing:
- How does the feature align with our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosphy?
- What makes this feature enjoyable or rewarding for players?
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- How does it enhance player cooperation, competition, or emergent gameplay?
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?
-->

One of the unique things about the Wizard is that by its existence it does potentially violate some of the antagonist pillars, but that's intended!

[Antagonist design pillars](https://docs.spacestation14.com/en/space-station-14/round-flow/antagonists.html) that it has a unique behavior to:

- Just a Spark
  - Wizards are 100% meant to disrupt a round; they are a major force of chaos after all.
  - That being said, when a Wizard's effects come in contact with crew and/or antagonists, this can cause unique situations and spark interaction. E.g. By giving the entire living playerbase guns or magic, it could help tip the scales in a crew vs nukie fight.

- Escalation
  - As above, a Wizard is like Nukies and have very strong potential right off the bat. This is so they can combine spells in a unique and creative way to make a more interesting round.
  - The Wizard may find itself using station gear to negate some downsides (such as armor, magboots to counter slipping, healing supplies) but this is limited by what can be obtained from the station and may in some cases (such as armor inhibiting the use of spells) limit the Wizard's innate powers.

- Discoverability
  - The Wizard is generally not a "quiet" antagonist, though there may be spells that allow a Wizard to specialize in deception (e.g. Mindswap). Spells are as a rule loud and noticeable, and with the announcement console in the Wizard's den they are even more discoverable.
  - The Wizard has relatively low armor and healing access, easy to slip, and no unique stun or stamina resistance. It's very much the definition of a glass cannon, so counterplay comes from catch the wizard during cooldowns or off-guard. 

Despite it potentially violating some antagonist pillars, it does help highlight the [core design principles](https://docs.spacestation14.com/en/space-station-14/core-design.html) of the game, mainly:

- Chaotic
  - The Wizard is the embodiment of this pillar. You know you're in for a wild ride when a wizard is around. The potential they have for introducing chaos is pretty high. By being able to shift reality, the choices are basically as creative as the contributors can get. This chaos is primarily felt if a player directly engages with the Wizard and can therefore be mitigated by trying to avoid and stay far away from the Wizard's sphere of influence. 
  - Spells can have a wide range of abilities, using weaponizing different features and game mechanics across the codebase. By combining them through freeform selection the wizard is able to have these features interact in emergent gameplay with wildly unexpected or rare results. The creativity of the wizard player is the tool that drives the round.
  - It can get old doing the same old thing all the other wizards are doing. Trying out new and creative combination can really spice up the round!
- Seriously Silly
  - There's almost nothing more unhinged than a Wizard and their antics. A well timed fireball or a smite may end up being hilarious in a story told later.
  - The spells themselves are designed to be inherently silly; the Summon Guns spell including water pistols is silly on its own, but becomes something serious when squared up against another person getting a powerful laser gun.

The world is your oyster, you're literally a wizard in space.

## Roundflow & Player interaction

<!--
Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
- Which department will interact with the feature? How does the feature fit into the [design document](../space-station-14/departments.md) for that department?
-->

The Wizard is a _rare_ antagonist, but one that could show up absolutely **anywhere**. They're meant to be unfairly strong and weave chaos into any roundtype.
And because of this they should never be common. Maybe they should be seen only a few times a day across a server, if not less. They should be available as a roundstart antagonist and as a mid-round, making their inclusion into a round a random surprise for when it may take. A roundstart Wizard may end up shaping the entirety of the round, while a late mid-round could intensify the existing chaos to a new level for crew.

Many of the Wizard's spells should have some back-and-forth in terms of player agency and interaction. For example, they could have a wand of polymorph which will turn a player into a random creature. That player would still have their own agency but also the positive (or negative) attributes with becoming the creature. The wand could easily backfire on the wizard and the other player could be turned into something fearsome, like a syndicate borg.

The Wizard being quite strong should be limited by the amount of spells they can buy. The ideal situation is to _avoid_ making "the game winning build" but instead allowing the creativeness of the player to mix and match different spell & equipment combinations to make something interesting. While there may be some classic combinations (such as a timestop and fireball spell), giving players way more interesting options will help cut down on pure offensive Wizards.

### Friendly Wizards

A **friendly wizard** is a wizard who will either refuse to use spells on crew OR will help out the station against other threats without an iron-clad reason.

An iron-clad reason would be something like Nukies relentlessly pursuing the Wizard, or a conversion antagonist attempting to convert the Wizard. In no other circumstances should a Wizard act friendly towards the crew.

A Wizard forcibly taking over the station, whether it's through actual force, mind-swapping or threats, is not a friendly wizard. On the same coin, a wizard not killing a person every second is also not a friendly wizard: **As long as a wizard is using their spells in some way that effects the station, they're not friendly.**

Like any friendly antag, an antag just joining up with the station with zero reason isn't fun for anyone. But an iron-clad reason as stated above helps make rounds more interesting and memorable.

To discourage friendly Wizards, they should be given simple objectives to help guide them into antagonizing the station:
- Number of Spells Cast:
  - A simple track of how many spells were cast could help. This would also include events triggered and wands fired.
- Flavor Objectives:
  - A collection of random flavor objectives could also help - like having a hostile takeover of a certain department (or disrupt that department)
- Optional Challenge Buy:
  - To give people more of a set of structured objectives, and an alternative way to end the round, an optional challenge buy can be introduced.
  - This would give the wizard tasks to complete so they can get more wizcoins to become more powerful and eventually trigger some sort of end of round.

There are some types of objectives to avoid:
- Copying Traitor/Ninja objectives (Kill X, Sabotage Y)
  - This would make Wizards feel like they need to take specific spells to complete those tasks, instead of supporting player creativity.
- Making the Challenge Buy the main mode:
  - Turning all antags into a progressive power-scaling mode kills identity and makes them too samey.
- Flavor Objectives requiring certain spells
  - Having objectives like "polymorph X crew" would also force the wizard to buy specific spells.

### Hiding in Base/Space (Beginning of Round Stalling)

Some Wizards may hide in their den or in space and do nothing but event spells. This isn't good because while the event spells may have some sort of large impact on the round, the wizard themselves are effectively removing themselves from it.
- Event spells
  - The plan to prevent Wizards from sitting back and firing off events is that the event trigger will also automatically detect if the Wizard is either on a space tile (a certain distance away from the station) or not on the station grid. If any of those are true, there should be a mechanic to automatically teleport the wizard back onto the station.
- Spacing Protection
  - This mostly applies to Hardsuits or Softsuits of some sort. While some spells necessitate wearing the Wizard's robes to even work (marking you as valid), others could discourage spacing by giving double cooldowns for Wizards wearing spacing protection.

### Polymorphs

Being polymorphed by a Wizard does **not** convert you to their team, no matter the result of the polymorph! The only exception is if you were already on the Wizard's team to begin with (ex. Wizard Apprentice).

### End State

The Wizard game mode does not have a natural end state generally, as the antagonist is mainly encouraged to come up with some gimmick to terrorize the station enough for them to call the shuttle.

In part, a shuttle should be automatically called if a majority % of crew are dead regardless of game mode. The shuttle would be unrecallable so people cannot stall out the round.

As stated earlier in this document, an optional buy-in to do objectives up to a round-end state coould also be implemented to give people who are less than creative some end goal to work towards while also getting bonuses along the way.

## Administrative & Server Rule Impact (if applicable)

<!--
- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
- How are the rules enforced mechanically by way the feature will be implemented?
-->

The Chaos the Wizard brings may introduce challenges to the admin team.
Furthermore, some optional challenge purchases may be introduced to give the wizard more drive. So people who aren't as creative, but crave a challenge, will have some guidance on what to do which may reduce friendly wizards. 

### Issues with previous SS14 iterations

These were issues identified with the previous SS14 implementation of the Wizard antagonist, and how this design document proposes solving them:

- Event Spells
  - These are spells like Summon Guns or Magic - which turns everyone into a free agent. This was added initially because it would be too much of a net positive for the crew to get a bunch of guns and magic for them to use against the Wizard without any intra-conflict. 
  - The previous implementation turned all crew into a free agent, which caused some admin headache as Free Agents aren't meant to become murderhobos, yet were given equipment to do so. Instead of mass-changing crew, the new implementation is that a small group of players will be made into a antagonists at a low percent based chance each time the event fires off (and the event will fire off automatically instead of manually). By making them strict antagonists it should both make the lines clearer for players and admins alike.

- Fast Greenshift
  - One issue was that a Roundstart Wizard had the potential to turn the rest of the round into a greenshift if they died too fast. One option _could_ be to end the round instantly when they die, however that has its own issues when we move to dynamic. So while it could be implemented as a temporary band-aid, another option could be that if a Wizard dies too fast, another one could be called in immediately.
  - Other missing features such as Wizard Apprentices (a much lower power wizard), summoning Slaughter Demons, and a Lich power could help the roundflow continue if the wizard was to die early -- if they decide to purchase the extra help. 

- Absurdly Powerful
  - This is part in due to some unintended effects (rod deleting people and things) and some overtuned abilities. Abilities and equipment are planned on being adjusted, while still remaining strong. A Wizard is absolutely meant be a glass cannon which confers disadvantages. There will be times that a player may be hit by an unfair choice (ex. polymorphed into something simple, gibbed), but that is the will of the game, and should such moments occur they should come at a high opportunity cost for the Wizard.

- Choice of Spells
  - The Wizard has a relatively low choice of spells and some are overtuned, which means that people will gravitate towards those choices, resulting in repetitive rounds leading to player dissatisfaction. So more spells are on the way to address this.

# Technical Considerations

<!--
- Are there any anticipated performance impacts?
- Does the feature require new systems, UI elements, or refactors of existing ones?
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
-->

Since Wizard's been out there for some time, there are likely some refactors that need to happen to get Wizard fully back in. Those include (but aren't limited to):
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
