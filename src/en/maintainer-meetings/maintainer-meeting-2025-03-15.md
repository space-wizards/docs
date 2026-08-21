# Maintainer Meeting (15 March 2025)

```admonish info
- Myra
- Errant
- Simyon
- Milon
- Slam
- Orks
- Shadow
- Crazybrain
- Julian
- Scar
```

This meeting was recorded:

{% embed youtube id="nyGBaORro8c" loading="lazy" %}


## Blood cult (Scar)
- Funky wants to upstream it

<br>

- Get the design doc in
    - Otherwise ok

## Should we generally do more outreach to ask people to upstream content-type stuff that we are interested in? (Errant)
 
- We would have more content and "parity" with downstreams
- All downstreams could automatically enjoy that content
- We would have to do reviews on very complicated PRs, 
- We might annoy the "owner" of those contents if the review is very tedious or never gets anywhere
- Even after we do end up successfully upstreaming some specific antag, if we then later end up changing it in some contentious way, we could generate ill will that "we took over and then ruined it"

<br>

- We should (by that I mean Lead maintainer) write a proposal for this.

## Experimental branches / Test merges (Errant)
###### Big ass note alert
Should we have dedicated experimental branches for developing/upstreaming specific huge features

### Current approach
The incoming Huge Feature is a PR. When it is close to completion, it gets merged into master in a disabled state (Myra: Since when???), allowing it to be turned on manually for testing

#### Cons:
- Nightmare to review. They just sit there because no one wants to review 5 million lines, and can't test it alone. But you can't just toss a half-finished thing on Vulture
- Coding it in a way that can be "turned off" might require extra work, or temporary compromises during develoyment
- Feature is difficult to test until it's "almost ready"
- There is more hesitation to merge something into master, even if turned off
- Might interfere with the development/operation of master branch working on the same PR for multiple people is somewhat less conveninent than working on a branch

### Proposed
Through some vote-based or autocratic process we decide to create an experimental branch for a specific new feature. This could simply be a part of forming a strike team, which would presumably involve the creation of upstreaming of such a huge feature. 
- A new fork of master is made, and the feature in its current state merged into it. This experimental branch will not be involved in the normal release or hotpatch procedures. Instead, we just merge master into it whenever.
- When we want to test the feature, we publish the experimental branch to vulture, run the test (with pre-arranged maint and admin coverage), then publish master again when done
- When the maintainer consensus decides that the feature is ready to ~~go~~ head to stable, we just merge the experimental branch into master. With a single, finely-crafted changelog to boot.

#### Cons:
- Experimental branches with no open prs might get forgotten
- **We would need new labels for Branch: Experimental, and perhaps some clarification in the review procedure about eased requirements for such branches and/or clarification for the approval/merge decisions for them** (Should a specific maint or group of maints be "in charge" of each experimental branch, with final say over what gets merged into it? Keep in mind that the merge of the experimental branch back into stable would still undergo the normal release review procedure, this would just prevent bikeshedding *along the way* there)
- Possibly increased workload with keeping it deconflicted with changes on master, although this will either make the merge at the end easier, or can just be skipped to be done at the end in one go, which would have to be done to begin with.
- If we have too many experimental branches, they might start to stall. So just not have several of them open at the same time. And have specific
- If we want to keep experimental on Vulture for an extended period of time, we would have to disable auto-publish, and re-enable it after we go back to master

<br>

- Conlusion: This sounds like a sure a think? This is kinda being bikeshed like hell in this voicechat and I can't pay attention.
- We should work on this on discourse and make some discussion on it.

## Sidetrack: Planka and strike teams
- We are waiting the Planka devs to release v2
    - When is that?
        - IDK

## Sidetrack: Maintainer bot when
- On hold
- It does have a version to try out right now but someone needs to set it up
- Still has stuff needing to be implemented

## What should lead maints focus on doing?
- Clean up the org
- Think of a way of how to deal with inactive staff (Assigned to @Myra)
- OK the rest should probably be handeled on discourse actually

