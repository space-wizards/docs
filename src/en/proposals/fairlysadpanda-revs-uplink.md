_Operative: you will be going deep undercover at the new Nanotransen research lab we have uncovered in the sector. Your objective is to seize control of the space station from those unsuspecting fools so we may use it and its crew for our own ends. Compromise their chain of command and use their identification to destroy their security systems contained in their Uplink Terminal. You may use any method at your disposal to achieve this end. Be aware that Nanotrasen security teams are sufficiently armed to pose you difficulties if your objective is discovered too early._

_Good luck, operative. Long live the revolution._

# Revolutionaries 2.0: The CentComm Uplink Console

| Designers                      | Implemented | GitHub Links |
| ------------------------------ | ----------- | ------------ |
| Hannah 'FairlySadPanda' Dawson | :x: No      | TBD          |

# Overview

Revolutionaries is a classic Space Station 13 game mode, updated and revised for maximum chaotic fun. A cabal of Head Revolutionaries, specialist infiltrators from the Syndicate, have sneaked aboard the Space Station. Their job: deliver the space station into Syndie hands.

To do this, the Head Revolutionaries need to compromise the central security framework that controls and monitors the space station. This is done by obtaining, by any means, one or more Department Head IDs, breaking into the bridge, and hacking into the CentComm Uplink Terminal. After a timer, shortened each time a new Head ID is inserted into the machine, the Revolutionaries gain complete control over the station and win the round.

If the Head Revolutionaries are neutralized before this happens, CentComm will send a dismissable emergency shuttle to pick up the crew.

## Background

The current Revolutionaries game mode ("Revs") as implemented is a problematic game mode that has lead to:

- Repeated revisions to anti-metagaming rules, via both SOP and Space Law
- A large number of complaints and discussions about improvements on Discord including, but not limited to:
  - Revs causing a murderhobo tide that Security has to fight with murderhobo violence
  - Boring stalemates and unclear round state, especially for the loyalist crew
  - The endless feels-bad forced round-removal of discovered Head Revs and Heads Of Staff, sometimes for over an hour
  - Paint-by-numbers round activities entirely focussed on flashes and MindShield implants.
- Drain on Admins, both due to players demanding ERT revents in response to a discovered revolution and rules enforcement.

Revs is badly in need of a refactor to encourage a more dynamic round that encourages paranoia from Security and smart play from the Revolutionaries. This document forms one half of the "Revs 2.0" refactor, alongside a to-be-written replacement of the Flash/MindShield conversion game mechanics. For the original overview document, [see here](https://github.com/space-wizards/docs/pull/132).

# TL;DR

The current "kill all Heads" win condition for Revolutionaries is replaced.

The bridge Communications Computer is upgraded to a Centcomm Security Uplink terminal.

This terminal is pretty hard to destroy, internally-powered, bolted to the floor and very heavy. If the terminal somehow gets destroyed (a Singuloose, immovable rod, etc) then CentComm will detect this and dispatch the needed machine board to make another to the trade station.

This Computer works like a Communications Computer, but represents the station's connection to CentComm. This connection can be switched off by inserting one of a set of keycards: one of the original Department Head IDs (but not the Captain's spare). This starts a timer. Each additional Head ID reduces this timer. The timer can be disabled by accessing the terminal and cancelling it.

If this timer expires, and it's a Revs round, the Revs win. Even if it isn't, all cards on the station automatically become All Access.

# The Rules

One or more Head Revolutionaries are spawned from the usual pool of players who have opted-in. These Head Revolutionaries have one specific goal: deliver the station, mostly-whole, into Syndicate hands.

- To deliver the station into Syndie hands, the Bridge must be taken over with the **CentComm Uplink Terminal** given at least one Head ID. This triggers a countdown until the uplink is severed and the Revs win. Doing so results in a major syndicate victory and the round ending. Each Head ID input after the first reduces the countdown.

- A draw is achieved if the round ends with no Heads escaping to Centcomm

- A minor crew victory is achieved if the round ends with an evac and at least one Head escapes to Centcomm.

