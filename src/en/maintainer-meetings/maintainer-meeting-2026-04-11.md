# Maintainer Meeting (2026-04-11)

:::info
**Attendees:**
- Julian
- Geeky
- Slart
- Princess_Chzblz
- Scar
- āda*
- Roomba
- Slam
:::

This meeting was recorded:

{% embed youtube id="meow meow :3" loading="lazy" %}

## Trail maintainer policy
weh
https://github.com/space-wizards/docs/pull/613

Slarti: I'm still writing down my notes for the intro voice chat session, but I was quite busy this week, sorry for the delay.

## Reverting the changes to the review policy
The changes need to be revised and voted on.
We should ask zoldorf to press the funny button.

## Second Hand Items Test (Princess/Daxter)
Second hand items test has conclused! And we have some results from testing.
- Results were inconclusive. People either very positive or very skeptical of them, and testing didn't really answer any potential questions to problems that arose, mostly in regards to balance.
- It's also going to need to have some rewrites considering systems it touched were touched by uplink refactors, and I was pretty lazy with resolving the merge conflicts. :P

Conclusion: Expand the test for 2 more weeks, don't merge into stable.
Maybe polish it a little and keep an eye on balancing to prevent meta choices.

## Vent Critters Autoattack Test (SlamBamActionMan/Princess)
Vent critters autoattack test has been concluded.
- We have basically no feedback at all.
    - `Slam:` Pretty sure the feedback popup just plain did not work during testing. I tried a few rounds and I never got it to show up. :/
- Honestly, with vent hoardes I haven't seen issues with this on stable in a long while.
    - `Slam:` I observed this having the intended effect! Had a round where I observed a player playing a very intentionally friendly spider (they ended up being killed by a borg after biting them too much), and in deadchat they said that the feature made them keep a careful distance from other crew. 
    - Personally I tried to be a bartender spider but ended up biting Pun Pun by accident, who I then got in a fight with, and crew thought I was hostile for it and killed me. Which, yeah, what is the antag vent spider doing behind the bar counter pretending to serve drinks?

Conclusion: Revert because the code still needs changes.
Probably not needed anymore with vent hordes, maybe make them weaker and allow them to be free agents.

## PSA: New dependency injection features (Slarti)
https://github.com/space-wizards/RobustToolbox/pull/6394
In case you missed it, inside `EntitySystem`s you can now use
`[Dependency] private readonly EntityQuery<PhysicsComponent> _physicsQuery = default!;`
instead of calling `GetEntityQuery` in `Initialize()`.

Inside `BUI`s you can now use system dependencies as well, not only Manager dependencies.

