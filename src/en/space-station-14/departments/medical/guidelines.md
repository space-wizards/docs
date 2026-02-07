# PR Guidelines

## Making a Medical PR

Medical related PRs include anything covered by the Medical Workgroup document. PRs which touch BodySystem and related components, the Medical Department's round flow, and Reagents are medical related PRs and must adhere to the PR guidelines listed here. 

Medical related PRs should, in their description or title, state whether this change is meant to be for the current upstream medical system or for debodying/disco-med (See [Medical Workgroup Document](medical-workgroup.md)). A PR without clear intention may be subject to closure if it does not follow the guidelines for either current upstream medical, or disco-med. 

For any additional questions please consult the medical workgroup through the SS14 discord server.

### PRs for Current Medical
A PR for current medical should typically be for fixing up or rebalancing current behavior. These PRs must justify their existence, the current medical system is extremely flawed so a portion of the PR description should be explaining why this should be merged instead of waiting for better medical implementation. Microbalance PRs will be closed at workgroup discretion. Common justifications may include: bugfixes, exploits, highly unbalanced/meta behavior, or small additions which do not greatly alter key systems. 

In addition these PRs cannot and should never reverse debodying or hardcode body system behavior into another system. If a PR is unable to meet these guidelines and cannot be changed to meet these guidelines, it must be refactored to adhere to disco-med guidelines or be closed. 

### PRs for Disco-Med/Debodying
A PR designed for debodying/disco-med must adhere to the [Medical Design Document](../medical.md). Disco-Med and Debodying PRs are expected to be of higher code quaity and will be more heavily scrutinized. These PRs should clearly explain how this advances the medical system or advances the destruction/reconstruction of BodySystem in their description. Disco-Med and debodying PRs should not be making code compromises. If a PR must make code compromises, then its description must explain both what those compromises are and what is needed to remove such compromises, as well as labeling these compromises in code with TODOs.

PRs which have to be split into multiple parts may require a design document, this is particularly true if any of the following criteria are met:
- PR is not covered by a previous design document
- PR was not pre-approved by a medical workgroup member
- PR strays from the Medical Design Document or Medical Workgroup Document
- PR is of such large scope that it may need to be divided amongst multiple contributors
- PR requires multiple other systems to be refactored first

For more questions on Debodying and Disco-Med please see: [Medical Workgroup Document](medical-workgroup.md)

### PRs for Offmed
PRs for offmed shouldn't be merged into master as offmed is a testing branch. These should instead be merged directly into the offmed branch themselves. Since offmed is a feature testing branch and completely under the control of the medical workgroup, any PR intended for offmed may be closed for any reason.
