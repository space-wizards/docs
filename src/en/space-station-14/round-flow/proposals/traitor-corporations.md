# Syndicate Traitors (Corporations Rework)

| Designers      | Implemented | GitHub Links |
| -------------- | ----------- | ------------ |
| FairlySadPanda | :x: No      | TBD          |

# Summary

This is a proposal for a rework of the Traitors game mode. It is not a rework of the Traitor antagonist.

This proposal adjusts some of the current game mechanics surrounding the game mode. It is designed to build a stronger round narrative and give players involved in the round more fun and engaging experiences.

This rework primarily focusses on the role of distinct corporations within the Syndicate and their interactions with NT and each other. It reworks the "every tot for themselves" approach of the current Traitor game mode, allowing for a more diverse set of things that can happen. It also proposes some further work that would build on the intitial rework, that would touch on the Traitor game mode more commonly.

# Why This Isn't A Progressive Objectives Proposal

A "progressive objectives" mechanic for Traitors works like this:

1. The traitor spawns. They are given a simple task to steal some documents, and are given some TC.
2. The traitor succeeds! They gain TC and get a harder mission to kill a crewmate.
3. The traitor succeeds! Now they gain more TC and have to kill a Head...
4. The traitor succeeds! Now they get given even more TC... and when the station runs out of objectives, the traitor gets an objective like "set off the nuke" or "die a glorious death".

The issue with this is that it creates a power ramp for Traitors and pre-assumes a "won" round for Traitors is a destroyed or otherwise massively griefed station. Whilst players do like rounds with maximum death and chaos, Traitor, which tends to be the most common round in rotation, needs to avoid being geared toward excessively chaotic rounds. This tends to put pressure on Security and encourages more of a PVP-style approach to Traitors, when in spirit it is supposed to work a bit more like a social deduction game.

Whilst a progressive objective mechanic might be a fun new alternative to the current Traitor round type, this proposal is focussing on improving the current systems.

# Syndicate Corporations Are Important

The Syndicate is a collection of corporations that are united only by their dislike of Nanotrasen and their distrust of each other. They have continually-shifting internal politics, and even they struggle to keep track of who is even currently signed up as an official Syndicate member.

For the purposes of this document, all Syndicate Corporations are identical, so we'll just be using three common ones as names:
- Cybersun Technologies
- Donk Co.
- Waffle Corp.

Syndicate Corporations are the "true" antagonists of rounds of Traitor, rather than the Traitors themselves. The Traitors work for the Corporations, and the Corporations have objectives that the Traitors need to complete.

## Corporations Have Relations To Other Corporations

Each Syndicate Corporation has one of three relations to each other organization. Each relationship is bi-directional, so both parties have the same relationship with each other.

- Ally: The corporations are currently allied towards a common goal.
- Neutral: The corporations do not currently share any goals, but have not found reason to cross swords internally.
- Enemy: The corporations are feuding.

This relationship web is generated randomly each round, and doesn't have any particular weighting. A round could feature a united Syndicate all of whom really want to kick NT's teeth in, or a mafia of competing interests more interested in killing each other.

In addition, the number of Corporations active in a given Traitor round is randomized. A Corporation that is available in the round and can have Traitors assigned to it is called a "candidate".

## Traitors Each Work For One Corporation

For example, Urist McHands might work for Cybersun, and Urist McDwarf works for Donk Co. This is actually how the game already works.

Traitors do NOT get their own objectives: their Corporation does. This has one notable exception: see the Survive/DAGD section below.

## Traitors All Have The Same Codewords, The same Uplink, And So On

All Syndicate Traitors share a codebook and tools. The role of Traitors themselves don't change as part of this rework.

## Syndicate Corporations Have Objectives

When it is time for the first Traitor on the round to be picked, each candidate Corporation decides on their objectives for the round. Objectives are a complex subject and liable to be chipped to death in implementation, but here are some general principles:

1. Objectives are generally interesting individually but not round-ending themselves.
2. Objectives have a difficulty weighting. When objectives are picked, it should be possible to create a set of relatively balanced sets of objectives using these weightings.
3. Objectives encourage use of different parts of the Traitor uplink, including theft, sabotage, and violence.

Once a Syndicate Corporation has claimed an objective, Ally and Neutral organizations to that Corporation **cannot** also claim that objective.

The total difficulty of the objectives that the Syndicate Corporation has to complete scale with the number of candidate corporations in the round. For example: a round with eight Traitors that have managed to all join the same Corporation would get a long list of objectives, whereas eight Traitors in eight Corporations would each get quite short ones.

Once each Corporation has picked its objectives, Traitors are picked and assigned to candidate Corporations randomly. A Corporation with at least one assigned Traitor is called "active".

## Syndicate Traitors Know Who Else From Their Corporation Is On The Station

Traitors, when they spawn, will be able to see who else from their Corporation was assigned to the station. They will not see who else from other Corporations were spawned.

## Syndicate Corporations Can Help Or Hinder Each Other

Once the Traitors have been picked for the round, the game will then consult what Corporations in the round are Allies and Enemies.

