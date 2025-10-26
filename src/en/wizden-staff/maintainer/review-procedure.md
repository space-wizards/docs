# PR Review Procedure

This documents lists the Maintainer procedure for reviewing and merging PRs to the [Space Station 14 repository](https://github.com/space-wizards/space-station-14) `master` branch. 
Hotfixes intended to be merged directly to the `stable` branch must follow additional restrictions specified in the [Hotfix Procedure](hotfix-procedure.md).

Any portion of this procedure may be waived and/or modified with written permission (_via Discord or Github_) from a Lead Maintainer, Project Manager or Wizard.

Failure to follow this procedure can result in disciplinary action.

## PR Requirements
All PRs must adhere to the [code conventions](../../general-development/codebase-info/conventions.md).

All PRs must be triaged, as per the [triage procedure](triage-procedure.md) guidelines.
Upon actioning on a PR (merging, closing, reviewing), if it is not triaged, the person actioning must triage the PR.

All PRs must not conflict with [core design principles](../../space-station-14/core-design/design-principles.md). 
Additionally, the PR author should describe how the changes they made fit into the game.
Sufficiently large feature PRs may also warrant a **Design Doc** detailing the broader scope and purpose of their changes.

All PRs must completely fill out the Github PR Template to a satisfactory level.
This includes filling out all applicable sections and attaching media when necessary.

### Breaking Changes

Breaking changes are defined as one or more of the following:
- Modifying a public API
- Moving code into a different namespace
- Changing prototype IDs (*even if migrations are present*)

All PRs that include **breaking changes** should also include a section with a summary of the changes as well as instructions on how to fix issues that may come from them.

After the PR is merged, a maintainer should make a post in the [breaking changes](https://forum.spacestation14.com/c/development/breaking-changes/70) section of the forum using the template.
This consists only of the breaking changes section from the PR itself as well as a link to the PR.

## Decision Policy
```admonish info "Exceptions on Maintainer Workgroups"
[Maintainer Workgroups](maintainer-workgroup-policy.md) have exceptions to policy regarding decisions and discussions.
This is intended to help expedite pull requests and maintain a design direction, by directing applicable pull requests to their relevant maintainer workgroups.

Exceptions to policy are listed where applicable.
```

2 Maintainers are required to sign off on decisions about a PR.
One of the sign-offs may come from a maintainer who is an author or collaborator for the PR, but the other maintainer must be uninvolved.

To merge a PR, **all** the following conditions must be met:
- The PR must receive 2 approvals for both **Code** and **Design**, given in the form of an approval checkmark on the PR's Github page.
A checkmark is assumed to indicate approval for both code and design, unless stated otherwise by the approver.
A PR created by a maintainer is assumed to have their implicit approval.
  - If a PR's changes primarily target a game area that belongs to a Maintainer Workgroup, the PR must receive at least one approval from a maintainer belonging to that workgroup. If the author is a workgroup member, they cannot self-approve for design.


- All outstanding maintainer change requests must be resolved.
If the maintainer who left the request wants, they can choose to forgo requiring the changes.
In this case, when the PR is merged, a Github issue should be created to indicate the changes that need to be made.


- If the PR has the `Changes: Sprites` label, it must additionally be approved by at least one **Art Lead** through the addition of the `S: Art Approval` tag.
Changes that are solely minor sprite fixes are exempt from this.

> Always **Squash and Merge** rather than Merge, unless a policy specifically tells you to use regular merge (see the [Hotfix](https://docs.spacestation14.com/en/wizden-staff/maintainer/hotfix-procedure.html) and [Release](https://docs.spacestation14.com/en/wizden-staff/maintainer/release-procedure.html) procedures). This can be selected with the dropdown menu on the Merge button.

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

If a PR is closed belonging to a game area controlled by a maintainer workgroup, these reasons **must** be citable from any merged design document.
If a reason cannot be cited from any merged design document, the design document **must** be amended to include these reasons.

If there is disagreement between two maintainers about whether a PR should be merged or closed, a discussion should be held as described in the "Discussion Policy" section.

## Exemptions:

```admonish info "Use Your Head"
The following are situations in which the typical decision policy can be modified or opted out of.
If you do not feel confident, feel free to follow the normal process or ask a fellow Maintainer for assistance.
```

### Fixes

PRs which fix bugs, cleanup code, improve performance, or refactor systems _without_ the introduction of new features or balance changes can be processed by a single maintainer (who is not the PR author).
The remaining decision policy requirements still apply.

### Resprites

PRs solely modifying sprites need only a single approval from an **Art Lead**.
These cannot be self-approved.

### Map Changes

PRs solely modifying map files and/or map prototypes need only a single approval from a **Head Mapper**. These may be self-approved.

### Rule/Config Changes

PRs solely containing rule changes and/or server config changes submitted by (or with written approval from) a Head Game Admin may be merged at any time with the approval of the Head Game Admin team.

### Stale PRs

A PR is considered stale if it is simultaneously awaiting changes from the author and hasn't received an update for a long period of time.

After 3 weeks, a maintainer should reach out to the PR author and give them a few days to confirm that they are still working on the PR.
If they are able to or unwilling to, the PR should be marked as stale and closed.
After 6 weeks, a PR can automatically be considered stale and closed without needing to attempt to contact the author.

Note that PRs undergoing maintainer discussion or awaiting review are not considered stale.

### Experimental PRs

An Experimental PR is any PR marked with the `Intent: Experimental` label. This label is assigned at a Maintainer's discretion and indicates the PR contains features or changes that a) are expected to get a lot of feedback from players, or b) the Maintainer team is seeking a lot of feedback on from playtesting. While all PRs benefit from feedback and may be changed at a later time, Experimental PRs are intended to indicate to the community that feedback is especially appreciated. 

Adding the label to a PR will create a forum thread with the PR's name and number in the Feedback category of the forum. Once merged, any changelog entry for the PR will have an additional :test_tube: symbol to indicate its Experimental status. 

It is strongly recommended that a `FeedbackPopup` prototype for the thread is added to `Resources/Prototypes/FeedbackPopup/feedbackpopups.yml`.

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
The maintainer should then create a Topic in the `PR Reviews` Discourse Category with the PR's name, number, link, and appropriate tags.

Discussion can then proceed with maintainers and admins giving opinions and coming to a conclusion or compromise.

Votes started on a PR that affects a game area controlled by a maintainer workgroup must reach a supermajority (66%) instead of a simple majority.

If the vote was started to settle a disagreement between two members of the same maintainer workgroup, the discussion policy is to be followed normally.

Once a conclusion is reached or regular discussion ceases, one of the following must occur:
- If the discussion was created due to a disagreement in the PR decision,
  - If a definitive decision was reached (Approve/Close), then it should be acted upon by a maintainer.
  - If a compromise within the scope of the PR is reached, then the PR should be approved once the compromise is implemented.
Inability/refusal to implement the compromise should result in the closure of the PR.
  - If no definitive decision was reached, then the PR should be closed.
- If the discussion was _not_ created due to a disagreement in the PR decision,
  - If a definitive decision or reasonable compromise was reached, then it should be acted upon and/or implemented.
  - If no definitive decision was reached, the maintainer who created the discussion may choose to resolve the PR as they see fit.

A positive conclusion should be indicated on the PR with the `S: Conceptual Approval` tag.
This replaces the need for 2 design approvals (though the code still needs to be separately reviewed) and allows the PR to be merged.

If the discussion has a negative conclusion, the closure message for the PR should include a brief summary of the discussion.
This should have information about the elements that need to be addressed if a subsequent PR were to be made.

## Docs Repo
For PRs made to the [Space Station 14 Docs Repo](https://github.com/space-wizards/docs), the above policy is to be used unless specified otherwise.

### Design Doc Process

For design documents proposing new features to be added to the game, the normal 2-approval system is used. 
Once it is approved, however, it should not be merged and instead marked with the `S: Doc Approved` label. 
This lets the author know that the design has initial approval, and they are good to start on the content PR. 

Once the content-side implementation is ready to be merged, ensure that the doc PR is updated to reflect relevant information and changes to the content PR.
Afterward, both PRs can be merged at once.

### Other

For PRs which update instructional or reference documentation (_including but not limited to setup guides, style guides, system documentation_), only a single approval is needed before it can be merged.
Likewise, only a single maintainer needs to express concern to close it.

Note that this does not apply to changes to internal procedure or other modifications which require voting or group deliberation.


## Review Guidelines
The following are general guidelines to follow when reviewing PRs. 
These are especially important to follow for first-time contributors.

- Use **constructive** language and avoid being overly negative.


- Try not to be _overly_ vulgar or swear in a derogatory way.


- Avoid comments that personally criticize the author.
It's okay to critique code and decisions, but you shouldn't insult their character.


- For people who may not be familiar with a system, try to be more thorough in your explanations.


- When possible, direct people to either the [developer wiki](https://docs.spacestation14.com/index.html), `#howdoicode` discord channel, or alternate source for information.


- Make an effort to be available after reviewing a PR.
You don't need to be constantly online, but if the author has questions, they should be able to get a response in a reasonable amount of time.


- Be formal when closing PRs.
Discourage others from engaging in rude behavior and try not to upset the PR author.
People can often be emotional after their PR is closed.


- For relatively minor changes, opt to simply [complete them yourself](https://cli.github.com/manual/gh_pr_checkout) and push to the PR.


- When requesting changes to a PR be made, keep them within the scope of the PR.
For example, while requesting small numerical adjustments on a `No C#` PR is fine, it would exceed the scope of the PR to request a new system to be added.
In cases like these, it is best to close the PR and explain the changes that would need to be made.


- If a PR touches code outside of your area of expertise and you are not confident in properly reviewing it, you should try and contact another maintainer to help with the review if possible.


- If you are helping another maintainer review a PR but do not want to dedicate yourself to a full review, you should try and follow partial review guidelines.


## Partial Review guidelines.

- Maintainers are not expected to be familiar with every system in the game or have knowledge of all fields of expertise in computer science. As such it is always okay to ask another maintainer to help with your review.

- This policy exists to lower the workload on maintainers who are requested to help with a review due to their expertise as well as improve communication around partial reviews. A maintainer may choose to leave a full review and ignore these guidelines if they want. 

- If you leave a partial review you should clearly state so. You should also try to state why the review is partial for example:
  - There were a number of standout coding issues that should be addressed before leaving a full review.
  - This PR touches an area of your expertise and you noticed some coding issues you need addressed, you do not plan to leave a full review.
  - You wanted to request a couple general things you want changed, but do not plan on returning to the PR later.

- Explaining why you're leaving a partial review helps communicate your intentions to other maintainers so that they can do full reviews later, and approve once their reviews are finished and your changes have been addressed.

- If another maintainer does not state their intention to come back to a PR later after leaving a partial review, it's best to assume they won't be coming back to do a full review. 

- As usual, doing a partial review never exempts you from changing your mind and doing a full review later. Partial reviews are purely for helping with a PR's quality without having to dedicate yourself to a full review. 
