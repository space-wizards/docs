# Maintainer Meeting (2026-05-23)

:::info
**Attendees:**
- Princess
- Slam
- Jez
- Ada
- Aeshus
- ScarKy0
- Julian
- Simyon
:::

This meeting was recorded:

{% embed youtube id="meow meow :3" loading="lazy" %}

## PSA: new DependencyAttribute source generator

https://github.com/space-wizards/RobustToolbox/pull/6549

In case you did not see it yet, `[Dependency]` now is handled by a source generator. It basically works the same, however dependencies should no longer have the `readonly` keyword and the containing class has to be `partial`. This is enforced with an analyzer that will create a warning, meaning you cannot merge any old PRs that don't do this the new way as they will fail tests in the merge queue.

Important TODO: We should go through all the docs pages containing code examples and update them accordingly.

## PSA: Staff Re-Organization (Princess)
The Staff Re-Organization policy has reached its first working draft. 
I will be posting it all in a thread after the maintainer meeting so be ready!

## PSA: Searching for Maintainer Mentors (Princess)
It's time. 
Sign up to be a Maintainer Mentor here: https://forum.spacestation14.com/t/sign-ups-maintainer-mentor/27650

## PSA: Space Law Changes PR (Princess)
We have a PR up to change space law, it's going to be merged it's just going through one last round of review.
Discourse thread: https://forum.spacestation14.com/t/rework-of-space-law/27643
I presume this is going to go into staging/stable? Since we shouldn't have two sets of rules dependant if you're on master/stable.
Just want to get a consensus on that :V

## Integration Test Superlist
Slam and some other maints have made a big list of areas of the game which lack test coverage. 
That list can be found here:
https://docs.google.com/spreadsheets/d/1hHZIsxbF6-BR0iobeEyNxg78btb4IArHRyA_EvXj7Iw/edit?gid=1578252140#gid=1578252140

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- Slarti
- iaada
- Princess
:::

