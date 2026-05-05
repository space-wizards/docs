## Docs PR Review Procedure
  
The Docs repo has a different review policy compared to the Content repository.
Since the Docs repo can be pushed to directly by maintainers, is mostly text-based, can be easily reverted/changed, and does not affect forks, most docs pull requests can be handled by a single maintainer.

### Pushing to the Docs and Content Repositories
Maintainers and docutainers have direct push access to the docs repository and are encouraged to use it to update any outdated information, whether it's technical documentation, amending a design document, or just fixing grammar. 

Docutainers can also review and merge guidebook PRs on the content repository, but should not abuse this to merge non-guidebook-related pull requests.

### PR Reviews
PRs that update instructional or reference documentation (including, but not limited to, setup guides, style guides, and system documentation) require only a single approval before they can be merged.
Likewise, only a single maintainer needs to express concern to close it.

Note that this does not apply to changes to internal procedures or other modifications that require voting or group deliberation under relevant policy.

When leaving comments or requesting changes:
- Use **constructive** language and avoid being overly negative.
- Try not to be _overly_ vulgar or swear in a derogatory way.
- Avoid comments that personally criticize the author. 
  - It's okay to critique ideas and decisions, but you shouldn't insult their character.
- For people who may not be familiar with a part in their PR, try to be more thorough in your explanations.
  - Explain your review to teach people unfamiliar with the subject.
- When possible, direct people to either the [developer wiki](https://docs.spacestation14.com/index.html), `#docs` discord channel, or an alternate source for information.
- Make time to respond to questions or comments from the PR author on your review comments, so that the author doesn't have to assume and make mistakes.
  - You don't need to be constantly online, but if the author has questions, they should be able to get a response in a reasonable amount of time.
- Be formal when closing PRs. 
  - Discourage others from engaging in rude behavior and try not to upset the PR author. People can often be emotional after their PR is closed.
- For relatively minor changes, opt to simply [complete them yourself](https://cli.github.com/manual/gh_pr_checkout) and push to the PR.
- When requesting changes to a PR, keep them within the scope of the PR.

#### Design Documents
Major PRs that introduce or change a design document should require at least two maintainer approvals. Unlike other doc PRs, design docs can only be approved by those with content maintainer permissions.
If the addition is large enough, a maintainer can call a vote on the design document; however, this should be done only when the scope of the pull request warrants it.

Major game features usually follow the following dynamic:
1. A contributor creates a preliminary design document demonstrating what they would like to add, offering a high-level overview of how it fits into the game.
2. Maintainers discuss the document in an informal discussion. If most agree, the document is marked with `S: Doc Approved`, and the contributor can start work on the actual feature. As the feature is developed, the document is updated if necessary.
3. Once the content-side implementation is ready to be merged, both the design document and the content pull request are merged in tandem.

The intention is to ensure that contributors do not waste time implementing a feature that may not fit well with Upstream's intended gameplay.
