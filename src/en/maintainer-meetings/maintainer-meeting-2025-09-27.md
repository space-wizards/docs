# Maintainer Meeting (27 September 2025)

```admonish info

**Attendees:**
- Scar
- Myra
- Simyon
- Tiniest Shark
- Errant
- Fildrance
- notafet
- Janet
- Julian
- aada
- ArtisticRoomba 
- Slam

```

This meeting was recorded:

{% embed youtube id="7tS89lzASdM" loading="lazy" %}

## REALLY BIG FAT NOTE
I am begging all of you to stay on topic instead of messing around codermin-abusing Vulture. It's annoying to try and have discussion when half of the maintainer body (including LMs) is giggling and not paying attention to important discussion.

## Welcome new maintainer ada!!🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
Wooo

## Roundstart, Locker, and Vendor Equipment (ArtisticRoomba)
We have had pull request after pull request attempting to change what people get on roundstart, as well as in lockers and vendors.

We need to establish definitions as to what should be in what. It is really grating having to deal with these PRs, especially on the upstream repository.

Generally, we should define the following:
- What do people get on their person, roundstart?
    - Is it the basic tools or equipment to do their job?
        - Engineering currently gets their tools, but science has to collect theirs from their locker.
- What do people get in their locker?
    - Is it more rare or restricted equipment?
        - Warden and the Head of Security spawn with insulated gloves. Should they, or should this type of equipment move into their locker?
        - Security has had so much stuff moved in and out of loadout that there are a *lot* of duplicate items between the two.
- What do people get from vendors?
    - Is it shared equipment, or equipment that is limited?
        - Engineering gets insulated gloves both in their locker as well as their restricted vendor.

Decisions:
- Vendors should contain mostly expendables
    - Some spare tools and such
- We should move job-essencial equipment into lockers
    - Ensure we have enough lockers for latejoins/job joins
- Mapped department equipment should be through a spawner so it can be editable through YAML

## Engineering & Atmospherics Workgroup (ArtisticRoomba)
A notice to the Engi and Atmos workgroup that the Engineering design document is ready for preliminary review. I would like to get it approved by the workgroup before I start a maintainer vote.

