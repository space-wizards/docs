# Short, Properly Capitalized Title

Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar.

| Designers | Coders | GitHub Links |
|---|---|---|
| your names here | coder names here | PR Links, or None |

`Designers` should be the names that you, the authors of this document, use on GitHub and/or Discord. This is optional but strongly recommended, since:

- This acknowledges credit where it is due
- People who are confused about the written intent can use this information to contact the authors

`Coders` should be the names of the contributors who plan on implementing this feature. To get a design doc approved you will need either
- have the technical knowledge to be able to implement the proposed feature yourself.
- have someone else who agreed to do this for you.
- already have an existing implementation elsewhere that just needs to be ported.

In either case you will have to write an outline on how you plan to playtest this feature in the **Playtest** section to show that it is technically sound and feasible.

`Github Links` should be updated as they are merged and may include multiple PRs, if relevant.

## Overview

A very short, maybe three sentence summary of what this proposal is about. A high level "overview" or "what this adds".

## Background

Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game, and other features motivating this feature. 

If there's been past iterations of the feature, make sure to include what did and did not work with those attempts, and how your feature is different. What lessons could be learned, and how are you addressing them?

## Design Pillars

Understanding how your feature fits into the game on a game design level is very important. Space Station 14's goal is to create specific types of gameplay and moments for players that make the game engaging, so your feature needs to show how its mechanics and aesthetics achieve those things. Explaining this also makes it easier for future developers to understand what impact your feature is trying to have, so that new changes or additions to the game preserve what makes your feature work. For this, it's recommended you establish a few "design pillars", i.e. the core design ideals that your feature is attempting to achieve. Try to motivate them based on our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosophy.

Consider addressing:
- What feeling should players have when they interact with this feature? Is it different for different roles?
- What uniqueness does the feature bring to players? What makes it engaging for players? Why is it important? 
- SS14 is a game that strongly encourages players to interact with each other. How does the feature enhance player cooperation, competition, or emergent gameplay?
- How does the feature's design pillars align with the game's core design pillars? How do they strengthen the game in that regard?

## Game Mechanics & Features

Give a description of what game mechanics you would like to add or change. This should be a general overview, with enough details on critical design points that someone can directly implement a playtest from this design document. Exact numbers for game balance however are not desired, as these will be adjusted later either during development or after it has been implemented, but mention *what* will have to be balanced and what needs to be considered when doing so.

``` admonish "Implementation & Reference Document"
This section should be expanded upon as your proposal envolves into being an Implementation and Reference Document. 
```

## Game Design Rationale

With the mechanics described, this section should address how they relate to feature's design pillars and the game's [Core Design Principles](../space-station-14/core-design/design-principles.md). 

Consider addressing:
- What purpose do the different mechanics serve from a game design perspective? How do they align with the feature's design pillars?
- How well does the feature gel with other features already in the game? Is it at odds with other mechanics? 
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How unique are the mechanics to this one feature? Can they be used elsewhere in the game, or are they specialized to just this single feature? How could they interact with other systems?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?

``` admonish "Implementation & Reference Document"
This section should be expanded upon as your proposal envolves into being an Implementation and Reference Document. 
```

## Playtesting 

- How should this feature be playtested? Are you able to do it via prototype uploads, or do you need an experimental branch? Is this already available on a downstream server?
- Are there any uncertainties you would like to see in the playtest? What are your biggest concerns?
- What would be the scope of the playtest? What is the bare minimum you would need to implement to feel that the playtest accurately represents the feature?

``` admonish "Proposal Document"
This section should be removed once your proposal moves into being an Implementation Document.
```
