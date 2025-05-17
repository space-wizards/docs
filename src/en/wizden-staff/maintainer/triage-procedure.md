# Triage Procedure
This document lists the procedure for how to triage Space Station 14 repository Issues and PRs, as well as definitions for the label categories.

Triage is the process of assigning appropriate labels for an Issue or PR, making it easier for reviewers, contributors and other staff to correctly prioritize items, convey progress and find things that are suitable for their area of expertise. When when not distinguishing between Issue and PR, the term "item" is used.

## Who can Triage?

Triage permissions are assigned to trusted contributors and staff on the project; being a maintainer is *not* a requirement to be able to Triage, though someone with Triage access should have codebase knowledge to the extent that they can perform Triage correctly. Performing Triage does not require going as in-depth as a Code Review would, and should largely be possible by reading the PR description and skimming the code. 

For a non-maintainer to be given Triage permissions, a thread should be opened up in the main private staff channel where staff are given 24 hours to provide input. If there is dissent by the end of the 24 hour period, staff should discuss and attempt to reach a resolution shortly thereafter. If there is no dissent, the candidate is to be given the "Triager" role on Discord and Triage permissions on Github.

Maintainers have Triage permissions by default. Game Admins can be given Triage permissions without a thread at a Maintainer's or Project Manager's discretion. 

Abuse of the Triage permissions (intentionally assigning incorrect labels, closing PRs/issues against policy or otherwise abusing the permissions) may result in the permissions being removed and other actions taken, at the discretion of a Project Manager.

## Triage Procedures

When performing a triage, the goal is to add all relevant labels to the item. Some labels have concrete definitions to follow (such as the `Size` or `Branch` label categories), while others are subjective and need to be evaluated based on the item's contents. Triagers may close Issues at their own discretion should they no longer be relevant to keep open. *PRs may* ***not*** *be closed via triage*, as that is an action reserved for Maintainers. 

When closing an issue, ideally either link to the PR that resolved it, post an in-game screenshot showing the issue is no longer relevant or mention why the issue should not be addressed and is an intended mechanic (in this last case, mark the Issue with `Issue: Intended Feature`).

### New Issue / PR Triage

Github automatically assigns the `S: Untriaged` label to any Issue or PR that is submitted. Triage should be performed on any such new item. Read through the item and assign appropriate labels based on its content.

For a triage to be completed, the item must have *at least one* label from the following label categories. This is signified by these categories having a 1-letter category name:
  - Area / A
  - Difficulty / D    (_Only mandatory for Issues. PRs may have it at the triager's discretion_)
  - Priority / P
  - Status / S
  - Type / T

The following categories are assigned automatically by Github:
  - Size
  - Changes

Once a triage is completed, remove the `S: Untriaged` label and attach `S: Needs Review` for PRs, or `S: Requires Content PR` for Issues (alternative labels may be more appropriate, such as when closing an issue).

### Priority Labels

Priority labels are used to indicate how important an item is to the project. These range from `P0` (critical) to `P3` (standard). Every triaged item should have one.

- **P0 - Critical:** Reserved **only** for bugfixes affecting one or more live servers that render the game unplayable (e.g., round cannot progress, major server crashes, widespread inability to perform core gameplay actions). Use with extreme caution.
- **P1 - High:** Reserved for **non-critical but high-impact** bugfixes and **admin tooling**. These should be prioritized over all other PRs but are **not** emergencies. The goal is to keep the number of open P1 PRs as low as possible. **Do not assign P1 to new content.**
- **P2 - Raised:** For items that are beneficial, useful, or deserve Maintainer attention, but don't qualify for P0/P1.
- **P3 - Standard:** The default for most issues and PRs that are not urgent.

These limits can be exceeded by reasonable Staff consensus.
Within the above limits, any single Maintainer can adjust the priority of an unassigned item. 
If an item is assigned to a Maintainer, then the item should not be reprioritised without consulting them first.
In case of unresolvable dispute about the priority of an item, Lead Maintainers have final say.

If the reason for a change is not completely obvious, a comment should be left explaining it, as a change with no explanation is more likely to itself be changed again later by another Maintainer acting in good faith.

### Old Issue / PR Re-Triage

If an item have not been interacted with for a long time (>1 month), it *may* be relevant to re-triage. There are no labels to indicate an old item requires re-triage.

The goal of a re-triage is to determine if any of the labels need to change; this could be because the item is no longer necessary, has already been completed or is no longer frozen, as examples. 

## SS14 Github Label Categories

Each label has a description that explains what is to be used for in its category. The list below describes what the label categories represent.

| Category | Shorthand | Description |
|---|---|---|
| Area | A | Describes which area of the project an item is related to. An item may be related to multiple areas, however it should always have at least one. An example would be a guidebook entry on an undocumented Science feature, which would fit within both the Guidebook and Science area. If an item doesn't seem to fit in any area, report it to a maintainer to see if a new label needs to be made. |
| Branch | Branch | If an item is intended for a non-master branch. Most commonly used for hotfixes. |
| Changes | Changes | Indicates an item should be handled by someone with knowledge in a certain area. Automatically generated by Github. |
| Difficulty | D# | 0-3, with 0 the hardest. An estimate of how complex the item would be to review or create a PR for. <br>`DB: Beginner Friendly` should include clear steps towards a solution for the issue. |
| Fun | Fun | For the silly little labels. Should be used sparingly. |
| Intent | Intent | If the item is intended to be processed using an alternate review/merge policy. Used for hotfixes or test merges.
| Issue | Issue | Reserved for Issues, where a complex bug should be replicated to ensure it's accurately reported. Not necessary for all bug reports. |
| Priority | P# | 0–3, with 0 the highest. Indicates how important the item is to the project. See [Priority Labels](#priority-labels) for full usage guidelines. |
| Size | size | How large the PR is codewise. Automatically generated by Github. |
| Status | S | The current status for the item. There should be at least one label in this category, though at times multiple may be applicable. |
| Type | T | What the item is attempting/suggesting to do. Multiple types may be applicable. |

## Non-Triager Labels

Some labels should not be used/removed by Triagers, as they are either automatically applied or are to be used at Maintainer/PM discretion only.

| Label | Reason |
|---|---|
| Changes category | Applied automatically.* |
| Fun category | Only at Maintainer/PM discretion. |
| Size category | Applied automatically.* |
| S: Approved | Only Maintainers can approve items. Applied automatically. |
| S: Awaiting Changes | Applied automatically. |
| S: Conceptual Approval | Can only be applied by a Maintainer, following Review Procedure. |
| S: Undergoing Maintainer Discussion | Maintainer Discussions are at Maintainers' discretion. |
| S: Art Approval | Can only be applied by an Art Lead following their approval. If the Art Lead has forgotten to apply it, Triagers may apply this label. |

\* May still be applied in certain cases, if the automatic labelling is not working/not implemented.
