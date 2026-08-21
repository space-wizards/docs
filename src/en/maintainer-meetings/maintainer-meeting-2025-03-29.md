# Maintainer Meeting (29 March 2025)

```admonish info
- Myra
- Errant
- Simyon
- ScarKy0
- Julian
- PJB
- Milon
- Slam
- Chromium
- Orks
- Slart
```

This meeting was recorded:

{% embed youtube id="Gcy9ZeqQcYc" loading="lazy" %}

## What do we do about fixing UseDelays (metalgearsloth)
- Resetting the default ID is baked into every interaction which means you can't actually use your own ID as it will just fallback to the default.
- Do we just have subscribers check for .TryResetDelay / .IsDelayed themselves?
- Removing this will probably break a lot of things.
- I was just trying to fix the storage UseDelay and realised it's just not possible atm.

<br>

Undiscussed due to no one knowing about `UseDelays`

## Freeze new event shuttles until we got incremental grid loading (Slart)
- Right now ALL event shuttles get spawned at the start of every single round, adding a ton of entities of which most are never used, since only 1 or 2 shuttles are randomly used each round. 
- This was originally done to prevent the server from freezing for a short moment when spawning shuttles, but the shuttle count has drastically increased since then. 
- The freeze would be lifted when we make shuttle loading incremental so they can be spawned without lagging the server. 
    - There are a few PRs for admin-only shuttles and I would have to check if these are preloaded as well. If not, then they would be exempt from the freeze. 

<br>

- Turns out it only is an issue for ghost role shuttles?
    - We should implement incremental map loading and grid loading.
        - This means freezing ghost role shuttles *SPECIFICALLY*
    - Simyon also wants them to have something like missions since they are just a "Respawn"
        -  or to remove em fully for a refactor.

## Plan about April fool's (Myra)
- So afaik the April fool's branch is currently handled by Milon and Scar
- When should we put a stop to April fool's prs?
    - After stable merge (tomorrow)
