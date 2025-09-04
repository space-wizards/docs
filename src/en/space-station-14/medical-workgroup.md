# Medical Work Group Document

## Overview
Given the split, unbalanced, and blatantly unfinished nature of this game's medical system it's necessary that the medical workgroup's responsibilities and limitations are in a public space such that they can be easily understood and read.

The medical workgroup is responsible for the medical system of Space Station 14 which includes but is not limited to: Damage, BodySystem, Reagents, Metabolism, BodySystem, the Medical Department, and Chemistry. The goal of the medical workgroup is to nearly completely overhaul all of these systems to match the mechanical depth of Space Station 13's various medical systems.

To accomplish this impossible task I have set aside three basic responsibilites of the workgroup.

### Responsibiltiy 1: Maintaining Current Medical Balance

This comprises of two things, keeping medical balance static as microbalancing is bad and takes away from work we could put towards making it better, but also doing active maintenance on it. Fixing bugs, adding small features, code improvements, cleanup ect. 

Upstream medical balance should be in a "acceptable enough" state, and big changes should only be made if something has gone horribly wrong or needs fixing. New features should be scrutinized and only accepted if they are small and easily reversible or portable to a new medical system. Larger medical changes that may interfere with development should either be redirected to the development of a new medical system if possible, or closed and or frozen if not. 

Any new PRs for current med should be compliant with the great debodying no matter what or be closed at the discretion of the medical workgroup.

### Responsibility 2: The Great Debodying Cleanup

The bigger responsibility is "The great debodying." This must be enforced if we are to have a body system and complex medical systems.

All debodying should be compatible with the goals of the new medical system. Debodying is the most important step of the process because it makes building a new medical system a lot easier and gives us a lot more options to make changes without compromise.

Debodying comprises of two things:

#### 1. Removing the depdencency of all systems reliant on bodysystem or organ code in favor of more generic methods that anything can hook into.
Previous attempts to overhaul medical came with the assumption that bodysystem would be on every living entity, such that it was often used as a check for if an entity was a mob that was alive. This resulted in extremely rigid code that assumed that many entities would not only have a body, but that there would be specific organs that did specific things and if you wanted something even slightly different, you'd have to make a brand new system for it.

Needless to say, this coding approach does not flex the benefits of ECS and is not up to modern wizden coding standards. As a result, all of this code needs to be completely refactored or thrown out. 

As a general rule of thumb: Anywhere that checks for a body component, we should be raising handleable events that body system hooks into. And we should make as little assumptions as reasonably possible about what these events are doing. The less rigid the code, the more creatively contributors can use the system and the more flexible we can be with a new medical system. 

#### 2. Refactoring and cleaning up reagent code and attached reactive systems.
Reagent code is messy, broken, and comes with a lot of assumptions and workarounds that aren't nice.

As a goal, reagent code should be easy to understand, have a usable API, and its features should justify themselves. A lot of reagent code is made with the assumption it would be used for something someday, but that day never came to fruition. 

### Responsibility 3: Psycho-Med

Psycho med is the name we've given to the current medical project, and as a result the third responsibility is developing that system.

Because of the massive changes required to make a new medical system happen, psycho-med development will need to be done in parallel to current upstream and reviewed and tested off of upstream. From there the system can be merged upstream in large feature complete chunks that would normally be unreviewable due to size and complexity. 

This gives us the leverage to make big sweeping changes while still being able to adequately test them and without the worry of breaking things or having to do big rollbacks that result in setbacks, delays, and loss of morale. 

As of writing, Psycho-Med has no current singular document and due to the current size of the team one isn't needed. And as we are going to be merging Psycho-Med in large chunks, the need of a doc to close issues is not needed because any upstream medical changes fall under responsibilities 1 and 2. 
