# Role Classification System

| Designers            | Implemented | GitHub Links |
|----------------------|-------------|--------------|
| chromiumboy          | :x: No      | TBD          |

## Problem statement
Currently, all antagonist and ghost roles are categorized by broad labels, such ‘solo antagonist’, ‘team antagonist’, and ‘free agent’. Due to the expansiveness of these labels, it is difficult to clarify to players, admins, and other members of the development team how roles assigned these labels should behave. For example, mice, syndicate visitors, and closet skeletons, are all ‘free agents’, but expectations around player behavior when playing these different roles are likely to vary.  The burden of explaining these expectations to others falls entirely upon a short text description that players only see once when they accept the role, which is far from satisfactory. 

## Proposed solution
Instead of using a small set of predefined labels for describing antagonist and ghost roles, we should consider breaking them down into a set of aspects that can be freely combined, much like the [SCP Anomaly Classification System](https://scp-wiki.wikidot.com/anomaly-classification-system-guide). Having our own role classification system would be very useful from both a design perspective, as well as an aid for players, by providing needed granularity in the descriptions of these roles and as a way of rapidly providing a high-level overview of how different roles are expected to function. 

In this proposal, each antagonist and ghost role is defined by an associated faction (e.g., 'NanoTrasen', 'Syndicate', 'Animal') and four different key aspects: Disruption, Notice, Escalation, and Fraternity. Each aspect has four different ‘levels’ associated with it that modify expectations around player behavior. This system could be readily expanded upon to accommodate crewmember roles as well.

### Disruption
Disruption relates to how disruptive player actions should be to other players and round flow in general.

| Level | Label | Player facing description |
|-------|-------|---------------------------|
| 0 | None | "Do not adversely interfere with the workings of the station or its crew." |
| 1 | Mild | "Minor interference with the workings of the station or its crew is permissible." |
| 2 | Moderate | "Active interference with station operations and its crew is expected." |
| 3 | Severe | "You must do your best to shut down station operations and end the round." |

### Notice
Notice relates to how noticeable the player's actions should be to others on the station. Note that this aspect may not apply to certain roles, such as silicons.

| Level | Label | Player facing description |
|-------|-----------|---------------------------|
| 0 | None | "Being detected would be disastrous for your mission - avoid notice at all costs." |
| 1 | Low | "You work best when you aren’t attracting much attention. Keep a low profile." |
| 2 | Moderate | "Being stealthy may be beneficial for achieving your objectives, but you have other tools you can rely on." |
| 3 | High | "You’re here to here to cause trouble and get everyone’s attention." |

### Escalation
Escalation relates to expectations around combat and the use of violence against other players.

| Level | Label | Player facing description |
|-------|-------|---------------------------|
| 0 | Never | "Do not intentionally harm humanoids. If in danger, attempt to de-escalate the situation, or flee." |
| 1 | Normal | "Normal escalation rules relating to the use of violence apply to you." |
| 2 | Elevated | "You may use violence, but it should be used to achieve your goals, or to remove direct threats to you." |
| 3 | Extreme | "The escalation rules do not apply to you. You are free to cut down any enemies you encounter." |

### Fraternity
Fraternity relates to player cooperation with other faction members.

| Level | Label | Player facing description |
|-------|-------|---------------------------|
| 0 | None | "The other members of your faction are your competitors. Either ignore them, or eliminate them." |
| 1 | Low | "The other members of your faction are your rivals. Temporary alliances might arise if your goals align." |
| 2 | Moderate | "The other members of your faction are your colleagues. You are welcome to assist them." |
| 3 | High | "The other members of your faction are your allies. Do whatever you can to support them." |

### Classification examples
Here are some examples of how the classification system described above could be applied to clarify expectations on how antagonists and ghost roles should be played. (Note, these examples are meant to be illustrative, not definitive in how these roles should actually be classified.)

| Role | Faction | Disruption | Notice  | Escalation | Fraternity |
|------|---------|--------|------------|------------|------------|
| Cyborg | Nanotrasen | 0 | N/A | 0 | 3 |
| Mouse | Animal | 1 | 1 | 0 | 2 |
| Skeleton | Nanotrasen | 1 | N/A | 1 | 1 |
| Thief | Syndicate | 1 | 1 | 0 | 1 |
| Traitor | Syndicate | 2 | 2 | 2 | 2 |
| Nuclear Op. | Syndicate | 3 | 2 | 3 | 3 |

## Communicating role classifications to players
Role classifications should be communicated clearly to players, and should be readily accessible at any time. The most obvious location to host them is the player objectives subscreen. Here is a mock-up of what this might look like.

<img width="400" height="773" alt="role-description" src="https://github.com/user-attachments/assets/7abbae8e-5cae-4bf6-bed0-18b7ae251606" />
