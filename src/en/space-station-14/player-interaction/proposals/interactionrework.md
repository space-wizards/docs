# Verb-Centric Interactions

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| scattagain | scattagain | :x: No | TBD |

## Overview

*to prevent confusion, clicking refers to what the game calls interacting (by default, left clicking), and interacting refers to all direct actions that can be taken on an entity.*

This proposal aims to rework entity interactions to centered around verbs.
The main premise is that activating, alt-activating, and clicking will effectively be shortcuts to verbs on that entity.

## Background

This came from a failed attempt at a feature I wanted in the game, a simple "interaction hints" screen element (similar to many other games) which tells the user before they do something, what your buttons do in the current context.  
Soon I found out that this was unfortunately impossible due to how the game is structured, theres no real way to reliably get information like that.

*Due to the nature of this proposal and my reasoning for it, my original feature idea will come up alot, especially in [Game Design Rationale](#game-design-rationale)*

## Features to be changed

Currently, alt-activating will trigger the first `AlternativeVerb` on that entity. Ideally, the same should be done with `ActivationVerb` and `InteractionVerb`.  
Clicking would attempt at an `InteractionVerb`, but would fallback to an `ActivationVerb` if necessary.

Infact, this all seems to be already outlined by the comments of both `ActivationVerb` and `InteractionVerb`
- `ActivationVerb`
  > These are verbs that activate an item in the world but are independent of the currently held items. For
  > example, opening a door or a GUI. These verbs should correspond to interactions that can be triggered by
  > using 'E', though many of those can also be triggered by left-mouse or 'Z' if there is no other interaction.
  > These verbs are collectively shown second in the context menu.
- `InteractionVerb`
  > These verbs those that involve using the hands or the currently held item on some entity. These verbs usually
  > correspond to interactions that can be triggered by left-clicking or using 'Z', and often depend on the
  > currently held item. These verbs are collectively shown first in the context menu.

## Game Design Rationale

This would, ideally, make interactions more consistent between components and entities that share the same component.

In the case of the interaction hints, it could help dramatically in guiding new players into the controls of the game and even prove useful to more experienced players finding faster ways to do things they were previously doing with the verbs menu.  
It would prevent, or at the very least lessen, accidents made by incorrect assumptions.  
It would hopefully make interactions feel more fluid and predictable.

# Technical Considerations

Issues with "prediction"; in many cases where verbs can only be decided on the server which has to be sent over the client, causing a delay while this happens.
This is a much bigger issue than this proposal can cover (See [this comment](https://github.com/space-wizards/docs/pull/525#issuecomment-3368646645) and its links).

Due to that and the nature of this change many systems across the whole game would need atleast some refactoring to support prediction and use verb interaction, some of which are entirely impossible (or atleast without heavy changes to its logic) such as atmos logic.

There needs to be considerations for multiple components with interactions. You cant make multiple activation events on one entity due to the changes so some sort of priority system needs to be implemented.
