# Animation State Machine System

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| Ataman | Ataman | :x: No | TBD |

## Overview
This is a proposal to add an animation state machine (ASM) system that can be used to implement all kinds of temporary or persistent animations to entities like blinking eyes and waddling. The system would offer a framework consisting of timers, triggers, and conditions that can be defined in YAML to run these animations at the appropriate times.

## Background
Things like blinking eyes and clown shoe waddling have been implemented in the past by creating specialized systems for their sole task of running simple animations under certain conditions. In almost every PR for these, one can find comments wishing for a more generalized animation system that could be used instead.

## Features to be added
### Animation State Machine
The ASM will consist of a system and components (primarily client-side) to trigger animations under certain conditions, all defined in YAML. Since an entity might need to run multiple animations simultaneously, the component will consist of a list of ASMs to run in parallel.

Each ASM state will contain conditions, triggers and/or timers resulting in the execution of a single animation. 

### Conditions, Triggers, and Timers
In order to define when these animations are supposed to run, hardcoded types for use in YAML are required, for example:

#### Conditions
These will be checked and must return true for the specified animation state to run.
- ```HasComponents```                     Is true if the entity contains all specified components.
                                              (For example: Coughing requiring a ```LungComponent```).
- ```MatchComponentPropertyValue```       Is true if the given component and datafield exists on an entity and has the specified value.
                                              (For example: Blinking requiring the ```MobStateComponent``` with ```CurrentState``` being ```MobState.Alive```.)

#### Triggers
Used to trigger state condition checks, for example:
- A wrapper around ```SubscribeLocalEvent<TComp, TEvent>()``` used for reacting to arbitrary events.
- ```ComponentAdded``` / ```ComponentRemoved```

An implicit trigger will be executed when entities enter the client's rendering area. 

The main reason for triggers is to minimize performance impact, as testing many conditions of several entities every frame could have a large impact on performance.

#### Timers
Allow animations to be played at fixed or random intervals
- ```RandomTimeRangeTimer```                Fires at random intervals inside a defined range. (For example: Blinking, Coughing)
- ```TimeIntervalTimer```                   Fires at fixed intervals. (For example: Blinking indicator light)

## Game Design Rationale
Animations are great for adding flavor and immersion to the game in many ways, the above mentioned examples just being a few. Animations are currently difficult to implement correctly and require coding knowledge of animations as well as the system running said animations. The new system would be much easier to use, especially once YAML support for animations is implemented.  

## Roundflow & Player interaction
This will be a background system, it will not affect roundflow and should never require a player to interact with it.

## Administrative & Server Rule Impact (if applicable)
N/A

# Technical Considerations
## General
Ideally, the whole system should run client side. To account for triggers that depend on events which happen outside a player's rendering view; all state conditions need to be tested once an entity comes into view. If this should impact performance, a flag will be added to disable this trigger for animations where it's irrelevant.

Performance impact will heavily depend on how states are implemented. Many timers running at short intervals with subpar conditions could have a noticable performance impact - this can be mitigated through hard coded minimum intervals. 

This proposal ignores multi-state machines in favor of not adding more complexity to an already complex implementation.

## Animations don't support YAML
While YAML defineable animations would be preferable, this should be doable using hardcoded animations. If animations ever support YAML, this system can easily be updated to use those instead.

## SpriteComponent changes/refactor, yes or no?
While a refactor of SpriteComponent has some advantages like not adding another system and automatically upgrading all sprites with ASM availability; this proposal is using an independent system due to the following reasons:
- The ASM could be used for more than sprites, for example: sound cues for coughing.
- An independent system can be added and removed more easily from the engine.
- The ASM component can be isolated to those entities that need it. (A piece of paper probably doesn't need animations).

## New Types
- ```AnimationStateMachineComponent```      Component to hold all state machines of an entity and their states.
- ```AnimationStateMachineSystem```         Client-side only system to execute the ASM's of all entities inside the players rendering view.
- ```AnimationStateMachineState```          Abstract base type for ASM states.
- ```AnimationStateMachineTrigger```        Abstract base type for triggers.
- ```AnimationStateMachineTimer```          Abstract base type for timers.
- ```AnimationStateMachineCondition```      Abstract base type for conditions.
