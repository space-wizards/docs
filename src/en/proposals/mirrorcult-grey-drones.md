# Grey Drones

| Designers | Implemented | GitHub Links |
|---|---|---|
| mirrorcult | :x: No | TBD |

<img src="https://tgstation13.org/wiki/images/0/09/Swarmer.png" width=64 height=64 style="image-rendering: pixelated"/>

## Background

On some SS13 servers, an antagonist called the **swarmer** exists (or existed, as it was disabled in some places). It's goal was to destroy machines & structure around the station and convert it into material to create more swarmers with. Essentially grey goo. They had extremely limited combat capabilities (mostly traps & stuns) and are generally hated for being extremely annoying, disruptive, and overly centralizing.

**Drones** also exist on some SS13 servers, and even on SS14 for a time (disabled for being too much of an admin burden). They're not antagonists, and are intended to just be a little ghostrole that tries to repair the station and keep itself out of the way of the crew. Because of this, they end up being weirdly restrictive and almost like a separate part of the round entirely since they're forced to not interact with anyone.

This concept seeks to unify the two and solve the issues of both while creating an interesting grey-morality antagonist at the same time.

---

I'm calling them **grey drones** here initially as an homage to grey goo and a reference to their position as antagonists which have more of a grey morality but I'm probably not going with this name for an actual implementation lol

## Overview

**Grey drones** are a mid-round ghostrole antagonist that can spawn in maintenance. 

They're space-capable silicons and quite fast, along with the ability to sneak under airlocks like mice, but have zero combat prowess and little bulk. They also can't interact with machines or speak, but can use the binary channel of the station to communicate with eachother. They come with a set of unremoveable tools that are quite powerful, as well as slots for metal and glass they can use to build structures. Using a decent bit of steel and wires, grey drones can create another shell that can be inhabited and multiply, though they'll usually prefer to use that material to expand.

Their goal is well-defined and is simply to **increase the number of tiles on the station with habitable air by any means necessary**. This implies a couple things. Grey drones:
- are incentivized to deconstruct walls and doors both to get materials and to create new openings for air, but they don't particularly care about touching structures or anything else useful. They're also willing to steal metal and glass directly if they find it lying around.
- goals sometimes align with the crew and are thus somewhat often **actually useful to the station**, as they're quite willing to fix hull breaches and tackle atmospheric issues.
- will often try to build useless rooms or expansions to the station, coordinating amongst themselves to store materials and collaborate, while negotiating with other silicons (who are also on their channel!)

The intended effects here are quite obvious but I will list them regardless:
- The crew, and individual crewmembers, have the interesting choice to think about ignoring or temporarily allowing the grey drones to roam freely because of their aligned goals.
- Grey drones serve the function that previous maintenance drones did--allowing players to get back into the round and learn or have fun with construction mechanics--while sidestepping the admin burden, since they're antagonists with limited capabilities.
- Grey drones have a lot of the same gameplay as swarmers did--multiply, try to deconstruct and build new things, run from the crew--while not being overly annoying since they have negative incentives with regards to spacing areas or deconstructing machines, as well as not having any combat capability.
- With a clearly defined numerical goal, players feel motivated to have fun and actually perform their task and see the fruits of their efforts rather than just fuck off and do nothing
- A non-combat-focussed antagonist fills out the midrounds with some more actual variety in how players interact with them and makes everything more interesting

### Possible future ideas

- Maybe a special RCD that can't deconstruct floors but can "eat" metal/glass to turn into ammo?
- Maybe some way to emit oxygen to try and fill rooms without relying on distro or atmos infrastructure in general?
- Another way of creating grey drone shells that is less swarmer-like?