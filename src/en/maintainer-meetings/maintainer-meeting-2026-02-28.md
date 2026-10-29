# Maintainer Meeting (2026-02-28)

:::info
**Attendees:**
- Julian
- Slam
- Errant
- Scar
- TinyShark
- Orks
- Slartibartfast
- Keron
- Zoldorf
- Ress (not a maintainer but they get to be here anyways :) )
:::

This meeting was recorded: 2026-02-28

## **THIS MEETING IS BEING RECORDED AND WILL BE PUT ON YOUTUBE!**

{% embed youtube id="meow meow :3" loading="lazy" %}

## What I learned in Gibbing School is... (Jean)
- This is just a ~~reminder~~ tribute.
- https://forum.spacestation14.com/t/gibbing-removal-feedback/26320
- (discuss findings from gibbing and ashing test removal)

## 42819 encourages using titles in names (Jean)
- https://github.com/space-wizards/space-station-14/pull/42819 encourages breaking Rule 1.13 and needs a rule change (or a more technical solution like titles in IDs or loadout dropdown to avoid title slippery slope of
Mr. Dr. Sgt. John Grayman IIVVLXM Esquire Ph.D).
> Rule 1.13 Use realistic character names, and do not use names of famous people
> ...
> No titles/honorifics
> ...
> Clowns and mimes are exempt from the prohibition on titles/honorifics, and have loosened restrictions on low effort and implausible names.

- `Scar`: I think it's worth bringing it up to the headmins to change "Clowns and mimes" to "Jobs with stagenames". Cause musicians have the same thing for a very long time now.
- - `Ress`: This is being voted for for change within the admin team.
- `Slarti`: Small side note: Can we make the `Of Admin interest` label make the PR link get relayed to #ga-general or a separate channel? That way we won't have any more cases where we forget to inform the admins about such changes.


## The future of Salvage (Slam)

Slam bringing an update on BreakSalv and informing Contributors what to be expected in the future for Salvage (as our messaging has been a bit opaque on that).

## The Docs Repo (Princess)
- There's been some internal discussion on the docs repo and fixing it up and it would be good to be on the same page about that.
- Janet has asked for permission to completely overhaul the docs repo and its formatting, this would probably result in all open docs PRs being merge conflicted into oblivion
- In addition we need foundational docs not just for staff organization but also for content organization
    - We also need docutainer policy (real) which should be discussed sooner rather than later so we can accelerate the above.
- We should be addressing the elephant in the room weekly until it's in a comfortable spot.
    - I propose having at least *small* docs meeting post-stable review until we've gone through the docs repo backlog and addressed the above points.

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- ScarKy0
- Slam
- Jean
- Slarti
- aada
- Princess
- Errant
- Tiniest Shark
:::

