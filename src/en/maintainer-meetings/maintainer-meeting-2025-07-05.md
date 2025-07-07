# Maintainer Meeting (5 July 2025)

:::info
**Attendees:**
- Errant
- Simyon
- Scar
- Myra
- Slam
- Tiniest Shark
- Notafet
- Slarti
- Julian
- Fildrance
- Tayrtahn
:::

This meeting was recorded:

{% embed youtube id="X_nP8IBSP2M" loading="lazy" %}

## P0 Handling (EmoGarbage)
- We need to have an actual process for reverting PRs that cause P0 issues.
- Maints need to know what's happening
    - Maints weren't notified of rounds not starting on Vulture for like 3 hours
      - `Slarti`: let the admins know they are free to do a @maintainer ping in such cases
    - A fix didn't get published until 2 hours after that
    - We should have some kind of pipeline for this kind of thing. Ideally if we have rounds ending in 0 seconds we get a webhook message or something. At the very least ping maints in `#staff-sorority` or `#maintainers`. 
      - `Slarti`: Yeah, an automated warning sounds good.
- It's easiest to revert PRs directly after they're merged. We should probably be just reverting outright instead of doing bandaids. It's good just for sanity reasons to not be crunch pushing PRs last minute.
  - `Slarti`: Yeah, I don't see a problem with doing quick reverts if something is bugged, especially if we don't know how long a fix will take. A revert is a few mouse clicks, same for reverting a revert. I would like to keep the game playable, so if something major shows up on vulture a revert should be fine as long as it won't cause any conflicts with other PRs. So for people have been reluctant to revert something, but there is no reason not to make it a more common practice if it has a benefit for our players.
- `Slarti`: I would also like if we could ensure that major refactors are best merged directly after a release, so that we have more time to squash out any bugs that show up (in this case it was a honest mixup with the release schedule though). And for major refactors it would be good to time it so that either the reviewer or the author are available after the next vulture update hits, so that they can quickly fix things in case vulture has problems. It might make sense to publish testing after merging if that is better for your schedule.
    - `ROOMBA`: Tangent, is there any reason why we're waiting to do vulture updates every day/12h rather than have them update when a new PR is available (like old times godo)? The biome refactor unfortunately hit vulture at midnight/deadpop hours.
      - `Slarti`: We don't want to kick players off the server all the time. New merges come in maybe 10 times a day.
      - `ROOMBA`: I guess, though server restarts are pretty quick and in this case would affect one server (instead of the entire cluster like it did previously).

## PR Revert Procedure (EmoGarbage)
- If we're reverting a PR for technical issues we need to have actual information about what's wrong.
    - I am being so deadass. If a PR is getting reverted for technical issues we need to actually have something to show the author. They will obviously be reopening the PR so let's not just kick the can down the road.
- If a PR is throwing exceptions or causing crashes, we need to get grafana logs.
    - I'm not sure if all maints have grafana access. If they don't, then that needs to be incorporated into whatever our onboarding procedure is.
        - `ROOMBA`: Maints have Grafana access however you have to be above 18 (because PII) and the way to access the logs from Grafana is a little obtuse and needs writing down somewhere for sakes.
        - `Slarti:` We really need a Grafana guide for maintainers (and forks!) so that we know how to use the tools there. I didn't even know I could see all error messages happening on the game servers via Loki until a few weeks ago. This has been insanely useful for finding bugs and more maintainers should keep an eye on it.
    - These logs need to be publicly posted. Ideally we are making git issues for these because splitting it 50/50 discord-github is cancer.
      - `Slarti`: Some of the logs contain player account names, which maybe need to be cleaned up before posting them. But otherwise I agree, I have been making a few issues from errors I have found with Loki, but it's hard to find everything that comes up. 
    - We should also make a special label for these because there's confusion on whether or not to close issues pertaining to reverted PRs (it's in our best interest not to) and it's just good for categorization.
- People involved in the PR need to be notified that there's an issue (reviewers, authors)
    - Pings for PR authors and reviewers both in discord and on github, ideally.
    - By the time something is getting reverted, we should have all the problems chronicled somewhere so we can actually see what happened.
    - If we're having a discussion about the issues and what went wrong, put it all in one place. This can either be `#contributors` or `#maintainers` but either way people shouldn't have to be digging all over the place to figure out what's wrong.
        - Please keep these respectful as the standards for them rn are the literal pits. This goes for every part of the revert process (PR, reporting, etc.) but the discussions especially.
        - `Slam`: Active discussions of an issue are bound to risk being spread-out; while I think it is good if we decide on a central place, requiring a summary in the Revert PR's github thread (e.g. listing our findings) would be beneficial as well.
