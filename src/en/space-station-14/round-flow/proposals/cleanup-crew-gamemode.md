# Cleanup Crew
```admonish warning "Attention: Legacy Documentation!"
This document is ported from before the game-area reorganization and has not been reviewed or updated.
It may not fit with the new design requirements.
```

| Designers | Implemented | GitHub Links |
|---|---|---|
| mirrorcult | :x: No | TBD |

## Overview

Cleanup Crew is a lowpop (0-20 players) gamemode built around the concept of repairing destroyed stations from previous rounds. The goal is to provide a fun, relatively chill experience that differs from the base game but still interacts with all of its systems (especially construction, power, atmos, etc), acting as an educational experience, while also being very atmospheric.

The NanoTrasen Emergency Cleanup Crew, one spacemonth after the sudden abandonment of their finest new station, will start the game on a medium-large ERT shuttle near the disheveled station. The shuttle is stocked with everything you could need--lots of materials & RCDs, medical supplies, atmospheric supplies, generators, janitorial equipment, etc.

Each cleanup crew member has a designated role (atmospherics, power, repair, janitorial, security, etc) but they can of course branch into doing anything as needed with their supplies. The goal of the cleanup crew is to ensure:

- the station's tilemap is as close to the original station's tilemap as possible
- as many of the original tiles have viable air as possible
- the new station has as many of the same machines as the old station, and that as many of them are powered as possible
- as few spills, blood & dirt remain as possible
- as many "intruders" are eliminated as possible

The cleanup crew is given a time limit of 1-3 hours (depending on how large the map is & its chaos value), after which they must FTL away inconspicuously to evade detection by the Syndicate.

## Intruders

As mentioned before, the map is mostly kept unchanged from the saved version, but it *has* been a whole spacemonth!

It's possible that some hostile fauna (and some decorative flora for that rundown feel) have moved in. These can include:

- Xenos, which will have spawned resin walls and eggs randomly
- Spiders, which will have spun lots of webs and nests
- Carp & sharks, which will be scattered around the station with a dragon or two sprinkled around
- Orecrabs, with corresponding rock deposits that must be cleared out
- Nothing! No one got there before you did. A chill experience

Only one class of intruders is selected for the whole station, and they (along with any infrastructure they bring with them) are procedurally dotted around the station in clusters or in singular surprise instances.

The cleanup crew comes loaded with plenty of medical supplies and !!FUN!! pulse & powerful ballistic weaponry, so these aren't generally much of a real threat, but they do make for a more dynamic experience.

## Scoring

The cleanup crew, at the end of the round, is scored based on the factors mentioned above. The score is compared to how the original station would have scored, and some flavor text is displayed congratulating or disparaging the cleanup crew on their hard work.

## Map Saving Mechanic

To elaborate on how the maps are selected:

After any round finishes on some server, a quick heuristic "chaos value" (power, atmos, tiles missing) is calculated to evaluate how "destroyed" a station is. If the chaos value is high enough (but below a certain critical threshold of too much destruction), the map is saved, with some annoying entities removed (all mobs are replaced with skeletons, for example), and then stored as a blob in the DB to be used later.

Up to ~20 (maybe less, maybe more) stations can be saved at a time, and when a cleanup crew gamemode spawns, one is removed from the list and loaded in. If a map cannot be loaded, another is tried, until there are none left in the list. If there are no viable maps for cleanup, the gamemode is unavailable for play.

After the map is loaded, a short procedural pass spawning random mess decals and flora such as trees and bushes or vines is done. Afterwards, if an intruder (see above) was selected, they are spawned in as well.

Some scenarios, like a nuke going off after nukies, will mark the map as unable to be saved for cleanup crew, since it's obviously a bit too much of an outlier.