## Stable review
- [35520](https://github.com/space-wizards/space-station-14/pull/35520) [ADMIN] Minor Refactor AdminNameOverlay
- [35572](https://github.com/space-wizards/space-station-14/pull/35572) Wizard PDA
- [35158](https://github.com/space-wizards/space-station-14/pull/35158) make slime hair less transparent
- [35602](https://github.com/space-wizards/space-station-14/pull/35602) Changed Pride to Hubris in ion_storm.yml
- [35058](https://github.com/space-wizards/space-station-14/pull/35058) Sentry turrets - Part 3: Turret AI
- [35438](https://github.com/space-wizards/space-station-14/pull/35438) DetGadget Hat Revitalization
- [35583](https://github.com/space-wizards/space-station-14/pull/35583) Remove cellular resistance for slimes
- [35600](https://github.com/space-wizards/space-station-14/pull/35600) Fingerprint Reader System
- [35605](https://github.com/space-wizards/space-station-14/pull/35605) Give the station map inhand sprites
- [35608](https://github.com/space-wizards/space-station-14/pull/35608) Reagent guidebook reactions UI dividers
- [35330](https://github.com/space-wizards/space-station-14/pull/35330) Revert "Make radioactive material radioactive"
- [35455](https://github.com/space-wizards/space-station-14/pull/35455) add altered silicon to rules
- [35564](https://github.com/space-wizards/space-station-14/pull/35564) [HOTFIX] - Players with unknown playtimes now are tagged as new players
- [35648](https://github.com/space-wizards/space-station-14/pull/35648) Players with unknown playtimes now are tagged as new players, take 2
- [31812](https://github.com/space-wizards/space-station-14/pull/31812) Better Insectoid Glasses
- [35587](https://github.com/space-wizards/space-station-14/pull/35587) Save Space Station 14 from the Toilet Gibber Forever
- [34535](https://github.com/space-wizards/space-station-14/pull/34535) Changed Damage Overlay to check Burn Damage
- [35623](https://github.com/space-wizards/space-station-14/pull/35623) Wizard's Magical Pen
- [35643](https://github.com/space-wizards/space-station-14/pull/35643) Added decelerator percentage drain
- [35650](https://github.com/space-wizards/space-station-14/pull/35650) Made butter require less milk
- [35651](https://github.com/space-wizards/space-station-14/pull/35651) CVar - Toggle display of round-end greentext
- [35667](https://github.com/space-wizards/space-station-14/pull/35667) Make implants unshielded
- [33185](https://github.com/space-wizards/space-station-14/pull/33185) Add undergarments & "Censor Nudity" toggle to options
- [35644](https://github.com/space-wizards/space-station-14/pull/35644) More scars!
- [35570](https://github.com/space-wizards/space-station-14/pull/35570) Lathe menu UI displays a count of available recipes
- [35429](https://github.com/space-wizards/space-station-14/pull/35429) Cargo Mail System
- [35518](https://github.com/space-wizards/space-station-14/pull/35518) add forceghost admin command
- [35145](https://github.com/space-wizards/space-station-14/pull/35145) Add sun shadows (planet lighting stage 2)
- [35718](https://github.com/space-wizards/space-station-14/pull/35718) Aroace pride pin, scarf, and cloak
- [35728](https://github.com/space-wizards/space-station-14/pull/35728) Initial delivery balance changes
- [35746](https://github.com/space-wizards/space-station-14/pull/35746) Steal the mail thieving objective
- [35748](https://github.com/space-wizards/space-station-14/pull/35748) Slightly better letter loot table
- [35593](https://github.com/space-wizards/space-station-14/pull/35593) Python Suit Storage Visual
- [33570](https://github.com/space-wizards/space-station-14/pull/33570) Added New Cocktails and new fill level sprites to existing drinks.
- [35764](https://github.com/space-wizards/space-station-14/pull/35764) Performer's Wig
- [35769](https://github.com/space-wizards/space-station-14/pull/35769) Removable mindshields and revolutionary tweaks.
- [35776](https://github.com/space-wizards/space-station-14/pull/35776) Mail Resprite
- [35751](https://github.com/space-wizards/space-station-14/pull/35751) Update to borg ion storms
- [35313](https://github.com/space-wizards/space-station-14/pull/35313) New Feature: Warden job rolls before security officer/cadet/detective
- [34809](https://github.com/space-wizards/space-station-14/pull/34809) Add Gold and Coal Rock Anomalies
- [33689](https://github.com/space-wizards/space-station-14/pull/33689) Tools/Devices: In-hand Sprites
    - Comically large scissors
        - I think maybe we should make them smaller? Personal opinion (Myra) I will leave this to an art maint
- [35790](https://github.com/space-wizards/space-station-14/pull/35790) IconSmooth additional smoothing keys
- [35785](https://github.com/space-wizards/space-station-14/pull/35785) Locks nitrous oxide canisters
- [35819](https://github.com/space-wizards/space-station-14/pull/35819) Add the ability to pet the mail teleporter
- [35821](https://github.com/space-wizards/space-station-14/pull/35821) Whitehole/Singularity grenade price adjustments + whitehole grenade fix
- [35794](https://github.com/space-wizards/space-station-14/pull/35794) Paradox Clone

## Notes
- Slart can't come but anything Paradox clone related check out the todo list https://github.com/space-wizards/space-station-14/issues/35831


## Closing thoughts
- I just want to say to everyone in the maintainer team and our contributors how much amazing content we managed to get these last few days. Keep it up!
- We are not doing another random stuff corner sorry not sorry.