- A major crew victory if all Head Revs are neutralized, either by death, inprisonment or neutralization\*. If this occurs, all Rev members of staff de-convert and Centcomm (belatedly) detects the mind control rays being blasted at the station, sending an evacuation shuttle and allowing the round to end. (If the surviving chain of command wants a longer round, the shuttle can be recalled).

Depending on the Station map, Revolutionaries may not be able to be rolled that round. This reflects mapping progress (if the map has been updated with an Uplink Terminal) and also if the map has a good-enough defensible location for the Terminal to be placed in. However, this will need lots of play testing to determine.

If the Flash/Mindshield meta still exists, the rules for confirming a Revolution are extended to include an attempted unlinking of the space station. There are no other special rules that admins need to worry about in this mode: however, deliberately destroying the Uplink Terminal or deliberately unlinking it from the Station's grid and flinging it off into space so as to make it largely impossible for the Revolutionaries to win is plausible and may cause ahelps.

_\*A 2.0 implementation of the Rev conversion mechanics should/must have a way of neutralizing the Head Rev conversion ability, allowing them to remain in the round._

# The Uplink Terminal

The **Centcomm Uplink Terminal** is a very tough computer console that lives somewhere on the ship. It's generally assumed it lives on the bridge, but it's actually mapper's choice where it goes. However, some general suggestions are:

1. The location should be in an important room, as it represents the core security nexus for the entire station.
2. The location should be somewhat defensible, or easily convertable to being so with some supplies to create barricades and walls.
3. The location shouldn't be directly accessible by Security, as this makes attacking it and defending it a bit too easy for that department.

Note that this sort of traditional attack/defend level design is not that normal in mapping, so it's OK if one station or another is more easy or more difficult to defend. As noted in [the rules section above](#the-rules), some stations might be found to to simply not have a good location to add an Uplink Terminal to.

## The Fluff/The Lore

The Uplink Terminal is the computer responsible for talking to CentComm. It's where CentComm messages come in to when sent, and where CentComm sends crew manifests, security information, and other important information to. The Terminal is responsible for setting up door access before the crew starts their shift. It also reports back metrics to CentComm like "what's the alert level", "where is the station at the moment" and "is the station in tiny bits".

The existence of these terminals and the ability to transfer control of stations between security systems is due to a right-to-repair clause in Space Law to prevent old space stations from going to waste. Nanotrasen's used this law to repurpose such popular space stations it's found (floating adrift in deep space) as Barratry.

During rounds, it's the fancy way of sending communications. It's like when a captain in a Star Trek episode needs to stand somewhere on the bridge to send a message to the crew to abandon ship or something.

## The Terminal Is Robust

The terminal is really hardy. It's an indepentent computer structure which is indepentently powered and has a high amount of structure damage resistance. It can't be broken into with tools or unanchored with tools. Essentially, it's as hardy as CentComm can reasonably make it. It can still be nuked, eaten by a singuloose, and so on.

## (It is not infinitely robust)

If the terminal is destroyed (except by nuke) then CentComm will send an automated annoyed message to the crew and send a replacement computer board to the automated trade station. This is absolutely a way that the Revolution could game the system, but considering that they'd need to do something very drastic to do so...

## Gameplay Role

The Terminal if de-linked from CentComm or destroyed will cause all security systems on the station to offline, meaning all IDs become AA.

The Terminal can be used to send communications and set alert levels just like a Communications Computer. Its robust nature means it's also a reliable place to call the shuttle from.

The Terminal monitors the existence of the Head ID cards. Anyone can look at the terminal and know how many of the IDs are still "in play" - i.e. not destroyed or unreasonably far from the space station for recovery.

In Revolutionary rounds, the Terminal can be exploited by a Head Revolutionary to initiate an unlinking sequence. This unlinking sequence works as follows:

1. The Head Revolutionary gets at least one Head ID card.
2. The Head Revolutionary breaks into the room with the terminal in it (probably the bridge).
3. The Head Revolutionary\* inserts the ID card into the terminal.
4. The Head Revolutionary waits through the timer.
5. If the Head Revolutionary has any more Head ID cards, they can insert them to decrease the length of the timer.

