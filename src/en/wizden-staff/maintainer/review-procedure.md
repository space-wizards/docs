# PR Review Procedure
This does not apply to rule change or server config change PRs from the Head Game Admins. In an emergency these requirements may be waived with written permission from a project manager.
Not following this procedure/policy will result in disiplinary action being taken.
## Requirements
- All PRs *should* adhere to the [code conventions](../../general-development/codebase-info/conventions.md), but this is not a hard requirement since some specific usecases may require straying from convention for readability.
- PRs must be properly tagged with the relevant department/game areas.
- PRs affecting gameplay must reference a design doc/proposal. For smaller changes, the design may be outlined in the PR description. All gameplay PRs must not conflict with the core game design and should ideally reference how they fit into it.
- PRs primarily fixing bugs must be tagged with the "Bug Fix" tag.
- **2 Maintainers are required to review/sign off on merging a PR**. *This requirement may be waived with written permission from a PM when the situation warrants it.*
## Policy
- When reviewing a PR assign it to yourself to let others know that you will be "owning" the PR. If you decide to stop owning the PR, un-assign yourself so that others may take over the PR. By owning a PR you are taking responsibility for keeping track of the PR's progress and keeping the PR author informed of what is the status of the review process. Anyone may review an owned PR, however before taking action talk with the owner first. *If changes are approved by the "owner" any maintainer may merge the PR if they also approve the changes.*

- If you think a PR warrants further discussion with maintainers, you may **optionally** create a review thread in maint-reviews.  *This is not a requirement*, but is recommended when you aren't sure about something. If you do this, make sure to tag the PR with the "In Discussion" tag, and summarize the result of the discussion in the PR *before* taking any action(Such as merging or closing). The discussion thread should have the PR number in the title, and a link to the PR included within. You should also be appropriately tagging the discussion thread with the relevant work groups. Any maintainer may do this, not just the PR owner but make sure to check to not make a duplicate.

- All non-gamebreaking revert PRs *must* undergo a maintainer discussion before being created. If there is a PR that you would like to be reverted, please *create a thread in maint-reviews with the format REVERT-PRNumber and ping the relevant work group maintainers.* Discussions should reach a resolution within 48 hours, if discussions have stalled notify the Game Director or a PM.
**This does not apply for reverts made to the staging branch during the review period**, as there will be a discussion thread for the release.

- When closing a PR you must give a reason explaining why the PR is being closed, ideally this should include an alternative solution or approach. If a PR has been "dormant" it may be closed after attempting to contact the author with no response. A PR is considered "dormant" after 4 weeks of inactivity.

- When reviewing a PR use *constructive* language and avoid referring negatively to the author's ability. Strong but fair criticism of code/decisions are fine, personal criticisms are not.

- When reviewing code, don't assume that all contributors have your knowledge of the codebase. Giving a short explaination of how something works can be far more helpful than responding with jargon and pointing to the docs. *Sometimes a newer contributor may need more help, in that case direct them to #HowDoICode or the docs. But ideally you should try to give them a short explaination on what they need to do rather than just a "change this".