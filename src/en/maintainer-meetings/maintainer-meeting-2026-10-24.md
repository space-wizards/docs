# 2026-10-24 Maintainer Meeting

:::info
## Maintainers In Attendance

* Nem
* SlamBamActionMan (NOT A REAL MAINT)
* Ress (Infra)
* Errant
* Fildrance
* Orks
* AJCM
* Pok

:::

(Meeting recording goes here)

# Topics

## Release Update Policy, take 2 (Fildrance?)

We were supposed to review <https://github.com/space-wizards/docs/pull/676> the last time, but it got postponed to allow the game director to participate in the talks. Then things happened, so nothing about this got done. We should probably do this talk now, then.

**ACTION (NEM) Set up meeting next week to discuss**

## Release Update Policy, addendum (Errant)

Regardless of the outcome of the previous topic, I would like to come to a consensus on one specific point, move staging cutoff to earlier than Thursday. Even if we agree on nothing else for now, let’s talk about this and/or do a vote, and start doing staging cutoff/blocker tracking earlier in the future. (Proposal was the Saturday of the preceding week)

* Potential issue brought up by Princess Cheeseballs: extending the time between cutoff and release means that important fixes in that timeframe will be delayed for much longer.

## Put levi on staging?

Seems to have reasonable support from the maintainer group.

**ACTION (Errant) Bring a plan to devops for review (flowchart of actions)**

# Release Blockers

