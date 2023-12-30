# Maintainer Meeting (30 Dec 2023)

**Time:** 30 Dec 2023 18:00 UTC

**Attendees:**
- DrSmugleaf
- EmoGarbage
- Lank
- Bhijn
- Jezithyr
- PJB
- ElectroSR

## Replace reagent id strings with the reagent prototype | ElectroSR
- This is to avoid having to constantly fetch the prototypes whenever solutions are modified, which becomes important if we add more properties like boiling/freezing.
- Note that solutions already don't support prototype reloading for things like heat capacities.
- **When Electro (or smug) codes it**

## Making discussions not shorten my lifespan by several years | EmoGarbage
Discussions have gotten unquestionably worse and it makes me hate doing them ever. shit blows! poorly! low quality sloppy!
- Do we needback #bugs-feedback
    - Low-entry cost leads to low interest and lack of investment in discussions
    - Too fast-paced to actually manage any kind of sane discussion
    - Derails hard and frequently turns into circular discussions
- Keeping balance issues / suggestions / feature requests in github issues
    - People occasionally suggest controversial balance changes as github issues
    - These issues fly under the radar until someone makes a PR pointing at some random github issue that no one has given a look at
- Getting reliable feedback
    - Discussions devolve into pointless hearsay because we don't have good sources of info
    - Consider having some way for maints/admins/PMs to call upon the hordes to gather info in a timely manner
    - Consider querying admins for relevant in-game observations on topic
    - Can we get a private shared maint/admin channel i beg of you
- Organizing feedback
    - Secondary forums channel for compiling feedback on topics
    - Consider limiting to contributors or implement 30 second slowmode
    - Actually implement some decently high standards of discussion so it isn't just someone dropping in to say something sucks
    - Half the time i pop in to check out a thread the criticism is so vague that it literally just amounts to "remove all the changes" and you literally can glean 0 info out of it
    - Consider having some time limit on these so we can cut them off when they're still useful and get info out of them
- **Need a better way to get selective feedback (such as from admins)**
- **Round end survey**
- **Have GitHub issues only represent things we actively want**
- **Also check staff discord perms for #bugs-feedback**

## Do we add a new ComponentShutdownNoEntityShutdown event | metalgearsloth
- **When someone codes it**
- Make it not a pain in the ass to use without code duplication (demonstrate how it would be used)

## Cross-Server design | EmoGarbage
Mostly applies to MRP: players get upset when features designed for one mode aren't made with considerations for another.
- Features are primarily designed for LRP and frequently have little consideration of Space Law
- Gamemodes rely on mechanics like murder to trigger early round ends
- Higher skill-level servers stomp some antags because the balancing occurs on servers with lower average skill

Content that has caused issues between LRP/MRP:
- Revs and when the round should end (all are executed vs continuing the round)

## Early Access Roadmap
- **nothing on this roadmap matters except early access trailer.**
- A trailer for Steam
    - ask enrico about the trailer
- [**game admin items**](https://github.com/space-wizards/space-station-14/issues/23246)
    - [chat filter](https://github.com/space-wizards/space-station-14/issues/17313)
    - [rp whitelist automation](https://github.com/space-wizards/space-station-14/issues/23245)
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
