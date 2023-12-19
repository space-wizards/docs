# Maintainer Meeting (16 Dec 2023)

**Time:** 16 Dec 2023 18:00 UTC

**Attendees:**
- DrSmugleaf
- PJB
- EmoGarbage
- Faint
- Lank
- Visne
- ElectroSR
- notafet
- Julian
- Jezithyr
- chromiumboy

## Dump the wiki | metalgearsloth
- Originally never intended long-term
- I don't want to be forced into maintaining this
- Just link people github if they want something out of game
- **Add banner**

- **Possible solutions:**
    1. **Set up new site that is "the guide book, online". Current wiki keeps existing**
        * Preferably with a banner or something "use guide book for up-to-date info"
    2. Set up new site, kill wiki
    3. Make a system to automatically integrate guidebook content into the wiki

- **We're not stupid enough to delude ourselves into thinking anybody is going to step up to do (3) so lol**

## P5S | ElectroSR
- [P5S thread](https://discord.com/channels/310555209753690112/1153246232064569394/1184947317829287947)
- [Engine PR](https://github.com/space-wizards/RobustToolbox/pull/4693)
- Electro is making another PR to use arrays instead of 100 dicts
- **Please god PJB finish the better profiler infrastructure**
    - **Ability for maintainers to make profiles of game servers without bugging PJB**
    - **Benchmarking server, automated benchmarks**

## \<bikeshed Discord .NET library> for the server OOC relay | PJB
- It's easier to setup
- Will it add significant overhead
- **Do it**

## Better error monitoring system for game servers | PJB
- **Nobody checks grafana**
- **Checking Grafana sucks**
- **When PJB infrastructures it**
    - Pain and suffering

## Trailer 2 electric boogaloo | PJB
- **Ping maintainer and/or PM for feedback, send it in one message to Enrico and end the suffering.**
- how do we actually hold ourselves to it :godo:

## Admin Affecting Issues | CE
- Erase verb is broken in its current state. It fails to delete some messages if the target is spamming.
- Skeleton still sometimes spawn in nullspace or whatever it's called requiring admin intervention to fix.
- Replays are completely broken. Before they broke the seek bar was glitched and would fast forward/backwards indefinitely after you used it. Seems to have been following the mouse well after the user stopped clicking.
    - Send a message in contrib notifications or somewhere that old replays are (currently?) broken.
    - **Have a separate download in the repo for old launcher that works with old replays.**
    - Set up a steam beta for an old launcher for old replays?
- Adminhelp is often glitched and not showing specific players even if you can hear the ahelps being sent. You cannot right click player names in the ahelp menu.
    - Broken right clicks:
        - AHelp
        - F7 players tab
        - F7 objects tab
- There should be functionality for responding to ahelps through discord.
    - **Wow we already addressed the ahelp thing halfway**
- Vehicles break after going over ice requiring admin intervention to fix.
- Restart votes seem to be abused to determine whether there are admins on.
    - A fix to this could be allowing votes when admins are on but them having no effect.
- Add round numbers to ahelp (or to PDAs and call them shift numbers)

## Do we record maintainer meetings | Petalmeat
- **Have to ask all maintainers and PMs if they are comfortable with it.**

## Server hosting docs
- **Have a shorter docs page for people that want a server for only themselves or themselves+friends, link to it with a bot command.**

## Early Access Roadmap
- **nothing on this roadmap matters except early access trailer.**
- A trailer for Steam
    - ask enrico about the trailer
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
