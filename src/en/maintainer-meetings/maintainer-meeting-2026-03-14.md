# Maintainer Meeting (2026-03-14)

:::info
**Attendees:**
- Slam
- TiniestShark
- Errant
- Chzblz
- Julian
- Slarti
- Scar
:::

This meeting was recorded:

{% embed youtube id="meow meow :3" loading="lazy" %}

## Topics go here (Your name)
Follow this template please, two hashtags for h2, bellow it goes the details.
- Prefebly try to seperate them like this with doted lines
- Fun fact! You can remove the example template options if you want!

## Topic: The new roadmap (Slarti)

I started converting the [preliminary roadmap](https://hedgedoc.spacestation14.com/RCRDvbSmTzmoQuLcgoMAxQ?both#) (public link [here](https://hedgedoc.spacestation14.com/s/5wpBdb7Oq#)) into a [github project](https://github.com/orgs/space-wizards/projects/60/views/6), and I'm aiming to get it done until this maintainer meeting. For a few points I'll still need some more details from specific maintainers or workgroups, but that can be done over time.

The goals is to give more direction to the contributions we get, rather than contributors having to take guesses which features will be accepted by maintainers or not, and we often had to decline already fully coded new features in the past.

I chose a github project for this to make it easy to keep track of and edit any issues, or to add new ones.

The roadmap should only contain major refactors, reworks and new gameplay features, smaller stuff should simply be a normal issue so that we do not spam the roadmap too much. I recommend making mega-issues that keep track of a list of subissues and then include only the mega-issue in the roadmap. If you want to add something best do a quick check with the other maintainers first.

We might want to pin it somewhere visible or mention it on the docs repo or the website, so that players and forks will be able to see our long-term

## Topic: Core Design Pillars (Princess)

I made a draft of some new core design pillars [core pillars](https://hedgedoc.spacestation14.com/6Ci0Wm2BR4i5Vym4GnztrA#) to replace the old ones. They're heavily inspired by the old ones with some clarification and changes. 

I'd like people's general thoughts on them, before I move onto other pillars for things like round flow and antagonists and such. Be sure to mention things that should be clarified and/or added. Although if your suggestion is too specific it might be best put in a future doc :P

## Topic: Protobreak (Slam/Princess)

Slam has hosted a few playtests of a prototype break salvage. This is here to discuss them and if we think this design has a future/what is needed/general thoughts and or questions.

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- ScarKy0
- Princess Cheeseballs
- Tiniest Shark
:::

- [43035](https://github.com/space-wizards/space-station-14/pull/43035) - Fix hypodart uplink description
- [42972](https://github.com/space-wizards/space-station-14/pull/42972) - Stop AI knocking on shutters, blast doors
- [42962](https://github.com/space-wizards/space-station-14/pull/42962) - Add building animations to techfabs
- [43049](https://github.com/space-wizards/space-station-14/pull/43049) - Make DamageSpecifier serializable & obsolete DamageGroups
  - `Slarti`: This and the other PR below containing changes to how damage works from a technical standpoint also include some balance changes to chemicals as a side-effect. It's totally expected for this to happen with the current speed of development of medical refactors, trying to keep balance exactly the same as it was each step along the way is completely unfeasible, and the balance will need a major overhaul anyways once limb and organ damage are implemented. But last time this balance was touched things got *very* heated, so it's important that we correctly communicate this to the players to make clear that this is temporary and not representative of the final product. I already left some comments on this and the other PR that you can use as a reference in case anyone complains. We could also give lilten a head up for his next video.
  - **HOTFIX**: https://github.com/space-wizards/space-station-14/pull/43056
- [43055](https://github.com/space-wizards/space-station-14/pull/43055) - Make sure vox passively regenerate at the same pace as everyone else
- [43021](https://github.com/space-wizards/space-station-14/pull/43021) - Dynamic feedback popup
- [42796](https://github.com/space-wizards/space-station-14/pull/42796) - Xenoborg extractor
    - `Princess` Was made as a test and needs to be reverted as it didn't have a full review.
    - **HOTFIX**: Revert this and 43007!
- [43061](https://github.com/space-wizards/space-station-14/pull/43061) - Adding serpentcrest to map pool + overhauling several rooms
- [43064](https://github.com/space-wizards/space-station-14/pull/43064) - Change Bad Chembottle Suffixes
- [43013](https://github.com/space-wizards/space-station-14/pull/43013) - Add xenoborg gun sprites
- [42970](https://github.com/space-wizards/space-station-14/pull/42970) - Remove unused noise texture
- [42899](https://github.com/space-wizards/space-station-14/pull/42899) - Removed rollerskates & clown-outfit cargo bounties; reduce pancakes needed for pancake cargo bounty
- [43063](https://github.com/space-wizards/space-station-14/pull/43063) - [Fix] Door remote fixes
- [43089](https://github.com/space-wizards/space-station-14/pull/43089) - APC building doAfter fix
- [43072](https://github.com/space-wizards/space-station-14/pull/43072) - Fixed Mining Hardsuit Helmet Name + Added Internals to Crates
- [43109](https://github.com/space-wizards/space-station-14/pull/43109) - Hyper autolathe now requires the same ammount of manipulators as auto… lathe
- [43007](https://github.com/space-wizards/space-station-14/pull/43007) - Remove salv stuff from mothership
    - `Princess` Needs to be reverted with 42796
- [43038](https://github.com/space-wizards/space-station-14/pull/43038) - Brings Estoc DMR accuracy to standard rifle accuracy, removes movement speed debuff
- [43103](https://github.com/space-wizards/space-station-14/pull/43103) - Initial decoupling pass on Damageable
  - `Slarti`: See my comment above
- [43096](https://github.com/space-wizards/space-station-14/pull/43096) - Vulpkanin Gauze
- [43131](https://github.com/space-wizards/space-station-14/pull/43131) - Nukie guidebook improvements
- [41427](https://github.com/space-wizards/space-station-14/pull/41427) - Weather entities
- [43047](https://github.com/space-wizards/space-station-14/pull/43047) - Vent Hordes
