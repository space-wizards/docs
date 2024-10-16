# Robust Development
> Build Your Own Net Dream
>
> BYOND is the premier community for making and playing online multiplayer
games. As a player, enjoy hundreds of games created by our community, by people
just like you. As a developer, make your own indie sensation with an
easy-to-learn language, built-in online support, tools for developers, and
plenty of articles and tutorials.


| Designers | Implemented | GitHub Links | Crazy                   |
|-----------|-------------|--------------|-------------------------|
| benev0    | :x: No      | not yet      | :heavy_check_mark: Once |

<!-- note to self: edit for (statement -> reason) structure -->

## Preamble
Nearly all of the concepts described here will require their own design
document. This document is intended to be a high level examination of issues
facing development. All issues mentioned in this document should be addressed
in this document but may not be fully specified. It should be clear that the
scope of this proposal and size of work is ***extreme***.

This proposal alters proposes taking on large quantities of technical dept. In
the documentation, this technical dept already exists and should be addressed.
In the module section new technical dept is created by respcifieding that
services should be extracted; this will require a retrofit of the core content
repo, SS14, and subsequently all forks. In the publishing section

<!-- Concept -->
## Concept
Robust Toolbox is an engine which like its predecessor, BYOND, handles nearly
all of the low level networking. Paired with a well known architecture ECS,
Robust Toolbox should be high in consideration for many projects; however,
there are three major issues.

1. Documentation & Examples
2. Robust Toolbox Standard Modules
3. Robust Toolbox Publishing & Monetization

<!--  Developer Story? -->
## A Humble Dev

<!-- Design Pillars -->
## Design Targets
### Clear development path

These issues should be addressed so that development does not require *side
quests* (reading or creating SS14 source); although, *side quests* may be
recommended in the docs but should not be used as a crutch.

### Do not require devs to reinvent the wheel

Common functionality such as database interaction should be abstracted into
modules which can be imported into user games.

This functionality should be sourced like the game from the community allowing
imports from a remote git repository while trusting the content.

### Publishing with Space Wizards should be mutually beneficial

Space Wizards and the game should mutually gain visibility by Space Wizards
allowing games to be published on the launcher and developers bring new players
to the launcher.

Developers should be free to publish their games without concern of harm by
other Developers by theft or defamation by other community members.

## Addressing the issues
### Documentation & Examples
<!-- why -->
#### Design Targets
1. Linear Tutorial

    Perspective Devs should be able to follow a single tutorial line which will
demonstrate all the engine functionality required to create a feature complete
game<!-- to be defined -->. This can and should include a basic project, but
should avoid copy paste syndrome.

    Avoid Recursion at any point where a writher types "we'll revisit this
concept later" should be scrutinized heavily, and a new ordering should be
considered.

2. Standard

    Every Writer has a different style, this is will create issues when style
seeps into document structure. Documentation will need a standard structure.

3. Simple

    While documenting minimize dependencies in examples, and provide the
smallest examples that demonstrate features.

4. Current

    The content will be kept up to date with the latest version of Robust
Toolbox. Any version release of Robust toolbox will have a parallel version of
documentation.

    Breaking changes and Method Deprecations must be noted in the documentation.

### Robust Toolbox standard modules
<!-- why -->
#### Design Targets
1. Community Driven

    Like Robust Toolbox and Space Station 14 Modules will be community driven,
that is created and managed by the community.

2. Documented

    Modules are adding functionally this functionally should be documented;
however, as these are community projects these standards will likely be very
relaxed. Recommended templates based off of official Space Wizards
documentation should be provided in the module creation documentation.

3. Easy Dependency Management

    Developers who add a module to their project should not need to add whole
non config files the maximum complexity should be that of adding a new
submodule to the repo.

4. Validated

    The Space Wizards community that is developers using robust toolbox should
be able to trust their submodules. Minimally complaints about submodules should
be able to be taken on the forums.

    Better Space Wizards could curate a set of quality module projects.

5. License Clarity

    Developers should know the repercussions of adding a RT-module before it is
added to their code. Licenses should be recommended RT-modules open source
monetizable and public domain licenses should be encouraged.

### Robust Toolbox Publishing & Monetization
[RobustHub](./robusthub.md) has some of the same goals.

<!-- why -->
#### Design Targets
1. Mutual Visibility

    Developers should be encouraged to publish their game on robust hub knowing
that it will be seen by new players. Developers who then advertize their game
outside of the hub will pull additional players.

    The Hub should not mask games by being named for another game in any
location launcher, site, steam, etc.. This is a Deviation form the RobustHub
proposal.

2. Effectively Moderated

    The current strike rules are acceptable; however, the procedure in this
[document](../community/space-wizards-hub-rules.md) should be more formal. This
may require sending server contact info when hosting.

3. Safe Monetization

    Guidelines for taking player monetization including recommended procedures.
