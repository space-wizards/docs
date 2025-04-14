# Maintainer Meeting (23 November 2024)


**Time:** 23 November 2024

```admonish info

**Attendees:**
- Vasilis (Myra)
- PJB
- Errant
- Julian
- faint
- Slam
- Slarti
- Keron
```

Notice: This meeting was recorded: 

{% embed youtube id="VUykffqo8Co" loading="lazy" %}

## Test server

- V U L T U R E?
    - Sure!
- Is it a priotity given recent project occurrences?
    - Meh not really too hard to do, can't hurt.
- Requirements
    - Additions to game server to make it more clear that it's a test server
    - Popup when first joining server, bright yellow box in lobby UI? Something like that.
    - "You are playing on the test server! You'll get features first but beware bugs! This is how you can report them" that sorta thing.

- How to do it
    - Make a new publish workflow, do NOT run Discord/RSS Changelog pushes
    - PJB adds new fork to Robust.Cdn
        - Damn I am so glad I added this feature to Robust.Cdn :godo:
    - PJB configures Vulture watchdog to point to new fork.
    - Probably docs update on hosting tutorial too.

## Big congrats to the triage team!
- They have managed to triage all prs and issues!!
- WOOO

## PLEASE DO ADMIN PRS :3
- Yeah thats it
- https://github.com/orgs/space-wizards/projects/8

## Topics? What are those?
- Im filling the tables

## Should we review stable prs in game in meetings?
- Like someone just opens the game in the meeting to show off the features instead of showing off the link and going "sure" or "no"
    - Anything minor does not need to be reviewd like this
    - This should have been done ahead of time anyway in the review thread and before the meeting
    - Conclusion: We aitn doin it

## Stable review
The usual list of everything that is not a bugfix, refactor or mapping change (full commit list [here](https://github.com/space-wizards/space-station-14/commits/staging/))
- [31710](https://github.com/space-wizards/space-station-14/pull/31710) dark green jumpsuit recolor, casual green jumpsuits added
- [32954](https://github.com/space-wizards/space-station-14/pull/32954) Add a Walking alert
- [33096](https://github.com/space-wizards/space-station-14/pull/33096) The Jumpsuit Re-Detailening
- [33198](https://github.com/space-wizards/space-station-14/pull/33198) Intellicards now have a doAfter
- [32989](https://github.com/space-wizards/space-station-14/pull/32989) Removed bola stam damage
- [31492](https://github.com/space-wizards/space-station-14/pull/31492) Goliath rebalance
- [33113](https://github.com/space-wizards/space-station-14/pull/33113) improve BiomeDunGen
- [33176](https://github.com/space-wizards/space-station-14/pull/33176) Adds new sprites for shotgun shell boxes
- [33223](https://github.com/space-wizards/space-station-14/pull/33223) Added the ability to microwave inert flesh anomaly cores to turn into an anomalous meat mass
- [33282](https://github.com/space-wizards/space-station-14/pull/33282) Window sprite tweaks 
- [33201](https://github.com/space-wizards/space-station-14/pull/33201) Ethereal Jaunt Spell for Wizard & Jaunt ECS
- [33160](https://github.com/space-wizards/space-station-14/pull/33160) Half Revert [#31978](https://github.com/space-wizards/space-station-14/pull/31978)
- [32586](https://github.com/space-wizards/space-station-14/pull/32586) Borg type switching
- [32985](https://github.com/space-wizards/space-station-14/pull/32985) Add succumb action 10 sec delay
    - Should be revisited after newmed
- [33167](https://github.com/space-wizards/space-station-14/pull/33167) Adds gorilla gauntlet storage sprite and updates hit sound
- [33101](https://github.com/space-wizards/space-station-14/pull/33101) Improve crayon UI to not be stuck in 1996
- [33341](https://github.com/space-wizards/space-station-14/pull/33341) BRB sign in the Bureaucracy Crate
- [33019](https://github.com/space-wizards/space-station-14/pull/33019) Solar assembly crate buff
- [31761](https://github.com/space-wizards/space-station-14/pull/31761) Add admin remarks button to character editor
    - Unrelated: Lobby UI needs a cleanup anyway
- [33318](https://github.com/space-wizards/space-station-14/pull/33318) Adds paper label visuals to closets and lockers
- [32692](https://github.com/space-wizards/space-station-14/pull/32692) Wizard Summon Guns/Magic
- [33383](https://github.com/space-wizards/space-station-14/pull/33383) Dim light bulbs
- [33379](https://github.com/space-wizards/space-station-14/pull/33379) Shift air alarm sprites to better reflect their direction
- [33400](https://github.com/space-wizards/space-station-14/pull/33400) Increase softcap back to 80
- [32706](https://github.com/space-wizards/space-station-14/pull/32706) Remove drag & drop dropping items from containers
- [33417](https://github.com/space-wizards/space-station-14/pull/33417) Crew monitoring crate updated to contain flatpacks, science access instead of engi
    - Perhaps give it medsci perms?
- [32577](https://github.com/space-wizards/space-station-14/pull/32577) Construction menu grid view
    - Unrelated: Favs apparently dont save? pls
- [33376](https://github.com/space-wizards/space-station-14/pull/33376) Coloured Light Cost Reduction
- [33147](https://github.com/space-wizards/space-station-14/pull/33147) Coal presents and chrimmas tree options. Presents no longer itemify
- [33128](https://github.com/space-wizards/space-station-14/pull/33128) Gas pipe sensors
- [33358](https://github.com/space-wizards/space-station-14/pull/33358) Temporarily make singularity a bit harder to loose as non-antag
    - This was marked as "temporary" since it may prevent certain antag gimmicks. We should look back at this in the feature

## Other
- Potencially hotfix oasis chrimas

## Other notes
- Myra before you publish the maintainer video please see the notes on your alt 