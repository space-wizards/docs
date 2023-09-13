# Pull Request Guidelines

Following these guidelines will make contributing much easier, and will help your PRs be merged much faster by making them easy to review.

- If you're unfamiliar with the Git workflow, please read [our git guide](../setup/git-for-the-ss14-developer.md) and ask as many questions as you need in #howdoicode.
- Do not use the GitHub web editor to make pull requests. You are required to make sure your code compiles and you've tested your changes in-game before making the PR. **PRs created through the Github web editor are liable to be closed at a maintainer's discretion, as they have not been tested locally and cannot meet these requirements.** Repeated submission of PRs made through the web editor may result in a repository ban.
- Please **re-read your code preview on GitHub** before submitting a PR. If it's obvious to a reviewer it includes your last PR (i.e. PR2 includes PR1's changes), or that there are accidental changes, then it should be obvious to you.
- If your PR adds a new feature, you should provide a screenshot or video of it functioning properly ingame. This not only makes reviewing easier, but also makes writing the progress report easier.
- Avoid adding miscellaneous additional changes to a PR, e.g. changing the heat resistance of a pair of gloves alongside your PR adding a new gun.
- Avoid making lots of formatting changes in a file if you change very few lines in it. It makes the review significantly more difficult to parse what actually changed and can generate conflicts for other PRs.
- If you do make refactoring/formatting changes, make them separate commits from actual content/feature/functionality changes so that they are easier to review.
- Large refactors that touch a lot of other systems belong in a separate refactor-only PR with no content changes
- If you move a file to a different folder and/or namespace, put that in its own commit when possible to make it easier to tell what got changed in a file and what was just moved.
- Please have some familiarity with [C# conventions](https://docs.microsoft.com/en-us/dotnet/csharp/) (if working with C#) and [our own conventions](./conventions.md). Try to read how other parts of the codebase are formatted for a general idea.
- Try to split your PR into smaller ones where it makes sense to do so. This makes it significantly easier to read and can lead to faster reviews. It's also usually easier for you, and means you will receive earlier feedback and can avoid spending time making changes that have to be reworked.
- Avoid force-pushing to your branch. This makes all reviews show as 'outdated', even if they have not been addressed yet, which makes it much harder for us.
- When you're addressing reviews, click 'Resolve conversation' on GitHub once your revised code has been pushed.
- If you have questions about reviews that were submitted on your PR (or code questions in general, of course), feel free to ask for clarification on GitHub or Discord in #howdoicode.

## Reviews

We get around 700 PRs a month and only have a small number of active maintainers. All maintainers are volunteers and maintainer availability is very variable. Depending on the size and importance of your PR, it could take up to a few weeks before someone gets around to reviewing it. Responding to any changes may also take some time. Please be patient.

Anyone is welcome to review PRs. Reviews from other contributors can be just as valuable as reviews from maintainers, and often mean that PRs can be merged faster and can help relieve the worload for maintainers. If you are waiting for a review it might be a good idea to find another contributor in a similar position so that you can mutually review each other's PRs. Reading other people's PRs and thinking critically about how you would have written the code can also be a useful learning tool. 

### Asking for reviews
Please do not simply post your PR in our discord channels without context simply to ask for reviews. However, if your PR hasn't been reviewed by anyone and it has been a month, feel free to ping those listed here on GitHub or Discord. These aren't all of our maintainers, but they're currently the most active when it comes to reviews.

**For content reviews:**
- mirrorcult#9528, @mirrorcult on GitHub
- metalgearsloth#7697, @metalgearsloth
- ElectroSR#9529, @ElectroJr
- /tmp/moony#0029, @moonheart08

**For engine reviews:**
- metalgearsloth#7697, @metalgearsloth
- PJB#3005, @PJB3005
- ElectroSR#9529, @ElectroJr
- mirrorcult#9528, @mirrorcult

## Adding screenshots/videos to your PR
PRs which make ingame changes (adding clothing, items, new features, etc) are required to have media attached that showcase the changes or the PR will not be merged, in accordance with our PR guidelines. Small fixes/refactors are exempt. If you include media in your pull request, we may potentially use it in the SS14 progress reports, with clear credit given.

Use screenshot software like Window's built in snipping tool, ShareX, Lightshot, or recording software like ShareX (gif), ScreenToGif, or OBS (cross platform).
If you're unsure whether your PR will require media, ask a maintainer.

## Changelog
Changelog entries help make players aware of new features or changes to existing features.

### Changelog Template
The Github PR template contains the following changelog that you can use to format your changelog entry so that it is automatically updated in-game:

```
:cl:
- add: Added fun!
- remove: Removed fun!
- tweak: Changed fun!
- fix: Fixed fun!
```

By default, changes are credited to your Github username. If you would like your name to appear differently in-game, add a string on the same line as the `:cl:` with the name that you would like to use.

Each entry is either an `add`, `remove`, `tweak`, or `fix`. There can be multiple entires in each category. These set the change log icon and do not show up in the change log text.

Maintainers may, at their discretion, add, modify, or remove a change log entry that you suggest.

### Writing An Effective Changelog
The Changelog is for *players* to be aware of new features and changes that could affect how they play the game. It is *not* designed for maintainers, admins, or server operators (these should be in the PR description).

When writing your changelog entries, please follow these guidelines:

1. **Log entries should be complete, gramatically-correct sentences.** They should begin with a capital letter and end in a period.
  
   - Not so good: "fixed reflected projectiles dealing stamina damage" This sentence does not begin with a capital letter, does not end with a period.
   
   - Not so good: "Wide attacks no longer cost stamina, deal weapon damage." Dangling clause after the comma.
   
   - Not so good: "There is now more structures that can be made out of web" Missing a period at the end of the sentence, and since "more structures" is plural, the correct verb conjugation is "are". But this entire sentence could be revised using the active voice, e.g. "More structures can now be made out of web"
   
   - Not so good: "A craft for cloth consisting of silk." This is not a complete sentence.
  
2. **Log only changes with significant in-game impact.** This may include new features or changes or tweaks to existing features that affect balance. Minor changes to object apperances and descriptions typically do *not* affect how you would play the game. Changelog entries for major sprite updates are appropriate.

   - Good: "The R&D server can be deconstructed. Be warned: this resets all unlocked technology, points, and the current discipline." Without the Changelog entry, players may not know that R&D servers can now be deconstructed. It also provides them enough warning about losing technology so that they don't accidentally get surprised.

   - Not so good: "Adjusted pickaxe inhand sprites and added sprites for wielded pickaxes." You would see the changes when you decided to wield a pickaxe. Knowing that the pickaxes look different wouldn't change your traitor strategy.
  
   - Not so good: "Changed the plating sprite to be a little less blue." Same reason as above.
   
   - Not so good: "Changed sprites for some medipens."

3. **Use the present, active voice.**

   - Not so good: "HAMTR mech has been added."
   - Good: "The roboticist can now build the HAMTR mech." Revising this sentence in the active voice resulted in a more engaging sentence and included more relevant detail.

   - Not so good: "Added candy bowls for waiting lines." Who is doing the adding?
   - Good: "Candy bowls can now be found near waiting lines." The subject is now "candy bowls". Each sentence has a subject and a verb.

4. **Be concise.** Players should be able to understand the jist of the changes by skimming the Changelog. If they need more information, they can consult the guidebook. Avoid spamming multiple related changes across several different lines. If several security weapons were rebalanced, just say that to make players aware.

   - Not so good: "Central has distributed a new subversion of the standard particle accelerators. Nothing exciting, but they have brought back the old wiring layout. Apparently some of the newer versions were having firmware issues and it was more reliable. Keep on eye on it while it''s running will you? We don''t want an intern disabling the safeties and frying their face off." Do you understand what changed? Even the author thinks the change is "nothing exciting."

5. **Avoid technical jargon.**

   - Not so good: "Fixed microwaves defaulting to 5 seconds when the ui said instant." What is a *ui*? It could be improved by using the accepted abbreviation, "UI". Aside: Is instant really instant now, or does it just default to 5 seconds?
   
6. **Set the appropriate tone.**

   - Not so good: "Can you believe it? Arachnid re-rework just dropped! Check the PR for more details"
   
   - Not so good: "Arachnids have new sprites for being creampied." *crampied* has another, unfortunate meaning that undermines the professional tone of a Changelog entry.