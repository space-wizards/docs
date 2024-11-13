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

When closing an issue, ideally either link to the PR that resolved it, post an in-game screenshot showing the issue is no longer relevant or mention why the issue should not be addressed and is an intended mechanic (in this last case, mark the Issue with `Bug: Intended Feature`).

### New Issue / PR Triage

Github automatically assigns the `S: Untriaged` label to any Issue or PR that is submitted. Triage should be performed on any such new item. Read through the item and assign appropriate labels based on its content.

For a triage to be completed, the item must have *at least one* label from the following label categories:
  - Area
  - Category
  - Difficulty
  - Priority
  - Size
  - Status

While not mandatory, it's likely that the following label categories will be relevant for most items:
  - Changes

Once a triage is completed, remove the `S: Untriaged` label and attach 'S: Needs Review' for PRs, or 'S: Requires Content PR' for Issues (alternative labels may be more appropriate, such as when closing an issue).

### Old Issue / PR Re-Triage

If an item have not been interacted with for a long time (>1 month), it *may* be relevant to re-triage. There are no labels to indicate an old item requires re-triage.

The goal of a re-triage is to determine if any of the labels need to change; this could be because the item is no longer necessary, has already been completed or is no longer frozen, as examples. 

## SS14 Github Label Categories

Each label has a description that explains what is to be used for in its category. The list below describes what the label categories represent.

| Category | Shorthand | Description |
|---|---|---|
| Area | A | Describes which area of the project an item is related to. An item may be related to multiple areas, however it should always have at least one. An example would be a guidebook entry on an undocumented Science feature, which would fit within both the Guidebook and Science area. If an item doesn't seem to fit in any area, report it to a maintainer to see if a new label needs to be made. |
| Branch | Branch | If an item is intended for a non-master branch. Most commonly used for hotfixes. |
| Bug | B | Reserved for Issues, where a complex bug should be replicated to ensure it's accurately reported. Not necessary for all bug reports. |
| Category | C | What the item is attempting/suggesting to do. Multiple categories may be applicable. |
| Changes | Changes | Indicates an item should be handled by someone with knowledge in a certain area. |
| Difficulty | D | An estimate of how complex the item would be to review or create a PR for. Fairly subjective and should be based on the code.
| Fun | F | For the silly little labels. Should be used sparingly. |
| Intent | I | If the item is intended to be processed using an alternate review/merge policy. Used for hotfixes or test merges.
| Priority | P | How important the item is to the project. Contributors may tackle any item as they see fit, but this category should help guide what is important. |
| Size | size | How large the PR is codewise. Will ideally be automatically generated by Github. |
| Status | S | The current status for the item. There should be at least one label in this category, though at times multiple may be applicable. |

## Non-Triager Labels

Some labels should not be used/removed by Triagers, as they are either automatically applied or are to be used at Maintainer/PM discretion only.

| Label | Reason |
|---|---|
| Changes category | Applied automatically.* |
| Fun category | Only at Maintainer/PM discretion. |
| Size category | Applied automatically.* |
| S: Approved | Only Maintainers can approve items. |
| S: Awaiting Changes | Applied automatically. |
| S: Conceptual Approval | Can only be applied by a Maintainer, following Review Procedure. |
| S: Undergoing Maintainer Discussion | Maintainer Discussions are at Maintainers' discretion. |

\* May still be applied in certain cases, if the automatic labelling is not working/not implemented.
