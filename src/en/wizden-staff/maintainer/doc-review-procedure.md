## Docs PR Review Procedure
  
The Docs repo has a different review policy compared to the Content repository.
Since the Docs repo can be pushed to directly by maintainers, is mostly text-based, can be easily reverted/changed, and does not affect forks, most docs pull requests can be handled by a single maintainer.

### Pushing to the Docs Repo
Maintainers have direct push access to the Docs repo and are encouraged to use it to update any outdated information, whether it's technical documentation, amending a design document, or just fixing grammar.

### PR Reviews
PRs that update instructional or reference documentation (including, but not limited to, setup guides, style guides, and system documentation) require only a single approval before they can be merged.
Likewise, only a single maintainer needs to express concern to close it.

Note that this does not apply to changes to internal procedure or other modifications that require voting or group deliberation according to relevant policy.

#### Design Documents
Major PRs that introduce or change a design document should require at least two maintainer approvals.
If the addition is large enough, a maintainer can call a vote on the design document; however, this should be done only when the scope of the pull request warrants it.

Major game features usually follow the following dynamic:
1. A contributor creates a preliminary design document demonstrating what they would like to add, offering a high-level overview of how it fits into the game.
2. Maintainers discuss the document in an informal discussion. If most agree, the document is marked with `S: Doc Approved`, and the contributor can start work on the actual feature. As the feature is developed, the document is updated if necessary.
3. Once the content-side implementation is ready to be merged, both the design document and the content pull request are merged in tandem.

The intention is to ensure that contributors do not waste time implementing a feature that may not fit well with Upstream's intended gameplay.
