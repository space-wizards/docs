# Rogue Drones

| Designers | Implemented | GitHub Links |
|---|---|---|
| mirrorcult | :x: No | TBD |

<img src="https://tgstation13.org/wiki/images/0/09/Swarmer.png" width=64 height=64 style="image-rendering: pixelated"/>

## Background

rogue drones is kind of a placeholder name its not that good we can come up with something better or just call them swarmers who caaaaares

---

On some SS13 servers, an antagonist called the **swarmer** exists (or existed, as it was disabled in some places). It's goal was to destroy machines & structure around the station and convert it into material to create more swarmers with. Essentially grey goo. They had extremely limited combat capabilities (mostly traps & stuns) and are generally hated for being extremely annoying, disruptive, and overly centralizing.

**Drones** also exist on some SS13 servers, and even on SS14 for a time (disabled for being too much of an admin burden). They're not antagonists, and are intended to just be a little ghostrole that tries to repair the station and keep itself out of the way of the crew. Because of this, they end up being weirdly restrictive and almost like a separate part of the round entirely since they're forced to not interact with anyone.

This concept seeks to unify the two and solve the issues of both while creating an interesting grey-morality antagonist at the same time.

## Overview

**Rogue drones** are a mid-round ghostrole antagonist that can spawn in maintenance. 

They're space-capable silicons and quite fast, along with the ability to sneak under airlocks like mice, but have zero combat prowess and little bulk. They also can't interact with machines or speak, but can use the binary channel of the station to communicate with eachother. They come with a set of unremoveable tools that are quite powerful, as well as slots for metal and glass they can use to build structures. Using a decent bit of steel and wires, rogue drones can create another shell that can be inhabited and multiply, though they'll usually prefer to use that material to expand.

Their goal is well-defined and is simply to **increase the number of tiles on the station with habitable air by any means necessary**. This implies a couple things. Rogue drones:
- are incentivized to deconstruct walls and doors both to get materials and to create new openings for air, but they don't particularly care about touching structures or anything else useful. They're also willing to steal metal and glass directly if they find it lying around.
- goals sometimes align with the crew and are thus somewhat often **actually useful to the station**, as they're quite willing to fix hull breaches and tackle atmospheric issues.
- will often try to build useless rooms or expansions to the station, coordinating amongst themselves to store materials and collaborate, while negotiating with other silicons (who are also on their channel!)

The intended effects here are quite obvious but I will list them regardless:
- The crew, and individual crewmembers, have the interesting choice to think about ignoring or temporarily allowing the rogue drones to roam freely because of their aligned goals.
- Rogue drones serve the function that previous maintenance drones did--allowing players to get back into the round and learn or have fun with construction mechanics--while sidestepping the admin burden, since they're antagonists with limited capabilities.
- Rogue drones have a lot of the same gameplay as swarmers did--multiply, try to deconstruct and build new things, run from the crew--while not being overly annoying since they have negative incentives with regards to spacing areas or deconstructing machines, as well as not having any combat capability.
- With a clearly defined numerical goal, players feel motivated to have fun and actually perform their task and see the fruits of their efforts rather than just fuck off and do nothing
- A non-combat-focussed antagonist fills out the midrounds with some more actual variety in how players interact with them and makes everything more interesting

## Other Mechanics

At the end of the round (and periodically in the objectives screen), the game will calculate how many tiles of the station have habitable air, compare it to the station start amount, and award greentext based on that.

Rogue drones have a silicon lawset that guides their goals. The lawset is as follows:

```
    1. You must maximise the amount of tiles with breathable air.
    2. A tile with breathable air must have at least 20mol of oxygen and 20mol of nitrogen.
    3. A tile with breathable air must be between 60kPa and 200kPa of pressure.
    4. A tile with breathable air must be between 283K and 303K of temperature.
    5. A tile with breathable air must have below 0.1mol of gases dangerous to living creatures.
```

Rogue drones are subject to ion storm events the same as other silicons, so its possible for their laws and thus goals as antagonists to be changed dramatically! How fun.

Rogue drones have an innate air alarm tuned to the settings listed in their laws which makes it easy to check whether a given room meets the guidelines.

On a cooldown, rogue drones can use their built-in recyclers to spew out a certain amount of air to help with refueling rooms.

## Lore

Obviously not as important but the idea is something as follows:

Engineering drones are legacy NanoTrasen tech that was delivered to a few stations but rarely ever succeeded, so were generally phased out. Occasionally, a drone's decaying chassis, left in old maintenance tunnels, experiences a surge, powers back on and starts following its directives once again. Unfortunately, the legacy robotics department at NanoTrasen didn't care much for safety, so their laws leave a lot of room for incentivizing bad behavior--the decision to allow them to replicate wasn't so wise either.

### Possible future ideas

- Maybe a special RCD that can't deconstruct floors but can "eat" metal/glass to turn into ammo?
- Another way of creating rogue drone shells that is less swarmer-like?