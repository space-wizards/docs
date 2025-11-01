# Triage Procedure
This document lists the procedure for triaging Space Station 14 repository Issues and PRs, as well as definitions for the label categories.

Triage is the process of assigning appropriate labels to an Issue or PR, making it easier for reviewers, contributors, and other staff to correctly prioritize items, convey progress, and identify issues suitable for their area of expertise. When not distinguishing between Issue and PR, the term "item" is used.

## Who can triage?

Triage permissions are assigned to trusted contributors and staff on the project. Being a maintainer is *not* a requirement to be able to triage, although someone with Triage access should have codebase knowledge to the extent that they can perform Triage correctly. Performing Triage does not require going as in-depth as a Code Review would, and should largely be possible by reading the PR description and skimming the code. 

For a non-maintainer to be given Triage permissions, a thread should be opened up in the main private staff channel where staff are given 24 hours to provide input. If there is dissent by the end of the 24-hour period, staff should discuss and attempt to resolve it shortly thereafter. If there is no dissent, the candidate is to be given the "Triager" role on Discord and Triage permissions on GitHub.

Maintainers have Triage permissions by default. Game Admins can be granted Triage permissions at the discretion of a Maintainer or Project Manager, without requiring a thread. 

Abuse of the Triage permissions (intentionally assigning incorrect labels, closing PRs/issues against policy, or otherwise misusing the permissions) may result in the removal of the permissions and other actions taken, at the discretion of a Project Manager.

## Triage Procedures

### New Issue / PR Triage

GitHub automatically assigns the `S: Untriaged` label to any Issue or PR that is submitted. Triage should be performed on any such new item. Read through the item and assign appropriate labels based on its content.

When performing a triage, the goal is to add all relevant labels to the item. Triagers add tags that are subjective and need to be evaluated based on the issue or PR's contents.

For a triage to be completed, the item must have *at least one* label from all the following label categories:

| Name       | Tag Prefix | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Area       | A:         | Describes which area of the project an item is related to. An item may be related to multiple areas; it must always have at least one. An example would be a guidebook entry on an undocumented Science feature, which would fit within both the Guidebook and Science area. If an item doesn't seem to fit in any area, report it to a maintainer to see if a new label needs to be made, and otherwise assign it to `A: General Interactions`. |
| Difficulty | D:         | How hard the Issue or PR is to resolve. This is not mandatory for PRs. `DB: Beginner Friendly` should be tagged on any sufficiently simple Issue that has clear instructions on how to perform the fix.                                                                                                                                                                                                                                          |
| Priority   | P:         | How urgent the Issue or PR is to be resolved. These labels are covered in a section below.                                                                                                                                                                                                                                                                                                                                                       |
| Status     | S:         | The status of the PR. All Issues and PRs start with the tag `S: Untriaged`, and `S: Needs Review` is added once the Issue or PR is triaged. `S: Requires Content PR`, `S: Needs Content PR Merged`, and their engine equivalents, can be optionally added to Issues when a PR is required to close the Issue.                                                                                                                                    |
| Type       | T:         | Contextful tags about the sort of work covered by the Issue or PR, such as `T: Bugfix` or `T: New Feature`.                                                                                                                                                                                                                                                                                                                                      |

Once a triage is completed, remove the `S: Untriaged` label and attach `S: Needs Review` for PRs. If the PR was opened by a Maintainer, it should also receive the `S: Approved` label, as they count as the first approver.

During triaging, a Triager may optionally assign Issues to any of the available Issue Types GitHub provides:

| Type    | Definition                                                                                                |
| ------- | --------------------------------------------------------------------------------------------------------- |
| Bug     | Something unexpected in the game, like a bug, a problematic feature, or an exploit.                       |
| Feature | A feature request, such as a request to alter or add new content.                                         |
| Task    | A piece of work, such as a list of to-dos to complete a design document or a reminder to perform a chore. |


### Priority Labelling

Priority labels are used to indicate the importance of an item to the project. These range from `P0` (critical) to `P3` (standard). Every triaged item should have one.

| Name     | Prefix | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Critical | P0     | Reserved **only** for Issues affecting one or more live servers that render the game unplayable (e.g., round cannot progress, frequent server crashes, widespread inability to perform core gameplay actions, high-impact exploits that render core gameplay mechanics moot). PRs may only be tagged P0 if they fix a P0 Issue. P0 PRs **should** target the Stable branch, except when a good reason is given otherwise.                                                                             |
| High     | P1     | Reserved for **non-critical but high-impact** bugs, exploits, bugfixes, and admin tooling. These should be prioritized over all other PRs but are **not** emergencies. The goal is to minimize the number of open P1 PRs. **Do not assign P1 to new content.**                                                                                                                                                                                                                         |
| Raised   | P2     | A non-critical, non-high-impact Issue or PR that is notable for some reason, and therefore worthy of Maintainer attention ahead of Standard Issues and PRs. Examples include content PRs that implement part or all of a design document, large-scale refactors deemed beneficial to the project, Issues used to organize work on an ongoing project, bugs and exploits that are common and have a moderate impact on the game, or high-impact bugs that are only reproducable in rare circumstances. |
| Standard | P3     | The default for any non-urgent Issue or PR.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

