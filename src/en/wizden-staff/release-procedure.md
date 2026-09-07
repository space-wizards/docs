# Release Procedures

All times are in CEST/UTC+2
We can always just deviate from the established times below, if necessary. But having a particular time written down would help us know when we should consider some part of the process to be overdue and start asking about it

This page describes how our release cycle functions. 
In short, we use 4-week based release cycle. 'Anchor' for cycle start and end is 'maintainers meeting' event. One release cycle does not technically (calendar-wise) 'end' with 'maintainers meeting', it 'overlaps' with next one, we are allowed to add code for next release (in master branch), while we are stabilizing our release ('staing' or later - 'stable' branch). Each cycle SHOULD lead to creation of new stable release.

## Week 3 of cycle - Saturday 20:00 - Staging cutoff

Week 1-3 of release cycle contain no special events related to our new release, PRs are merged into master. Activities, targeted at previous release (stabilization/hotfixing/etc) are described at later parts of this document.

### 0. Coordinate
Before process starts, 'Release captain' should be chosen. It is temporary informal role during this release, controlling execution of all release key steps. When the person is chosen - announce so in staff channel and tag @maintainers with message (can be done together with staging cutoff announcement), to ensure no one else is already on it. It is the Producer role team's responsibility to arrange who will be Release Captain.

'Release captain' hat can be handed over for the rest of duration of release or just temporarily in case current 'captain' cannot fully operate due to any problems, having person who can properly dedicate time to release coordination is of most importance.

