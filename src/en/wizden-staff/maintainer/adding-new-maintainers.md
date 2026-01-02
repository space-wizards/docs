# Adding New Maintainers

This document defines the process for adding new Maintainers to Space Station 14.

## Requirements

Maintainers represent Space Wizards as staff. Certain requirements must be met before a person can become a Maintainer:
- A vote must be held according to the Voting Process outlined below.
- Be a member of the Space Station 14 Discord server.
- If the nominee has caused Administration issues in the past, these issues must be raised and discussed during the voting process. Administration issues include, but are not limited to, being banned from the game, banned from the Discord server, or having a history of being rude to other members of the community.
- Have a good understanding of the Space Station 14 codebase and how it works. This must be raised and discussed during the voting process.
- Have a solid understanding of the culture and values of the game and community

### Voting Process

To add a new Maintainer, a current Maintainer has to nominate the candidate. Once a person has been nominated, the following process should be followed:
1. A vote will be created in the "Internal" category on the Space Station 14 Discourse, using the appropriate template. This vote will be open for one week, and all Maintainers will be notified of the vote.
2. During this time, Maintainers should discuss the nomination, raise concerns, and ask any questions they may have.
    - If there is a unanimous vote in favor or against the nomination by the end of day 2 of the vote, it may be closed early.
        - If this happens, the Lead Maintainer Team will review the vote and decide if it should be closed or remain open for the full week.
    - If there is no clear majority, the vote must remain open for the full week.
    - Concerns about a nominated person must be addressed before the vote may close. This will delay the vote until the concerns are resolved.
    - For a vote to pass, it must have a supermajority (66%) of votes in favor. 
        - Abstain votes are considered neutral. Only votes in favor or against are counted.
3. Once the vote is closed, the results will be announced. If the vote passes, the person being nominated will be contacted by a Lead Maintainer and asked if they would like to accept the position. If they agree, they may then be added to the Maintainers list.

### Special Maintainer Roles

Some roles are special Maintainer roles and follow a different process to the normal Maintainer role. These roles are as follows:
- **Head Mapper**: A Maintainer responsible for ensuring mapping standards and approving and merging mapping PRs.
- **Art lead**: A Maintainer responsible for ensuring a consistent art style and approving sprite PRs.
- **Robust Toolbox Maintainer**: A Maintainer of Robust Toolbox, our underlying game engine. 
- **UI Lead**: A Maintainer responsible for ensuring a consistent UI style.

#### Starting a Vote for a Special Role

The process for adding a special Maintainer is the same as for a normal Maintainer, but with the following alterations:
- Only a member that is already a part of the special role can nominate a new member for that role.
    - When the role is empty, any maintainer can nominate a new member.
    - Lead Maintainers can nominate a new member for the role, even if they are not a part of that role.
- The normal template will be used.
    - This template has two votes that run concurrently:
        - One for members of the special role to vote on.
        - One for all Maintainer to vote on.
    - Both votes must pass for the nomination to be accepted.


## On-boarding New Maintainers
Once a new Maintainer has been accepted, they must be on-boarded. The pre-requisites for on-boarding are:
- The new Maintainer provides their Discord, GitHub and Space Station 14 usernames to the Lead Maintainer that is on-boarding them.
- They must log onto the Wizden Forums once.

### On-boarding Process

1. Invite the new Maintainer to the `Maintainers` group on Discourse, as well as the special Maintainer groups if they are a special Maintainer.
2. Add the new Maintainer to our Keycloak.
3. Ask PJB to invite the new Maintainer into our GitHub organization.
4. Update the Maintainer list on our [docs](/en/wizden-staff/space-wizards-maintainer-list.html)
5. Add relevant workgroups on Discourse and Discord.

### Additional Notes

- Read the [maintainer tools](/en/wizden-staff/maintainer/maintainer-tools.html) page to see some useful tools that can help you as a maintainer.
- Read the [maintainer policy](/en/wizden-staff/maintainer/maintainer-policy.html) and [review procedure](/en/wizden-staff/maintainer/review-procedure.html) to see which rules you have to follow when merging PRs.
- Read the [doc page](/en/general-development/codebase-info/releases.html) on how our release model and maintainer meetings work. They happen every two weeks and the event schedule can be found on discord.
- After being invited to the GitHub organization, go to the space-wizards org > People > Find yourself > and set your organization visibility to public. This allows people to more easily see you are a maintainer (you will have a “Member” attached to your comments) AND you get to flex the org on your github profile.
- It is recommended to set up two-factor authentication for your Discord, SS14, and github accounts to ensure they cannot be compromised.
- If you want to debug something on the live wizden servers, then you can ask a headmin for debugging permissions. These will need to be approved by the admin team first. Remember that these should only be used for debugging purposes and should not be abused.
- Optional: Ask for permissions to see our grafana dashboards. These contain server performance metrics, game statistics, and admin tools to view bans. You have to be at least 18 years old because it contains PII.
- The [#staff-sorority](https://discord.com/channels/310555209753690112/1193403928096821358) channel is for staff chat that needs to be non-public, for example discussions about abusable bugs, highly controversial opinions on game design, reports to community moderators and so on. Anything not SS14 related should go into [#staff-offtopic](https://discord.com/channels/310555209753690112/1145595686201610252). Code and game design discussion should go into the respective public channels whenever possible so we don’t spam the staff channel and contributors can take part. Important staff discussions should be a forum post on discourse so they don’t get lost.
