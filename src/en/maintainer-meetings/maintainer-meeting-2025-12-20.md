# Maintainer Meeting (20 December 2025)

```admonish info
**Attendees:**
- Simyon
- Princess_Chzblz
- ScarKy0
- notafet
- ArtisticRoomba
- Julian
- Errant
- Fildrance
```

This meeting was recorded:

{% embed youtube id="meow meow :3" loading="lazy" %}

## Visitor Shuttles (Princess)
Are there any shuttle maps we want to keep as we remove visitor shuttles from the game?

- The one shuttle with a reactor that explodes after some time as a sort of escape room?
- go ask admins

`Roomba`: Rip and tear until it is done.

## YAML Gas Reactions Testing (ArtisticRoomba)
The Engineering/Atmospherics Workgroup would like to test YAML gas reactions on Vulture by switching it to a test branch. We've agreed on this before but I'd like to just formalize/remind people about it.

- this so peak
- requires an announcement on the forums for vulpture test
- 3-5 days (might be shorter)

## Change release procedure back to all master (we started talking about this during the meeting)

- Having a stable branch has good value
    - Running servers with stable branch is also good
- Don't remove stable branch no matter what even if no servers are running it
- go go gadget bug reports
- using a different server serves no use as pop will just migrate
- right now not many players on vulture that fully report issues
- possible thing during / before meeting: staff joins vulture and go plays
- if we were to make all servers master, reverting that when feedback popups are in might be an idea. [41352](https://github.com/space-wizards/space-station-14/pull/41352)

**Revisit this idea next meeting**

## Stable review

```admonish info
Write your name here if you read this list fully.
**I checked this PR list:**
- Princess
- Beck
- iaada
- Slarti
- Tiniest Shark
- Simyon
```

- [41783](https://github.com/space-wizards/space-station-14/pull/41783) Soap, Banana peel, and Slip entity tables
- [41840](https://github.com/space-wizards/space-station-14/pull/41840) Toys entity tables
- [41566](https://github.com/space-wizards/space-station-14/pull/41566) Decouple standing state and drop item behavior
- [41693](https://github.com/space-wizards/space-station-14/pull/41693) Change Ephedrine, Desoxyephedrine and Hyperzine properties
- [41685](https://github.com/space-wizards/space-station-14/pull/41685) Warfarin and Hemorrhinol, Hemophilia turned into a StatusEffect
- [41723](https://github.com/space-wizards/space-station-14/pull/41723) New figurine voicelines
- [41716](https://github.com/space-wizards/space-station-14/pull/41716) Replace Vestine-derivatives in plant mutations, change uplink prices & hypopen to reflect changes
- [41731](https://github.com/space-wizards/space-station-14/pull/41731) Vestine now Mutates Plants to Produce Vestine
  - `Slarti`: I'm ok with trying this out, but I think this will lead to massive amounts of traitor chems being produced. The problem is that once you have the mutation you can duplicate it infinitely. With this much lead you will be able to kill the entire station.
      - `Princess`: I did a lot of testing with it to get the numbers right, you need a pretty massive plant setup with a ton of potency to get any of the chemicals in numbers even close to what botany was getting before. 
    - Not an issue. Just requires some testing.
- [41743](https://github.com/space-wizards/space-station-14/pull/41743) Remove explosive component from mothership cpre
- [37551](https://github.com/space-wizards/space-station-14/pull/37551) Adds the sticky grappling hand
    - `Errant`: How is this acquired/where does it come from? Do we typically add changelog for admeme-only items?
    - it comes in foolbox
    - Grappling hook has severe code issues
    - this is like so peak actually
- [41551](https://github.com/space-wizards/space-station-14/pull/41551) Add voice mask implant
  - `Slarti`: I'm not really sold on this one because it seems like a direct upgrade to the voice mask just without the risk of getting caught. Not everything should come as an implant. And it somewhat overlaps with the changeling.
      - `Princess`: This is intended to replace the current voice mask since the current voice mask was really easy to defuse. On Vulture I've seen it work to great effect where a Traitor using it can pass the "Remove your mask" check. It's also definitely not with no risk since in the cases I saw, the Traitor got caught in a lie, got searched, and their disguise fell apart. 
  - Fine rn
- [41741](https://github.com/space-wizards/space-station-14/pull/41741) Remove Zookeeper and Boxer jobs
    - `Princess`: The visitor ghost role versions still exist but lack their localization files meaning they show up as "job-name-zookeeper"
    - Remove visitor ghostroles, bottom text
    - As a fix remove the zookeeper and boxer ghost role versions
- [41755](https://github.com/space-wizards/space-station-14/pull/41755) Fixed hyperzine (micro)injector descriptions
- [38654](https://github.com/space-wizards/space-station-14/pull/38654) Snap Booms (fake snap pops)
- [41739](https://github.com/space-wizards/space-station-14/pull/41739) Add GenPop Enter/Leave to ID Card Computer. Add shuffle the accesses a bit.
- [34971](https://github.com/space-wizards/space-station-14/pull/34971) Double bullet speeds
- [41580](https://github.com/space-wizards/space-station-14/pull/41580) Make xenoborg light brighter
- [41763](https://github.com/space-wizards/space-station-14/pull/41763) Hitscans now have names
- [41765](https://github.com/space-wizards/space-station-14/pull/41765) Reverts Mop + Glowstick Storage Rotation
- [41764](https://github.com/space-wizards/space-station-14/pull/41764) Misc Proper Rotation Sprites
- [41678](https://github.com/space-wizards/space-station-14/pull/41678) Allow removing species from the RNG pool of a new player's initial auto-generated character
- [41789](https://github.com/space-wizards/space-station-14/pull/41789) Reapply "Trip APCs when they exceed a power limit (#41377)"
    - `Princess`: Did we merge all the fixes for this yet? If not we should revert or get those merged. 
        - Yes. Probably. 
- [41732](https://github.com/space-wizards/space-station-14/pull/41732) Clothing equipping doAfter tweak
- [41794](https://github.com/space-wizards/space-station-14/pull/41794) Bagel Theater will randomly spawn in partially broken
- [41512](https://github.com/space-wizards/space-station-14/pull/41512) Hushpup Shotgun
    - `Orks`: I'm ok with guns being this cheap but this is very powerful compared to every other uplink gun. I personally would rather rebalance all of them instead of adding new ones
        - `Princess`: I planned to do a pass over guns after this was merged and when the Traitor workgroup was up and running, but we're still waiting on that discord channel. 
    - it'll be handled by the traitor workgroup :)
- [41737](https://github.com/space-wizards/space-station-14/pull/41737) Add paper labels to gas canisters
- [41138](https://github.com/space-wizards/space-station-14/pull/41138) Make door bolting powergaming no longer relevant anymore
    - `Simon`: Title does not actually indicate what the PR changes, please keep a lookout in the future for PR titles to be accurate. :slugnod:
- [41814](https://github.com/space-wizards/space-station-14/pull/41814) Chefs start with chef shoes
- [41809](https://github.com/space-wizards/space-station-14/pull/41809) Change that specifies escape via the escape shuttle rather than pods in escape objectives
- [41830](https://github.com/space-wizards/space-station-14/pull/41830) Smart Fridges can contain anything edible
- [41642](https://github.com/space-wizards/space-station-14/pull/41642) diona are now less debilitated by rooting in blood
- [41832](https://github.com/space-wizards/space-station-14/pull/41832) Re-sprite the Ripley
- [41808](https://github.com/space-wizards/space-station-14/pull/41808) ScramOnTrigger teleportation logic rewrite
- [41576](https://github.com/space-wizards/space-station-14/pull/41576) Add KI pills to the radsuit locker
- [40330](https://github.com/space-wizards/space-station-14/pull/40330) Hand labeler can always remove labels
- [41844](https://github.com/space-wizards/space-station-14/pull/41844) Don't remove borg access without power
- [41845](https://github.com/space-wizards/space-station-14/pull/41845) Killsign cleanup
- [36786](https://github.com/space-wizards/space-station-14/pull/36786) Edible Produce are now also Butcherable
- [41627](https://github.com/space-wizards/space-station-14/pull/41627) Adding a random gate
- [41757](https://github.com/space-wizards/space-station-14/pull/41757) Skeletons are now affected by Holy damage
    - `Errant`: As someone brought up on the PR, it's mildly concerning that this will make it confusing that zombies don't take holy damage
        - `Princess`: Skeleton needs a nerf and I don't think this is the way to do it. They need to take more blunt damage and pierce for one. 
        - `Shark`: I think more blunt damage would be the way to go. Maybe less pierce since there's not much to hit. This PR also just feels like it's trying a bit too hard to make Holy useful in a niche scenario.
    - big nothing burger of a pr basically
        - holy damage is like pretty much never used
        - no one in their right mind pulls out a bible to deal with a skeleton (i used the shotgun, you know why? The shotgun don't miss.)
        - just make them more vurnerable to pierce (remove the modifier)
        - give them real blunt vurnerability
- [41791](https://github.com/space-wizards/space-station-14/pull/41791) Make gun chamber empty by default
- [41705](https://github.com/space-wizards/space-station-14/pull/41705) Update to Bardrobe to add Pun Pun's outfit
- [41823](https://github.com/space-wizards/space-station-14/pull/41823) Remove roundstart tools from some cyborgs
~~- [41860](https://github.com/space-wizards/space-station-14/pull/41860) Remove most unknown shuttle events~~
~~- [41862](https://github.com/space-wizards/space-station-14/pull/41862) Revert "Remove most unknown shuttle events"~~
    - `Errant`: I think these two actually add to a zero sum? So nothing happened 
- [37855](https://github.com/space-wizards/space-station-14/pull/37855) ERT Overhaul 1/3: Apparel
- [38105](https://github.com/space-wizards/space-station-14/pull/38105) ERT Overhaul 2/3: Equipment
- [41863](https://github.com/space-wizards/space-station-14/pull/41863) Prevent Initial Infected from rolling on evac
- [41262](https://github.com/space-wizards/space-station-14/pull/41262) Ignite atmosphere on explosions
- [41696](https://github.com/space-wizards/space-station-14/pull/41696) Cryogenics evenheal + New chem "Arcyrox"
- [41546](https://github.com/space-wizards/space-station-14/pull/41546) Xenoborg door control module
- [41610](https://github.com/space-wizards/space-station-14/pull/41610) Add audio collections for Weh, Hew, and Honk to Vulps (so that they have audio when they do that)
- [41663](https://github.com/space-wizards/space-station-14/pull/41663) Station AI now rolls before most standard crew
    - `Princess`: Since antags don't roll with job priority, this will add issues for any downstreams using malf AI. We should fix that asap. 
        - Make a breaking changes post
- [41473](https://github.com/space-wizards/space-station-14/pull/41473) Add foolbox
- [35866](https://github.com/space-wizards/space-station-14/pull/35866) Tweak Killer Tomato Size
- [35071](https://github.com/space-wizards/space-station-14/pull/35071) Metabolizing bloodstream
    - `Princess`: Need a hotfix merged for this still: [41906](https://github.com/space-wizards/space-station-14/pull/41906)
    - `Slarti`: Small reminder to not merge PRs that touch sensitive core features directly before the staging cutoff. Better wait until after the cutoff so that we have two full weeks on vulture to catch any problems.
        - keep an eye out in the future :tm:
- [38537](https://github.com/space-wizards/space-station-14/pull/38537) Adds BallisticAmmoSelfRefillerComponent
- [41893](https://github.com/space-wizards/space-station-14/pull/41893) Give Vulps "Unique" Stomachs
- [41896](https://github.com/space-wizards/space-station-14/pull/41896) Mirror contrib guidelines to GitHub
- [41900](https://github.com/space-wizards/space-station-14/pull/41900) Adds debug wizard's grimoire
- [41902](https://github.com/space-wizards/space-station-14/pull/41902) Make StaminaModifier into a status effect, apply to Hyperzine