'Release captain' should start with creating new instance of checklist (from temlate - https://outline.spacestation14.com/settings/templates/release-check-list-Qacv6vN8XM) and should keep it up to date.

### 1. Cut the staging branch

Announce cutoff 1 hour before starting with message in #maintainers Discord channel
```@Maintainers Hello crew, i am your Release captain for this release! We are starting to prepare things up now. Staging cutoff in 1 hour.```

Cutoff can be postponed if there are any problem with priority greater then p1.

Otherwise run the `ss14-prepstaging` function from [Myra's powershell script](https://gist.github.com/VasilisThePikachu/762b90187a5f9a0cca3249cc335cab31). It does the whole cut for you: it fetches `upstream`, syncs your local `staging` with `upstream/staging` (**oldest** commit in the update), merges `upstream/master` into it and pushes the result (**newest** commit), then prints a ready-to-paste Release Review Thread skeleton (title, commit range, compare URL and a placeholder for the Outline doc link).

>If you need to do it manually:
>```
>git switch master
>git pull upstream master
>git rev-parse HEAD
>```
>Note down the displayed hash - the **newest** commit in the update
>
>```
>git switch staging
>git pull upstream staging
>git rev-parse HEAD
>```
>Note down the displayed hash - the **oldest** commit in the update
>
>```
>git merge master
>git push upstream staging
>```

Starting that point - further merges into Staging should only happen if it's REALLY necessary, to ensure that we have time to review proposed changes and don't break things in the last moment. The process for this follows the [Hotfix Procedure](https://docs.spacestation14.com/en/wizden-staff/maintainer/hotfix-procedure.html). Revert or other changes may also be the result of a Maintainer vote after the meeting, this will be detailed below.

### 2. Create the Outline doc and open the Release Review Thread

1. Create the upcoming Maintainer Meeting doc from a template in [Outline](https://outline.spacestation14.com/settings/templates/yyyy-mm-dd-maintainer-meeting-mmNlS0WVxq) from the meeting doc template.
2. In #maint-reviews, open the Release Review Thread titled `YYYY-MM-DD Release Review Thread` with the text printed by `ss14-prepstaging`, drop in the link to the Outline doc, and ping all Maintainers. Review threads are currently on Discord, but may move to Discourse in the future.

> Manual setup:
> * Title format: "YYYY-MM-DD Release Review Thread"
> * List the current commit range: <`oldest commit hash`> - <`newest commit hash`>
> * Link the current commit range: `https://github.com/space-wizards/space-station-14/compare/<oldest commit hash>...<newest commit hash>`
> * link created outline Maintainer Meeting doc

### 3. Add the list of Feature Changes to the Outline doc

Go through the commit range list and note every feature/balance PR in the current release. See the template for the format to be used.
> You can use [this script](https://discord.com/channels/310555209753690112/909229454449078333/1350070411571757086) to generate the correctly formatted string for each PR, but you need to pick out the PRs from the full commit list manually

Notify maintainers in discord 'Release Review Thread' when PR list is up.

```@Maintainers PR list is up, please run over list and leave notes when nessesary. Reminder to lease 'BLOCKER' keyword for PRs that you view as highly problematic and needs revert (or at least no release should be done with them 'as-is'). Make sure to add yourself to 'finished reviewing' section after looking at all of the items in list.```

## Until the Meeting - Review PRs in list

### 1. Maintainers add topics that need discussion to the Outline doc

### 2. Maintainers review the feature changes 
Add any concerns/comments you have directly to the doc, you can also respond to other notes. Once you finished reviewing, add yourself to the "finished reviewing" list in the doc.

#### The BLOCK tags

If something is unfinished/broken/etc enough that maintainer thinks it should not be in the current release (in its current state), add a note starting with "BLOCK", followed by the concern or reasoning. You can further add what hotfix/conditions you think could salvage the PR in question for the current release, or if it should just be reverted outright.

Using this unambiguous tag will help us have a smoother meeting and make the later vote/hotfix/revert process easier to decide.
If you do not mark your comment with BLOCK, we will still go over it during the meeting but it will be treated as a "non-binding" lesser concern/suggestion/idea/future feature, not something that demands a vote. (If you will be at the meeting, you will still be able to change this to a BLOCK then)

Two such objections are required for a PR to go **instantly** to a revert vote (should be done in 'Release Review Thread' in discord), if someone adds a second one at this stage then we can see ahead of time that there will be a vote, and can maybe even figure out/address any concerns before the meeting. This helps everyone involved, so if at all possible, review and log BLOCKs early.

#### In Absentia

These comments also serve as the best way for people who can't make it to the meeting to engage with the revert process in a fair way. If you can't show up but have a concern, leave a BLOCK note along with your concern/reason/considtions, the meeting will not remove BLOCKs just because you are not there to argue for them. (Although if no one else seconds it before or during the meeting, then it will still not go to a vote)

## Week 4 Saturday 20:00 - Maintainer Meeting

It would be nice if we all showed up on the clock, so we could start sooner. 

Make sure to note maintainers with messages when appropriate
```@Maintainers Maintainer meeting in 1 hour```
```@Maintainers Maintainer meeting in 10 minutes```
```@Maintainers Maintainer meeting is starting NOW!```

Historically, meetings have started with the Topics section. That will not be detailed in this doc. At some point, the meeting will get to the feature reviews.

### Feature Reviews, Revert votes
Go through any PRs that have comments. See if any notes need to be edited to become BLOCKing, if anyone seconds them, or if anyone changes their mind in some other way.
If at least two Maintainers have chosen to block a PR, there will be a vote after the meeting. Decide and document **now** what the vote options will be. The default option should be Revert, for simplicity. **Check the chat for any Maintainers not on voice trying to get a word in edgewise**. If the PR's author is present, consider consulting them.

Agree now **who** will start all the votes ('Release captain' should do it), both so the votes don't get forgotten and to force the future-votemaker to double-check if sufficient details about the votes have been noted down. (It sucks trying to figure out missing details by yourself after the fact)

### Hotfix votes
Optionally, some SIMPLE/straightforward change to the PR may be suggested. Such as tweaking numbers to something **specific** not just "it should do less damage", removing some specific, concrete part, or fixing a well-defined bug/issue. It should be discussed **who** will/might write this fix, not just hope that someone will start writing it afterwards. It does not need to be set in stone or a volunteer from the meeting, but we should have some idea at least. Final deadline for fix should be chosen right away, and actions upon not reaching results on said deadline.

Since unlike a revert, a hotfix can't be finished in moments, we have to consider the possibility that there will be a schedule slip. As such, for hotfixing to be considered an option, we will specify an acceptable delay. **If we are unwilling to risk such a delay for the feature, then we should simply vote for a revert instead**, and fix it by the next release. Recommended default delay is 24 hours after the original expected Release. (Note that the time chosen is the maximum, we might finish sooner. But we should be willing to accept the full length of the delay. Record the delay's 'End time' in the meeting notes.

> All votes, whether for revert or hotfix, are RELEASE BLOCKERS. If some issue is minor enough that we could just release with it, then it might be better to just address it in the next release or hotfix it after release through the regular hotfix procedure.

### Evaluate active Feedback Pop-Up 
Feedback Pop-Ups is a feature that allows us to request players ingame to provide feedback for specific topics/PRs. As part of the meeting, go through the current active `FeedbackPopup` protoypes in `Resources/Prototypes/FeedbackPopup/feedbackpopups.yml` and evaluate which should be removed, remain on master, or provided to the stable servers. 

*No action is required* to have a pop-up remain only on the testing server, as the `PopupOrigin` property being set to `wizden_master` ensures it does not show on the stable servers. If a pop-up should be made visible on the stable servers, change the property to `wizden_master wizden_stable`. 

## Right after the Meeting
Votes are immediately started for blocked PRs. Open a Discourse thread for each vote in Discord 'Release Review Thread'. If multiple PRs are conceptually linked, and/or were contested "as one", they can be combined into one thread. Copy the summary about the situation from the meeting notes, for anyone who was not present at the Meeting. The recording might not yet be available for review before votes have to be cast.

Polls will be kept open until the official release time (roughly 24 hours later), so that every Maintainer can get their chance to vote. They must have only 2 outcomes, plus Abstain: such as Keep/Revert/Abstain, or Keep/Hotfix/Abstain. Abstain votes will not have any effect on the outcome, they merely serve to indicate that someone has seen the vote but is not participating. 
>Binary votes leave no requirement for interpretation when they finish, so we don't need to have the Maintainer team assembled for closing up the release. Whoever is there can enact the results, even if alone, with no special pressure or responsibility for making "the correct call", since it has already been determined by (the best available) consensus.

Afterwards, link the threads in #ongoing-votes and ping all maintainers.
``` @Maintainers Votes for reverts/hotfixes are up, please make sure to leave a vote, it will be closed in next 24h```

## Week 4 - Sunday, before Release

The proposed hotfix(es) can be prepared before release, but no one should feel forced to code just so we don't have a delay. If we are voting on a hotfix then we have already accepted a potential delay. It's also possible that the vote will decide to keep the PR, making the fix/change unnecessary.

Release can be postponed but status on hotfixes should be regularly checked, this is activity for 'Release captain'.

## Week 4 - Sunday, 21:00 - The Official Release Time

The Maintainers present can begin. If necessary, coordinate in the 'Release Review Thread' who's doing what. Close the votes and check the status of any other release blockers.

* If a vote's result is KEEP, the PR is no longer considered a blocker even if we want to later fix it.
* If a vote's result is REVERT, create a PR to revert the feature from Staging. This does not require multiple maint approvals - it already has them from the vote. Since we are reverting a feature from master, before it ever hit stable, remove it from the changelog as well
> Reverting a PR does not do this automatically, you need to edit changelog.yml directly. Note that you also can't add a new changelog on a hotfix PR through the normal process - they are only read from PRs on the master branch.
* If a vote's result is HOTFIX and the hotfix was already completed and approved, merge it now. Note that while the concept of the fix has been approved by the vote, it might still be a good idea to have multiple Maintainers look at it before merging, depending on complexity and ambiguity (although ideally there would be zero ambiguity). A delay was already accepted.
* If a vote's result is HOTFIX, and the hotfix is not yet completed or approved, we enter a Delay. This should be announced internally so everyone is aware, but no ping is required. Then go do whatever you want, it's sunday! Lizard will be fine.

In case of a tie, recount the Lead Maintainer votes only. If it's still a tie, take the more cautious option and consider the vote a REVERT or HOTFIX, whichever is applicable.

If no blockers remain, go to The Release.

## Delay
If the hotfixes could not be finished or tested in time, we enter a Delay. The expected maximum duration of the Delay has been agreed upon during the Maintainer meeting, and within this timeframe we should consider the delay acceptable enough not to be "concerned".

If the fix gets completed before the 'End Time', then 'Release captain' can start the release immediately, but they are also free to just note it and leave someone else to do it later within the accepted Delay.

'Release captain' should reconvene at the End Time, to decide the continued fate of the blocking PR(s). At this point there will likely be Maintainer consensus established in some way, written decisions from the Lead Maintainers / Game Director, or Lead Maintainers will be present, but if they aren't, then the Maintainers present decide whether to revert the PR in question or go into overtime waiting for the fix. There is no script for after going into overtime.

> It is up to 'Release captain' to choose if problem fixes worth additional time until release, but as a general rule it should be noted that complex/heavy fixes are undesirable (highly discouraged), as 'staging' branch does not have any testing grounds.

## The Release (timinig depends on 'when its ready'™)

### 1. Merge Staging into Stable

Do not create a PR.
Use either [Myra's script](https://gist.github.com/VasilisThePikachu/762b90187a5f9a0cca3249cc335cab31)
or plain git:

```
git checkout staging
git pull upstream staging
git checkout stable
git pull upstream stable
git merge staging
git push upstream stable
```

### 2. Add tag to release

Add release version tag on commit that will be used for our new release.

version in following script should be formed using following template
```wizden-v{YEAR}.{START-MONTH}.{HOTFIX}```
replace `START-MONTH` with two-digit month number in which release should have been published originally, and `HOTFIX` is zero-based number of publishes done for the sake of hotfixes.

example - previous release was supposed to be out on Sunday 2026-07-26 - that is start of new release cycle (the fact that it got out on 2026-07-27 does not matter - we use planned calendar dates), so next maintainers meeting and release is supposed to be in 4 weeks, 2026-08-23, so our version number for it will be `wizden-v2026.08.0` even if after A LOT of hotfixes it will be out on 2026-09-01. And any following small hotifxes, that will be released following it but without staging branch usage - will be called `wizden-v2026.08.1`, `wizden-v2026.08.2` etc.


```
git checkout stable
git pull upstream stable
git tag <version>
git push upstream <version>
```


### 3. Run Publish

You can use github-cli to start publish, [Myra's script](https://gist.github.com/VasilisThePikachu/762b90187a5f9a0cca3249cc335cab31) already does this for you.

To do it manually, go to [github's web GUI](https://github.com/space-wizards/space-station-14/actions/workflows/publish.yml) and run the workflow with the stable branch:

![runpublish.png](../assets/images/wizden-staff/runpublish.png)


Make sure that publish workflow finishes green, and check changelog discord channel to make sure new updates are published.

// TODO - need to add steps that will create GitHub release record for new release, ideally without any additional manual actions


### 4. If there were any hotfixes on Staging that weren't already merged back, merge Stable into Master.

This needs to be done via PR on github (because the master branch is protected from pushing).
You can merge this PR by yourself immediately, but **DO NOT SQUASH IT**.

If there are merge conflicts at this step, note that you could publish stable before you get bogged down fixing the conflict for master so meanwhile the publish tests can run.


### 5. Monitor if Salamander actually gets the new release after their next restart

Specifically these two servers sometimes restart for the patch, but don't actually get it due to "funny network reasons". If this happens, any Maintainer can run ```!updateserver servername``` on Discord to restart them again.

### 6. Announce that release is out and works on it are finished

Notify maintainers that all works related to release are finished.

``` @Maintainers Relase '<version>' is finished, out on CDN and Salamander! If you will notice any critical problems - please share them and make sure to prioritize hotfixes or reverts over other kind of works. ```

'Release captain' should orchestrate works on any urgent fixes / reverts that will surface once new version is available to players. Pay extra attentntion to Admins and forks (#space-wizards-enclave Discord channel) feedback.