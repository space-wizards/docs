# Maintainer Meeting (8 November 2025)

```admonish info

**Attendees:**
- Slarti
- Errant
- Scar
- Myra
- ada
- Tiniest shark
- Keron
- Princess Cheezeballs

```

This meeting was recorded:

{% embed youtube id="6NM0iSeihbs" loading="lazy" %}

## Announce changes to the PR freeze/restriction list (Slarti)
We change it all the time, making it hard for contributors to keep track of, and we can't expect them to re-read the list every single time they make a PR.
So ideally we should make a short announcement somewhere everytime something changes. I would suggest
- to leave comment on the issue itself whenever someone adds or removes a freeze or restriction.
- and a discourse thread where we post the same comment maybe? That way it also gets mirrored to discord automatically.

Idea: We make a single thread we comment under every new freeze (or just use breaking changes). Otherwise I guess we can make a new catagory in development.

Myra approves this, waiting for the other lead maints.

## Silicon Workgroup doc (Scar)
The silicon workgroup finalized their design document.
The discussion is [here](https://forum.spacestation14.com/t/silicon-design-document/25120) and the PR can be found [here](https://github.com/space-wizards/docs/pull/544).
If no major issues are brought up we will probably call a vote by the end of the week.

## Stable review

```admonish info

Write your name here if you read this list fully.
**I checked this PR list:**
- Slarti
- Slam (will be absent from meeting)
- aada
- Princess
- Tiniest Shark
- Errant
- Myra
- Scar

```

- [#39212](https://github.com/space-wizards/space-station-14/pull/39212) Gas recycler tweaks
- [#40820](https://github.com/space-wizards/space-station-14/pull/40820) Space Carp are fireproof now
- [#39871](https://github.com/space-wizards/space-station-14/pull/39871) LaunchOnTriggerComponent
- [#35068](https://github.com/space-wizards/space-station-14/pull/35068) Internals: prioritize gas tanks over jetpacks 
- [#36292](https://github.com/space-wizards/space-station-14/pull/36292) Add Crazy Lube to the Toy Box.
- [#41068](https://github.com/space-wizards/space-station-14/pull/41068) Fixes .50 Uranium projectile sprite
- [#40472](https://github.com/space-wizards/space-station-14/pull/40472) Admin alerts now link players with tpto
- [#41148](https://github.com/space-wizards/space-station-14/commit/85f607f1e67e398df169e21f5b27a1ec4e1daabd) Make water cups spill when worn.
    - `Princess`: This one got 1984'd by github. Should we even have this in the list?
    - `Slarti`:The commit is still in the timeline, and the change is still merged of course. So I would keep it here and hopefully github unshadowbans them, so that it will show up again.
    - `Errant`:Freakin' github, man... I changed the link to point to the commit instead 
- [#39417](https://github.com/space-wizards/space-station-14/pull/39417) Update DamageableSystem to modern standards
- [#41144](https://github.com/space-wizards/space-station-14/pull/41144) More-generic bar flask name/description
    - `Tiniest Shark`: A Bar flask is a generic term for any sort of flask of this type. the description is a nod to that, this feels a bit unnecessary.
- [#40861](https://github.com/space-wizards/space-station-14/pull/40861) Implemented parenting and minimum default for loadout groups
- [#36251](https://github.com/space-wizards/space-station-14/pull/36251) Resprite and refactor wall dispensers (fuel, cleaner)
- [#41167](https://github.com/space-wizards/space-station-14/pull/41167) Rename kira special to the citrus bikeshed
- [#40570](https://github.com/space-wizards/space-station-14/pull/40570) Widen Ammo UI
  - `Slarti`: Nothing wrong with this PR, but in general the hand context UI needs a lot of love. The margins look off and many items have text simply clipping outside.
- [#40565](https://github.com/space-wizards/space-station-14/pull/40565) Department heads can now approve the use of their departmentally-restricted items
- [#41184](https://github.com/space-wizards/space-station-14/pull/41184) General touchups to antagonist flavor text
- [#41191](https://github.com/space-wizards/space-station-14/pull/41191) Readd CutWireVariationPass
- [#41165](https://github.com/space-wizards/space-station-14/pull/41165) Rejuvenating Resets Item Charges
- [#41029](https://github.com/space-wizards/space-station-14/pull/41029) Allow pacifists to use disabling modes of energy magnum and energy shotgun
- [#40991](https://github.com/space-wizards/space-station-14/pull/40991) Change the recipe for licoxide to not require lead
- [#41136](https://github.com/space-wizards/space-station-14/pull/41136) Add 2 New Reagents (Felinase and Caninase)
- [#40065](https://github.com/space-wizards/space-station-14/pull/40065) Add multi-job exclusion support to objectives, and add more appropriate job restrictions to certain thief objectives.
- [#40326](https://github.com/space-wizards/space-station-14/pull/40326) Migrate random shuttle events to load dynamically
    - `Princess`: So for some context, this was test merged to vulture to see the performance impact based on current shuttles. Entity spawning in amounts for the shuttles we have shouldn't cause any noticable lag and from testing and attempting to really make the server suffer this appears to be the case. It would be good to get some accurate benchmarks but from local and server testing, it seems preloading the shuttles was not worth the performance save. 
    - `Slarti`: The PR title is a little confusing as this does not migrate anything, it just completely disables preloading without any replacement and spawns the entire shuttle directly. Also I'm very sussed out by this, because irrc sloth said it was introduced for a reason. And Errant had been doing some testing for a game tutorial gamemode, where each player was spawned on a separate, very small map and that also caused lag for other clients, so I doubt that shuttles would be any different.
        - `Princess`: I looked at the PR and sloth mentioned that shuttles, specifically LoneOps would lag the server when spawned dynamically. I decided to run a test and spawn 5 at once on Vulture to give a worse than worst case scenario (I've spawned 7 shuttles at once before to try and lag the server) there was no pause, nothing on grafana tickrate didn't budge, nobody in the round noticed anything. This apparently used to lag the server for "several seconds" according to sloth's comment? I'm not sure what changed but there's literally nothing these days.
            - `Princess`: Preloaded shuttles PR [#24490](https://github.com/space-wizards/space-station-14/pull/24490)
        - `Errant`: That's not what I observerd, if I said that then I miscommunicated. I got lag when I loaded **Reach**. That is small *for a station*, but rather huge for a shuttle. I got absoultely no lag from loading my own test map, though it has less entities than a typical shuttle would. If admins tested loading actual shuttles on Vulture, their results should be taken as representative. Also, conveniently for us, the biggest shuttle (nukie ship) loads on roundstart, so even if that one lags the server for a moment, no one will pick up on it.
            - `Princess`: Spawning NukeOps, the whole gamemode, does lag vulture! Luckily it's not a midround spawn.
        - `Myra`: I guess we can just try it and see :tm: although I would really want to see lazy loading grids to become a thing somewhat soonish. But I do also understand thats a reletivly hard feature to code.
    - `Jean`: Just a reminder if we use this as justification to drop the freeze we should probably keep a disclaimer that shuttles are likely to be dropped wholesale in the case of breaking changes to how shuttles function. This was a devil's bargain we struck with adding them in the first place due to the maintenace burden of updating them. Rather than "promising" to fix them I think we'll have better results just letting people make new ones wholesale when updates require they be retired. Theyre a nice relatively easy to create and review entry into mapping so I think its healthier for them to have turnover anyway.
- [#41230](https://github.com/space-wizards/space-station-14/pull/41230) Add Reporter Beacon
- [#41232](https://github.com/space-wizards/space-station-14/pull/41232) Edible Chameleon Clothing
- [#39831](https://github.com/space-wizards/space-station-14/pull/39831) Assorted tweaks to towel trinkets
- [#38750](https://github.com/space-wizards/space-station-14/pull/38750) Borg module action QOL: put module name into tooltips
- [#41271](https://github.com/space-wizards/space-station-14/pull/41271) Add DNA injector
- [#41098](https://github.com/space-wizards/space-station-14/pull/41098) Voice Sensor Item
- [#41276](https://github.com/space-wizards/space-station-14/pull/41276) Make bleach a better space cleaner
  - `Slarti`: Ideally it would be a sidegrade instead of a direct upgrade. But maybe it's fine since it is harder to make?
    - `aada`: I think it's fine as an upgrade so long as it requires a chemist. Convincing someone to make poison for you is a reasonable barrier.
    - `Princess`: This is fine I think for now. Ideally for cleaning it should be a sidegrade but for that we'd need better cleaning mechanics/chem interactions so for now just making it a more efficient and illegal/dangerous space cleaner is good enough. 
