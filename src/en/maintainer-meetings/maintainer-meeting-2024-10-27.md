# Maintainer Meeting (27 October 2024)

**Time:** 27 October 2024

```admonish info

**Attendees:**
- Vasilis (Myra)
- PJB
- Jezithyr
- Slartibartfast
- Slam
- Julian
- Chief Engineer
- KeronSHB
```

Notice: This meeting was recorded:

{% embed youtube id="8CcREpgDzRk" loading="lazy" %}

## Maintainer meeting topics

### How do we do hotfixing properly

https://github.com/space-wizards/docs/pull/322
    - Should we Cherry pick? How do we avoid commit spaghetti?
    - Should we rebase or squash merge?

PJB here explained git visually. With some ideas on how to handle it, Look at the video to see the drawing

Decided workflow:
1. Make hotfix PRs against stable
2. Get PR merged via maintainer approved
3. Make PR to merge stable into master, clearly explaining what hotfix is being merged in.

When done like this, the only commits in the stable->master PR should be a "merge branch stable into master" merge commit, and the hotfix(es).

### How to handle hotfix changelogs

To recap, changelog generation effectively works in two stages:
1. PR bodies are parsed when merged, and "part" files are put into `Resources/Changelog/Parts`.
2. These part files are consumed and merged into the main `changelog.yml` file.

PJB's idea was to reconfigure the changelog bot to only run the second step on `stable`. PR body changelogs would be switched to start committing part files only, and those would be consumed when they're merged into stable. Changes to the `changelog.yml` done on stable for hotfixes wouldn't conflict with changes to `master`, ideally. 

## Stable review
Summary of everything that isn't a bugfix or map change:
- [32465](https://github.com/space-wizards/space-station-14/pull/32465) Make APC UI work correctly with multiple users
- [32631](https://github.com/space-wizards/space-station-14/pull/32631) Qm external access
- [32629](https://github.com/space-wizards/space-station-14/pull/32629) Firebot Tweaks
- [32007](https://github.com/space-wizards/space-station-14/pull/32007) Increase AI Playtime Requirements
    - We should refactor all our playtimes, they are too high 
- [32779](https://github.com/space-wizards/space-station-14/pull/32779) Block emotes for sleeping
- [32736](https://github.com/space-wizards/space-station-14/pull/32736) Add poster about the SSD term
- [32253](https://github.com/space-wizards/space-station-14/pull/32253) Warden Hat Texture Change
- [32564](https://github.com/space-wizards/space-station-14/pull/32564) rainbow lizard plushie
- [32505](https://github.com/space-wizards/space-station-14/pull/32505) Cyborg module action icons
- [32762](https://github.com/space-wizards/space-station-14/pull/32762) organ sprite touch-ups
- [32309](https://github.com/space-wizards/space-station-14/pull/32309) Arcade Prize Additions
- [32565](https://github.com/space-wizards/space-station-14/pull/32565) Adds nitrogen to engi tank dispenser
- [32064](https://github.com/space-wizards/space-station-14/pull/32064) New reptile sounds
- [28075](https://github.com/space-wizards/space-station-14/pull/28075) FTL coordinate disk command for admins: ftldisk
- [28897](https://github.com/space-wizards/space-station-14/pull/28897) Several small SFX tweaks
- [32848](https://github.com/space-wizards/space-station-14/pull/32848) Added new Microphone instrument style "Kweh"
- [32854](https://github.com/space-wizards/space-station-14/pull/32854) enable ejecting in biogenerator UI
- [32625](https://github.com/space-wizards/space-station-14/pull/32625) Give AI a Sound Cue when an Antimov board is inserted
- [32851](https://github.com/space-wizards/space-station-14/pull/32851) Enhance Vending Machine UI: Adjust Minimum Height for better User Experience
- [32547](https://github.com/space-wizards/space-station-14/pull/32547) Change the window titlebar to show the joined server
- [28645](https://github.com/space-wizards/space-station-14/pull/28645) Sanitize shorthand emotes throughought the whole message
    - Needs hotfix (at the bottom) 
- [32563](https://github.com/space-wizards/space-station-14/pull/32563) Remove flares and shotgun flares from lathe options
- [32776](https://github.com/space-wizards/space-station-14/pull/32776) Set Salamander round restart time to 5 minutes
- [30359](https://github.com/space-wizards/space-station-14/pull/30359) Traitor activation fix for missing PDA
- [32323](https://github.com/space-wizards/space-station-14/pull/32323) ghost locator maints loot
- [32235](https://github.com/space-wizards/space-station-14/pull/32235) Add Towels
- [32750](https://github.com/space-wizards/space-station-14/pull/32750) Allow strip removing items if you're holding something
- [32858](https://github.com/space-wizards/space-station-14/pull/32858) Scalpels now cut like knives
- [32914](https://github.com/space-wizards/space-station-14/pull/32914) MMIs and positronic brains now talk like pAIs in plushies 
- [32422](https://github.com/space-wizards/space-station-14/pull/32422) Blunt damage will do stamina damage on wide attacks
- [32908](https://github.com/space-wizards/space-station-14/pull/32908) Reduce player softcap for wizden servers and panic bunker wizden Levi
- [32915](https://github.com/space-wizards/space-station-14/pull/32915) Mutetoxin buff
- [32906](https://github.com/space-wizards/space-station-14/pull/32906) prevent typing sound from playing when AI interacts with consoles
- [32929](https://github.com/space-wizards/space-station-14/pull/32929) Let station AI use long range fax machines
    - Should we make the ai have an intaraction blacklist instead of a whitelist?
- [32930](https://github.com/space-wizards/space-station-14/pull/32930) Ammo boxes now have sprites for being parially filled!
- [32112](https://github.com/space-wizards/space-station-14/pull/32112) Syringe gun!
- [32347](https://github.com/space-wizards/space-station-14/pull/32347) Adding intellicard functionality.
- [32441](https://github.com/space-wizards/space-station-14/pull/32441) Add Nuclear Cola centrifuge recipe
- [32849](https://github.com/space-wizards/space-station-14/pull/32849) In-hand apprasial tool sprite
- [31910](https://github.com/space-wizards/space-station-14/pull/31910) Visualized regions for NavMapControl

NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE 

To be considered to be merged before release:
- [32974](https://github.com/space-wizards/space-station-14/pull/32974) Fix playtime formatting
On master playtimes are currently formatted wrong and don't show up correctly when over 24 hours.
This is problematic since we and servers use playtime for whitelist purposes.
- [32997](https://github.com/space-wizards/space-station-14/pull/32997) Fix Bug With Uppercase Radio Keys
Due to a chat sanitation change the `:S` for the radio channel selection is currently interpreted an emote


## Aftermeeting stuff
- Use Github project more?
- Update codeowners