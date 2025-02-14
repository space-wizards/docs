# Hotfixing Procedure
This does not apply to rule change or server config change PRs from the Head Game Admins. In an emergency these requirements may be waived with written permission from a project manager.
Not following this procedure/policy will result in disiplinary action being taken.
## Requirements
- **Three maintainers must *sign-off*** (Aproval is required, reviewing is reccommended but optional) on a hotfix PR for it to be merged. This can be bypassed in an emergency, for a critical fix.
- The Hotfix procedure only applies to PRs being merged straight to "stable". **When merging bugfixes to master, this procedure does NOT apply, use the normal PR procedure instead!**
- All Hotfixes must adhere to the normal [PR Review Procedure](../maintainer/review-procedure.md) in addition to any requirements listed here.
- Hotfixes must be tagged with the "Hotfix" and relevant department/game area tags.
- Hotfixes are for fixing bugs only and not adding new content or minor balance adjustments. *If a balance issue is bad enough to majorly impact game quality, it should be considered a bug and is eligable for a hotfix. This is up to maintainer judgement, but if you are unsure it's recommended to create a discussion thread prefixed with "HOTFIX-PRNumber".
## Policy
- Whether a PR should be classifed as a bug fix or not is up to the maintainers reviewing the PR. But in general, a bug fix adjusts existing content/code to fix an issue without dramatically changing the game or adding new content.

- Balancing changes are usually not bug fixes. A balancing change adjusts tuning values on a gameplay system/mechanic to change gameplay to be more in line with the intended experience. If the experience before the change is still playable then the balancing change is not a bug fix, however if the gameplay is *causing major issues for players/admins* then a balancing change can be considered as a bugfix in this case.
## Creating and applying a hotfix
A hotfix needs to be based on the branch the bug appears in.
During the release phase bugs on staging need to be fixed using hotfixes based on staging and vice versa.
The hotfix branch needs to be merged into the affected branch (staging/live) and then into master.

If a bug needs to be fixed on live during the release cycle the hotfix branch needs to be based on live and then merged into staging and master.

This will eventually be done by a github action or a bot automatically.