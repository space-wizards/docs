# 2026-06-27 Maintainer Meeting

# MAINTAINER MEETING

We lost the template in the Divorce. :(

Per the re-org, the Maintainer Meeting will be hosted by the Production Team which will go through the commit history before release and verify everything is up to snuff, then pass it to the Maintainer team for further review, discussion, and important development talks.

Given that there *are* no commits to review due to unique circumstances, this meeting will only have topics. \n

## Maintainers In Attendance

* Princess
* Slarti
* Fildrance
* ScarKy0
* Ress
* Jez
* Smug
* Ada
* Slam
* Mervill
* Roomba

(Meeting recording goes here)

## Topics

### Discuss how Maintainer Meetings will work in the future

* Maintainer Meetings are organized by production, who will approve a release or raise issues with it
* They will then hand the meeting to the maintainer team to raise their own concerns before the meeting and add topics and such
* Meeting will happen and they will discuss the desired hotfixes/changes/issues and how to approach them as well as topics
* Production and Maintainers will address any staging PRs needed as organized by the meeting

Basically: Production Team replaces LMs for the meetings and also does a bit extra.

### Repo Merge

In regards to merging the repos, there are a number of issues which need to be addressed including:

* Merge conflicts
* Code Quality Issues
* Duplicate Commits

The question is: What’s the best way to deal with these.

### Requesting feedback on PRs that got left/abandoned on Space Wizards Federation

Some of the downstream maintainers asked me to forward some PRs to be looked at. And on what will happen to these PRs when we will be moving ship again.

* [https://github.com/Space-Wizards-Federation/space-station-14/pull/5](https://github.com/Space-Wizards-Federation/space-station-14/pull/87)
* <https://github.com/Space-Wizards-Federation/space-station-14/pull/87>

\~\~ Ress

### Launcher Needs Some Love, Whose Job is That?

For reference here are our current development roles:

 ![](attachments/f98dc10d-dbc4-4f13-a6fe-84903a16ace5.png " =2242x401")

### Bots and Forums Relays


1. Previous relays often duplicated data, would it be best to have a “relay category” on discord and have all relays there?


2. For bots, Discord has changed how bots are handled and we need to deal with that ASAP. Also we should have Operations people who are dedicated specifically for things like Discord/Github bots tbqh.

   
   1. AAAAAAAA FML! Ye all of these changes, especially for a server/guild of our size are a pain. At this point in time, my privileged intents request (the stuff that is required to run the bots, especially 2-way relay chats for OOC and Admin chat) has not been processed by Discord yet. Furthermore this is yearly paperwork that we. And any other game server host has to do when they have a Discord server/guild above 10.000 members.

       \~\~Ress

### Bug Report Button

Please I beg of you, Subnautica button it would be so good. If we can delay them sending until end of round that would be ideal and shouldn’t be difficult if we can cache them. Either that or have them go to a private repo where they can be vetted and cloned to the main repo.

* Dedicated bug tracker?
* Save bug reports to DB and push on round end?
* Send bugs to private repository as to not explode our Github issues!!!

### Discord Development Category

Much like the temp-discord I plan to move maintainer related stuff, including the private development channels, into the development category to de-bloat the staff category. Unfortunately the development category is super bloated. Even if we crunch some of the channels down, it’s still gonna be bloated, we need a way to saw Development in half into two categories. Any ideas? “Design+Development?” “SS14 Development+Tech Development?” I’m a fence sitter, I love sitting on fences.
