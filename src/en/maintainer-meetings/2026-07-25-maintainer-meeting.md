# 2026-07-25 Maintainer Meeting

:::info
## Maintainers In Attendance

* ScarKy0
* SlamBamActionman
* Princess
* Ada
* Errant
* Jezithyr
* Samuka
* ArtisticRoomba
* Julian
* Ress
* Hyphenation

:::

(Meeting recording goes here)

# Topics

Comment from Slarti: I really recommend moving any topics to the next meeting unless you want a 6 hour meeting. The PR list is already way too long. And we might have to consider switching back to biweekly stable releases if the merge rate stays this high.

## Trimming Map max pop (Slam)

* This has been pretty extensively discussed, with proposals to lower it to 60-70 pop. Head mappers want this very strongly to make the maps cater better to players.
* A main concern was AFK players sticking around, but that is resolved with PR [44353](https://github.com/space-wizards/space-station-14/pull/44353). 
  * I don’t know the actual ingame effects of the AFK kicking, would love to hear from admins if they noticed any difference.
* We have all our game servers back up (+1 more!) and we have space left over; there is room for reduction without kicking players off Wizden.

# Release Blockers

* Pipe Layering Broken(?)
  * <https://github.com/space-wizards/space-station-14/pull/44637> PR that broke it
  * <https://github.com/space-wizards/space-station-14/pull/44886> PR that fixes it
    * the robot vacuum is angy
    * Merged before the meeting
    * **The issue still exitst! Though now it only happens if you try to construct a radiator over an existing vent. Trying to construct a vent over a radiator, or anchoring either of them over the other one, is prevented.**
* Destruction Thresholds need rebalancing. 1 C4 can’t get through 1 Reinforced wall at the moment which is cringe. 
  * <https://github.com/space-wizards/space-station-14/pull/44755> 
  * ~~Alternatively we could revert~~ [~~https://github.com/space-wizards/space-station-14/pull/40090~~](https://github.com/space-wizards/space-station-14/pull/40090) ~~and then re-merge it later, but I think it got built on top of already.~~
    * ~~Quick Revert~~ then merge into master
    * Same for Parenting PR!
    * 40090 was now reverted by <https://github.com/space-wizards/space-station-14/pull/44924>
* Changelog project to actually get an ingame changelog
  * <https://github.com/space-wizards/space-station-14/pull/44771>
    * Infra issue, want to use a C# app for changelog
* ~~Windoors not able to close properly; common frustration for players right now~~
  * [~~https://github.com/space-wizards/space-station-14/pull/44081~~](https://github.com/space-wizards/space-station-14/pull/44081)
    * Merged
    * Seems fixed, though windoors still work a bit odd. if a windoor is built/placed flush against a wall ((which would probably never happen normally, as there is no point to do this)) they will be able to open, but not close.
* ~~Borgs can hold anything~~
  * [~~https://github.com/space-wizards/space-station-14/pull/44863~~](https://github.com/space-wizards/space-station-14/pull/44863)
    * ~~Revert~~ [~~https://github.com/space-wizards/space-station-14/pull/42439~~](https://github.com/space-wizards/space-station-14/pull/42439) ~~instead~~
    * Reverted by <https://github.com/space-wizards/space-station-14/pull/44924>
* ~~Some UIs Broken (Engine)~~
  * [~~https://github.com/space-wizards/space-station-14/issues/44758~~](https://github.com/space-wizards/space-station-14/issues/44758)
  * ~~We need to merge~~ [~~v283.1.2~~](https://github.com/space-wizards/RobustToolbox/releases/tag/v283.1.2) ~~into staging!~~
    * ~~Princess will make a PR for this :)~~
    * Merged <https://github.com/space-wizards/space-station-14/pull/44923> and <https://github.com/space-wizards/space-station-14/pull/44927>
* ~~Up AFK Time Limit~~
  * [~~github.com/space-wizards/space-station-14/pull/44859~~](http://github.com/space-wizards/space-station-14/pull/44859)
  * Merged

# PR List

(excluding bugfixes, small and medium refactors and mapping changes, text only changes or similar)

* [43525](https://github.com/space-wizards/space-station-14/pull/43525) Vehicle system: Movement & Buckling


* [39571](https://github.com/space-wizards/space-station-14/pull/39571) Smarter Entity Targeting


* [44057](https://github.com/space-wizards/space-station-14/pull/44057) [MALD PR] Remove mimic vendor gamerule


* [43977](https://github.com/space-wizards/space-station-14/pull/43977) Remove background box from main menu


* [44061](https://github.com/space-wizards/space-station-14/pull/44061) Mini Gravity Generator requires charging


* [38505](https://github.com/space-wizards/space-station-14/pull/38505) Sheep v2
* [40540](https://github.com/space-wizards/space-station-14/pull/40540) Disposals refactor


* [44132](https://github.com/space-wizards/space-station-14/pull/44132) Camera resprites


* [43549](https://github.com/space-wizards/space-station-14/pull/43549) Changeling intro song


* [36895](https://github.com/space-wizards/space-station-14/pull/36895) Unite LogComponent, FoodSlicableComponent and partially ButcherableComponent into one. Sharp component removal.


* [43267](https://github.com/space-wizards/space-station-14/pull/43267) Clothing Inhand Additions


* [44137](https://github.com/space-wizards/space-station-14/pull/44137) Changeling escape with identity objective


* [44114](https://github.com/space-wizards/space-station-14/pull/44114) Add RotatableComponent to BaseItem


* [41614](https://github.com/space-wizards/space-station-14/pull/41614) [Aseprite Tool] Add Copy Displaced To New Canvas Button


* [44203](https://github.com/space-wizards/space-station-14/pull/44203) Evil Changeling Shop Icon


* [40090](https://github.com/space-wizards/space-station-14/pull/40090) [MICROBALANCE PR] Explosives no longer pierce armor


* [44228](https://github.com/space-wizards/space-station-14/pull/44228) Make NumberObjective Max inclusive


* [44212](https://github.com/space-wizards/space-station-14/pull/44212) Changeling Random Objectives


* [42987](https://github.com/space-wizards/space-station-14/pull/42987) add a drum kit


* [43805](https://github.com/space-wizards/space-station-14/pull/43805) Changeling reagent stings


* [44284](https://github.com/space-wizards/space-station-14/pull/44284) Ghosts have follow buttons in chat
  * `Samuka`: maybe revert this?


* [47](https://github.com/Space-Wizards-Federation/space-station-14/pull/47) Adds temperature protection to scarves


* [118](https://github.com/Space-Wizards-Federation/space-station-14/pull/118) ~~Directional arrow~~
  * `Errant`: This does not seem to have been copied over to the relevant repo, does not exist on master. Or if it does, it’s not working


* [44319](https://github.com/space-wizards/space-station-14/pull/44319) Bwoink "quick info" system for names


* [44323](https://github.com/space-wizards/space-station-14/pull/44323) Add .noai file


* [44317](https://github.com/space-wizards/space-station-14/pull/44317) Add trust score and account creation date to the player panel


* [8](https://github.com/Space-Wizards-Federation/space-station-14/pull/8) Construction menu recipe history


* [114](https://github.com/Space-Wizards-Federation/space-station-14/pull/114) Remove Staff of Entrance from Magic Event Spell


* [44350](https://github.com/space-wizards/space-station-14/pull/44350) Mailing unit resprite


* [44353](https://github.com/space-wizards/space-station-14/pull/44353) Add AFK kicks back in
  * `ROOMBA`: blocker for map pop trimming has been removed now but I think jez would want to to re-evaluate it
  * `Errant`: There is an open PR for increasing the AFK detection time. If duration is brought up, use [#44859](https://github.com/space-wizards/space-station-14/pull/44859) instead of opening a new one


* [37907](https://github.com/space-wizards/space-station-14/pull/37907) Sprite Fade Overlay Restricted to overlapping clickables


* [44404](https://github.com/space-wizards/space-station-14/pull/44404) Allow aghosts to open several storage UIs


* [44367](https://github.com/space-wizards/space-station-14/pull/44367) Toggle dead chat


* [43736](https://github.com/space-wizards/space-station-14/pull/43736) added ammonia electrolysis


* [43905](https://github.com/space-wizards/space-station-14/pull/43905) All zombies are now re-ghostable.


* [39403](https://github.com/space-wizards/space-station-14/pull/39403) Spider and Spacemobs Night Vision


* [43747](https://github.com/space-wizards/space-station-14/pull/43747) Pointing at inventory items with mouse binding


* [44473](https://github.com/space-wizards/space-station-14/pull/44473) Update client with the new logo


* [44368](https://github.com/space-wizards/space-station-14/pull/44368) Custom icon ammo counter
  * `Slarti`: Needs cleanup, I’ll open an issue later


* [44394](https://github.com/space-wizards/space-station-14/pull/44394) Stinky Smite


* [44363](https://github.com/space-wizards/space-station-14/pull/44363) Add randomizer lock buttons to character editor screen
  * `Errant`: The functionality seems nice, but the UI should probably be revisited


* [44442](https://github.com/space-wizards/space-station-14/pull/44442) Ghost Half-Bright


* [43778](https://github.com/space-wizards/space-station-14/pull/43778) Changeling no longer clones harmful status effects


* [43816](https://github.com/space-wizards/space-station-14/pull/43816) Change dwarves to use displacement maps instead of sprite scaling


* [44526](https://github.com/space-wizards/space-station-14/pull/44526) Add accessibility option to remove noise from the night vision overlay
  * `Scar`: The accessibility menu has already been rewritten since this PR was merged.
    * `Errant`: I wrote my comment to the wrong line… Moved it


* [38789](https://github.com/space-wizards/space-station-14/pull/38789) Describe reagent colours with words


* [44524](https://github.com/space-wizards/space-station-14/pull/44524) Self-predicting popups


* [43820](https://github.com/space-wizards/space-station-14/pull/43820) Changeling last resort


* [43725](https://github.com/space-wizards/space-station-14/pull/43725) Make Centrifuging Pest Killer a source of Mercury, Ethanol, and Chlorine.


* [44589](https://github.com/space-wizards/space-station-14/pull/44589) Modularize all reduced motion options


* [44592](https://github.com/space-wizards/space-station-14/pull/44592) Admin playertab can now filter for roles


* [39715](https://github.com/space-wizards/space-station-14/pull/39715) Nukeops disk-centric win condition


* [44583](https://github.com/space-wizards/space-station-14/pull/44583) Removed all Backpack Straps


* [44577](https://github.com/space-wizards/space-station-14/pull/44577) Changeling Night Vision


* [44087](https://github.com/space-wizards/space-station-14/pull/44087) Solutions Refactor Care Package - Service Department


* [37419](https://github.com/space-wizards/space-station-14/pull/37419) Gyroscope throttling take 2, automatic, inertia based


* [43554](https://github.com/space-wizards/space-station-14/pull/43554) Generic Target System


* [44198](https://github.com/space-wizards/space-station-14/pull/44198) Prevent a Microbomb Implant Action while pacified.


* [41004](https://github.com/space-wizards/space-station-14/pull/41004/changes) Add SpawnAfter for SpawnEntitiesBehavior
  * Princess: Not a huge Fan of this one, both in implementation and code. This should be an engine feature anyways as we need a way to spawn a paused entity and then reparent/initialize later so you can spawn an entity with MetabolismComponent during Metabolism without throwing an exception.
    * `ROOMBA`: Is this like an entity lazy initialization thing or is this metabolism code being metabolism code
    * Princess: Lazy initialization thing, other systems have the same issue but I’ve primarily seen it in metabolism with the “Enumeration modified” exception.
  * Revert [**https://github.com/space-wizards/space-station-14/pull/37716 **](https://github.com/space-wizards/space-station-14/pull/37716)and [**https://github.com/space-wizards/space-station-14/pull/41004**](https://github.com/space-wizards/space-station-14/pull/41004)


* [44587](https://github.com/space-wizards/space-station-14/pull/44587) Removal of Liquid/Supercooled Gas Canisters from Cargo Requests


* [44599](https://github.com/space-wizards/space-station-14/pull/44599) Beards can now be hidden


* [44111](https://github.com/space-wizards/space-station-14/pull/44111) Multicoloured Hair Proof of Concept + Minor Marking Code Tweaks


* [42830](https://github.com/space-wizards/space-station-14/pull/42830) Viper and Pulse Carbine have full-auto mode selected by default


* [44499](https://github.com/space-wizards/space-station-14/pull/44499) Add ghost random warp


* [37716](https://github.com/space-wizards/space-station-14/pull/37716) New not fun meteors


* [44628](https://github.com/space-wizards/space-station-14/pull/44628) Shields Rework


* [44655](https://github.com/space-wizards/space-station-14/pull/44655) Event log tool


* [42806](https://github.com/space-wizards/space-station-14/pull/42806) Silicon Law Display UI Refactor


* [44701](https://github.com/space-wizards/space-station-14/pull/44701) smoother doafter animation


* [40963](https://github.com/space-wizards/space-station-14/pull/40963) Update Space Villain's UI


* [40961](https://github.com/space-wizards/space-station-14/pull/40961) Make Space Villain LMTR wire remove HP and MP limits and skip game end checks


* [44187](https://github.com/space-wizards/space-station-14/pull/44187) Add option to toggle HRTF audio processing


* [44736](https://github.com/space-wizards/space-station-14/pull/44736) Remove M90GL


* [43854](https://github.com/space-wizards/space-station-14/pull/43854) 80s Hair


* [43299](https://github.com/space-wizards/space-station-14/pull/43299) Lizard Plushie Slippers update


* [43996](https://github.com/space-wizards/space-station-14/pull/43996) add a fretless bass guitar instrument


* [43730](https://github.com/space-wizards/space-station-14/pull/43730) Skeleton Nerfs and Cleanup


* [42296](https://github.com/space-wizards/space-station-14/pull/42296) Getmore Bakemore Crate Rebalance


* [43110](https://github.com/space-wizards/space-station-14/pull/43110) removed damage from toy base sword to fix #42825


* [43099](https://github.com/space-wizards/space-station-14/pull/43099) Make locked machines deconstruction consistent


* [42350](https://github.com/space-wizards/space-station-14/pull/42350) WYA to Where you at


* [43527](https://github.com/space-wizards/space-station-14/pull/43527) Vehicle system: Core systems & Components
* [39769](https://github.com/space-wizards/space-station-14/pull/39769) New Agent Id UI


* [41264](https://github.com/space-wizards/space-station-14/pull/41264) Added "Assistive items" loadout group


* [44251](https://github.com/space-wizards/space-station-14/pull/44251) Expand and tweak several random-name datasets


* [43008](https://github.com/space-wizards/space-station-14/pull/43008) Move all accents into being RelayAccentSystems, add InventoryRelayedEvent support


* [38528](https://github.com/space-wizards/space-station-14/pull/38528) Randomized Markings (take two)
* [39416](https://github.com/space-wizards/space-station-14/pull/39416) Trash bag of holding and lil trash bag change


* [41664](https://github.com/space-wizards/space-station-14/pull/41664) Survival boxes are smaller and contain no food
  * Princess: Removes the flare which is overall a net negative for the game. We should probably make it a 2x3 and include the flare + 1 other thing or make flares more available. Not a blocking issue.
  * `ROOMBA`: we can also just chip a corner from the survival box just to make it evil. but yeah flare should stay IMO.
  * `Scar`: Some forks give an item that opens the guidebook in the survival box, so maybe something along those lines for the extra item? Might be hard with a 1x1 space only though.
  * Have it be a business card from Nanotrasen uses advanced bluespace print technology.
    * MAKE A GITHUB ISSUE I NEED MY FUCKING FLARE BACK!!!!


* [38941](https://github.com/space-wizards/space-station-14/pull/38941) Change dual-port air vent to function like a regular vent


* [40337](https://github.com/space-wizards/space-station-14/pull/40337) Battlecry UI improvements


* [36673](https://github.com/space-wizards/space-station-14/pull/36673) Add Friendly and Hostile Slime Reactions.


* [39264](https://github.com/space-wizards/space-station-14/pull/39264) More item status


* [38249](https://github.com/space-wizards/space-station-14/pull/38249) Make Spanish accent more linguistically accurate


* [44624](https://github.com/space-wizards/space-station-14/pull/44624) Wizard Guardian


* [44789](https://github.com/space-wizards/space-station-14/pull/44789) added missing items to chameleon kits


* [44809](https://github.com/space-wizards/space-station-14/pull/44809) re-allow humans with non realistic eye colors


* [43532](https://github.com/space-wizards/space-station-14/pull/43532) Vehicle system: Mech & CardboardBox Integration


* [44811](https://github.com/space-wizards/space-station-14/pull/44811) Firehelmets have small power cell now


* [38108](https://github.com/space-wizards/space-station-14/pull/38108) Toggleable visor for security helmets


* [44644](https://github.com/space-wizards/space-station-14/pull/44644) DestructibleComponent [AlwaysPushInheritance]


* [44432](https://github.com/space-wizards/space-station-14/pull/44432) Screeching & Changeling Screech


* [44421](https://github.com/space-wizards/space-station-14/pull/44421) Changeling Resilience


* [43315](https://github.com/space-wizards/space-station-14/pull/43315) Add sharpness graphics option

# Question Time!

## Do we have plans around telemetry, now that logging is happening

Needs a ton of infrastructure so it’s down to someone to code it. Is planned and on the TODO list for infra.

## How is the respritening going? 

It is continuing to progress, right now walls, doors and tiles are done. Wall-mounts are being worked on next.

## New Cooking Stations?

Needs a cooking refactor, a contributor is working on designing one but a proper cooking system is gonna take a lot of time and dedication.

## How’s Breaksalv going?

Breaksalv is progressing and is waiting on some PRs to be merged.

## Are there any other major changes you guys are working on/ what are you focusing on?

Couple things, one major antag which will hopefully be added next update. Also we’re bringing back monthly updates. Lotta technical stuff being done in the background including engine optimizations and rewrites plus potentially Z-Levels

## How are things going since y'know?

Great!!! I can actually sleep and our team is working better than ever.

## Will we be getting new Maptainers?

Yes. Also hopefully more new other maintainers. But we need better policy for it and proper mapping guidelines.

## Do we have a Mapping tool overhaul in the pipeline?

Shrug. Something we want, previous contributor disappeared, and we’re working on an engine editor (real) which would help.


Releases since the last non-squashed PR: 0 :cry:


\

*Niko is a cat*