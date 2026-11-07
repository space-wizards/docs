# Maintainer Meeting (2026-03-28)

:::info
**Attendees:**
- Slam
- Ada
- Scar
- Princess_Chzblz
- Fildrance
:::

This meeting was recorded:

{% embed youtube id="f6dhm62TI9c" loading="lazy" %}

## Topic: April Fools and Experimental PRs
Next week is April fools and we haven't made any plans yet for it.
Next week we also want to test two PRs on Vulture: [42399](https://github.com/space-wizards/space-station-14/pull/42399) and [43042](https://github.com/space-wizards/space-station-14/pull/43042).

- `Slarti`: I won't make it to today's meeting, so I'm just leaving a comment here in advance. I'll probably fix up my leggy and flip emote PRs from last year and put those into an april fools branch and switch the servers to that for a day if no one objects. If other maintainers want to add more stuff that's okay for me as long as it's just small gimmicks and not something like an entire new species, but I don't want to review a massive amount of contributor PRs or fix merge conflicts for it like I had to last year. And please no stuff that massively alters round flow either :sweat: 

- Merge 42399, switch vulture to 43042. Then, for April Fools switch to the April Fools branch which we should open today:tm:

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- Princess
- ScarKy0
- Slarti
- Tiniest Shark
- aada
:::

- [Wrapped parcels can go into mail carts](https://github.com/space-wizards/space-station-14/pull/43226)
    - `Scar`: I think this gives us a cool opportunity to rebrand the mail cart into some delivery cart, considering you can pack things into wrap for ease of transport. 
    - - `aada`: There's a surprising lack of draggable grid inventories, and none that compete with a crates mega storage.
    - `Shark`: That does do a pretty solid job of solving the 'cargo just reshuffles everything into one crate' issue.
- [[Fix] Silicon Ion Law Scramble Text](https://github.com/space-wizards/space-station-14/pull/43229)
- [Move a metric fuckton of AtmosphereSystem to Shared.](https://github.com/space-wizards/space-station-14/pull/42989)
- [fix bottle reagent localization](https://github.com/space-wizards/space-station-14/pull/43208)
- [Fix missing word from emitter alerts](https://github.com/space-wizards/space-station-14/pull/43225)
- [Make EntityTableSpawner spawn relative to grid instead of map](https://github.com/space-wizards/space-station-14/pull/43234)
- [Make the chem guidebook show when chemicals adjust body temperature (again)](https://github.com/space-wizards/space-station-14/pull/42394)
- [Tech disk resprite and pricing changes](https://github.com/space-wizards/space-station-14/pull/37719)
    - `aada`: The pricing changes are a straight buff and tech disks were already a bit of a money factory. Income isn't well balanced but it's another consideration on the pile.
    - **Follow-up PR**: PR that changes the sell values to be more consistent.
        - T1: 50
        - T2: 100-150
        - T3: 1000-1500
- [Update Packed's TEG Burn chamber](https://github.com/space-wizards/space-station-14/pull/43278)
- [Move salvage RandomSpawners to EntityTableSpawners](https://github.com/space-wizards/space-station-14/pull/43233)
- [Borg charger hitbox changes](https://github.com/space-wizards/space-station-14/pull/43300)
- [Move some simple random spawners to entity table spawners](https://github.com/space-wizards/space-station-14/pull/43305)
- [Fix melee attack sprite rotations](https://github.com/space-wizards/space-station-14/pull/43307)
- [Flatpack opening uses collision of flatpacked entity](https://github.com/space-wizards/space-station-14/pull/41849)
- [Improvments for Reach station](https://github.com/space-wizards/space-station-14/pull/43046)
- [trico no longer heals when mob is crit, and no longer heals rad](https://github.com/space-wizards/space-station-14/pull/43293)
- [Fixes ambuzol pills](https://github.com/space-wizards/space-station-14/pull/43331)
- [Change chat straight quotes to curly quotes](https://github.com/space-wizards/space-station-14/pull/43350)
- [Add a holy light effect to bible healing](https://github.com/space-wizards/space-station-14/pull/43189)
- [On Exo, fixed power for AI North and South external cameras](https://github.com/space-wizards/space-station-14/pull/43143)
- [CachedResources for GasTileDangerousTemperatureOverlay](https://github.com/space-wizards/space-station-14/pull/43032)
- [Refactor: Gas tile overlay split](https://github.com/space-wizards/space-station-14/pull/42881)
- [Move ID card name/title length limit to server](https://github.com/space-wizards/space-station-14/pull/43237)
- [Update ruined_prison_ship.yml](https://github.com/space-wizards/space-station-14/pull/43242)
- [Single item cargo orders are delivered in Parcel Wrap instead of crates](https://github.com/space-wizards/space-station-14/pull/40834)
- [Refactor Ion Law string generation](https://github.com/space-wizards/space-station-14/pull/42629)
- [Fix bug blocking character saves for species without hair](https://github.com/space-wizards/space-station-14/pull/43170)
- [Predict reagent grinder](https://github.com/space-wizards/space-station-14/pull/42815)
- [Fixed the two-handed activated sound bug](https://github.com/space-wizards/space-station-14/pull/38070)