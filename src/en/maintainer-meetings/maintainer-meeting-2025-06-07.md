# Maintainer Meeting (7 June 2025)

:::info
**Attendees:**
- Simyon
- Errant
- EMO
- Scar
- Slam
- Fildrance
- Tiniest Shark (Audience)
- PJB (Audience)
- Roomba
- Notafet
- Slarti
- Chromiumboy
- Tayrthan
:::

This meeting was recorded:

{% embed youtube id="9YOPX4y3Rig" loading="lazy" %}

## Release Procedures Proposal (Errant)
- Please read [the proposal](https://forum.spacestation14.com/t/maintainer-policy-change-release-procedure/20963) in advance and vote 
- Should the Release thread stay on Discord or move to the forum? Strong opinions in favor of both, so far
    - Discourse push notifications *can* allow fast communications
    - One Forum Channel for release could work
    
## What's up with all the rotatin'? (Slam)
- There's this very noticeable bug going on where items spawned from spawners are rotated, but all in the same direction.
- Further investigation seems to indicate they all spawn near (0.01~ precision) zero degrees world rotation.
- Decal Spawner PR in this Stable Merge seems to suffer from the same issue.
- EntityTable update caused this

## New Maptainer Spanky (Slam)
- Welcome! 
- the group meowing sessions start at 4pm GMT every day, be there or demotion

## Dissaproval Label Vibe Check
- its based

## New PR discussion system
- "i do like it"
- gives more formality 
- much more on topic
- "aysnc communication is better"
- ask again next meeting

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- ScarKy0
- Myra
- Fildrance
- EmoGarbage
- Beck
- Roomba
- Errant
- Simyon, your favorite Lead Maintainer (first time ever checking stable review
- Slam
- Tiniest Shark
:::

- [37564](https://github.com/space-wizards/space-station-14/pull/37564) Buff gas canister volumes moderately
- [37747](https://github.com/space-wizards/space-station-14/pull/37747) Liquid soap is now slippery
- [37765](https://github.com/space-wizards/space-station-14/pull/37765) Added a new detective's office sign
- [37771](https://github.com/space-wizards/space-station-14/pull/37771) Inhands for bartender tools and mugs.
- [37542](https://github.com/space-wizards/space-station-14/pull/37542) Add Code of Conduct
    - Is there any feedback so far? Has anyone who got tempblocked on Github complained/appealed? (Slam)
    - 5 people bonked so far 
    - no complaints
- [33840](https://github.com/space-wizards/space-station-14/pull/33840) Add basic discord client integration with ooc and admin chat support
    - Another reminder for the above topic (IK this is not what this is for, but I need to be sure this WILL happen otherwise discord OOC breaks.) (Myra)
- [37807](https://github.com/space-wizards/space-station-14/pull/37807) Add welded visuals to shutters and blast doors
- [34138](https://github.com/space-wizards/space-station-14/pull/34138) Make foods reflect their ingredients better
- [37789](https://github.com/space-wizards/space-station-14/pull/37789) kangaroos can now be equipped with north stars and knuckle dusters.
    - A monkey can already robust someone with just a crowbar, I'm a bit worried a kangaroo with a proper weapon will be even bigger of an issue. Though we have only Willow and thats mainly a skill issue ngl (Scar)
    - Scar is right but also it is very funny (Slam)
    - keep it for now
    - it is very funny
- [37800](https://github.com/space-wizards/space-station-14/pull/37800) Dirty Steel Tile now has Variants
- [37756](https://github.com/space-wizards/space-station-14/pull/37756) Bar sign AlignTile version and fixtures for bar signs
    - **BLOCK**: I think this should be reverted, it sets a bad precedent. These are identical entities, except one is offset. There should just be a way to change the alignment of the bar sign via some action. (Wrenching? Since wallmounted stuff can't be unanchored anyway) Then in the future this solution could also be used for any other wallmounted entities, such as the television. `Errant`
    - keep only the aligned version, remove the other one (breaking change for downstreams)
        - VOTE!!
        - Revert (Keep Aligned Version (With migrations), remove other version as solution)
        - Keep
- [37790](https://github.com/space-wizards/space-station-14/pull/37790) Updated Drozd and Lecter with magazine states and small animations.
- [30600](https://github.com/space-wizards/space-station-14/pull/30600) Spray nozzle can suck puddles into tank directly!
- [37778](https://github.com/space-wizards/space-station-14/pull/37778) Add WieldingBlockerComponent
- [37822](https://github.com/space-wizards/space-station-14/pull/37822) Lets angry AI gorillas pry open doors, smash things, and vault tables
- [37742](https://github.com/space-wizards/space-station-14/pull/37742) Add Fancy Speech Bubbles for Diona and Gingerbread
- [37728](https://github.com/space-wizards/space-station-14/pull/37728) Kill the TEG meta with really big hammers
- [37658](https://github.com/space-wizards/space-station-14/pull/37658) Significantly improve TEG power generation stability
- [35235](https://github.com/space-wizards/space-station-14/pull/35235) Sentry turrets - Part 6: Sentry turret control panels
- [37846](https://github.com/space-wizards/space-station-14/pull/37846) Updated weld overlay for blast door
- [37745](https://github.com/space-wizards/space-station-14/pull/37745) Add overkill thresholds to more objects
- [37725](https://github.com/space-wizards/space-station-14/pull/37725) Remove capacitors and matter bins
- [37834](https://github.com/space-wizards/space-station-14/pull/37834) Give cluwnes job icons
    - How does this effect borg laws?
    - "Unless a law redefines the definition of crew, then anyone who the HUD indicates to you has a job, including passengers, is a crewmember."
    - https://wiki.spacestation14.com/wiki/Silicon_Rules
    - Seems ok because it isn't a "job" - kind of like the zombie icon?
    - `Roomba` Players are already very confused on what is and isn't crew already. Cluwnes are supposed to be allowed to be hurt/gibbed so this is working backwards from what we want it to be and creates an inconsistency.
    - Falls under non-crew. That being said, there's the one PR [37038](https://github.com/space-wizards/space-station-14/pull/37038) that can alleviate it. (Slam)
        - is fine to merge
- [37866](https://github.com/space-wizards/space-station-14/pull/37866) reduced the number of slots in bookshelves
- [37870](https://github.com/space-wizards/space-station-14/pull/37870) Resprites hatch and hatch_maint
- [37819](https://github.com/space-wizards/space-station-14/pull/37819) inhands for CAKE + sprite fixes
- [37066](https://github.com/space-wizards/space-station-14/pull/37066) Decal Spawners
- [37806](https://github.com/space-wizards/space-station-14/pull/37806) Large Tail Wag
- [34465](https://github.com/space-wizards/space-station-14/pull/34465) Change explosive triggers to be more consistent
- [37895](https://github.com/space-wizards/space-station-14/pull/37895) Grape juice cup now has grape juice
- [37869](https://github.com/space-wizards/space-station-14/pull/37869) high-vis vest is now dimmer
- [30924](https://github.com/space-wizards/space-station-14/pull/30924) Chameleon clothes + EMP behaviour
    - having it changed on server with ```component.NextEmpChange = _timing.CurTime + TimeSpan.FromSeconds(1f / component.EmpChangeIntensity);``` is a tiny bit scary, maybe slow down or make it Math.Min()? yes, it calls dirty. (Fildrance)
    - just limit it to avoid seizures
    - not a blocker, make a P2+ issue (or ping author)
- [37787](https://github.com/space-wizards/space-station-14/pull/37787) New sprites for Coal and Gold ore crabs, new Bananium ore crab and Bananium rock anomaly.
- [37710](https://github.com/space-wizards/space-station-14/pull/37710) Add Practice Magazines to the Secfab
- [33887](https://github.com/space-wizards/space-station-14/pull/33887) Chameleon controller implant (Clothing fast switch)
- [34321](https://github.com/space-wizards/space-station-14/pull/34321) Add filters to cutter machine
- [34907](https://github.com/space-wizards/space-station-14/pull/34907) Select Fire Rifles
- [34371](https://github.com/space-wizards/space-station-14/pull/34371) Absinthe makes you mildly hallucinate
- [34906](https://github.com/space-wizards/space-station-14/pull/34906) Faster Drozd burst
- [33630](https://github.com/space-wizards/space-station-14/pull/33630) Improved French accent (th sound)
- [37957](https://github.com/space-wizards/space-station-14/pull/37957) Show TEG theoretical supply on inspect
- [37909](https://github.com/space-wizards/space-station-14/pull/37909) give characters wearing clown masks hair again
- [37901](https://github.com/space-wizards/space-station-14/pull/37901) Resprites black, brown, fancy, white cowboy boots
- [37945](https://github.com/space-wizards/space-station-14/pull/37945) Remove keep alive objective.
- [37899](https://github.com/space-wizards/space-station-14/pull/37899) Mirror resprite
- [37986](https://github.com/space-wizards/space-station-14/pull/37986) Further Mail Balancing
- [37989](https://github.com/space-wizards/space-station-14/pull/37989) Adding a new trait: Monochromacy!
    - ideaguys but we could probably add colorblindness traits too at this point, would need to be in a new category in traits though (Scar)
- [38000](https://github.com/space-wizards/space-station-14/pull/38000) Added bulk cleanades crate
- [38004](https://github.com/space-wizards/space-station-14/pull/38004) Made C-4 Major contraband instead of syndicate contraband
    - I don't think this is a good one. C-4 is only possible to acquire as an antagonist (Traitor/Nukie/Thief), and the claim that it has other uses doesn't ring true to me. If this is found on someone's person, they have *professional* explosive equipment. (Slam)
    - There is an argument that Security could utilize C-4 for some sort of breach into AI/department, but that feels extremely situational, probably needlessly destructive, and push comes to shove there's researchable explosive charges/Warden's breaching charge. (Slam)
    - **BLOCKER: REVERT**
- [36124](https://github.com/space-wizards/space-station-14/pull/36124) Layering for atmospheric pipes
- [38010](https://github.com/space-wizards/space-station-14/pull/38010) Air Grenade Cargo Order
- [37998](https://github.com/space-wizards/space-station-14/pull/37998) Lube Evaporates Slowly
- [36073](https://github.com/space-wizards/space-station-14/pull/36073) Use distinct action labels for toggling internals on and off.
- [35969](https://github.com/space-wizards/space-station-14/pull/35969) Add multipart machines
- [37996](https://github.com/space-wizards/space-station-14/pull/37996) improve noir glasses shader
- [37246](https://github.com/space-wizards/space-station-14/pull/37246) Add checks for various complex interactions
- [38038](https://github.com/space-wizards/space-station-14/pull/38038) Fix directional window inconsistencies
- [38006](https://github.com/space-wizards/space-station-14/pull/38006) Cargo food crate adjustments
    - `Roomba` Lukewarm reminder to myself that cargo arbritarge will heisentest if the crate has a percent chance to have an item. Ex. a crate could bring something like a cheeseburger that makes it cost 50 dollars more at a 10% chance, which will fail tests at a 10% chance.
    - We need some system to knock of all of the chance in entity tables
- [37979](https://github.com/space-wizards/space-station-14/pull/37979) Cryo sleep units no longer collide with mobs
- [38040](https://github.com/space-wizards/space-station-14/pull/38040) Increase uranium window health
- [37805](https://github.com/space-wizards/space-station-14/pull/37805) Stylized the nanotask printouts to be *pretty*
    - dont like pink check mark, looks off. but love moomoo. maybe its my problem (Fildrance)
    - salvagers use it for infinite movement (print and throw) (also pkas)
    - "Should have like 5 papers and then you feed it new ones tbh" ~slam
- [37362](https://github.com/space-wizards/space-station-14/pull/37362) Change "Terrorism" to "Station-Wide Destruction" in Space Law
    - Make sure someone updates the wiki since ik admiral was talking about not having access (EMO)
        - go ask pjb or crazybrain
        - or myra apperantly
        - crazy is doing it
    - This was merged to stable; wiki should be updated ASAP (Slam)
- [31442](https://github.com/space-wizards/space-station-14/pull/31442) Add text highlighting
- [32782](https://github.com/space-wizards/space-station-14/pull/32782) Add Diona rooting

- [27422](https://github.com/space-wizards/space-station-14/pull/27422) action refactor proper ecs edition
    - `Roomba` Any issues present that haven't been squished yet?
- [38048](https://github.com/space-wizards/space-station-14/pull/38048) Remove Lube From Trash Puddle Spawns
- [38075](https://github.com/space-wizards/space-station-14/pull/38075) Evac Repair Lockers
- [37727](https://github.com/space-wizards/space-station-14/pull/37727) Fixed Holoclown injector not breaking on drop


Weeks without non-squashed merges: 0 :cry: 
I am allowing you to publically shame anyone who is not squash merging (No /s here: DO at least tell the maintainer who didn't squash merge otherwise they will never know. Privately or staff chat idc just alert them.)
    - We have also updated the docs because it turns out squashing wasn't even written down anywhere :godo:
