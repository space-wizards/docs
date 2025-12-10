# Animation State Machine System

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| Ataman | Ataman | :x: No | TBD |

## Overview
This is a proposal to add an animation state machine (ASM) system which can be used to implement all kinds of temporary or persistant animations to entities like blinking eyes and waddling. The system would offer a framework consisting of timers, triggers and conditions that can be defined in YAML to run these animations at the appropriate times.

## Background
Things like blinking eyes and clown shoe waddling have been implemented in the past by creating whole specialized systems for their sole task of running very simple animations under certain conditions. In almost every PR for these, one can find comments wishing for a more generalized animation system that could be used instead.

## Features to be added
### Animation State Machine
The ASM consists of a system and components (running client side as much as possible) to trigger animations under certain conditions all defined in YAML. Since an entity might need to run multiple animations simultaneously, the component consists of a list of ASMs to run in parallel.

Each ASM state consists of conditions, triggers and timers resulting in the execution of a singular animation. 

### Conditions, Triggers and Timers
In order to define when these animations are supposed to run, we require hardcoded types for use in YAML. Some examples include:

#### Conditions
These are checked and must return true for the specified animation state to run.
- ```HasComponents```: Is true if the entity contains all specified components. (Example: Coughing requiring a ```LungComponent```).
- ```MatchComponentPropertyValue```: Is true if the given component and datafield exists on an entity and has the specified value. (Example: Blinking requiring the ```MobStateComponent``` with ```CurrentState``` being ```MobState.Alive```.)

#### Triggers
Used to trigger state condition checks, for example:
- A wrapper around ```SubscribeLocalEvent<TComp, TEvent>()``` used for reacting to arbitrary events.
- ```ComponentAdded```/```ComponentRemoved```.

An implicit trigger is also executed when entities enter the client's rendering area. 

The main reason for triggers minimize performance impact. Testing many conditions of several entities every frame would have a large impact on performance.

#### Timers
Allow animations to be played at fixed or random intervals
- ```RandomTimeRangeTimer```: Fires at random intervals inside a defined range. (Examples: Blinking, Coughing)
- ```TimeIntervalTimer```: Fires at fixed intervals. (Example: Blinking indicator light)

## Game Design Rationale
Animations are great for adding flavor and immersion to the game in many ways, the above mentioned examples just being a few. They add immersion for everybody, even the smallest mice. However, animations are currently difficult to implement properly and require not only coding knowledge for the animation itself but for the system running said animation in the first place as well.

## Roundflow & Player interaction
This is a background system, it does not affect roundflow and never requires a player to interact with it.

## Administrative & Server Rule Impact (if applicable)
N/A

# Technical Considerations
## General
Ideally, the whole system should run client side. To account for triggers that depend on events which happen outside a player's rendering view; all state conditions are tested once an entity comes into view. If this should impact performance, a flag will be added to disable this trigger for animations where it's irrelevant.

Performance impact heavily depends on how the concrete states will be implemented. Defining a handful of timers running at 0.1s seconds interval with badly chosen conditions could have a  noticeable performance impact. This issue can be migitated by implementing a hard coded minimum interval however.

This proposal ignores multi-state machines in favor of not adding even more complexity to an already complex implementation.

## Animations don't support YAML
While YAML defineable animations would be preferable, this should be doable using hardcoded animations. If animations ever support YAML, this system can easily be updated to use those instead.

## SpriteComponent changes/refactor, yes or no?
While a refactor of SpriteComponent has some advantages like not adding another system and automatically upgrading all sprites with ASM availability; this proposal is using an independent system due to the following reasons:
- The ASM could be used for more than sprites, i.e.: sound cues for coughing.
- An independent system can be added and removed more easily from the engine.
- The component can be isolated to those entities that need it. (A piece of paper probably doesn't need animations).

## New Types
- ```AnimationStateMachineComponent``` Component to hold all state machines of an entity and their state.
- ```AnimationStateMachineSystem``` Client-side only system to execute the ASM's of all entities inside the players rendering view.
- ```AnimationStateMachineState``` Abstract base type for ASM states.
- ```AnimationStateMachineTrigger``` Abstract base type for triggers.
- ```AnimationStateMachineTimer``` Abstract base type for timers.
- ```AnimationStateMachineCondition``` Abstract base type for conditions.
