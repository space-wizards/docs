# Maintainer Meeting (31 January 2026)

```admonish info

**Attendees:**
- Princess Cheeseballs
- Myra
- Slam
- Ada
- Tiniest shark
- akesima
- Orks
```

This meeting was recorded:

{% embed youtube id="3WnCZrtzBtU" loading="lazy" %}

## What's up with the Roundstart Equipment Design Doc? (Princess)
Follow this template please, two hashtags for h2, bellow it goes the details.
- I've seen a few PRs revolving around the roundstart equipment design doc that have gotten a lot of debate.
- I've also seen that it hasn't been merged yet, but PRs have been made.
- Does it need to be merged? Does it need changes? I feel like we're very disorganized in regards to it.

## Stable review

```admonish info

Write your name here if you read this list fully.
**I checked this PR list:**
- Princess
- ScarKy0
- Slam
- iaada
- Tiniest Shark
- Errant
- Janet
```

- [39684](https://github.com/space-wizards/space-station-14/pull/39684) Camera map
- [42019](https://github.com/space-wizards/space-station-14/pull/42019) Add Mortar and Handheld Juicer
- [42445](https://github.com/space-wizards/space-station-14/pull/42445) Fix flatpacker exploit ignoring board costs
    - `Princess:` I feel like people may mald about this one. There's probably a decent chunk of machine crafting recipies that aren't fun to make. Shouldn't be reverted but expect microbalance to follow.
    - `Slam:` The main one will be the VAW. Good. 
- [42448](https://github.com/space-wizards/space-station-14/pull/42448) Adds more starting materials for the mothership
- [42419](https://github.com/space-wizards/space-station-14/pull/42419) Nubody
    - `Scar:` Have all major bugs regarding nubody been fixed? I recall there being one that allows you to get unobtainable helmets via gibbing.
    - `Princess:` Not yet, I have some here that need to be hotfixed: [42699](https://github.com/space-wizards/space-station-14/pull/42699), [42703](https://github.com/space-wizards/space-station-14/pull/42703), [42709](https://github.com/space-wizards/space-station-14/pull/42709)
        - Done!
- [42372](https://github.com/space-wizards/space-station-14/pull/42372) Adjust the role timers for certain roles.
    - `Princess:` PRs like this and Emisse's new Mapping Standards stuff show we really need better delegation within content still. Stuff like this is very much of admin interest and should be handled majority by admins, and Emisse's mapping standards should be handled majority by the map leads. 
- [42189](https://github.com/space-wizards/space-station-14/pull/42189) Magic 9 Ball
- [42423](https://github.com/space-wizards/space-station-14/pull/42423) Round-start equipment rebalance: Medical
    - `Princess:` I haven't been following the roundstart equipment design doc stuff, but I think overall the changes in this PR were positive. 
- [42477](https://github.com/space-wizards/space-station-14/pull/42477) Adjust various traitor explosives
- [42484](https://github.com/space-wizards/space-station-14/pull/42484) Traitor Chemicals Rebalance
- [42482](https://github.com/space-wizards/space-station-14/pull/42482) Syndicate Wearables Category Rebalances
- [42468](https://github.com/space-wizards/space-station-14/pull/42468) Syndicate Weapons/Ammo rebalances + Weapons Case
- [42536](https://github.com/space-wizards/space-station-14/pull/42536) Remove loadout time towels
- [42476](https://github.com/space-wizards/space-station-14/pull/42476) Visual nubody (humanoid appearance refactor)
- [42539](https://github.com/space-wizards/space-station-14/pull/42539) Inflatable inflation (Add Inflatable Barricades to O2 lockers)
- [42556](https://github.com/space-wizards/space-station-14/pull/42556) "Fix RCD light spam, bypass of indestructible tiles and some plating fixes"
- [42541](https://github.com/space-wizards/space-station-14/pull/42541) Remove "Fuck Lizards" and "Lizard Power" decals from crayondecals.rsi
- [41961](https://github.com/space-wizards/space-station-14/pull/41961) Power Consumers Rebalance: Simple Dynamic Power Loading
- [42510](https://github.com/space-wizards/space-station-14/pull/42510) Tweak traitor deception items
- [42460](https://github.com/space-wizards/space-station-14/pull/42460) Force-prying crit borgs opens borg panel
  - `Slam:` This is a "hidden" interaction. Should probably at least have a guidebook entry.
  - `Scar:` It has a verb whenever you hold a tool (even if incorrect) over a borg, but I agree.
- [34052](https://github.com/space-wizards/space-station-14/pull/34052) Cargo console rework (retry)
- [41943](https://github.com/space-wizards/space-station-14/pull/41943) Colour picker, palettes, & other spraypainter stuff
    - `Princess:` When testing this I was reminded how miserable the UI is for this item.
- [42571](https://github.com/space-wizards/space-station-14/pull/42571) Makes defib cabinets constructable and deconstructable
- [42534](https://github.com/space-wizards/space-station-14/pull/42534) Simplify hands UI code
    - `Princess:` This removed split screen support :godo:
    - `Scar:` Is splitscreen something we even care about whatsoever?
        - `Princess:` No, and it would crash if both mobs had hands anyways so it wasn't even actual support.
- [42409](https://github.com/space-wizards/space-station-14/pull/42409) Grappling rework - Grappling hooks are now physics-driven
- [41352](https://github.com/space-wizards/space-station-14/pull/41352) Add feedback popups
    - `Princess:` How are we going to manage adding and removing feedback popups btw? Proto uploads can get cleared at any time so for long running stuff we'd need to PR it, but PRs need a non-author to approve. Will LMs handle it? Mostly just want some clarification for the future.
    - `Ress:` Wouldn't the simplest solution here to be to add the feedback prompts in the main pr of the feature authors want feedback on? We would be able to use the generic feedback category URL to accomplish this. Alternatively, these PRs are simple YML. And could be subject just be quickly approved?
        - Note, "popup conditions" feature would be nice so we can configure how often they popup like only showing up once per player (and not once per session like right now)
- [42596](https://github.com/space-wizards/space-station-14/pull/42596) Add an option for hold-to-attack in settings
- [42641](https://github.com/space-wizards/space-station-14/pull/42641) restore tritium fire energy to reenable maxcaps
- [42585](https://github.com/space-wizards/space-station-14/pull/42585) Make crowbars consistent with 1x2 item storage
    - `Princess:` A blocker for crowbars being larger is proper item slots in grid inv, and a blocker for that is grid inv being predictable. I am having issues debugging the bug blocking it, but essentially the server sometimes gives the wrong component data for items in containers sometimes. This is visible with status effects which currently mispredict if you have any of the speed boosting effects and your movement speed is refreshed.
- [42545](https://github.com/space-wizards/space-station-14/pull/42545) Move job weh plushies to locker loot
- [41915](https://github.com/space-wizards/space-station-14/pull/41915) Event Rule System Cleanup & Visitor Shuttle Removal
- [42594](https://github.com/space-wizards/space-station-14/pull/42594) Lizard Unhappy
    - `Princess:` What plans are there, if any to replace the sound? Looking into the origin, it's owned by Hannah Barbara Company and definitely not compatible with what we do here so this was the right call.
- [37038](https://github.com/space-wizards/space-station-14/pull/37038) Add Cyborg crew indicator
- [42698](https://github.com/space-wizards/space-station-14/pull/42698) Estoc DMR made Nukie Only

---

- [42520](https://github.com/space-wizards/space-station-14/pull/42520) - Thieving beacons automatically set coordinates when unfolded.
  - `Slam:` Is the "Set Coordinates" verb even necessary anymore then? 
  - `Scar:` Overall I dislike this PR because it feels a bit too "automatic", but nothing beyond my personal distaste.
- [42527](https://github.com/space-wizards/space-station-14/pull/42527) - Make Seed Non-Unique on Sample
- [42444](https://github.com/space-wizards/space-station-14/pull/42444) - Examination verb for insuls
- [42543](https://github.com/space-wizards/space-station-14/pull/42543) - Tile Stacking - attempt 2
- [32932](https://github.com/space-wizards/space-station-14/pull/32932) - Medibot doAfter and some other improvements
- [42453](https://github.com/space-wizards/space-station-14/pull/42453) - Add aloe cream storage sprite
- [39161](https://github.com/space-wizards/space-station-14/pull/39161) - SwitchButton
- [38043](https://github.com/space-wizards/space-station-14/pull/38043) - Replaces thief beer goggles objective with stealing HUD items
- [42172](https://github.com/space-wizards/space-station-14/pull/42172) - Replace metabolism groups with metabolism stages
- [42495](https://github.com/space-wizards/space-station-14/pull/42495) - Ban database refactor
- [42582](https://github.com/space-wizards/space-station-14/pull/42582) - Tweak Traitor Uplink - The Rest of the Uplink
- [42315](https://github.com/space-wizards/space-station-14/pull/42315) - Fix holoparasite stun
- [42612](https://github.com/space-wizards/space-station-14/pull/42612) - De-panic bunker Vulture & set Cvars for feedback panel
  - `Ress:` Chat, we did it! All servers are panic bunker free <3
- [42630](https://github.com/space-wizards/space-station-14/pull/42630) - Improvements to automatic job highlights
- [42649](https://github.com/space-wizards/space-station-14/pull/42649) - Add the Uplink changes to feedback popups.
    - `Scar:` Should this automatically popup round end? Or is that only a thing on vulture?
    - `Ress:` Only on vulture as its currently tagged as `wizden_master`, if you want it to appear everywhere, you'd have to change its popupOrigin to `wizden`.
        - `Princess:` Made a PR to make em popup on stable: [42716](https://github.com/space-wizards/space-station-14/pull/42716)
- [42608](https://github.com/space-wizards/space-station-14/pull/42608) - Health Analyzer Reactivation
