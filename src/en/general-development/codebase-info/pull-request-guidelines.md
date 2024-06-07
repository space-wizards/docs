# Pull Request Guidelines

Thanks for showing interest in contributing to Space Station 14!

To make the job of the maintainers easier and to keep the project moving at its quick pace, we have these guidelines that you should follow.

If you do not follow these guidelines, it is up to the maintainer's discression whether to close it or not.

## Before You Begin

- If you are unfamiliar with the Git workflow, please read our [Git for the SS14 Developer](../setup/git-for-the-ss14-developer.md) guide and feel free to ask questions in `#howdoicode`.

- Please have some familiarity with our [conventions](./conventions.md). If you aren't, try to read how simialr parts of the code are formatted.

- Large reworks and feature additions should first be [proposed in abstract](../feature-proposals.md) and accepted before you start actually implementing it.

## General Guidelines

- **Make separate PRs** for feature changes, bug fixes, and cleanup/refactors. This makes changes easier to review, reduces conflicts, and also easier to revert if something goes wrong.
    - Feature changes and bug fixes should be in their own PR.
    - Cleanups and “refactoring”, including variable renaming and indentation changes (for example, due to file-scoped namespacing) must be in their own PR.
    - Refactors must be in a separate PR. This includes changes that impact a significant number of public APIs (fields, methods, etc.) that require changes across multiple systems. These must be made in a separate PR from any content changes or bug fixes.
    - If you move a file to a different folder and/or namespace, put that in its own commit when possible to make it easier to tell what got changed in a file and what was just moved.
    - Mapping changes should be given a separate PR for each map changed. This includes even minor changes.

