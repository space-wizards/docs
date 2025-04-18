# PR Review Procedure

This documents lists the Maintainer procedure for reviewing and merging PRs to the [Space Station 14 repository](https://github.com/space-wizards/space-station-14) `master` branch. 
Hotfixes intended to be merged directly to the `stable` branch must follow additional restrictions specified in the [Hotfix Procedure](hotfix-procedure.md).

Any portion of this procedure may be waived and/or modified with permission from a Project Manager or Wizard.

Failure to follow this procedure may result in disciplinary action.

## PR Requirements
All PRs must adhere to the [code conventions](../../general-development/codebase-info/conventions.md).

All PRs must be triaged, as per the [triage procedure](triage-procedure.md) guidelines. 
If a PR is not triaged, this should be done at the same time as the PR is initially considered for review.

All PRs must not conflict with [core design principles](../../space-station-14/core-design/design-principles.md). 
Additionally, the PR author should describe how the changes they made fit into the game.
Sufficiently large PRs may also warrant a **Design Doc** detailing the broader scope and purpose of their changes.

All PRs that include **breaking changes** (*e.g. modifying public APIs, moving code into another namespace, changing a prototype ID, etc.*) should contain a "breaking changes" section.
This consists of a summary of the changes as well as how to apply them.
After the PR is merged, the maintainer should format a message containing the PR link, the entirety of the "breaking changes" section, and a ping for `@contrib-notification` and post it into the `#codebase-changes` channel of the Discord.

All PRs must complete fill out the Github PR Template to a satisfactory level.
This includes filling out all applicable sections and attaching media when necessary.

## Decision Policy
2 Maintainers are required to sign off on decisions about a PR.
One of the maintainers is allowed to be an author of the PR, but the other should be uninvolved.

To merge a PR, **all** the following conditions must be met:
- The PR must receive 2 approvals for both **Code** and **Design**, given in the form of an approval checkmark on the PR's Github page.
A checkmark is assumed to indicate approval for both code and design, unless stated otherwise by the approver.
A PR created by a maintainer is assumed to have their implicit approval.


- All outstanding maintainer change requests must be resolved.
If the maintainer who left the request wants, they can choose to forgo requiring the changes.
In this case, when the PR is merged, a Github issue should be created to indicate the changes that need to be made.


- If the PR has the `Changes: Sprites` label, it must additionally be approved by at least one **Art Lead** through the addition of the `S: Art Approval` tag.
Changes that are solely minor sprite fixes are exempt from this.

To close a PR, at **least one** of the following conditions must be met:
- At least 2 maintainers must express wanting to close the PR or an unwillingness to merge it. 
This can be expressed either on the PR itself, or privately.


- The PR contains content which violates Wizard Den's rules and/or code of conduct.


- The PR author has been **banned** from the Wizard's Den Github and/or Discord or is otherwise unable to be communicated with.


- The PR is **Stale**.


- The PR has been superseded by a different PR and thus no longer needs to be merged.

If a PR is closed, the maintainer must leave a message indicating the reason for its closure.
This should be a formal message that includes all relevant information.
If a maintainer discussion was held, it should be summarized and included here. 

If there is disagreement between two maintainers about whether a PR should be merged or closed, a discussion should be held as described in the "Discussion Policy" section.

## Exemptions:

```admonish info "Use Your Head"
The following are situations in which the typical decision policy can be modified or opted out of.
If you do not feel confident, feel free to follow the normal process.
```

### Fixes

PRs which fix bugs, cleanup code, improve performance, or refactor systems _without_ the introduction of new features or balance changes can be processed by a single maintainer (who is not the PR author).
The remaining decision policy requirements still apply.

### Resprites

PRs solely modifying sprites need only a single approval from an **Art Lead**.
These cannot be self-approved.

### Map Changes

PRs solely modifying map files and/or map prototypes need only a single approval from a **Head Mapper** (including a self-approval).

### Rule/Config Changes

PRs solely containing rule changes and/or server config changes submitted by (or with written approval from) a Head Game Admin may be merged at any time with the approval of the Head Game Admin team.

### Stale PRs

A PR is considered stale if it is simultaneously awaiting changes from the author and hasn't received an update for a long period of time.

After 3 weeks, a maintainer should reach out to the PR author and give them a few days to confirm that they are still working on the PR.
If they are able to or unwilling to, the PR should be marked as stale and closed.
After 6 weeks, a PR can automatically be considered stale and closed without needing to attempt to contact the author.

Note that PRs undergoing maintainer discussion or awaiting review are not considered stale.

### Drafts

PRs should not be marked as drafts unless there is a meaningful reason behind them.
Simply opening an incomplete PR as a draft is not permitted and will result in immediate closure.

Drafts are only permitted if a portion of the PR requires review and/or approval in order for other segments of the same PR to be completed.
Note that this does not apply if the PR is able to be easily atomized.

## Discussion Policy

Maintainer discussions are an optional way to gain insight into general staff sentiment.
They can be used both when there are disagreements regarding a PR and when a maintainer is not confident in the design of a PR.

PRs actively undergoing a maintainer discussion should not be merged.

To begin the discussion process, add the `S: Undergoing Maintainer Discussion` tag.
This should automatically create a post in the `#maint-reviews` discord channel with the PR's name, number, link, and appropriate tags.

Discussion can then proceed with maintainers and admins giving opinions and coming to a conclusion or compromise.
Once a conclusion is reached or regular discussion ceases, one of the following must occur:
- If the discussion was created due a disagreement in the PR decision,


- - If a definitive decision was reached (Approve/Close), then it should be acted upon by a maintainer.


- - If a compromise within the scope of the PR is reached, then the PR should be approved once the compromise is implemented.
Inability/refusal to implement the compromise should result in the closure of the PR.


- - If no definitive decision was reached, then the PR should be closed.

  
- If the discussion was _not_ created due to a disagreement in the PR decision,


- - If a definitive decision or reasonable compromise was reached, then it should be acted upon and/or implemented.


- - If no definitive decision was reached, the maintainer who created the discussion may choose to resolve the PR as they see fit. 


A positive conclusion should be indicated on the PR with the `S: Conceptual Approval` tag.
This replaces the need for 2 design approvals (though the code still needs to be separately reviewed) and allows the PR to be merged.

If the discussion has a negative conclusion, the closure message for the PR should include a brief summary of the discussion.
This should have information about the elements that need to be addressed if a subsequent PR were to be made.

## Review Guidelines
The following are general guidelines to follow when reviewing PRs. 
These are especially important to follow for first-time contributors.

- Use **constructive** language and avoid being overly negative.


- Avoid comments that personally criticize the author.
It's okay to critique code and decisions, but you shouldn't insult their character.


- For people who may not be familiar with a system, try to be more thorough in your explanations.


- When possible, direct people to either the [developer wiki](https://docs.spacestation14.com/index.html), `#howdoicode` discord channel, or alternate source for information.


- Make an effort to be available after reviewing a PR.
You don't need to be constantly online, but if the author has questions, they should be able to get a response in a reasonable amount of time.


- Be formal when closing PRs.
Discourage others from engaging in rude behavior and try not to upset the PR author.
People can often be emotional after their PR is closed.


- For relatively minor changes, opt to simply complete them yourself and push to the PR.


- When requesting changes to a PR be made, keep them within the scope of the PR.
For example, while requesting small numerical adjustments on a `No C#` PR is fine, it would exceed the scope of the PR to request a new system to be added.
In cases like these, it is best to close the PR and explain the changes that would need to be made.
