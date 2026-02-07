# Animation State Machine System

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| Ataman | Ataman | :x: No | TBD |

## Overview
This is a proposal to add a modular animation state machine (ASM) system that can be used to implement all kinds of temporary or persistent animations to entities like blinking eyes and waddling. The system would offer a framework consisting of timers, triggers, and conditions that can be defined in YAML to run these animations at the appropriate times.

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
- ```HasComponents```                     Is true if the entity contains all specified components. (For example: Coughing requiring a ```LungComponent```).
- ```MatchComponentPropertyValue```       Is true if the given component and datafield exists on an entity and has the specified value. (For example: Blinking requiring the ```MobStateComponent``` with ```CurrentState``` being ```MobState.Alive```.)

#### Triggers
Used to trigger state condition checks, for example:
- A small amount of periodically tested if-statements for stuff that doesn't have an event.
- A wrapper around event subscriptions (```SubscribeLocalEvent<TComp, TEvent>()```).
- A wrapper around ```BaseXOnTriggerComponent```
- ```ComponentAdded``` / ```ComponentRemoved```

An implicit trigger will be executed when entities enter the client's rendering area. 

The main reason for triggers is to minimize performance impact, as testing many conditions of several entities every frame could have a large impact.

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

## Decoupling visuals
As already mentioned, previous implementations of certain visuals used strongly coupled components and systems for each of their unique behavior. This proposal aims to reduce that coupling down to a minimum and allow contributors to focus on the fun part, animating, while all the technical stuff gets hidden behind the ASM implementation.

Blinking eyes could be implemented by inheriting an abstract class which overrides an ```Enter```/```Reset``` method and then add it to YAML.

Clown waddling could be implemented by inheriting another abstract method and overriding the ```GetNextAnimation``` and ```GetResetAnimation```.

Using a proof-of-concept implementation on my fork; making mice do a cute little hop from time to time merely required 50 lines of C# code (including boiler-plate and comments) and 13 lines of YAML.

## Animation conflicts
At the time of writing animation tracks cannot handle multiple animations editing the same property of a component simultaneously. The result is undefined animation behaviour. Due to this the ASM comes with the following drawback: A condition called ```AnimationNotRunning``` is added to the ASM, which must be used to prevent certain states from entering while other legacy animations are playing.

## AnimationStartedEvent engine addition
The ASM PR would be accompanied by an engine PR adding ```AnimationStartedEvent```. Used to support the previously mentioned ```AnimationNotRunning``` condition as the ASM would have to check this condition on every frame otherwise.

## Animations don't support YAML
While YAML defineable animations would be preferable, this is doable using hardcoded animations. If animations ever support YAML, the system can easily be updated to use those instead.

## New Types
- ```AnimationStateMachinePrototype```      Prototype for defining state machines.
- ```AnimationStateMachineComponent```      Component to hold all state machines of an entity.
- ```AnimationStateMachineSystem```         Client-side only system to execute the ASM's of all entities inside the players rendering view.
- ```AnimationStateMachineState```          Abstract base type for ASM states.
- ```AnimationStateMachineTrigger```        Abstract base type for triggers.
- ```AnimationStateMachineTimer```          Abstract base type for timers.
- ```AnimationStateMachineCondition```      Abstract base type for conditions.
