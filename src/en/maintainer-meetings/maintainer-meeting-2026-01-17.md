# Maintainer Meeting (17 January 2026)

```admonish info

**Attendees:**
- Errant
- Roomba
- Princess chzbls
- Myra
- PJB
- Akesima
- Scarky0
- Slam
- Simyon
- Julian

```

This meeting was recorded:

{% embed youtube id="j6viFWphri0" loading="lazy" %}

## The Great StyleCop Police State (ArtisticRoomba/Slarti)
Slarti brought up adding the StyleCop analyzers to the Content repository. The main benefits are:
- Reducing a lot of manual review/scanning required (usings in alphabetical, documented fields, etc.)
- Document your public methods/fields!!!
- Code is overall cleaner.

I have changed some defaults in `StyleCop.json`.

The following analyzers have been disabled by me for the following reasons:
- SA1309 (SA1309FieldNamesMustNotBeginWithUnderscore)
    - We are not writing `this.` to prefix every local method.
- SA1101 (SA1101PrefixLocalCallsWithThis)
    - We are not writing `this.` to prefix every local method.
- SA1503 (SA1503BracesMustNotBeOmitted)
    - `if (HasComp<FooComponent>(uid))`
        `return;`
    - This will warn on `if (HasComp<FooComponent>(uid)) return;`
- SA1633 (SA1633FileMustHaveHeader)
    - Not applicable.
- SA1401 (SA1401FieldsMustBePrivate)
    - I don't think it needs to be a warning.
- SA1402 (SA1402FileMayOnlyContainASingleType)
    - Events, enums and such.
- SA1133 (SA1133DoNotCombineAttributes)
    - `[DataField, AutoNetworkedField]`
- SA1134 (SA1134AttributesMustNotShareLine)
    - `[Dependency] private readonly FooSystem _foo = default!;`
- SA1516 (SA1516ElementsMustBeSeparatedByBlankLine)
    - This will warn on lists of private fields.
- SA1623 (SA1623PropertySummaryDocumentationMustMatchAccessors)
    - We have accessors and they will scream that you MUST write "get" or "set" on the documentation.
- SA1130 (SA1130UseLambdaSyntax)
    - Writing `delegate` instead of `() => {}` is much more friendly in tests.
- SA0001 (SA0001XmlCommentAnalysisDisabled)
    - Not applicable.
- SA1201 (SA1201ElementsMustAppearInTheCorrectOrder)
    - This is unfixable at the scale it appears in the codebase. There is no analyzer to do this for us.
        - `Errant`: Does the analyzer, or could it, enforce the ordering of yaml's datafields, though? "abstract parent id name" often gets swapped around and then copypasted wrong, and it can be annoying
        - `Roomba`: StyleCop for is C# only. Anything that makes sure that component fields and YAML fields match up would be the job of the YAML linter.
- SA1642 (SA1642ConstructorSummaryDocumentationMustBeginWithStandardText)
    - Another weird analyzer that makes your code comments start with specific words - it's not really applicable nor fixable at our scale.

The changes bring our warning count up from 486 to 27,625 (likely decreasing as I find unnecessary warns to trim down).

Raw, clean debug build times have increased from 35s -> 47s.

We will likely need to go over more warnings in the meeting that we'd like to silence as there's a lot that are up for discussion.

PR: https://github.com/space-wizards/space-station-14/pull/42469

Conclusions:
- For this to be useful we would need to have some system to enforce fixing stylecop warnings as a test/merge queue. Such as showing those style warnings as errors.
- Will cause a bunch of merge conflicts for us and downstreams. How worth is it?
- We can downgrade from warnings to suggestions instead.

## Docs Repo Cleanup/Split (ArtisticRoomba)
Docs pages are currently a mess, we all know that.

More accurately, the table of contents for the page is effectively unbrowsable and should not be so long.

I believe it would be wise to find a way to section the various development categories (design, technical documentation, staff and policy, meeting archives) into their own visible lists or sites or whatever.

In general, a clean, nice to browse docs site would be more attractive to contribute to and read. Right now I don't really like browsing random docs pages which I think is contributing to our whole wandering design problem.

You can't remove maintainer meetings from the ToC in mdbook. So yes, this really is not actionable at all unless you have a proposal to switch off mdbook.

## Revert [Rename LOOC chat to Help chat #41933](https://github.com/space-wizards/space-station-14/pull/41933) (Slam)
The PR's testing duration has passed and Ress have been able to gather the data. However they haven't had time to process the data, so a discussion regarding its result can't be had at this time. 

Until such a discussion can be had, the PR should be reverted.

* `Ress`: Internal forum post to be made when my research is done.

## Stable review

```admonish info

Write your name here if you read this list fully.
**I checked this PR list:**
- Errant
- ScarKy0
- Tiniest Shark
- Biggest Slam
- Princess

```



- Remove giftmas stuff from various maps
    - `Errant`: Should double-check that we got all maps