This timer blares out a warning that the station is being unlinked when the timer starts, with the time remaining. If the time remaining is modified (by inserting more ID cards), this is also announced.

Any crew member can stop the countdown by interacting with the terminal and clicking a big obvious red flashing button on it. This stops the timer\*\*.

If the timer reaches zero, the Revolutionaries win and a round restart is called. The Head Revolutionaries exploit the console to disable all security ~~ready for the Syndicate to show up~~ to free the crew from their corporate overlords and install themselves as "Consuls" of the station\*\*\*. Remaining living department heads and security officers are renamed "Enemies of the Revolution" and are ultra-valid, although given that the game is in end-of-round the murder has probably already started.

_\*Revolutionaries can insert cards. It's also possible that they could activate the timer, but this needs playtesting._

_\*\*The timer might reset to its starting value or might hold its starting value, so if restarted it continues counting down. This needs playtesting._

_*Consul is the Roman term for an elected political leader - other names could be overseer, overlord, operative...*_

# Head ID Cards

Each time a department head spawns, they spawn with a special ID. This special ID has a big obvious chip on it that can be seen by examining the card. This chip is missing from "spare" IDs and not even the HoP can make new ones.

The Head ID Cards are tracked by the Centcomm Uplink Terminal, so the state of the round can be known (is an ID inside the terminal, on the station, destroyed or out of range?).

If every single Head ID Card has been removed via distance or destruction, the Uplink Terminal will notice and a _very annoyed_ CentComm will send a master override ID to the automated trade station. This Uplink Override ID counts as the Captain's ID.

The following department heads have a Head ID Card:

- The Captain
- The Head of Personnel
- The Head of Security
- The Research Director
- The Chief Medical Officer
- The Quartermaster

# Important Patches To The Rev Gamemode That Should Go Alongside This Refactor

1. Head Revs are not shown as Head Revs to other Revs. This means a de-Revved crewmember has a slightly harder time IDing them.
2. Head Revs have access to the Syndicate radio channel for the purpose of co-ordinating with other Head Revs. This prevents the 1.0 problem where Head Revs would mill about without good direction, leading to boring rounds with early Rev identification by Security.
3. (If the Flash/Mindshield meta is still used) A limited number of Mindshields is available from CentComm at any one time. This means that a good loyal Cargo crew cannot end the round rapidly if the Revolution is discovered. After ordering a few, CentComm will need time to make more.

# Gameplay Notes

This round type is supposed to encourage a simple and clear round flow for both sides (Sec and the Revs). This flow is as follows:

1. The Revolution grows and plots. During this time, the Revolution can easily be stamped out, so the Head Revolutionaries play cautiously.
2. The Revolution is strong enough to seize a few Head ID cards. They don't need all of them, though.
3. The Revolution breaks into the room with the Uplink Terminal in it, barricades themselves in, and attempts to unlink the station.

Sec's strategy at each point is different, from investigation to protection to outright warfare.

This document deliberately avoids specific numbers when talking about timers. The timers should be controllable by server operators without need for code edits (i.e. via cvars) so that playtesting can be done to make the round fair.

Building a big barricade and fending off Sec to claim the station is intended to be a big climax to the round which also feels narratively appropriate (think _Le Miserables_). This is in similar vein to the other big climaxes from non-Traitor rounds:

1. _Zombie_: A huge horde of zombies snowballs and eats everyone whilst Chemistry rushes to make and distribute the cure.
2. _Nukies_: The nukies raid the station and potentially nuke it
3. _Cult_: Nar'sie is summoned!
4. _Wizard_: "Oh heck, it's a wizard" followed by total chaos.

Players should leave a Revolutionaries round with an interesting story. Whilst it's true that the basic structure of the finale of both Nukies and Revolutionaries is similar, the story of how the station got there is very different, and the "defend the timer" force in the later is a raggedly-armed band of mutineers rather than a spec-ops team.
