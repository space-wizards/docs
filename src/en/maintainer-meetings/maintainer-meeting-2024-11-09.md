# Maintainer Meeting (9 November 2024)


**Time:** 9 November 2024

```admonish info

**Attendees:**
- Vasilis (Myra)
- Jezithyr
- notafet
- Lank
- Errant
- Ret
- Chromiumboy
- Slartibartfast
- PJB
- Shadowcommander
```

Notice: This meeting was recorded: 

{% embed youtube id="fIMzlJB2oOY" loading="lazy" %}

## Github organisation

### Triage
- Who gets triage role? What should they do?
    - Currently anyone who asks gets it, should we change it?
        - We should probably only hand it to expirienced contribs or trustworthy enough
    - We should have a triage policy for these contributors to follow
        - Ensure we communicate they CANT close prs
    - Should we use github projects?

- Speaking of expirienced contrib and maintainer?... who is CONSIDERED one?
    - Currently its just give it to people we think deserve it
        - We should have some kind of "requirement"
    - Basicly anyone who is friendly enough and we know is trustworthy enough and knows the codebase.
        - This should be a document
        
### Codeowners
We should clean it up, and maybe add some people.

- Codeowners should be used as the "The person here MUST review your pr to be approved"
    - Github has a branch protection rule to [require approval from any of the owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners#codeowners-and-branch-protection) to allow merging

- We should tag prs for each workgroup that gets added to prs

### Github pr/issue discussion
- It can be pretty common for people to cause trouble in issues/prs needing moderators and maintainers to come in and lock conversations or hide the comments.
    - Github moderation sucks and we cant just make it so that only contribs can communicate in comments but still make new prs or issues.
        - We may need to bite the bullet and make an automated system to be "added" so that people cant as easily drive by to complain. Similar to how unreal engine does 
        - This will also allows to "warn" users about their behevior
        - Moving to another git forge is NOT 
    - For issues its better we try to find a way to have a "subnautica report bug" button (julian had something?)
        - This will create an issue on a diffrent repo, and then can move it to the main repo after its reviewed.


## Somewhat sidetrack: Replays and stalking
- Hiding yourself from replays should be standardised
    - While the public replay browser hides maints/admins, its not preventing someone from just getting the source and running it themselves or just downloading the replay and seeing the replay_final.yml file
        - This can only really happen server side with a client setting

## Branches and hotfixes
- Hotfixes should be hotfixed into stable and then stable gets merged into master **WITH A REGULAR MERGE, NOT SQUASH**
    - We shouldn't have conflicts 
    - Github action?

## Test server
Currently, we run servers from the stable branch. Its gonna be nice to have.

- It has been decided miros will be the test server
- Potencial issue: It may make skipping role prerequisites easier
    - Example: On master we made cap require 5 hours command, but stable still needs 1 hour. Players can keep playing cap on stable while getting command time.
        - If we block time progression on test servers, players may not wanna play there.
            - Ask admins?
    - Sidetrack: OUR PLAYTIMES REQUIREMENTS SUCK
        - Per server roletimers?
            - Or per server multiplier?
    - Test server cvar?
    - Per server permissions so that maints can have limited admin access
        - Myra Sidetrack: Wait how is codermin/grafana role going?
            - Grafana is pii
            - SS14.Admin lets you login anyway even if pii is disabled on the admin.
    - How would we set it up?
        - Publish to a seperate branch, publish that to robustcdn. Easiest
        - Something in robustcdn to differentiate testing vs release

###### Jez got sidetracked by the mothroach plushie
###### merch.spacestation14.com when?

## Stable review
For the full commit list, look [here](https://github.com/space-wizards/space-station-14/commits/staging/) instead.
- [32377](https://github.com/space-wizards/space-station-14/pull/32377) Add flash reaction effect
- [32942](https://github.com/space-wizards/space-station-14/pull/32942) Fix loneop spawnrate by reverting it to not use the shuttle event system
- [32460](https://github.com/space-wizards/space-station-14/pull/32460) add atmosia to devmap
- [32636](https://github.com/space-wizards/space-station-14/pull/32636) Add health analyzer unrevivability warning
- [32998](https://github.com/space-wizards/space-station-14/pull/32998) Removed the name "Hujsak"
- [33025](https://github.com/space-wizards/space-station-14/pull/33025) make ai speak robotically
- [32876](https://github.com/space-wizards/space-station-14/pull/32876) Extends the minimum round time for meteor swarm events
- [32786](https://github.com/space-wizards/space-station-14/pull/32786) Various Vaugely Connected Sprite Updates™: Encryption Keys, Station Map, Brig Timer
- [32212](https://github.com/space-wizards/space-station-14/pull/32212) Give proto-kinetic crushers, glaives, and daggers better inhands. Update the crusher and glaive icons
- [32291](https://github.com/space-wizards/space-station-14/pull/32291) Make the security belt contain more useful items by default
    - Sidetrack: Granades on sec belt go off with other granades, this should be looked at.
- [33018](https://github.com/space-wizards/space-station-14/pull/33018) Add 3 bottle boxes to nanomed plus
- [32720](https://github.com/space-wizards/space-station-14/pull/32720) Nukie med bundle now costs 24 tc and contains a unique defibrillator
- [33074](https://github.com/space-wizards/space-station-14/pull/33074) Pill Bottles can only store pills now
    - This was suggested to be reverted. Reason given:
Pill bottles are designed to also hold other tiny objects like cigarettes, bullets, credits, etc.
The same applies to cig containers. They're also supposed to be able to hold small things, like the disk, lighters, etc"
        - Decision: We keep it, look further at cigars boxes.
- [32363](https://github.com/space-wizards/space-station-14/pull/32363) Add a spare bible to PietyVend
    - This now lets you have infinite bibbles by refilling, may need a revert.
        - Decision: Keeping it for now
- [33078](https://github.com/space-wizards/space-station-14/pull/33078) Add notification for dependent wearables being dropped
    - Suggestion: Better if swapping a jumpsuit does not drop pockets/pda
- [32601](https://github.com/space-wizards/space-station-14/pull/32601) More pda space
    - Why does the pda need 8 programs?
        - This is a powercreep to allow someone to be able to get all programs.
    - Decision: See how it goes else reduce max PDA space in another pr.
- [33079](https://github.com/space-wizards/space-station-14/pull/33079) Carp Plush and Rehydratables can now be put into mop bucket
- [32820](https://github.com/space-wizards/space-station-14/pull/32820) ExaminableDamage now puts its message at the bottom and in color
    - Maybe should be moved below the description and above everything else... but also since its colored its more visible already.
    - Decision: Up to people who know ui design [who]
- [32953](https://github.com/space-wizards/space-station-14/pull/32953) Lower in-round votekick requirements
- [32528](https://github.com/space-wizards/space-station-14/pull/32528) Allow votekicks to be initiated in the lobby
- [29318](https://github.com/space-wizards/space-station-14/pull/29318) Muffins
- [33069](https://github.com/space-wizards/space-station-14/pull/33069) Borgs can no longer see mindshield + AI can no longer toggle off seeing job icons
- [32824](https://github.com/space-wizards/space-station-14/pull/32824) Minor antagonist guidebook changes
- [33053](https://github.com/space-wizards/space-station-14/pull/33053) Give Nukies a Hand Labeler
- [32490](https://github.com/space-wizards/space-station-14/pull/32490) Add cvars to votekick to customize requirements for the initiator
- [30443](https://github.com/space-wizards/space-station-14/pull/30443) Add on-call functionality for adminning
- [32458](https://github.com/space-wizards/space-station-14/pull/32458) Pills are explosion resistant
    - Sidetrack: Moths should be able to eat pills
    - Newmed sidetrack
- [32744](https://github.com/space-wizards/space-station-14/pull/32744) Hasten handcraft gauze recipe & decrease techfab gauze cost
- [31359](https://github.com/space-wizards/space-station-14/pull/31359) Service workers antagonist fix
    - Service worker needs to be looked at
- [33097](https://github.com/space-wizards/space-station-14/pull/33097) Adds a new AME sound effect
    - Maybe have a continuous hum?
- [33067](https://github.com/space-wizards/space-station-14/pull/33067) Adds headphones to loadouts
- [32743](https://github.com/space-wizards/space-station-14/pull/32743) Cardboard Box Capacity 4 -> 5
    - Sidetrack: Crates should hold at max 1 person or 0 people.
    - METAL GEAR
    - Cardboard boxes dont have a slowdown and its being abused by perameds
    - May be more funny to have 1 per box
- [33111](https://github.com/space-wizards/space-station-14/pull/33111) Combat and survival knife storage/inhand sprites
    - 5 tc??????????????????? IT USED TO BE 12???? Uh yeah look into that
- [32717](https://github.com/space-wizards/space-station-14/pull/32717) Collapsible ghost roles menu
- [33136](https://github.com/space-wizards/space-station-14/pull/33136) Added Popup for the Ligneous plant mutation when using hands
    - Reminder to unfuck botany
- [32945](https://github.com/space-wizards/space-station-14/pull/32945) make emergency lights (de)constructable
- [32887](https://github.com/space-wizards/space-station-14/pull/32887) Add Silicon Law cues to Every method a Silicon can have their laws change
- [33084](https://github.com/space-wizards/space-station-14/pull/33084) remove wanted list cartridge from captain PDA
- [32829](https://github.com/space-wizards/space-station-14/pull/32829) Rework the Flare Gun & add a Security Shell Gun
    - Maybe the sprite should be another color?
- [31292](https://github.com/space-wizards/space-station-14/pull/31292) Changes to "Burst" firemode; Drozd, WT550 and C20-r
    - Sidetrack: Safty toggle and bolts?
    - Throwing guns maybe should make them shoot

## Random discussions
- Species should not be limited from eating, but there should maybe be a warning before you eat something "dangerous". Or while you are eating it.
    - I wanna eat chocolate as a lizard :(
    - This just further proves we need a species design doc

## Other Notes
PJB kept screaming newmed during the stable review about 6 times now

Newmed fixes everything
Newmed fixes my merige

nya have a good day :3