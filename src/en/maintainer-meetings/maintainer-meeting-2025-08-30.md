# Maintainer Meeting (30 August 2025)

```admonish info

**Attendees:**
- Errant
- ArtisticRoomba
- Scarky0
- Miss Nanotrasen
- janet
- Slarti
- Slam
- Nik
- Julian
- Princess Cheeseballs
- Southbridge
- Tiniest Shark

```

This meeting was recorded:

{% embed youtube id="5V0GDijDQXA" loading="lazy" %}

## Stable review

```admonish info

Write your name here if you read this list fully.
**I checked this PR list:**
- Slarti
- Princess
- Southbridge
- ScarKy0
- Tiniest Shark
- Actionman

```

- [37783](https://github.com/space-wizards/space-station-14/pull/37783) Multiantag Gamemode
- [39902](https://github.com/space-wizards/space-station-14/pull/39902) Remove the dynamic game mode from player votes
- [35350](https://github.com/space-wizards/space-station-14/pull/35350) Added button and manager for in game bug reports (Part 1)
    - Princess: This got reverted
- [39872](https://github.com/space-wizards/space-station-14/pull/39872) Revert "Added button and manager for in game bug reports (Part 1)"
- [39680](https://github.com/space-wizards/space-station-14/pull/39680) Added baby and cube hair (awesome)
- [39303](https://github.com/space-wizards/space-station-14/pull/39303) Expand soap making, but better
- [39674](https://github.com/space-wizards/space-station-14/pull/39674) Increase the bananium horn use delay
- [39520](https://github.com/space-wizards/space-station-14/pull/39520) Removes duplicate CE and paramedic jumpsuits
- [37164](https://github.com/space-wizards/space-station-14/pull/37164) Allows disabler, practice disabler, disabler SMG, and practice laser rifle to be used by pacifists
- [37953](https://github.com/space-wizards/space-station-14/pull/37953) Allow hamster cages to sit on tables
- [39705](https://github.com/space-wizards/space-station-14/pull/39705) Atmos Firesuit Vox sprites
- [39088](https://github.com/space-wizards/space-station-14/pull/39088) Add new nukeops spawners!
    - Princess: I'm a bit concerned about the chameleon projector being in this list for a few reasons. Firstly, it's broken and causes friction issues still and is a very common thing admins have to fix in game, we should get that fixed ASAP. Second, it's a really annoyingly strong stall item if used properly, it has no battery life and I've seen syndies use it to hide for up to an hour doing basically unreactable ambushes to kill unsuspecting players. I don't think it's enough to be a blocker but we should try and get these issues fixed before next stable.
- [39090](https://github.com/space-wizards/space-station-14/pull/39090) Rebalance nukie planet
  - CptJeanLuc: I havent tested it, but I'm pretty sure the nukeops planet still needs to be saved unpaused or it breaks
  - Slarti: We should check this since might mean the spawners will spawn the same items every round if map init has been run
  - Southbridge: Most things are fine saved paused.
- [39091](https://github.com/space-wizards/space-station-14/pull/39091) Rebalance infiltrator (Nukie ship)
  - Slarti: Comment for all three PRs above: I like the random spawners instead of having fixed free items, this should give nukies some more variation in their equipment. We should keep an eye on the balance though, nukies really don't need any buffs at the moment since their win rate is really high at the moment. But it looks like Orks had that in mind when making these changes, so we will see if it works.
- [39710](https://github.com/space-wizards/space-station-14/pull/39710) Jumpability collisions
- [39727](https://github.com/space-wizards/space-station-14/pull/39727) Remove StaminaResistance from cardboard armor
- [38176](https://github.com/space-wizards/space-station-14/pull/38176) Added "highly illegal" contraband to guidebook
- [36521](https://github.com/space-wizards/space-station-14/pull/36521) Minor fix to give Lone Operatives the correct roletype
    - Princess: I agree with Minemoder that Lone Ops are team antags despite the name. I think we should revert this one. 
    - Tiniest Shark: Agreed, if it's Nukies they're fully allowed to cooperate and work with the team arn't they?
    - Errant: This is a bugfix, not a feature change. Before this PR, they were listed as Solo Antagonist in the ghostrole menu, but got the Team Antag mindrole. I don't have a strong stance on their role either way, but Nik said to make them solo antag. In any case, **this current contradiction has to be resolved** one way or the other. If this is reverted, change the ghostrole text to say Team Antagonist.
    - CptJeanLuc: But when would the lone op betraying the other nukies ever be a desirable outcome? To the other nukies it will just appear as if one of their teammates started griefing due to the syndicate hud.
    As for the cooperation, Solo antagonists are not "prevented" from cooperating with Team Antagonists. Nothing is stopping the Lone Op from working with the nukies. It just means a Solo Antag in such an alliance can theoretically betray a Team. Given that in this case they have the exact same goal and they all win if the station blows up, I don't see how this could cause any issues
        - Errant: I will admit that I used the word "betray" carelessly, as I was talking about solo-team interactions *in general*. I do not expect it to ever get to betrayal in the context of lone ops. What I think might actually happen, and only very rarely, is the loneop deciding to put their safety above the rest of the nukies, while they still all work to carry out the mission. That could result in some interesting interactions without being disruptive. Of course, this all requires that lone ops and team nukies even meet in the first place, which sounds like a fairly rare event to begin with, and I would expect the most lone ops to act as a mildly aloof member of the team automatically, even if their role says Solo Antag (which is permissible, as far as I understand)
    - Princess: I think given they have the same goal they should be team antagonists, especially considering they can spawn more team antagonists (reinforcements) who are explicitly team antagonists.
    - Errant: We have no official policy on this, but all the original mind role types were confirmed via head admin, presumably reflecting admin consensus. Since they are the ones who both monitor and judge role behavior, their viewpoint is at the very list highly valuable, and arguably should take precedent. It should only be overwritten by maintainer vote if we have some more concrete concern than that of individual admins. ((It's funny that I now argue for the status quo, I think I opposed Nik on them being Solo Antags in the first place))
    - Slam: To me the answer to this question can be derived by the answer to another question: Would a LoneOp get bwoinked for gunning down another Nukie? Sure it's probably a stupid thing to do that, but I am not concerned about strategy, I am concerned about *rules*, which is what the mind roles ultimately represent. As far as I can recall I have yet to receive a straightforward answer to this.
- [37068](https://github.com/space-wizards/space-station-14/pull/37068) Xenoborgs part 5
- [38723](https://github.com/space-wizards/space-station-14/pull/38723) New Feature: Kitchen spike rework
  - Slarti: This needs some bugfixes. I made an [issue](https://github.com/space-wizards/space-station-14/issues/39946).
  - Slarti: Ok, has been fixed [39959](https://github.com/space-wizards/space-station-14/pull/39959)
- [39099](https://github.com/space-wizards/space-station-14/pull/39099) Crawling Fixes Part 4: Can't crawl when weightless.
- [39586](https://github.com/space-wizards/space-station-14/pull/39586) Viable Canesword
- [39648](https://github.com/space-wizards/space-station-14/pull/39648) Prevent shoe buffs while crawling
- [39398](https://github.com/space-wizards/space-station-14/pull/39398) Impaired Mobility Disability
- [38224](https://github.com/space-wizards/space-station-14/pull/38224) Added Hemophilia Trait
- [39130](https://github.com/space-wizards/space-station-14/pull/39130) Admin Log Browser Improvements
    - Ress: Requesting that this is to be held off on a stable merge. There are currently issues with refreshing that makes it unclear if a search query is actually searched for or not.
    And I'd rather not piss off the entire admin team by having something merged that greatly upsets the current workflows. Prior discussions with Southbridge led to solutions hopefully being implemented soonish.
    - Slarti: [Link](https://github.com/space-wizards/space-station-14/issues/39960) to the issue with the mentioned problems.
    - Southbridge: Lets revert this for the stable merge.
- [39775](https://github.com/space-wizards/space-station-14/pull/39775) Recolor Mime and Musician job icons
- [39701](https://github.com/space-wizards/space-station-14/pull/39701) Adds stencil lettering to the spraypainter
- [39807](https://github.com/space-wizards/space-station-14/pull/39807) feat: add verb for smartfridge item insertion
- [39672](https://github.com/space-wizards/space-station-14/pull/39672) Made moths less vulnerable to flames
- [38159](https://github.com/space-wizards/space-station-14/pull/38159) Added more Derelict Cyborgs.
    - Princess: Syndicate Derelict borgs shouldn't have syndi comms or the ability to see syndi icons. I think we should patch this one since it just needs some minor YAML changes and it's a good PR otherwise.
    - Princess: I made a PR: [39978](https://github.com/space-wizards/space-station-14/pull/39978)
- [35100](https://github.com/space-wizards/space-station-14/pull/35100) Inflatable Module
- [38624](https://github.com/space-wizards/space-station-14/pull/38624) Batchable lathe jobs, editable lathe job order
    - Scar: While this PR works well by itself, we should also consider merging [39886](https://github.com/space-wizards/space-station-14/pull/39886) as it makes it infinitely less messy and more convenient to use.
- [39532](https://github.com/space-wizards/space-station-14/pull/39532) Syndicate locks are now selectable
- [39900](https://github.com/space-wizards/space-station-14/pull/39900) TriggerOnSimpleToolUsage and add tool locks to syndicate items
- [39730](https://github.com/space-wizards/space-station-14/pull/39730) Prevented Engiborgs from picking up AI lawboards
- [39901](https://github.com/space-wizards/space-station-14/pull/39901) Wizard can no longer teleport to arrivals
- [37705](https://github.com/space-wizards/space-station-14/pull/37705) Clipboards added to autolathe (and other folder changes)
- [39542](https://github.com/space-wizards/space-station-14/pull/39542) Re-anchorable structures
- [39805](https://github.com/space-wizards/space-station-14/pull/39805) New Feature: Symptoms of radiation poisoning
- [39927](https://github.com/space-wizards/space-station-14/pull/39927) Improved cardboard-weapon descriptions

Conclusions:
- Blocking Issue: Currently late-join players can spawn on the nukie planet. It is likely due to the latejoin spawners not being on all maps. 
    - Fixed
- Related issue: On some maps, people spawn in the warden office, and on Amber people spawn in the Atmos room. May want to check out https://github.com/space-wizards/space-station-14/blob/master/Content.Server/Spawners/EntitySystems/SpawnPointSystem.cs
- Issue: Add a test to check for late join markers on maps. 
- Checklist for late join spawners on maps: https://github.com/space-wizards/space-station-14/issues/39936

Worth mentioning:
- [39791](https://github.com/space-wizards/space-station-14/pull/39791) Moving Zombie Components to Shared
    - Princess: I think I'm with slarti on removing the NetworkedComponent from them. 
    - Slarti: Yep, that should still allow it to be used in entity effects without showing initial infected status to cheat clients. The client does not use these components anywhere since zombification isn't predicted.
        -  Princess: Shiva still knows though :^)
        -  Slam: I go through all the trouble to be hired by Security as II only for Shiva to cheatclient me :(((  (this actually happened)
    - I made a PR [39963](https://github.com/space-wizards/space-station-14/pull/39963)

```admonish info
Weeks without non-squashed merges: 0 :cry:
```
