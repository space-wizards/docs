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
5. A species must not be "deliberately" bad or unusually challenging to play.
6. A species must not represent a new challenge to moderation and adminning.
7. A species must be technically feasible to implement and maintain.
8. A species must not entirely circumvent one or more common gameplay elements of Space Station 14 without a suitable replacement.
9. A species must not be designed with a specific, critical flaw that, without that flaw, would make the species overpowered compared to other species

# Rules Details

### Rule 1: A Distinct Identity

Space Station 14 is a game about weird chaos on a weird space station. Specifically, it is a game themed to sci-fi and (some) fantasy tropes, with a focus on fulfiling a serious-yet-silly tone.

Species **must** be thematically and visually distinct from other species. It **should** be possible, via audio cues and examination of their sprite, to determine what species someone is, especially if that species has important combat abilities to consider.

If a species does not have a strong-enough distinction from another species, this is grounds for rejection. For example, a 'sharkperson' species with a big tail and a love of eating meat may be considered too similar in concept to a lizardperson.

At time of proposal, concept art, references and demonstrations are welcome to help illustrate this identity. If this species is played on downstreams or SS13 servers, showcasing their identity via a video is also welcome.

Remember that the most invested person in a character or creature design is always the creator. It is always on the proposer of a species to prove why a species is sufficiently interesting to be a candidate for upstream.

Species **may** be inspired by, and follow design cues from, external IP and inspirations. However, in these cases, the species **must** be able to stand on its own feet (if it has them) and be extensible and maintainable by maintainers long into the future. For example, a proposed species might be inspired by a lion-headed alien species in a comic the author of the proposal is a fan of, and they may reference that species in their proposal. However, a species **must not** be a close or direct lift of the original concept, and must show effort and consideration for Space Station 14's style and tone.

A species **must not** have an ability, theme, gimmick or otherwise that is only existant or relevant for servers that require roleplaying. This sort of design is suitable to HRP servers, but Wizard's Den species must be compatible with all levels of roleplay. For example, a species that has a capitalistic culture might spawn with some of their culture's currency to make trades with. Without a mechanical underpinning for this, this concept cannot be reliably explored on non-HRP servers, and is to be avoided. 

### Rule 2: New Features and Tech Improvements

A species **must** represent an opportunity for evolving the Space Station 14 design space or codebase. This can involve either:
* a completely new feature
* a significant remix of an existing feature, 
* fixing or overhauling an area of the codebase
* exploration of a design idea that has not been done before

This new feature or design idea **must** be non-trivial, and likely to be interacted with by a player semi-frequently during gameplay, and cannot be trivially accomplished by a common item separately.

For example, a dragon-themed species might be able to snort enough fire to light a cigarette (or a plasma-filled room). Whilst this is an interesting gimmick, it is unlikely to come up in gameplay often enough to be impactful, especially when the monkey next to them can accomplish the same effect with a welding torch.

New species proposals **must not** attempt to use quantity of features to circumvent this rule. It is not acceptable for a species to be proposed with several "bolt-on" features in lieu of of a centrally interesting one.

It is not uncommon for a species to be proposed that is almost or completely achievable via new assets alone, with some tuning of an existing species' properties. These species are often ideal for downstream servers, but would not meaningfully improve the ability for Wizard's Den to iterate on the game and make it better for everyone. This is more important than supporting every niche within the wider Space Station 14 playerbase (see The Golden Rule, above).

In certain circumstances, a species that demonstrates a sufficiently interesting use of current mechanics, potentially in service of some other in-development content, **may** be granted exemption from this rule (see The Golden Rule above).

### Rule 3: Balance

