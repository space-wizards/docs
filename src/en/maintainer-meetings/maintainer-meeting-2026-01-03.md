# Maintainer Meeting (3 Janurary 2026)

```admonish info
**Attendees:**
- Slam
- Errant
- Scar
- Myra
- Slarti
- Akesi ma
- Karon
- Princess Cheeseballs
```

This meeting was recorded:

{% embed youtube id="kaACrMc731o" loading="lazy" %}

## Happy new year! (Myra)
WOO


## Docs Review Meetings (ArtisticRoomba)
Currently, the documentation side of this project has several issues:
1. It's a rotting unreviewed mess.
    - Nothing ever gets reviewed unless the implementation is just really poor or a maintainer pushes their own stuff through. It's an insult to contributors to expect them to write out plans that we just discard.
    - Asynchronous discussions on the documents are fractured across three platforms (Discourse, GitHub, and Discord). This leads to a lot of banter and very rarely actual meaningful discussion, and even more rarely, actual action.
2. The dev wiki itself is heavily outdated and contains a lot of stuff we literally do not follow anymore.
    - Apparantly someone long ago restructured the entire dev wiki overnight without any warning.
    - A lot of pages are just straight filler. Departments have "PR Guildlines" which are blank. Department design documents themselves are mostly templates.
    - Our core design principles do not reflect our current design philosophy (considering we can't really agree on one). Some content in the repository is in violation of them and other "design pillars" like the antagonist design pillars.
        - A lot of the design pillars either need to be rewritten or offending implementations readjusted. Some of the core design pillars are good and some of them aren't, same with the antagonist design pillars, so unfortunately this is going to be a subjective case-by-case matter.
    - Some documents are marked as "Legacy documentation" that took place before the "game area restructuring" which is BS because that never came to fruition.

### Proposal
I'd like to add a new meeting to our schedule that takes place between our maintainer meetings. It would be at our regular time, just a week after Stable Review.

The meeting schedule would look like Stable Review -(one week)-> Docs Review -(one week)-> Stable Review.

In this meeting, attendees can sit down and make some decisions on our design document backlog. The hope is that, by discussing these synchronously, we'll have enough maintainers available to action on some documents according to our docs review policy.

The first meeting will be freeform, but at the end of each meeting, the attendees should establish some sort of topics list to discuss for the next meeting in order to stay on track. This should be done similar to admin meetings. I'm sure that, if the topics list falls through for some reason, any maintainer can work on it asynchronously.

- **What if I'm not able to attend but I still want to influence design?**
    - If you're not active enough to attend these discussions then it would probably be best to leave the discussion to those who are present and up-to-speed with the game. In any sense any large final decision is probably going to be put to a quick-maint-discussions vote so you'll be able to voice final concerns later.
        - `Errant`: Do we have any maints left who are in a timezone where the meeting timeslot is bad? 
    - `Slarti`: We can take some (short) notes during the discussion on a hegdedoc similar to maint meetings so we have any decisions written down, which should also give other maintainers a chance to comment on it.

- We should have some more discussion about this on discourse. We should not be making decisions on something like this when not all maintainers can attend. Give it a week for discussion.
    - Ask roomba if they are feeling to make the discourse thread

## Markings/Species Freeze (Janet/ArtisticRoomba)
Janet is requesting that markings and species be frozen for a few weeks. She needs it frozen because `HumanoidAppearance` and the markings system aren't suitable for the future plans with surgery, prosthetics, and general bodycode, so a refactor is in order.

The scope is `Content.*.Humanoid`, `Content.*.Body`, and components/prototypes defined with their types. It will last until the refactoring efforts revolving around `HumanoidAppearance` are finished.

See the message line [here](https://discord.com/channels/310555209753690112/900426319433728030/1456816126377066709).



## Stable review

```admonish info
Write your name here if you read this list fully.
**I checked this PR list:**
- Princess
- Roomba
- Errant
- iaada
- Tiniest Shark
- Janet
- Slam
```

- [41884 ](https://github.com/space-wizards/space-station-14/pull/41884) Re-work Arrivals Shuttle to have un-interactable substation and APC
- [33157](https://github.com/space-wizards/space-station-14/pull/33157)  Rebalance the Ghost Role Raffles
    - `Errant`: Unclear to me why the minor ghostrole time was increased by 5 seconds. No reasoning was given for that part. It's also kinda weird that the major antag lottery proto reduces the timer extend to 2 and then sets the maximum duration to the same as the starting. Why not just set it to 0, like the other one?
    - - `iaada`: Join extensions don't go above the max duration, so those 2 seconds aren't getting added and it should be changed to 0.

- [33251](https://github.com/space-wizards/space-station-14/pull/33251) Syndicate Wall Lockers and Secure Storage
    - `Roomba`: Shortest upstream review turnaround time
- [32931](https://github.com/space-wizards/space-station-14/pull/32931) feat: RnD tech research console now have reroll feature
    - `Errant`: Are rerolls logged so we can monitor how much it's used?
      - `iaada`: Glanced through and didn't see logging.
          - It should have logging
    - `Slarti`: Will this actually have a positive impact from a game mechanics perspecitive? At the moment you will have to diversify a little between different reasearch areas, which means other departments benefit more. But you you can just reroll and waste research points until you get that one tech you want to have. At that point I would rather replace the random rolls completely and add a tech tree or something.
    - Researching something else already has the same effect and rerolls all other available techs, but without wasting points.
    - RnD research being random is a deliberate design choice to get people to not rush specific research.
        - Vote: REVERT/KEEP (BUT check in with the science workgroup FIRST)
- [41335](https://github.com/space-wizards/space-station-14/pull/41335) Cleanup of circuit tote / stamp box prototypes + added small cardboard boxes as a general item
- [41326](https://github.com/space-wizards/space-station-14/pull/41326) Shield QoL + buff
  - `Slarti`: We really need to predict DestructibleSystem, having unpredicted examination strings like this is awful
- [40607](https://github.com/space-wizards/space-station-14/pull/40607) Station AI ghost role
- [41923](https://github.com/space-wizards/space-station-14/pull/41923) Added sprites for openable ingredients
- [41932](https://github.com/space-wizards/space-station-14/pull/41932) Miscellaneous Injector fixes + BorgHypo fill sprites.
- [41933](https://github.com/space-wizards/space-station-14/pull/41933) Rename LOOC chat to Help chat
    - `Slam`: I'll talk about this PR during the meeting since I'm still gathering data; if I don't make it to the meeting for whatever reason, this PR is to be reverted.
        - Revert.
        - This will have another rerun in vulture.
- [41885](https://github.com/space-wizards/space-station-14/pull/41885) Basic Dynamic Power Consumption Systems
- [41279](https://github.com/space-wizards/space-station-14/pull/41279) Allow cable coils to be destroyed
- [41960](https://github.com/space-wizards/space-station-14/pull/41960) Make donk co. microwave syndicate contraband
- [42026](https://github.com/space-wizards/space-station-14/pull/42026) Change "mafioso" (singular) to "mafiosi" (plural) in the Italian accent.
- [41955](https://github.com/space-wizards/space-station-14/pull/41955) Change Botany Minimum Quantity For Random Chems
- [42018](https://github.com/space-wizards/space-station-14/pull/42018) Change "pappa" (food) to "papà" (dad) in Italian accent
- [42020](https://github.com/space-wizards/space-station-14/pull/42020) Fix greytide terms in Italian accent
- [40076](https://github.com/space-wizards/space-station-14/pull/40076) Add jet injectors
- [41965](https://github.com/space-wizards/space-station-14/pull/41965) Voice mask effects are toggleable and hide your accent
- [38481](https://github.com/space-wizards/space-station-14/pull/38481) ERT Overhaul 3/3: Loadouts
- [42111](https://github.com/space-wizards/space-station-14/pull/42111) Lowered Xenoborgs MinPlayers From 40 To 30
- [42104](https://github.com/space-wizards/space-station-14/pull/42104) Merge IFF controls into one control. Make syndicate IFF turned off by default.
- [42077](https://github.com/space-wizards/space-station-14/pull/42077) Add crayon box to Big Bite meals
- [42133](https://github.com/space-wizards/space-station-14/pull/42133) Add antag control for the space ninja
- [42102](https://github.com/space-wizards/space-station-14/pull/42102) puts Space ninja survival box contents into their bag
- [42114](https://github.com/space-wizards/space-station-14/pull/42114) Give decoy bomb restock time.
- [42167](https://github.com/space-wizards/space-station-14/pull/42167) Ammonia restores Rat King Bloodlevel
- [40121](https://github.com/space-wizards/space-station-14/pull/40121) Chemmaster Pill Source
- [42119](https://github.com/space-wizards/space-station-14/pull/42119) Move borg module remove button to the left side
- [42112](https://github.com/space-wizards/space-station-14/pull/42112) Ninjas now get a custom bag!
- [42158](https://github.com/space-wizards/space-station-14/pull/42158) Jet Injector Tweaks and Cleanup.


### Blocking prs
- [#42032](https://github.com/space-wizards/space-station-14/pull/42032) Fix all currently known markup issues
    - This can be made to work without engine sided changes.
    - Done
- [#42195](https://github.com/space-wizards/space-station-14/pull/42195) Fix Disabler SMG bolts going through walls
    - This PR prevents disabler bolts from not getting deleted when they collide with players/walls/anything. 
    - Done
- Not sure if it's blocking but we might want to revert all the temporary christmas changes for this release. Maps are not that critical, but stuff like the insane presents and the christmas anomaly would make sense (unless we want to keep them for 2 more weeks).
    - https://github.com/space-wizards/space-station-14/pull/38940 should have a review hopefully so we dont have to do this every year.
    - Ask admins
    - Done
- [#42206](https://github.com/space-wizards/space-station-14/pull/42206) Pr that needs engine cherry picked
    - Cherry pick the engine update over. Fixes the chat formatting. I personally dont consider this blocking.
    - Done
- [#42221](https://github.com/space-wizards/space-station-14/pull/42221)
    - Admins requested I put this into staging. The main intent of the PR was to prevent dynamic and static bodies from going through the mover controller, so I'm fine with kinematic bodies going through until our physics engine is better:tm:
    - Done

### Should be looked at
- [RT #6355](https://github.com/space-wizards/RobustToolbox/issues/6355) VSCodium is currently completely unable to build the game due to the switch to slnx since that format is not yet supported by the C# extension. If there is a workaround we should write it down in our [Setting up a Development Environment guide](https://docs.spacestation14.com/en/general-development/setup/setting-up-a-development-environment.html) since we are recommending that IDE there and the current instructions will not work.
    - Myra: https://devblogs.microsoft.com/dotnet/introducing-slnx-support-dotnet-cli/#c#-dev-kit Not the first time I linked the workaround. If VSCodium does not even work with this workaround then this is their skill issue and not ours. SLNX has been out since net9 they had a long time to at least get the above workaround in. The only thing we can really do otherwise is remove VSCodium on the docs. We are not reverting back from SLNX for all the other stated reasons plus because a single code editor did not implement support, vscodium is also open source if you wish to contribite the support.
    - Slarti: Fair, but like you are saying we should update the docs accordingly. Because our current recommendation there is entirely broken.