- **Do not make multiple unrelated changes in one PR**. For example, do not make miscellaneous additional changes to a PR. (For example,changing the heat resistance of a pair of gloves alongside your PR adding a new gun.

- Generally, try to **split your PR** into as many smaller PRs as it would make sense to do. The smaller the PR, the faster it can be reviewed and the quicker you can iterate before being merged.

## Testing

- **You should test all of your changes in-game**. All bug fixes and features must be tested in-game. You should also test other features that may be indirectly impacted by your changes.
    - For the above reason, do not use the GitHub web editor to make PRs. An edit made through the web interface implies you haven't built or tested the change locally. Web edits are liable to be closed at a maintainer’s discretion. Repeated submission of PRs made through the web editor may result in a repository ban.

- Provide screenshots or videos that demonstrate testing being done. This also makes it easier to write progress reports.

## Before Submitting

- **Review your diff** using the code preview tab on GitHub.
    - Check for any unintended changes that have been committed
    - Check for any basic formatting errors

- Make sure you follow the [Pull Request Template](https://raw.githubusercontent.com/space-wizards/space-station-14/master/.github/PULL_REQUEST_TEMPLATE.md) which should have been autopopulated.

- Create your suggested changelog following the [changelog guidelines](#changelog). 

## Changelog

Changelogs are how we (the developers) tell the playerbase about changes that have been made to the game.

### Changelog Template

If you correctly followed the PR template, you should have a section to format how your changelog entry would look so that it would updated automatically in-game.

``````admonish info
```yaml
:cl:
- add: Added fun!
- remove: Removed fun!
- tweak: Changed fun!
- fix: Fixed fun!
```
``````

By default, all changelog changes are acreddited to your GitHub username. If you would like your name to appear as something else, add a string to the `:cl:` line with the name you wish to be used.

There are 4 types of entries, and you may have as many entries as you wish in your changelog:
1. **add**
2. **remove**
3. **tweak**
4. **fix**

Maintainers may, at their discression, add/modify/remove any changelog entry that you suggest.

### Writing an Effective Changelog

The Changelog is for players to be aware of new features and changes that could affect how they play the game. It is not designed for maintainers, admins, or server operators (these should be in the PR description).

When writing a Changelog entry, please follow these guidelines:

1. **Log entries should be complete, grammatically-correct sentences.** They should begin with a capital letter and end in a period.

   ```admonish example title="Grammar Example" collapsible=true
   **Do**:  
   `Fixed reflected projectiles dealing stamina damage.`

   **Don't**: (Not capitalized, no punctuation)  
   `fixed reflected projectiles dealing stamina damage` 

   Do:  
   `More structures can now be made out of webs.`

   Don't: (Passive voice, no punctuation, bad conjugating)  
   `There is now more structures that can be made out of web`
   ```

2. **Log only changes with significant in-game impact.** This may include new features or changes or tweaks to existing features that affect balance. Minor changes to object apperances and descriptions typically do not affect how you would play the game.

   ```admonish example title="Significant Changes Example" collapsible=true 
   **Do**:  
   `The R&D server can be deconstructed. Be warned: this resets all unlocked technology, points, and the current discipline.`

   Without the Changelog entry, players may not know that R&D servers can now be deconstructed. It also provides them enough warning about losing technology so that they don’t accidentally get surprised.

   **Don't**:  
   `Adjusted pickaxe inhand sprites and added sprites for wielded pickaxes`

   You would see the changes when you decided to wield a pickaxe. Knowing that the pickaxes look different wouldn’t change your traitor strategy.

   **Don't**:  
   `Updated Security on Meta Station`

   Mapping changes often fill the changelog and shouldn’t be included.
   ```

3. **Use the present, active voice.** Subject Action Verb.

   ```admonish example title="Present Voice Example" collapsible=true
   **Do**:  
   `The roboticist can now build the HAMTR mech.`

   **Don't**: (Who can build?)  
   `HAMTR mech has been added.`

   **Do**:  
   `Candy bowls can now be found near waiting lines.`

   **Don't**: (Who is adding?)  
   `Added candy bowls for waiting lines.`
   ```

4. **Be concise and avoid wordy, “IC” (In-Character) changes**. Players should be able to immediately undestand the jist of the change by reading the changelog entry. If they need more information, they can always consult the guidebook.

   ```admonish example title="Non-IC Examples" collapsible=true
   **Do**:  
   `The detective’s revolver now contains cap bullets instead of lethals.`

   **Don't**: (What budget cuts? What's more appropriate?)  
   `Due to budget cuts, detective’s revolver has been replaced with something more appropriate`

   **Do**:  
   `Space pens are no longer available.`

   **Don't**: (Who cares about NT's budget?)  
   `Due to Nanotrashen’s budget cuts, Space pens are no longer supplied on the station`
   ```

5. **Avoid technical jargon**.

   ```admonish example title="No Technical Jargon Example" collapsible=true
   **Do**:  
   `Microwave now defaults to the displayed time.`

   **Don't**: (What's a UI?)  
   `Fixed microwaves defaulting to 5 seconds when the ui said instant.`
   ```

6. **Set the appropriate tone**. The people reading these come from many different backgrounds and communities, so try to keep this as professional as possible. Avoid a converstational tone.

## After Submitting

You are free to keep working on the PR after submitting, such as making improvements or fixing bugs.

- **Do not force push to a branch**, unless requested by a maintainer.
    - This is because it marks all reviews as "outdated" even if they have not been resolved.

# Reviews

Reviews are an important part of the pull request process. 

Reviews help us obtain feedback from the community and maintain a high quality of code in the codebase. Since maintainers are volunteers, we ask for your patience. 

Don't be discouraged if the review process for large changes can take up to several weeks.

## Getting Reviews

- Anyone is welcome to review a PR. A review from a contributor is just as important as one from a maintainer.
    - If you feel that you are stuck waiting for a review, reach out to other contributors in a similar situation to mutually reivew each other's PRs.
    - Reviewing other PRs helps give you insights into what mistakes that the maintainers are looking for so that you can avoid them yourself.

- Maintainers periodically review open PRs, but this is not always a given.

- If it has been several days and you have not gotten an initial review, feel free to reach out on `#pr-review-request`.

## Addressing Reviews

- When you're addressing a review, click the "`Resolve converstation`" button on GitHub once you have pushed your fixed code.

- If you have questions about what a reviewer said about your PR, feel free to reach out to them for clarification on GitHub or on Discord, or even `#howdoicode`.

