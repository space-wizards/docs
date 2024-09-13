# Alert Code Changes

| Designers | Implemented | GitHub Links |
|---|---|---|
| Killerqu00 | :x: No | TBD |

## Overview

This proposal suggests changes to alert codes, expected procedures related to them, gameplay implications of having active alert codes and how will that influence the overall round flow. The main departments affected by this design document are security and command.

## Background

This discussion in Discord is a discussion about revolutionaries, crew morale and implications from these mechanics: https://discord.com/channels/310555209753690112/770682801607278632/1258800014205915157

## Problems

Here are the main problems with current alert system:

- There is no reason to not go blue/red as soon as round starts, except from theoretical bwoink. Blue gives security a free pass to search everyone on demand, so there is no reason for a play2win mentality HoS to *not* set a blue alert roundstart.
- Emergency codes do not have a persistent structure. Green/Blue/Red follow the order of how bad the situation overall is, but Yellow and Violet do not follow that: instead, they tell *what* the emergency is.
- There are no in-game implications for being on high alert. This is related to point 1, but it also results in emergency level rarely going down during the round.

## New Code Procedure

I suggest to change alert codes to a type-based system. Every alert code points out *what* is the problem, not the severity of it.

Blue alert is changed to "Security breach", and Red alert is changed to "Ongoing Attack/Terrorism".

![new system proposal](https://i.imgur.com/iLp24pq.png)

As a result of that, blue is no longer the "free random search pass" - you cannot put blue alert for a minor crime, since this does not qualify as confirmed syndicate activity or a security breach.

Here are some examples:
- Command ID has been stolen: blue alert is justified, since command access being in wrong hands is a big security breach;
- Bartender shot clown in the bar with their shotty: blue alert is not justified, it's not syndicate activity or a security breach.
- Digiboard has been stolen: blue alert is justified, since digiboard allows to supply someone with guns, which is a security breach;
- Bloodred with a L6 has been spotted: red alert is justified, since this is an attack on the station.
- Medical was bombed with a syndicate bomb: red alert is justified, since this is terrorism, therefore is also an attack on the station.

Also, guns are receiving a new field in their contraband text: alert code.
For example, a shotgun in armory would have a text that says: "This item is restricted to usage on blue alert or higher".
This isn't exactly a strict enforcement, but it will help with tracking bad security behavior (more on that later).

## Emergency Implications

Different emergencies would unlock different things across the station. In some cases, it aims to help crew; in some cases, it aims to help security and command, but also potentially worsen the situation if codes were declared without a good need for it.

- Yellow automatically sets EVA to emergency access. If there is no actual engineering emergency, EVA is only going to add problems to security, since breaking into high-sec areas from space is usually easier;
- Blue/Red blocks station passive income (no NT investments until emergency is resolved) and disables random supplies from CC. Instead, security+cargo may work together to sell contraband to CentComm for extra spesos(basically liquidating it);
- Red grants security soft All-Access(equal to HoP access). This may seem like a direct upside, but if Red is called in case of non-emergency, it actually benefits the antagonists: they can now kill a single secoff for AA;
- Specific emergencies unlock specific locked crates: any heavy arms emergency opens armory for security, any virus emergency opens the bio suit crates and lockers, etc;
- Any kind of not-admeme alert being set for extended time results in crew morale reduction time (explained further on). Exception: revolutionaries as a standalone gamemode and stuff.

## Crew Morale

Crew Morale (referred to as CM further on) is a hidden value that serves as a counter-measure to command and security running the station badly (referred to as BadHeading).

CM is supposed to be not metagameable, unless it is very low. This means that unique events should only be occuring when CM is very low.

High CM grants more positive events such as cool supplies from CC. Low CM results in negative stuff happening, up to a revolution.

**WARNING:** all parts of this doc mentioning a revolution imply that Revs were redesigned in a way shifting them to a less round-ending threat.

CM is not caused by crew directly (in most cases); it is caused by badheading/goodheading. Examples:

- Mass crew death results in CM drop;
- Creating amenities for crew results in CM raise (organising a pizza party or a concert);
- Prolonged alert codes being active drop CM based on their severity;
- Apprehending people that did not do things considered as harmful/hostile (slipping, stealing high-value things, harming people) results in CM drop. Important: **under no circumstances** should this be a simple antag check (security should not be punished for dealing with shitters);
- Lack of any action on things that the station needs causes CM drops (ex. TONS of messes);
- If CM is lower than default and no CM drops were triggered in a long while, CM will go up to default value.
- Certain critical events (such as singuloose or nukies) should disable CM system, since at this point station is already overwhelmed.

Some of the triggered event examples:

- Low CM can trigger a random minor negative event (skeleton spawn, vent creatures etc);
- Very low CM can trigger a head revolutionary spawning (please read the warning above);
- Very low CM can trigger a termination of a head from their position via CC announcement. Heads of departments that contributed to CM drop are picked when possible (for example, if "tons of messes" contributed to CM hitting "very low" threshold, HoP will be fired). This is not enforceable directly, but is rather aimed to create IC conflict between crew and command, as well as alerting crew of badheading occuring;
- High CM can trigger a random minor positive event (CC gifts, additional cargo funds etc).