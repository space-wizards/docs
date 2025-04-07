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
2. During this time, Maintainers should discuss the nomination, raise concerns, and ask any questions they may have. If there is a clear majority of Maintainers in favor or against the nomination, the vote may be closed early.
    - If there is no clear majority, the vote must remain open for the full week.
    - Concerns about a nominated person must be addressed before the vote may close. This will delay the vote until the concerns are resolved.
    - For a vote to pass, it must have a supermajority (66%) of votes in favor. 
        - Abstain votes are considered neutral. However, if counting all abstain votes as "No" would cause the vote to fall below the required 66% threshold, the vote fails.
            - Example with 10 votes:<br>
                7 Yes, 1 No, 2 Abstain -> 7/8 = 87.5% -> Pass<br>
                7 Yes, 0 No, 3 Abstain -> 7/7 = 100%, but if 3 Abstain are added -> 7/10 = 70% -> Still passes<br>
                6 Yes, 0 No, 4 Abstain -> 6/6 = 100%, but 6/10 = 60% -> Fails<br>
3. At the end of the week, the vote will be closed and the results will be announced. If the vote passes, the person being nominated will be contacted by a Lead Maintainer and asked if they would like to accept the position. If they agree, they may then be added to the Maintainers list.

### Special Maintainer Roles

Some roles are special Maintainer roles and follow a different process to the normal Maintainer role. These roles are as follows:
- **Head Mapper**: A Maintainer responsible for ensuring mapping standards and approving and merging mapping PRs.
- **Art lead**: A Maintainer responsible for ensuring a consistent art style and approving sprite PRs.
- **Robust Toolbox Maintainer**: A Maintainer of Robust Toolbox, our underlying game engine. 

#### Starting a Vote for a Special Role

The process for adding a special Maintainer is the same as for a normal Maintainer, but with the following alterations:
- Only a member that is already a part of the special role can nominate a new member for that role.
    - When the role is empty, any maintainer can nominate a new member.
    - Lead Maintainers can nominate a new member for the role, even if they are not a part of that role.
- The template used will be the "Special Maintainer Vote" template.
    - This template has two votes that run concurrently:
        - One for members of the special role to vote on.
        - One for all Maintainer to vote on.
    - Both votes must pass for the nomination to be accepted.