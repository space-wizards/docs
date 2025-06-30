# Species Guidelines

This document covers the policy for the acceptance and maintenance of proposed playable roundstart species on Wizard's Den servers. This document exists as both the direct rules and a further set of soft principles for proposing, developing and maintaining roundstart species for Space Station 14. 

## Why These Guidelines Exist

Selection of species is the first and most important decision a player will make at character creation. Space Station 14 is a game that encourages emotional connection and roleplaying, and this means that, once a character is created, it is very challenging for maintainers to "un-make" that character by removing the species from the game, or even significantly altering that species, should its design be found wanting. As such, species must be held at a high standard to be accepted.

In addition, species are a key aspect of the game's themes and setting. A level of consistency is required to ensure that the world remains immersive and engaging for all players.

Finally, species are often the cause of lengthy debates, especially for new species proposals. This policy document exists to guide discussion of species and ensure that this time can be better spent.

## The Golden Rule

Wizard's Den maintainers always have the final say on the content that they do or do not want on upstream. Everything in this document can be overruled by maintainer consent.

If Wizard's Den declines to accept a new species to upstream, this should not be considered a snub of the species concept as a whole. The objective of Wizard's Den is to provide a standardized - and fun - template for Space Station 14 servers run by many other groups. Downstreams having more content than upstream, with more ability to be experimental, and accepting content more easily, is a good thing, and all development is welcomed for the continued health of the game.

## Porting from SS13 and SS14 downstreams

From time-to-time, a species with significant popularity either on notable Space Station 13 servers or Space Station 14 downstreams may become in-demand for players on Wizard's Den.

**Being a popular species does not grant an automatic right to being upstreamed to Wizard's Den**. That said, popular species often gain momentum behind them that can iterate, sometimes repeatedly, until a good proposal is found.

All species must be considered fairly and equally for proposal, implementation and maintenance. Provenance is not a replacement for quality.

# Rules Summary

1. A species must have a **distinct identity** that is notably different in theme from the other species available on Wizard's Den.
2. A species must represent a **new feature or opportunity for technical improvement**.
3. A species must be, at least conceptually, reasonably balanced with the other species available on Wizard's Den.
4. A species must not be "othered" via its mechanics. Mechanics that directly encourage speciesism will be rejected.
5. A species must not be "deliberately" bad or unusually challenging to play (except for Plasmamen).
6. A species must not represent a new challenge to moderation and adminning.
7. A species must be technically feasible to implement and maintain.
8. A species must not circumvent or be fatally held back from greatness by a common gameplay element of Space Station 14.

# Rules Details

### Rule 1: A Distinct Identity

Species **must** be thematically and visually distinct from other species. It **should** be possible, via audio cues and examination of their sprite, to determine what species someone is, especially if that species has important combat abilities to consider.

If a species does not have a strong-enough distinction from another species, this is grounds for rejection. For example, a 'sharkperson' species with a big tail and a love of eating meat may be considered too similar in concept to a lizardperson.

At time of proposal, concept art, references and demonstrations are welcome to help illustrate this identity. If this species is played on downstreams or SS13 servers, showcasing their identity via a video is also welcome.

Remember that the most invested person in a character or creature design is always the creator. It is always on the proposer of a species to prove why a species is sufficiently interesting to be a candidate for upstream.

### Rule 2: New Features and Tech Improvements

A species **must** represent an opportunity for evolving the Space Station 14 codebase. This can involve either a completely new feature or a significant remix of an existing feature, representing the opportunity for code improvement.

It is not uncommon for a species to be proposed that is almost or completely achievable via YAML and assets alone. These species are often ideal for downstream servers, but would not meaningfully improve the ability for Wizard's Den to iterate on the game and make it better for everyone. This is more important than supporting every niche within the wider Space Station 14 playerbase (see The Golden Rule, above).

In certain circumstances, a species that demonstrates a sufficiently interesting use of current mechanics, potentially in service of some other in-development content, **may** be granted exemption from this rule (see The Golden Rule above).

### Rule 3: Balance