This saves a lot of boilerplate and we started cleaning this up (see [#43479](https://github.com/space-wizards/space-station-14/issues/43479)) to avoid contributors copy pasting it from old systems. Please make sure that newly merged PRs don't contain any code doing this the old way.

## Normalizing the usage of the Tester role (ArtisticRoomba)
Forewarning that I won't be able to attend the meeting - I'll be in a study session at uni cramming for finals.

I'm probably going to start pinging the tester role whenever I change something deep/impactful with Atmospherics asking people to keep a watch out for (x, y, z). I think other maintainers should do the same if they'd like the community to keep an out for things.

## Code freezes for admin logging refactor (Slarti)
https://github.com/space-wizards/space-station-14/pull/43538
The PR is massive, will probably take a while to review and merge conflict a lot since it's touching many systems, so we should probably add some code freezes until it's merged.

Some notes from Geeky

>Things that should be frozen:
>- Any form of Logging changes, the old system is being replaced
>- Any Admin tooling/ systems, as they would require the audiet logging that would be implemented by this.
>- Most Likley any form of DB changes
>- Just a side note: julain can speak more on it if hes at the meeting, but this is a clean cut of the old system. the Migration will drop the tables entirely, This migration requires a backup, system. An archival system is in the works however, and will be a ss14 admin system that will manage the partitioning of the logs.

Conclusion: Full freeze announcement not needed because we don't get many DB PRs anyways. AdminLogger API method gets renamed to stay backwards compatible and not merge conflict a billion systems.

> We are going to implement partitioning alongside the refactor (this is purely an infrastructure change and transparent to content).
> The old admin log table will be truncated to the last two months of logs and renamed so those will still be around for a bit.
> \- Julian

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- Slarti
- aada
:::

- [43371](https://github.com/space-wizards/space-station-14/pull/43371) Fix: Make clockwork glass grindable
- [43362](https://github.com/space-wizards/space-station-14/pull/43362) Makes singularities respect reduced motion option
- [41878](https://github.com/space-wizards/space-station-14/pull/41878) "Reduce motion of visual effects" now works for blood loss effect
- [42973](https://github.com/space-wizards/space-station-14/pull/42973) Heat distortion shader
- [40498](https://github.com/space-wizards/space-station-14/pull/40498) Remove PDA equip sprites
- [43392](https://github.com/space-wizards/space-station-14/pull/43392) Lathe Menu Title Enhancement
- [43395](https://github.com/space-wizards/space-station-14/pull/43395) Reduce speso value of tech disks
- [43349](https://github.com/space-wizards/space-station-14/pull/43349) Enables Auto-Whitelisting
- [43217](https://github.com/space-wizards/space-station-14/pull/43217) Adjust naming rules to allow give any job with a custom name leniancy
- [43012](https://github.com/space-wizards/space-station-14/pull/43012) Greatly reduce spawn rate of salt ore
- [43207](https://github.com/space-wizards/space-station-14/pull/43207) Gametest Part 2: Preliminary refactor every test to use GameTest as the framework.
- [43429](https://github.com/space-wizards/space-station-14/pull/43429) New Wizard robe and hat in-hand sprites
- [42399](https://github.com/space-wizards/space-station-14/pull/42399) Force Vent Critters to Attack
    - `Princess`: DONT FORGET TO REVERT!!!
- [42135](https://github.com/space-wizards/space-station-14/pull/42135) Hijack the Automated Trade Station objective
  - `Slarti`: Needs some code cleanup, I'm leaving a review.
      - `Princess`: I can address the review, but it's likely the current system will be replaced with one from a different PR.
      - `Slarti`: NOTE TO SELF: MERGE BUGFIX PR INTO STABLE BEFORE STABLE RELEASE
- [41633](https://github.com/space-wizards/space-station-14/pull/41633) Add blacklist to entitystoragecomponent, add blacklist to genpop lockers
  - `Slarti`: The default whitelist datafield value that was added to the component is a pretty massive breaking change for prototypes. Doesn't this change the behaviour of lockers etc quite a lot? Since there is a new blacklist datafield I think it makes sense to keep the whitelist datafield empty by default.
      - `Princess`: The code for entity store would hard check for the components that are now default in the whitelist before. This is a pretty big breaking change though.
      - `Slarti`: Should be fine then :+1:
- [43448](https://github.com/space-wizards/space-station-14/pull/43448) Removed JuicePotato reagent
- [43400](https://github.com/space-wizards/space-station-14/pull/43400) Add "failed to load crew manifest" message
- [43388](https://github.com/space-wizards/space-station-14/pull/43388) Fix banana creampie visuals, allow station AI to be pied
- [43428](https://github.com/space-wizards/space-station-14/pull/43428) Remove unused space worldgen.
- [41503](https://github.com/space-wizards/space-station-14/pull/41503) Add tile gun module
- [43057](https://github.com/space-wizards/space-station-14/pull/43057) Traitor Syndicate Reinforcement rebalance
- [40645](https://github.com/space-wizards/space-station-14/pull/40645) Make Chargers Items (Pickupable)
- [43445](https://github.com/space-wizards/space-station-14/pull/43445) Add random sell value to player mobs
- [43296](https://github.com/space-wizards/space-station-14/pull/43296) Replace space dragon timer deletion with gibbing
- [43243](https://github.com/space-wizards/space-station-14/pull/43243) Adds the scout xenoborg jump module
- [42947](https://github.com/space-wizards/space-station-14/pull/42947) Add lobby screen invisiblewall
- [38712](https://github.com/space-wizards/space-station-14/pull/38712) Universal uplink code
  - `Slarti`: Needs some bugfixes before the stable release
      - `Princess`: The bugfixes [43501](https://github.com/space-wizards/space-station-14/pull/43501)
      - MERGE BEFORE RELEASE
- [39173](https://github.com/space-wizards/space-station-14/pull/39173) Add parallelization to RadiationSystem.GridCast
    - `Princess`: Also needs some bugfixes before stable release, there's 2 PRs open that take different approaches [43508](https://github.com/space-wizards/space-station-14/pull/43508) and [43504](https://github.com/space-wizards/space-station-14/pull/43504)
    - MERGE PRINCESS PR BEFORE RELEASE

- [43458](https://github.com/space-wizards/space-station-14/pull/43458) Remove ambuzol and ambuzol plus from pill canister random
- [35237](https://github.com/space-wizards/space-station-14/pull/35237) Ports honkmother mitre from /tg/station 13, renames honkmother coat
- [43466](https://github.com/space-wizards/space-station-14/pull/43466) Make cameras react to the AI eye nearby
- [43513](https://github.com/space-wizards/space-station-14/pull/43513) Add notification for AI core being damaged
- [43322](https://github.com/space-wizards/space-station-14/pull/43322) Travel Camera
- [43505](https://github.com/space-wizards/space-station-14/pull/43505) Cause Anomalies to Go Supercritical [Traitor Objective]
- [43462](https://github.com/space-wizards/space-station-14/pull/43462) KILL THE AI [New Traitor Objective]
- [39767](https://github.com/space-wizards/space-station-14/pull/39767) Add nuke disk's location to nukeops greentext
- [43431](https://github.com/space-wizards/space-station-14/pull/43431) Expanded Tile Recipes for Cutter Machine
- [43486](https://github.com/space-wizards/space-station-14/pull/43486) Web vest resprites
- [43346](https://github.com/space-wizards/space-station-14/pull/43346) Add logic to Debug/Set Outfit command to also fill storage containers
