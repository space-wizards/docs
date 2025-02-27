# Maintainer Meeting (1 February 2025)

**Time:** 1 February 2025

```admonish info
**Attendees:**
- Myra (Vasilis)
- Errant
- Scugky0
- Slam
- Orks
- Slartibartfast
- Aeshus
- KaronSHB
- Shadowcommander
- Chromiumboy
- Simyon
```

This meeting was recorded:

{% embed youtube id="MywWIHBLyC4" loading="lazy" %}

## 3mo Xeno Arch and its direction
- Could we briefly discuss 3mo Xeno Arch and if we want to help push it through for some future stable release (preferably next, but likely the one after)?
    - Should be split up, 230 files is a bunch to review.
    - Author agrees it is not ready for review due to a PVS bug.

## Design doc discussion thread 
- Design doc templete 
    https://github.com/SlamBamActionman/docs/blob/SlamBamActionman-design-doc-proposal/design-doc.md
    - Example: https://github.com/SlamBamActionman/docs/blob/SlamBamActionman-design-doc-proposal/sec-doc.md
        - Myra says ship it, we should review it internally tho

## Stable review
- [34197](https://github.com/space-wizards/space-station-14/pull/34197) Additional Ionstorm Law Updates
- [33782](https://github.com/space-wizards/space-station-14/pull/33782) Add option to disable bwoink sound.
- [34448](https://github.com/space-wizards/space-station-14/pull/34448) Pride Scarves
- [33809](https://github.com/space-wizards/space-station-14/pull/33809) Space lizard plushie can now be worn on your head
- [34500](https://github.com/space-wizards/space-station-14/pull/34500) Adds bullet collision to wall mounted cameras
- [33871](https://github.com/space-wizards/space-station-14/pull/33871) Add a 10u vial of plasma to the chemical locker
- [34469](https://github.com/space-wizards/space-station-14/pull/34469) Rarer Highcaps
- [34447](https://github.com/space-wizards/space-station-14/pull/34447) New dry fire sound
- [33821](https://github.com/space-wizards/space-station-14/pull/33821) Add Airlocks with Bar and Kitchen access
- [32691](https://github.com/space-wizards/space-station-14/pull/32691) Welding gas mask toggleable with action
- [34502](https://github.com/space-wizards/space-station-14/pull/34502) Electrified doors/windoors now spark, new tips to deal with doors without access or when electrified
- [34232](https://github.com/space-wizards/space-station-14/pull/34232) Blueprint double emergency tank
- [34563](https://github.com/space-wizards/space-station-14/pull/34563) Add system to kick people if they connect to multiple servers at once.
- [34403](https://github.com/space-wizards/space-station-14/pull/34403) Give the chef access to cloth boxes
- [34589](https://github.com/space-wizards/space-station-14/pull/34589) lecter visual update
    - Start a vote for a potencial revert
- [32653](https://github.com/space-wizards/space-station-14/pull/32653) Feature/make radial menu great again
- [34604](https://github.com/space-wizards/space-station-14/pull/34604) Return Drozd full-auto and semi-auto firing modes
- [34076](https://github.com/space-wizards/space-station-14/pull/34076) C4 Helmet
- [34436](https://github.com/space-wizards/space-station-14/pull/34436) Make radioactive material radioactive
- [34258](https://github.com/space-wizards/space-station-14/pull/34258) Renaming sexy mime and clown mask
- [34614](https://github.com/space-wizards/space-station-14/pull/34614) Replace starter borg brain with Positronic
- [34556](https://github.com/space-wizards/space-station-14/pull/34556) display the current version in the changelog window
- [29224](https://github.com/space-wizards/space-station-14/pull/29224) New solar sprites, new solar panel upgrades, and some solar panel fixes.
- [34658](https://github.com/space-wizards/space-station-14/pull/34658) Added Unused HoS's Flask to HoS locker
    - It could use a resprite to be smaller
- [34674](https://github.com/space-wizards/space-station-14/pull/34674) add a chem dispenser to the nukie planet
    - Needs a changelog
- [34087](https://github.com/space-wizards/space-station-14/pull/34087) Hi-viz vest now actually hi-viz
- [33045](https://github.com/space-wizards/space-station-14/pull/33045) Storage UI V2
    - Has a few bugs currently including:
        - Window positioned remembered
        - Star icons are brokie
        - Theres a flicker when inserting items
            - Available options:
                - Revert
                - Keep and hotfix later
                - Block release until bugfix
- [34538](https://github.com/space-wizards/space-station-14/pull/34538) Added Pain Numbness Trait
- [33048](https://github.com/space-wizards/space-station-14/pull/33048) Added the ability for pAIs and station maps to be stored in engineering belts
    - Why specifically engi belt?
        - Maybe the change should be added to other belts too?
- [33062](https://github.com/space-wizards/space-station-14/pull/33062) Engineering guidebook megaupdate v2
- [31626](https://github.com/space-wizards/space-station-14/pull/31626) Add conditional camera offset based on cursor - Hristov Rework, Part 1
    - Should have [31662](https://github.com/space-wizards/space-station-14/pull/31662) merged before release.
- [34079](https://github.com/space-wizards/space-station-14/pull/34079) Fake mindshield componentry and Implanter
    - Has bug that is not on staging [34718](https://github.com/space-wizards/space-station-14/pull/34718)
- [34049](https://github.com/space-wizards/space-station-14/pull/34049) Buff frezon to acceptable values, pending a frezon rework
- [34693](https://github.com/space-wizards/space-station-14/pull/34693) Stun baton precise attack thrust animation
- [34651](https://github.com/space-wizards/space-station-14/pull/34651) New salvage ruin: the ruined prison ship
- [34574](https://github.com/space-wizards/space-station-14/pull/34574) drozd visual update
- [34734](https://github.com/space-wizards/space-station-14/pull/34734) Nuke Timer MinimumTime
- [34593](https://github.com/space-wizards/space-station-14/pull/34593) Fix vulture spawning additional salvage debris
- [32110](https://github.com/space-wizards/space-station-14/pull/32110) Sentient medibot now can inject
- [32352](https://github.com/space-wizards/space-station-14/pull/32352) Criminal Records Computer Better UX + Filtering
- [32502](https://github.com/space-wizards/space-station-14/pull/32502) Added some more borg names
- [33533](https://github.com/space-wizards/space-station-14/pull/33533) Syndicate and CentComm Radio Implanters
- [33346](https://github.com/space-wizards/space-station-14/pull/33346) New Highpop map: Convex recreational complex
- [34337](https://github.com/space-wizards/space-station-14/pull/34337) Seperate EMAG into EMAG and Authentication Disruptor
- [34463](https://github.com/space-wizards/space-station-14/pull/34463) Astro Asteroid Sand
- [34721](https://github.com/space-wizards/space-station-14/pull/34721) The Goliath Hardsuit
- [34730](https://github.com/space-wizards/space-station-14/pull/34730) Juice that makes you go boom
- [33454](https://github.com/space-wizards/space-station-14/pull/33454) Adjust inventory size of ginormous scrap
- [33932](https://github.com/space-wizards/space-station-14/pull/33932) Add history tab to bounty console
- [33512](https://github.com/space-wizards/space-station-14/pull/33512) Minor shotgun changes and comments for future changes
    - https://tryitands.ee
- [34557](https://github.com/space-wizards/space-station-14/pull/34557) Fixed: Ore now correctly drops the right amount of ore
- [34772](https://github.com/space-wizards/space-station-14/pull/34772) Implement mrp rule changes pursuant to community votes

### Things to note:
- Airlocks not closing caused by a new RT release
    - https://github.com/space-wizards/space-station-14/issues/34779
        - Sloth claims a fix was made on engine, once new engine releases hotfix it into engine.
            - If there is no fix we revert the engine version.
- Renable small salvage wrecks for all servers
    - https://github.com/space-wizards/space-station-14/pull/34593
        - Make a vote to discuss it.
- Reminder for us to remove the 10th anniversary duct tape logo if we have not
    - Forks dont like it (even though they could like... fix it) so yeah sure. Revert it.
- Hotfix these?
    - https://github.com/space-wizards/space-station-14/pull/34751
    - https://github.com/space-wizards/space-station-14/pull/34793
        - Make a vote
- To review:
    - https://github.com/space-wizards/space-station-14/pull/32136