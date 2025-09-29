# PR Guildlines

## Important

All PRs must adhere to the [Medical Design Document](en/space-station-14/departments/medical.md) and/or the [Medical Workgroup Document](en/space-station-14/medical-workgroup.md) for questions about the differences between these documents please consult the medical workgroup through the SS14 discord server.

## How to label Medical PRs

Medical related PRs should, in their description or title, state whether this change is meant to be for the current upstream medical system or for debodying/psycho-med. A PR without these labels is not subject to closure unless the author is unable or unwilling to have their PR adhere to the design goals of either system. 

### PRs for Current Medical
A PR for current medical should typically be for fixing up or rebalancing a current behavior and justify why it should be fixed up or rebalanced. Because the current medical system is flawed and simplistic, justification is a very important part of the PR description, why do we need to make changes now instead of just brushing it off until medical is refactored as a whole. Common justifications would be bugs, exploitative behavior, unbalanced behavior, or small additions which do not greatly alter key systems. 

In addition these PRs cannot and should never reverse debodying or hardcode body system behavior into another system. If a PR is unable to be changed to meet these criteria it must either be refactored to be made for psycho-med or be closed. 

### PRs for Psycho-Med/Debodying
A PR for debodying/psycho-med must be cleary stated as such and must adhere to the [Medical Design Document](en/space-station-14/departments/medical.md). These are subject to much heavier scrutiny since psycho-med and debodying related changes are expected to be final. These PRs should clearly explain how this advances the medical system or advances the destruction/reconstruction of body system within the PR itself without compromises. If compromises have to be made, which is common and expected, it should be explained what the compromises are, what is needed to remove them, with a plan of removal, and why the compromises can't be addressed first. 

PRs which have to be split into multiple parts may require a design document, this is particularly true if any of the following criteria are met:
- PR is not covered by a previous design document
- PR was not pre-approved by a medical workgroup member
- PR strays from the Medical Design Document or Medical Workgroup Document
- PR is of such large scope that it may need to be divided amongst multiple contributors

For more questions on Debodying and Psycho-Med please see: [Medical Workgroup Document](en/space-station-14/medical-workgroup.md)

### PRs for Offmed
PRs for offmed shouldn't be merged into master as offmed is a testing branch. These should instead be merged directly into the offmed branch themselves. Since offmed is a feature testing branch and completely under the control of the medical workgroup, any PR intended for offmed may be closed for any reason.
