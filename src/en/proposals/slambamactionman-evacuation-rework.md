# Evacuation Rework

| Designers | Implemented | GitHub Links |
|---|---|---|
| SlamBamActionman | :x: No | TBD |

## Overview

While the goal of escaping to CentCom (for both antag and crew) is in a good place balance-wise, its current implementation is inflexible, contains ludonarrative dissonance and strongly encourages the largely unpopular antag strategy of "shuttle bombing".
This design proposal aims to give both antags and crew more gameplay-valid options for escaping to CentCom that align with narrative options, making shuttle bombing a less reliable method to achieve kill objectives while not outright removing it.

## Background

This design proposal will have wide-ranging consequences for multiple gamemodes and roles; as such, it's divided up into sections focusing on specific scenarios and roles.

### Evacuating the station & Ludonarrative Dissonance

Crew escaping is largely a roleplay/self-imposed goal. Save for some unique scenarios (Command during Revolutionaries) there is nothing directly incentivizing crew to reach CentCom at the end of a shift. From a gameplay perspective, crew may be aware that antags have goals that involve killing/marooning them and don't want to give an opposing player free greentext by staying behind on the station. From a narrative perspective, staying on an abandoned station or one filled with zombies is something that is reasonable for a character to want to avoid. This is also enforced by the game; evacuating is portrayed as a way to get to a safe location and as such becomes an implicit goal for crew.

Despite this narrative, there are scenarios where the narrative is fulfilled yet the game does not treat it as such. This can be observed with **Escape Pods** and **Evacuating in Non-Evac Shuttles** (Cargo/Salvage/Shittles). While these options allow crew to evacuate from the station, for the purposes of gameplay they do not count. This is largely done due to balance reasons as described in the sections below.

