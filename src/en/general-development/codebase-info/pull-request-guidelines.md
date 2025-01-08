# Pull Request Guidelines

Thank you for contributing to Space Station 14. When submitting pull requests (PRs), please follow these guidelines to make your pull requests easier to review and merge. Pull requests that do not follow these guidelines may be closed at a maintainer's discretion.

## Before You Begin

- If you're unfamiliar with the Git workflow, please read our [Git guide](../setup/git-for-the-ss14-developer.md) and ask as many questions as you need in #howdoicode.

- Please have some familiarity with [C# conventions](https://docs.microsoft.com/en-us/dotnet/csharp/) (if working with C#) and [our own conventions](./conventions.md). Try to read how other parts of the codebase are formatted for a general idea.

- Large new features and comprehensive reworks to existing large features (ie antags or anything that could be considered a subdepartment unto itself), should first be [proposed and accepted in abstract](../feature-proposals.md) before you start working on actually implementing it.

- Read the [Freezes and Restrictions issue](https://github.com/space-wizards/space-station-14/issues/8524) and make sure your PR does not interfere with anything or requires special requirements.
  
- If you are fixing a bug that is present on the live servers, or addressing an urgent balance issue on the live servers, consider if your change should be a hotfix.
  - Hotfixes must target the stable branch, so for these you have to fork your working branch from stable, not master.
  - You will still be able to open your PR on the master branch, even if you fork from stable but change your mind later.
  - Such a working branch, however, will not show any unreleased changes that have been merged into the game since the last release. You will not see if your code interferes or conflicts with those changes. This may become a problem, should the target of your PR be changed to the master branch. For this reason, content or feature changes should be based on the master branch.

## Content

- **Make separate PRs for feature changes, bug fixes, and cleanup/refactors.** This makes changes easier to review, reduces conflicts, and also easier to revert if something goes wrong.

    - Feature changes and bug fixes should be in their own PR.
    - Cleanups and "refactoring", including variable renaming and indentation changes (for example, due to file-scoped namespacing) must be in their own PR. 
    - **Refactors must be in a separate PR.** This includes changes that impact a significant number of public APIs (fields, methods, etc.) that require changes across multiple systems. These must be made in a separate PR from any content changes or bug fixes.
    - If you move a file to a different folder and/or namespace, put that in its own commit when possible to make it easier to tell what got changed in a file and what was just moved.
    - Mapping changes should be given a separate PR for each map changed. This includes even minor changes. 

- **Do not make multiple unrelated changes in one PR.** For example, do not make miscellaneous additional changes to a PR, e.g. changing the heat resistance of a pair of gloves alongside your PR adding a new gun.

    - Try to split your PR into smaller ones where it makes sense to do so. This makes it significantly easier to read and can lead to faster reviews. It's also usually easier for you, and means you will receive earlier feedback and can avoid spending time making changes that have to be reworked.
 
- **Start each PR with a short summary of what your PR does in simple terms, and if it's a gameplay PR link to design documents if applicable.** Being able to quickly see what your PR intends to do and how it relates to established design documents makes for faster triages and reviews. When submitting a small change, or when there is no existing design document that is applicable, the design may instead be outlined directly in the PR description.

## Testing

- **Test all of your changes in-game.** All bug fixes and features must be tested in-game. You should also test other features that may be indirectly impacted by your changes.

    - For the above reason, **do not use the GitHub web editor to make PRs.** Web edits are liable to be closed at a maintainer's discretion. Repeated submission of PRs made through the web editor may result in a repository ban.

- **Provide screenshots or videos** that demonstrate testing done. This also makes it easier to write progress reports.

## Before Submitting

- Decide/confirm if your change is an urgent **hotfix**.
    - Hotfixes do not wait for the next bi-weekly release after being merged.
    - Bugs that impact the live server or urgent balance changes can be considered a hotfix.
    - Only changes **based on the stable branch** can become a hotfix.
    - When you open a PR on github, you can select which branch it will target, and the master branch is always selected by default. For a hotfix you must select the stable branch manually.
    - If you are uncertain if your change should be a hotfix, open it targeting the master branch. Then, ask on the PR if it can be made a hotfix.

- **Review your diff** using the code preview tab on GitHub.

    - Check for changes that you did not intend to commit.
    - Check for accidental whitespace additions or line end changes.

## After Submitting

You are free to make changes to your PR after submitting, for example, if you make improvements or fix bugs that you discover after submitting.

- **Do not force push to your branch** after receiving a review unless a maintainer requests it. Doing so makes all reviews show as 'outdated', even if they have not been addressed yet.

# Reviews

Reviews are an important part of the pull request process. Reviews help us obtain feedback from the community and maintain a high quality of code in the codebase. Since maintainers are volunteers, we ask for your patience. The review process for large changes can take up to several weeks.

## Getting Reviews

- Anyone is welcome to review PRs. Reviews from other contributors can be just as valuable as reviews from maintainers, and often mean that PRs can be merged faster and can help relieve the workload for maintainers. If you are waiting for a review it might be a good idea to find another contributor in a similar position so that you can mutually review each other's PRs. Reading other people's PRs and thinking critically about how you would have written the code can also be a useful learning tool. 

- Maintainers periodically review open PRs.

- If it is taking several days to get an initial review, it is appropriate to ask for a review in #pr-review-request.

## Addressing Reviews

- When you're addressing reviews, click 'Resolve conversation' on GitHub once your revised code has been pushed.

- If you have questions about reviews that were submitted on your PR (or code questions in general, of course), feel free to ask for clarification on GitHub or Discord from the reviewer or in #howdoicode.

# Changelog
Changelog entries help make players aware of new features or changes to existing features.

## Changelog Template
The Github PR template contains the following changelog that you can use to format your changelog entry so that it is automatically updated in-game:

```
:cl:
- add: Added fun!
- remove: Removed fun!
- tweak: Changed fun!
- fix: Fixed fun!
```

By default, changes are credited to your Github username. If you would like your name to appear differently in-game, add a string on the same line as the `:cl:` with the name that you would like to use.

Each entry is either an `add`, `remove`, `tweak`, or `fix`. There can be multiple entries in each category. These set the change log icon and do not show up in the change log text.

Maintainers may, at their discretion, add, modify, or remove a change log entry that you suggest.

#### Admin changelog

Putting `ADMIN:` in the changelog will place all changelogs below it into the admin changelog category instead of the main changelog category.

Note: The category is case-insensitive, but if it is not alphabetical ending with a colon, it will fail parsing the category and will fall back to placing the changelogs in the previous category or the main changelog category.

```
:cl:
ADMIN:
- add: Added fun!
- remove: Removed fun!
- tweak: Changed fun!
- fix: Fixed fun!
```
or
```
:cl:
- add: Added fun!
- remove: Removed fun!
- tweak: Changed fun!
- fix: Fixed fun!
ADMIN:
- add: Added fun!
- remove: Removed fun!
- tweak: Changed fun!
- fix: Fixed fun!
```

## Writing An Effective Changelog
The Changelog is for *players* to be aware of new features and changes that could affect how they play the game. It is *not* designed for maintainers, admins, or server operators (these should be in the PR description).

When writing your changelog entries, please follow these guidelines:

1. **Log entries should be complete, grammatically-correct sentences.** They should begin with a capital letter and end in a period.
  
   - Not so good: "fixed reflected projectiles dealing stamina damage" This sentence does not begin with a capital letter, does not end with a period.
   
   - Not so good: "Wide attacks no longer cost stamina, deal weapon damage." Dangling clause after the comma.
   
   - Not so good: "There is now more structures that can be made out of web" Missing a period at the end of the sentence, and since "more structures" is plural, the correct verb conjugation is "are". But this entire sentence could be revised using the active voice, e.g. "More structures can now be made out of web"
   
   - Not so good: "A craft for cloth consisting of silk." This is not a complete sentence.
  
2. **Log only changes with significant in-game impact.** This may include new features or changes or tweaks to existing features that affect balance. Minor changes to object appearances and descriptions typically do *not* affect how you would play the game. Changelog entries for major sprite updates are appropriate.

   - Good: "The R&D server can be deconstructed. Be warned: this resets all unlocked technology, points, and the current discipline." Without the Changelog entry, players may not know that R&D servers can now be deconstructed. It also provides them enough warning about losing technology so that they don't accidentally get surprised.

   - Not so good: "Adjusted pickaxe inhand sprites and added sprites for wielded pickaxes." You would see the changes when you decided to wield a pickaxe. Knowing that the pickaxes look different wouldn't change your traitor strategy.
  
   - Not so good: "Changed the plating sprite to be a little less blue." Same reason as above.

   - Not so good: "Updated Security on Meta Station." Mapping changes often fill the changelog and shouldn't be included. 

3. **Use the present, active voice.**

   - Not so good: "HAMTR mech has been added."
   - Good: "The roboticist can now build the HAMTR mech." Revising this sentence in the active voice resulted in a more engaging sentence and included more relevant detail.

   - Not so good: "Added candy bowls for waiting lines." Who is doing the adding?
   - Good: "Candy bowls can now be found near waiting lines." The subject is now "candy bowls". Each sentence has a subject and a verb.

4. **Be concise and avoid wordy, "IC" changes.** Players should be able to understand the gist of the changes by skimming the Changelog. "IC" changes are harder for players to read and understand what the change was. Make changes concise and to the point. If they need more information, they can consult the guidebook. Avoid spamming multiple related changes across several different lines. If several security weapons were rebalanced, just say that to make players aware.

   - Not so good: "Central has distributed a new subversion of the standard particle accelerators. Nothing exciting, but they have brought back the old wiring layout. Apparently some of the newer versions were having firmware issues and it was more reliable. Keep on eye on it while it''s running will you? We don''t want an intern disabling the safeties and frying their face off." Do you understand what changed? Even the author thinks the change is "nothing exciting."

   - Not so good: "Due to budget cuts, detective's revolver has been replaced with something more appropriate." What is more appropriate?
   - Good: "The detective's revolver now contains cap bullets instead of lethals."
   
   - Not so good: "The Syndicate has changed around their stock prices and gotten rid of some old dusty headsets" It is unclear what changed and what this has to do with "stock prices" and "dusty old headsets".
   - Good: "The syndicate headset has been removed from the uplink." Clearly explains what was changed.
   
   - Not so good: "Due to Nanotrashen's budget cuts, Space pens are no longer supplied on the station."
   - Good: "Space pens are no longer available."

5. **Avoid technical jargon.**

   - Not so good: "Fixed microwaves defaulting to 5 seconds when the ui said instant." What is a *ui*? It could be improved by using the accepted abbreviation, "UI". Aside: Is instant really instant now, or does it just default to 5 seconds?
   
6. **Set the appropriate tone.**

   - Not so good: "Can you believe it? Arachnid re-rework just dropped! Check the PR for more details"
   
   - Not so good: "Arachnids have new sprites for being creampied." *creampied* has another, unfortunate meaning that undermines the professional tone of a Changelog entry.