### Allies

If two active Corporations are Allies, one or both of the Corporations will gain an objective to assist the other in their objectives. (Note "one or both" here. Just because Cybersun wants to help Donk Co., this might not be reproached.) If only one Corporation is picked to assist the other, this will be the Corporation with the lower total difficulty of their objectives, or a coin toss if even.

The objective for an Allied Corporation reads as follows:

"Assist our ally, CORPORATION NAME, in completing their objectives. Our contact with them is NAME OF TRAITOR."

This replaces the objective to "asssist so-and-so with their objectives" as found currently.

### Enemies

If two active Corporations are Enemies, one or both of the Corporations will gain an objective to disrupt the other in their objectives. (Note "one or both" here. Just because Cybersun wants to mess with Donk Co., this does not mean Donk Co. are aware Cybersun are on the station.)

The objective for an Enemy Corporation reads as follows:

"Our hated enemy, CORPORATION NAME, is also here on the station. Prevent them completing their objectives. One objective they have is as follows: OBJECTIVE HERE"

Unlike for Allies, Enemy Corporations are not told the identities of any of the other Corporation. Instead, they can deduce this in-game if needed.

## Sleeper Agents Interact With This System

Sleeper agents will be assigned to an active Corporation on spawn. They will not join a Corporation that has completed all its objectives. If this results in a Corporation becoming active, depending on that Corporation's Ally and Enemy status, this will trigger Ally/Enemy objectives being added to other candidate corporations.

Sleeper Agents are told who is in their Corporation, but this is NOT the case for agents already on the station: a sleeper agent is a surprise to their own team.

## Survive and DAGD

The "survive" and "DAGD" roles are assigned to every traitor randomly, with a low chance of a traitor gaining DAGD (which stands for "Die a Glorious Death").

Most Traitors will assume every other traitor has to survive. For the purposes of Corporation relationships, survival and DAGD do not prevent success of these objectives (the Syndicate, as much as they hate each other, hate NT more, and don't want to encourage any operative to fall into enemy hands).

Survivor/DAGD are not revealed to other Traitors, even on the same team.

Due to their impact on rounds, DAGD Traitors are specficially signposted to observers (including the dead), admins, and on the End Of Round screen. Whilst specific objectives are not revealed automatically to observers, DAGD encourages behaviour that can look like serious rule-breaking, and to mitigate admin load, observers should be told if a traitor is allowed to do actions normally contrary to the rules like deliberate singuloosing.

## End Of Round

When End Of Round is triggered, each active corporation's objectives (and if they succeeded) is shown to all players. This allows all traitor players to know what in spess was even happening with that other weird guy, and so on.

### EOR on MRP

On MRP servers, objectives are not flagged as "completed". Instead, at the end of round, during the more relaxed MRP end-of-round phase, Traitors are given the opportunity to mark if they consider their objectives done or not, and write a short reason why. This is referred to as "pink-texting", and encourages traitors to play their role with more of an RP, interactive focus.

# Technical Steps

This work would involve replacing some of the current Traitor code, mostly for objective assignment. However, it would not involve touching the overwhelming majority of how Traitors work. For a single sleeper agent spawning in a Survival round, the game is much the same as ever.

This work would involve adding pink-text support behind a Cvar for MRP servers.

This work would involve being able to define Syndicate organizations in YAML a bit more deeply than they currently can be. It likely involves creating at least a small icon for each corporation (to use as an objective icon and in their EOR objective list).

This work would involve making sure that the various controls, including number of corporations, maximum/minimum number of people per corporation, if allies/enemies are enabled, if corporation members can see the IDs of other corporation members, and so on, is customizable, where appropraite, at either the YAML or Cvar level. It should be possible to create the current "traditional" traitor mode, within reason, within the new implementation.

# Some Potential Future Work

## Different Uplink Stores For Different Corporations

Maybe Donk and Waffle have interesting unique guns, and only Gorlex has access to Nuclear Operative gear?

## Shifting Allegiances

Maybe the Syndicate could suddenly shift allegiances during a round? This would be a radio announcement broadcast globally, reading something like:

"Due to the CEO of Waffle Corp refusing to attend the birthday party of Donk Co's CFO's great aunt, these two corporations are now at war!"
"After the kindling of a steamy romance between the leaders the Gorlex Maurauders and Waffle Corp on a celebrity special of Lava Island, these two corporations are now allies!".
"Despite their best efforts to stay angry at each other, Cybersun Industries and Waffle Corp's recent feud over pancake recipes has burnt out."

These shifting allegiances would then flip (or delete) the corresponding objectives, should they exist.

## Backstabbing Corporations

A Corporation could appear to be Allied with another Corporation, but this could in fact be a ruse: this would lead to one Corporation having an Ally objective with the other, and the other having an Enemy objective in return.

## Corporation Intel

It could be possible for either Security or individual Traitor corporations to gain intelligence on the Syndicate to find out who is allied with whom, or potentially even expose particular traitors on the station, via completing some sort of task (such as identifying a traitor, an objective they had, and the corporation they're working for to Centcomm, for example?).