Any Issue or PR can have its Priority placed in a category outside the above descriptions by reasonable Staff consensus. In addition, the Project Lead's word is final on if an Issue is P0 or not.

Within the above limits, any single Maintainer can adjust the priority of an unassigned item. 
If an item is assigned to a Maintainer, then the item should not be reprioritised without consulting them first.
In case of an unresolvable dispute about the priority of an item, Lead Maintainers have final say.

If the reason for a change is not completely obvious, a comment should be left explaining it, as a change with no explanation is more likely to itself be changed again later by another Maintainer acting in good faith.

### Re-Triaging Old Issues and PRs

If an item has not been interacted with for a long time (more than one month), it *may* be relevant to re-triage. There are no labels to indicate an old item requires re-triage.

The goal of a re-triage is to determine if any of the labels need to change; this could be because the item is no longer necessary, has already been completed or is no longer frozen, as examples. 

Triagers **may** tag an Issue or PR as `S: Stale` if, during a re-triage, it is determined that an Issue has likely become irrelevant or out-of-date, a draft PR has been open for a long while without any progress being made, or a PR has been inactive for a long time after being supersceded or having had changes requested.

Non-Maintainer Triagers **must not** tag a PR as `S: Derelict`. This tag is to be added by Maintainers only, usually when closing derelict PRs.

### Closing Issues

Any Triager **may** close Issues if they are no longer relevant.

When closing an issue, triage best practice involves adding a comment that contains one or more of the following:
* a link to the PR that resolved it,
* an in-game screenshot or video showing the issue is no longer relevant,
* a note why the issue should not be addressed due to being an intended mechanic (in this last case, mark the Issue with `Issue: Intended Feature`).

### Never Closing PRs

Non-Maintainer Triagers **must never** close Pull Requests. This is **always** a Maintainer's responsibility.

## Other SS14 Github Label Categories

Some other types of labels exist that do not usually fall within the triage process. These include:

| Category | Shorthand | Description                                                                                                                                                             |
| -------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Branch   | Branch    | If an item is intended for a non-master branch. Most commonly used for hotfixes.                                                                                        |
| Changes  | Changes   | Indicates an item should be handled by someone with knowledge in a certain area. Automatically generated by GitHub.                                                     |
| Fun      | Fun       | Labels used to decorate funny Issues and PRs. Should be used sparingly.                                                                                                 |
| Intent   | Intent    | Flags if an Issue or PR is intended to be processed using an alternate review/merge policy. Used for hotfixes or test merges.                                           |
| Issue    | Issue     | Reserved for Issues only, and used to denote the state of a bug report, such as requiring replication or being potentially fixed. Not necessary for simple bug reports. |
| Size     | size      | How large the PR is codewise. Automatically generated by GitHub.                                                                                                        |

## Non-Triager Labels

Some labels **should not** be used/removed by non-Maintainer Triagers, as they are either automatically applied or are to be used at Maintainer/PM discretion only.

| Label                               | Reason                                                                                                                                              |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| All Changes tags                    | Applied automatically.*                                                                                                                             |
| All Fun tags                        | Only at Maintainer/PM discretion.                                                                                                                   |
| All Size tags                       | Applied automatically.*                                                                                                                             |
| S: Approved                         | Only Maintainers can approve items. Applied automatically.                                                                                          |
| S: Awaiting Changes                 | Applied automatically.                                                                                                                              |
| S: Conceptual Approval              | Can only be applied by a Maintainer, following Review Procedure.                                                                                    |
| S: Undergoing Maintainer Discussion | Maintainer Discussions are at Maintainers' discretion.                                                                                              |
| S: Art Approval                     | Can only be applied by an Art Lead following their approval. If the Art Lead has forgotten to apply it, Triagers may apply this label.              |
| S: Concern                          | Only applied by a Maintainer with concern about a particular PR.                                                                                    |
| S: DO NOT MERGE                     | Only applied by a Maintainer to PRs when that must be blocked from merging due to integration problems, extreme controversy, or other good reasons. |

\* May still be applied in certain cases, if the automatic labelling is not working/not implemented.
