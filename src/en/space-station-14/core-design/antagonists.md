```admonish warning "Attention: WIP!"
This doc is actively under development and is not fully complete. Things may change!
```
# Antagonist Design
Antagonists are one of the fundamental pillars of Spacestation 14, serving as a way to inject chaos into a round. Historically the implementation of different antags have been very hit or miss, ranging from wildly successful (space wizard) to contensious and disliked (Revolutionaries). 

The goal of this document is to lay out core design principles for creating antagonists that players enjoy playing as *and* against, in addition to categorizing the possible types of antagonists.

This document is not a strict list of requirements, but intends to serve as a foundation for what antagonists should feel and play like. In some cases a particular antag may deviate from the princples in this doc, and that's fine as long as the design still works and provides  quality gameplay.

This document focuses mainly on the high-level concept of antagonists and how to categorize them. Other documents will go into the specific goals/guidelines for creating a particular type of antagonist.

# Design Pillars
These are the core design pillars for antagonists. The design of all antagonists should follow these pillars as closely as possible.

## Just a Spark
- Antagonists alone should not be able to take over a round. Their interactions with the crew should be what turns their spark into a raging inferno of chaos, or snuff it out into embers.
## Escalation
- Antag actions and effects on rounds escalate over the course of the round to their full potential.
## Full time job
- Antags should be discouraged from simply playing as crew, or being friendly/assisting the crew.
## Back and Forth
- Success or failure shouldn’t depend on a single event, rather there should be minor wins and losses over the course of a round that add up to the final climax.
## Discoverability
- There should be clear breadcrumbs present to provide clues to which antagonists are present. The crew should also be aware of their counterplay options to prevent antagonists from easily snowballing. 
## Accessibility
- Antags should be provided all the information required to perform their role, along with what they are allowed and not allowed to do to achieve their objectives. Mechanics/identification should not rely solely on colors for differentiation or functionality.
## Fun to lose against (or as)
- Losing/dying to an antag should not feel unfair to a player. Player’s should always have some option in terms of counterplay. Same goes for antags, they should always feel like they have options and are not hard countered.

# Antagonist Categories
These are the categories that an antagonist must fall into. Categories define how many players are playing as a particular antag and their relationship towards objectives. Antagonists should belong to only one category.

## Lone Antagonist
- Solitary in nature. Either there is only one of its type present or each of them act independently with their own objectives. Lone antagonists may team up if their objectives align.

## Team Antagonist
- A group of antagonists with a shared objective. Group antags are considerably more powerful (and thus rarer) than solo Antags. This group generally has a fixed set of members that are known to each other. Group antags may work with solo/other group antags if their goals align.

## Conversion Antagonist
- A small group or single antagonist that starts off weak but with high snowball potential. These may have a hierarchical structure, with the original serving as a “leader” role. Converts crew into aligned antagonists or resources that can be used to upgrade itself. It’s important that this type disincentives crew from willingly converting themselves to make snowballing harder or features some form of anti-snowball mechanic.

# Antagonist Alignments
These serve as a guide to how much impact an antag should have on a particular round or station from their abilities/items. Additionaly, alignments also quantify how impactful the particular antags objectives are on the rest of the station. Antagonists can only have one alignment.

## Major
- Can very quickly ramp up to a station-level crisis by using their powerful tools/abilities. These antags tend to become the main focus of a round if they are not engaged early on. Tends to primarily work alone. Most major antag objectives are exclusive which results in conflict between other major antags if they are present.

## Minor
- Typically prevented from mass sabotage or murder through mechanics or objectives. Usually completing self-serving short term goals using their limited tools/abilities. May join up with major antags if their goals align.

## Neutral
- An antagonist with a self-serving goal that is not directly in conflict with the crew. Neutral antagonists avoid direct conflict and escalation while prioritizing their own survival. They also have the freedom to align themselves to crew or antagonists, depending on which group aligns best with their objective and chance of survival.

## Assisting
- Typically the result of another antag's actions. Assisting antagonists goals are aligned with their creator/converter. May assist other antagonists if it benefits their creator.

## Pest
- Can either be a minor threat or non-issue external or internal to the station, usually lacks the ability to communicate with crew in any significant way, and has very limited abilities at their disposal with an extremely simple self-serving direct objective.

# Examples
These are some examples of how to use categories/alignments when creating antagonists. These descriptions are illustrative examples only and may not reflect the actual designs of any current or future antagonists.

## Nukies: Major Team
Nukies are a Major Team Antagonist with the goal of getting to and setting off the station's nuclear self-destruct warhead. 

- They are a team-based antagonist because they start with a small limited team of players and they don't have an effective means of converting crew en-mass. They have reinforcements and borging but those are secondary mechanics and don't really qualify them as a conversion antagonist.

- They are a major antag because achieving their objective will result in the complete destruction of the station and they have access to very powerful weapons and tools to achieve their goals. They are also incentivized to engage in direct combat as their objective is in one of the most secure areas on the station and their equipment is primarily combat focused.

- The tendency for them to engage directly in combat, their very identifiable equiptment and round-ending objective, very clearly solidifies them into the category of major antag.

## Blob: Major Conversion
Blob is a Major Conversion Antagonist with the goal of self-replicating and overtaking the entire station.

- They are a conversion-based antag because the intial starting blob core is very weak and vulnerable, however as the blob expands across the station it gains more power. Additionally, blobs can convert crew members into blob zombies to help protect the core.

- They are a major antagonist because their goal is to expand and completely overtake the station and turn it into one giant blob organsim. Their abilities are initially very wealk however, they scale exponentially with time and the amount of space inhabited by the blob.

## Thief: Neutral Solo
Thief is a Neutral Solo Antagonist with the goal of stealing objective items to satisfy their kleptomania.

- The thief being a solo antagonist is self-explanitory.

- A thief's objective is to simply steal their objective items and not get caught. The objective itself isn't in conflict with the objectives of the crew, but stealing certain items may result in chaos ensuing on the station. This clearly makes the thief a neutral antagonist as they aren't directly in conflict with the crew.
