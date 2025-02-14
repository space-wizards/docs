# Maintainer Meeting (18 January 2025)

**Time:** 18 January 2025

```admonish info
**Attendees:**
- Myra (Vasilis)
- Simyon
- ScugKy0
- Errent
- Aeshus
- Orks
- chromiumboy
- Julian
- PJB
```

This meeting was recorded:

{% embed youtube id="JNNk3PwQXfI" loading="lazy" %}

## WELCOME NEW MAINTS
- Welcome to hell

@Boaz(Johan Ullman/Silas) 
@Aeshus 
@Simyon 
@Orks (Beck T) 
@ScugKy0 (Kristopher Laborde) 

## Release schedule, but specifically. Second maint meeting? (Errant)
- https://discord.com/channels/310555209753690112/1329098063532523621

- What time should stable publish happen in, we should vote on this
- The general proposal is fine, funnily enough i did some of it here on accident before the meeting. We could vote on it and do minor changes.
- Should we cancel the second maintainer meetings? They dont seem to be getting anyone

## Accepting one of the three AI design docs that are floating around (Chromiumboy)
- https://discord.com/channels/310555209753690112/1329103080163250207/1329110051159281684
- By [Moony](https://github.com/space-wizards/docs/pull/160)
- By [Saphire](https://github.com/space-wizards/docs/pull/334)
- By [Aeshus](https://github.com/Aeshus/docs/blob/ebcf19a686b3b6a7240fbc9e916b530bfeeccacd/src/en/space-station-14/round-flow/proposals/station-ai.md) (wait this is not a pr?)
    - Ok these are too many words to read out in one maintainer meeting. We can decide in a vote later on.
- [Law syncing](https://github.com/space-wizards/docs/pull/361) 
    - Admin guidence required.

## 10 year anniversarry tomorrow (Errant)
- We have planned basically nothing, we already locked the release candidate 2 days ago, can we rush something in the last second?
    - [We did this I suppose](https://github.com/space-wizards/space-station-14/pull/34486)
    - admins can run an event i suppose
    - There will be a website annoucement too i suppose

## Make a role for stable release?
- Sure, prob through reaction role

## We need a better release model (again)
- TLDR: We do Release reports
- In general we should have someone write up all the changes.
- Pairs nicely with the ping discussed above.
- (not in this release tho hell no)

## Githubs new "Types" feature for Issues
- We could turn some labels to "types"

## About old maintainers that are inactive currently
- We should probably ask them if they still wanna be on the team. Otherwise we dont really want to remove anyone currently for inactivity.

## Stable review
- [34085](https://github.com/space-wizards/space-station-14/pull/34085) Elkridge Depot (The station formerly known as Cell) 
- [32280](https://github.com/space-wizards/space-station-14/pull/32280) Apply forensics when loading with an ammo box
- [34128](https://github.com/space-wizards/space-station-14/pull/34128) Fix rainbow lizard plushie inhands
- [33783](https://github.com/space-wizards/space-station-14/pull/33783) Lobby chat width and custom lobby titles
- [34070](https://github.com/space-wizards/space-station-14/pull/34070) Adds bullet collision to station lights
- [34051](https://github.com/space-wizards/space-station-14/pull/34051) Remove kessler and zombeteors gamemodes from the secret pool
- [34182](https://github.com/space-wizards/space-station-14/pull/34182) Added distinct ad and bye chatter to Dr. Gibb vending
- [34233](https://github.com/space-wizards/space-station-14/pull/34233) Implement approved rule changes
- [34263](https://github.com/space-wizards/space-station-14/pull/34263) Update vessel_warning.ogg
- [34273](https://github.com/space-wizards/space-station-14/pull/34273) Add bleating accent to goats
- [34326](https://github.com/space-wizards/space-station-14/pull/34326) change locking to use ComplexInteraction
    - Do a keep revert vote
- [34178](https://github.com/space-wizards/space-station-14/pull/34178) Drink titles and soda vendor consistency
- [34341](https://github.com/space-wizards/space-station-14/pull/34341) Renamed water melon juice to watermelon juice
- [34346](https://github.com/space-wizards/space-station-14/pull/34346) Copy Thresholds Added to Air Alarms
- [34193](https://github.com/space-wizards/space-station-14/pull/34193) Fixed Forensic Gloves to be Security Contraband
- [34240](https://github.com/space-wizards/space-station-14/pull/34240)  add large instruments to the cargo request computer
- [34219](https://github.com/space-wizards/space-station-14/pull/34219) Adds a border to Oppenhopper poster
- [34369](https://github.com/space-wizards/space-station-14/pull/34369) Add a popup message when ghost Boo action does nothing
- [34368](https://github.com/space-wizards/space-station-14/pull/34368) Let ghosts sometimes make certain devices say creepy things
- [34367](https://github.com/space-wizards/space-station-14/pull/34367) Add directional escape pod sign
- [34339](https://github.com/space-wizards/space-station-14/pull/34339) Make indestructible tiles not breakable by explosions
- [33420](https://github.com/space-wizards/space-station-14/pull/33420) Role Types
- [34198](https://github.com/space-wizards/space-station-14/pull/34198) HOTFIX Tweaked air alarm default settings for nitrogen breathing crew
- [34394](https://github.com/space-wizards/space-station-14/pull/34394) Bomb defusal lockers always should have tools
- [34401](https://github.com/space-wizards/space-station-14/pull/34401) Reduce Panic Bunker Minimum Playtime to 2 hours
- [33339](https://github.com/space-wizards/space-station-14/pull/33339) Add IPIntel API support
- [34270](https://github.com/space-wizards/space-station-14/pull/34270) Darkened Service job interface icons for better contrast
- [34407](https://github.com/space-wizards/space-station-14/pull/34407) Insuls Spawner
- [34378](https://github.com/space-wizards/space-station-14/pull/34378) Manual Valves Resprite
- [34409](https://github.com/space-wizards/space-station-14/pull/34409) Raise syndicate kobold reinforcement HP crit threshold from 75 to 100 to match monkey
- [34412](https://github.com/space-wizards/space-station-14/pull/34412) Porting Pride-O-Mat to Upstream
- [34431](https://github.com/space-wizards/space-station-14/pull/34431) craftable pet carrier
- [34439](https://github.com/space-wizards/space-station-14/pull/34439) Adds omnisexual pin
- [34048](https://github.com/space-wizards/space-station-14/pull/34048) Persist deadmin to database, add admin suspension system
- [33483](https://github.com/space-wizards/space-station-14/pull/33483) Add Discord webhook on watchlist connection
- [34396](https://github.com/space-wizards/space-station-14/pull/34396) Added missing details from worn capes to head of department beadsheets
- [34380](https://github.com/space-wizards/space-station-14/pull/34380) Replace ERT Medic's Advanced Medkits with 2 Combat Medkits
- [34358](https://github.com/space-wizards/space-station-14/pull/34358) Remove the ability to print the station anchor circuit board
    - It should be made not flatpackable instead. But we can keep it for this release.
    - Bug machine construction should probably be changed. Like making it multiple parts like the PKA.
- [34426](https://github.com/space-wizards/space-station-14/pull/34426) Make Mime PDA interactions silent
- [34420](https://github.com/space-wizards/space-station-14/pull/34420) Smite vending machine
- [34034](https://github.com/space-wizards/space-station-14/pull/34034) Printable bedsheets
- [34053](https://github.com/space-wizards/space-station-14/pull/34053) Remove christmas anomaly spawn
- [34443](https://github.com/space-wizards/space-station-14/pull/34443) Remove baby jail
- [34406](https://github.com/space-wizards/space-station-14/pull/34406) Add a CCVar to allow from hiding admins in the reported player count
    - WHAT HAPPENS IF THERES 2 ADMINS ON? -1 PLAYERS? MYRA IS CRYING
- [34424](https://github.com/space-wizards/space-station-14/pull/34424) New and Modified Map Spawners
- [34445](https://github.com/space-wizards/space-station-14/pull/34445) Space Ruins Variant
- [33991](https://github.com/space-wizards/space-station-14/pull/33991) Plasma Station
- [34265](https://github.com/space-wizards/space-station-14/pull/34265) Special reagents now appear in the guidebook
- [34251](https://github.com/space-wizards/space-station-14/pull/34251) Bended radiator

## Other notes:
Sloggers
![](https://cdn.discordapp.com/emojis/1328497168159608913.webp?size=128)