- [43708](https://github.com/space-wizards/space-station-14/pull/43708) Minor door animation tweak
- [43515](https://github.com/space-wizards/space-station-14/pull/43515) Start splitting out DamageableComponent
- [43161](https://github.com/space-wizards/space-station-14/pull/43161) T-ray scanner modes
- [35653](https://github.com/space-wizards/space-station-14/pull/35653) Injury slowdown resistance for combat and merc boots
- [38691](https://github.com/space-wizards/space-station-14/pull/38691) Air Friction changes for Mobs that can move in air
- [39044](https://github.com/space-wizards/space-station-14/pull/39044) Detective coat changes, let detectives start with a winter coat
- [40519](https://github.com/space-wizards/space-station-14/pull/40519) Enable safety on windoors
- [43699](https://github.com/space-wizards/space-station-14/pull/43699) Added IngestionBlocker modifier to radiation hood
- [43282](https://github.com/space-wizards/space-station-14/pull/43282) Let borg modules exclude other modules
- [43412](https://github.com/space-wizards/space-station-14/pull/43412) Solutions Refactor Part 1 - Solution Prototypes
- [43477](https://github.com/space-wizards/space-station-14/pull/43477) Added new AME controller flatpack, deleted unused crates
- [43673](https://github.com/space-wizards/space-station-14/pull/43673) Redo Changeling Identity Networking + New Objective
- [43675](https://github.com/space-wizards/space-station-14/pull/43675) Changeling voice mimicry
- [43768](https://github.com/space-wizards/space-station-14/pull/43768) Make Mothership explosive again
- [43671](https://github.com/space-wizards/space-station-14/pull/43671) Changeling Biodegrade
- [43759](https://github.com/space-wizards/space-station-14/pull/43759) Changeling gaining DNA
- [39970](https://github.com/space-wizards/space-station-14/pull/39970) Make cyborgs magnetize items
- [39269](https://github.com/space-wizards/space-station-14/pull/39269) Fix loot not spawning on VGRoid
- [43785](https://github.com/space-wizards/space-station-14/pull/43785) Changeling Dna Sting
- [43674](https://github.com/space-wizards/space-station-14/pull/43674) Resprite of the anita and plump pies + add Sliceable
- [43737](https://github.com/space-wizards/space-station-14/pull/43737) Fix ghost follow on antag spawn
- [43810](https://github.com/space-wizards/space-station-14/pull/43810) Allow butter to be mixed into solutions
- [42817](https://github.com/space-wizards/space-station-14/pull/42817) Cremate Verb Icon
- [43809](https://github.com/space-wizards/space-station-14/pull/43809) [NERF] [MICROBALANCE] Make half pipe hold only 100 L
- [43829](https://github.com/space-wizards/space-station-14/pull/43829) Change chemical dispenser and ChemMaster increments
- [43877](https://github.com/space-wizards/space-station-14/pull/43877) Add powered layers for Station Map
- [42145](https://github.com/space-wizards/space-station-14/pull/42145) Examination verb for identity-covering items
- [43910](https://github.com/space-wizards/space-station-14/pull/43910) VULPKANIN TYPING INDICATOR ADDITON
- [43921](https://github.com/space-wizards/space-station-14/pull/43921) Fix Gorlex Hypospray having no delays
- [43963](https://github.com/space-wizards/space-station-14/pull/43963) Added mid-size stack state for bananium
- [43939](https://github.com/space-wizards/space-station-14/pull/43939) Make Botanical Belt in Botany Lockers Filled Instead of Empty
- [43895](https://github.com/space-wizards/space-station-14/pull/43895) Improve Escape Menu
- [43804](https://github.com/space-wizards/space-station-14/pull/43804) allow ammonia to be extracted from biomass via biogenerator.
- [43599](https://github.com/space-wizards/space-station-14/pull/43599) Quality and Sprite changes to Conveyor Belts
- [36701](https://github.com/space-wizards/space-station-14/pull/36701) Buyable + destructible desk bell, desk bell variants
- [43976](https://github.com/space-wizards/space-station-14/pull/43976) replace chainsaw sounds, delete current ones
- [36384](https://github.com/space-wizards/space-station-14/pull/36384) Add Fake Wizard Robes
- [43973](https://github.com/space-wizards/space-station-14/pull/43973) Tradestation now has automated atmos!
- [40444](https://github.com/space-wizards/space-station-14/pull/40444) Minor improvements for holopads
- [43983](https://github.com/space-wizards/space-station-14/pull/43983) Reorder Cow and Goat Mob parent order to give correct stomach type
- [39279](https://github.com/space-wizards/space-station-14/pull/39279) Predict LubeSystem and LubedSystem
- [43533](https://github.com/space-wizards/space-station-14/pull/43533) Exo Station - Psychologist, Botany & Sec updates
- [43889](https://github.com/space-wizards/space-station-14/pull/43889) Hue based skin color clamping
- [37708](https://github.com/space-wizards/space-station-14/pull/37708) Overhauled the Fireaxe and Fire Axe

`Slarti`: Small comment, prediction. bugfix and cleanup PRs can usually be left out of this list.
`Princess` We also have some hotfix PRs that need to be merged:
- [43968](https://github.com/space-wizards/space-station-14/pull/43968) [STAGING] Misc Solution Fixes
    - Make Space Cleaner better to account for smaller spray sizes. Fix firebomb recipe to be craftable.
- [43962](https://github.com/space-wizards/space-station-14/pull/43962) [STAGING] Ensure Antag Ghost Roles make a new mind, add a test for it.
    - Make it so reventant's actions don't stay with a player when they get a new ghost role.
- [43807](https://github.com/space-wizards/space-station-14/pull/43807) [STAGING] Fix End of Round Text not localizing text.
    - Make it so end of round text is localized again
- [43790](https://github.com/space-wizards/space-station-14/pull/43790) [STAGING] Get Rid of a obsolete test failer in IngestionSystem
    - Remove some OnMapInit behavior from IngestionSystem which no longer triggers test fails anymore. This allows for moproaches and monkey cubes to work again.