Despite this, there are multiple instances where the ludonarrative dissonance has caused confusion among players.
([1](https://discord.com/channels/310555209753690112/1214830576150904882)
[2](https://discord.com/channels/310555209753690112/1210183276560515152)
[3](https://discord.com/channels/310555209753690112/1168797764205940746)
[4](https://discord.com/channels/310555209753690112/903965207091642429/1212912623180320899)
[5](https://discord.com/channels/310555209753690112/1017887598401814629/1209668240444227685)
[6](https://discord.com/channels/310555209753690112/1159574990774079568/1209347110579740722)
[7](https://discord.com/channels/310555209753690112/1208825540761354321/1209029316998864966)
[8](https://discord.com/channels/310555209753690112/675078881425752124/1208222775047618560)
[9](https://discord.com/channels/310555209753690112/1114911717445611580/1207828586577272863) to show just a few). While it's not a *major* gameplay-impacting problem, the lack of gameplay feedback is not a positive. Designing a way to remove this dissonance should be possible, which this design proposal aims to do.

```admonish tip Observation
Escaping from the station with alternate methods (i.e. Escape Pods and non-Evac shuttles) is desirable from a narrative standpoint, but the game's mechanics do not match this narrative due to balance reasons. 
```

### Traitor Objectives

This design proposal affects traitors in two ways; themselves escaping to CentCom ("Escape to CentCom alive & unrestrained" objective) and their targets escaping ("Kill or Maroon"/"Steal" objectives).

#### Escape to CentCom alive & unrestrained

As stated by maintainers and observed by the community, escaping to CentCom without being restrained requires a satisfying amount of skill; the main objectives of killing/stealing need to be performed in such a way that the antag is either not discovered or, if they are, they are able to sneak past Sec and hide on the shuttle without being found. This is sufficiently difficult and largely rewards antags who are stealthy enough to avoid detection or robust enough to fight their way onto the shuttle.

```admonish tip Observation
Any change that may impact the "Escape to CentCom alive & unrestrained" objective should aim to preserve this balance, either by providing an equally or more difficult option to achieve the objective (and being aware that providing options inherently makes the objective easier).
```

#### Kill or Maroon Target / Steal X from Target

Killing and stealing are largely seen as balanced objectives that are fun for both sides; any imbalance is easier to adjust for on individual item levels than an overall change to the objective system. 

There is one exception to this, which is the controversial act of "shuttle bombing". While shuttle bombing is undeniably effective and can add a climax of chaos at the end of a round, it's also known to be seen as a cheap tactic that can ruin the enjoyment for other players at the end of a round. Since the evacuation shuttle near-guarantees your target to be on it, it can be preferable to play as a **passive traitor** until it arrives. Being a passive traitors means you are neglecting to attempt your objectives during the shift, reducing the amount of interesting scenarios happening on-station you would otherwise contribute to. This proposal is submitted under the assumption that shuttle bombing is currently too reliable of an option for traitors, causing it to happen too often with little effort or planning from the antag to ensure its success. 

```admonish tip Observation
Shuttle bombing *should* be an option for Traitors; it's however too reliable at the moment, causing it to be a more common occurrence than is desirable. When prevalent it promotes passive traitors, leading to uneventful rounds.
```

### Revolutionaries 

Note: Revolutionaries are likely going to change in the future.

If we observe Revs as they are right now it's not uncommon to see rounds stall where Revs have control over the station but can't locate the final Command member(s), or vice versa. To give a sliding scale of success Rev rounds have ending conditions where a Revolution/supression is only partially successful if both sides have surviving members. This encourages crew to stay on station until they find the hiding player, though often this translates to complaints that the hiding player is stalling the round. 

```admonish tip Observation
Revolutionaries have an issue with stall rounds; the dominating side is discouraged from calling the evac shuttle if there are hiding players of the opposing side, and have no way to flush out hiding players.
```

### Zombies

While a zombie round that goes in the crew's favor has little interaction with escaping the station, those rounds where the zombies gain the upper hand definitely do. In the current state of the game, Cargo becomes the de-facto escape option for crew due to its reliability and player-controlled ability to avoid the station altogether. Going to the Evac Shuttle as a survivor becomes pointless if Cargo can pick you up. The Cargo shuttle *should* be a strong option for the crew who make it onto it, but it could be argued that it's ability to avoid interacting the zombie round altogether is too strong.

```admonish tip Observation
The Cargo/Salvage Shuttle should always be a strong option for crew, but there is little reason for the people controlling it to interact with the station once it's been made safe.
```

```admonish info
Extended, Survival and Nukies do not really track escaping the station, and as such aren't touched on in this design proposal.
```

## The Design Proposal

With the observations from the Background section in mind, this proposal aims to achieve the following:

1. Allow escaping using the alternate escape methods.
2. Make those alternate escape methods a point of conflict for objective holders (antags & Command), to ensure the evac shuttle is still a usable default at the end of a shift.
3. Promote on-station antag activity over on-shuttle antag activity.

### Coordinates Disks & CC FTL

```admonish warning Note
This design proposal makes *no changes* to the Evacuation Shuttle. It will function exactly as it does in the game currently.
```

Escaping to CentCom using *Escape Pods* or *Non-Evac Shuttles* now count as escaping to CentCom for the purposes of gameplay objectives. To counter-balance this, enabling FTL travel to CentCom for these spacecraft is no longer trivial, requiring a unique single-instance item available to Command: **The CentCom Coordinates Disk** (CC CD for short). The CC CD spawns in the **Escape Pod Controller Console**, described further below.

#### Non-Evac Shuttles

Non-Evac Shuttles no longer get the option to travel to CentCom by default. Instead, all shuttle consoles have a slot for a Coordinates Disk. Inserting the CC CD into a console unlocks the CentCom travel option, though the option may not be selected until the Evac Shuttle has left the station. The CD may be inserted into any console that controls the shuttle, such as the remote Cargo/Salvage consoles, and unlocks the FTL option in all connected consoles.

Additionally:
- The option to travel to CentCom becomes unlocked the moment the Evac Shuttle leaves, and the time it takes to travel there should be such that they arrive at the same time as the Evac Shuttle (with perhaps a minimum required time). 

#### Escape Pods

The destination of Escape Pods is now decided by the CD inserted into the **Escape Pod Controller Console**, a computer located in a secure Command area (Bridge or Telecomms). Since the CC CD spawns in the console by default, this means that if the CC CD remains untouched for the entire shift all Escape Pods will travel to CentCom once the Evac Shuttle launches. Should the CC CD not be in the console at the time the Evac Shuttle leaves the station, the Escape Pods will *not* launch. 

There is an exception to this; all Escape Pods now have a wall-mounted Disk Console. Inserting a CD into the Disk Console will override whatever CD is inserted into the Escape Pod Controller Console. The Disk Console can be examined to see if a destination is currently set via the Escape Pod Controller Console or the Disk Console.

Additionally:
- Escape Pods now dock at CentCom instead of floating in space somewhere near around CC. The goal is to reinforce the survival after taking an escape pod.
- Escape Pods now have a max occupancy. The specific implementation is up for discussion; it could require passengers to be buckled in or else get launched out the airlock, the pod could fail to launch if too many are in it, etc. The goal is to avoid stacking an absurd number of crew in the pods.

## How would this impact the game?

Overall, the introduction of the CC CD will cause the end of the shift to play out differently depending on *the actions antag & crew take during the shift*. Below are some scenarios and how they will likely play out:

### Command have the CC CD, Traitors are passive

During a round where traitors are known on the station but the shift have played out calmly, Command are now given the option to influence how the evacuation will go. They can let the CC CD remain in the Escape Pod Controller Console and opt to use the escape pods themselves to leave the station. Alternatively Cargo/Salvage can be given the CC CD, with Command using those shuttles to travel to CC. Crew can utilize these methods as well. The Evac Shuttle is always an option for the Command/crew who the CC CD option is not available to. 

This will reduce the reliability of shuttle bombing for passive antags; targets are no longer guaranteed to be on the Evac Shuttle. This encourages traitors to act on-station, resulting in either the two scenarios below:

### Traitor have stolen the CC CD

If a traitor manages to steal the CC CD and keep it until the end of the round (which should be a difficult task, considering the Escape Pod Controller Console's location), this opens up opportunities depending on what objectives they have.

If they have completed their objectives and are only concerned with escaping, escape pods and shuttles now become a viable option. Security will have a hard time patrolling them all, allowing the traitor a more clean getaway as a reward for their theft. It also allows loud antags to escape without forcing a fight on the evac shuttle involving the entire crew, further reducing murderboning.

If the traitor instead has a kill/maroon objective, possessing the CC CD *ensures* that their target will be on the Evac Shuttle. This re-introduces the same level of reliability to shuttle bombing, but requires the theft of the CC CD for it to be successful. Thanks to this shuttle bombing can't be done with full passivity during the round. 

It's worth noting that unless cooperation is involved, a stolen CC CD will only benefit a single traitor. Other traitors will still be forced to utilize the Evac Shuttle as normal.

### Command have the CC CD, Traitors are active

If traitors have performed their objectives on-station during the shift but failed to take the CC CD from Command, Command are given control over the escape options available to antags. The CC CD can be removed from the Escape Pod Controller Console, locking out traitors from using them to escape. This forces traitors to take the Evac Shuttle, exposing them to the same situation as is currently in the game. Additionally, Security can be certain that no other escape methods are available, allowing them to confidently patrol evac and be on the lookout for any known antags.

### Revolutionaries

While the round will not be impacted much if one side is dominating, this proposal does allow the winning side to end a stalled round. By removing the CC CD, the winning side ensures that the other side must go to the Evac Shuttle to escape the station. Failure to do so would maroon them on the station, resulting in a loss from that side. On the contrary, should the losing side get their hands on the CC CD they can utilize either escape pods or shuttles to successfully make it off the station alive. The winning side can try to prevent this by patrolling those options, possibly introducing a confrontation at the end of the shift.

### Zombies

Zombie rounds can play out differently depending on where the CC CD is.

If it remains in the Escape Pod Controller Console, only Escape Pods and Evac becomes viable escape options, forcing Cargo/Salvage to fight their way through Evac if they wish to leave. Cargo is still a very safe option as it can dock out from the station to avoid zombies entering it, but it's no longer a completely safe alternative. 

If the CC CD gets removed from the Escape Pod Controller Console, it can be used by the shuttles to provide a much safer escape option. This does not come without a risk however; should Command fail to retrieve the CC CD it might fall on the hands of crew to break in and get it instead, and any crew spread around the station will be forced to either head to Evac or Cargo as the Escape Pods are no longer an option.

Then there's also the scenarios where a single crewmate gets their hands on the CC CD allowing them to selfishly escape in a pod on their own, or maybe the CC CD gets lost completely and now Evac is the only option...

## Closing thoughts

Crew should already become somewhat familiar with CDs by the time this change is implemented, as they are already part of a Salvage FTL rework seen here: https://github.com/space-wizards/space-station-14/pull/23240

This design proposal came from the strange feeling I got that evac pods are currently purely a RP functionality, when they could be so much more. I hope this proposal will introduce more interesting endgame scenarios involving evacuation and ultimately expand the evac pod/non-evac shuttle escape options to be more engaging.
