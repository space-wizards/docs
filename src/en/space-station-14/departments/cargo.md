# Cargo Department Design Document

## Core Concept

The Cargo department is one of the primary resource generators for the station and the main location for storing a lot of materials and items. Anyone can grab a parcel and deliver it, but what do you do when you have 30... 100? That is where the cargo department comes in, with a well coordinated cargo team and some well planned contraptions being able to deliver large numbers of materials and items and still have money left over afterwards.

## Introduction

Cargo is very simple, you sell things to get money, you use money to get things, you deliver those things. For a low number of items this can be very easy for even a complete novice to achieve. Two legs and a go-to attitude only go so far, and eventually anyone would be overwhelmed by the number of jobs left to do. That is where cargo needs to get creative, using the tools available to them to optimize and automate.

There is only so much a cargo department can achieve by itself, however. If they are going to be able to supply even greater quantities, they may need to rope in the science department for fancy tools or the engineering department for station expansions. If these departments work closely together, they should be able to achieve anything, with cargo as the backbone to supply it all.

Despite the potential complexity, cargo is the most accessible department for new people. It is possible for anyone to contribute, but also for anyone to follow and understand the complex setups which have been made. A person can stand in cargo for 10 minutes watching crates move and gain the confidence to set up their own conveyor belt. The whole may be complex, but each individual part can be understood just by looking at it.

## Design Pillars

### P1: Anyone can contribute.

Even the most inexperienced player should be able to contribute or help out in the department without needing a 30 minute explanation of the systems. There should be simple goals with clear paths to those goals; the path can get more complex for optimization, but there should always be a clear, potentially slower path.

### P2: Scale matters.

No solution to cargo's problem should scale neatly. But there should be a solution at every scale.

As cargo is sometimes required for other departments to access sections of their content, there must be easy ways to achieve the minimum that departments need. This method should be one that does not scale well, and if you tried to use it to deliver more items it would be unwieldy.

The same goes in the other direction, there should be ways to deliver a ludicrous amount of materials to departments, but they require extensive setup and planning to get right. A waste of time if you only need a few things.

These methods should not replace each other but have use cases in different areas, think: container ship, truck, plane deliveries. If you need something ASAP you can use a plane, if you need a lot you can use a ship, if you need flexibility you can use a truck.

### P3: Logistics and Storage is hard, but cargo excels at it.

Other departments should not have ways to trivialize storage. Practical limits should encourage requesting things from cargo when they have things in storage, and potentially giving cargo spare resources if they have too much, to avoid needing to store it all. Other departments should not feel like storage is a chore, however, but instead that cargo enables them to make storage easier and have the materials they need on hand.

Cargo should have the tools and space to store and organize large numbers of materials and items.

### P4: Collaboration is an engine.

The progression in cargo should not rely on just itself or just others. It should rely on both. This should be done using a feedback loop between departments. For example, the science department might be able to research an early tool to make cargo's job easier and allow them to deliver more materials. They may have a later tool which is an even more direct upgrade; this tool should be much more expensive in materials than the first tool, so that by first getting the first tool, the second becomes more achievable. There may be more helpful tools than this; they should take another order of magnitude jump in strain placed on cargo to acquire. The result of this is, even with infinite materials, science would still need to perform science to unlock the tools. Even with infinite science points, cargo wouldn't be able to jump straight to the end-game tools and would need to use the early ones to build up to it.

This feedback loop should exist wherever practical for departments, with the departments gaining access to material-expensive tools which can be acquired most easily by first helping cargo.

## Desired Gameplay
- First/second point of contact for a lot of base supplies and materials.
  - While not the only resource provider on the station, Cargo should be a reliable option when seeking out supplies. Having a solid foundation of materials always at the ready should be a goal to strive for. Cargo players should feel a desire to fulfill (reasonable) requests when they come in.
- Friction when unable to provide.
  - When resources run low (either due to a lack of work or outside influences) the reliability should come into question, with pressure to get back into operational quantities. A station without a working Cargo department should *feel* its absence, however, it should not prevent other departments from performing their role. No one should be waiting around for 20 minutes because Cargo is having problems.
- Stronger when crew helps.
  - Cargo's gameplay should encourage crew collaboration where crew will want to help. The resource generation the department provides should be catalyzed by non-Cargo personnel using their unique role responsibilities.

## Undesired Gameplay
- Having a strong internal positive feedback loop, cutting off the need for station collaboration.
  - As a department with the motivation to generate tangible rewards for itself, there is a risk of slipping into gameplay systems where it sees assisting other roles as wasting resources. Cargo gameplay should aim to encourage interactions with other crew. When possible, highjack the desire for progression with complementary systems enable collaborative gameplay.
- Isolationism.
  - Related to the point above. While Cargo has the ability to provide equipment to other departments, it shouldn't go so far as to make Cargo encouraged to supplant what those departments provide. If Cargo decides to do another department's duty, they should never be as good at it.
- Broken efficiency.
  - With a focus on efficiency Cargo is also at a risk of finding overpowered systems or strategies that invalidate gameplay in other areas. Features must be monitored and balanced to avoid this. If Cargo is rewarded without putting in the appropriate work the gameplay will feel hollow and unfun. 
