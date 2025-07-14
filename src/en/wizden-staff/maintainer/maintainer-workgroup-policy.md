# Maintainer Workgroups
This document outlines Maintainer Workgroups, a subteam within the Maintainer staff group.

Workgroups consist of active maintainers that hold special knowledge on the workgroup's area.
These members generally define what the area is supposed to be, the problems of the area, what can be worked on to make the area better, and more.
The members of these groups hold more weight in discussions involving their workgroup as well.

## Justification
At the time of this document's creation (July 14, 2025), upstream Space Station 14's direction has largely halted and is undefined.
Discussions involving a design direction (ex. discussing the future of antagonists, departments, or large features) stall frequently or generate a lot of unnecessary friction.

This is largely due to the problem of having "too many cooks in the kitchen" so to speak.
There are a lot of Maintainers and Project Managers that have their own opinion or idea as to what something should be.
Furthermore, these Maintainers or Project Managers hold beliefs that aren't written down or are hard to refer back to.
This leads to even more friction when contributors work on their favourite department or want to implement a feature, as the contributor doesn't know what Maintainers want.

Currently, the upstream repository has ~800 pull requests that need reviewing.
Some of these pull requests are features that are not desired, or don't contribute well to a larger defined goal of what a department should be.
Simply merging these pull requests would lead to content bloat that crowds and distorts what an area should be—and closing them currently requires the input of two Maintainers that agree on the closure.
If they don't agree, a long voting process is started which draws out the process (and, to be honest, nobody wants to do them).

### Previous Implementation
Workgroups previously existed in the project, however, they were extremely passive and fell out of relevance.
These workgroups also contained members that did not frequently work on or play these departments.
This is undesirable—the leaders of workgroups should know firsthand what they're working with and what it should look like in the future.

## Goals
Maintainer workgroups plan to achieve the following:
1. **Define a real body to represent a game area and lead its design and development**
   - With this, contributors can directly interface with people that know the problems of the game area, what it should be in the future, and what they should work on.
   - The group can carve out their idea of what a department should be, writing directional design documents that help contributors see the future of a game area.
2. **Expedite pull request conceptual design review, and regulate pull requests that are not fit for a game area**
   - A small group focused on a game area can properly evaluate and approve or deny pull requests that don't work towards the group's defined future vision.

## Policy

### Formation
Workgroups are self-formed with the assistance of a Lead Maintainer, Project Manager, or Wizard, which helps create roles and a space for discussion in the upstream Discord.
These roles can also deny the workgroup's formation if it is deemed an unnecessary atomization or focus.

As few as **two** Maintainers can form a workgroup.

Additionally, workgroup members should fulfill the following criteria:
- They have worked on the SS14 area and/or have interacted with the area in-game extensively.
- They are an active Maintainer and participate frequently in discussions involving the game area on the Forums, Discord, or GitHub.

### Joining and Removal
The joining procedure is semiformal:
1. A Maintainer contacts a member of the group and asks to join. A member of the group can also nominate a person to join the group.
2. A vote must be created, for three days, in the group's Discord channel dedicated to the workgroup.
3. A supermajority (66%) of votes in favor must be observed in order for the vote to pass.
   - Voting can be expedited if a unanimous decision presents itself.
   - If there is no clear majority, the vote must remain open for the full 3 days.

The removal procedure follows this exact same process, except for removal.

Members of the group that are inactive for a long time (~6 months) or do not frequent discussions should be removed by the same removal steps.

### General Discussions
Members of the group are encouraged to be transparent, and discussions should partake in a relatively public channel.
These channels can be restricted to contributors but shouldn't be hidden away in internal channels unless sensitive information is being discussed (a game-breaking exploit or otherwise).

Generally, active public discussion on a dedicated topic in a dedicated place can help give insight to contributors as to what needs to be worked on and what can be made better in that topic.
Development can be coordinated between maintainers and contributors, which allows maintainers to spend more time reviewing desirable pull requests instead of starting votes on undesirable ones.

### PR Reviews
Members of a workgroup still have to follow the same PR review procedure when evaluating a pull request within their workgroup.

When a conflict arises between a maintainer workgroup and a maintainer not part of the work group on a pull request, the same pull request voting procedure can take place.
However, the votes needed to reach a decision must be a supermajority (66%) instead of a simple majority.

This is intended to allow the workgroup to still achieve their goal or vision if there is friction. However, the entire maintainer team can still weigh in and block or allow a change if they are mostly for or against the change.

Conflicts on pull requests that are internal to the workgroup are subjected to the same PR review procedures, however, these are supposed to be few and far between, with most conflicts being resolved through alternative directions or decisions.

### Design Documents
Workgroups are encouraged to make design documents for their game area.

These design documents are invaluable to contributors, as they help give them an insight into maintainer opinion and help them make changes we actually want.

Simple questions can be asked and answered in a design document, like:
1. **What about the game area is currently bad?**
   - Is it the mechanics, current systems, core design?
2. **How did we try and fix the problem(s) in the past?**
   - What problems were we trying to address in the fix?
   - What exactly did we do?
   - Did it work, or was it a partial success or complete failure?
3. **What should we try next?**
   - Why do we think it'll work this time, or what does it try and work towards?

This document can be partially *living*, or revisited at a later date to revise and re-document changes made, and how they affected the game area over time.

### Inter-workgroup Collaboration
Workgroups are encouraged to discuss with each other and make sure the various goals or features they implement align or compliment each other. Workgroups can either discuss this in the upstream Discord or save discussion for a dedicated maintainer meeting topic.