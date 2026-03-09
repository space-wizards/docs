# Personal AI (pAI)
<!--
`Designers` should be the names that you use on GitHub and/or Discord. This is optional but strongly recommended, since:

- This acknowledges credit where it is due
- People who are confused about the written intent can use this information to contact the authors

`Implemented` is the status of the feature.

Github links can include multiple PRs, if relevant.
-->

| Designers                                                                         | Implemented     | GitHub Links |
|-----------------------------------------------------------------------------------|-----------------|--|
| Velken | :white_check_mark: Yes | [#42344](https://github.com/space-wizards/space-station-14/pull/42344) |

## Overview

<!-- A very short, maybe three sentence summary of what this proposal is about. A high level "overview" or "what this adds". -->

This is for the ghost role pAI - which is to help answer any frequently asked questions for pAIs and to help others understand what the pAIs are about.

Personal AIs in short are helpers to their holders, and are meant to give assistant to their owner.
A pAI are not proper silicion, but a companion that acts as a sapient tool-secretary for their owner.

## Background

<!--
Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game.

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.
-->

Personal AI devices are commonly found around the station. Their existance is of a companion to help their owner.

Their general goal is to be an assistant, be it by helping remember something, yell for help or even using their abilities.



## Features to be added

<!-- Give a description of what game mechanics you would like to add or change. This should be a general overview, with enough details on critical design points that someone can directly implement the feature from this design document. Exact numbers for game balance however are not necessary, as these can be adjusted later either during development or after it has been implemented, but mention *what* will have to be balanced and what needs to be considered when doing so. -->

Personal AIs need more abilities to be purchasable, as their current options is very limited.

Some of the pAIs abilities are locked from the store if they don't have the valid corresponding access in the ID that is inserted with them in the PDA. And become unable to use said abilities while not having the required access.
More ways to limit what conditions a pAI needs to meet to unlock more actions are always desired, as they create a roundflow of players going after those conditions to improve their companions.
More variants for pAIs and customization of them are also a desired options.

## Game Design Rationale

<!--
Consider addressing:
- How does the feature align with our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosphy?
- What makes this feature enjoyable or rewarding for players?
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- How does it enhance player cooperation, competition, or emergent gameplay?
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?
-->
Personal AIs have access to a lot of information, but have lack of autonomy, including talking in comms directly, this locks them to being assistants instead of independent actors.
The lack of autonomy allows to give pAI some more powerful abilties, that would, otherwise, not be given to a crew member.
However, there is a limit on how powerful those abilities should be, and it should never exceed to a point where one starts to get multiple pAIs to have several abilities at once, their memory store has limited funds specifically so that they must be careful with what they choose.

A pAI should always be able to:
- Talk;
- See its surroundings;
- Know who their owner is;

A normal pAI should NEVER be able to:
- Move on its own;
- Harm their owner directly;
- Talk in comms;

The abilities a pAI buys in the store should be a choice of the pAI, but, their owners can give them instructions on what would best suit the needs. Once a pAI entity has bought an action, that cannot be undone for anything easier than getting a new pAI device, this is to prevent pAIs from just cycling their actions to have access to all available in their store.

There can variants for pAIs, one such example, is the syndicate pAI, which has access to talk in the syndicate channel, it is not a direct antagonist, but it is of antagonistic origin, and should be siding with its owner's side.
