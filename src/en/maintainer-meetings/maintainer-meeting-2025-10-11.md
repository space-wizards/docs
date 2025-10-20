# Maintainer Meeting (11 October 2025)

```admonish info

**Attendees:**
- Fildrance
- Errant
- ArtisticRoomba
- Scar
- Myra
- Ada
- Tiniest shark
- Slarti
- Princess
- Keron
- Julian
- Slam
- Spanky

```

This meeting was recorded:

{% embed youtube id="Y-3AI01hd0c" loading="lazy" %}

## New Roadmap (Slarti)
WIP doc:
https://hedgedoc.spacestation14.com/RCRDvbSmTzmoQuLcgoMAxQ#
Please add anything you think should be in there. We can go through together it in the meeting.

We currently have a problem with our lack of design documentation. Contributors make random PRs and have to guess what features maintainers want in the game. The roadmap should be a list of features, refactors, or other things on the TODO list that are conceptually pre-approved and maintainers are in general agreement about that the game needs them.

Each of these should have an issue listing any requested implementation details the solution should have, so that a contributor can start working on it without having to guess what the maintainers expect of them. Roadmap issues could be either uploaded in the form of a doc like this, or use a github project for easier editability (if we have to make a PR on the docs repo every time we want to change something then we won’t keep this list up to date). If a maintainer is working on an issue it should be assigned to them. If an issue is looking for a contributor to work on it should be marked as such, same for cases where it’s better for a maintainer to handle it and we specifically we don’t want help.

- One idea is to use Projects on github
    - The issue with gh projects is that pjb has to manually mark them public
        - Not really too big of an issue
- As an issue like the freeze section
    - Nah
- JETFISH
    - When you fish it (When it works)
- It would be better to make this a forum post so everyone can discuss it more deeply outside of the meeting.
    - https://forum.spacestation14.com/t/extremely-important-new-updated-roadmap/24311/24

## Freezing playtimers (Myra, suggested by Toast)
We have had 9 playtime related prs in the past 2 weeks according to Toast. It is technically a micro balance which we do have a stance on, but should it also be specifically clarified?

- Note: UPDATING existing ones was my proposal, not adding new ones
- IMO they should all be coming from the maint/admin team instead.
- Decided on maintainers/admin only restriction.
    - Sidenote from discussion: We should maybe add a new pr template for "read the issues" even though its already in the pr guidelines the concern is that its not read by people (Myra: Skill issue on their side its even in the git tutorial)
    - Maybe we should also make a notice to contribs somehow?

## UI and Map freezes progress (Myra)
Last meeting we mentioned freezing maps and UI and I think we said yes to the UI one but I don't see a map freeze added... sooo?

- Maps will be handled by ArtisticRoomba soon after this.
- I will poke UI maints for their freeze.

## Extending Offmed Playtest (Princess on behalf of Janet)
Janet pushed some big changes to offmed on the 9th, and would like a bit more time to test them.
This is an official request to extend offmed testing by a week to the 19th rather than the 12th.
- Slarti: We merged a ton of PRs recently and it would be good to see if there are any bugs without having them show up all at once with the release so that it's easier to figure out when it started happening. So I would prefer if we can either regularly merge master into the Offbrand branch or switch back and forth from time to time so we keep that testing server feedback for the master branch. But if it's only planned for one more week and not extended further it's probably fine.
- Janet: i'm kinda burned out on the amount of time i'm spending observing and engaging in rounds combined with the maintenance burden of doing the nightly merges as well as any revisions to offmed that are needed from the tests, i'd prefer to have a 1 week period after 2 weeks of non-offmed
    - Sure, by next stable release for 1 week as requested.
    - By that time we may have the feedback thingy.

