# Voting Cartidges

| Designers | Implemented | GitHub Links |
|---|---|---|
| CptJeanLuc/IProduceWidgets | :x: No | TBD |

## Overview

Three new cartridges focused around facilitating voting, and in-world-ing various player activities.
1. Democracy Cartridge. Lets you vote on various things. Loaded into all crew assigned PDAs by default.
2. Democracy+ Cartridge. Lets you create votes for anyone with a decomocracy cartridge to vote on. Loaded into command PDAs by default.
3. Internal Affairs Cartridge. Lets you vote on whether or not a command member should be demoted or fired. The goal is to mechanic-ize a way for players to deal with shithead command members while also alleviating admin load for this particularly awful issue type.

## Background

Presently players often find themselves in the need of a way to assess the entire crew's desire to continue a round or take some sweeping action. This is currently done by a "voice vote" over the general radio channel. This has some serious drawbacks. Namely, its not at all clear most of the time what the outcome was. It also just feels kinda lame.

Adding a way for players to vote via their PDA does a few things. It adds some mechanical support to the idea of crew choice and support for command decisions. It also allows for much more interesting interactions such as having your PDA stolen to rig votes or disenfranchise individuals.

The core idea is thus:

## Democracy Cartridge
The democracy cartridge is an application loaded onto your PDA at round start, or via a cartridge available to the HOP which lets you take part in various votes or referrenda so long as you are in posession of your PDA.
When a referendum becomes open, your PDA beeps, and tells you there is a new poll to vote on.
For each referendum, you are given a series of buttons you may press in order to affirm, oppose, or abstain from a referendum. Votes are final, and at the end of a timer for the referendum all cast votes are tallied, and displayed anonymously, saved for the rest of the round.
That is all the votes do. They do not mechanically force anything to happen. They just gauge the crew's opinion.

## Democracy+ Cartridge
The democracy+ cartridge is much like the democracy cartridge. It differs in that it has the ability to create new referenda.
Though a cartridge may exist for adding this software to your PDA, it should be unavailable by normal means. Instead, democracy+ is loaded by default on all Head PDAs. This adds some more interesting reasons to steal a PDA, and also adds some extra agency to command members.
There should be a character limit on the text of the referendum, intended to force them to be short and to the point.
When a referndum is made, it should include the name on the ID loaded in the PDA. It does not however require any particular access to do so. It should fail to create a referendum without an ID and alert the player to this.
There should be a hefty per-PDA or cartridge cooldown on creating referendums, but no such restriction on voting on open referendums in the case more than one is active at the same time. This is to prevent spamming the feature and diluting its utility.
Once referendums are created they should not be able to be changed or canceled.

## Internal Affairs Cartridge
The Internal Affairs Cartridge is a more specific tool.
Its purpose is to add an in-world, within the rules, way for command members or anyone with their PDA (and perhaps some pseudo randomly chosen special agents for added chaos) to assess the ability and faculties of other command members.
The goal is to eliminate violent coups that originate outside the rules (i.e. other non-antag command members) due to the percieved or real ineptitude of command members. This should strive to in every way prevent the need for admins to investigate who is at fault for a failure of command.
For every command member on the station, whether round start or late join, a referendum will appear within the Internal Affairs software allowing command members to vote to fire another command member.
The votes are "anonymous" in that each of the 7 command positions share their vote with all PDAs of the same command type. I.E. if there are 3 QM PDAs for any reason, they all share the same "cargo department" vote.
If there are more than one PDA of a given command, then if ANY of that PDA type have voted on a referendum to fire a member of command, then the associated department vote is cast.
These referendums differ from others in that the votes may be un-cast at any time BEFORE a command member is fired. This allows politicing and negotiation.
To facilitate the firing, should it be necessary, each command member starts with an unremovable implant that is set to explode them into crit, fry their ID or other access items on their person, and remove any Internal Affairs or Democracy+ cartridges from any PDA on their person. (An alternative may be to require the relevant access on an inserted id for the Internal Affairs cartridge to allow voting.)
fried ID cards should be visbly charred, still count for steal objectives, but otherwise be as functional as a passenger ID with only maintenance access, as well as changing their job icon.
If a command member is fired, it should automatically vote to fire all other command members UNLESS there is an existing PDA of the same type as the fired command member which is still capable of voting on Internal Affairs referenda.
The HOP should be granted a single extra implanter, help under as secure a guard as possible, for the purpose of promoting another crew member to a command role. They do not however get any more PDAs or PDA cartridges capable of voting on Internal Affairs.
Different PDA votes should be displayed on the referenda as the associated color of the department from which the vote came. Red for sec, yellow for eng, light blue for medical, etc.
The HoP and Captain version of the software should have extra weight to their votes. The HoP can cast a double-vote, and the captain can cast a tripple-vote.
Ignoring the possibility of undercover-agents or admin PDAs voting, this would give us 5 normal department votes, 2 service (or command) votes, and 3 Command votes for a total of a possible 10 votes to fire any given player.
Should any player recieve 5 or more votes the vote should succeed. This means that in a normal round the Captain and HoP could choose to fire a command member, or the five department heads could choose to fire the captain, or any number of such combinations.

For balance reasons, it might be fun to make this a function of the MindShield implant, but that should come with more deliberation. The functionality should be possibly however if desired.

## The rest?


