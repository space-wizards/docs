# PR Review Procedure

This documents lists the Maintainer procedure for reviewing and merging PRs to the [Space Station 14 repository](https://github.com/space-wizards/space-station-14) `master` branch (otherwise known as the Content repository).

Any portion of this procedure may be waived and/or modified with written permission (_via Discord or Github_) from a Lead Maintainer, Project Manager or Wizard.

```admonish note
Note that these procedures are ultimately flexible, however Maintainers that deviate from this policy are expected to provide concrete and valid reasoning when doing so. Getting one or more other maintainer(s) to agree with your deviation is advisable.
```

## Reviewing Pull Requests

### PR Body
1. **All parts of the Pull Request Template must be filled out.**
   2. The _About_ section should explain what the pull request does, and only what it does.
   3. The _Why/Balance_ section should justify the pull request's existence.
      4. Small bugfixes do not need a lengthy justification.
      5. If a pull request is balance-centric, the justification should be lengthy and properly explain why the change is needed. Justifications that only explain what the pull request *does* or the *effects* that the changes have should be automatically closed.
   6. The _Technical Details_ section should give a high-level overview of the changes.
      7. This is more important during bugfixes or large refactors. It is not the job of maintainers to find out by themselves what the changes of a pull request are. In essence, someone who throws us slop to review and figure out if it works should not be entertained.
   8. The PR must have _media_ when applicable.
      9. Changes involving visuals, mechanics, or bugfixes should have media attached to demonstrate the changes to Maintainers and the community.
      10. If media is absent, it is questionable whether the author has tested their fix.
      11. Media is usually not required when the fix is intuitively obvious from reading the `diff` (inverted boolean logic for example).
   12. The _Breaking Changes_ section must be filled out.
       13. Breaking changes occur when the following is changed:
           14. A public API was modified.
           14. Code was moved to a different namespace, or a namespace was changed.
           15. Prototype IDs were changed or deleted (even if the IDs were migrated).
       16. Breaking changes _should_ include helpful advise on how to fix them if complicated. Simple redirections like "Use `x` namespace", "Use `Entity<T>` instead", "use `RefactoredSystem` helpers instead" are good examples.

Any pull request that does not follow these guidelines can and should be closed with the guidelines referenced.

```admonish note
Maintainers are expected to follow the pull request body guidelines in order to demonstrate a good example of what pull requests should look like.
```

### Deciding on PRs
Pull requests must pass both _code review_ and _design review_ in order to be merged. Guidelines for code review and design review are flexible and dependent on the type of pull request being merged.

If a pull request does not fit any descriptor listed here, then it is assumed to need just two approvals for _code review_.

When a maintainer approves a PR, it is implied that they are approving for both _code review_ and _design review_. The maintainer must comment if they only give _code review_ approval or _design review_ approval.

#### Non-player-facing changes
Pull requests that are non-player-facing like small bugfixes, code cleanup (minimal or no logic modification) or documentation additions only need **one approval** for code review and no approval for design review.

Pull requests that significantly refactor