## Maintainer Partial Review Guidelines (Princess)
Doc for updating the Review guidelines section to include partial reviews and suggestions for partial reviews.
Needs review before I put it up to a proper vote. [Partial Review Guidelines](https://github.com/space-wizards/docs/pull/503)

- What do other maintainer want from it?
    - Slarti: It could be rephrased
    - Should partial reviews be marked as not a full approval
        - It's basically just getting someone else to do requested changes for a part you dont understand. You can just dismiss the review if its done.

## Desoxyephedrine (Princess)
I realized my opinions of desoxy are bigger than just a comment on the glassthle PR. 
Glassthle PR is a step in the right direction, but desoxy just needs to be nerfed heavily before it's balanced.
- 35% additional movement speed is insane and way too high.
- It has effectively no downsides to continuous use.
- Trivially easy to get in large quantities
In addition I'd like to state that Desoxy being major contraband is kind of an issue. I'm not a big fan of things which distract sec from doing their job, this change is one of them and doesn't affect actual antags who abuse deso. 
In addition it often just results in:
- Captain making meth legal roundstart so they can abuse deso
- Captain making meth legal for sec roundstart so only sec can abuse deso
- CMO not working with security in fear of their deso being confiscated
Reagent contraband is good, especially for stuff like napalm but deso being major contraband is creating more problems while solving none.

`Slam`: I, too, have had desoxy in my sights as of late. I do think the primary culprit is the hypopen and I would *greatly prefer* if those nerfs are pushed through first, but deso is still probably just a tad overtuned regardless.
However I would like to see any changes to it as part of a larger rebalance effort that takes ephedrine and (more importantly) hyperzine in mind. Hyperzine is right now "budget deso" which is kind of stupid considering it's meant to be the antag version. [39458](https://github.com/space-wizards/space-station-14/pull/39458) is doing some attempts at changing deso/ephe but I am not sure if it's the right way to ago about things.

Discussion post: https://forum.spacestation14.com/t/ambrosia-ephedrine-family-nerfs/24297

## New Quick Discussions (Simyon)
How is that going, any wishes?

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- Princess
- aada
- Tiniest Shark
- Simyon
- ScarKy0
- Errant
- Beck
:::

- [40532](https://github.com/space-wizards/space-station-14/pull/40532) Random Instrument Collection
    - `Simon`: I am sus of the fact that the super synth is included in this. The DAW already is the "general" instrument and is hard to get as a goal. I think the super synth shouldn't be an item you can gamble for.
    - `Slarti`: Yeah, I agree. Having a normal and admin variant of the super synth just makes it less special. It's just a better DAW now since it's an item instead of a structure. Also the DAW is intended to have a complicated crafting recipe so you have to go on a quest to find the required instruments for building it. So I think you should not just be able to buy it. And in general items that are just straight up upgrades to other items should be avoided from a game design perspective.
    - BUG (unrealted): You can get a DAW without the crates by using flatpacks (20 steel)
        - Perhaps make the DAW easier to aquire.
    - VOTE: Revert/Keep
- [25875](https://github.com/space-wizards/space-station-14/pull/25875) Add explosive cord.
  - `Slam`: Gonna wanna keep an eye on this one to make sure it doesn't cause too much chaos. 
- [40246](https://github.com/space-wizards/space-station-14/pull/40246) Admin smite: Homing rods.
- [40160](https://github.com/space-wizards/space-station-14/pull/40160) Added white towels to autolathe and uniform printer
- [35671](https://github.com/space-wizards/space-station-14/pull/35671) Make Closets Less Tanky Than Gun Safes
- [40303](https://github.com/space-wizards/space-station-14/pull/40303) Vulp Plushie
- [39914](https://github.com/space-wizards/space-station-14/pull/39914) More Vox Sounds
- [39979](https://github.com/space-wizards/space-station-14/pull/39979) New GitHub issue templates
    - `Simon`: Did we notice anything in regards to issue quality after this was merged?
    - `Beck`: I think so! It makes issues a lot easier to format imo
- [40572](https://github.com/space-wizards/space-station-14/pull/40572) Salv Instrument Spawn Rework
    - `Simon`: Same thing as 40532. Concerns about the super synth.
    - Agreed, should not be in there.
    - VOTE: Revert/Keep (Use same vote as #40532 for if Supersynth should be player accesible.)
- [39087](https://github.com/space-wizards/space-station-14/pull/39087) Readds Tasers to Security
  - `Slam`: I am willing to move these out of Vulture testing but I am still not fully sold on them + offmed kinda overshadowed how they work in heavy combat. Putting them in the hands of the wider playerbase and monitoring feedback seems like it might be a good move.
  - `Beck`: This should stay in vulture, I personally didn't see any real feedback from it.
  - `Myra`: It shall only be on vulture for another release!
- [40567](https://github.com/space-wizards/space-station-14/pull/40567) Added Vox Mime Hardsuit Sprite
- [40588](https://github.com/space-wizards/space-station-14/pull/40588) Removes Taser Bolt Damage & Allows Tasers to be used by Pacifists
- [40597](https://github.com/space-wizards/space-station-14/pull/40597) Replace outdated tip 79 about artifact scanners
- [40618](https://github.com/space-wizards/space-station-14/pull/40618) Hit 'em with the Michaelwave
- [40631](https://github.com/space-wizards/space-station-14/pull/40631) Rephrases two Whistle descriptions
- [40638](https://github.com/space-wizards/space-station-14/pull/40638) moved desoxyephedrine from ambrosia to glasstle
- [40640](https://github.com/space-wizards/space-station-14/pull/40640) Stage Name For Musicians
  - `Slam`: We really gotta fix the bug where the crime console uses the character's original name... Makes it hard to know who to mark and also messes with the Wanted HUD.
  - `Ress`: Also needs fixing on the admin side, as it will list their character name in the player overview menus, instead of their stage names. So if we're going to change this, it's probably for the best that their own character name temporarily gets changed to their stage name for that round?
- [36696](https://github.com/space-wizards/space-station-14/pull/36696) Prisoner Eva Suit is now an Emergency Eva Suit
- [38044](https://github.com/space-wizards/space-station-14/pull/38044) Increase puddle spillover volume to 50u
- [39868](https://github.com/space-wizards/space-station-14/pull/39868) Organized Head Locker Fills Feat. Circuit Totes.
- [40646](https://github.com/space-wizards/space-station-14/pull/40646) Disable panic bunker for Leviathan
- [39567](https://github.com/space-wizards/space-station-14/pull/39567) Add utility knife/box cutter
  - `Slam`: I will be using this, but not for utility. >:)
  - `Tiniest Shark`: Considering this thing only does 4 damage i am terrified how you'll use it.
- [36597](https://github.com/space-wizards/space-station-14/pull/36597) Material Door rebalancing
  - `Errant` Isn't making them faster to deconstruct (ie, breach) contrary to the stated goal of making them a more viable option?
  - - `aada` They can't be locked in the first place, so breaching isn't really an issue.
- [40674](https://github.com/space-wizards/space-station-14/pull/40674) You can now stuff the nuke disk in plushies
    - `Princess`: We need to merge some anti storage cheese, specifically in regards to cigarette boxes being able to store items they really shouldn't, and food items being able to store items larger than them. We may want to add an item size smaller than 1x1 (a 1x1 with a weight of 0 rather than 1) for things like pills and bullets that way we don't have to suffer with more whitelists.
    - `Slarti`: I merged this, but with the current exploits where you can stack items infinitely inside them this should probably be fixed or reverted for the release.
- [38230](https://github.com/space-wizards/space-station-14/pull/38230) nerf cheese prices, part 1: bedsheets
- [38246](https://github.com/space-wizards/space-station-14/pull/38246) nerf cheese prices, part 2: electronics
    - `Tiniest Shark`: It'd be nice to get a system that dynamically scales prices on sold items so PRs like this arn't necessary in the future.
    - `Errant`: Wasn't there an integration test that checks items for this sort of stuff? Does it need to be expanded in what type of items it checks?
    - `Slarti`: I already made an [issue](https://github.com/space-wizards/space-station-14/issues/40678) for that, manually fixing the prices is a Whac-A-Mole game, but we had to do something with the PRs
- [37975](https://github.com/space-wizards/space-station-14/pull/37975) Adds smart equip to pocket 1, pocket 2, and suit storage slots
    - `Errant`: I can see how it makes sense to have hotkeys for these slots, but I am concerned about the ongoing key bloat
- [40694](https://github.com/space-wizards/space-station-14/pull/40694) Ian Suit gives accent!
- [39204](https://github.com/space-wizards/space-station-14/pull/39204) Incendiary rounds do pierce
- [40227](https://github.com/space-wizards/space-station-14/pull/40227) Add Arrivals sign
  - `Slarti`: Needs a mega-issue for mapping it to every map
- [40009](https://github.com/space-wizards/space-station-14/pull/40009) Skeletons are now playable instruments
- [39181](https://github.com/space-wizards/space-station-14/pull/39181) Create more Holy Books based off Spacestation 14 Dieties
- [39698](https://github.com/space-wizards/space-station-14/pull/39698) Remove the Tanakh and Satanic Bible from the game.
- [40700](https://github.com/space-wizards/space-station-14/pull/40700) Let gorillas pull things
- [40584](https://github.com/space-wizards/space-station-14/pull/40584) Change Discord round restart text
- [40601](https://github.com/space-wizards/space-station-14/pull/40601) Give mimes their french bread back
    - `Princess` Do any other survival boxes give moths cotton nutribricks? Or is this the only one that does? 
    - `Slam`: Moths eat the wrapper. The wrapper is not very moth-food-coded though. [39838](https://github.com/space-wizards/space-station-14/pull/39838) is meant to give moths their own nutribrick but I'd honestly rather make the wrapper more obviously moff food because sharing is caring and fits with the emergency meal being made as practical as possible.
        - `Princess`: We could just make it so it doesn't make a plastic sound when unwrapped. Also change the sprite to not look like plastic.
        - `Slam`: Yeah something like that. I can't give a thumbs up reaction here so uh... 👍 That works.
        - `Slarti`: I always liked sharing my nutri bricks with my moth friends
    - `Tiniest Shark`: Ideally we can do a pass on Moth food at some point so there's some form of standardization. Or at least something a bit more interesting than just "X but it's got cotton in it". The bricks being advertised as a twofer is a headcanon ive always liked though.
      - `Slarti`: Yeah, the current trend of "the same recipe but with cotton" is kinda boring, misses the point of the food restriction and just doubles the recipe count. Moths should have unique food recipes. But new microwave recipes are frozen and we will need to clean up the old ones at some point anyways.
- [40115](https://github.com/space-wizards/space-station-14/pull/40115) Vox burn into fried chicken
  - `Slam`: Seems a bit sus making Vox have their whole own Destructible component definition just for this. But it IS funny.
  - `Princess`: New gibbing and ashing behavior is bad but I will let this pass for the funny factor.
- [40615](https://github.com/space-wizards/space-station-14/pull/40615) Head of Security's Energy Magnum (and Warden's Energy Shotgun)
  - `CptJeanLuc`: The projectile this fires is missing the projectile fixtures. Author said they want this so it goes through windows, but imo thats probably not a good reason. It will lead to some strange collision behavior that won't be uniform with other projectiles and is hard to special case for due to how our fixtures are setup. Also it breaks the consistency of projectiles hitting things and lasers passing through transparent things with no real reason for that to be the case imo.
      - Projectiles should have different colors per its mode
      - This may be a massive design discussion if this is not normal.
- [40102](https://github.com/space-wizards/space-station-14/pull/40102) Cancer Mice Ghostrole Info
- [39888](https://github.com/space-wizards/space-station-14/pull/39888) Biosuit Suit Slots
  - `Slam`: Yaaaas Vox stay winningggg
- [40761](https://github.com/space-wizards/space-station-14/pull/40761) MRE wrappers / cotton nutri-bâtards are no longer twice as nutritious as nutribricks
- [40569](https://github.com/space-wizards/space-station-14/pull/40569) Added Vox Beak Types, New Markings, and Sprite Layering Fixes
- [40762](https://github.com/space-wizards/space-station-14/pull/40762) Added the golden shaker (playtime reward for Bartenders)
    - `Princess`: Can salvage get a golden landmine :^)
- [40757](https://github.com/space-wizards/space-station-14/pull/40757) Change Energy Shotgun to fit as a Warden weapon
- [37445](https://github.com/space-wizards/space-station-14/pull/37445) Slightly re-nerf zombification speed
- [39334](https://github.com/space-wizards/space-station-14/pull/39334) Add disclaimer about AI generated content to Readme.md
- [37920](https://github.com/space-wizards/space-station-14/pull/37920) Fix: Allow energy shotgun lethal projectiles to hit holos
- [39920](https://github.com/space-wizards/space-station-14/pull/39920) Added folders and clipboards to trinkets tab
- [40782](https://github.com/space-wizards/space-station-14/pull/40782) Allow more energy projectiles to hit holo creatures
    - `Princess`: Does this allow holoparasites or their hosts to be stunned or take stamina damage?
      - `Slam`: Needs to be doublechecked but if they are, the solution would be to not make holos stunnable.
          - Only with the admeme taser
- [40783](https://github.com/space-wizards/space-station-14/pull/40783) Wrapped Parcels can be labelled with Papers
- [40647](https://github.com/space-wizards/space-station-14/pull/40647) Update Mind Shielding section in Space Law
- [40797](https://github.com/space-wizards/space-station-14/pull/40797) Add slowdown to nocturine, buff duration and minor delay reduction
  - `Slam`: I'm gonna have to endure a whole other two weeks of "Should have nerfed the hypopen"... :(
      - `Princess`: Well if we didn't get merged in time that means I can request a more evil review to refactor the system >:)
          - `Slam`: ;_;
  - `Beck`: I personally say revert and merge the hypo pen nerf stuff.
  - VOTE: Revert/Keep (Change the changelog to clerify it though)/Try with hypopen nerf (Keep it in testing)
      - Sidenote: We should be merging stuff that is meant to be merged together... well together. Or mention it in the changelogs
- [40790](https://github.com/space-wizards/space-station-14/pull/40790) Move Bulldog Drum to Emag

## Ambush

 -  `Errant`: I have targeted https://github.com/space-wizards/space-station-14/pull/38705 on staging, can we please get it into this release cycle, it fixes a P0 issue. The PR already has 2 approves, but as a hotfix it needs 3
     -  Merged

## Decoy Section

- Nik is a cat
