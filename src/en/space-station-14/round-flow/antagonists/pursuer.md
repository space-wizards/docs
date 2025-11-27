# The Pursuer

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| SlamBamActionman | SlambamActionman | :x: No | TBD |

## Overview

The Pursuer is a midround antag focused on creating a short duration of high-intensity action for part of the crew, while keeping its overall station impact is relatively low. One crewmember is selected as the Pursuer's target and must evade capture long enough for the Pursuer to be killed, either via the assistance of other crewmembers or a natural timer on the Pursuer's end, while the Pursuer aims to kill and gib the target through various brute-force methods. The Pursuer is designed to be loud, intimidating and bulky, with a ramping strength that pushes towards an exciting climax.  

## Background

The Pursuer is derived from the original concept of the [Exterminator antag](https://docs.spacestation14.com/en/space-station-14/round-flow/antagonists/exterminator.html), which was also designed as a bulky single-target elimination antag. While the Exterminator was thematically appreciated it had certain features that encouraged playing in a way that ended up not being very engaging. Some of the issues identified with the Exterminator were:
- Its stealthy yet bulky features made waiting for Evac and jumping the target with a high-blunt weapon the easiest strategy.
- No mechanics were in place to keep it from going on a murder spree against the rest of the crew.
- Had very high specific resistances depending on its form that required knowing about them beforehand to fight effectively.
- Was very easily metagamed due to how it appeared on the station (random Passenger not on the manifest without ID). 

The Pursuer was born out of a desire to keep the single-target elimination while addressing the features above. As the name implies it focuses more on the chase itself and is intended to allow the target chances to actively escape. 

Part of its design was inspired by the multiplayer game Dead By Daylight, which has a similar focus on chase mechanics. With all the features that it ended up having the Pursuer ended up being styled after [Mister X from Resident Evil 2](https://en.wikipedia.org/wiki/Mr._X_(Resident_Evil)), being a huge bio-engineered super soldier with dead grey skin and piercing red eyes, hiding underneath a not-very-inconspicious coat and hat.

The antagonist has been playtested multiple times on Wizden via an admeme prototype, and has also been played on downstream servers with positive reception. 

## Features to be added

The Pursuer is a midround ghostrole antag that spawns in a random location in space near the station (similar to Space Ninja/Dragon). Upon spawning, the Pursuer is assigned a random player on the station as a target, notified to the player as an objective listing the target and its occupation.

The Pursuer has the following attributes and abilities:
- An always-on pinpointer that points towards the target.
- A slow but powerful wideswing punch.
  - The cooldown on the punch is relatively high, and while each individual punch may deal heavy damage, it DPS should end up being low.
  - Being punched should allow the hit party to escape; this can be achieved via making the punch inject hyperzine into the target.
  - The punch should also deal heavy structural damage to encourage the Pursuer to be destructive to the environment.
  - The punch damage scales with distance to the target, becoming weaker the further away the Pursuer is.
- A very fast and uninteruptable airlock prying.
  - Since the Pursuer does not have an ID and crew/AI will attempt to hinder it via closing and bolting doors, the prying is necessary to follow the target.
- High health/resistances and immune to several impeding status effects (stuns, slipping, cold, etc.).
- Initial slow speed that ramps up as damage is taken.
- A timer that ticks down gradually; the timer ticks faster the further away the target is.
- Unremovable infinite jetpack boots.
- Security comms and combat gloves.
- Inability to hold or pull things.
- Inability to speak (though can emote and scream).
- Big booming footsteps that can be heard from far away.

Upon spawning, the target player is given a pop-up message and ominous sound effect warning them that they have become hunted and should prepare. This message *must* be written such that it becomes clear to new players that they should seek assistance. While being hunted the target player, any shuttle the target is on is unable to start/launch FTL (noted as "FTL disruption detected" or similar in the shuttle UI).

The Pursuer's goal is to find and gib the target by repeatedly punching it, succeeding its objective when the target gibs and then automatically acidifies a few moments after. The target's goal is to survive until either crew manages to kill the Pursuer or the Pursuer's timer runs out, at which point the Pursuer acidifies.  

A key feature of the Pursuer's balance is its speed. The initial speed of the Pursuer should be slow enough that the target will have little difficulty running away, putting the onus on the Pursuer to facilitate coming closer to the target. This can be done by destroying walls, smashing windows or relying on other station issues to slow the target down or force them into a dead end. These destructive acts, along with the overarching goal, should force other crewmembers into acting by attacking the Pursuer (the Pursuer may even encourage this by attacking crew directly, though note that being distant from the target will make the punches weaker). Once the Pursuer takes damage it will gradually become faster and faster, first reaching a speed at which it can pressure the target better, and as damage increases it will become oppressively fast. When near death the Pursuer should be able to easily catch up to the target, though at that point being injured much further will cause death.

## Game Design Rationale

To summarize the Pursuer, it's essentially a lethal game of tag between two players. While the Pursuer and its target are the main actors in a Pursuer scenario, other crew assisting is encouraged and provides an event for players during the round. 
Overall the Pursuer is intended to be a *relatively* low-impact antagonist to the overall station, similar to a Space Ninja. With the loud footsteps, the target's pop-up and its low starting speed crew should have ample time to arm up and get ready to attack it, giving the station more control over how to deal with the antagonist.

There are multiple ways to combat a Pursuer; while running is the easiest, once the Pursuer has taken enough damage this will become difficult to rely on. Creating obstacles, bolting doors, taking speed-enhancing drugs, speedboots and assistance from other players are some emergent ways to prevent its progress. From playtesting we have seen creative acts such as throwing a crit target into a disposals bin, switching the target's body with another to confuse the Pursuer, going into tight hallways as a Mime and blocking it off, holobarriers and more.

The Pursuer is primarily a station-bound antag. Not only can the target not FTL away (unless it's Evac), but with its infinite jetpack it should be able to find and kill its target in space too. Careful balance must be made such that it doesn't completely dominate in space, but it should be empowered such that if the target goes into space with a jetpack, they will want to return back into the station again as soon as possible. Remaining in space against the Pursuer for a long duration should equal death.

## Roundflow & Player interaction

As a midround antag the Pursuer should come active sometime after the initial start-up phase of the game. It's not necessary for it to wait until the mid-late round since it benefits heavily from the station being in disrepair, so some variation in crew preparedness is likely desired. 

As a violent antag, players should not try to befriend it and it should not act friendly in turn (or at the very least, it should not try to *not* kill its target). To help with this the Pursuer is unable to speak and has a notably intimidating appearance. This is enforced by its timer and lethality; the Pursuer is allowed to ignore other players, and on the flipside with its distance-based damage scaling it should be hard for it to cause death to non-targets if it is not actively in chase.

Security will of course be the primary department to deal with this antagonist, though it does open up some opprtunities for other roles. The Paramedic with the rollerbed is often seen as a good choice for if the Pursuer crits the target, and passing through departments may help with navigating good paths. AI is encouraged to bolt doors in front of the Pursuer and open up pathways for the target, and of course any Passenger with a baseball bat is more than welcome to try bashing in the monster's head.

Some edgecases such as the target going cryo needs to be handled as well.

## Administrative & Server Rule Impact (if applicable)

Other than friendly antagging, I hope that the mechanics discourage murderboning non-targets enough that Pursuers refrain from doing it due to its inefficiency. There is a small possibility that the target and Pursuer player decides to work together for some reason, with the Pursuer staying near to get full punching power, but even then there is a time limit on how long the Pursuer can remain alive. Due to the slow punching speed and the effect it has (speed injection) it is naturally difficult to hunt down and kill multiple players at once.

## Further developments

While the Pursuer as described here has some features, it's still fairly simple when it comes to the tools at its disposal (mainly punching/prying). There are some possible additions that could be made to give the Pursuer some more options, though they are not deemed necessary for the antag's core functionality:

- Punching pushes players and objects, dislodging and moving them away from the Pursuer.
  - This has been tested and helps with crowding crew ganging up on the Pursuer, though it can make the Pursuer very strong in space or when the target has been crit.
- A rush move, giving a short burst of speed in one direction. This could be combined with a strong pushback and/or structure damage.
  - Sometimes the slow start can feel a bit *too* slow. Giving a burst of speed could help the Pursuer keep up but likely isn't actually good enough to catch the target.
- A loud scream that pushes back and stuns players in a circle around it.
  - Should be followed by a large slowdown, most likely. Could help when the Pursuer is very crowded, though might not make much of a difference...
- A healing action that, after a channeled doafter, provides the Pursuer with some amount of health. This should be a one-use action.
  - Gives the Pursuer an opportunity to heal, which helps cause a lull in the action for the chased target as it disappears away from the crew.
- Pop-ups when the Pursuer takes damage, providing flavor-text that it is breaking apart.
  - It can be hard for crew to see that their attacks are actually doing anything, since the Pursuer only gets faster and faster. The pop-ups could provide some progression for the crew and indicate that they are injuring it.

# Technical Considerations

There are a few features that need to be supported (FTL prevention, pinpointer for a random crewmember, damage scaling based on distance) but these are easily separated into components. Otherwise a lot of the Pursuer can already be done via yaml.
