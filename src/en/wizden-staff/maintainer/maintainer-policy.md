# Maintainer Policy
This is the policy that all maintainers are expected to follow when it comes to behavior and responsibilities. 

This policy applies in addition to the [General Staff](../staff-policy.md) and [Conflict Resolution](../staff-conflict-resolution.md) Polices.

**Breaking any of these rules will result in disiplinary action being taken**
## Reviews and Feedback
- All maintainers must follow the [PR Review](../maintainer/review-procedure.md) and [Hotfix Procedures](../maintainer/hotfix-procedure.md) when they apply.
- Maintainers should try to the best of their ability, to keep PR authors informed on the status of their PRs.
- Maintainers should keep public criticism of code *constructive* and avoid making comments in regards to the authors of the code. **Harsh but fair** citicism of code is *acceptable*, but criticism of its author is not.
- Maintainers should try to perform code reviews *whenever possible*, getting content into the game is everyone's responsibility.
- If there is a conflict around game design between something in the docs and someone's idea, what is detailed in the documentation takes precedent. If a change to specific documentation is needed, it should be brought up with the respective work group for discussion and changes should be made to the documentation if needed.

## Deferral Policy
- Maintainers are not expected to know everything about every part of the game, but when reviews are made they are expected to at least have oversight from someone who does know.
- In cases where a PR has higher need to be merged than others but an active maintainer cannot fully complete a PR review on their own they may defer a part of their review to another maintainer.
  - Case can include but are not limited to Blocking PRs, Bugfixes, and Important Community Content PRs.
- Deferrals are different from normal reviews in that it is a full review split between two or more maintainers.
  - When a maintainer defers their review, they complete as much of the review as possible and then hand over the sections of the PR they need help with to a more knowledgeable maintainer.
  - The maintainer who is deferring the review should specifiy what part of the code they are deferring and request a maintainer review it for them they should be specific about what or who they need if possible.
  - The maintainer should also specify why they are deferring it rather than requesting a review
    - Since deferring is meant to speed up review procedure this is typically for PRs that are important to merge and should clarify that importance. 
  - Deferrals should be used to hasten the review process without sacrificing code quality, so a maintainer deferring part of their review should be able to complete most of the review themselves.
- Deferrals should be asked for in a separate channel from normal reviews such that they don't get buried
  - This channel should also be used for important PRs that cannot be deferred due to being mostly or fully requiring the expertise of another maintainer
- When a maintainer has a PR deferred to them, they should follow normal review procedure with some changes:
  - A maintainer doing a deferred review doesn't have to sign off on the entire PR, just the section sent to them
    - A maintainer can request changes and block the PR from being merged as normal
  - When a maintainer approves of the section assigned to them, they should express so in a comment on github and notify the maintainer who deferred the review to them.
  - A maintainer is not stopped in any way from doing a full review with a full approval themselves.
- Once all deferred parts of the review are approved can the original maintainer finish their review and approve the PR
  - Note that this only counts as approval of the original maintainers, any maintainers who reviewed a deferred part of the PR can still review the PR later and approve it themselves.

## In-game Permissions
- Maintainers can request to be given in game permissions by the admin team.
- Maintainers may only use the permissions they are given for the purposes of debugging issues, and playtesting new features. 
- Maintainers must not **under any circumstances** access any data related to a player's account. The only exception to this is logs from a round for the purposes stated above.
- Maintainers may only host playtests with a Propermin from the admin team who must handle ahelps and log the playtest as an event. 
- Maintainers **must** deadmin while playing.
- **Any violation of the above rules will lead to in-game permissions being indefinitely revoked.**

## Changing Maintainer Policy

- Any Maintainer can propose a change to the Maintainer Policy.
- The proposal must be made in the /Internal/Maintainers/ category on Discourse.
- The proposal must have a vote open for at least 72 hours.
    - This may be extended if there is a significant amount of discussion.
- The proposal must have a supermajority (66%) vote in favor to pass.
- A PR to the Docs repository can be made at any time, even if the vote is still ongoing.
    - If there is an ongoing vote, the PR must not be merged until the vote has concluded.

### Exceptions
- Lead Maintainers can change the policy without a vote if it is an emergency or the change is minor.
    - An emergency is defined as a situation where the policy is causing immediate harm to the project.
    - A minor change is defined as a change that does not significantly impact the responsibilities of Maintainers.
- A vote may be skipped if the change is minor and the Lead Maintainers agree, but the Maintainers must be informed of the change.
- A vote is always required for changing the policy that defines the rules on how Maintainer Policy is changed.
