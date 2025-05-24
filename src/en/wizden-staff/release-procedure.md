# Release Procedure

All times are in CEST/UTC+2\
We can always just deviate from the established times below, we are not launching a rocket. But having a particular time written down would help us know when we should consider the current release to be in jeopardy

Releases are on every second week.

## Thursday
##### 20:00
Delete the old Staging branch and fork a new one from Master

Further merges into Staging follow hotfix procedures, and should be avoided if possible. This is to ensure that we have time to review proposed changes and don't break things in the last moment. 

##### 20:01
Make the new Release Review Thread in #maint-reviews "YYYY-MM-DD Release Review Thread"\
In the thread
* List the current commit range
* Create the meeting hedgedoc and link it
* Ping all maintainers

Add the list of Feature changes to hedgedoc\
This list should be double-checked because it's easy to miss something and since it's unreasonable to ask one person to spend excessive amounts of time double-checking it. 
It makes sense for at least one other person to check any remaining PRs if they should also be added. Anyone is free to review and suggest additional PRs to be listed, but it's best do this right after the thread is opened, 
to reduce the possibility that late-added entries get skipped by early reviews.

Maintainers individually add their proposed meeting topics to hedgedoc

##### UNTIL THE MEETING
Maintainers review the feature changes list and add any concerns/comments.\
If something is unfinished/broken/etc enough that you think it should not be in the current release (in its current state), **add a note starting with "VOTE", followed by the concern or reasoning.** You can further add what hotfix/conditions you think could salvage the PR in question for the current release.\
Using this unambiguous tag will help us have a smoother meeting and make the later vote/hotfix/revert process more deterministic.\
You can add notes without asking for a vote, but they will be "non-binding", and we might just skip over such lesser concerns/suggestions/ideas/~~jokes~~ during the meeting if we need to save time.

These comments also serve as the best way for people who can't make it to the meeting to engage with the revert process in a fair way. If you can't show up but have a concern, leave a VOTE note along with your concern/reason/considtions, the meeting should not strike VOTE calls just because you are not there to argue for them. (However, two objecting maints are needed for a vote to proceed, so if no one else backs it up before or during the meeting, it will still be included in the release).

## Saturday
##### 20:00 Maintainer meeting

It would be nice if we all showed up on the clock, so we could start sooner. Pre-meeting ping, maybe?

Historically, meetings have started with the Topics section. That will not be detailed in this doc.\ 
At some point, the meeting gets to the feature reviews.\
Go through any PRs that have comments. See if any notes need to be edited to become a VOTE, or if anyone changes their mind in some other way.\
If there are at least two VOTEs on a PR, it goes to a vote. Decide now what the vote options will be. The default option should be Keep/Revert, for simplicity.\
Optionally, some SIMPLE/straightforward change to the PR may be suggested. Such as tweaking numbers to something **specific** not just "it should do less damage", removing some specific, concrete part, or fixing a specific bug/issue.  This is a HOTFIX vote - during the runup to release, someone will attempt to hotfix the issue. If the hotfix is successfully merged, then the PR is kept in the release. \
For a hotfix to be considered as an option, we have to be willing to accept at least some delay with the release, it's not really fair or a great long term strategy to expect someone to rush hotfixing the issue between saturday and sunday, and for this to get a proper test/review. So when a HOTFIX vote is suggested, it has to be accompanied by a deadline - when is the time we should consider reverting the feature instead. Establishing a target time in advance will save us the additional stress of having to make that call later, during what will be already a stressful situation.\
We should probably also discuss who will write the fix, not just hope that someone will start writing the fix afterwards (yes, that has happened). It does not need to be a ~~tribute~~ volunteer from the meeting, but we should have some idea at least.

#####  AFTER THE MEETING
Votes are immediately started for contested PRs, in the release review thread. Ping all Maintainers.
> *By whom? Historically, mostly I have been doing that, and I'm fine with that SO LONG as we can keep the vote details specific and unambiguous so I don't have to come up with the details myself once everyone already left*
 
Polls should only have 2 options each: such as Keep/Revert, or Keep/Hotfix. This leaves no requirement for interpretation when the polls finish, and we don't have the maintainer team assembled. Whoever is there can enact the results, even if alone, with no special pressure or responsibility for making "the correct call".

>*Current issue: Discord sucks and the vote length can't properly be timed to our schedule. We should go with 24h vote and just note the results when the time is supposed to be up, I guess*
>Alternatively, we can just establish that if there was a vote, the release will happen when the vote runs out. Since with these proposed steps, setting the vote up should not take much time and happen right after the meeting, this would mean Sunday ~22h which would probably be an acceptable time? 

## Sunday
~~Race against the clock to finish the hotfixes in time :3~~

Make sure we are on the same page about who will do the release, and about any currently still pending issues/votes. Myra usually does the release, but just in case they might not be able to make it, we should at least verbally confirm.

##### ??:00 **<-- Pick a time**
The Official Release Time.\
Votes are tallied by anyone present, and the results posted in the release review thread 
> (since, because discord sucks, the polls would still be open at this time)

If the result is KEEP, or HOTFIX and the hotfix was already successfully merged, proceed to The Release.\
If the result is REVERT, remove the PR from staging now. This should not require multiple maint approvals - we already have consensus on it. Then proceed to The Release.\
If the result is HOTFIX, and the hotfix is not yet done, we enter a delay. This should be announced internally, so everyone is aware.
> *Should we communicate externally when we enter a delay? I don't think it's necessary, but then people will just start wondering and guessing?*

If the fix gets completed before the delay deadline, you can now do the release immediately.\
As the delay deadline approaches Available maintainers should reconvene, to decide the continued fate of the blocking PR. 
> *Short vote? Lead maintainers decide? No suggestion, too situational?*

In case of a tie during a maintainer vote, recount the lead maintainer votes only. If it's still a tie, take the more cautious option and consider the vote a REVERT or HOTFIX, whichever is applicable for the current vote. 

### The Release
Merge Staging into Stable (via push, do not create a PR). 
> List git steps? Link Myra's script?

If there were any hotfixes, merge Stable into Master as well.\
Publish Stable
> *Describe this in more detail*

*monitor if Salamander and Lizard actually deploy the new release after their next restart. See maintainer-info for details*

# Afterthoughts

With Vulture, it is no longer super-important for us to be around at release and closely monitor it. It's still a decent idea, but at this point players have already been testing the release candidate for days so there should not be any huge nasty surprises. For this reason, we have a pretty free hand at where we want to place the time of release, or when to execute a delayed release once the required fixes are complete.

> Pick the official Release Time. 

> In light of the recent suggestions from FSP, we could also consider making the Sunday meeting be ONLY about the Feature PRs and any urgent issues/concerns otherwise related to the release, to make the meeting shorter? We could discuss regular topics at another time?
