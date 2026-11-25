# Revert Procedure

The revert procedure is a set of guidelines for maintainers to follow when they need to revert a change in the codebase. This is typically done when a change has caused issues or bugs that need to be addressed quickly.

## When to Revert
- A change has caused a critical bug that needs to be fixed immediately.
- A change has caused a significant performance issue.
- A change has caused a significant gameplay issue that needs to be addressed immediately.

In all of these cases, the change should be reverted as soon as possible to prevent further issues. This is especially important if the change has been merged onto master and is affecting the live game.

## Revert Procedure
0. **Create an Issue**: Create an issue that outlines that the servers are indeed on fire or that the change has caused other major issues. Assign yourself to the issue and add any relevant details.
1. **Identify the Change**: Determine which change needs to be reverted. If applicable, any PRs that depend on the change should be identified as well.
2. **Create a Revert**: Use either the `git revert` command to create a new commit (and PR it!) that undoes the changes made by the original commit, or use the GitHub UI to create a revert pull request. Make sure to include a clear message explaining why the revert is necessary. Apply the P0 label to the PR and link to the issue created in step 0.
3. **Review the Revert**: Follow standard review procedures for the revert. This includes having another maintainer review the changes to ensure that the revert is correct and does not introduce new issues.
4. **Merge the Revert**: Once the revert has been reviewed and approved by another maintainer, it can be merged. Once merged, you must run the `Publish Testing` [workflow](https://github.com/space-wizards/space-station-14/actions/workflows/publish-testing.yml) to ensure that the revert is applied to the testing server.
5. **Investigate the Original Change**: After the revert has been merged, the original change should be investigated to determine what went wrong. This may involve looking at the code, running tests, or discussing with other maintainers. 
Create a timeline of events, including when the change was made, merged, and when the issue was first reported. This will help in understanding the context of the issue and what needs to be done to fix it. If any policies were violated, this should be noted as well. It is important to understand the root cause of the issue to prevent it from happening again in the future.
6. **Update the Issue**: Update the issue created in step 0 with the findings from the investigation. This will help track the issue and provide context for future changes. If the original change needs to be fixed, create an issue detailing what went wrong and what needs to be done to fix it.
7. **Inform the Original Contributor**: Comment on the original PR to explain why the change was reverted and what needs to be fixed. Use the following template for the comment:
```
@[Pr author's username],

The changes done in this PR have been reverted due to [reason for revert].
For more information, see the #[issue number].

Please feel free to open a new PR with the necessary changes once the issue has been addressed.
```
8. **Document**: If the investigation revealed any gaps in the process or policies that led to the issue, document these in the relevant documentation.

**Note**: The timeline of a revert is important. The revert should be done as quickly as possible. Ping Lead Maintainers if a revert is not being done quickly enough. 

## Servers On Fire
If a change has caused the servers to become unstable or crash, the following steps should be taken:
1. **Notify the Maintainers**: Immediately inform the Maintainers about the issue. This can be done via Discord. This may be done by any staff member.
2. **Assign a Maintainer**: A Maintainer should be assigned to handle the issue. This can be a Lead Maintainer or any other maintainer who is available. The assigned maintainer should be able to work on the issue immediately and be available for any questions or discussions that may arise.
3. **Identify the Cause**: Determine which change caused the issue, if at all. This involves looking at the commit history and/or looking at server logs via Grafana.
4. **Revert the Change**: Follow the revert procedure outlined above to revert the change
5. **Restart affected Servers**: Regardless of server stability or round status, the affected servers should be restarted to ensure that the patch is no longer applied.

**Note**: Do not attempt to fix the issue while the servers are on fire. The priority is to stabilize the servers first, then address the underlying issue.

## Additional Notes
- Reverts should be done as quickly as possible to minimize the impact on the game and players.
- If a revert is necessary, it should be communicated clearly to the community to avoid confusion.