- [42201](https://github.com/space-wizards/space-station-14/pull/42201) - Make xenoborg thrusters anti-easy-sabotagge
- [34165](https://github.com/space-wizards/space-station-14/pull/34165) - expanded FillLevelSpriteTest test and fixed found issues
- [41962](https://github.com/space-wizards/space-station-14/pull/41962) - Intercom resprite
- [39793](https://github.com/space-wizards/space-station-14/pull/39793) - Ironsands Structures
- [41425](https://github.com/space-wizards/space-station-14/pull/41425) - Melee weapons animations upgrade
    - `Slam`: I think this change works in some cases, in some cases not. E.g. without having an impact vfx it is harder to read light attacks, and self-attacks involve swinging the weapon outwards. 
    - `Slam`: Ideally I'd want to see some of the old animations supported in the new format.
- [42234](https://github.com/space-wizards/space-station-14/pull/42234) - Dragon rift no longer deletes all rifts when destroyed
- [41936](https://github.com/space-wizards/space-station-14/pull/41936) - Msg Toolshed Command
- [42267](https://github.com/space-wizards/space-station-14/pull/42267) - Revert Closable Jugs
- [42200](https://github.com/space-wizards/space-station-14/pull/42200) - [FEATURE] More icons
    - `Errant`: Isn't this going to be potentially confusing for borgs when trying to determine who is crew? I don't think we ever got the Crew Indicators
    - `Slam`: Can we please merge that? Minemoder has been consistently asking and has cited it as an example when it comes to issues with Admin-Maintainer relations. https://github.com/space-wizards/space-station-14/pull/37038
        - Please review ASAP
- [42146](https://github.com/space-wizards/space-station-14/pull/42146) - Guarantee glue and lube in toybox
- [42271](https://github.com/space-wizards/space-station-14/pull/42271) - Chameleon Projector Battery, Price Decrease
- [42205](https://github.com/space-wizards/space-station-14/pull/42205) - Xenoborg camera monitor now shows xenoborgs names
- [42280](https://github.com/space-wizards/space-station-14/pull/42280) - Vox now say they become fried chicken upon taking enough heat dm
- [42184](https://github.com/space-wizards/space-station-14/pull/42184) - Reorganize and clean Fun yml
- [41208](https://github.com/space-wizards/space-station-14/pull/41208) - Ninja bomb planting tweak
- [42276](https://github.com/space-wizards/space-station-14/pull/42276) - Warden Suit Tail Fix
- [42292](https://github.com/space-wizards/space-station-14/pull/42292) - Remove battery from the handheld health analyzer
- [39189](https://github.com/space-wizards/space-station-14/pull/39189) - fix: respect AllowedSlots for gogo hat
- [41236](https://github.com/space-wizards/space-station-14/pull/41236) - Bring back shrug sanitization in a different form
- [42211](https://github.com/space-wizards/space-station-14/pull/42211) - Add craft for bonfire and bonfire with stake
- [42209](https://github.com/space-wizards/space-station-14/pull/42209) - Increase shuttle FTL cooldown to prevent FTL spamming
  - `Slam`: I do not think this will be sufficient in stopping the behavior the PR claims to stop. You're not gonna be able to catch up to another shuttle in 60 seconds. 10 minutes? More viable.
      - `Princess`: There's a delicate balance between not overly punishing a player messing up the not great FTL UI and preventing players from using shuttle cheese. I think anything beyond 60 seconds we should just find a different better solution.
          - A more proper "non bandaid" solution should be sought after, but in the meantime it is alright to keeep.
- [39195](https://github.com/space-wizards/space-station-14/pull/39195) - feat: allow removing empty smart fridge entries
- [42320](https://github.com/space-wizards/space-station-14/pull/42320) - Fix projectile deceleration
- [41201](https://github.com/space-wizards/space-station-14/pull/41201) - Add the Syndicate Delivery Console + Corpsman Medicine Bundle
    - `Princess`: I'm interested to see how this one plays out. Also did you remember to make it unanchorable Slam? 
        - `Slam`: Don't you mean un-unanchorable :godo: But no, but at the same time it's probably not gonna be gamebreaking because the bag itself is portable anyhow. But I can hotfix it in if it'll help.
            - `Princess`: Probably worth a hotfix.
                - Hotfix is accepted.
- [42337](https://github.com/space-wizards/space-station-14/pull/42337) - Add the Syndicate Delivery Console to the Nukie planet + target station map
- [42208](https://github.com/space-wizards/space-station-14/pull/42208) - Foldable wig on clowns mask
- [39288](https://github.com/space-wizards/space-station-14/pull/39288) - fix: clear health bar/icon overlay damage containers on update
- [41248](https://github.com/space-wizards/space-station-14/pull/41248) - Add the ability for station maps to track grids they are not on
- [42123](https://github.com/space-wizards/space-station-14/pull/42123) - Medical Cyborg Modules Rework.
- [42155](https://github.com/space-wizards/space-station-14/pull/42155) - Spray bottles with visible reagent contents
- [42317](https://github.com/space-wizards/space-station-14/pull/42317) - Reworks destruction Space Law to include Silicons
- [39837](https://github.com/space-wizards/space-station-14/pull/39837) - Allow late join from arrivals to be considered for antagonist.
- [42370](https://github.com/space-wizards/space-station-14/pull/42370) - Allow the admin door remote to toggle overcharge
- [42302](https://github.com/space-wizards/space-station-14/pull/42302) - Balance swing at Vestine
- [42383](https://github.com/space-wizards/space-station-14/pull/42383) - Lower hyperzine injector cost
- [42381](https://github.com/space-wizards/space-station-14/pull/42381) - Lower smuggler's satchel price to 1TC
- [31776](https://github.com/space-wizards/space-station-14/pull/31776) - Role time tracking support for admins
- [42334](https://github.com/space-wizards/space-station-14/pull/42334) - Adds EMP Resistance component, gives it to ninja suit and headse
- [38898](https://github.com/space-wizards/space-station-14/pull/38898) - Allow station tiles to be placed on solid ground and other platings
    - `Princess`: I'm worried about the code quality of this PR, specifically ExplosionSystem.Processing. Much of the code added should be API and having two dictionary lookups per tile, as well as dirtying that history for every tile. It only applies to those that have a stack but I feel like chunk history should be acquired before we are looking at individual tiles. We also should not be doing a CompOrNull for every single tileRef we process either.
        - The code should be looked at further and optimised.
            - VOTE: Revert - Keep. Revert reason: Code optimisation and performance concerns. Unable to be properly hotfixed.
- [42350](https://github.com/space-wizards/space-station-14/pull/42350) - WYA to Where you at
- [42391](https://github.com/space-wizards/space-station-14/pull/42391) - Buff throwing knives kit
- [42393](https://github.com/space-wizards/space-station-14/pull/42393) - Fix scram allowing you to bring someone along
- [42392](https://github.com/space-wizards/space-station-14/pull/42392) - Viper High Capacity Ammo
- [42319](https://github.com/space-wizards/space-station-14/pull/42319) - Pry open critical Borgs
- [41870](https://github.com/space-wizards/space-station-14/pull/41870) - Fix tritium fires breaking conservation of mass
- [42407](https://github.com/space-wizards/space-station-14/pull/42407) - Fix TritiumFireReaction low fuel limiting behavior
- [42421](https://github.com/space-wizards/space-station-14/pull/42421) - Increase TEG power generation by 75%
- [42400](https://github.com/space-wizards/space-station-14/pull/42400) - Increase trit-to-frezon ratio from 1:8 to 1:50
- [38335](https://github.com/space-wizards/space-station-14/pull/38335) - Maid uniform sprite change.
- [42376](https://github.com/space-wizards/space-station-14/pull/42376) - Add a target station map to the LoneOp shuttle
- [42295](https://github.com/space-wizards/space-station-14/pull/42295) - Xenoborgs now drop pieces of pinpointer
- [42416](https://github.com/space-wizards/space-station-14/pull/42416) - Make lathes refund materials when recipe gets cancelled
- [42283](https://github.com/space-wizards/space-station-14/pull/42283) - allow shuttle to Scan for Objects while FTL is on cooldow
- [42412](https://github.com/space-wizards/space-station-14/pull/42412) - Fix TryAllReactionsTest reacting early and not checking priorit
    - `Errant`: Please tell PR authors to actually fill out the template even if they are a wizard
- [42390](https://github.com/space-wizards/space-station-14/pull/42390) - Reduce unnecessary ComponentInit work for airtight entities
    - `Errant`: This does not need to be/should not be in the changelog. We should remove it
        - `Slam`: Not player-facing, no changelog needed.
    - `Scar`: Personally I'm of belief we should start including technical changes in our changelog if they face things players could notice (Prediction, Major cleanups, etc). Seeing this won't really be noticed by plares it could probably be removed from theCL.
        - `Beck`: I agree with scar
- [42408](https://github.com/space-wizards/space-station-14/pull/42408) - Put arrows on all the single-directional pipes
- [42298](https://github.com/space-wizards/space-station-14/pull/42298) - Make cancer mice actually hurt
- [42415](https://github.com/space-wizards/space-station-14/pull/42415) - Make heavy xenoborg able to "swim" in space
- [41850](https://github.com/space-wizards/space-station-14/pull/41850) - Cryo pod UI
- [41457](https://github.com/space-wizards/space-station-14/pull/41457) - Make chemicals not react inside pills (and stomachs)
    - `Errant`: We should probably ask Baldman about this in a week
        - They already have :godo:
    - `Slam`: I am sceptical of this PR. It feels like it will lead to pill shenanigans and we have already seen Baldman use it to create CLF3 pill launchers.
    - `Princess`: It's so far been nothing that you can't already do with bottles more easily.
- [38231](https://github.com/space-wizards/space-station-14/pull/38231) - Improved Health Examination Coloring
- [36132](https://github.com/space-wizards/space-station-14/pull/36132) - Rebase vials to DrinkBase, closeable vials, mini vials
- [42040](https://github.com/space-wizards/space-station-14/pull/42040) - Add Paper Centrifuge
- ... and ~50 bugfixes and non-feature changes
