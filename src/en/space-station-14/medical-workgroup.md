# Medical Work Group Document

## Overview
Given the split, unbalanced, and blatantly unfinished nature of this game's medical system it's necessary that the medical workgroup's responsibilities and limitations are in a public space such that they can be easily understood and read.

The medical workgroup is responsible for the medical system of Space Station 14 which includes but is not limited to: Damage, BodySystem, Reagents, Metabolism, and the Medical Department (including Chemistry). The goal of the medical workgroup is to nearly completely overhaul all of these systems to match the mechanical depth of Space Station 13's various medical systems.

To accomplish this impossible task I have set aside three basic responsibilites of the workgroup.

### Responsibiltiy 1: Maintaining Current Medical Balance

This comprises of two things, keeping medical balance static as microbalancing is bad and takes away from work we could put towards making it better, but also doing active maintenance on it. Fixing bugs, adding small features, code improvements, cleanup ect. 

Upstream medical balance should be in an "acceptable enough" state, and big changes should only be made if something has gone horribly wrong or needs fixing. New features should be scrutinized and only accepted if they are small and easily reversible or portable to a new medical system. Larger medical changes that may interfere with development should either be redirected to the development of a new medical system if possible, or closed/frozen depending on circumstances. 

Any new PRs for current med should be compliant with the great debodying no matter what or be closed at the discretion of the medical workgroup.

### Responsibility 2: The Great Debodying Cleanup

The bigger responsibility is "The great debodying." This must be enforced if we are to have a body system and complex medical systems.

All debodying should be compatible with the goals of the new medical system. Debodying is the most important step of the process because it makes building a new medical system a lot easier and gives us a lot more options to make changes without compromise.

Debodying comprises of two things:

#### 1. Removing the depdencency of all systems reliant on bodysystem or organ code in favor of event based and generic systems.
The current medical system is built on the assumption that BodyComponent is a guarantee on every controllable entity, from humans, to mice, to robots to even ghosts! This resulted in extremely rigid code that assumed that many entities would not only have a body, but that there would be specific organs that did specific things and if you wanted something even slightly different, you'd have to make a brand new system for it or add hardcoded into an existing system to add the behavior. 

This approach is not flexible enough to allow for a wide range of unique species, doesn't take advantage of ECS, and doesn't meet Wizden's current coding standards. As a result all code which iterfaces with, or relies on BodySystem and its related components needs to be reworked, refactored, or deleted. A homogenous entity without organs shouldn't need a BodyComponent to eat or breathe for example, but with the current medical implementation this is completely impossible. 

As a general rule of thumb: Anywhere that checks for a BodyComponent, we should be raising handleable events that body system hooks into and then has relevant organs handle. We should make as few assumptions as reasonably possible about what these events are doing. The less rigid the code, the more creatively contributors can use the system and the more flexible we can be with a new medical system. 

#### 2. Refactoring and cleaning up reagent code and attached reactive systems.
Reagent code is messy, broken, and comes with a lot of assumptions and workarounds that aren't nice.

As a goal, reagent code should be easy to understand, have a usable API, and its features should justify themselves. A lot of reagent code is made with the assumption it would be used for something someday, but that day never came to fruition. 

### Responsibility 3: Psycho-Med/Offmed

Psycho med is the name we've given to the planned medical system for upstream, and as a result the third responsibility is developing that system.

Offmed is an extension of Psychomed, it is a body-system agnostic medical system that simulates a lot of the behavior we want out of psycho-med without having to deal with the baggage of dealing with current body systems. 

It is the duty of the medical work-group to maintain and manage both for different and distinct reasons. 

#### Psycho-Med

Because of the massive changes required to make a new medical system happen, psycho-med development will need to be done in parallel to current upstream and reviewed and tested off of upstream. From there the system can be merged upstream in large feature complete chunks that would normally be unreviewable due to size and complexity. 

This gives us the leverage to make big sweeping changes while still being able to adequately test them and without the worry of breaking things or having to do big rollbacks that result in setbacks, delays, and loss of morale. 

As of writing, Psycho-Med has no current singular document for organizational reasons. 

Medical is an exceptionally large system with many aspects requiring a number of targeted documents and discussion for specific systems (solutions, metabolism, organd and body, damage ect.) 

In addition with refactoring still going on it would be jumping the gun to try and finalize any ideas which are not going to be completable in the near future. Instead we have a general [medical design doc](/departments/medical.md) which goes over what behavior is desired for a new medical system as well as a number of issues that need tackling. For more information consult @princesscheeseballs on Discord. 

#### Offmed

Offmed, aka "Offbrand-Medical" is an official-unofficial upstream medical system. Like other unofficial medical systems integrating into it comes with the baggage of potential upstream breaking changes and loss of support. Everything in Offmed is subject to change on a structural level as it is a testing bed for the features we want to see, not the finalized version of them in any capacity.

That being said, Offmed is meant to take advantage of the currently merged refactors and changes to bodysystem meaning it will evolve as psycho-med evolves. Consider it a look into the future of medical since a lot of the simulationist aspects are using smoke and mirrors tactics to avoid touching systems that still need refactoring or building. Features from offmed will be ported to psycho-med as needed and when we are able to. 

As such, offmed is not planned to be officially released in any permanent capacity. Releases and tests are handled by the medical work-group and are for testing purposes without obligation for long term support or a regular release schedule. 
