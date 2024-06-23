# Security Improvements

| Designers | Implemented | GitHub Links |
|---|---|---|
| Killerqu00 | :x: No | TBD |

## Overview

This design document reviews main problems with security department that are currently present in the game and proposes fixes to them. This document will not go over recent (at the moment of writing this document) changes in rules and Space Law due to them being changed and polished at the moment.

## Background

This design document is a result of many discussions about current problems on both Discord and forums. Some links:

[Playing security is miserable](https://ptb.discord.com/channels/310555209753690112/1237264749281021952) on Discord

[Prisoner and security feedback](https://ptb.discord.com/channels/310555209753690112/1231862578536251434) on Discord

[Security in general is miserable](https://ptb.discord.com/channels/310555209753690112/1218720748097503252) on Discord

[Security tweaks (Rework?) feedback](https://ptb.discord.com/channels/310555209753690112/1203731006331560027) on Discord

[Security department is in extremely bad state](https://forum.spacestation14.com/t/security-department-is-in-extremely-bad-state/8147) on forums

[Why is security so miserable to play?](https://forum.spacestation14.com/t/why-is-security-so-miserable-to-play-what-can-be-done-about-it/7708) on forums

## Hall Interactions

Hall interactions are actions that security performs to you usually during the blue alert or if there is something suspicious about you. It may be a random search, a question like "Why are you carrying a spear as a passenger?" or a peaceful arrest. Non-peaceful arrests and chases will be covered outside of this section.

In general, there is a big problem with hall interactions: escalating the interaction to a fight is better when your opponent is typing something. This is very bad, because it means that it is better to magdump/stunbaton/run from them instead of actually going with the situation.

There are 2 solutions I see here:

1. Message interruption (the "-OOF!" thing) should work not only on being stunned, but on any hit, melee or gunshot. That automatically unfocuses the window, which allows for instant action.

2. Harm mode indicators. Here's how it could look:

![Harm mode indicator](https://i.imgur.com/nSY76PA.png)

## Chases

Let's say your hall interaction has already escalated to a chase.

Currently, there is almost no way for security to cut the distance between the pursuer and the escaping person. Disablers exist, but they have low charges and are heavily ping-dependant. The solution to this problem is some sort of ranged slowdown for security. I suggest to implement this via reworking tazers and adding them back as a T1 research.

Instead of insta-stunning, tazers will now apply 50% slowdown for 5 seconds on a target, unless they are wearing armor/hardsuit.
This introduces better tools for security to engage in chases, while still leaving room for counter if you are an antagonist.

As a result, I believe that this will shift the chases into a state where it's no longer always a better choice for a suspect to just run away, which will lead to more issues with security being solved (or at least attempted) to be solved verbally, or (for antagonists) using something else instead of magdumping the closest security officer upon being asked a question.

## Isolating areas

In certain cases, isolating a certain area is important for security. For example, if CE got gibbed by a minibomb, it would be rather difficult for security to secure the crime site for a detective. Same applies to cells with prisoners - there is little counter to a prisoner running out of a cell as soon as the windoor opens for a warden to give the prisoner something or to simply get ouf of a cell.

There is already a tool for that - holographic barrier projector, however, in its current state, it's really bad and almost never used.

I suggest that holographic projectors get a single useful trait - barriers created by the projector won't have collision for anyone with Brig access. Others will still be able to vault, just as before. 

This turns the beforementioned situation with a prisoner in a following interaction:
- Warden brings a prisoner into a cell;
- Warden places a barrier right outside of a cell;
- Warden uncuffs the prisoner;
- Warden walks out of the cell without any troubles;
- Prisoner might try to escape by vaulting the barrier, but will probably get disabled by a Warden.

This interaction loop leaves counterplay, but makes security job easier.

## Security Records

Security Records have improved a lot, but there is still 1 function (except from QoL such as filtering by status) that is missing.

Currently, security officers either have to update entries while being in security or to rely on warden/HoS entirely for that (since not every map has records mapped in general security area, some have the computer only in warden room).

The solution for this is PDA security records cartridge - probably not a roundstart option, but rather a T1/T2 research. With this, officers will be able to set statuses manually.

## Alert Codes Rework

Currently, alert codes are in a weird position. Some of them are linear in order of ascending severity: Green is "All Clear", Blue is "Be Alert" and Red is "Everything Is Falling Apart". However, Violet, Yellow and Admeme-type alerts are different - these are meant to signal *what* kind of an emergency is ongoing, not *how severe* it is. Before SOP was removed in rules refactor, it also affected the order of command authority, often in confusing ways.

This is an example of real-life codes for emergencies at hospitals. Each emergency type is represented by a color.

![types of emergencies graded by colors](https://i.imgur.com/FnhDYyG.png)


For SS14, I suggest to adapt this system. Here's an outline of how it would look like:

![new system proposal](https://i.imgur.com/IliqzBu.png)

You will also be able to set multiple alerts.

For the sake of simplicity, I propose that on LRP, any emergency allows for searches or using high-grade security gear. On MRP, however, security would have to follow this table: if there are no emergencies allowing for random searches, security cannot do them.

This change is actually pretty minor: command already announces what is going on when changing alerts currently. This change will allow for more context for latejoiners and for crew that didn't get the context of said alert level raise for some reason.

## Alarm Consequences

For the sake of modularity, this will be discussed separately from the Alert Codes rework, using the current alert system. 

Currently, there are zero consequences for abusing alarm system. You can just set the alarm to blue upon any minor crime being committed in order to give security a random search pass.

The most suitable system for this would be the system of high risk-high reward: the higher your alarm level is, the bigger the negatives for a normal shift are. For a shift that already derailed into chaos, these consequences will be tolerable.

Here are some automatic events that could trigger on different alert levels:

1. At Red/Yellow, EVA room automatically opens and External access airlocks become all-access. This is, of course, bad for a normal shift, since it would open lots of opportunities for antags, but if the station is getting spaced at a major scale, this is going to save crew.

2. At Green, security supplies from CentComm will never be supplied. At Blue/Red, they will be supplied at bigger rates. Also, some of the supplies that are mapped should be removed (such as Riot Gear). That also means that civilian-related supplies will be rarer at Blue/Red.

3. At Red, medical entrance will automatically become all-access. This is already something that command does pretty often, but it also has hidden dangers in a form of totally healthy people getting easy access to medicine/chemicals.

4. At Red, security will  automatically get soft All Access (access to main departmental zones). This CAN be implemented via mapping (like Maraphon does with security checkpoints), but that would require changes to basically every map. This also has a big risk of antagonists getting soft AA by looting a single officer.

## Secure Crates

Secure crates for security also could use some tweaks.

Certain crates should be locked behind alert levels: for example, you shouldn't be able to order lazer crates on green. Also, secure crates should have an anti-tamper system: upon being broken, they will automatically send an alert message to both security and cargo comms.

This will solve some powergaming problems, especially with salvage: it will become harder to get guns without security knowing. Antags, however, will still be able to emag them/get the security ID/jam the tracker.