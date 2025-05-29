# Hotfixing Procedure
This does not apply to rule change or server config change PRs from the Head Game Admins. In an emergency these requirements may be waived with written permission from a Project Manager or Lead Maintainer.
Not following this procedure/policy will result in disiplinary action being taken.
## Requirements
- **Three Maintainers must *sign-off*** (Aproval is required, reviewing is reccommended but optional) on a hotfix PR for it to be merged.
- The Hotfix procedure only applies to PRs being merged straight to "stable" or "staging". **When merging bugfixes to master, this procedure does NOT apply, use the normal PR procedure instead!**
- All Hotfixes must adhere to the normal [PR Review Procedure](../maintainer/review-procedure.md) in addition to any requirements listed here.
- Hotfixes must be given the "Hotfix" label during triage. They will also automatically receive a label indicating their branch.
- Stable Hotfixes are for fixing bugs only, not for adding new content or minor balance adjustments. *If a balance issue is bad enough to majorly impact game quality, it should be considered a bug and is eligable for a hotfix. This is up to Maintainer judgement, but if you are unsure it's recommended to create a discussion thread prefixed with "HOTFIX-PRNumber".
- Hotfixes to Staging may include any changes that are deemed necessary for the upcoming release, but are otherwise still referred to as Hotfixes and follow these procedures.
## Policy
- Whether a PR should be classifed as a bug fix or not is up to the Maintainers reviewing the PR. But in general, a bug fix adjusts existing content/code to fix an issue without dramatically changing the game or adding new content.
- Balancing changes are usually not bug fixes. A balancing change adjusts tuning values on a gameplay system/mechanic to change gameplay to be more in line with the intended experience. If the experience before the change is still playable, then the balancing change is not a bug fix. However, if the gameplay is *causing major issues* for Players or Admins then a balancing change can be considered a bugfix.
## Creating and applying a hotfix
A hotfix needs to be based on the branch the bug appears in. Normally, this is the stable branch. During the release period, however, the same procedure can apply to the release candidate on the staging branch.
After the PR is merged, the fixed branch (either stable or staging) must be merged back into master on the upstream repository. This cannot be done via git push, so open a PR. You do not need additional approvals for such back-merges, but may choose to ask another Maintainer to check the PR before you merge it.

It is important that you **DO NOT SQUASH a back-merge!**

## Not-so-hotfixes
If a hotfix is still unmerged after a week, it should be retargeted to the master branch. Remove the hotfix labels and tag as well.

## Walkthrough
- Determine the target branch (staging or stable)
- Create your working branch
```shell
git checkout <target branch>
git pull upstream <target branch>
git switch -c <hotfix branch name>
```
- Code and test the hotfix
- Push the hotfix to your remote repository
```shell
git push origin HEAD
```
- Go to github and create a PR for the appropriate upstream branch
- Get 3 Maintainer Approvals (including yours)
  - or written permission from a PM/Lead Maintainer
- Merge the hotfix PR
- Create a PR to merge the now-fixed upstream branch into upstream master
  - DO NOT SQUASH
- Delete your hotfix branch


## Hotfixing from the Master branch

If a fix was already merged into master, it may be possible to turn it into a hotfix for stable/staging, but **this situation should be avoided whenever possible**. Cherry-picking is extra work and has caused us some issues in the past in the later step when the branches get back-merged, so creating hotfixes on the appropriate branch in the first place or waiting until they make it through the release cycle are the preferred methods.

- Create your empty working branch from the appropriate target branch, as above
- Make sure that your local master branch is also up to date
- Get the commit hash of the merged PR from the git log or github
   ![image](https://github.com/user-attachments/assets/7ef72e09-3f01-438d-bc8b-4b658b3225df)
- Instead of coding your own changes on your branch, pick the existing commit from master
```shell
git cherry-pick <commit hash>
```
- Follow the rest of the normal procedure for merging your working branch, with one exception:
- DO NOT SQUASH MERGE when you accept a cherry-picked hotfix PR