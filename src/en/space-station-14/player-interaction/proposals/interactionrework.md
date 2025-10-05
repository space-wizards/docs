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

Infact, this all seems to be already outlined by the commends of both `ActivationVerb` and `InteractionVerb`
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

Initially switching to something like this would be pretty simple, just do the same thing we've already been doing for alt-activations.  
In practice many components across the whole game would need atleast some refactoring. For the most part this would *probably* just be tedious boilerplate replacing but due to the effective removal of simple interaction events, there will be alot more boilerplate for even simpler tasks.

There needs to be considerations for multiple components with interactions. How would priority work? You cant make multiple activation events on one entity due to the changes.