* ~~Several issues and concerns with Blinking? Need specifics~~
  * ~~Bloat on the action bar~~ 
  * ~~Balance concerns regarding Flashes~~
  * ~~Hotfix~~ [~~#46552 Remove the close eyes action~~](https://github.com/space-wizards/space-station-14/pull/46552) ~~seems like it will address both of these aspects~~
    * ~~ACTION (AJCM-git)~~
  * ~~Anything else?~~
  * Fix was merged and resolves this being a blocker. Should still be looked at afterwards
* ~~Things anchored to grids are not properly centered, and look weird~~
  * ~~Confirmed fixed on latest engine, we just need to include a new engine release in staging. (And hope that it brings no new issues, because we are still not testing staging changes at scale)~~
  * ~~Fixed via~~ @[Fix anchorentity not snapping to tile center](mention://c8e5cc82-27c7-485d-b636-6f94933e46cf/pull_request/56546e57-c30d-4040-b7a0-d16e8d50c776) 
  * ~~Engine version hotfix~~ [~~46570~~](https://github.com/space-wizards/space-station-14/pull/46570 "https://github.com/space-wizards/space-station-14/pull/46570") 
  * Fix was merged
* ~~Hotfix~~ [~~#46528 Fix vacuum shader~~](https://github.com/space-wizards/space-station-14/pull/46528) ~~?~~
  * **~~ACTION (NEM) Review and merge~~**
  * Merged

* ~~Partial Revert vote Vending machine ghostroles~~
  * ~~PR open~~ [~~https://github.com/space-wizards/space-station-14/pull/46590~~](https://github.com/space-wizards/space-station-14/pull/46590) ~~needs one more code review~~
  * Merged
* ~~Partial Revert vote Janibelt tools~~
  * ~~PR open~~ [~~https://github.com/space-wizards/space-station-14/pull/46591~~](https://github.com/space-wizards/space-station-14/pull/46591) ~~needs one more code review~~
  * Merged


* ~~FTL fix~~ 
  * ~~PR open~~ [~~https://github.com/space-wizards/space-station-14/pull/46577~~](https://github.com/space-wizards/space-station-14/pull/46577)
  * It’s going straight to stable, so no longer considered a blocker for the release\n

# I read through the PR list:

* Nem
* AJCM-git
* Errant
* Pok

# PR List

* [46166](https://github.com/space-wizards/space-station-14/pull/46166) EVA Storage is now Command+External access
* [46170](https://github.com/space-wizards/space-station-14/pull/46170) Blood-Red Magboots on NukeOps
* [45828](https://github.com/space-wizards/space-station-14/pull/45828) Franks Funky Fertilizer
* [45696](https://github.com/space-wizards/space-station-14/pull/45696) the return of ambigen13.ogg
* [45500](https://github.com/space-wizards/space-station-14/pull/45500) Injectable & drawable monkey cubes
* [45452](https://github.com/space-wizards/space-station-14/pull/45452) Mild Cryopod changes before stable
* [45420](https://github.com/space-wizards/space-station-14/pull/45420) Move edit button in PermissionsEui
* [46164](https://github.com/space-wizards/space-station-14/pull/46164) Add two new posters based on Raptor and Vulture
* [46180](https://github.com/space-wizards/space-station-14/pull/46180) Respritening: subtly adjust contrast for floor tiles
* [46178](https://github.com/space-wizards/space-station-14/pull/46178) Respritening: New cardboard_special
* [46181](https://github.com/space-wizards/space-station-14/pull/46181) Respritening: Correct missing attribution to marianolarre
* [46183](https://github.com/space-wizards/space-station-14/pull/46183) Respritening: Split suit_storage.rsi into door and effects counterparts
* [46188](https://github.com/space-wizards/space-station-14/pull/46188) Respritening: Fix style for all closet related YAML
* [46189](https://github.com/space-wizards/space-station-14/pull/46189) Respritening: New closets, lockers, wallmounted lockers, and wardrobes!
* [46179](https://github.com/space-wizards/space-station-14/pull/46179) Respritening: Move cardboard_special to its own RSI
* [46193](https://github.com/space-wizards/space-station-14/pull/46193) Bloodstream multiplier is 1.2 instead of 2x
* [46194](https://github.com/space-wizards/space-station-14/pull/46194) Midround Changelings, version 2
* [46197](https://github.com/space-wizards/space-station-14/pull/46197) Fix Dynamic Rule (Real)
  * `Ress`: Go encourage some admins to run a few rounds with it!
    * ACTION (AJCM-git) Ping admins to announce this can be manually done for testing
* [46199](https://github.com/space-wizards/space-station-14/pull/46199) Wizards and Changelings on Dynamic
* [45721](https://github.com/space-wizards/space-station-14/pull/45721) Zombies now have hands (less metagameable in the strip menu) - but they're too clumsy to hold anything.
* [45625](https://github.com/space-wizards/space-station-14/pull/45625) Reopen #45584 Station Map Construction Graph Improvements
* [45523](https://github.com/space-wizards/space-station-14/pull/45523) Upgrades to attribution UI
* [46191](https://github.com/space-wizards/space-station-14/pull/46191) Add examine text for tool refinable entities
* [46228](https://github.com/space-wizards/space-station-14/pull/46228) the press vest is now armour (providing an entire 1% pierce resist)
* [42631](https://github.com/space-wizards/space-station-14/pull/42631) Switch buttons for more power switches
* [46237](https://github.com/space-wizards/space-station-14/pull/46237) Prune unused Sprite assets
* [46249](https://github.com/space-wizards/space-station-14/pull/46249) Tweak dynamic rule a bit
* [46250](https://github.com/space-wizards/space-station-14/pull/46250) Powdered wig touchup
* [46209](https://github.com/space-wizards/space-station-14/pull/46209) Buff nuclear option and add new trigger sound
* [45416](https://github.com/space-wizards/space-station-14/pull/45416) Fix spawn entity guidebook text, missing admin shuttle window fluent keys
* [42710](https://github.com/space-wizards/space-station-14/pull/42710) Minor gas device UI tweaks
* [46200](https://github.com/space-wizards/space-station-14/pull/46200) Thief Command Hardsuits Objective
* [46247](https://github.com/space-wizards/space-station-14/pull/46247) Purchasable Slime Cubes
* [46081](https://github.com/space-wizards/space-station-14/pull/46081) Service Cyborg module touch up
* [46275](https://github.com/space-wizards/space-station-14/pull/46275) Add rear velocity compensation for projectile spells.
* [45482](https://github.com/space-wizards/space-station-14/pull/45482) Updated Solid Headband Sprites
* [42949](https://github.com/space-wizards/space-station-14/pull/42949) Gave the QM a formal dress
* [45814](https://github.com/space-wizards/space-station-14/pull/45814) BananaHonk recipe requires alcohol because it is alcoholic
* [45076](https://github.com/space-wizards/space-station-14/pull/45076) Cleaned up wizard robes + Added new robes
* [43984](https://github.com/space-wizards/space-station-14/pull/43984) Add size whitelist to CrateRodentCage
* [44921](https://github.com/space-wizards/space-station-14/pull/44921) Added Additional Available Alchohol Bottles to Booze Dispenser
* [44144](https://github.com/space-wizards/space-station-14/pull/44144) Move bulldog mags to syndicate
* [46271](https://github.com/space-wizards/space-station-14/pull/46271) In gas mixer, the Primary port is now called Back port
* [46276](https://github.com/space-wizards/space-station-14/pull/46276) Big sprites cleanup (Part 1?)
* [46282](https://github.com/space-wizards/space-station-14/pull/46282) Big sprites cleanup (Part 2)
* [46284](https://github.com/space-wizards/space-station-14/pull/46284) Big sprites cleanup (Part 3)
* [46309](https://github.com/space-wizards/space-station-14/pull/46309) Big sprites cleanup (Part 4)
* [46311](https://github.com/space-wizards/space-station-14/pull/46311) Big sprites cleanup (Part 5)
* [46122](https://github.com/space-wizards/space-station-14/pull/46122) Make logs sliceable
* [46035](https://github.com/space-wizards/space-station-14/pull/46035) Round out Belts to fit more items.
  * `Errant`: I’m confused what’s the rationale for the janibelt getting (the ability to hold) basic tools? How does that intersect with janitorial duties? On the surface level, that part of the change just seems like a bit of power creep since tools are *nice to have* on you?
    * **ACTION (Errant) Trim concern items PR**
* [46038](https://github.com/space-wizards/space-station-14/pull/46038) Vacuum shader
  * `Nem`: I don’t like this approach to communicating hazards to the players.
    * Potential Consensus: Its not ideal but not revert-worthy 
* [43786](https://github.com/space-wizards/space-station-14/pull/43786) Strapable Supplybot
* [45984](https://github.com/space-wizards/space-station-14/pull/45984) Handheld radio now lights up when on.
* [45950](https://github.com/space-wizards/space-station-14/pull/45950) Allow secondary/tertiary config atmos entities to be copied in the map editor
* [46324](https://github.com/space-wizards/space-station-14/pull/46324) Allow Space Cats (and Syndicats) to pilot Vims and fit in pet carriers.
* [38056](https://github.com/space-wizards/space-station-14/pull/38056) Slightly rework pathfinding obstacle avoidance and handling
* [46235](https://github.com/space-wizards/space-station-14/pull/46235) Makes secure weapon crates more difficult to break into
* [46157](https://github.com/space-wizards/space-station-14/pull/46157) Energy Webvest Properly Named
* [45927](https://github.com/space-wizards/space-station-14/pull/45927) give ghost vending machines access to ~~cargo~~ service radio.
  * `Errant`: This seems to have become immediately defunct/irrelevant, given that [45600](https://github.com/space-wizards/space-station-14/pull/45600) removed these ghostroles. See revert vote on that PR
* [46310](https://github.com/space-wizards/space-station-14/pull/46310) Service cooking module fix
* [46336](https://github.com/space-wizards/space-station-14/pull/46336) Remove sunset from jukebox
* [46325](https://github.com/space-wizards/space-station-14/pull/46325) Add a cap to the number of Genetic Ancestor reinforcements a traitor can buy + reduce the cost of the reinforcement.
* [46246](https://github.com/space-wizards/space-station-14/pull/46246) Climbing to collider center
* [46344](https://github.com/space-wizards/space-station-14/pull/46344) Construction menu search bar grabs focus on opening
* [43031](https://github.com/space-wizards/space-station-14/pull/43031) Improve usability of basic cooking ingredient containers
* [46084](https://github.com/space-wizards/space-station-14/pull/46084) Show nukie reinforcements as nuclear operatives at round end
* [46314](https://github.com/space-wizards/space-station-14/pull/46314) Don't make the ‘ghost roles’ button red if the ghost roles window is already open.
* [46340](https://github.com/space-wizards/space-station-14/pull/46340) Vape item usability improvement
* [45691](https://github.com/space-wizards/space-station-14/pull/45691) Add a series of outfits for virtual singers
* [45874](https://github.com/space-wizards/space-station-14/pull/45874) Clown Mask Folding, Additional Vulpkanin Mask Sprites
* [46171](https://github.com/space-wizards/space-station-14/pull/46171) Accessible Makeshift Laser Pistol
* [46107](https://github.com/space-wizards/space-station-14/pull/46107) feat: new burger sequence ingredient sprites
* [45657](https://github.com/space-wizards/space-station-14/pull/45657) Reduce Tricordrazine Combat Viability
* [45310](https://github.com/space-wizards/space-station-14/pull/45310) Completely Refactor IconSmooth
* [46328](https://github.com/space-wizards/space-station-14/pull/46328) Adjust Material Silo UI to Be Side-By-Side
* [46353](https://github.com/space-wizards/space-station-14/pull/46353) Correctly size bowl's solution and make it examinable
* [41644](https://github.com/space-wizards/space-station-14/pull/41644) add blinking to species
  * (nominated as a release blocker, see above)
* [43166](https://github.com/space-wizards/space-station-14/pull/43166) Vox can now caw and hiss
  * `Errant`: I actually think that we should stop pushing the vox more and more toward “space bird”. They are *aliens.* In my opinion, whatever resemblance to birds there is, should be treated as a coincidence rather than a target template. (Yes I am aware of the irony/hipocrisy, given that their “iconic screech” is literally just a modulated hawk). We still don’t have any kind of species guidelines, do we?
    * ACTION make an issue to add a effect to the sound
* [43991](https://github.com/space-wizards/space-station-14/pull/43991) Make PDA Cartridge Slot take priority over the ID slot
* [46358](https://github.com/space-wizards/space-station-14/pull/46358) Make medals not sliceable into cloth
* [43980](https://github.com/space-wizards/space-station-14/pull/43980) Clientside Only Typing Preview
* [46345](https://github.com/space-wizards/space-station-14/pull/46345) Arrivals Ambience
* [46351](https://github.com/space-wizards/space-station-14/pull/46351) Buffed Binoculars and added them to the autolathe
* [46366](https://github.com/space-wizards/space-station-14/pull/46366) Adding ftl launch admin debug command
* [45600](https://github.com/space-wizards/space-station-14/pull/45600) Remove vending machines from the random sentience game rule
  * `Errant`: REVERT This does not actually seem to give any reason for why this was removed? Two other PRs in the release add new things to vending machine ghostroles. Unless I’m misunderstanding something about what this does, I say we start a revert vote
    * ACTION (Errant) patch to re-allow vending machines
* [42459](https://github.com/space-wizards/space-station-14/pull/42459) Add Waypointers
  * `Pok`: Localization of Waypointer names is missing (see [46530](https://github.com/space-wizards/space-station-14/pull/46530))
    * Merged to master, not necessary for release
* [46364](https://github.com/space-wizards/space-station-14/pull/46364) Mobs in a Space Dragons stomach no longer Rot
* [45846](https://github.com/space-wizards/space-station-14/pull/45846) Adding Printable Light Packages & Improving EntityProviders
* [46223](https://github.com/space-wizards/space-station-14/pull/46223) Rework Hemorr + Hemotoxin Sting
* [45898](https://github.com/space-wizards/space-station-14/pull/45898) Foamblade Sound Effects
* [44990](https://github.com/space-wizards/space-station-14/pull/44990) Device Network refactor part 2: Prediction & DeviceLinking
* [45167](https://github.com/space-wizards/space-station-14/pull/45167) The Changeling's Horror Form
* [46301](https://github.com/space-wizards/space-station-14/pull/46301) Fake ID's
* [45463](https://github.com/space-wizards/space-station-14/pull/45463) Plant Analyzer and Tray UI
* [46382](https://github.com/space-wizards/space-station-14/pull/46382) Trammers can now have assistive items
* [46260](https://github.com/space-wizards/space-station-14/pull/46260) vendor malfunction' station event (some vending machines will eject some of their contents)
* [46399](https://github.com/space-wizards/space-station-14/pull/46399) Tram Driver Jumpskirt
* [46394](https://github.com/space-wizards/space-station-14/pull/46394) Box and Marathon - readds psychologyst job
* [46395](https://github.com/space-wizards/space-station-14/pull/46395) Dresses in Uniform Printer
* [46384](https://github.com/space-wizards/space-station-14/pull/46384) Syndicate Reinforcement Buffs
  * `Nem`: Keep an eye on these. I want to know if this will need reigning in.
    * ACTION make part of the other admin ping about dynamic?
* [46388](https://github.com/space-wizards/space-station-14/pull/46388) Move Tactical Maid Headband To SyndieDrobe Contraband Inventory
* [46412](https://github.com/space-wizards/space-station-14/pull/46412) Nukie ID Titles
* [46378](https://github.com/space-wizards/space-station-14/pull/46378) Make glass shards of all types recyclable
* [45714](https://github.com/space-wizards/space-station-14/pull/45714) aghost keybinds + minor removal
* [46432](https://github.com/space-wizards/space-station-14/pull/46432) Lizard Feet on Ninja Suit
* [46315](https://github.com/space-wizards/space-station-14/pull/46315) Guidebook: update Jobs page + add Civilian page
* [46421](https://github.com/space-wizards/space-station-14/pull/46421) Wizard, Ninja, and Pirate ID Titles
* [46439](https://github.com/space-wizards/space-station-14/pull/46439) Fixing #46187 by giving RehydratableComponent a set of catalysts instead of only one catalyst (and added Holy Water to the default catalysts)
* [46245](https://github.com/space-wizards/space-station-14/pull/46245) DNA Imprinting
* [46433](https://github.com/space-wizards/space-station-14/pull/46433) Clown Lizard Plush Sound Effects
* [46385](https://github.com/space-wizards/space-station-14/pull/46385) followup to #46260 making it affect a percentage of machines on station instead of a raw quantity
* [45895](https://github.com/space-wizards/space-station-14/pull/45895) Updates to almost all guidebook species pages
* [46448](https://github.com/space-wizards/space-station-14/pull/46448) Create new CloneOrganMarking overload to copy the Hideability from the source organ
* [46354](https://github.com/space-wizards/space-station-14/pull/46354) Candy bowl changes: inventory grid, craftable
* [46436](https://github.com/space-wizards/space-station-14/pull/46436) Various antagonist flavor-text touchups
* [44650](https://github.com/space-wizards/space-station-14/pull/44650) T-ray: show cables/pipes under walls and grilles
* [45926](https://github.com/space-wizards/space-station-14/pull/45926) Improved Vending Machine Ghost UX
  * `Errant`: This seems to have become immediately defunct/irrelevant, given that [45600](https://github.com/space-wizards/space-station-14/pull/45600) removed these ghostroles. See revert vote on that PR
* [45499](https://github.com/space-wizards/space-station-14/pull/45499) Toggle self ghost
* [46443](https://github.com/space-wizards/space-station-14/pull/46443) Remember guidebook search and scroll position when switching entries
* [46486](https://github.com/space-wizards/space-station-14/pull/46486) Energy Katana Belt Sprite Fix
* [46478](https://github.com/space-wizards/space-station-14/pull/46478) Give kobolds a different death emote from monkeys
* [46425](https://github.com/space-wizards/space-station-14/pull/46425) Remove Vent Horde Ghostrole Raffles
* [45824](https://github.com/space-wizards/space-station-14/pull/45824) Port of the "Trasen-Knox" UI theme from /tg/station
* [46513](https://github.com/space-wizards/space-station-14/pull/46513) Makeshift laser pistols are small size
* [46458](https://github.com/space-wizards/space-station-14/pull/46458) Hike Station Prototypes
  * `Nem`: Merged early. Probably fine.
* [45068](https://github.com/space-wizards/space-station-14/pull/45068) Diona markings rework
* [46532](https://github.com/space-wizards/space-station-14/pull/46532) NoSlips in Basic Operative Bundle
  * `Errant`: I think it might be a better replacement to give them something else? The idea with the magboots was to give rookies a way to avoid slips. They now have this automatically, and they don’t need that noslip, it’s merely a nice-to-have. Is there something else that might be better bang for their bucks in the “default kit” ? Maybe they would be better off with more magazines and C4? Or are noslips a huge passive buff over magboots?
* [46515](https://github.com/space-wizards/space-station-14/pull/46515) Add back and forward buttons to the guidebook
* [46239](https://github.com/space-wizards/space-station-14/pull/46239) Refactor biomass reclaimer insertion and processing
* [45238](https://github.com/space-wizards/space-station-14/pull/45238) Centered mob sprites to match hitboxes
* [46544](https://github.com/space-wizards/space-station-14/pull/46544) Proper Syndicate's Winter Coat Name
  * `Errant`: English is not my first language but this sounds kinda awkward? Wouldn’t it be “syndicate winter coat” ? Is that technically grammatically incorrect? I don’t think it is, because we can just use syndicate as the adjective, not as a noun?
* [46159](https://github.com/space-wizards/space-station-14/pull/46159) Give holy water better parity with 'mundane' water
* [46418](https://github.com/space-wizards/space-station-14/pull/46418) Make Agent ID job icon groups look like buttons and show the selected one
* [46540](https://github.com/space-wizards/space-station-14/pull/46540) Disable recycler hand interaction
* [46449](https://github.com/space-wizards/space-station-14/pull/46449) Botany Omni Rework
* [45080](https://github.com/space-wizards/space-station-14/pull/45080) Orders can no longer be approved on different map


# Question Time!

* can i put ress in the spot and make him talk a bit about the new (tentative?) docs site while we are all here
  * Ress is making an amazing new docs site that’s gonna be awesome!
  * Github based markdown flow
* How are you guys doing considering The Situation™?
  * Better than last week! Worse than next week!
* Who can be contacted about the natives and other dependencies to merge <https://github.com/space-wizards/RobustToolbox/pull/7112>
  * ACTION: Bother Simyon to review this
    * Simyon has been bothered.
* question: new maintainers when?
  * We are restructuring and we have halted the onboarding of new team members for a period of a couple weeks.
* Question: How can contribs best help during the aftermath of this whole situation? Just keep doing what we're doing?
  * Keep making PRs and contributing! Priority shifts are likely to happen as we reorganize. 
  * Please review PRs! We love when contribs do that!
* Is the wiki forever doomed to rot in the deepest parts of maints?
  * The wiki itself is something we want to return soon - deployment schematics are nearly ready but due to Events have not been deployed.
  * Once we return to normalcy, this will be a priority.
  * Mapserver will also make a return.
* questions: any future plans for mapping tools?
  * Current tools are bad.
  * This is aligned with the pre-mentioned repriortization as something that can broadly benefit the entire ecosystem.
* Can IconSmooth 2.0 be considered for this stable release?
  * It was merged to master and thus it will be an annoyance later.
  * **ACTION (Nem) Vote to include**
* What is the current stance on the respritening?
  * We’re discussing this internally


Releases since the last non-squashed PR: 1


*Niko is a cat*