Species **must** be conceptually within the power window of humans, slimepeople, and the other roundstart species. Species proposals **must** articulate the general upsides, downsides and sidegrades a player will encounter when playing that species.

 A species **does not** need to be completely balanced at the point of proposal; simply that it is **capable** of being balanced by the one implementing the species, and kept balanced in the future by maintainers, without removing or drastically altering the theme and design of the species.

 It is not neccessary to fine-tune balance at point of proposal. "This species is better in cold climates and moves slowly in warm ones" is preferable to "this species takes 20% less cold damage and moves 20% slower when in environments above its own core temperature".

 It is actively discouraged to "bolt-on" upsides and downsides that distract from the core theme and identity of the species, especially at time of proposal. A species' design is far more important, and far harder to fix, than its mechanics.

 A species **must not** be intentionally designed in a way that makes them specifically good or bad at one particular job on the space station. For example, a short, bearded humanoid species fond of drink and industry should not be, by design, better at being a miner or salvager than any other member of the crew. An ability they have that is useful in those roles should also be useful in other roles.

 It is acceptable for a species to be *emergently* better at some aspect of a job. For example, a species with a tail that can pull things might be better than average at moving crates around the station, which is valuable to a Cargo team. But this is a skill that is useful broadly, rather than being focussed on one particular discipline. Other species should not feel comparatively less capable at a job than any one specific species.

 A species **must not**, under **any** circumstances, be designed in a way that makes them unusually good or unusually bad at combat. Combat is an essential part of Space Station 14, and species with wildly divergent abilities make the act of balancing it extremely difficult.

 ### Rule 4: Speciesism

 Speciesism is banned on Wizard's Den in its entirety. As such, species **must not** directly encourage the "othering" of those that play those species - for example, causing health problems in those around them, or being incapable of socializing or interacting healthily with the rest of the crew.

 ### Rule 5: Deliberately Challenging Species

 Species **must** not be designed in such a way that a new player, picking a random character and rolling that species, would have an excessively negative experience due to lack of game knowledge. This **does not** mean a species cannot have a notable, potentially deadly, downside. However, that downside **should** be recoverable from, presented obviously to a player who has no prior context of that species, and teachable within the game by other players.

 For example: a species suffers from oxygen poisoning. This means they must wear internals at all times, except in specific circumstances where oxygen is not present. This species **should not** punish the player by dying rapidly if their internals fail or are removed, and, if they do die, they **should** be revivable.

 If a species is significantly challenging to play as, compared to normal round-start species, the following rules apply:
 - It **must not** be able to be selected round-start by new players.
 - It **must not** be able to be picked if a random species is chosen.
 - It **should not** be added to the potential species drawn from for antagonists such as Nuclear Operatives.

 If a species is deliberately challenging to play, it **must** have design documentation outlining the intended challenge the species presents.
 
 Deliberately challenging species must **not** be designed in such a way as to promote speciesism (see Rule 4 above).

 Species that are deliberately challenging **must not** negatively impact round flow for other players. For example, a species may require being sealed in an airtight suit to avoid exploding. If the airtight suit is ruptured, it would be unacceptable if the resultant explosion commonly resulted in the deaths of those around them.

 ### Rule 6: Admin burden

 A species **must not** have a powerful mechanic or ability that creates burden for the in-game or out-of-game admin team, either by a requirement for rulings or increasing admin help chat load.

 A species **must not** require a specific admin policy in order to manage. For example, Diona nymphs may in-universe and mechanically transmit their former host's brain into a new form, but such a new form should be covered by normal new life/revival rules, not an expectation of the writing of a new, specific, rule. 

 ### Rule 7: Technical Feasibility

 Some more out-there designs for species are wholly within the sort of concept that Space Station 14 would love to have, but would represent a significant technical problem to implement or maintain. 
 
 For example, a species may be unusually large, requiring a 64x64px sprite. Because all clothing sprites are sprited for 32x32px, it would be technically unfeasible to support this species without an excessively-significant amount of respriting and aggressive use of displacement maps.

 The proposer of a species **should** be able to break down the technical workload required to bring the species to life, and **should** be capable of at least part of that workload themselves.

 ### Rule 8: Circumvention of Intentional Game Design

Species **must not** circumvent a significant portion of gameplay.

An example of circumventing gameplay would be an implementation of a robot species that allowed players to completely ignore the Medical department via self-repair with tools. Or, due to experiencing no equivalent to hunger or thirst, ever needing to visit the chef or bartender.

Another example would be a species with in-built protection against common combat mechanics. For example, a species that is immune to being stunned, shocked, or slipped. Such drastic alterations to a player's roundflow are more suitable to mid-round free agents and antagonists, such as closet skeletons, rat kings or space dragons. See also Rule 3 above.

### Rule 9: Overpowered Species With Critical Flaws

Species **must not** be balanced so as to be unusually powerful (so as to be strictly, objectively and clearly better in non-trivial ways) if not for a critical flaw reigning in their utility.

These species represent a balancing tightrope for maintainers, especially in a game with constantly-evolving content and balance, and such varied gameplay experiences round-to-round, such as Space Station 14.

An example of being held back by only one thing would be a species that has an unusually high amount of effective health but a major weakness to being stunned. Such extreme designs often work on paper, and may even work in practice on first implementation, but are vulnerable to being exploited by players past the point of being fun. In this example, the weakness to being stunned may be so bad as to make combat against the species entirely one-dimensional, or via the collection and use of specific in-game items and mechanics be evaded entirely, creating a species that requires a draining series of hotfixes and patches to bring back to effective parity.

# Modifying Species After Introduction

From time-to-time, a species that was previously added to Space Station 14 may be proposed for review by maintainers. This review would focus on that species' current quality and conformance to the above rules, and propose remediating remedies, if appropriate, to bring the species up to standard.

## Significant Modification to a Species

Additions and improvements to previously-created species are always welcome, but significant modification to a species involves significant modification to players's characters, which may be controversial.

Consultation should be taken from players before deployment of significant re-designs or changes in concept to a round-start species are merged to stable. This may involve seeking feedback from players on the test server about the changes, making players aware of the changes via the Discord, and so on.

## Removal of a Species

A species is the first and most important choice a player makes when building a Space Station 14 character. As such, removing species from the game effectively involves deleting players's characters. This sort of change can be controversial, and must be handled responsibly.

Outright removal of a species that has been deployed outside of an event (such as April Fool's) or a test-merge to Vulture **must be** agreed to by a maintainer vote, after consultation with the Wizard's Den player community. Alternative remediating steps should be considered first, and full deletion should be considered a last resort.

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
