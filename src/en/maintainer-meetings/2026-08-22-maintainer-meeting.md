# 2026-08-22 Maintainer Meeting

:::info
## Maintainers In Attendance

* Roomba
* Princess
* Velken (Trial)
* Jessica (Trial)
* Errant
* Aeshus
* Slam
* Julian
* Electro
* Jezithyr
* Aada
* Nem (Trial)
* Samuka (Trial)
* ScarKy0
* Kazne

:::

(Meeting recording goes here)

# Topics

## Cvars

### Errant

Recent issues with server cvars ran the whole range of “admins want to tune game.minimum_job_fallback on Vulture but it has no permission flags” to someone accidentally breaking Salamander playtime tracking for over 2 weeks because the system worked in an unpredictable way with a 0 value, but *also because no maint could possibly be aware that the value was changed*. (Something similar happened earlier on Raptor with the DDOS flood prevention at login, which unfortunately caused a lot of false positives and players being annoyed by the entire feature) \nThese two issues seem to be on opposite axes - if we allow more cvars to be modified without serverconfig, there will be more undocumented uses of the possibility. And yet, “PR a serverconfig change” only really works on master, unless it’s a huge enough issue to be a hotfix

* Fildrance: We need to have ‘what is different from defaults’ command that outputs all local changes?
* Jezithyr: Have default permissions be defineable in YAML
* Princess: We should have CVAR standards for when we add new CVARs
* Jezithyr: Scope cvars with ForkId due to client conflicts/overriding 

## Botany

### Princess

With the merging of the Botany refactor, we should seriously think about *what* Botany should look like in the future rather than just having a prettier version of what we already currently have. In addition I didn’t want to block release or revert these changes but there’s some pretty serious balance changes and code quality issues with the refactor that need to be addressed. 

It would be better to actually hash out a proper plan for botany to address these issues and build on the solid foundation we now have.

* aada: There’s several design doc PRs to consider.
* Jezithyr: Design meeting for botany :)

## Refining Release Schedule

### Princess

Release this month was a bit hectic, there’s been talks about returning to 2 weeks but I feel like that would just increase the amount of hectic releases even if the amount of “release blocking” fixes will be smaller. I instead propose that we do this:

* Warning for stable cutoff - 1 week before cutoff (Thursday)
* Stable cutoff (Thursday)
* Maintainer meeting (Saturday)
* Release - 1 week after Stable cutoff (Thursday)


* (Errant) We could also make the meeting doc (this file) at the halfway mark or at the stable warning, with the PRs already available, so we can review half of them ahead of time. Without a full meeting
* Slam: Allow early releases if it’s a particularly simple release without a bunch of issues or a big PR list


## Spearheading Maintainer Policy

### Roomba

Please for the love of god we need to spearhead and implement our maintainer policy. There was a thread on this internally however its now stalled for one reason or another. We need to:

* Compile all/some of the opinions/points that were raised in the internal thread into one document.
* Ask a Staff Manager to host a vote or another discussion on the policy so we actually have something concrete to iterate on.
  * `Scar`: SMs were already notified, I believe August is already looking into it(?)
  * Jez: This is being worked on after this meeting with me and Electro

Otherwise stuff like giving Art Leads selfmerge perms is going to be dead as soon as it comes up since our core policy doesn’t even exist, we’re still going off of our old policy (which is OK but we decided against porting it wholesale).

# Release Blockers

* ~~Change Default CVAR for Jobs~~
  * ~~(Princess) this changes the expected behavior for Job spawning and has been pretty poorly received, especially because there are A LOT of jobs that are marked as required roundstart which heavily affects lowpop negatively.~~
  * ~~(Velken) the larger issue seems to be “being department head sucks” and “i don’t want to be forced into a role”.~~