- Other things I forget about:
    - How does this work for PRs with breaking changes? do we do another announcement? we should have a template.
        - `ROOMBA`: Forks are instructed to pull from stable as all content in `master` is not final. However some PRs that are reverted but still have their posts up might present some confusion? At the end of the day they find out what changes they need to make when they merge the PR so.
    - Do we put relevant info for the reversion on the revert PR or the original PR (true bikeshedders only)
        -  `Slam`: Makes sense on the revert PR; just make sure the original author & reviewers gets tagged!
    - We accidentally leave PR changelogs in all the time when reverting. Does PJBot have the technology for this?
        - `ROOMBA`: We had some larger discussions on what the """new""" changelog system should be on [Discourse](https://forum.spacestation14.com/t/changelogs-and-how-to-handle-them-between-multiple-branches/21413) and the PR reversion jungle dance was a topic. Ideally the changelog is somehow tied to the commit so it can be freely incorporated/reverted piecewise.
            - PJB said that it would ideal for stable to have a seperate CL file and do a git merge for the changelogs during release.
            - While it is preferred to have changelog entries tied to the commit, PJB would prefer it more if the changelog system was kept somewhat independent from the commit.

## Engine/Content Breaking Changes Reminders/Trackers (ArtisticRoomba)
- An [engine PR](https://github.com/space-wizards/RobustToolbox/pull/5442) that refactored TextLinks related stuff had breaking changes
- A [PR to content](https://github.com/space-wizards/space-station-14/pull/32203) was made to fix these, however it was forgotten about and not merged
    - I only found out about this when I was implementing rules for a fork and thought that I was messing stuff up.
- All textlinks in guidebook entries were broken for *10 months* including text links that go to server rules
    - This means that if your server rules were *not* accessible via a child entry in the table of contents, you were unable to view server rules. This goes for the "you seem to be a new player, here's the rules" screen.
- Maints are supposed to push announce for the discourse B/C relay but I physically am unable to do so (-emo)
    - `ROOMBA`: Certified discord perms moment.
- Content fixes for engine breaking changes should be watched more closely.
    - Labels when an engine pr is merged will be good/when the engine changes are pushed. 

## Magic String Landmines (EmoGarbage)
- Biome refactor had a hard crash because old legacy code (gateways) had magic strings getting indexed.
    - Mild digression: is this somehow not covered in testing? I know we have a test for checking if the round starts so we may need to adjust something wrt CVARs so that it actually matches live server conditions. 
- We have the `ForbidLiteral` attribute now: we should update our engine API for prototypes to use it.
    - At the very least, `IPrototypeManager.Index<T>(string)` should have the attribute.
    - Arguably all the PrototypeManager stuff should, but that might be annoying for sanity reasons when prototyping stuff. At the very least we should be throwing errors for code that can cause hard crashes when unrelated things get changed.
      - `Slarti`: Maybe even replace all the `Spawn` API methods with an overload that takes an `EntProtoId` and mark the old ones using `string` as obsolete. This one is the worst offender, but I'm not sure if this is technically feasible.
- This is generally easy to bandaid with static EntProtoIds so can we get this through pretty quickly so that we don't have to worry about it in the future?

## Sprite replication & AppearanceSystem Compliance (Slam)
- Recommended reading: [AppearanceSystem Compliance](https://github.com/space-wizards/docs/pull/307) 
- To summarize: the way our ECS systems are set up means that for some entities it's functionally impossible to accurately replicate the sprite from one entity onto another *without including non-sprite functionality.* E.g. `ClientClothingSystem` sprites are hard-coupled with having an `InventoryComponent` with a clothing entity equipped.
  - These combined gameplay/visuals systems force you to either code in special cases, or find a way to suppress the gameplay code.
- `VisualizerSystem`s exist that only deal with the visuals, modifying sprites based on an `AppearanceData` dict.
  - By copying the `AppearanceData` and using the relevant VisualizerSystem, you can often get an accurate replication of a sprite. Nice!
  - Some implementations only go halfway, where `AppearanceData` is used but a gameplay system still does the sprite change (e.g. `MachineSystem`).
- How can we solve this?
  - AppearanceSystem Compliance doc proposes moving all logic that changes visuals to `VisualizerSystem`s.
    - Concerns about bloating the number of systems; anything that wants to change sprites would need two systems, two components: `ExampleSystem` & `ExampleVisualizerSystem`
    - Redundant data; since VisualizerSystems only change based on AppearanceData, sprite changes based on main system data would need that data copied over to AppearanceData, making for unnecessary double networking.
  - Making SpriteComponent shared.
    - ElectroJr proposed this.
    - Networking would be off by default, but can be turned on to sync/copy sprites.
    - Would require the server to keep track of sprite states and update them accordingly, possibly (?) performance-impacting.


## New Labeller (Simyon)

Any issues? Any wishes?

- Approving applies "Needs changes"
    - Fixed already, requires update from PJB.
        - Cool!
- Maybe implement area "owners" for tagging
    - Small example: https://github.com/dotnet/runtime/blob/main/docs/area-owners.md

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- Slarti
- Roomba
- Errant
- Slam
- Scar
- Simyon
- Tiniest Shark
:::

- [38439](https://github.com/space-wizards/space-station-14/pull/38439) Chameleon Controller Implants can be deimplanted
- [38456](https://github.com/space-wizards/space-station-14/pull/38456) Remove Icon Smoothing for Airlocks, Doors, and Plastic Flaps, and Shutters from Walls
  - `Slarti`: Should this apply to exo airlocks and walls as well, since they have a different art style (question for Slam)? Also one proto was missed in there.
      - `Slam`: Way ahead of you on that one; Exo walls already did not have icon smoothing for its airlocks.
          - `Slarti`: How about the blast door? It still is smoothed with the walls, where the airlocks are not.
              - Ask art leads
              - `Tiniest Shark` It should definitely not be smoothed like other entrances for consistency
  ![](https://hedgedoc.spacestation14.com/uploads/1b1a0a85-395c-492f-a61e-32c4c2ff4a71.png)

- [38218](https://github.com/space-wizards/space-station-14/pull/38218) Scurrets
  - Wawa!
      - FSP has some fixes merged into master outside of the stable range that should be hotfixed in. BLOCKER technically.
          - PR list:
              - https://github.com/space-wizards/space-station-14/pull/38736
              - https://github.com/space-wizards/space-station-14/pull/38561
- [38142](https://github.com/space-wizards/space-station-14/pull/38142) Make... sloths... speak... slowly...
- [38032](https://github.com/space-wizards/space-station-14/pull/38032) Flask Visual Overhaul & YML Organizing
- [38385](https://github.com/space-wizards/space-station-14/pull/38385) Allow Maintainers to use customvote command
- [37952](https://github.com/space-wizards/space-station-14/pull/37952) Make role ban pannel pretty
- [38370](https://github.com/space-wizards/space-station-14/pull/38370) Generic Numeric Alerts
- [38441](https://github.com/space-wizards/space-station-14/pull/38441) Retractable items get removed by handcuffs
- [37182](https://github.com/space-wizards/space-station-14/pull/37182) Readds the Hypereutactic Blade for traitors, adds Hypereutatic blade for Nukies
    - `ROOMBA`: Despite the nerfs on addition, repordedly these items are still pretty overpowered.
    - `Slarti`: The admins reported this to be way to powerful for nukies. I would suggest keeping the traitor variant of the blade, but removing it from the nukie uplink.
        - `ROOMBA`: Yeah, ScarKy voiced extensively before the PR that even with all TC removed and 75% reflect, nukies still won pretty hard in playtests.
            - `Scar`: My complaints were about the 100% reflection chance. 75% looks fine, the only issue is moths in no-gravity with them (which is a shared problem for both nukies and traitors). Other than that small thing I think the item is in a decent (maybe a bit stronger) spot.
            - `Slarti`: Movement speed reduction should probably also apply in zero-g
        - `Errant`: VOTE: Keep / Revert
            - BLOCKER
            - `ROOMBA`: We should discuss the traitor balance as well while we're here.
            - `Scar`: That would be better for a discourse topic, we could spend hours talking out it during the meeting and still not come to a conclusion...
            - `ROOMBA`: [Relevant open PR for reducing reflect to 75%](https://github.com/space-wizards/space-station-14/pull/38753)
- [38206](https://github.com/space-wizards/space-station-14/pull/38206) Allow admins to export round logs to CSV files
    - Myra merged this even though i assigned myself (simyon) to it (not bad, just note for the future) 
        - It appears i am blind, apologizes (Myra)
            - Its fine, dw (Simyon)
                - Im stepping down now as my punishment (Myra ex lead maint /s)
- [38509](https://github.com/space-wizards/space-station-14/pull/38509) Staff of Healing for Pacifists
- [38276](https://github.com/space-wizards/space-station-14/pull/38276) Add wall-based ambient occlusion
- [38526](https://github.com/space-wizards/space-station-14/pull/38526) Re-Add Stamina Damage Resistances to Nukie & ERT Suits after the Test Merge.
- [38541](https://github.com/space-wizards/space-station-14/pull/38541) Added a handheld station map to the cyborg thruster module
    - `ROOMBA`: Formally begging for no more borg modules microbalancing until whitelisted hands are real (PR is open for it)
    - `Slarti`: I wouldn't call this one microbalance, it was accidentally removed in a major overhaul. But in general I would say restrict all microbalancing, not only for borg modules.
        - `ROOMBA`: I'd like to have policy pertaining to this, right now we have a bad habit of saying we're stricting stuff, but only to ourselves, leaving contribs in the dark and causing a lot of unnecessary friction when we have to say no. I'd like our stance against microbalancing put into our PR review procedure somehow. Maybe Emo's axed section on low-desire changes from the PR review procedure rewrite would help here?
        - `Slarti:` I think the best thing we can do is being consistent with PRs that break freezes or restrictions. And do what admins do for these things and use an answer template that can be quickly copy pasted and is clear to understand. For example: "Thank you for your contribution! Unfortunately [PR category] is currently frozen/restricted, see our [list of current freezes and restrictions](github.com/space-wizards/space-station-14/issues/8524): [copy paste the text from the freeze list here]. As such this PR will be closed, but feel free to further contribute in the future!""
            - Add new borg modules to the freezes
            - Actually treat microbalancing as restricted
            - Make a deeper conversation about moving the freezes/restrictions to the docs.
                - Gives us a chance to review freezes/restriction while we are at it
                    - Example clothes and displacement maps are out of date now probably
- [38573](https://github.com/space-wizards/space-station-14/pull/38573) allow combat mode toggling when unable to interact
- [37238](https://github.com/space-wizards/space-station-14/pull/37238) New status effect system
- [38445](https://github.com/space-wizards/space-station-14/pull/38445) Quartermaster's PDA has AstroNav preinstalled
- [38597](https://github.com/space-wizards/space-station-14/pull/38597) Bladed flatcaps are minor contraband
  - `Slarti`: Doesn't this make it useless as a stealth item?
      - `ROOMBA:` They had "this contains glass shards in the blade (...) something" in the description, so discoverable upon inspection.
      - `Slarti`: Yes, but that was still more easy to miss compared to the big red contraband symbol.
      - `ROOMBA`: Unsure where we want to go forward on it, I guess we can ask ScarKy as our resident maint-admin?
      - `Slam`: If it's visible in the description, it should be fair game. Bladed flatcaps are such a low-stakes contraband that its fine if its stealth only holds up to a cursory glance.
          - Not a blocker, not a deal for now.
- [38514](https://github.com/space-wizards/space-station-14/pull/38514) Toy/Plushie Inhands and Wearables
- [38601](https://github.com/space-wizards/space-station-14/pull/38601) HoP's beret
  - `Slarti`: Isn't new roundstart clothing still frozen? We should be more consistent with freezes.
  - `ROOMBA`: Unsure as to if we should be giving the higher-heads (HoP) berets, I thought it was good art direction to have people like HoP and Capt have their commander caps and the lower heads have berets only. Art direction might want to re-consider this?
  - `Errant`: VOTE revert. It's under freeze, although it's debatable if we still need that freeze. Otherwise, I feel like the HOP has a very distinct recognizable look, which would be impacted by clothing variants? I would like to hear the definitive opinion of the Art Leads on this, it was not clear to me how much the approval was for "yes this is a great change" vs "the sprite looks good"
  - `Slam`: Agreed that the freeze should be up for discussion. I don't mind new hats, but I think they should be *new* hats, not just beret recolors.
  - `Tiniest Shark`: I had been strict on berets as a Cargo reward, and thought they were a general command item. Admittedly I hadn't thought much past "Oh, command = beret" and forgot the HoP had a distinctive headwear already. I'm good for reverting, I saw the prior approval and thought conceptually it was approved and just needed a sprite check.
      - Take it to the Art Leads
          - Blocker
- [38479](https://github.com/space-wizards/space-station-14/pull/38479) Various Headphones Fixes and Tweaks
- [35536](https://github.com/space-wizards/space-station-14/pull/35536) Allow the Command & Super door remotes to use the access of their user. (Re-creation of PR due to changes to game balance)
- [38284](https://github.com/space-wizards/space-station-14/pull/38284) Added directional beacons
- [38676](https://github.com/space-wizards/space-station-14/pull/38676) Retro laser sprite fix
- [38131](https://github.com/space-wizards/space-station-14/pull/38131) Reduce most salvage mob health, reduce most salvage weapon damage.
- [38482](https://github.com/space-wizards/space-station-14/pull/38482) Scurrets - Audio Improvements
- [36708](https://github.com/space-wizards/space-station-14/pull/36708) Pressure Relief Valve
- [38434](https://github.com/space-wizards/space-station-14/pull/38434)  Switch HSV to the default colorspace for character customization

### shitpost corner
me when im in a violating thermodynamics in a heat engine competition and my opponent is $Q_{out} = Q_{in} \cdot (1-n)$ where $W = Q_{in}$

i have stared at atmos monstermos equalization and firelock code for three (3) full days
cant wait for day four
You have my unending respect for the fact you have not gone insane yet

https://kbitty.eu/

MEOW
    
:tada: Weeks without non-squashed merges: 4 :tada: 
Gonna direct merge a PR just to spite everyone -Scar