You can review the design document [here](https://github.com/space-wizards/docs/pull/519/files).

## Medical Workgroup Design Doc (Princess Cheeseballs)
A notice that the Medical Design docs are also ready for preliminary review. I'd like for them to get a look over by Janet and anyone else interested in reading them as well.

You can review the medical design docs [here](https://github.com/space-wizards/docs/pull/510)

## New Maps Blocker (ArtisticRoomba)
I am considering blocking all new maps until mapping guidelines are completed. Otherwise they will literally never get done and we have to keep making exceptions.

You can find an in-progress draft of the mapping guidelines [here](https://hedgedoc.spacestation14.com/seEoI7phQ0uAb2WnrKdMrQ). This is where we should work on them for now on so people can work on them asynchronously.

Only mapping leads and maintainers who have done mapping should work on the guidelines. I am not interested in opening this up to other contributors at this stage.

## Migrate from legacy branch protections to Rulesets (Ress)
Currently the branch protection rules are on the legacy system that GitHub won't update anymore. I propose that these are migrated over to the new system called "Rulesets". The reasoning for why is to take advantage of the new power-user features such as merge queues, selective merging options on a specific branch, required approval numbers, etc. All while allowing the option for these selective rules to be bypassed by org members.

I envision 3 new rulesets to be created. 2 of these are moved from legacy branch protections to rulesets. And the final one is a new one to only allow squash merging on master, while allowing it to be overwritable for the cases that its needed. (See funny note at the end of the doc)

1. Branch protection master (Ported from legacy branch protection)
    - Targeting branch "master"
    - Enabled "Require a pull request before merging"
    - - Optionally set required approvals
    - Optionally enable "Require status checks to pass"
    - - Along with "Require branches to be up to date before merging"
    - Enabled "Block force pushes"
    - Rule bypass allowed for:
    - - PJBot
2. Branch protection stable (Ported from legacy branch protection)
    - Targeting branch "stable"
    - Can be removed or left in place as a legacy rule.
3. Only Squashing master
    - Targeting branch "master"
    - Enable "Require a pull request before merging"
    - - Set the options to Squash only
    - Rule bypass allowed for:
    - - role: write
    - - role: maintain
    - - role: admin
    - - PJBot
    - This will ensure that any repository maintainer will be prompted to squash merge, but also ensure that they can overwrite it in cases that they need it!
![](https://hedgedoc.spacestation14.com/uploads/6be8603b-f6ab-4174-8990-7781789ce516.png)

##  Merge Queue Proposal (ArtisticRoomba)
One of the issues with current test runs on GitHub is that tests will only run at the head of the branch that is to be merged into the main branch.

This means that tests will not run for the product of the merged PR. This can prove especially annoying when dealing with pull requests that are very behind `master`, think 200-3000 commits. Some PRs will test fine but when merged they will break master and I now have to pull time away to fix something I caused, instead of going to bed.

Another note is that sometimes I push a quick fix but I have to wait ~9-10 minutes for tests to complete before merging.

I was wondering if we could enable GitHub's merge queue, where pull requests are automatically merged into a testing branch (the product of the PR) and tests run on that. If they pass, the PR is merged into master, and if they fail, the PR is removed from the merge queue and the PR stays open.

I actually tried this out on the fork that me and Southbridge maintain, Moffstation. It worked out pretty well but sometimes it was annoying for tests that we *know* would fail (submodule changes) as the merge queue would not merge the PR unless you bypassed the queue and did a direct merge. You would need admin rights to bypass these restrictions, so we didn't keep it around for long.

However, Ress demonstrated that with new branch rules that we can just assign certain roles to bypass it, so any maintainer can decide to not go through the merge queue when they need something merged that doesn't pass tests.

Myra: Done out of meeting, we got merge queues now and the branch protection thingies above.


## New GitHub Issue templates (Ress)
- [39979](https://github.com/space-wizards/space-station-14/pull/39979) New GitHub Issue templates

This probably has to be looked at by project leadership, or at the very least someone higher then maintainer.

Having less friction on making issues helps the entire project, having these issue templates makes filling out issues so much easier to understand for someone who doesn't have a development background. 10-20 minutes of back and forth with me on this PR and a merge will have a long lasting effect on how issues are created. A live interactable demo of how these templates work is in the PR.

Merged :3

## UI code freeze? (Janet)
- [#29903](https://github.com/space-wizards/space-station-14/pull/29903) has been a long time coming and I'd like to commit to getting it in this next stable cycle or the one after.

  Any new UI code needs to avoid referencing `StyleNano` or style classes that are getting removed/renamed, and any additional UI code coming into master will need to be incorporated into the PR if it has any styling elements relying on `StyleNano` before we get it in.
  
  Therefore, I propose we freeze UI code (excepting non-styling-relevant changes) until the PR is in.
  
## Offmed Vulture Testing (Janet)

- Maintainers are expressing a lot of interest in me using Vulture as a test bed server for Offmed instead of a downstream


  How? xd
  
  - Scarky: Use a side branch like on April Fools
  - Fildrance: How much time do you need?
    - Janet: 2 weeks or so
  - Myra: You'll need to merge master manually
      - Fildrance: This will block testing other stuff as well

Conclusion:
- We are using vulture on a seperate branch on wizden (and also can be the pr branch), jenet will keep master up to date into the seperate branch.
- Also make sure to do the experimental procedures (namely set the MOTD (put a big ansii cat to gather attention), make an annoucment (no ping) on discord and forums. Maybe the watermark vulture uses if we can do that by then.)


## Required for stable
- [ROBUST-6229](https://github.com/space-wizards/RobustToolbox/issues/6229) Latest engine breaks all MacOS devices
    - Currently a bug on vulture, due to robust looking for an openAL from the launcher (arm64 update is not fully out yet and the launcher stuff is not done), and not falling back to the operating system one. PJB will fix this one probably. OBV this will need an engine update.
        - Launcher update incoming to fix this
            - Fixed: https://spacestation14.com/updates/25-09-26-launcher-update-v0-34-0/


## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- Slarti
- Roomba
- ScarKy0
- Princess
- Tiniest Shark
- Beck
- aada
- Simyon
- Janet
:::
- [40103](https://github.com/space-wizards/space-station-14/pull/40103) Cockroach Gib when Stepped on
- [40310](https://github.com/space-wizards/space-station-14/pull/40310) +1 Spam mail
- [40339](https://github.com/space-wizards/space-station-14/pull/40339) Massively reduce how lethal Man-O-War shuttle is
- [39887](https://github.com/space-wizards/space-station-14/pull/39887) Add jetpacks to the Nukie Infiltrator
- [37867](https://github.com/space-wizards/space-station-14/pull/37867) Dark/Light Grass & Desert Astrotiles
- [37712](https://github.com/space-wizards/space-station-14/pull/37712) Devices with access restrictions list those restrictions in their examination description
- [39588](https://github.com/space-wizards/space-station-14/pull/39588) The station AI can be destroyed
- [40379](https://github.com/space-wizards/space-station-14/pull/40379) Clerify salamander description
- [39707](https://github.com/space-wizards/space-station-14/pull/39707) Detunes Ninja Stun To Actually Have Some Counterplay
- [40401](https://github.com/space-wizards/space-station-14/pull/40401) Add intellicards to AI crates
- [40402](https://github.com/space-wizards/space-station-14/pull/40402) Intellicards rename to AI stored on them
- [40374](https://github.com/space-wizards/space-station-14/pull/40374) Remove drone lawset from ion storms
- [35966](https://github.com/space-wizards/space-station-14/pull/35966) Antag Rolebans
    - `Ress`: While the game admin team hasn't handed out any official lasting Antag rolebans yet, we did play around with them on willing players to test them out in Vulture. No issues were found with them. So I think their ready for release!
    - `Beck` Did the issue of a job and antag having the same name get fixed? I think it will do bad things if they have the same name
         - `Errant` It won't "break" anything, but it will not ban the antag role, it will automatically pick the job. This behavior was not specified in the Breaking Changes notice. But I think its fine, so long as we either add an additional check for this within a reasonable timeframe, or do the antag/jobrole reparenting that was brought up during review.
         - `Beck` agreed!
- [40234](https://github.com/space-wizards/space-station-14/pull/40234) Turn the Satanic Bible's pentagram around, fix left inhand
- [37304](https://github.com/space-wizards/space-station-14/pull/37304) Adds Nukie IDs and PDAs, makes Nukie IDs able to copy accesses.
  - `Slarti`: This is a pretty significant buff to nukies, giving them basically 3 TC more, and they only need the chameleon in the rare case of stealth ops. Not sure if that is a good idea with the current win rate.
  - `Roomba`: This was approved before the high winrate and only took until now to get through due to the backlog. Might want to revert considering circumstances have changed.
  - `Princess`: I disagree with reverting, not buying an agent ID is a nukie noobtrap and if the win rate is still high I'd rather they be nerfed in other ways that don't make the experience harder for new players. Plus this makes it so Nukies aren't crew by default allowing AIs to actually use their very good lethal turrets. 
  - `Slam` Considering we did a fairly major overhaul of the shuttle and planet equipment, this is not an unusual change.
- [40183](https://github.com/space-wizards/space-station-14/pull/40183) Bring vulpkanin in-line with other species on hugging
    - `Scar:`REVERT: The PR has been merged despite the maintainer vote being in the favor of "Other" (At the time of merging) and further votes have only been added after I mentioned it in staff general. Ever since vulps released there has been not a single issue regarding petting on the admin side (I've been keeping an eye on the vulp-related PRs). The consensus at the time of merging was essentially either change the text to be more "normal" or to observe the PR to see if it really is an issue. My proposition is to revert the PR and get back to this next maintainer meeting, upon seeing what players think.
    - `Errant`For the record, this was merged by a wizard citing "executive decision". Our regular processes do not (and perhaps *can't   nev*) cover such a situation.
    - `Beck` I think the best solution would be to allow players to choose but it seems like a lot of work
    - `Slam` The merge was done during a review VC where people who hadn't voted on the thread voiced in favor of merging, and part of the reason for closing was that there was no overwhelming consensus on either side. Even the Other category was split between approve and disapprove. And if I am going to be frank; this is such a fluff feature that we were spending a disproportionate amount of time on.
    - `Slam` PJB's comment on the PR for why it was closed was badly phrased and caused undue distress.
- [40236](https://github.com/space-wizards/space-station-14/pull/40236) Add chemical analysis goggles to ChemDrobe
- [40461](https://github.com/space-wizards/space-station-14/pull/40461) Added diagnostic huds to the engi-vend
  - `Slarti`: Can we write down a design doc with clear rules for what should be a loadout, what in a locker and what in a vendomat? We are getting dozens of these microbalance PRs and it's currently all over the place. For sanity reasons I would suggest just freezing them completely until someone writes one and then handle all items in a single cleanup PR.
- [40201](https://github.com/space-wizards/space-station-14/pull/40201) Crashed the snakeskin boots stock-market by removing their hidden no-slip properties
- [40375](https://github.com/space-wizards/space-station-14/pull/40375) Rename medifab implanter to implant extractor and made it's description clearer
- [40317](https://github.com/space-wizards/space-station-14/pull/40317) Silence mime bags
- [39466](https://github.com/space-wizards/space-station-14/pull/39466) Make ichor heal brute, burn, and toxin evenly
- [40426](https://github.com/space-wizards/space-station-14/pull/40426) Add contraband levels for several reagents
- [40311](https://github.com/space-wizards/space-station-14/pull/40311) Added Cutting Slicing and Executing options to the cane blade
- [40433](https://github.com/space-wizards/space-station-14/pull/40433) Made all tarantulas able to drag entities
    - `Roomba`: We are slowly starting to add dragging to literally every mob and it's starting to get annoying
    - `Beck` seems ok to me, its more fun to drag stuff and I don't see why it shouldn't be allowed
    - `Slam` Canister/locker dragging is sometimes used in combat and kinda annoying; but as stated in the PR it is not a problem inherent to mobs. 
- [40372](https://github.com/space-wizards/space-station-14/pull/40372) The Experimental Lecter 8
  - `Slarti`: We should enforce the PR restrictions more. We keep merging them even if contributors are breaking the restrictions, and contributors will keep making more PRs that are restricted as a result.
  - `Roomba`: If we really want to enforce the PR restrictions then we should just revert this.
  - `Slarti`: No need to revert since it's already merged now in my opinion, but if future PRs violate the restrictions then we really have to close them. If we ever want to get rid of the backlog then we have to learn to say no to contributions. And if we don't intend to enforce the restrictions then they should be removed.
  - `Princess` I think the gun restriction is good since it lets us filter to only guns that are interesting in some way. I personally think this gun is interesting as an ERT weapon so it's fine.
  - `Slam` "Guns - Seek maintainer approval beforehand." Is it a good restriction if we have to follow it strictly even for content that, as evaluated in this case, is fine to have? What is the difference between seeking approval on Discord vs. on Github? 
- [40430](https://github.com/space-wizards/space-station-14/pull/40430) Renames the radar console computer board to "mass scanner computer board"
- [40427](https://github.com/space-wizards/space-station-14/pull/40427) Inhand Sprites for Clear Glass
- [40334](https://github.com/space-wizards/space-station-14/pull/40334) Show hand labeler label text on examine
- [40486](https://github.com/space-wizards/space-station-14/pull/40486) Changed corpsman description
- [40460](https://github.com/space-wizards/space-station-14/pull/40460) Fool players with status command
- [40487](https://github.com/space-wizards/space-station-14/pull/40487) Health increase for station AI cores
- [40360](https://github.com/space-wizards/space-station-14/pull/40360) Vulpkanin Admin Smite
- [40101](https://github.com/space-wizards/space-station-14/pull/40101) Target Dummies Now Show Damage Numbers from Projectiles to User
- [40524](https://github.com/space-wizards/space-station-14/pull/40524) Agent ID verbs now don't require you to pick it up
- [37982](https://github.com/space-wizards/space-station-14/pull/37982) Move circuit tiles and faux tiles to the cutter machine
- [38138](https://github.com/space-wizards/space-station-14/pull/38138) Recharger tweaks.
- [36496](https://github.com/space-wizards/space-station-14/pull/36496) Descriptions for .20 Rifle
- [38005](https://github.com/space-wizards/space-station-14/pull/38005) Xenoborg jammer now ignores xenoborg associated frequencies
- [35294](https://github.com/space-wizards/space-station-14/pull/35294) Add "Lizard Visage" Snout Markings to lizards
- [39856](https://github.com/space-wizards/space-station-14/pull/39856) Xenoborg items are now highly illegal


:::info
Weeks without non-squashed merges: 0 :cry: 
Install Myra's reminder script!
:::