* ~~Variantize Some Maps~~
  * ~~(Princess) there’s some maps that still need to be fixed, mostly shuttles we should get a list and then ensure all of them are fixed before Stable.~~
    * All maps are now fixed
  * (~~Errant) All shuttles and event shuttles have been re-Aligned and Variantized on~~ [~~https://github.com/space-wizards/space-station-14/pull/45504,~~](https://github.com/space-wizards/space-station-14/pull/45504,) ~~please review~~\n~~(Note that they might have less-obvious mapping issues on them still)~~
    * * ~~The Meta Station emergency shuttle just flat out crashes the dev client if you get near it while it’s initialized. Something about foodcontainers I think, but since the map is not in use I did not care enough to look into it much~~
  * ~~(Errant) There have been multiple reports that some maps had some airlocks/shutters/etc lose device links during the manual fixing of the maps, before StructureAligner was circulated. No one has been able to point at anything specific, though~~
  * ~~(Errant) As of now (thursday evening) every map except Exo still has 40-100+ misaligned entities. These are most likely a large pile of firelocks and shutters (which easily avoid detection) and perhaps a few airlocks here and there. All maps except Exo should have the latest **Align** ran on them and resaved~~

    \
* ~~Engine Bugs~~
  * ~~(Princess) UI has some major issues, some close buttons don’t work. Some UIs will crash in dev such as the gas analyzer.~~ 
  * ~~(AJCM)~~ [~~Invisibility is~~](https://github.com/space-wizards/space-station-14/issues/45390) ~~broken  and t~~[~~heres a pr fixing it~~](https://github.com/space-wizards/RobustToolbox/pull/6905)
  * ~~(Velken) I still can’t open admin logs on dev.~~
* ~~Satiation Serialization~~
  * ~~(Scar) Satiation has plenty of bugs after the refactor and has serialization and save-load issues according to sloth.~~ [~~Issue~~](https://github.com/space-wizards/space-station-14/issues/45476)
  * [~~https://github.com/space-wizards/space-station-14/pull/45548~~](https://github.com/space-wizards/space-station-14/pull/45548)
* Lockers too Strong
  * (Princess) <https://github.com/space-wizards/space-station-14/pull/45521> 
  * Lockers have the plasteel modifier currently which makes them much harder to break into. Big balance change that seems undesired. Aada would rather all structures be easier to damage while I’d rather have it so walls are stronger than 
    * (aada) Originally I had made the damage modifier sets with the idea that they could be used from walls and structures all the way down to items. This meant that flat damage reductions were rather conservative which allowed middle tier weapons (toolboxes or so) to deal enough to do a few points of damage to plasteel entities, or crowbars able to deal a few points to steel.
    * (Princess) I’ll rename XStructureMod to XStaticMod
* Fallback roles
  * (Slam) <https://github.com/space-wizards/space-station-14/issues/45213>

This has been discussed a bit internally, Slam will explainnnn 


\
* ~~Lights and wall space~~
  * ~~This came up during mapping, the two biggest issues we face (and this is releveant for the release, because every downstream will face this when remapping)~~

    ~~Posters and Lights now “collide” a lot, because wall lights used to be *next* to the walls, but now we are treating them as if they were wallmounts. And they now fight for the precious little available wall space for mounting stuff~~\n\n~~If we want lights to be ON the wall, we should turn them into actual wallmounts. But we might also want to consider taking them off the walls completely, to free up the space. Floor lights, standing lights (ceiling lights… *somehow??)*~~
    * ~~Also, let’s not make downstreams remap all walls to resolve overlap issues, and then make them remap tehm again next release~~
    * [~~https://github.com/space-wizards/space-station-14/pull/45533~~](https://github.com/space-wizards/space-station-14/pull/45533)

  \

# I read through the PR list:

* Princess
* ScarKy0
* aada
* Velken
* Nem

# PR List

(excluding bugfixes, small and medium refactors and mapping changes, text only changes or similar)

* * [32134](https://github.com/space-wizards/space-station-14/pull/32134) Stationary teleporters
    * `Scar`: The sound of those is EXTREMELY loud and goes for like a distance of 15 tiles. Not a big problem but should open an issue about it probably.
    * `Aeshus`: (In general, this PR predated sheetlets) I commonly see hard-coded colors in multiple places in new UI PRs; should we come up with a policy to better enforce/require stylesheet/sheetlet use? We don’t really have a strictly defined palette, so even with stylesheets, it’s not uncommon for arbitrary colors to be set; do we have anyone who could be a final decider for this?
  * [34166](https://github.com/space-wizards/space-station-14/pull/34166) Refactor hunger and thirst systems
    * `Scar`: Has a few issues left. One of them is a stable blocker currently. Listed in the “Release Blockers” section.
  * [34191](https://github.com/space-wizards/space-station-14/pull/34191) Tramstation
  * [36259](https://github.com/space-wizards/space-station-14/pull/36259) Yaml audio params are often ignored
    * `Aeshus:` Bugs fixed in “[44952](https://github.com/space-wizards/space-station-14/pull/44952) Hotfix: Fix mistaken AudioParams.WithVariation calls + LockComponent cleanup”
    * `Scar`: The fix was already merged
  * [37841](https://github.com/space-wizards/space-station-14/pull/37841) Power outages are shorter and only affect the main (largest) grid
  * [38794](https://github.com/space-wizards/space-station-14/pull/38794) 0G Hypereutactic-blade speed fix
  * [39096](https://github.com/space-wizards/space-station-14/pull/39096) feat: ConditionalSpawnerComponent can now stack items it spawns automatically
  * [39686](https://github.com/space-wizards/space-station-14/pull/39686) Add ability to include "experimental" icon for labeled PRs
    * `Aeshus`: This hard-codes a resource path + colors in C# instead of using stylesheets/sheetlets.
      * `Aeshus:` The current method would probably be to use more StyleClasses, but I think this process could be improved.
    * `Aeshus:` I’m also not sure we should be using more icons for this, as it isn’t super clear what the extra icon means. I don’t think there’s a tooltip, either?
    * `Slam`: Ye this PR kinda wack ngl I should revisit it (also deltanedas says its borked)
  * [39734](https://github.com/space-wizards/space-station-14/pull/39734) Exception now meows when an error occurs on the server
  * [40404](https://github.com/space-wizards/space-station-14/pull/40404) Enforce ordering for radial menu
    * `Aeshus`: Introduced bug fixed in “45464 [MALD PR] fix the AI door menu” (discussed below).
    * `Aeshus`: I’m not totally sure we should have an implicit ordering based on the localized tooltip text, as that will still cause issues for players switching between forks with different localizations (e.g. alternative translations, different player languages)
    * `Velken`: Some radial menus should have a fixed ordering (example: AI door menu). It is really annoying that the buttons change order after one toggles one of the settings. 
  * [40636](https://github.com/space-wizards/space-station-14/pull/40636) Predict Light Replacers & Add Radial Menu
    * `Aeshus`: What’s the consensus on Radial Menus? It seems to me we want to move away from the verb menu to a more contextual radial menu? 
  * [40693](https://github.com/space-wizards/space-station-14/pull/40693) Predict Forensics V2.0 (Ready for Review)
  * [40815](https://github.com/space-wizards/space-station-14/pull/40815) Fix teleport scroll teleporting into walls
  * [41053](https://github.com/space-wizards/space-station-14/pull/41053) Xenoartifact: legendary microwave trigger
  * [41062](https://github.com/space-wizards/space-station-14/pull/41062) Fix highlights don't work for other languages
    * `Aeshus`: Undocumented breaking change in the ordering of the `CharacterData` struct, whos ordering is relied on by some code and probably wasn’t necessary as they could’ve changed the `string?` type to a `protoId` type instead of switching its order. 
    * `Aeshus:` This also had an undocumented change to all of the Localization IDs for all multi-word job names, and I’m curious of we have a policy around this as I’m not sure how much trouble this will cause downstream localizers?
      * `Aeshus`: This is a result of using PrototypeIDs, which don’t have spaces so they don’t know where to add the “-” for kebab-case (and thus are all one-word now), yet they still retain code for adding dashes if the protoid had a space in it.
      * `Aeshus`: I’ve have other PRs with localization id changes and was wondering if we should try to avoid that as much as possible? Should we plan a migration to normalize what we’d like their ids to be like?
  * [41122](https://github.com/space-wizards/space-station-14/pull/41122) Refactor and predict Alert Levels
    * DO IT AFTER THE MEETING!!!!!!!!!!!!!!!!!!!!!
  * [41186](https://github.com/space-wizards/space-station-14/pull/41186) Artifact Lamp
  * [41272](https://github.com/space-wizards/space-station-14/pull/41272) Instrument UI MinVolume slider
    * `Aeshus:` This implements a new custom control that should be standardized and shared, as we have a similar control for the options UI, `OptionSlider`; it’s a common pattern to want a slider + text next to it.
      * `Aeshus:` Should probably get RT modified to support this.
  * [41455](https://github.com/space-wizards/space-station-14/pull/41455) Additional console commands for debugging Xeno Artifact
  * [41506](https://github.com/space-wizards/space-station-14/pull/41506) MaskSystem Cleanup + Enable Masks to be pulled by others
  * [41604](https://github.com/space-wizards/space-station-14/pull/41604) Instrument UI overhaul
    * `Aeshus`: Has bug patched in “[45055](https://github.com/space-wizards/space-station-14/pull/45055) Fix percussion channel and switch to one-based channel indexes in instrument UI.”
  * [41899](https://github.com/space-wizards/space-station-14/pull/41899) Improve UX and visuals of communications console
    * `Aeshus`: I like the art but this does look very discordant with a lot of other UIs right now. Is *this* the direction we want to move our UIs into? Who would decide this?
      * Organize a meeting to discuss standards pls & thank you :)
  * [42401](https://github.com/space-wizards/space-station-14/pull/42401) Removed the numeric identifier from the names of pets, rat kings, revenants, and space dragons
    * `Scar`: This PR also made silicons not have their identifiers in brackers. Feels unintentional and looks rather ugly in-game.
    * `Nem`: I can fix that - this issue applies to all the other ones as the ‘( )’ was hardcoded. Just needs the FTL for name formats tweaked. Would like to discuss if this should be done for all mobnames 
  * [42420](https://github.com/space-wizards/space-station-14/pull/42420) Fix SharedEntityStorageSystem.Remove causing a debug assert with an invalid parent
    * `Aeshus:` Bug fixed in (now merged) in “[45503](https://github.com/space-wizards/space-station-14/pull/45503) Bugfix: SharedEntitySystem.Remove parents you to the grid or the map.”
  * [42497](https://github.com/space-wizards/space-station-14/pull/42497) Monkeys & kobolds now have whitelisted neck slots
  * [42626](https://github.com/space-wizards/space-station-14/pull/42626) Mark EntityPrototypeHelpers as obsolete
  * [42721](https://github.com/space-wizards/space-station-14/pull/42721) Xenoarchaeology - fix #42713, allow sibling nodes to count toward time add
  * [42785](https://github.com/space-wizards/space-station-14/pull/42785) IHeatContainers for TemperatureComponent
    * `Scar`: Vulps lost their heat transfer changes, will need an issue opened to adjust their temperature regulation.
    * `Nem`: Issues with bodies heating/cooling were raised by valued playtesters
    * `Scar`: The heating/cooling being slower was intentional (to my knowledge), the change to vulps was straight up removed however due to API changes not supporting it anymore.
  * [42850](https://github.com/space-wizards/space-station-14/pull/42850) [FEATURE] Engineer Xenoborg Module Rework
  * [42871](https://github.com/space-wizards/space-station-14/pull/42871) Lizard Plushie Inhand and Helmet Resprite
  * [42879](https://github.com/space-wizards/space-station-14/pull/42879) Integration tests for atmos networking
    * `Aeshus`: (In general) We still need a true guide for integration testing to point contributors to, so we can make requirements on this.
  * [42908](https://github.com/space-wizards/space-station-14/pull/42908) Add SegmentedBarChart, remove SplitBar and BeakerBarChart
    * `Aeshus`: (UI nerd stuff): Do we want to inherit from the top-level control or should all custom controls inherit from `Control` containing that control as a chid.
      * See: [`AbsorbentItemStatus.xaml`](https://github.com/space-wizards/space-station-14/pull/42908/changes#diff-41972ec4a984fedad823f771b1b2098eec374186f847778b3b32b15a5ddc4ab5)
  * [42939](https://github.com/space-wizards/space-station-14/pull/42939) Directional Window Corners
  * [43014](https://github.com/space-wizards/space-station-14/pull/43014) Gives the Heavy Xenoborg a Burst Fire Laser module; causes targets to burst into fire with burst fire
  * [43018](https://github.com/space-wizards/space-station-14/pull/43018) Makes syndicate hardsuit headlights brighter, adds juggsuit light
  * [43062](https://github.com/space-wizards/space-station-14/pull/43062) Lizard Job Plushie Inhands & Helmet Sprites (Plus Organization)
  * [43107](https://github.com/space-wizards/space-station-14/pull/43107) Predict intercom examine.
    * `Slam:` Small reminder for maints to remember posting Breaking Changes! This caused quite a stir.
  * [43112](https://github.com/space-wizards/space-station-14/pull/43112) Adds the xenoborg engineer deflector field module
  * [43120](https://github.com/space-wizards/space-station-14/pull/43120) Xenoborg Nanite Gun + ComplexProjectileComponent
  * [43126](https://github.com/space-wizards/space-station-14/pull/43126) Adds the Xenoborg Heavy Radioactive module
  * [43268](https://github.com/space-wizards/space-station-14/pull/43268) Reclaimer Loop Prevention Integration Test
  * [43294](https://github.com/space-wizards/space-station-14/pull/43294) Buff/Nerf Bluespace Storage to hold Ginormous items; Be smaller.
  * [43530](https://github.com/space-wizards/space-station-14/pull/43530) Replace the windows on the nukie base and infiltrator with plastitanium windows
  * [43545](https://github.com/space-wizards/space-station-14/pull/43545) network HandsComponent, fix changeling not updating hand displacements on transform
  * [43569](https://github.com/space-wizards/space-station-14/pull/43569) Update Powercell Reagents to have Lithium and Uranium
  * [43605](https://github.com/space-wizards/space-station-14/pull/43605) Add a popup when a melee weapon repeatedly fails to damage an entity
  * [43667](https://github.com/space-wizards/space-station-14/pull/43667) PressureImmunity StatusEffects
  * [43668](https://github.com/space-wizards/space-station-14/pull/43668) Muted StatusEffects
  * [43750](https://github.com/space-wizards/space-station-14/pull/43750) Adrenaline StatusEffects
  * [43864](https://github.com/space-wizards/space-station-14/pull/43864) Mindshield Refactor + Changeling Fake Mindshield
  * [43903](https://github.com/space-wizards/space-station-14/pull/43903) Fix some SpriteComponent-related warnings and ConstructionPlacementHijack cleanup
  * [43935](https://github.com/space-wizards/space-station-14/pull/43935) Projectiles prototypes reorganization/cleanup
  * [43997](https://github.com/space-wizards/space-station-14/pull/43997) Scrolling text screens
  * [44010](https://github.com/space-wizards/space-station-14/pull/44010) Bagel - Atmos changes
  * [44048](https://github.com/space-wizards/space-station-14/pull/44048) Add audio device switching to options
  * [44113](https://github.com/space-wizards/space-station-14/pull/44113) Disposals dynamic power consumption
  * [44125](https://github.com/space-wizards/space-station-14/pull/44125) Cargo shuttles - Atmos and tweaks
  * [44127](https://github.com/space-wizards/space-station-14/pull/44127) APC: add visual states for breaker trips, power delivery
  * [44169](https://github.com/space-wizards/space-station-14/pull/44169) Changeling Devour Most Objective
  * [44178](https://github.com/space-wizards/space-station-14/pull/44178) Recycler Resprites
  * [44189](https://github.com/space-wizards/space-station-14/pull/44189) Monkey sprites for the color jumpsuit, default ClothingVisuals checks for equipper species
  * [44220](https://github.com/space-wizards/space-station-14/pull/44220) Changeling Escape as Department Objective
  * [44235](https://github.com/space-wizards/space-station-14/pull/44235) Add max FPS to options menu
  * [44245](https://github.com/space-wizards/space-station-14/pull/44245) EntityEffectActions can target the user.
  * [44262](https://github.com/space-wizards/space-station-14/pull/44262) Ambient occlusion overlay optimisation + art change + cleanup
  * [44356](https://github.com/space-wizards/space-station-14/pull/44356) Change PaperVisuals to use Thickness instead of Box2
  * [44361](https://github.com/space-wizards/space-station-14/pull/44361) Fix powercelldraw
  * [44364](https://github.com/space-wizards/space-station-14/pull/44364) Serialization content changes
  * [44377](https://github.com/space-wizards/space-station-14/pull/44377) Add option to mute audio on unfocus
  * [44389](https://github.com/space-wizards/space-station-14/pull/44389) Oil gun
  * [44391](https://github.com/space-wizards/space-station-14/pull/44391) Shock module
  * [44412](https://github.com/space-wizards/space-station-14/pull/44412) Tram Driver
  * [44436](https://github.com/space-wizards/space-station-14/pull/44436) Add EntitySpawnVariationPass as an EntityEffect
    * `Nem`: We should be taking actions to make all variations consistent to this.
  * [44494](https://github.com/space-wizards/space-station-14/pull/44494) Cleanup: fix content-side obsolete TransformComponent warnings
  * [44500](https://github.com/space-wizards/space-station-14/pull/44500) Decal chents + prediction
  * [44512](https://github.com/space-wizards/space-station-14/pull/44512) Adds the security bola, converts existing bola into makeshift bola; bolas require active hand to be empty to remove
  * [44513](https://github.com/space-wizards/space-station-14/pull/44513) Update to newest XamlX
  * [44567](https://github.com/space-wizards/space-station-14/pull/44567) Fix ExpireIdCard
  * [44576](https://github.com/space-wizards/space-station-14/pull/44576) Botany refactor
  * [44622](https://github.com/space-wizards/space-station-14/pull/44622) Coin tossing
  * [44626](https://github.com/space-wizards/space-station-14/pull/44626) Dev map - New Cargo area, and many more tweaks and fixes
  * [44640](https://github.com/space-wizards/space-station-14/pull/44640) fix: bug where enabling auto chat highlights would overwrite existing custom highlights
  * [44666](https://github.com/space-wizards/space-station-14/pull/44666) Dock types visible on shuttle nav console
  * [44677](https://github.com/space-wizards/space-station-14/pull/44677) Add check if mouth is covered for changeling devour
  * [44681](https://github.com/space-wizards/space-station-14/pull/44681) Actions icons refactor
    * `Scar`: Broke togglable icons at some point. You know, the silly ones when if you are targetting an action the icon has a different sprite?
  * [44732](https://github.com/space-wizards/space-station-14/pull/44732) Add WhitelistManager that tracks the whitelist status of connected players
  * [44735](https://github.com/space-wizards/space-station-14/pull/44735) Update postshaders for multi-shader support
  * [44751](https://github.com/space-wizards/space-station-14/pull/44751) Fland Station - Redesign TEG room + tweaks and fixes
  * [44755](https://github.com/space-wizards/space-station-14/pull/44755) Full Structures Rebalance
  * [44756](https://github.com/space-wizards/space-station-14/pull/44756) Gas filter and mixer: show settings in examine message
  * [44759](https://github.com/space-wizards/space-station-14/pull/44759) Add recursive storage checking to the admin contra overlay.
  * [44772](https://github.com/space-wizards/space-station-14/pull/44772) Move Accents to Shared v2
  * [44790](https://github.com/space-wizards/space-station-14/pull/44790) Move server_config.toml to Resources, copy only on publish.
  * [44797](https://github.com/space-wizards/space-station-14/pull/44797) Add custom sus icon in cham outfit change implanter
  * [44801](https://github.com/space-wizards/space-station-14/pull/44801) Directional visibility for wall-mounted entities 2
  * [44810](https://github.com/space-wizards/space-station-14/pull/44810) Add the ability for ghosts to extinguish candles.
  * [44812](https://github.com/space-wizards/space-station-14/pull/44812) Organ relations
  * [44816](https://github.com/space-wizards/space-station-14/pull/44816) Fix: Add `SharedContainerSystem.CanInsert` check to the `InventorySystem.CanEquip`
  * [44831](https://github.com/space-wizards/space-station-14/pull/44831) Ridable Office Chairs
  * [44832](https://github.com/space-wizards/space-station-14/pull/44832) fix asphyx ghost type sprite
  * [44833](https://github.com/space-wizards/space-station-14/pull/44833) Fix overflow jobs still rolling for players banned from them
  * [44834](https://github.com/space-wizards/space-station-14/pull/44834) Reorganize jumpsuit and jumpskirt prototypes and sprites
  * [44843](https://github.com/space-wizards/space-station-14/pull/44843) Update content for polygon occluders
  * [44848](https://github.com/space-wizards/space-station-14/pull/44848) Text black outline
  * [44849](https://github.com/space-wizards/space-station-14/pull/44849) Fix EntityMenu not removing entities when sprite becomes invisible
  * [44851](https://github.com/space-wizards/space-station-14/pull/44851) Foldable Light Riot Helmet
  * [44857](https://github.com/space-wizards/space-station-14/pull/44857) The Respritening - Batch 1
  * [44860](https://github.com/space-wizards/space-station-14/pull/44860) Fix: Insert items into clothing instead of butchering them when used
  * [44861](https://github.com/space-wizards/space-station-14/pull/44861) Changeling Blood Check
  * [44867](https://github.com/space-wizards/space-station-14/pull/44867) Prediction + small Cleanup: WaggingSystem
  * [44870](https://github.com/space-wizards/space-station-14/pull/44870) Refactor: Split `StunbatonComponent` into generic components
  * [44871](https://github.com/space-wizards/space-station-14/pull/44871) Update submodule to 284.0.0
  * [44878](https://github.com/space-wizards/space-station-14/pull/44878) BuckleSystem: buckled/strapped event on startup
  * [44882](https://github.com/space-wizards/space-station-14/pull/44882) Apply Entity Effects On Melee
  * [44883](https://github.com/space-wizards/space-station-14/pull/44883) Fix mechboard UI state
  * [44889](https://github.com/space-wizards/space-station-14/pull/44889) Replace telescience ruin master key with science key
  * [44890](https://github.com/space-wizards/space-station-14/pull/44890) Update submodule to 285.0.0
  * [44892](https://github.com/space-wizards/space-station-14/pull/44892) Bugfix: anomaly vessel panel visibility, add Inverted field to WiresVisuals
  * [44895](https://github.com/space-wizards/space-station-14/pull/44895) Bugfix: Light tubes and bulbs break into glass shards
  * [44896](https://github.com/space-wizards/space-station-14/pull/44896) VendingMachine refactor (systems. UI, components)
  * [44897](https://github.com/space-wizards/space-station-14/pull/44897) Revert engine to 284.0
  * [44899](https://github.com/space-wizards/space-station-14/pull/44899) Revert "Update to newest XamlX (#44513)"
  * [44903](https://github.com/space-wizards/space-station-14/pull/44903) Fix the G.O.R.I.L.L.A Gauntlet
  * [44909](https://github.com/space-wizards/space-station-14/pull/44909) Artifact trigger continuation popup
  * [44910](https://github.com/space-wizards/space-station-14/pull/44910) Fix TriggerOnToolUseSystem
  * [44911](https://github.com/space-wizards/space-station-14/pull/44911) Bugfix: Tail wag respects tail visibility in occluding suits
  * [44912](https://github.com/space-wizards/space-station-14/pull/44912) Bugfix: Fix inverted prototypes spawn chance in `ConditionalSpawnerSystem`
  * [44913](https://github.com/space-wizards/space-station-14/pull/44913) Bugfix: Carpets are destructible again
  * [44914](https://github.com/space-wizards/space-station-14/pull/44914) Bugfix: Check UIDs in TryMergeStacks
  * [44915](https://github.com/space-wizards/space-station-14/pull/44915) Bugfix: Broken Computers are destructible again
  * [44917](https://github.com/space-wizards/space-station-14/pull/44917) Fix default metamorphic glasses (e.g. milk) solution not showing
  * [44927](https://github.com/space-wizards/space-station-14/pull/44927) Update Engine to v284.0.1
  * [44930](https://github.com/space-wizards/space-station-14/pull/44930) Gives corgis the ability to smoke & Remove Smart Corgi
  * [44935](https://github.com/space-wizards/space-station-14/pull/44935) Fix Telepad order duplication
  * [44937](https://github.com/space-wizards/space-station-14/pull/44937) Fix Telepad is able to shutdown
  * [44939](https://github.com/space-wizards/space-station-14/pull/44939) Cleanup implant tags
  * [44944](https://github.com/space-wizards/space-station-14/pull/44944) Artifact Triggers - Interact using Entity
  * [44947](https://github.com/space-wizards/space-station-14/pull/44947) Improve VehicleCanRunEvent
  * [44948](https://github.com/space-wizards/space-station-14/pull/44948) Resized survival box and added flare back
    * `Nem`: I prefer the original solution proposed by @[Adjustments to emergency locker fills](mention://9add8676-2a75-406a-bc49-c36e7383e711/pull_request/05fb081b-b618-4c73-b7cd-6f9d238688e9) (Prior to it being changed again to account for flares in the survival box)
  * [44950](https://github.com/space-wizards/space-station-14/pull/44950) [Hotfix] Audio emote
  * [44952](https://github.com/space-wizards/space-station-14/pull/44952) Hotfix: Fix mistaken AudioParams.WithVariation calls + LockComponent cleanup
  * [44957](https://github.com/space-wizards/space-station-14/pull/44957) Hotfix: Add and apply LightMaskPrototypes from #34056
  * [44959](https://github.com/space-wizards/space-station-14/pull/44959) Fix broken syntax is some scripts
  * [44960](https://github.com/space-wizards/space-station-14/pull/44960) Fix a dumb bug with the changeling's screech
  * [44961](https://github.com/space-wizards/space-station-14/pull/44961) fix: make bluespace beaker normal sized item like large beaker
  * [44963](https://github.com/space-wizards/space-station-14/pull/44963) Move MutingSystem to Shared, update Deathgasp/VentriloquistPuppetSystem.
  * [44964](https://github.com/space-wizards/space-station-14/pull/44964) Fix vehicles retaining movement input after unbuckling
  * [44965](https://github.com/space-wizards/space-station-14/pull/44965) Move SuicideSystem into its own directory
  * [44967](https://github.com/space-wizards/space-station-14/pull/44967) RecyclerLoopTest: check all materials, simplify test.
  * [44973](https://github.com/space-wizards/space-station-14/pull/44973) Refactor interaction outline
  * [44977](https://github.com/space-wizards/space-station-14/pull/44977) Give mobs amusing name prefixes
  * [44978](https://github.com/space-wizards/space-station-14/pull/44978) Bugfix: Added arachnid metabolism to all chems with Animal Bloodstream metabolism.
  * [44979](https://github.com/space-wizards/space-station-14/pull/44979) [STABLE] v283.1.3
  * [44980](https://github.com/space-wizards/space-station-14/pull/44980) v284.0.2
  * [44982](https://github.com/space-wizards/space-station-14/pull/44982) Fix stack test async + stack system warning
  * [44994](https://github.com/space-wizards/space-station-14/pull/44994) Fix ShouldIgnoreRestrictions logic
  * [44995](https://github.com/space-wizards/space-station-14/pull/44995) Make AFK events shared
  * [44996](https://github.com/space-wizards/space-station-14/pull/44996) [Hotfix] Map limits are now 65. Jobs completely rebalanced into 3 Pops. Reach gone.
  * [44998](https://github.com/space-wizards/space-station-14/pull/44998) Changeling Guidebook
  * [45003](https://github.com/space-wizards/space-station-14/pull/45003) Add Head tag to OrganBaseHead
  * [45004](https://github.com/space-wizards/space-station-14/pull/45004) C4 can no longer be stuck to hardsuit helmets
  * [45006](https://github.com/space-wizards/space-station-14/pull/45006) TriggerOnCollision for Impact Grenades
  * [45008](https://github.com/space-wizards/space-station-14/pull/45008) Replace "Wall" tag with WallComponent
  * [45009](https://github.com/space-wizards/space-station-14/pull/45009) Minor SharedRoleSystem code cleanup
  * [45011](https://github.com/space-wizards/space-station-14/pull/45011) [Hotfix] Update the Wizden maxpop count
  * [45012](https://github.com/space-wizards/space-station-14/pull/45012) Stable into master
  * [45013](https://github.com/space-wizards/space-station-14/pull/45013) Bugfix: Guardian popup spam, mech attack blocker
  * [45014](https://github.com/space-wizards/space-station-14/pull/45014) Fix guidebook typos
  * [45017](https://github.com/space-wizards/space-station-14/pull/45017) Added Sushi Station
  * [45018](https://github.com/space-wizards/space-station-14/pull/45018) centcomm update
  * [45019](https://github.com/space-wizards/space-station-14/pull/45019) Refactor animal reagent/entity production
  * [45020](https://github.com/space-wizards/space-station-14/pull/45020) Revert - Remove The Throngler from Grand Lottery - #28060
  * [45022](https://github.com/space-wizards/space-station-14/pull/45022) Make more ApcPowerReceiverComponent fields DataFields
  * [45023](https://github.com/space-wizards/space-station-14/pull/45023) Revert - Remove throngler lottery mention from Tips - #28073
  * [45024](https://github.com/space-wizards/space-station-14/pull/45024) Cluwne Agent ID UI Fix
  * [45033](https://github.com/space-wizards/space-station-14/pull/45033) Make brass items grind directly into brass, add extra recipes for brass.
  * [45036](https://github.com/space-wizards/space-station-14/pull/45036) Mech Control Panel now closes on Pilot Eject.
  * [45040](https://github.com/space-wizards/space-station-14/pull/45040) Artifact Triggers - Attacks/Collisions
  * [45041](https://github.com/space-wizards/space-station-14/pull/45041) Unify blink and katana dash teleportation (also removed EnergyKatana system/component)
  * [45043](https://github.com/space-wizards/space-station-14/pull/45043) Made contraband flippos more accesible to non-antags
  * [45044](https://github.com/space-wizards/space-station-14/pull/45044) add disable ghost bubbles if ghost not visibility
  * [45045](https://github.com/space-wizards/space-station-14/pull/45045) Hand blocker for vehicles (and mechs)
  * [45047](https://github.com/space-wizards/space-station-14/pull/45047) Fixing sprite license issues & metadata cleanup
  * [45049](https://github.com/space-wizards/space-station-14/pull/45049) Changeling Store Identity Count Condition
  * [45051](https://github.com/space-wizards/space-station-14/pull/45051) map proto fixes
  * [45052](https://github.com/space-wizards/space-station-14/pull/45052) Shorten goliath stun duration
  * [45053](https://github.com/space-wizards/space-station-14/pull/45053) snowball update
  * [45054](https://github.com/space-wizards/space-station-14/pull/45054) Minor tram driver fixes
  * [45055](https://github.com/space-wizards/space-station-14/pull/45055) Fix percussion channel and switch to one-based channel indexes in instrument UI.
  * [45056](https://github.com/space-wizards/space-station-14/pull/45056) Job weight rework
    * `Scar`: This broke job selection altogether. Or rather changed it to a degree players really disliked. You shouldn’t be forced to play roles you have set to “Never”. Already a Release Blocker.
  * [45057](https://github.com/space-wizards/space-station-14/pull/45057) Add job prio commands
  * [45058](https://github.com/space-wizards/space-station-14/pull/45058) Fix windoors failing to close when placed next to walls
  * [45061](https://github.com/space-wizards/space-station-14/pull/45061) refactor: change cache-dependent commands to use _IPrototypeManager.Categories
  * [45062](https://github.com/space-wizards/space-station-14/pull/45062) Let Defibrillators be used on anything
  * [45063](https://github.com/space-wizards/space-station-14/pull/45063) Bugfix: Holosigns, dragon rifts align themselves with the grid
  * [45064](https://github.com/space-wizards/space-station-14/pull/45064) Updated Sushi Station with feedback
  * [45065](https://github.com/space-wizards/space-station-14/pull/45065) Fix comm console alert button
  * [45066](https://github.com/space-wizards/space-station-14/pull/45066) Conveyor belts actions tweak
  * [45067](https://github.com/space-wizards/space-station-14/pull/45067) Bugfix: Metamorphic glass overlay layers show incorrectly.
  * [45069](https://github.com/space-wizards/space-station-14/pull/45069) Make heisendetector open new issues
  * [45070](https://github.com/space-wizards/space-station-14/pull/45070) Cleanup event handler methods with nullable parameters
  * [45071](https://github.com/space-wizards/space-station-14/pull/45071) Update RobustToolbox to 285.0.1
  * [45072](https://github.com/space-wizards/space-station-14/pull/45072) Bugfix: destructible disposals, empty contents on destruction
  * [45074](https://github.com/space-wizards/space-station-14/pull/45074) Refresh both weightless and movement speed modifiers on each refresh call.
  * [45075](https://github.com/space-wizards/space-station-14/pull/45075) Update submodule to 286.0.0
  * [45077](https://github.com/space-wizards/space-station-14/pull/45077) Fix machine frames crashing game when destroyed by gun
  * [45079](https://github.com/space-wizards/space-station-14/pull/45079) Fix entity leak in SaveLoadSaveTest, StackTest cleanup
  * [45085](https://github.com/space-wizards/space-station-14/pull/45085) Fix UIBox2 assert failures
    * `Aeshus`: UIBox2 caused a lot of build issues across the codebase, but they should all be fixed now with the latest RT merge. 
  * [45088](https://github.com/space-wizards/space-station-14/pull/45088) Astro-tile consistency pass
  * [45089](https://github.com/space-wizards/space-station-14/pull/45089) Fix ActionUI allocations
  * [45090](https://github.com/space-wizards/space-station-14/pull/45090) Make GetEyeOffsetRelayedEvent a struct
  * [45094](https://github.com/space-wizards/space-station-14/pull/45094) Remove gravity component from generated space dungeons
  * [45095](https://github.com/space-wizards/space-station-14/pull/45095) update namespace for shared ghost folder
  * [45096](https://github.com/space-wizards/space-station-14/pull/45096) Bagel Station - issue fixes
  * [45097](https://github.com/space-wizards/space-station-14/pull/45097) BreakerFlipRule tweaks and ApcToggleBreaker cleanup
  * [45099](https://github.com/space-wizards/space-station-14/pull/45099) Box Station - Issues fixes
  * [45100](https://github.com/space-wizards/space-station-14/pull/45100) map proto fixes (#45051)
  * [45101](https://github.com/space-wizards/space-station-14/pull/45101) Hardsuit Helmet, Hardhat, Fire Helmet Lights Redux
  * [45102](https://github.com/space-wizards/space-station-14/pull/45102) fix jug saying it's filled, when it's not
  * [45103](https://github.com/space-wizards/space-station-14/pull/45103) Always raise MobStateChanged on client
  * [45104](https://github.com/space-wizards/space-station-14/pull/45104) Changeling Regen Stasis
  * [45105](https://github.com/space-wizards/space-station-14/pull/45105) Xenoborg crystal
  * [45106](https://github.com/space-wizards/space-station-14/pull/45106) Misc/Old Inhand Fixes
  * [45108](https://github.com/space-wizards/space-station-14/pull/45108) Update stealth shader to use SCREEN_UV
  * [45111](https://github.com/space-wizards/space-station-14/pull/45111) Elkridge Station - Issues fixes
  * [45112](https://github.com/space-wizards/space-station-14/pull/45112) Bugfix: You can once again hear when you talk.
  * [45113](https://github.com/space-wizards/space-station-14/pull/45113) refactor: small selection of tests for EntityTableSystem
  * [45114](https://github.com/space-wizards/space-station-14/pull/45114) Marathon Station - Issues fixes
  * [45121](https://github.com/space-wizards/space-station-14/pull/45121) Map packed issues
  * [45123](https://github.com/space-wizards/space-station-14/pull/45123) [Internal] [Fix] Behonker type fixes
  * [45124](https://github.com/space-wizards/space-station-14/pull/45124) Add toggle to the AFK automatic checks for downstreams
  * [45125](https://github.com/space-wizards/space-station-14/pull/45125) Plasma Station - Issues fixes
  * [45131](https://github.com/space-wizards/space-station-14/pull/45131) Snowball update
  * [45132](https://github.com/space-wizards/space-station-14/pull/45132) Bureaucracy Inhands
  * [45138](https://github.com/space-wizards/space-station-14/pull/45138) Plasma Station - Redone belts and recyclers
  * [45140](https://github.com/space-wizards/space-station-14/pull/45140) Bugfix: Better lifecycle handling for DisposalHolderComponent and BeingDisposedComponent
  * [45141](https://github.com/space-wizards/space-station-14/pull/45141) Clearing borg hands fix
  * [45142](https://github.com/space-wizards/space-station-14/pull/45142) Lights fixes while mapping + yml cleanup
  * [45143](https://github.com/space-wizards/space-station-14/pull/45143) Add scream emote for chasm falls (reviving #44075)
  * [45148](https://github.com/space-wizards/space-station-14/pull/45148) Feature/issue 41116 artifacts partial fix
  * [45149](https://github.com/space-wizards/space-station-14/pull/45149) Replace some usages of object reads with generic type reads
  * [45150](https://github.com/space-wizards/space-station-14/pull/45150) Fix GasMaxPressureHolderComponent.Air relying on serialization to not be null
  * [45151](https://github.com/space-wizards/space-station-14/pull/45151) Make creating the database not take 2 whole seconds in integration tests
  * [45152](https://github.com/space-wizards/space-station-14/pull/45152) Add xenoborg bio knife
  * [45154](https://github.com/space-wizards/space-station-14/pull/45154) Scrap Inhands (+Extra)
  * [45157](https://github.com/space-wizards/space-station-14/pull/45157) Add Strawberry Ice
    * `Aada`: I’m not sure about having a stronger desoxy + stronger downside, rather than balancing desoxy and its downsides to be the desired chem for the job.
    * `Relay from downstream - HiveHum`: Concerns about the effects, theming and details @[https://discord.com/channels/310555209753690112/310555209753690112/1540816285279977492](mention://3f70ba1e-66de-4ae7-8820-73853d6edf9f/url/e48fe676-6817-41b3-af53-9bc6b38dc191) Being addressed in thread
  * [45158](https://github.com/space-wizards/space-station-14/pull/45158) refactor: removed IsFirstTimePredicted misuse
  * [45160](https://github.com/space-wizards/space-station-14/pull/45160) Packed Station - cryogenics issue, and minor improvments
  * [45161](https://github.com/space-wizards/space-station-14/pull/45161) Elkridge Station - cryogenics issue
  * [45164](https://github.com/space-wizards/space-station-14/pull/45164) Changelog test publishes
  * [45165](https://github.com/space-wizards/space-station-14/pull/45165) Move DamageOverlay to an Entity System + Component
  * [45168](https://github.com/space-wizards/space-station-14/pull/45168) Xenoborg laser resprite
  * [45170](https://github.com/space-wizards/space-station-14/pull/45170) Ninja first name error fix
  * [45171](https://github.com/space-wizards/space-station-14/pull/45171) Smart equip fixes: Allow you to smart-equip guns without...
  * [45174](https://github.com/space-wizards/space-station-14/pull/45174) Bugfix: Better RCD LocId handling.
  * [45178](https://github.com/space-wizards/space-station-14/pull/45178) Fix light tube sprite
  * [45179](https://github.com/space-wizards/space-station-14/pull/45179) Remove TCS for constructioncomponentvalid
  * [45180](https://github.com/space-wizards/space-station-14/pull/45180) Update submodule to 287.0.0
  * [45181](https://github.com/space-wizards/space-station-14/pull/45181) Clearing borg hands fix (#45141)
  * [45186](https://github.com/space-wizards/space-station-14/pull/45186) Ignore space tiles for rooves
  * [45187](https://github.com/space-wizards/space-station-14/pull/45187) Add spacelight
  * [45188](https://github.com/space-wizards/space-station-14/pull/45188) Prevent StatusEffect relay "collection modified" error
  * [45190](https://github.com/space-wizards/space-station-14/pull/45190) Tram update
  * [45193](https://github.com/space-wizards/space-station-14/pull/45193) Give Xenoborgs EMP resistance
  * [45194](https://github.com/space-wizards/space-station-14/pull/45194) Rebalance mothership modules
  * [45195](https://github.com/space-wizards/space-station-14/pull/45195) [Hotfix] Increase Server Population limit to 80
  * [45196](https://github.com/space-wizards/space-station-14/pull/45196) STABLE -> MASTER
  * [45197](https://github.com/space-wizards/space-station-14/pull/45197) Update engine to 288.0.0 and fix tests.
  * [45199](https://github.com/space-wizards/space-station-14/pull/45199) Fix firespreading test
  * [45201](https://github.com/space-wizards/space-station-14/pull/45201) Update submodule to 288.0.1
  * [45202](https://github.com/space-wizards/space-station-14/pull/45202) Big prototype and datafield cleanup
  * [45208](https://github.com/space-wizards/space-station-14/pull/45208) MapLight added to maps
  * [45210](https://github.com/space-wizards/space-station-14/pull/45210) Fix decal prediction
  * [45215](https://github.com/space-wizards/space-station-14/pull/45215) Add ignored departments for fallback
  * [45220](https://github.com/space-wizards/space-station-14/pull/45220) Make every EntitySystem partial
  * [45224](https://github.com/space-wizards/space-station-14/pull/45224) Fix decal dirtying
  * [45226](https://github.com/space-wizards/space-station-14/pull/45226) Disable resource auto deletion in tests
  * [45227](https://github.com/space-wizards/space-station-14/pull/45227) Fix ReflectComponents.cs spread comment
  * [45229](https://github.com/space-wizards/space-station-14/pull/45229) Mouse now has black eyes instead of red when being held
  * [45230](https://github.com/space-wizards/space-station-14/pull/45230) Increase diona thirst decay rate
  * [45234](https://github.com/space-wizards/space-station-14/pull/45234) Cleanup: Resolve GetAnchoredEntitiesEnumerator, Get\*TilesEnumerator warnings
  * [45237](https://github.com/space-wizards/space-station-14/pull/45237) Heisentests: SkinColorationStrategy.VerifyClamped for nearby RGB lookup, avoid HSV/HSL roundtrips
  * [45239](https://github.com/space-wizards/space-station-14/pull/45239) Changeling Chemicals
  * [45240](https://github.com/space-wizards/space-station-14/pull/45240) Examinable doafters
  * [45241](https://github.com/space-wizards/space-station-14/pull/45241) Snowball Station Parallax
  * [45242](https://github.com/space-wizards/space-station-14/pull/45242) QM Turtleneck Tactical Switch
  * [45244](https://github.com/space-wizards/space-station-14/pull/45244) Make satiation able to increase over time & reframe satiation not assuming it decays by default
  * [45247](https://github.com/space-wizards/space-station-14/pull/45247) Xenoborg guided missile
  * [45250](https://github.com/space-wizards/space-station-14/pull/45250) bagel update
  * [45253](https://github.com/space-wizards/space-station-14/pull/45253) Fix Botany refactor
  * [45256](https://github.com/space-wizards/space-station-14/pull/45256) Fix Dwarf Displacement Cloning
  * [45260](https://github.com/space-wizards/space-station-14/pull/45260) Cull LINQ from `SatiationSystem`'s `Update`
  * [45261](https://github.com/space-wizards/space-station-14/pull/45261) Fix agent ID cards not spawning with intended access
  * [45262](https://github.com/space-wizards/space-station-14/pull/45262) Clumsy status effect + tests
  * [45263](https://github.com/space-wizards/space-station-14/pull/45263) Bugfix: SharedForensicsSystem: correct entity in Resolve, cleanup
  * [45265](https://github.com/space-wizards/space-station-14/pull/45265) Prevent forced Emotes from reagents getting recorded in chat.
  * [45266](https://github.com/space-wizards/space-station-14/pull/45266) Fix Airlock(Windoor) state on reconnect
  * [45268](https://github.com/space-wizards/space-station-14/pull/45268) Move BecomesStationComponent to Shared
  * [45269](https://github.com/space-wizards/space-station-14/pull/45269) Localize hydroxysomnolene popups
  * [45278](https://github.com/space-wizards/space-station-14/pull/45278) Examinable tool doafter
  * [45279](https://github.com/space-wizards/space-station-14/pull/45279) ThrowingSystem.TryThrow methods return a result now
  * [45283](https://github.com/space-wizards/space-station-14/pull/45283) XATInteractWith multiple-nodes bugfix
  * [45284](https://github.com/space-wizards/space-station-14/pull/45284) Refactor ItemSlotsSystem and fix insertion/ejection handling
  * [45286](https://github.com/space-wizards/space-station-14/pull/45286) Fix TryThrow returns from #45279
  * [45287](https://github.com/space-wizards/space-station-14/pull/45287) Drunk status effect additions (clumsiness)
  * [45296](https://github.com/space-wizards/space-station-14/pull/45296) Make cuff timer reduction only apply when stamcrit, asleep or crit/dead
  * [45298](https://github.com/space-wizards/space-station-14/pull/45298) Fix `GuidebookDataSystem` late MsgEntity warning
  * [45300](https://github.com/space-wizards/space-station-14/pull/45300) centcomm update
  * [45301](https://github.com/space-wizards/space-station-14/pull/45301) bagel update
  * [45302](https://github.com/space-wizards/space-station-14/pull/45302) derotate 3 maps
  * [45303](https://github.com/space-wizards/space-station-14/pull/45303) box update
  * [45304](https://github.com/space-wizards/space-station-14/pull/45304) packed update
  * [45305](https://github.com/space-wizards/space-station-14/pull/45305) relic update
  * [45306](https://github.com/space-wizards/space-station-14/pull/45306) snowball update
  * [45307](https://github.com/space-wizards/space-station-14/pull/45307) sushi update
  * [45308](https://github.com/space-wizards/space-station-14/pull/45308) tram2 update
  * [45309](https://github.com/space-wizards/space-station-14/pull/45309) update wizards den, nukieplanet, deathmatch maps
  * [45311](https://github.com/space-wizards/space-station-14/pull/45311) terminal update
  * [45312](https://github.com/space-wizards/space-station-14/pull/45312) update emergency shuttles and infiltrator
  * [45313](https://github.com/space-wizards/space-station-14/pull/45313) Update Exo
  * [45314](https://github.com/space-wizards/space-station-14/pull/45314) Gas resprites
  * [45315](https://github.com/space-wizards/space-station-14/pull/45315) marathon update
  * [45319](https://github.com/space-wizards/space-station-14/pull/45319) Making sure Elkridge follows the Respritening's guideline thingies
  * [45320](https://github.com/space-wizards/space-station-14/pull/45320) Update Plasma Station (Respritening)
  * [45325](https://github.com/space-wizards/space-station-14/pull/45325) Update submodule to 288.1.0
  * [45326](https://github.com/space-wizards/space-station-14/pull/45326) Update Automated Trade Station with respritening
  * [45327](https://github.com/space-wizards/space-station-14/pull/45327) Elkridge respritening changes fix
  * [45328](https://github.com/space-wizards/space-station-14/pull/45328) Update salv dungeons to work with the respritening
  * [45329](https://github.com/space-wizards/space-station-14/pull/45329) Xenoborg module recipes and blacklists
  * [45330](https://github.com/space-wizards/space-station-14/pull/45330) Fix Botany refactor 2
  * [45333](https://github.com/space-wizards/space-station-14/pull/45333) Remove duplicate cmd-replay-toggleui-desc localization
  * [45335](https://github.com/space-wizards/space-station-14/pull/45335) Fix WeaponRandomSystem overriding bonus damage
  * [45336](https://github.com/space-wizards/space-station-14/pull/45336) Replace repeated #1B1B1E panel backgrounds with shared styles
  * [45337](https://github.com/space-wizards/space-station-14/pull/45337) Fix unbuckling from office chairs and being under them
  * [45340](https://github.com/space-wizards/space-station-14/pull/45340) Uplink renaming
  * [45346](https://github.com/space-wizards/space-station-14/pull/45346) Extract notify on non-functioning from emitter
  * [45349](https://github.com/space-wizards/space-station-14/pull/45349) Update exo with the `align` command
  * [45352](https://github.com/space-wizards/space-station-14/pull/45352) Fix secret door drawdepth
  * [45354](https://github.com/space-wizards/space-station-14/pull/45354) Add generic container vehicle entry and exit handling
  * [45355](https://github.com/space-wizards/space-station-14/pull/45355) Janimaid smite fix!!!
  * [45359](https://github.com/space-wizards/space-station-14/pull/45359) Buffed the weakest xenoborg modules
  * [45362](https://github.com/space-wizards/space-station-14/pull/45362) Xenoborg Rocket module
  * [45366](https://github.com/space-wizards/space-station-14/pull/45366) Fix examinable item toggle status
  * [45370](https://github.com/space-wizards/space-station-14/pull/45370) Minor weather fix
  * [45378](https://github.com/space-wizards/space-station-14/pull/45378) Admin remarks notification
  * [45379](https://github.com/space-wizards/space-station-14/pull/45379) Changeling Total Identity Count Tracker + Admin-Only Objectives For Testing
  * [45382](https://github.com/space-wizards/space-station-14/pull/45382) Error on CS8785 source gen warnings
  * [45393](https://github.com/space-wizards/space-station-14/pull/45393) Fix ahelp window not appearing on first init
  * [45394](https://github.com/space-wizards/space-station-14/pull/45394) Pause passive regen for 5 seconds after taking damage
  * [45395](https://github.com/space-wizards/space-station-14/pull/45395) Structure Aligner System
  * [45399](https://github.com/space-wizards/space-station-14/pull/45399) Fix UI Window Memory Leak in `CloseRecentWindowUIController`
  * [45401](https://github.com/space-wizards/space-station-14/pull/45401) Surveillance camera & monitoring UI - bugfix & cleanup
  * [45405](https://github.com/space-wizards/space-station-14/pull/45405) You can now drink from sinks
  * [45409](https://github.com/space-wizards/space-station-14/pull/45409) Respritening Batch 1 Polish & Airlocks overhaul
  * [45410](https://github.com/space-wizards/space-station-14/pull/45410) Fix puddle mispredicts
  * [45413](https://github.com/space-wizards/space-station-14/pull/45413) Changeling Transformation Automatic Drop
  * [45417](https://github.com/space-wizards/space-station-14/pull/45417) Structure Rebalance followup
  * [45424](https://github.com/space-wizards/space-station-14/pull/45424) Butchering Bugfix for Slicing Tools
  * [45426](https://github.com/space-wizards/space-station-14/pull/45426) [MICROBALANCE PR] BUFF MAX CAPS A LITTLE BIT
  * [45431](https://github.com/space-wizards/space-station-14/pull/45431) Remove Neurotoxin Bar Drink
  * [45434](https://github.com/space-wizards/space-station-14/pull/45434) Fix OpenAL device display
  * [45437](https://github.com/space-wizards/space-station-14/pull/45437) Movement Modifier Status Effect fix
  * [45439](https://github.com/space-wizards/space-station-14/pull/45439) Ambuzol rework
  * [45447](https://github.com/space-wizards/space-station-14/pull/45447) Fix xenoborg guided missile launcher being able to cycle the missiles
  * [45449](https://github.com/space-wizards/space-station-14/pull/45449) Remove empty steps from construction menu.
  * [45460](https://github.com/space-wizards/space-station-14/pull/45460) Changeling Headslug Nerf and Buff
  * [45461](https://github.com/space-wizards/space-station-14/pull/45461) publish pipeline now commits changelog, READY FOR STABLE
  * [45462](https://github.com/space-wizards/space-station-14/pull/45462) Enable changelings
    * `Scar`: :grinning:
  * [45464](https://github.com/space-wizards/space-station-14/pull/45464) [MALD PR] fix the AI door menu
    * `Aeshus`: The source of this bug was really weird, as it seemed to have been implicitly casting an `T[]` to a `Span<T>` to access the Span’s `Span.Sort()` method (like is available for other collection types), which behaves differently than `Array.Sort(arr)`. Something about covariance/contravariance. Should probably have an analyzer to make sure this doesn’t happen again.
    * `Aeshus`: Also, do we have a policy on PR names (e.g. “[MALD PR]” for a bug fix)
  * [45468](https://github.com/space-wizards/space-station-14/pull/45468) Fix Grille Iconsmooth
  * [45472](https://github.com/space-wizards/space-station-14/pull/45472) Fix Communal Satiation
  * [45477](https://github.com/space-wizards/space-station-14/pull/45477) Fix Mobstate Ling Bug
  * [45478](https://github.com/space-wizards/space-station-14/pull/45478) .editorconfig: prefer case block braces on same level as `case`
  * [45481](https://github.com/space-wizards/space-station-14/pull/45481) Change minimum job fallback to 'None'
  * [45492](https://github.com/space-wizards/space-station-14/pull/45492) Buff armblade damage.
  * [45493](https://github.com/space-wizards/space-station-14/pull/45493) Add GravityAffected to SeatBase
  * [45503](https://github.com/space-wizards/space-station-14/pull/45503) Bugfix: SharedEntitySystem.Remove parents you to the grid or the map.
  * [45506](https://github.com/space-wizards/space-station-14/pull/45506) Add a confirmation message to the regenerative stasis action
  * [45507](https://github.com/space-wizards/space-station-14/pull/45507) Snails & snoths now use adjectives instead of numeric identifiers
  * [45514](https://github.com/space-wizards/space-station-14/pull/45514) Rate limit emitters, only raise PowerStateChanged on a change in state.
  * [45516](https://github.com/space-wizards/space-station-14/pull/45516) Nerf xenoborg rocket module
  * [45519](https://github.com/space-wizards/space-station-14/pull/45519) Tweaked Hristov attributes
  * [45520](https://github.com/space-wizards/space-station-14/pull/45520) Variantize autofill
    * `Aeshus`: Changes some LocIDs, do we care about keeping them consistent? Is this a problem for localization forks?
  * [45522](https://github.com/space-wizards/space-station-14/pull/45522) Changeling Mute Sting + balance/bug pass
  * [45525](https://github.com/space-wizards/space-station-14/pull/45525) add missing plastic tile items
  * [45530](https://github.com/space-wizards/space-station-14/pull/45530) Fix vim guide string
  * [45534](https://github.com/space-wizards/space-station-14/pull/45534) Fix Emote Sounds not loading in vocalsystem
  * [45536](https://github.com/space-wizards/space-station-14/pull/45536) Moved Pax from Toxins.yml to Narcotics.yml
  * [45538](https://github.com/space-wizards/space-station-14/pull/45538) Fix bow and arrow shooting yourself
  * [45539](https://github.com/space-wizards/space-station-14/pull/45539) added girlmeth to maintspill loot table and add contra label
    * `Aeshus`: This is a PR name of all time.
  * [45544](https://github.com/space-wizards/space-station-14/pull/45544) Update main window method
  * [45545](https://github.com/space-wizards/space-station-14/pull/45545) Update submodule to 289.0.0

# Question Time!

## What was in the UI meeting?

Discussed the art direction and vibe for what UI/UX should be in the future. Mostly just groundwork laying and not much else.

## For Botany Meeting would there be a way to sign up?

We need a way for people to be aware of design meetings and be able to sign up if they are particularly experienced or whatever.

## Have yall heard about the twitch intergration plugin that durk is working on, and would you be open to including some of the basic non round affecting effects on wizden?

We have, we are in support of it, we would like to add engine support for it and help it get finished, and we probably would want to have support for it on Wizden for events and such.

## Have there been further discussions about what we possibly/want to do to get Vulture to be more active?

More playtests! More features!!!

## Art Bible / Style Guide when?

It’s being worked on, we need a base tileset first though :)

## Will the salv section of the dev enviorment ever be finished? 

Yes. Eventually!

## Mapping lead, we might need a new mapping lead; What do you have to do to be a mapping lead? New maintainers???????

Mapping leads are “““hired””” on a case-by-case basis. If you want to be seen as a potential mapping lead you should be good on map design/level design and be active in review - though we’re really looking for maptainers that are willing to bang out issues with maps that violate the (to be made) mapping guidelines.

We really only want 3 Map Leads at most.

## Are we going for [https://github.com/space-wizards/docs/pull/671/changes](https://github.com/space-wizards/docs/pull/671/changes "https://github.com/space-wizards/docs/pull/671/changes") ?

It has been merged :sunglasses:

## Yo question, are documents like species docs and stuff going to be reviewed again soon?

Yes, they need to be moved to outline or another website. We want all of our design docs in one place that’s easier to edit compared to Github.

## DB changes, are they currently viable to get reviewed in a timely manner?

I'm pretty much open to DB changes, just be aware that its just not my own opinion on it, and there for wait times may be long before stuff is handled, *looks at admin logs stuff I've been trying to push through*...

## Is there any discussion about making a features wishlist/roadmap like RMC?

Yes, we have a few but they’re outdated or disorganized. We have a couple specialized roadmaps which are available but that’s about it :P


Releases since the last non-squashed PR: 0 :cry:


*Niko is a cat*

^ Hes a wolf actually. Nik is a cat.