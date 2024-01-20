# Maintainer Meeting (20 Jan 2023)

**Time:** 20 Jan 2023 18:00 UTC

**Attendees:**
- DrSmugleaf
- PJB
- Lank
- Julian
- Jezithyr
- faint
- EmoGarbage
- ShadowCommander
- Chief_Engineer

## Consolidating admin logs | metalgearsloth
- **Basically log categories**
- Make it backwards compatible
- When you code it
- [Discord message](https://discord.com/channels/310555209753690112/900426319433728030/1197878030253707346)

## PRs for admin usage prototypes | metalgearsloth
Deny all PRs for admin usage prototypes:
- We have admin uploads
- Bloats the repo with meme content that's never used anywhere and requires ongoing maintenance
- Do we dump it on the admin repo
    - **No**
- **Allow admin-usage prototype PRs to the main repo**
- **Mark admin-only prototypes with an "Admin" suffix and admin-only category**
- **Have a test that checks that admin-only prototypes aren't mapped in**
- **Lower standards for reviewing, but don't allow copyrighted stuff to be on the main repo**
- **Anything that is supposed to be secret can stay in the admin repo**
- **Put them in a separate folder with a text file that clarifies to downstreams that they may be removed at any time**
- **If one of them breaks during a refactor it is fine to remove it**

## Code freezes | EmoGarbage
- We are extremely inconsistent about what a freeze means
- We dont actually enforce them in a consistent way
- We should outline what needs to be done for the freeze to end because leaving some vague criteria up in the air sucks
- [Current freezes](https://github.com/space-wizards/space-station-14/issues/8524)
- Current conditions:
    - Maintainer approval will be required beforehand.
    - If the freeze is due to an ongoing rework then the rework PR will take precedent and your PR may require reworking prior to merge.
    - A design doc may be required depending upon the content. For example, a new item may not require a design doc, but a new antagonist will require one.
    - The PR will be scrutinised more than normal and will take longer to be reviewed.
    - As usual your PR is subject to not being merged into the repository, especially if maintainer approval is not sought beforehand.
- **Reword "freezes" to be clearer.**
    - Scrutinized?
    - **Restrictions**
    - Something for rework coming soon.
- **Have a separate thing for freezes that won't be accepted at the current time.**
- **We can review current freezes/restrictions after every maintainer meeting**
- **We need a list of things that can be ported as-is from SS13**
- **Define beginner-friendly PRs better vs first codebase PR**
    - We have a label, but it hasn't been managed well. The current ones are either outdated or harder than a first PR should be.

### Lobby songs freeze
- They take up too much space compared to the rest of the repository
- Do we stream them
- Do we have a CDN
- Do we have them on a separate repo
- **We stream them**
    - WYCI
    - Allow clients to fire HTTP requests in content (in a way that you don't make the client a botnet)
    - Not on the local network
- **Keep them frozen until that system is implemented**


## Current admin issues
- Ahelp relay does not tell you whether the player has disconnected or not. [23716]
- Ahelp window should tp you to the last character if the player is disconnected [20189]
- Specific admin actions can only be performed on logged in players(e.g. Erase) [23796]
- ASN bans (CE will make epic insanely detailed issue soon™️)
- Ghost roles need to have clearer descriptions so people stop getting bwoinked for being friendly antags [24333]
- A command to force a round type/map temporarily instead of putting it on perpetually as it works currently

## Early Access Roadmap
- **nothing on this roadmap matters except early access trailer and admin issues.**
- A trailer for Steam
    - ask enrico about the trailer
- [**game admin items**](https://github.com/space-wizards/space-station-14/issues/23246)
- gamemodes/antags
    - dynamic [c#16548](https://github.com/space-wizards/space-station-14/pull/16548)
    - wizard
- Steam account linking
- The game runs like shit how do people play this
    - "IDK but maybe when I fix the watchdog you can figure it out easier" | 09/09/2023
    - "I only played VRChat since last time and VRChat runs like shit so I don't know how people play this" | 23/09/2023
    - "" | 21/10/2023
    - Miros runs fine | 16/12/2023
        - I am 5 parallel universes ahead of you
    - We have a new Minecraft server it runs fine now (SS14 runs fine, really)
    - Here lies Minecraft long live Satisfactory

Crashes / Critical bugs: (when are we moving these to GitHub)
- Crashes the server reliably.
- Something that bricks your client often (needs a client restart).
    - Example: Blackscreens the client until you reconnect.
- If something ruins the round and is disabled because of it.
    - Example: Communal lung bug.
      => till next time
      like and subscribe
      smash that button
      ~~did you know only 6% of contribs join this meeting?~~ According to YouTube's statistics,

## PJB personal roadmap
- Audio rework DONE NO WAY
- Fix infra
- Watchdog rework: testmerges, **better way to get traces from game servers**
- Fix perf oh god
- PJB is reading about window scaling