- [42705](https://github.com/space-wizards/space-station-14/pull/42705) - Remove InternalsComponent from BaseSimpleMob
- [37949](https://github.com/space-wizards/space-station-14/pull/37949) - Ghost types
- [42706](https://github.com/space-wizards/space-station-14/pull/42706) - Remove writing apps from the Mime PDA
- [41920](https://github.com/space-wizards/space-station-14/pull/41920) - Entity Table Probabilities API
- [41108](https://github.com/space-wizards/space-station-14/pull/41108) - Sent fax now tells where it was sent from
- [42668](https://github.com/space-wizards/space-station-14/pull/42668) - Atmos GetAirflowDirections API
- [42619](https://github.com/space-wizards/space-station-14/pull/42619) - Gas device power switches use switch buttons
- [42729](https://github.com/space-wizards/space-station-14/pull/42729) - Give HoP genpop enter and leave access
    - `Slarti`: The PR itself is probably fine, but we had a few others like this one and we should finally fix the ID card console bug that prevents you from modifying IDs if you are missing any access category on it (rather than just blocking only those categories). Irrc there is an ancient PR, but it has been awaiting changes for ages.
- [37833](https://github.com/space-wizards/space-station-14/pull/37833) - Prevent anomalies from spawning multiple entities on the same tile when instructed not to.
- [42758](https://github.com/space-wizards/space-station-14/pull/42758) - Make Ichor work in the bloodstream 
- [42764](https://github.com/space-wizards/space-station-14/pull/42764) - Syndimov Kit
- [42787](https://github.com/space-wizards/space-station-14/pull/42787) - Remove Uranium from Mute Toxin recipe
- ~~[42789](https://github.com/space-wizards/space-station-14/pull/42789) - Add feedback popup for gibbing/ashing removal~~
    - `Princess`: This was reverted with the reverting of gibbing removal, not sure why it's on the list...
        - `Errant`: An oversight. You can just remove or mark such entries in the future if you are sure
- [42569](https://github.com/space-wizards/space-station-14/pull/42569) - Added Insulated Components to RK and Servants.
- [42613](https://github.com/space-wizards/space-station-14/pull/42613) - Optical thermal scanner implementation
- [42813](https://github.com/space-wizards/space-station-14/pull/42813) - Add opticial thermal scanners to engivend
- [42819](https://github.com/space-wizards/space-station-14/pull/42819) - Chaplains can now choose a custom name
    - Admin concerns, see Topics
- [39591](https://github.com/space-wizards/space-station-14/pull/39591) - scale ammonia and nitrous oxide damage with gas quantity
- [39513](https://github.com/space-wizards/space-station-14/pull/39513) - Emitters now give alerts if interfered with.
  - `Slarti`: The code needs some cleanup, I made an [issue](https://github.com/space-wizards/space-station-14/issues/43053)
- [42101](https://github.com/space-wizards/space-station-14/pull/42101) - Make nukie infiltrator shuttle pinpointer universal
- [42829](https://github.com/space-wizards/space-station-14/pull/42829) - Make conveyors stack items that stop
- [42820](https://github.com/space-wizards/space-station-14/pull/42820) - Solved #42803 - Syndie contra explicitly has no allowed departments or jobs
- [42837](https://github.com/space-wizards/space-station-14/pull/42837) - Empty Crayon Box
- [40925](https://github.com/space-wizards/space-station-14/pull/40925) - Animated Vox Tails
- [42838](https://github.com/space-wizards/space-station-14/pull/42838) - Fix-sprites-practice-disabler
- [42847](https://github.com/space-wizards/space-station-14/pull/42847) - Change warfarin to heparin
- [42740](https://github.com/space-wizards/space-station-14/pull/42740) - Fix RCD not being able to place hull tiles in space
- [38991](https://github.com/space-wizards/space-station-14/pull/38991) - New high pop station - Serpentcrest
- [42791](https://github.com/space-wizards/space-station-14/pull/42791) - Minor tweaks to Urist names
  - `Errant`: Look how they massacred my boi... Would anyone support switching "Uristititi" back? My original thought process there was that everyone would be searching for "Urist", thus any letter after that can be considered a harmless whimsy
      - `Scar`: For the sake of simplicity keeping "Urist" everywhere should be better. But also if you just search for "Urist" then "Uristititi" shows up too. I think it's a bit too minor to care about it right now.
      - `Shark`: I don't think simplicity should always be the highest priority, especially when the flavour wasn't added back in anywhere else.
- [42768](https://github.com/space-wizards/space-station-14/pull/42768) - Vulpkanin Yawns
- [37832](https://github.com/space-wizards/space-station-14/pull/37832) - Slat tiles and decals
- [42876](https://github.com/space-wizards/space-station-14/pull/42876) - Fix gas filter always outputting 20C filtered gas
- [42878](https://github.com/space-wizards/space-station-14/pull/42878) - Regular bots are now repaired gradually, just like borgs
- [42843](https://github.com/space-wizards/space-station-14/pull/42843) - Vulp Tail Wags + Tail Fixes
- [41479](https://github.com/space-wizards/space-station-14/pull/41479) - (Re)Add sneezing emote.
- [42772](https://github.com/space-wizards/space-station-14/pull/42772) - Identity Mask now updates equipped Agent ID name
- [42722](https://github.com/space-wizards/space-station-14/pull/42722) - Vulpkanin Sulfur Blood + Organs
  - `Slarti`: I'm not a fan of this one. It feels like we are just giving them special blood because multiple other species have it, making them in turn less unique. Also sulfur blood does not fit thematically at all for an animal-based species that breathes oxygen, it would be more much fitting for a rock-based one. (Sorry, Scar)
  - `Scar`: Ultimately it's harmless and got approval from the med workgroup. Sulfur blood can also be used as an explaination for why they have different heating properties.
  - **HOLD VOTE**
- [42926](https://github.com/space-wizards/space-station-14/pull/42926) - AI can now read papers and envelopes
- [42927](https://github.com/space-wizards/space-station-14/pull/42927) - Change basic viper magazine to high capacity in operative bundle
- [42912](https://github.com/space-wizards/space-station-14/pull/42912) - New moth emote. Flaps wings!
  - `Slarti`: Do we still have the bug that the emote wheel completely scrambles the emote positions every time a new prototype is added? If so we should probably not add any new emotes until that is merged because it breaks muscle memory every time
  - Probably note fixed. Set a freeze until the bug is fixed?
- [42950](https://github.com/space-wizards/space-station-14/pull/42950) - Added Emp interaction with Bar Sign
- [42929](https://github.com/space-wizards/space-station-14/pull/42929) - Vox, Diona and Vulp Unique Sneezes
- [42969](https://github.com/space-wizards/space-station-14/pull/42969) - Fixed Det coat armor status
  - `Errant`: Isn't this kinda the same situation we had [with the berets](https://github.com/space-wizards/space-station-14/pull/33815), where we have decided not to give armor to cosmetic items so "armoring up" is an intentional choice that is also visually telegraphed? Granted, it is not exactly the same situation, since it's the armor slot not the head slot, so the "that extra armor does not make all that much of a difference anyway" part does not apply
      - `Slam`: The difference here is that the helmet armor is very minor (10%) while the body armor of a vest provides a more meaningful value (30%). Considering a lot of the Detective's identity is emulating a stereotypical noir detective, I think it is fine that we make a concession here. 
          - `Errant`: Okay but in the same breath, why is the noir detective bulletproof, he is supposed to be a detective not a riot cop. If he is ambushed, that almost feels fair, and if he expects trouble, why is he going there/why is he wearing his casual coat...
          - `Slam`: It's just a padded coat. The Detective role is just as vulnerable to being jumped as a normal SecOff; inviting that more by giving less resistances would just encourage Detectives to put on the regular armor vests Sec has access to. Unlike the helmet, the body armor is not a trivial amount.
- [42930](https://github.com/space-wizards/space-station-14/pull/42930) - update basic operative bundle contents
- [42984](https://github.com/space-wizards/space-station-14/pull/42984) - More xenoborg names
- [42990](https://github.com/space-wizards/space-station-14/pull/42990) - Make prescription glasses actually work
- [42968](https://github.com/space-wizards/space-station-14/pull/42968) - Improved camera static shader randomness
- [41079](https://github.com/space-wizards/space-station-14/pull/41079) - Add unlockable reporter cosmetics
- [42994](https://github.com/space-wizards/space-station-14/pull/42994) - Remake the "Vegan Meatball" salvage wreck
- [42998](https://github.com/space-wizards/space-station-14/pull/42998) - EMP implant uplink texture (Addresses #42008)
- [42983](https://github.com/space-wizards/space-station-14/pull/42983) - Non-obsoletion warnings as errors in Release.
  - `Slarti`: I merged this one, but I'm reconsidering if this is a good idea because Tay had to revert a new [engine analyzer](https://github.com/space-wizards/RobustToolbox/pull/6430) because the game will no longer build until the warnings are all cleaned up. And this might cause some problems for forks - each time we add a new analyzer they will have to immediately fix all the warnings (or disable this PR).
  - `Scar`: Is there some way we can selectively choose to ignore this when working on PRs? I agree this is very handy for preventing warnings, but at the same time the listed issue is pretty major.
- [42915](https://github.com/space-wizards/space-station-14/pull/42915) - Lizard rehappy alternative
- [42696](https://github.com/space-wizards/space-station-14/pull/42696) - Largely Revert Unique Corgi Hardsuit and Equipment Sprites
- [41812](https://github.com/space-wizards/space-station-14/pull/41812) - Give borgs default prying
  - `Errant`: Will it be obvious to a new player HOW to do it, without the tooltip saying? Since the interaction is different than with a normal crowbar. We might want to specify.
  - `Scar`: There's a verb on airlocks that says "Pry". I don't think there's a nicer way to communicate this as we are right now. Text in the alert would just be ugly.
  - `Errant`: To clarify, there is *already* a mouseover tooltip on the alert. Which explains what it means. But does not say HOW. It's there on the tooltip that I would put this info 
  - **NOTE BEFORE STABLEMERGE**: Scar will make a staging PR that makes changes to the tooltip.
- [43030](https://github.com/space-wizards/space-station-14/pull/43030) - Partially revert "Remove bad accents"

## Niko is a cat
You mean nik?

## Go get [some food](https://en.wikipedia.org/wiki/Kapsalon)!