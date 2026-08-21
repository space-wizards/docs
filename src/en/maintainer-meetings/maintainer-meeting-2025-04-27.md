# Maintainer Meeting (27 April 2025)

```admonish info

- Myra
- EmoGarbage
- Scar
- Orks
- Milon
- PJB
- Roomba
```

This meeting was recorded:

{% embed youtube id="j3H3XQpSR0M" loading="lazy" %}

## Game Audio Review (EmoGarbage)
The actual audio experience of playing the game has deteriorated to a level that's genuinely unplayable.

We need a few things:
- A comprehensive pass over basically all audio
- A freeze on new audio and sounds
    - Wouldn't a freeze paralyze most new additions? (Nik)
        - How many prs contain audio additions?
    - How long will it take?
        - A month ish
            - eeeeeeeeeeeeeeeeeeeeeeeeeeh>>>!>!?!?!?!
- Better standards for how we define audio
- Updated docs for contribs on what we expect
- Better requirements for PRs to ensure things are in order

<br>

- Ensure PR's with audio should have a video of the audio playing in context
- Tag prs with audio changes
- Discourse was mentioned
- Test would be nice but we dont know how to make em lol
    - About the clipping: Its a neat idea but is that a common problem we have?
    - Also this is more of a "wyci"

## Improving / updating breaking change annoucements. (EletroSR)
See discussion around https://discord.com/channels/310555209753690112/900426319433728030/1365121905765388309

- The problem
    - People dont post breaking changes to github
    - The standards for what is considered a "Breaking change" are low and makes it hard for downstreams to filter
        - Currently "List any breaking changes, including namespaces, public class/method/field changes, prototype renames; and provide instructions for fixing them"
- Proposed solution
    - Just post em on github, no pinging on discord. A fork can just view the github discussions.
        - or DISCOURSE!!!!!!
        - We can bikeshed later where we want it.
            - NVM apparently we decided already :godo: discourse it is.
                - We will set a relay in the codebase changes channel from the forum.
    - Stricter standards on what is condiered "breaking"
        - A simple file rename or protype move is not enough.
        - We can talk about what this entails later.

## Mapping Changelog (ArtisticRoomba)
- I have submitted a PR which adds a mapping changelog in its own separate tab. Now that I'm a head mapper I can kick this back up.
- The changelog is desired by players and mappers who contribute to the game, and last I checked it was desired internally as well.
- I'm not sure what else is required beyond the PR in order to properly implement it, so I'm asking here right now.

<br>

- Before i could write anything the infra side was done by pjb now
    - So yeah its funded. Ship it.

## RSI meta.json attributions are merge conflict bait and difficult to maintain (ArtisticRoomba)
- Contributors have started to load RSIs full of states with little atomization (see toys.rsi)
- Copyright attribution is a single line on the entire file, so multiple PRs targeting an RSI have to resolve conflicts merge after merge (see toys.rsi)
- This sometimes leads to things getting accidentally dropped or lost in a conflict
- Usually new contributors are experiencing these problems (sprite changes, new items, etc.) so it's an unnecessary hassle when we have to teach them how to un-mess-something-up.
- A PR to update the schema to enable multi-state attribution was made however it is not the correct solution
- It was proposed to do per-file (not per-state) attribution in the meta.json, using something RGA-like
- Why not just use RGA, so we can use one standard we've already made?
- RSIEdit needs to have support to easily process and generate this stuff.
- Someone else has to tackle this issue as I genuinely do not know how to code C# for actual programs.

<br>

