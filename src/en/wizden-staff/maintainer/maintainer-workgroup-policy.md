# Maintainer Workgroups
This document outlines Maintainer Workgroups, a subteam within the Maintainer staff group.

Workgroups consist of active Maintainers that hold special knowledge on the workgroup's area.
These members write and actively maintain design documents targeting this area, which outline problems, potential solutions, and direct future development.

## Goals
Maintainer workgroups plan to achieve the following:
1. **Define a real body to represent a game area and lead its design and development**
   - With this, contributors can directly interface with people that know the problems of the game area, what it should be in the future, and what they should work on.
   - The group can carve out their idea of what a department should be, writing directional design documents that help contributors see the future of a game area.
2. **Expedite pull request conceptual design review, and regulate pull requests that are not fit for a game area**
   - A small group focused on a game area can properly evaluate and approve or deny pull requests that don't work towards the group's defined future vision.

## Policy

### Supervision
Maintainer Workgroups are overseen by the Lead Maintainers.

They are to make sure that the aforementioned policy is followed.

### Formation
Workgroups are formed by a Lead Maintainer, Project Manager, or Wizard, by request from a Maintainer.
These roles can also deny the workgroup's formation if it is deemed an unnecessary atomization or focus.

As few as **two** Maintainers can request to form a workgroup.

Additionally, workgroup members should fulfill the following criteria:
- The Maintainer has authored a large volume of pull requests to the game area that have been merged.
  - Alternatively, the Maintainer has demonstrated that they possess knowledge or experience on the SS14 game area that is higher than a regular maintainer.
- They are an active Maintainer and participate frequently in discussions involving the game area on the Forums, Discord, or GitHub.

A request to form a workgroup must be made in the Maintainers category on Discourse for documentation.
The following information should be provided when making a request:
- The game area that the group will oversee.
- Members of the group, and why you think the members would be a good fit for the group, whether it be their knowledge, technical expertise, or other reasons.
- Any other information you'd like to present as justification.

#### Game Area Scope
The game area that a Maintainer Workgroup controls should be something tangible and definable.
Workgroups targeting a game area that is large in scope (ex. spanning multiple antagonists or departments) should be avoided.
Additionally, unnecessary atomizations or tiny game areas shouldn't be a focus.

When establishing a game area for formation, think back to [SMART criteria](https://en.wikipedia.org/wiki/SMART_criteria).
It's also a good idea to apply this to your future design documents and game area goals as well.

Some examples of good and bad game areas are below:
- **Good:**
  - Singular departments like Science or Medical.
    - Reasonable atomizations of departments, ex. Engineering and Atmospherics are also acceptable.
  - Singular antagonists like Wizard, Traitor, or Nuclear Operatives.
  - Smaller game areas like Chef, Botany, or Janitor.
- **Bad:**
  - An "antagonist" area.
  - A "roundflow" area.
  - A "radio jammer" area.

### Joining
Maintainers wanting to join a workgroup should fulfill the same member criteria defined in the Formation section.

```admonish warning
Maintainers should be cautious when joining excessive amounts of workgroups.
Workgroups are intended to lead a game area and direct development on it.
A maintainer that is largely absent or stretched too thin due to being involved in too many workgroups will slow down the workgroup and its development, and it will likely lead to maintainer burnout from attempting to manage multiple workgroups at the same time.

It is recommended to be active in a select few workgroups, ones that you find personal interest in.
```

The joining procedure is semiformal:
1. A Maintainer contacts a member of the group and asks to join. A member of the group can also nominate a person to join the group.
2. A vote must be created, for three days, on Discourse, open to all Maintainers.
3. A supermajority (66%) of votes in favor must be observed in order for the vote to pass.
   - Voting can be expedited if a unanimous decision presents itself.
   - If there is no clear majority, the vote must remain open for the full 3 days.

### Removal
Removal is entirely handled by Lead Maintainers, Project Managers, or Wizards.
Members of the group that are inactive for a long time (~6 months) or do not frequent discussions should be removed.

### General Discussions
Members of the group are encouraged to be transparent, and discussions should partake in a relatively public channel.
These channels can be restricted to contributors but shouldn't be hidden away in internal channels unless sensitive information is being discussed (a game-breaking exploit or otherwise).

Generally, active public discussion can help give insight to contributors as to what needs to be worked on and what can be made better in that topic.
Development can be coordinated between maintainers and contributors, which allows maintainers to spend more time reviewing desirable pull requests instead of starting votes on undesirable ones.

### PR Reviews
```admonish warning
A workgroup **has no authority** over a game area until an initial design document is merged.
```

Any pull request to a game area controlled by a maintainer workgroup must receive one conceptual approval from a Maintainer belonging to that workgroup.
Pull requests authored by a workgroup member that target a workgroup cannot be self-approved for design.

This is to encourage directing pull requests targeting certain game areas to groups that have more experience with that game area.

If a pull request belonging to a maintainer workgroup is closed citing game design reasons, these reasons **must** be citable from any merged design document.
If a reason cannot be cited from any merged design document, the design document **must** be amended to include these reasons.

When a conflict arises between a maintainer workgroup and a maintainer not part of the work group on a pull request, the same pull request voting procedure can take place.
However, the votes needed to reach a decision must be a supermajority (66%) instead of a simple majority.

This is intended to allow the workgroup to still achieve their goal or vision if there is friction. However, the entire maintainer team can still weigh in and block or allow a change if they are mostly for or against the change.

Conflicts on pull requests that are internal to the workgroup are subjected to the same PR review procedures; however, these are supposed to be few and far between, with most conflicts being resolved through alternative directions or decisions.

### Design Documents
Workgroups are encouraged to make design documents for their game area.
View the [Game Area Design Document Template](en/general-development/game-area-design-doc.md) and the [Department Design Document Template](en/templates-docs/department-design-template.md) for a good document basis.

When a workgroup creates a design document, it is said to be owned by that workgroup.

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

#### Design Document Amendments
Design documents owned by a workgroup should be revisited from time to time to update the document with new information on current game mechanics, situations, problems, direction, and more.
They must also be amended if a pull request was closed without citing a reason from a design document.

Any change to a design document owned by a workgroup can be merged with one approval from a member of that workgroup.
Workgroup members cannot self-approve their own pull requests changing their own design document.

### Inter-workgroup Collaboration
Workgroups are encouraged to discuss with each other and make sure the various goals or features they implement align or compliment each other. Workgroups can either discuss this in the upstream Discord or save discussion for a dedicated maintainer meeting topic.
