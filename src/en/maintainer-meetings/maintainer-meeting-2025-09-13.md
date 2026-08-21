# Maintainer Meeting (13 September 2025)

```admonish info

**Attendees:**
- Myra
- ArtisticRoomba
- Errant
- Scarky0
- Slarti
- Simyon
- Tiniest shark 
- Slam
- Julian

```

This meeting was recorded:

{% embed youtube id="N5-UYCLha2I" loading="lazy" %}

## De-enumifying skin colors (ScarKy0)
We have two PRs that do the same thing, we should probably decide which one to use. While not a major blocker for anything, it would be good to get them in the same release as Vulpkanins due to them needing some sort of color clamping. (Read my notes under the PR below)
- We will look at and merge Jannet's PR and notify scar when its merged.
- Blocker for merge

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- ScarKy0
- Errant
- Princess
- Slarti
- Tiniest Shark
:::

- [#37661](https://github.com/space-wizards/space-station-14/pull/37661) Add senior courier PDA for cargo techs
- [#38144](https://github.com/space-wizards/space-station-14/pull/38144) Fix small issues with Text Highlighting
- [#39358](https://github.com/space-wizards/space-station-14/pull/39358) Updated Aseprite Tools
- [#39948](https://github.com/space-wizards/space-station-14/pull/39948) Remove a default Cyborg name
- [#39950](https://github.com/space-wizards/space-station-14/pull/39950) Stop Sentience Event targeting Zombified Creatures
- [#35236](https://github.com/space-wizards/space-station-14/pull/35236) Sentry turrets - Part 7: Electronics and construction graphs
- [#38774](https://github.com/space-wizards/space-station-14/pull/38774) Scurrets - can wear pet bags, mail bags and spears
- [#39989](https://github.com/space-wizards/space-station-14/pull/39989) Messy drinker immunity and cleanup
- [#39931](https://github.com/space-wizards/space-station-14/pull/39931) Clown bags squeak when inserting items
- [#39880](https://github.com/space-wizards/space-station-14/pull/39880) Do after checks for being inside container
    - `Princess`: BLOCKER. This has broken meatspikes. You can no longer butcher entities on them, and can't pull entities off of meatspikes. I have a fix PR up I need to rebase to stable. 
        - [#40299](https://github.com/space-wizards/space-station-14/pull/40299)
- [40026](https://github.com/space-wizards/space-station-14/pull/40026) Lizard Tails Can Be Hidden By Clothing
- [39718](https://github.com/space-wizards/space-station-14/pull/39718) Update 4 visitor shuttles & nanomed inventories
- [39859](https://github.com/space-wizards/space-station-14/pull/39859) Adds a secHUD to the noir-tech glasses
- [39810](https://github.com/space-wizards/space-station-14/pull/39810) Trimmed Sentience Targets from Corgis Smile and Cockroaches
- [39351](https://github.com/space-wizards/space-station-14/pull/39351) Helm + Mask Displacements for Reptilians (and some unique helmets)
- [39083](https://github.com/space-wizards/space-station-14/pull/39083) Some more vox customization
- [39814](https://github.com/space-wizards/space-station-14/pull/39814) Add inhand sprites to Cartons and Cups, give new inhands to Cans.
- [39894](https://github.com/space-wizards/space-station-14/pull/39894) Burger Inhands
- [40085](https://github.com/space-wizards/space-station-14/pull/40085) Berry Delight recipe edit
- [39238](https://github.com/space-wizards/space-station-14/pull/39238) Atmos Delta-Pressure Window Shattering
    - `ROOMBA`: This has a major bug that affects thindows, I know how to fix it but I don't have any time in my life right now to afford it. Non-blocking. 
- [40098](https://github.com/space-wizards/space-station-14/pull/40098) Give inflatable walls the DeltaPressure component
- [39107](https://github.com/space-wizards/space-station-14/pull/39107) Add heat distortion shader for hot gases
    - `Scar`: BLOCKER. The shader is currently broken in negative tile coordinates. We need to hotfix the fix [#40228](https://github.com/space-wizards/space-station-14/pull/40228) and [#40186](https://github.com/space-wizards/space-station-14/pull/40186)
- [40053](https://github.com/space-wizards/space-station-14/pull/40053) Fool players with decoy presets
- [40097](https://github.com/space-wizards/space-station-14/pull/40097) Add 2.25 second delay to scurret petting
- [40099](https://github.com/space-wizards/space-station-14/pull/40099) Can't crawl over counters
    - `Princess`: Needed feature but I worry it's poorly communicated to players, also this affects mice's ability to enter the kitchen on several maps. We may want to look at the fixture layers we have in the future, we have one layer literally only used by the singularity that we could use if needed that could be repurposed as a "floor collision" layer for very short entities.
    - `Slarti`: Distinguishing between tables and counters is not a good way to solve this since there is no good visual indication which is which. I would prefer reverting this and finding another solution, or prevent crawling under any table, but keep the ability for mice to move below them.
    - `Scar`: I agree to reverting until we get some proper way to handle fixtures.
        - [BLOCKING] REVERT VOTE: Revert, keep
- [40063](https://github.com/space-wizards/space-station-14/pull/40063) Fixes Theobromine missing from Iced Coffee
- [39932](https://github.com/space-wizards/space-station-14/pull/39932) Fixed a error in the "Adventures of Ian and Renault" books
- [40126](https://github.com/space-wizards/space-station-14/pull/40126) Give shutters the DeltaPressure component
- [37539](https://github.com/space-wizards/space-station-14/pull/37539) Vulpkanin Species
    - `Scar`: This is the best day this project had ever since the release of Station AI. Yip Yap Growl Whine.
    - `Scar`: For real though, vulpkanin colors arent currently clamped due to the PR allowing to do so being unmerged. While I wouldn't count this as a blocker, it would be good to get that PR in right now, as to not break any characters next stable. [#40067](https://github.com/space-wizards/space-station-14/pull/40067) or [#39175](https://github.com/space-wizards/space-station-14/pull/39175). Notify me once either gets merged and I'll make the PR for clamping the colors.
    - `Slarti`: I would consider this a blocker for the release. Currently you can pick extremely saturated colors, and if we fix it at a later point players will complain that we are breaking their characters, so this should be part of the initial release.
        - [BLOCKER] ee above and above meeting note
- [38424](https://github.com/space-wizards/space-station-14/pull/38424) Adjusted minimumPlayers for Wizard midround events.
- [40133](https://github.com/space-wizards/space-station-14/pull/40133) Drink outta da toiler
    - `Errant`: Do you think god stays in heaven because he too lives in fear of what he has created? 
    - `Slarti`: God is dead and we killed him.
- [40158](https://github.com/space-wizards/space-station-14/pull/40158) Revert antique laser and appraisal tool sizes
- [31213](https://github.com/space-wizards/space-station-14/pull/31213) Add some alternate jumpsuit designs which can be toggled
- [40194](https://github.com/space-wizards/space-station-14/pull/40194) Atmos dP Guidebook Entry
    - `ROOMBA:` Still needs guidebook links on inspect. Non-blocker, just a pain to do considering guidebook inheritance.
- [39983](https://github.com/space-wizards/space-station-14/pull/39983) Being grappled with a grapple gun allows you to cross chasms
- [40211](https://github.com/space-wizards/space-station-14/pull/40211) Lets diona sap trigger artifact blood nodes
- [40206](https://github.com/space-wizards/space-station-14/pull/40206) Derelict Mediborgs can Scan Solutions and see Mob Health
- [37113](https://github.com/space-wizards/space-station-14/pull/37113) Add support for contraband text to the reagent guidebook
- [39024](https://github.com/space-wizards/space-station-14/pull/39024) "idk" no longer shrugs, instead sanitizing to "I don't know"
- [40265](https://github.com/space-wizards/space-station-14/pull/40265) Make Butterflies zombie immune
- [32139](https://github.com/space-wizards/space-station-14/pull/32139) Add admin shuttles
- [40143](https://github.com/space-wizards/space-station-14/pull/40143) No take; Only throw.
- [39203](https://github.com/space-wizards/space-station-14/pull/39203) Food Item Size Adjustment
- [39879](https://github.com/space-wizards/space-station-14/pull/39879) Added SmartFridge circuitboards
- [40294](https://github.com/space-wizards/space-station-14/pull/40294) Clake frag round fix
    - `Errant`: What impact does this have on the weapon's DPS, does balance/pricing need to be revisited? Was this considered when merging?
        - `Princess`: The grenade had its explosive damage reduced heavily in a different PR and was given projectiles instead to make up for it. Trigger refactor broke it so the projectiles wouldn't fire, this just makes them fire.

### The maint meeting buffet
unlike admin meets, we have food here.
ps: if you dont bring anything i will bully you
- Myra: Chicken nuggets
- Simyon: Hamburgers
- Scar: Chocolate
- Julian: Chicken soup
- Tiniest Shark: Cheap Pizza
- Roomba: those really cheap paper-tasting fortune cookies from panda express
- CptJeanLuc: Crispy Fried Vox Wings


:::info
Weeks without non-squashed merges: 0
Please install Myra's warning script.
:::
