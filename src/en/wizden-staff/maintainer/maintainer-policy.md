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
- Sometimes a PR is a blocker, or critical to the game in some way where regular review procedure needs to be expidited, in a way different from p0 issues and hotfixes
- In these cases if a Maintainer is unable to complete a review themselves they should defer to a maintainer who can.
- Deferrals are different from normal reviews in that it is a whole review split between two or more maintainers.
  - In a deferral a maintainer completes their review but defers part of the review to a maintainer with more expertise than them.
  - This would be effectively asking another maintainer to review one specific file/system/concept being modified.
  - The maintainer being defered to does not need to do a full review with approval, but just needs to approve the code relevant to their expertise
- Deferrals should be asked for in a separate channel from normal reviews such that they don't get buried
- Deferrals should only be used if a PR is important, this includes: bugfixes, blockers, and otherwise nonspecified important content
- If a majority of a PR requires a deferral, you may still use deferral channels to ask another maintainer to review, but it may be better that said deferred maintainer does a full review.

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
