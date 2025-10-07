# Maintainer Meeting (12 April 2025)

```admonish info
- Simyon
- Errant
- Slart
- Scar
- Orks
- Notafet
- Emo (Guest)
- Chromiumboy
- Myra (As audience)
- PJB
```

This meeting was recorded:

{% embed youtube id="n2YTTJUxvhs" loading="lazy" %}

## [SS14-35523](<https://github.com/space-wizards/space-station-14/issues/35523>) is a PR 0 Critical Issue, has been open for 44 days. (Errant)
- We don't really have any idea how to go about solving it, but nevertheless it's a P0 that has been open for a very long time, and perhaps we should focus on what could be done to get closer to getting to the bottom of it
    - Check often on P0 
    - For issues leave replication steps?
- Were any issues noticed?
- Admin ping after meeting to get opinions from admemes
- Might be outdated at this point

## Is the Squash message warning insufficient (Errant)
Every release, we notice a bunch of people not squash merging their pr's

First Myra wants to say, [INSTALL IT PLEASE](<https://greasyfork.org/en/scripts/531064-github-squash-reminder>)

- Is there a reason people are not using the squash merge warning, or is it still insufficient warning? 
    - Merging stuff on mobile platforms where you cannot run userscripts
- Should people start to be reminded about it every time a squash is missed?
(added by myra)
- Should it be policy to require the squash warning script to be installed?
    - Probably not, not everyone wants to run userscripts (or is on mobile)
    - Hard to enforce
   - Seriously this is starting to become a problem now, if we are at the point we have to remind people every release thread this should be policy.
      - "Why is not squashing bad?" 1. Floods the commit history 2. Makes git blame harder to view in certain cases 3. Makes stable review more annoying

## Daylight savings is real and it will hurt you (Myra)
- Do we move maint meetings an hour ahead or behind in these situations? Or just let it stay with the adjustment?
    - We just do whatever discord says when it is (assuming no one has any issues with the time discord says its at)

## Design Doc orginization stuff
- Periodically check on old docs that are not implemented
- New docs will be reviewed in DISCOURSE (MY BELOVED)
- Templates outdated (maybe?)
- Pings about policy changes will continue until docs improve

## Work Groups
- Get rid of them?
- Strike teams soon :tm:
- Discord roles stay as the subscription stuff for pinging maints in review threads is good-ish (to get the roles you ping a PM which kind of sucks)
    - reaction role that shit
- get rid of the Forum category
    - dont if it deletes the topics in there 
- delete the docs page for them

## Chat Refactor (Fildrance)
- [SS14-33858](<https://github.com/space-wizards/space-station-14/pull/33858>) requires architectural review
    - only pjb can do it?
    - just two weeks away
    - requires sign off so it can be cleaned up
    - its very cool that we got this far
        - respect to slam, fsp and fildrance
    - up priority and push it more

## Many PRs
- Maintainer bot (from julian)
- instruct maintainers to review more backlog PRs
- fasttrack old PRs?
- unleash triage team on backlog?
- many old PRs are balance changes or very minor
- limit minor balance changes to maintainers only
    - it goes by us anyways?
    - or make it go by us first (pre approval?)
- ease the requirement to close an old PR?
- make a discourse thread for this

## Stable review
- [25253](https://github.com/space-wizards/space-station-14/pull/25253) Death Nettle changes
- [28573](https://github.com/space-wizards/space-station-14/pull/28573) "I'm Weh-cellent" Cap
- [35123](https://github.com/space-wizards/space-station-14/pull/35123) Sentry turrets - Part 4: The sentry turret and its primary systems
- [35193](https://github.com/space-wizards/space-station-14/pull/35193) Shove down a person on uncuff if harm mode is on
- [36093](https://github.com/space-wizards/space-station-14/pull/36093) Better jetpack emitter
- [36044](https://github.com/space-wizards/space-station-14/pull/36044) More responsive votekick system (reduce timer and successive timeout)
    - dont change config defaults, change config presets instead
    - this PR should have gotten a breaking changes
- [36210](https://github.com/space-wizards/space-station-14/pull/36210) Cleanup and small update to the stethoscope!
- [36201](https://github.com/space-wizards/space-station-14/pull/36201) Undetermined thieving satchel
- [35191](https://github.com/space-wizards/space-station-14/pull/35191) New food recipe: World Peazza
- [36216](https://github.com/space-wizards/space-station-14/pull/36216) add: Dragon rift color changes based on charge
- [36258](https://github.com/space-wizards/space-station-14/pull/36258) Change the name and description of the templar helmet.
- [36212](https://github.com/space-wizards/space-station-14/pull/36212) Diphenhydramine causes drowsiness
- [35863](https://github.com/space-wizards/space-station-14/pull/35863) Improve sprite fading behaviour
    - requires cleanup
- [34566](https://github.com/space-wizards/space-station-14/pull/34566) Add PKA and PTK-800 shuttle gun recipes to sec techfab
    - ship guns that dont take ammo is very abusable
    - ship guns not used often, kinda bloaty 
- [34580](https://github.com/space-wizards/space-station-14/pull/34580) Mob collisions
    - turn off on wizden for now
    - has issues with small mobs (ratkings and stuff)
- [36280](https://github.com/space-wizards/space-station-14/pull/36280) Add 10u of plasma to SyndieJuice
- [36317](https://github.com/space-wizards/space-station-14/pull/36317) Remove "SHUTTLES" from the allergy list in ion_storm.yml
- [36272](https://github.com/space-wizards/space-station-14/pull/36272) Reduce storage implant to a 2x L shape/6 slots
- [36300](https://github.com/space-wizards/space-station-14/pull/36300) Add additional Biome Markers.
- [36113](https://github.com/space-wizards/space-station-14/pull/36113) Centcomm death rattle implant
- [35057](https://github.com/space-wizards/space-station-14/pull/35057) New security box fills, renamed and replaced sechud box icon
- [36380](https://github.com/space-wizards/space-station-14/pull/36380) Printable vials
- [36036](https://github.com/space-wizards/space-station-14/pull/36036) Add inhands for Holoprojectors, labelers, cone, brb sign, fartbag
- [36399](https://github.com/space-wizards/space-station-14/pull/36399) Replaced Sterile Swabs in NutriMax with a Swab Dispenser
- [35152](https://github.com/space-wizards/space-station-14/pull/35152) Feature/shader radial menu
- [36273](https://github.com/space-wizards/space-station-14/pull/36273) Add cooked dragon steak and cutlets
- [36276](https://github.com/space-wizards/space-station-14/pull/36276) Antagonist roles now require 1h playtime.


Wow this is actually probably our smallest release reviews.

### Worth bringing up
- We need ftl file support for the admin upload. (Orks)
   - Otherwise it won't work with localized text. Not sure who best knows how to code that. 
      - Probably sloth, electro or pjb.
    - check localization manager

### Shitposting corner
woof woof arf <- nik rn
simyon is stinky teehee
Let the vox eat trash!
merge vulps immediately
:3 :3 :3