- Need this to be reviewed by PJB [35302](https://github.com/space-wizards/space-station-14/pull/35302) and thats only it apparently. Roomba was not present to add anything else.

## The TEG meta needs to be killed with really big hammers (ArtisticRoomba)
- While I am the TEG's biggest fan (terminal CE main) I have concluded that the current state of the TEG (lack of game mechanics and restrictions for atmos regarding the TEG) is straight up counterproductive to the game's health
- Players are discouraged from running regular engines due to the TEG's comparative lack of danger, superior runtime, and lack of maintenance
- Elite atmosians oftentimes shut down new players from doing engines or a TEG design of their own because they already have built a hyperoptimized setup by the 5 minute mark
- This directly conflicts against SS14's core design pillars regarding _Player Agency_
- Pipe bursting, delta-P window shattering, and other core game mechanics would limit the TEG, however those do not exist right now.
- We can kill the TEG by re-inspecting the radiator math (currently large delta-Ts can be accomplished by just one radiator, which is unrealistic) and nerfing radiator's radiation to space accordingly
- We can alternatively kill the TEG by drastically reducing the efficiency.
- We can instead encourage Atmosians to focus on Carnot efficiency (encouraging a continuous, hot burn, which common mini burn chamber designs are difficult at doing efficiently). However I think focusing on the first point is enough.
- Supermatter Soon Patent Pending Trademark? It adds an actual element of danger, keeping it in-line with all other engines, while allowing for very in-depth tinkering (if more gasses are real TM)

<br>

- We all agree this is good for the game already, and its not worth to go in depth in a maintainer meeting about this topic.
    - So yes, we should kill teg meta.

## Stable review
- [35890](https://github.com/space-wizards/space-station-14/pull/35890) Decrease Syndicate raid suit size, add bundle backpack
- [36449](https://github.com/space-wizards/space-station-14/pull/36449) Add Aluminum Source (Cans)
- [36408](https://github.com/space-wizards/space-station-14/pull/36408) Wizard added in all at once!
- [36385](https://github.com/space-wizards/space-station-14/pull/36385) Descriptions for .25 caseless
- [36383](https://github.com/space-wizards/space-station-14/pull/36383) Descriptions for .45 magnum
- [36466](https://github.com/space-wizards/space-station-14/pull/36466) PlayerPanel Follow button
- [32227](https://github.com/space-wizards/space-station-14/pull/32227) Skirt of Life resprite + white shoes to paramedic loadout
- [36445](https://github.com/space-wizards/space-station-14/pull/36445) Departmental Economy
  - We should discuss the feedback we got from deltaV players
      - Essentially their concerns are fixed by [36944](https://github.com/space-wizards/space-station-14/pull/36944)
          - Could be cool if you could fax it if thats not already a feature.
          - Also means the clown cant just drain all of services money on toy boxes or something.
  - The cargo telepad needs to be nerfed as unlocking it trivializes gameplay (Roomba)
      - Everyone can basically make stuff appear in their department because they have the console
      - The cargo telepad is a holdover from an ancient state of SS14 where there was no ATS
      - Was moved to research as a tech
      - Unsure how it would even fit into current day SS14, it should probably be removed
      - The ATS needs to see discussion on how antagonists should interact with it (it can be killed pretty easily and cargo made unviable for the rest of the round)
      - See pull [34195](https://github.com/space-wizards/space-station-14/pull/34195)
          - The telepad should be removed when
              - The ATS console can't be destroyed by player grief. Or indestructible
              - Being able to just instantly bring items in is bad gameplay. And removes some intresting gameplay of flying and protecting the ATS.
- [36503](https://github.com/space-wizards/space-station-14/pull/36503) Neutralised anomaly infections drop inert cores
- [31648](https://github.com/space-wizards/space-station-14/pull/31648) Condensed gases can now be metabolized.
- [31814](https://github.com/space-wizards/space-station-14/pull/31814) Examining now shows Coords on Handheld GPS, Coord readout update frequency increased
- [32308](https://github.com/space-wizards/space-station-14/pull/32308) ID card computer bug fixed (And made it more fun!)
- [36394](https://github.com/space-wizards/space-station-14/pull/36394) Remove flash payload from stinger grenades
- [31533](https://github.com/space-wizards/space-station-14/pull/31533) New deathmatch map: DM01 Entryway
  - Do we even still support the deathmatch gamemode?
      - Yes
- [36338](https://github.com/space-wizards/space-station-14/pull/36338) Added a crate of shark plushies to cargo
- [35805](https://github.com/space-wizards/space-station-14/pull/35805) Adds 10% slowdown to syndicate commander hardsuit
    - Nukies are basically balanced 50/50 right now according to statistics so I don't really want to see any more nukie nerfs (Roomba)
- [35759](https://github.com/space-wizards/space-station-14/pull/35759) Binocular Neck Slots!
- [36532](https://github.com/space-wizards/space-station-14/pull/36532) Change colour tone of blue and green crayons
  - Might be worse for floor art? Why not just change the sprite color of the icon instead? (Slarti)
      - Maybe keep the blue but maybe match the green to something inbetween what it currently is.
- [36267](https://github.com/space-wizards/space-station-14/pull/36267) Fire extinguishers can now extinguish items, including when held/worn
- [35580](https://github.com/space-wizards/space-station-14/pull/35580) The long overdue downfall of stun meta - Stamina resists on Nukie & ERT Suits.
  - The title is misleading, this only adds it to ERT suits. Nukie armor was still in discussion. Having technical support for it is good. The commented out yaml code should be removed. (Slarti)
- [33548](https://github.com/space-wizards/space-station-14/pull/33548) Command to open chatbox in a new window
  - Didn't this break with the steam overlay? (Slarti)
      - It's not popped-out so shouldn't (Milon)
- [30703](https://github.com/space-wizards/space-station-14/pull/30703) Add SolutionContainerVisuals to the hypospray
- [36555](https://github.com/space-wizards/space-station-14/pull/36555) Add implant names to implanters
- [36511](https://github.com/space-wizards/space-station-14/pull/36511) update editorconfig docstring indentation
- [36562](https://github.com/space-wizards/space-station-14/pull/36562) Add the knock spell to the grimoire
- [35995](https://github.com/space-wizards/space-station-14/pull/35995) Remove deathrattle functionality from tracking implants
- [35889](https://github.com/space-wizards/space-station-14/pull/35889) Increase chest rig explosive resistance
- [36472](https://github.com/space-wizards/space-station-14/pull/36472) Now you can see if there's a beaker in the chemmaster
- [33370](https://github.com/space-wizards/space-station-14/pull/33370) 3mo xeno archeology (first phase)
- [36017](https://github.com/space-wizards/space-station-14/pull/36017) Inhand sprites for figurines
- [36225](https://github.com/space-wizards/space-station-14/pull/36225) Remove elite and juggernaut hardsuits from traitor uplink, add elite webvest
- [36604](https://github.com/space-wizards/space-station-14/pull/36604) XenoArch Rebalancing
- [36595](https://github.com/space-wizards/space-station-14/pull/36595) Restore Artifexium Effect
- [35752](https://github.com/space-wizards/space-station-14/pull/35752) New Experimental Science T3: Desynchronizer
- [36607](https://github.com/space-wizards/space-station-14/pull/36607) add bluespace flash effect
- [36609](https://github.com/space-wizards/space-station-14/pull/36609) Blueprint tweaks.
- [35359](https://github.com/space-wizards/space-station-14/pull/35359) Role subtypes
- [35447](https://github.com/space-wizards/space-station-14/pull/35447) New Arsenal T3: Temperature Gun Revitalization
- [36419](https://github.com/space-wizards/space-station-14/pull/36419) Basic Resources Crate
- [34959](https://github.com/space-wizards/space-station-14/pull/34959) Add chatty lathes
- [34955](https://github.com/space-wizards/space-station-14/pull/34955) New Sprites for cables
    - There's a [PR](https://github.com/space-wizards/space-station-14/pull/32822) that changes the cable orientation so they're visible in more situations (previously they were commonly obstructed)
    - This PR is more for accessibility (colorblindness) reasons. But the sprite could use some more improvements in my opinion. (Slarti)
- [36584](https://github.com/space-wizards/space-station-14/pull/36584) space adder sprite cleanup
- [35997](https://github.com/space-wizards/space-station-14/pull/35997) Standardize In-hand Sprites for Gloves
- [36640](https://github.com/space-wizards/space-station-14/pull/36640) add subtype to admin notice
- [34121](https://github.com/space-wizards/space-station-14/pull/34121) Added Junkeys
- [33327](https://github.com/space-wizards/space-station-14/pull/33327) Adds handheld artifact container to cargo orders
- [36630](https://github.com/space-wizards/space-station-14/pull/36630) Hydroponic trays can now be bought
- [32796](https://github.com/space-wizards/space-station-14/pull/32796) make borgs require prying to open instead of screwing
  - I'm not a fan of this change. This just needlessy changes controls and will be confusing to players with no benefit. All wirepanels in the game are opened with a screwdriver and the examination text says it is a wirepanel. The argument was that in SS13 there is a wirepanel inside a hatch that you have to open first. But it makes no sense to change this until we actually implement that feature. Can we make a poll for reverting this? (Slarti)
      - Just keep it
- [30463](https://github.com/space-wizards/space-station-14/pull/30463) Geiger counters can now be heard by everyone nearby
- [35590](https://github.com/space-wizards/space-station-14/pull/35590) Make tank harness smaller in inventories and craftable at lathes
- [36650](https://github.com/space-wizards/space-station-14/pull/36650) Add Solid Headband
- [34057](https://github.com/space-wizards/space-station-14/pull/34057) Banjo can now be worn on your back.
- [36656](https://github.com/space-wizards/space-station-14/pull/36656) random names for space dragons
- [36542](https://github.com/space-wizards/space-station-14/pull/36542) Allowing Cats to walk
- [36032](https://github.com/space-wizards/space-station-14/pull/36032) Contraband examine changes (again)
- [36209](https://github.com/space-wizards/space-station-14/pull/36209) Added the ability to refuel torches (and other expendable lights)
- [35170](https://github.com/space-wizards/space-station-14/pull/35170) Allow clown mime and borg customize names
- [36663](https://github.com/space-wizards/space-station-14/pull/36663) Add Experiment plushie
- [31754](https://github.com/space-wizards/space-station-14/pull/31754) Allow fire extinguishers and sprays to push grids you are standing on
- [36402](https://github.com/space-wizards/space-station-14/pull/36402) Removed the periodic table from the poster spawner
- [35594](https://github.com/space-wizards/space-station-14/pull/35594) reorganize security lathe recipes, add category filters
- [35913](https://github.com/space-wizards/space-station-14/pull/35913) Implement client-side theming for OutputPanel scroll-down button.
- [30812](https://github.com/space-wizards/space-station-14/pull/30812) setgamepreset command rework (take two)
- [36688](https://github.com/space-wizards/space-station-14/pull/36688) Slightly tweak base funding allocations.
- [34473](https://github.com/space-wizards/space-station-14/pull/34473) sec holobarrier charge increase
- [36579](https://github.com/space-wizards/space-station-14/pull/36579) Remove egg-plant from MegaSeed Servitor
- [36693](https://github.com/space-wizards/space-station-14/pull/36693) Increase base amount of egg in egg-plant
- [36382](https://github.com/space-wizards/space-station-14/pull/36382) Add inhand sprites for the drink shaker
- [36185](https://github.com/space-wizards/space-station-14/pull/36185) Update filing cabinet inventories
- [34627](https://github.com/space-wizards/space-station-14/pull/34627) Agent -> Corpsman
  - Isn't the name "Agent" a SS13 classic? (Slarti)
      - Why not just call it the nukie medic
          - It does not sound cool... but it should be that.
          - "Medic Delta" does not have the same punch as "Corpsman Delta"
- [32426](https://github.com/space-wizards/space-station-14/pull/32426) ciggie sounds
- [33872](https://github.com/space-wizards/space-station-14/pull/33872) extend hotbar hotkeys to 20 keys via shift
  - I think if you do need more than 10 actions something already went significally wrong with UI design. I guess it's ok to have this for forks? (Slarti)
      - There may be a bug where its not properly listed in the keybinds menu. Acording to PJB.
- [36126](https://github.com/space-wizards/space-station-14/pull/36126) New Speech Indicators for species that don't have any.
- [34223](https://github.com/space-wizards/space-station-14/pull/34223) Updated air scrubber and air vent sprites.
  - I'm not a fan of the sprites. They look like deadly blade traps. These sprites are some of the most common ones in the game, usually you see multiple of them on your screen at all times. However, since 95% of players never need to interact with them they should stay in the background, but the new sprites pop out too much. In addition the status lights are less visible than before. I left a more detailed comment on github. (Slarti)
  - I second this (Roomba), the sprites clash visually with the general enviornment of the game. They're supposed to blend in, given that there's a lot of them, but they are very noisy and stick out. It doesn't match the game at all.
  - I do not like the sprites either, I agree with the concerns raised above (Milon)
      - Vote if we should revert these or just touch them up a bit further.
          - Or touch up the old ones a little. Like making the fan in the vent finny slower.
          - Note this has a few accessibility issues right now currently.
- [36492](https://github.com/space-wizards/space-station-14/pull/36492) Local Material Silo
    - Players can still take the silo into maints and succ lathes dry if they want to troll security or cargo (Roomba)
        - Keep it running as is. Worst case scenario we act on it later on.
            - Lilten made a video already wow
- [34181](https://github.com/space-wizards/space-station-14/pull/34181) Change 'Irish slammer' to 'Grenade Penguin'
- [33338](https://github.com/space-wizards/space-station-14/pull/33338) Make artifact module actually useful.
- [36697](https://github.com/space-wizards/space-station-14/pull/36697) Resprited the Chief Engineer's mantle/manica
- [36287](https://github.com/space-wizards/space-station-14/pull/36287) New Drinks
- [32920](https://github.com/space-wizards/space-station-14/pull/32920) Add new color turtlenecks in WinterDrobe
    - We've granted so many exceptions to the clothing freeze that we are ending up with the problem we are trying to prevent. We should actually enforce our freezes. (Roomba, also yes I am a part of this problem)
        - Turtlenecks may be an issue for head identification
        - Emo wants a revert, we will put it up to vote
- [34878](https://github.com/space-wizards/space-station-14/pull/34878) Reduces handheld security radios range for picking people's messages up.
- [35165](https://github.com/space-wizards/space-station-14/pull/35165) Flippo Engraved Lighter is now in detective locker
- [34416](https://github.com/space-wizards/space-station-14/pull/34416) ERT Janitor Weapon - Hydra
    - This should just be accessible to Janitor somehow. (Roomba)
        - Yes
- [34769](https://github.com/space-wizards/space-station-14/pull/34769) Gave Bartender Pineapple Juice Cartons
- [35908](https://github.com/space-wizards/space-station-14/pull/35908) Removed collision from wall mounted lights and security cameras
- [34261](https://github.com/space-wizards/space-station-14/pull/34261) Removed Interior Shuttle Walls
- [36666](https://github.com/space-wizards/space-station-14/pull/36666) Rebalance and reduce playtime requirements for most roles.
- [33336](https://github.com/space-wizards/space-station-14/pull/33336) Give salvage borgs a tool module.
- [35446](https://github.com/space-wizards/space-station-14/pull/35446) Scarf Resprite
- [33219](https://github.com/space-wizards/space-station-14/pull/33219) Aquatic tail and back fin markings for lizards
- [36744](https://github.com/space-wizards/space-station-14/pull/36744) Plurality pin addition (now not on master branch)
    - Sir, the ten thousandth pin has hit the repo.
    - We need to either put a pause on this or the chamelon pin to solve this needs to be real
    - Milon was working on UI antibloat for loadouts (Roomba)
    - I support Milon's loadout changes. There is also another PR doing the same right now, we should compare which one looks better. (Slarti)
- [36085](https://github.com/space-wizards/space-station-14/pull/36085) Descriptions for .35 auto
- [35800](https://github.com/space-wizards/space-station-14/pull/35800) Makes more items recyclable.
    - The station should generally have more ways to gain materials independent from salvage (Roomba)
- [36061](https://github.com/space-wizards/space-station-14/pull/36061) Heterochromia for Moth
- [34292](https://github.com/space-wizards/space-station-14/pull/34292) Departmental shelves whitelist expansion (Attempt №3)
    - Why is this a whitelist to begin with? (Roomba)
        - Sure nuke the whitelist later on. This wont block stable
            - Should also check other whitelists later on. 
- [36767](https://github.com/space-wizards/space-station-14/pull/36767) Decrease amount of mail, increase profits
- [34949](https://github.com/space-wizards/space-station-14/pull/34949) Fire protection for ERT engineering hardsuit
- [35808](https://github.com/space-wizards/space-station-14/pull/35808) Nonlethal throwables crate
- [36070](https://github.com/space-wizards/space-station-14/pull/36070) The Beverage Jug Can Now Look Open
- [35986](https://github.com/space-wizards/space-station-14/pull/35986) Pirate Gear Tweaks.
- [35685](https://github.com/space-wizards/space-station-14/pull/35685) Resprite main altars
- [32946](https://github.com/space-wizards/space-station-14/pull/32946) Adds beanies to the WinterDrobe!
    - Another example of the exceptions we've been making to the clothing freeze (Roomba)
- [36510](https://github.com/space-wizards/space-station-14/pull/36510) Santa hat with a foldable beard
- [34065](https://github.com/space-wizards/space-station-14/pull/34065) The Bartender can now make Eggnog
- [35825](https://github.com/space-wizards/space-station-14/pull/35825) Require traitors to maroon their objective no matter what
  - This one is causing [critical bugs](https://github.com/space-wizards/space-station-14/issues/36902) with greentext. (Slarti)
      - Revert or hotfix ASAP
- [35732](https://github.com/space-wizards/space-station-14/pull/35732) Wizard Headset
- [35713](https://github.com/space-wizards/space-station-14/pull/35713) Reorder electronics recipe file, add filter categories
- [36774](https://github.com/space-wizards/space-station-14/pull/36774) Reworked Mail Spawning
- [36704](https://github.com/space-wizards/space-station-14/pull/36704) Add RGA/RSI to Credits
  - The way it is currently implemented this is a giant wall of text no one will ever look at. It simply copies the copyright line for every single rsi. Causes lag when opened. And sloth mentioned credits still need to be updated manually, is that correct? (Slarti)
      - How bad is the lag?
          - Half a second when you open the tab
              - Could be worse, the open source licenses do this too.
- [32847](https://github.com/space-wizards/space-station-14/pull/32847) Add the medical HUDs to medical's loadouts (except chem)
- [34586](https://github.com/space-wizards/space-station-14/pull/34586) Add rehydratable mop bucket cube, refactor the rehydratable yml
- [36531](https://github.com/space-wizards/space-station-14/pull/36531) Increase thief to player ratio
- [35854](https://github.com/space-wizards/space-station-14/pull/35854) Added a semi-functional genderfluid pin.
- [36801](https://github.com/space-wizards/space-station-14/pull/36801) Station AI Name Identifier
- [28339](https://github.com/space-wizards/space-station-14/pull/28339) Firelock temperature and pressure warning lights
  - Causes [visual bugs](https://github.com/space-wizards/space-station-14/issues/36889) (Slarti)
      - Minor bug fix. All good
- [29949](https://github.com/space-wizards/space-station-14/pull/29949) Bots overhaul
- [30212](https://github.com/space-wizards/space-station-14/pull/30212) Tweak Security protection values
- [34579](https://github.com/space-wizards/space-station-14/pull/34579) Metal foam grenade rework, small tweaks to grenade timers
    - I (roomba) have plans for making metal foam grenades more powerful for Atmospherics, so I don't consider the changes made to foam grenades here permanent
- [36811](https://github.com/space-wizards/space-station-14/pull/36811) dragons can now pry doors
- [36790](https://github.com/space-wizards/space-station-14/pull/36790) Make funding allocation computer more configurable
- [31864](https://github.com/space-wizards/space-station-14/pull/31864) Fingerprint taking improvements
- [32103](https://github.com/space-wizards/space-station-14/pull/32103) Command uniform
- [32375](https://github.com/space-wizards/space-station-14/pull/32375) downprice many cargo orders
- [36825](https://github.com/space-wizards/space-station-14/pull/36825) Cherry Pick Round-start Solar Variation
- [33469](https://github.com/space-wizards/space-station-14/pull/33469) Nerf Firelock electronic prices
- [36842](https://github.com/space-wizards/space-station-14/pull/36842) Give Admins "Tails"
- [34517](https://github.com/space-wizards/space-station-14/pull/34517) Moth-pockets
- [33286](https://github.com/space-wizards/space-station-14/pull/33286) Four new food crates for the ATS
- [36846](https://github.com/space-wizards/space-station-14/pull/36846) Add 1 dragon name
- [33443](https://github.com/space-wizards/space-station-14/pull/33443) Remove steel sheet hull fixing
    - Engi Guidebook needs to be updated to reflect this (Roomba)
        - Not a blocker but should be done
- [36857](https://github.com/space-wizards/space-station-14/pull/36857) pAI Software Catalog
    - Any other ideas for this? Is the starting amount of money too much? (Beck)
        - Not a topic for the meeting
- [34199](https://github.com/space-wizards/space-station-14/pull/34199) Make toy sword less obvious
- [35361](https://github.com/space-wizards/space-station-14/pull/35361) Adds shorts/pants to ClothesMate vending machine
- [35609](https://github.com/space-wizards/space-station-14/pull/35609) Moths can eat pills
- [36830](https://github.com/space-wizards/space-station-14/pull/36830) Xenoborgs part 1
- [31015](https://github.com/space-wizards/space-station-14/pull/31015) Put items inside cakes!
- [35915](https://github.com/space-wizards/space-station-14/pull/35915) Removed syndicate surgery duffel, added advanced circular saw to Medical Doctor uplink.
- [36135](https://github.com/space-wizards/space-station-14/pull/36135) Cotton Grilled Cheese Sandwich
- [34896](https://github.com/space-wizards/space-station-14/pull/34896) Meat Patty
- [36313](https://github.com/space-wizards/space-station-14/pull/36313) Turnstiles
    - Is conga line fixed? Is it a feature? (Beck)
        - Let it run out and otherwise patch it out.
- [36392](https://github.com/space-wizards/space-station-14/pull/36392) Genpop Closets & IDs
- [36815](https://github.com/space-wizards/space-station-14/pull/36815) Tearable Deliveries V2
- [36897](https://github.com/space-wizards/space-station-14/pull/36897) Disable shadows for observer pointlight



### Worth bringing up
- [36424](https://github.com/space-wizards/space-station-14/pull/36424)  Wizard Teleport Scroll (Teleport Location ECS)
    - "we really need to get this PR in for this because it's a huge wizard balance (hide in space wizard is extremely bad)"
- [36809](https://github.com/space-wizards/space-station-14/pull/36809) Clear MIDI masters properly to avoid replay freezes ~~Already merged~~ It was merged on MASTER not good.
    - Important bug fix for replays
        - Cherrypick it to staging
- [35825](https://github.com/space-wizards/space-station-14/pull/35825) reportedly has issues 
    - Look at [this issue](https://github.com/space-wizards/space-station-14/issues/36902)
        - We agreed on it above in the stable merge
- Engine upgrade to bring [RT-5887](https://github.com/space-wizards/RobustToolbox/pull/5887) Fix grid fixtures using locale dependent ids
    - This fixes a long standing issue where some players suddenly get a black screen! Very important
- [SS14-ISSUE-36920](https://github.com/space-wizards/space-station-14/issues/36920) Maroon traitor objective should have more obvious naming
    - "Maroon" is a wierd word not many people know, especially now with 35825
        - However fixes the objectives should fix this too, but not a blocker.
- [36936](https://github.com/space-wizards/space-station-14/pull/36936) another important bugfix that should be hotfixed soon
    - Someone plz review it 
- [36927](https://github.com/space-wizards/space-station-14/issues/36927) Janiborg soap can be depleted to gain a handslot
    - I don't know how to fix it (I was really tired), tried fixing it already. Event isn't being fired on the soap properly when handled by a borg.
    - Should probably be nuked in the meantime otherwise every janiborg can get a free handslot very easily
- [36943](https://github.com/space-wizards/space-station-14/issues/36943) SpillTileReaction stopped working
    - Stuff like foam no longer works
- [36925](https://github.com/space-wizards/space-station-14/issues/36925) The entire game world reloads if you snip a machine's manager wire
    - This was also happening to other things but I genuinely forgot what it was happening to (Roomba)
- Please someone save me from the `GameRuleComponent` heisentest
    - ![gamerulecomponent.png](../assets/images/maintainer-meetings/2025-04-27/gamerulecomponent.png)
- [36955](https://github.com/space-wizards/space-station-14/pull/36955) has been merged into master and needs to be cherry picked into staging/stable. Currently emags and some wizard staffs have infinite charges.
    - Hotfix to staging
