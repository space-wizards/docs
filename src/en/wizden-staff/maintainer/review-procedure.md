# PR Review Procedure

## Abstract
This documents lists the Maintainer procedure for reviewing and merging PRs to the [Space Station 14 repository](https://github.com/space-wizards/space-station-14) `master` branch (otherwise known as the Content repository).

Any portion of this procedure may be waived and/or modified with written permission (_via Discord or Github_) from a Lead Maintainer, Project Manager or Wizard.

```admonish note
Note that these procedures are ultimately flexible, however Maintainers that deviate from this policy are expected to provide concrete and valid reasoning when doing so. Getting one or more other maintainer(s) to agree with your deviation is advisable.

Note that all pull requests that are scheduled for release to `stable` are reviewed during _Stable Review_ in maintainer meetings.
```

## Reviewing Pull Requests

### PR Body
1. **All parts of the Pull Request Template must be filled out by the author.**
   1. The _About_ section should explain what the pull request does, and only what it does.
   2. The _Why/Balance_ section should justify the pull request's existence.
      1. Small bugfixes do not need a lengthy justification.
      2. If a pull request is balance-centric, the justification should be lengthy and properly explain why the change is needed.
      3. Justifications that only explain what the pull request *does* or the *effects* that the changes have should be automatically closed.
      4. Major content additions should align with the core design principles. Sufficiently large content additions might warrant a pull request to detail the broader purpose of the changes and how they fit into the current game.
   3. The _Technical Details_ section should give a high-level overview of the changes.
      1. This is more important during bugfixes or large refactors. It is not the job of maintainers to find out by themselves what the changes of a pull request are. In essence, someone who throws us slop to review and figure out if it works should not be entertained.
   4. The PR must have _media_ when applicable.
      1. Changes involving visuals, mechanics, or bugfixes should have media attached to demonstrate the changes to Maintainers and the community.
      2. If media is absent, it is questionable whether the author has tested their fix.
      3. Media is usually not required when the fix is intuitively obvious from reading the `diff` (inverted boolean logic for example).
   5. The _Breaking Changes_ section must be filled out.
      1. Breaking changes occur when the following is changed:
         1. A public API was modified.
         2. Code was moved to a different namespace, or a namespace was changed.
         3. Prototype IDs were changed or deleted (even if the IDs were migrated).
      2. Breaking changes _should_ include helpful advise on how to fix them if complicated. Simple redirections like "Use `x` namespace", "Use `Entity<T>` instead", "use `RefactoredSystem` helpers instead" are also welcome.
   6. The _Changelog_ section should be filled out if applicable.
      1. Poor quality changelogs should be pointed out and requested to be fixed.

Any pull request that does not follow these guidelines should be closed with the guidelines referenced.

```admonish note
Maintainers are expected to follow the pull request body guidelines in order to demonstrate a good example of what pull requests should look like.
```

### Approving PRs
Pull requests must pass code review in order to be merged.
The number of reviews required are determined on the type of pull request being reviewed.

```admonish note
Pull requests may be reviewed, approved, and merged by a single maintainer in specific circumstances. When a maintainer does so, the maintainer is expected to provide concrete and valid reasoning for doing so. For example, a maintainer that is known for reviewing and making prediction PRs can probably process a prediction PR by themselves.
```

If the pull request does not line up with any category listed here, defer to two approvals for a pull request.

Maintainers cannot self-approve pull requests that would only require one approval.
For example, a maintainer cannot create a PR for a small bugfix and then instantly merge it after - it must be reviewed by another maintainer.

Note that they can self-approve pull requests that require two approvals.

- **One Approval:**
  - Light code cleanup
    - This can be something like cleaning up errors in a few files, fixing formatting, or documenting a large group of files.
  - Bugfixes small in scope
    - Small bugfixes that don't touch major hotpaths, or critical code paths (like Atmospherics, Reagents, Physics, Movement, HTN, etc.).
  - Player-facing changes small in impact
    - Guidebook changes or renames, description changes or renames.
    - Small content additions that have little balancing impact, ex. new logic gates.
- **Two Approvals:**
  - Heavy code cleanup
    - Large cleanup of warnings across the codebase or the refactoring of an entire system.
    - Obsoletion of public methods.
    - Prediction of systems.
  - Critical bugfixes
    - Bugfixes that touch hotpaths or critical code paths should be brought under more scrutiny and thus involve another maintainer.
  - Performance improvements
    - These should usually come with a custom BenchmarkDotNet benchmark to prove that the PR has a meaningful affect.
  - Player-facing changes large in impact.
    - Major features, minor tweaks, new content.

#### Exceptions
There are some exceptions to the one-approval or two-approval system. They are listed below.
1. **Mapping changes must be approved by a Mapping Lead and only require one approval if the PR contains only mapping changes.**
   1. This still applies even if the change is technical in origin (like fixing a datafield spamming/inflating the size of YAML).
   2. Mapping Leads can self-approve their own mapping changes.
2. **Sprite changes must be approved by an Art Lead and only require one approval if the PR contains only sprite changes.**
   1. Art Lead approval is not required in the case of a sprite being minorly fixed up (for example, translation/rotation, removing stray pixels, etc.).
   2. Art Leads cannot self-approve sprite changes.
3. **Changes targeting a Maintainer Workgroup's game area must be approved by a member from the workgroup.**
   1. Workgroup members can self-approve changes targeting their own workgroup.
4. **Rule or server configuration changes require the approval, either written or on GitHub, of the Head Game Admin team.**

### Closing PRs
Pull requests can be closed in two ways:
- A maintainer expresses **concern** using the `S: Concern` label on GitHub. The amount of maintainers disapproving of the change required to close the PR is the same amount that would be required to merge the pull request.
  - For example, PRs that are classified as small content additions can be closed by one maintainer.
- It meets any one of the requirements to close listed in the below section.

#### Other Reasons for Closing
- As previously mentioned, the pull request body is not filled out to an acceptable level given the changes.
- The pull request's effects on the game are nil to none when thinking about the larger picture. Examples are:
  - Description changes that only make it "sound cooler" or "seem clearer" when in reality the name makes no difference.
  - Microbalancing like small, finite adjustments of armor value, TC cost, etc. These changes should be backed up heavily if making extremely finite adjustments.
- The pull request has not received any activity for a long time (30d+) after a requested change.
- The author has refused or is unwilling to implement the requested changes.
- The pull request has sat merge conflicted for a long time (30d+).
  - It is encouraged to request the author if they are willing to update it if you would like to start reviewing the pull request before doing so.
- The pull request is a draft even though it is not being put up for preliminary review.

### Discussing PRs
A maintainer may start a discussion if there is a disagreement between another maintainer on whether to merge or close a pull request, or for any other technical reason.
It is highly recommended to defer to multiple maintainers informally in a public channel.
For organization, it is best to call for a quick discussion in `#maint-quick-discussions`.

If absolutely 100% necessary, a vote may be called by tagging a PR with `S: Undergoing Maintainer Discussion`.
This will auto-create a topic on Discourse for the pull request calling maintainers to discuss and vote on whether to merge or close the pull request.

Once a conclusion is reached or regular discussion ceases, one of the following must occur:
- If a definitive decision was reached (Approve/Close), then it should be acted upon by a maintainer.
  - PRs targeting a workgoup's game area must reach a supermajority (66%) instead of a simple majority.
- If a compromise within the scope of the PR is reached, then the PR should be approved once the compromise is implemented.
  Inability/refusal to implement the compromise should result in the closure of the PR.
- If no definitive decision was reached, then the PR should be closed.

A positive conclusion should be indicated on the PR with the `S: Conceptual Approval` tag.
This invalidates all disagreements/`S: Concern` tags and allows the pull request to be merged as long as it passes code review.

If the discussion has a negative conclusion, the closure message for the PR should include a brief summary of the discussion.
This should have information about the elements that need to be addressed if a subsequent PR were to be made.