- Should vulture be put into the April fool's branch for the duration of the April fool's event? Or let it run on master (without April fool's content) as usual?
    - No for the below reasons (a server spared from the fun)
- How do we return to stable? We can't publish the same version twice to my knowledge. We can commit something random.
    - 3 days

<br>

- Define policy for april fools branch (when, how long?, what extend?, what servers?)
- Wow this topic went on for longer then i thought

## Not-so-hotfixes (Slam)
- We've had two PRs that were marked as hotfixes for ~2 months.
    - https://github.com/space-wizards/space-station-14/pull/35087
    - https://github.com/space-wizards/space-station-14/pull/34948
        - Both need review accoridg to Slart
- What is our procedure for hotfixes that aren't hotfixed? Are they hot or not?
    - Please make sure you notify maintainer when a hotfix is made
    - If a review is needed, ensure the author is aware of the review
    - Let the author communicate when they did the review
    - Have a time limit 
        - MAINTAINER BOT?

## Stable review
- [35701](https://github.com/space-wizards/space-station-14/pull/35701) Update Space Law to reflect Implant changes
- [35823](https://github.com/space-wizards/space-station-14/pull/35823) Enable antag-before-job rolling for roundstart antags
- [35306](https://github.com/space-wizards/space-station-14/pull/35306) Added Bacchus' Blessing Drink
- [35318](https://github.com/space-wizards/space-station-14/pull/35318) Corrupt borg speech if they are damaged or low power
- [34578](https://github.com/space-wizards/space-station-14/pull/34578) Reduce base electrocution stun time from 8 to 5 seconds
- [34095](https://github.com/space-wizards/space-station-14/pull/34095) NanoTask
- [35326](https://github.com/space-wizards/space-station-14/pull/35326) Take 2: Rename ammunition box (.50), Liberation Station .50 stock
- [35856](https://github.com/space-wizards/space-station-14/pull/35856) Puddles on the floor sticking to the walls
- [35838](https://github.com/space-wizards/space-station-14/pull/35838) Paradox clones get all storage items the original has.
- [35829](https://github.com/space-wizards/space-station-14/pull/35829) make paradox clone receive the original's objectives
- [35888](https://github.com/space-wizards/space-station-14/pull/35888) Increase storage size of Syndicate Backpack
- [34929](https://github.com/space-wizards/space-station-14/pull/34929) Chameleon vests now act like winter coats
    - Monitor it
    - Preferbly will only work as a winter coat when its a winter coat
- [35906](https://github.com/space-wizards/space-station-14/pull/35906) Paradox Clones receive the implants the original has
- [35898](https://github.com/space-wizards/space-station-14/pull/35898) Killer tomatos take damage from weedkiller and plantbgone
    - Offtopic: They should have a dead sprite
- [35909](https://github.com/space-wizards/space-station-14/pull/35909) Paradox Clones spawn with their suit sensors off
- [35144](https://github.com/space-wizards/space-station-14/pull/35144) Smite Vendor Restock and General Soda Machine Balance
    - There are too many drinks
        - The bartender should still have SOMETHING to do
    - Monitor it
- [35901](https://github.com/space-wizards/space-station-14/pull/35901) Renaming the "Mime Cap" to "White Cap"
- [35830](https://github.com/space-wizards/space-station-14/pull/35830) Metagame improvements to antag-before-job selection system
- [35937](https://github.com/space-wizards/space-station-14/pull/35937) Donk Co. Microwave heats twice as fast
- [35323](https://github.com/space-wizards/space-station-14/pull/35323) snake can now be seen inhand and worn on neck like friend
- [35125](https://github.com/space-wizards/space-station-14/pull/35125) consistent grapes
- [35925](https://github.com/space-wizards/space-station-14/pull/35925) Fix recipe and animation for copypasta
- [35151](https://github.com/space-wizards/space-station-14/pull/35151) inhand sprites for Produce
- [35433](https://github.com/space-wizards/space-station-14/pull/35433) Add In-hand Sprites for miscellaneous items
- [35702](https://github.com/space-wizards/space-station-14/pull/35702) Mail Bag
- [33676](https://github.com/space-wizards/space-station-14/pull/33676) some robotics inhands
    - Wow we have a lot of inhand sprites
    - https://github.com/space-wizards/space-station-14/issues/35943 This got brought up
- [35834](https://github.com/space-wizards/space-station-14/pull/35834) Removed the heat damage from disablers and disabler SMGs
    - Pacifists should be made to be able to shoot these
        - Put it up on vote
- [34984](https://github.com/space-wizards/space-station-14/pull/34984) Medical Item In-Hand Sprites
- [35820](https://github.com/space-wizards/space-station-14/pull/35820) Support separate displacement maps for left and right hand
- [36075](https://github.com/space-wizards/space-station-14/pull/36075) Make pow3r validation logic available on release.
- [36079](https://github.com/space-wizards/space-station-14/pull/36079) Enable parallel Pow3r solver on Vulture
- [36039](https://github.com/space-wizards/space-station-14/pull/36039) A Bunch of New Figurine Voicelines
- [35622](https://github.com/space-wizards/space-station-14/pull/35622) Admin Overlay stacking and ghost hiding
- [19460](https://github.com/space-wizards/space-station-14/pull/19460) Add smuggler stashes
- [35940](https://github.com/space-wizards/space-station-14/pull/35940) Show paradox clones in deadchat
- [35910](https://github.com/space-wizards/space-station-14/pull/35910) Fix faction icons for paradox clones
    - Should they count as "required to kill" on the nukeops gamerule?
    - They should be given to freedom to either silently join the nuke ops team or go against the nukeops team and help the crew
- [36003](https://github.com/space-wizards/space-station-14/pull/36003) Raw meatball cooks into cooked meatball
- [36105](https://github.com/space-wizards/space-station-14/pull/36105) Add paradox clone to admin antag control
- [35004](https://github.com/space-wizards/space-station-14/pull/35004) Updates to Hydroponic sprites
    - I *think* we overrode some of the other sprites someone else made above, get an arttainer to short this out.
- [36104](https://github.com/space-wizards/space-station-14/pull/36104) Add a new poster


### Urgent Marked
- [35985](https://github.com/space-wizards/space-station-14/pull/35985) Fix 1x1 storage windows
    - Merg

woof
