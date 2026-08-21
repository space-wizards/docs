# Maintainer Meeting (16 August 2025)

```admonish info

**Attendees:**
- Scar
- Myra
- Simyon
- Slam
- Orks
- Errant
- Slarti
- Princess_Chzblz
- Julian
- Tiniest Shark
- Fildrance
- Keron
- Shadowcommander

```

This meeting was recorded:

{% embed youtube id="jfuO05jYIzo" loading="lazy" %}

## Experimental PRs and Feedback (Princess)
- Would be good to have a clear consensus on experimental PRs as a concept
- Also getting in game feedback PR reviewed and merged to line up
- Discuss any PRs we are aware of we could merge as experimental
- Discuss feelings on feedback thread from vulture chem tests
- `Slam`: Relevant PRs: [CL 19](https://github.com/space-wizards/SS14.Changelog/pull/19) & [39686](https://github.com/space-wizards/space-station-14/pull/39686)

## Triage procedure stuffs
- Pull requests have pretty much all been triaged!!!!!!!!!
- Panda came up on stage, who is a recent new triager
    - She discussed about using githubs subissues and types to better triage issues
        - Julian agrees we should keep using these features along with jetfish when it is released to all maints.
        - Should this be policy to use subissues and types?
        - How do we handle the giant pile of issues?
    - Julian thought about allowing triagers to allow to assign stuff to specific workgroups.
    - We should focus on creating bug reports for stuff we see for example on liltenhead videos or in public chat channels/forums.

## Stable review

```admonish info

Write your name here if you read this list fully.
**I checked this PR list:**
- Slarti
- Princess
- Scar
- Southbridge
- Tiniest Shark
- Slam
- Errant
- beck
- Simyon (i spedran this)
- Myra

```

- [39308](https://github.com/space-wizards/space-station-14/pull/39308) Renames slugcat jelly-donuts to scurret jelly-donuts
    - `Simyon`: I am deeply sad
- [38881](https://github.com/space-wizards/space-station-14/pull/38881) Berry Delight
- [35797](https://github.com/space-wizards/space-station-14/pull/35797) Advanced Clowning Module
- [39340](https://github.com/space-wizards/space-station-14/pull/39340) Make wallmount screen, telescreen, and signal timer destructible
- [36935](https://github.com/space-wizards/space-station-14/pull/36935) Xenoborgs part 4
- [39374](https://github.com/space-wizards/space-station-14/pull/39374) Updated syndicate throwing knives description
- [39272](https://github.com/space-wizards/space-station-14/pull/39272) Add Offset Canes + Trinket Canes Group
- [39296](https://github.com/space-wizards/space-station-14/pull/39296) add: air alarm scrubber select all gases button
- [39317](https://github.com/space-wizards/space-station-14/pull/39317) Adds infinite debug power APC, substation, SMES
- [39349](https://github.com/space-wizards/space-station-14/pull/39349) Move scale command to content and turn it into a toolshed command
- [38852](https://github.com/space-wizards/space-station-14/pull/38852) MessyDrinker for dogs
  - `Slarti`: This needs prediction.
  - `Scar`: Ill handle it. PR was originally made before eating/drinking was predicted. (Done: 39660)
  - `Slarti`: Has been addressed
- [37363](https://github.com/space-wizards/space-station-14/pull/37363) Fun with cardboard!
- [39424](https://github.com/space-wizards/space-station-14/pull/39424) add scale:multiplyvector toolshed command
- [34002](https://github.com/space-wizards/space-station-14/pull/34002) Changeling devour and transform
    - `Simyon`: Changeling just a week away
- [33375](https://github.com/space-wizards/space-station-14/pull/33375) Bloonion mutation
- [38392](https://github.com/space-wizards/space-station-14/pull/38392) Resized baseball bats to be more realistic
- [39453](https://github.com/space-wizards/space-station-14/pull/39453) give paused maps from polymorph and cryostorage a name
- [39465](https://github.com/space-wizards/space-station-14/pull/39465) Add changeling briefing sound
- [35277](https://github.com/space-wizards/space-station-14/pull/35277) Sentry turrets - Part 8: AI notifications
- [35531](https://github.com/space-wizards/space-station-14/pull/35531) Starting glasses for Captain and HoP
    - `Slam`: I expect this to result in HoPs being given the spare administration glasses. Really we should find a way to let Captain get a pair of glasses that is only useful for Captain, just so that we stop having Captains pawning off their spare and/or grabbing Secglasses instead.
    - `Slam`: At least it's rarer to see HoPs grabbing secglasses these days since they're Security-restricted.
- [39310](https://github.com/space-wizards/space-station-14/pull/39310) Add voice locks to various hidden syndicate items
- [39531](https://github.com/space-wizards/space-station-14/pull/39531) Adds rare Hamlet variant: Fragile Hamlet
    - `Princess`: Needs conditional triggers when we get them.
    - `Slarti`: We already have trigger conditions, but step triggers are kinda their own separate thing at the moment that then call a normal trigger when succeeding. We got plans to refactor them as well so that they are included into the new system [39267](https://github.com/space-wizards/space-station-14/pull/39267)
- [39562](https://github.com/space-wizards/space-station-14/pull/39562) Base changeling objective(s)
- [38668](https://github.com/space-wizards/space-station-14/pull/38668) Borg hands & hand whitelisting
- [36473](https://github.com/space-wizards/space-station-14/pull/36473) Weapon Resizing
    - `Slam`: I predict this PR to be very impactful for game balance and will be keeping a close eye on it. 
- [39569](https://github.com/space-wizards/space-station-14/pull/39569) Compact Security Jetpacks
- [39621](https://github.com/space-wizards/space-station-14/pull/39621) In Memoriam - Memorializing those who've passed within the SS13+SS14 community
    - `Simyon`: Based and peak
- [39472](https://github.com/space-wizards/space-station-14/pull/39472) Rebalance advanced Brute chems, and more
  - `Slarti`: @Slam, could you update the PR description so that it's more clear what the final changes are and what wasn't included?
  - `Southbridge`: Agreed, it's very difficult to talk to players about this change when half of the info and screenshots of the PR description do not line up with the changes.
  - `Slarti`: Has been updated :thumbsup: (oh god, the emojis on hedgedoc look awful)
  - `Errant` will there be some kind of announcement/communication regarding this?
- [38023](https://github.com/space-wizards/space-station-14/pull/38023) Better robotics console

## Release notes
- BLOCKING (probably I rather wait for this to get patched. KEEP PRIVATE FROM NON STAFF FOR NOW) (Myra) https://discord.com/channels/310555209753690112/1193403928096821358/1406282718060482621
  - `Slam`: If the fix ends up being more complicated, temporarily disabling the relevant item is also an option.
  - `Errant`: Since the ~~demon is already here~~ bug is already on stable, is there a point to consider this a blocker? its not like holding the release back will "protect" stable. If no fix is ready by release time, we should just go ahead normally and hotfix when possible
  - `Myra`: Slart made a fix, they will pr it after the maint meeting.
      - PR: https://github.com/space-wizards/space-station-14/pull/39690
