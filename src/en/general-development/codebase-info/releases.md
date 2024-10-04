# Release Process
Space Station 14 uses a rolling release model for updating the servers. **Updates are deployed every 14 days** onto the "stable" branch, while development takes place on the "master" branch. For urgent bugfixes, **hotfixes are pushed nightly** from the "stable" release branch or immediately *if the fix is critical*. **Content on the development "master" branch is *not fully commited to*** and may be removed or held back from the next update. 

What does this mean for you? If you're a fork developer, this means that you now have the choice to pull from the *more stable* release branch, *or* pull from the latest development branch to get the latest changes even if they might change or get reverted. If you're a contributor or upstream maintainer, this means that your changes won't immediately be pushed to live (unless they qualify as a bug fix). If you're a player this means that there will be larger but less frequent updates that have more content, while the daily updates will be limited to bugfixes.

## How does this work?
### Deploying Updates
Updates are deployed every 14 days over the course of a weekend (Usually on a Saturday). 2 days prior to update day, "master" will be branched into "staging" and maintainers will perform a review of the upcoming changes. During this period, changes may be made or PRs may be reverted on the staging branch. Release day also coincides with the day of the regular maintainer meeting, half of which will be devoted to looking over the changes prepared for release. The outcome of this meeting determines if the update will be deployed as is, receive changes, or be delayed. The following 2 days after an update is deployed will allow for balance/minor gameplay fixes to be deployed under the normal Hotfix procedure.

### Review/PR Procedure
All PRs must be reviewed according to the PR review procedure [documented here](../../wizden-staff/maintainer/review-procedure.md), and may be merged to the development branch "master" at any point. PR's fixing code bugs or critical gameplay issues *may* be merged directly onto the "stable" branch but in that case must additionally follow the Hotfix procedure [documented here].

### What is Hotfixable?
Any issue that directly impacts a player's ability to play the game in a largely negative way and can be considered by most to be a "bug" is eligable to be merged as a Hotfix. Critical gameplay issues may also fall into this category as well. "Critical" being an issue that is majorly disruptive to players **or admins**. *Outside of an emergency*, all **Hotfixes require 3 maintainers to sign-off** on merging (Ideally they should also review but giving approval is enough). Bugfixes may be applied to master following the regular review requirements.

### Branching
There are *three* branches that are used in this process:

**Master:** This is the primary development branch and where PRs normally get merged into. Content in the development branch is not final and may be reverted or changed before ending up being released. This branch should generally not be used for hosting a server or as an upstream since it is not guarunteed to be stable and may have reverts.

**Stable:** This is the "release" branch that the wizden servers run off of. Content in this branch should generally be considered "commited" and won't be reverted except for in exceptional circumstances. This is the branch you should use as an upstream or if you are hosting a server. Only bugfix PR gets directly merged into this branch, content PRs are merged into "master" and then the entire branch is deployed to "staging" and then merged into "stable".

**Staging:** This is a special branch mainly only used for preparing updates. During the update period (2 days leading up to the release), this branch will be pulled off from "master" to review the merged PRs in preparation for the release. Any changes/reverts needed for the release will be made in/to the "staging" branch which will be merged into the "stable" and "master" branches on update day. When not preparing an update, the staging branch is not used.
