# Content PR Review Procedure

## Abstract
This document outlines the Maintainer procedure for reviewing and merging PRs to the [Space Station 14 repository](https://github.com/space-wizards/space-station-14) `master` branch (otherwise known as the Content repository).

Pull requests targeting the `staging` or `stable` branch are subject to the [Hotfix Procedure](hotfix-procedure.md).

Any portion of this procedure may be waived and/or modified with written permission (_via Discord or GitHub_) from a Lead Maintainer, Project Manager or Wizard.

```admonish note
Note that these procedures are ultimately flexible; however, Maintainers who deviate from this policy are expected to provide concrete and valid reasoning when doing so.
Getting one or more other maintainers to agree with your deviation is advisable.

Note that all pull requests scheduled for release to `stable` are reviewed before or during _Stable Review_ at maintainer meetings.
```

## Reviewing Content Pull Requests

### Reviewing the PR
All pull requests must adhere to the [code conventions](../../general-development/codebase-info/conventions.md).

All parts of the Pull Request Template must be filled out by the author.

If the author has obviously not read the conventions or PR guidelines, or the pull request template has not been filled out to a satisfactory level, close the PR.

All PRs must be triaged according to the [triage procedure](triage-procedure.md) guidelines.
You should triage the pull request when reviewing it for the first time.

When leaving comments or requesting changes:
- Use **constructive** language and avoid being overly negative.
- Try not to be _overly_ vulgar or swear in a derogatory way.
- Avoid comments that personally criticize the author. 
  - It's okay to critique code and decisions, but you shouldn't insult their character.
- For people who may not be familiar with a system, try to be more thorough in your explanations.
  - Explain your review to teach people unfamiliar with the system.
- When possible, direct people to either the [developer wiki](https://docs.spacestation14.com/index.html), `#howdoicode` discord channel, or alternate source for information.
- Make an effort to be available after reviewing a PR. 
  - You don't need to be constantly online, but if the author has questions, they should be able to get a response in a reasonable amount of time.
- Be formal when closing PRs. 
  - Discourage others from engaging in rude behavior and try not to upset the PR author. People can often be emotional after their PR is closed.
- For relatively minor changes, opt to simply [complete them yourself](https://cli.github.com/manual/gh_pr_checkout) and push to the PR.
- When requesting changes to a PR, keep them within the scope of the PR.
  - For example, while requesting small numerical adjustments on a `No C#` PR is fine, it would exceed the scope of the PR to request a new system to be added. In cases like these, it is best to close the PR and explain the changes that would be required.

### Approving PRs
Pull requests must pass code review in order to be merged.
The number of reviews required are determined by the type of pull request being reviewed.

```admonish note
Pull requests may be reviewed, approved, and merged by a single maintainer in specific circumstances.
When a maintainer does so, the maintainer is expected to provide concrete and valid reasoning for doing so.
For example, a maintainer that is known for reviewing and making prediction PRs can probably process a prediction PR by themselves.
```

A pull request created by a Maintainer has one approval by default.
However, Maintainers cannot self-approve pull requests that would only require one approval to merge.
For example, a maintainer cannot create a PR for a small bugfix and then instantly merge it after - it must be reviewed by another maintainer.

#### Examples
```admonish info
If the pull request does not line up with any category listed here, defer to two approvals.
```

- **One Approval:**
  - Light code cleanup
    - Cleaning up errors in a few files, fixing formatting, or documenting a large group of files.
  - Bugfixes small in scope
    - Small bugfixes that don't touch major hotpaths, or critical code paths (like Atmospherics, Reagents, Physics, Movement, HTN, etc.).
  - Player-facing changes small in impact
    - Guidebook changes or renames, description changes or renames.
    - Locale changes.
    - Item additions to inventory fills.
    - Container size tweaks.
    - Loadout item tweaks, additions, or removals.
- **Two Approvals:**
  - Heavy code cleanup
    - Large cleanup of warnings across the codebase or the refactoring of an entire system.
    - Obsoletion of public methods.
    - Prediction of systems.
  - Critical bugfixes
    - Bugfixes that touch hotpaths or critical code paths should be brought under more scrutiny and thus involve another maintainer.
  - Performance improvements
    - These should usually come with a custom BenchmarkDotNet benchmark to prove that the PR has a meaningful effect on performance.
  - Player-facing changes large in impact.
    - Major additions like new antagonists, medical systems, atmospherics processing states, etc.
    - Wide balancing revamps (ex. the rebalancing of an entire antagonist's store).

#### Exceptions
There are some exceptions to the one-approval or two-approval system. They are listed below.
1. **Mapping changes must be approved by a Mapping Lead, and only require one approval if the PR contains only mapping changes.**
   1. This still applies even if the change is technical in origin (like fixing a datafield spamming/inflating the size of YAML).
   2. Mapping Leads can self-approve their own mapping changes.
2. **Sprite changes must be approved by an Art Lead, and only require one approval if the PR contains only sprite changes.**
   1. Art Lead approval is not required in the case of a sprite being minorly fixed up (for example, translation/rotation, removing stray pixels, etc.).
   2. Art Leads cannot self-approve sprite changes.
3. **Changes targeting a [Maintainer Workgroups](maintainer-workgroup-policy.md)'s game area must be approved by a member from the workgroup.**
   1. Workgroup members can self-approve changes targeting their own workgroup.
4. **Rule or server configuration changes require the approval, either written or on GitHub, of the Head Game Admin or infrastructure team.**
5. **Changes targeting a [codeowner](codeowners-policy.md)'s scope can be approved and processed by a single codeowner.**
   1. The changes must have tests that fully cover the changes that the pull request makes.
   2. If the changes are targeting performance improvements, the improvements in question must be demonstrated by a benchmark.
   3. Codeowners can self-approve their own changes targeting the codeowner's scope; the above requirements must be met before merging.
   4. The pull request must be open for at least 3 days before it is merged by a single codeowner.
   5. The fact that a scope is owned by a codeowner does not prevent other maintainers from processing a pull request via the normal review procedure; it is recommended to defer to the codeowner.

### Closing PRs
Pull requests can be closed in two ways:
- A maintainer expresses **concern** using the `S: Concern` label on GitHub. The number of maintainers who disapprove of the change required to close the PR is the same as the number required to merge the pull request.
  - For example, PRs that are classified as small content additions can be closed by one maintainer.
- It meets any one of the requirements to close listed in the section below.

#### Other Reasons for Closing
- As previously mentioned, the pull request body is not filled out to an acceptable level given the changes.
- The author has obviously not read the [code conventions](../../general-development/codebase-info/conventions.md).
- The PR's effects are inconsequential in the bigger picture for the amount of effort. Examples include:
  - Description changes that only make it "sound cooler" or "seem clearer" when in reality the name makes no difference.
  - Microbalancing, like small, finite adjustments of armor values, TC cost, etc. These changes should be rarely entertained.
- The pull request has not received any activity for a long time (30d+) after a requested change.
- The author has refused or is unwilling to implement the requested changes.
- The pull request has sat merge conflicted for a long time (30d+).
  - It is encouraged to request the author if they are willing to update it if you would like to start reviewing the pull request before doing so.
- The pull request is a draft even though it is not being put up for preliminary review.
- The PR has been superseded by a different PR and thus no longer needs to be merged.
- The PR author has been banned from the Wizard's Den GitHub and/or Discord or is otherwise unable to be communicated with.
- The PR contains content that violates Wizard Den's rules and/or code of conduct.

### Discussing PRs

If there is significant disagreement in the maintainer team about what to do with a PR, extended discussion is best held in a forum thread: tag the PR with `S: Undergoing Maintainer Discussion` and a bot will automatically create a cross-linked forum post.[^forum]

To achieve a final resolution, a deciding maintainer should do their best to weigh all discussion in the thread based on its own merits. While contributing maintainers are free to state their final opinion directly ("close" or "merge"), a simple "yes/no" vote count should not be the deciding factor for a pull request, and maintainers are encouraged to properly state their reasoning and engage with the discussion further.[^wikipedia]

If a maintainer feels that a discussion has run its course[^productivediscussion] and that a final resolution can be made. This should preferably be a maintainer with experience with the topic at hand (for example, in a relevant workgroup) but should not be a hard requirement, to avoid a resolution never being made entirely. They are expected to explain their decision based on the discussion presented in the thread so far, keeping the above guidelines in mind.

A positive conclusion should be indicated on the PR with the appropriate approval tag (`S: Conceptual Approval` for design, `S: Approved` for technical decisions).
This invalidates all disagreements/`S: Concern` tags and allows the pull request to be merged as long as the "other side" (both design and technical review) are good.

If a maintainer feels that the resolution produced by another maintainer is significantly incorrect, or did not account for the discussion properly, they should take this up with a higher authority (Lead Maintainers, Wizards, or in the future perhaps a Game Design lead). This should not be abused to endlessly keep a discussion going, and should not be used as a form of "maintainer shopping."

[^forum]: Forum threads generally avoid more low-effort "drive-by" comments from random players/contributors, and are easier to moderate.
[^wikipedia]: See also: [Wikipedia:Polling is not a substitute for discussion](https://en.wikipedia.org/wiki/Wikipedia:Polling_is_not_a_substitute_for_discussion)
[^productivediscussion]: It is entirely possible for a discussion to still be ongoing but just be repeating itself with no more productive points being made. This would still be a valid scenario in which to just put a pin in it.

### Tagging a PR as Experimental
An Experimental PR is any PR marked with the `Intent: Experimental` label.
This label is assigned at a maintainer's discretion when seeking or expecting significant feedback.

While all PRs benefit from feedback and may be changed at a later time, Experimental PRs are intended to indicate to the community that feedback is especially appreciated.

Adding the label to a PR will create a forum thread with the PR's name and number in the Feedback category of the forum. Once merged, any changelog entry for the PR will have an additional :test_tube: symbol to indicate its Experimental status.

It is strongly recommended that a `FeedbackPopup` prototype for the thread is added to `Resources/Prototypes/FeedbackPopup/feedbackpopups.yml`.

### Merging PRs
A pull request is ready to be merged if it meets the approval requirements for the PR and all requested changes are resolved.

Next:
1. Check one final time to ensure that the changelog is correct and the breaking changes section is accurate.
2. Add the pull request to the merge queue.
3. Post the breaking changes announcement in the [Breaking Changes](https://forum.spacestation14.com/c/development/breaking-changes/70) category in `Development` on Discourse.

If the pull request gets kicked out of the merge queue due to failing tests, check if the test failure is related to the PR. If not, re-add the pull request to the merge queue.

If the test is a Heisentest (a bug causing a rare, sporadic test fail), it should be logged in the [Heisentest bug tracker](https://github.com/space-wizards/space-station-14/issues/41081).