Species **must** be conceptually within the power window of humans, slimepeople, and the other roundstart species. Species proposals **must** articulate the general upsides, downsides and sidegrades a player will encounter when playing that species.

 A species **does not** need to be completely balanced at the point of proposal; simply that it is **capable** of being balanced by the one implementing the species, and kept balanced in the future by maintainers, without removing or drastically altering the theme and design of the species.

 It is not neccessary to fine-tune balance at point of proposal. "This species is better in cold climates and moves slowly in warm ones" is preferable to "this species takes 20% less cold damage and moves 20% slower when in environments above its own core temperature".

 It is actively discouraged to "bolt-on" upsides and downsides that distract from the core theme and identity of the species, especially at time of proposal. A species' design is far more important, and far harder to fix, than its mechanics.

 ### Rule 4: Speciesism

 Speciesism is banned on Wizard's Den in its entirety. As such, species **must not** directly encourage the "othering" of those that play those species - for example, causing health problems in those around them, or being incapable of socializing or interacting healthily with the rest of the crew.

 ### Rule 5: Deliberately Challenging Species

 Species **must** not be designed in such a way that a new player, picking a random character and rolling that species, would have an excessively negative experience due to lack of game knowledge. This **does not** mean a species cannot have a notable, potentially deadly, downside. However, that downside **should** be recoverable from, presented obviously to a player who has no prior context of that species, and teachable within the game by other players.

 For example: Vox suffer from oxygen poisoning. This means they must wear nitrogen internals at all times, except in specific circumstances where oxygen is not present. Vox **should not** rapidly die if their internals fail or are removed, and, if they do, **should** be revivable. 

 This rule has a specific carve-out for one, and only one, species: Plasmamen, who **must not** be able to be selected roundstart by unqualified newbies.

 ### Rule 6: Admin burden

 A species **must not** have a powerful mechanic or ability that creates burden for the in-game or out-of-game admin team, either by a requirement for rulings or increasing admin help chat load.

 A species **must not** require a specific admin policy in order to manage. For example, Diona nymphs may in-universe and mechanically transmit their former host's brain into a new form, but such a new form should be covered by normal new life/revival rules, not an expectation of the writing of a new, specific, rule. 

 A species **must not** have an ability, theme, gimmick or otherwise that is only existant or relevant for servers that require roleplaying. This sort of design is suitable to HRP servers, which Wizard's Den notably runs zero of.

 ### Rule 7: Technical Feasibility

 Some more out-there designs for species are wholly within the sort of concept that Space Station 14 would love to have, but would represent a significant technical problem to implement or maintain. 
 
 For example, a species may be unusually large, requiring a 64x64px sprite. Because all clothing sprites are sprited for 32x32px, it would be technically unfeasible to support this species without an excessively-significant amount of respriting and aggressive use of displacement maps.

 The proposer of a species **should** be able to break down the technical workload required to bring the species to life, and **should** be capable of at least part of that workload themselves.

 ### Rule 8: Circumvention of, or Deliberate Limitation by, Intentional Game Design

Species **must not** by themselves either circumvent a significant portion of gameplay or only be held back from obvious imbalance by some specific critical vulnerability.

An example of circumventing gameplay would be an implementation of IPCs, a common roundstart robot species, that allowed those IPCs to completely ignore the Medical department. Or, due to experiencing no equivalent to hunger or thirst, ever needing to visit the chef or bartender. Another example would be a species with in-built protection against common combat mechanics. For example, a species that is immune to being stunned, shocked, or slipped. Such drastic alterations to a player's roundflow are more suitable to mid-round free agents and antagonists, such as closet skeletons, rat kings or space dragons.

An example of being held back by only one thing would be a species that has an unusually high amount of effective health but a major weakness to being stunned. Such extreme designs often work on paper, and may even work in practice on first implementation, but are vulnerable to being exploited by players past the point of being fun. In this example, the weakness to being stunned may be so bad as to make combat against the species entirely one-dimensional, or via the collection and use of specific in-game items and mechanics be evaded entirely, creating a species that requires a draining series of hotfixes and patches to bring back to effective parity.

# What To Do If Your Species Is Declined

If you have not found success in your concept for a new species, there are a few options you can take.

## Submit to a downstream instead

Downstreams fulfil specific niches and do not have the same development and maintenance requirements as Wizard's Den. As such, many downstreams would gladly accept a design that Wizard's Den has passed on. In time, these downstreams may iterate and develop these designs into one that Wizard's Den could accept.

## Create a "subspecies" via markings

Consider if your idea for a species could instead be done via new markings or other extensions to a current species. For example, a "synthetic lizardperson" species does not need to be a specific species in its own right to still be readable and playable as this concept on Wizard's Den.

## Create the sprites and sound effects anyway

There is a serious lack of sprite and audio variety for Space Station 14 servers. Even if the exact right balance of design and features for your species has not been found, someone else might be able to "carry the torch" in the future and finally get a proposal accepted.

## Collaborate and Try Again

Consider what the problems with your proposal are and talk to others about them. See if other people have ideas or suggestions. Research species on downstreams and talk to maintainers about what they'd be interested in accepting.

Once you've done your research, create a new proposal and, within, explain what you've changed since your last proposal and why. Good luck!