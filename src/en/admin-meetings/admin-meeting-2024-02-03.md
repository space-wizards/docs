# Admin Meeting 2024-02-03

## Agenda

- Brief updates from last meeting
- What are the top 5 ish admin issues at the moment that devs can fix?
- Mirror bans
- Event feedback vote
- Trialmin process improvements
- What do admins want from the chat system beyond a filtering system?

## Topic Details

### What are the top 5 ish admin issues at the moment that devs can fix?

#### Summary

> An admin issue is an issue that causes non-negligible admin burden. Issues that players face can be admin issues, but even game breaking player issues are not necessarily admin issues.
> 
> This meeting topic is only interested in the most critical admin issues, and only the ones which can be fixed by developers. The goal is to ensure developers are aware of the issues.
> -Chief_Engineer

#### Meeting Goals

1. Quickly create a list of, at most, a few admin issues which can be fixed by developers, and which are currently causing the most substantial load on game admins.
2. Create a list that describes each issue with enough detail that a game admin can either create or find GitHub issues for those items so that they can be forwarded to maintainers.

### Mirror bans

#### Summary

> A mirror ban is a ban that is placed on our servers for actions a player took on another server. The [related thread](https://discord.com/channels/310555209753690112/1192505119141535804/1192505119141535804) appears to have stalled, so this topic seeks to find conclusions to the discussion there.
> 
> Discussion points mentioned here should be relayed to the thread, either through actual discussion or through posting the relevant section of the meeting minutes.
> -Chief_Engineer

#### Meeting Goals
1. Determine a rough consensus or narrow voting options for the mirror ban criteria: Where must the player have been originally banned from to be eligible for a mirror ban?
2. Determine a rough consensus or narrow voting options for the mirror ban criteria: What must the player have been originally banned for to be eligible for a mirror ban?
3. Determine a rough consensus or narrow voting options for the question: Do we verify the criteria in some way, and if so how?
4. Determine a rough consensus or narrow voting options for the mirror ban criteria: Once any original ban criteria and verification criteria have been met, do we take any additional steps before placing the mirror ban, like running a vote?
5. Determine a rough consensus or narrow voting options for the mirror ban criteria: If the additional steps are time consuming, is there an expedited process for time sensitive mirrors, like raiders?
6. Determine a rough consensus or narrow voting options for the question: What do we do if a player appeals a mirror ban?

### Event feedback vote

#### Summary

> We currently use a 1-9 scale as the standard for event feedback. What are people's opinions on using a 1-5 scale with a "I didn't notice any admin intervention" option?
> 
> The purposes of this would be:
> 1. 1-9 is so granular that the difference between adjacent options may be meaningless.
> 2. It is currently unclear which option players should pick if they do not notice an event, which may skew results for low visibility events.
> 3. Having feedback on how many players noticed an event will give some indication of how wide impact the event was.
> -Chief_Engineer

#### Meeting Goals

1. Answer the question: What should be the standard event feedback vote?

### Trialmin process improvements

#### Summary

> We will be accepting new trialmins soon. Are there any improvements that can be made to the way they are handled? This includes anything from the onboarding guide and announcement to mentoring and mentor reviews to internal votes and discussions.
> 
> Our current mentoring process is:
> 1. Mentors are selected by CE
> 2. Trialmins are accepted
> 3. 1-2 days later, they are assigned their mentors
> 4. Mentors aim to do weekly reviews of at least the notes and bans made by their mentees
> -Chief_Engineer

#### Meeting Goals

1. Have an actionable list of improvements to be made to the trialmin process, that can ideally be actioned before the next batch is accepted.

### What do admins want from the chat system beyond a filtering system?

#### Summary

> The contributor currently refactoring the chat system has asked us for our feedback on what the admin team would need out of an upgrade chat system.
> -nikthechampiongr

> There is a list (Link removed) that can be added on to.
> -Chief_Engineer

#### Meeting Goals
1. Provide relevant feedback to the contributor so they can understand what the needs of the admin team are from the chat system from Critical functionality to stuff that would be good to have.

# Meeting Minutes

## Attendees

```admonish info 
- Zoldolf - Wizard
- Chief_Engineer - Headmin
- ShadowCommander - Project Manager
- ElectroSR - Project Manager
- ryan_strudfelt - Propermin, Mediator
- nikthechampiongr - Propermin, Minutes Editor
- ajexrose - Propermin
- Sphiral - Propermin
- TurboTracker - Propermin
- WithinElysium - Propermin
- Repo - Propermin
- Crazybrain - Propermin
- Skarlet - Propermin
- Kezu - Propermin
- Kayek - Propermin
- FairlySadPanda - Special Guest
```

## Minutes

### Top 5ish admin issues

- Grids collide when FTLing.
- F3 menu does not show information about grid/map/coords. [#24925](https://github.com/space-wizards/space-station-14/issues/24925)
- A lot of the log types are either unclear, dead, or both. Logs need to be cleaned up and properly annotated.
- There is no way to search specifically for the contents of chat messages in logs. Any query inputted in the log panel will search the entire log, often giving irrelevant results.

### Mirror Bans

- This may lead to players that have been voucher banned never being able to get a voucher if other servers mirror our bans.
- Mirror bans can only come from trusted servers.
- All mirror bans should be tagged.
- Mirror bans should have attached notes with more information on what it was for, why it was mirrored, etc.
- General consensus seems to be that mirror bans should not be made unless the reason is something agregious such as Pedophelia, or people who are purely disruptive to the game such as raiders. Basically if an individual has done something that makes us not want them in our server under any circumstances.
- For a mirror ban to be applied a record of the player's notes in the other server must be provided.
- After a potential ban has been properly tagged and has had information attached it can either be applied immediately(this can be handled by trusted individuals) or put to a vote.
- The following information can be shared with other servers for mirror bans: Uid of the player, note history, replays. 
- We could either allow players to appeal those bans normally, or require that they get unbanned on the mirrored server.

```admonish info "Conclusion"

Bans will only be mirrored from trusted servers for reasons that make us not want to have that player play on our servers under any circumstances. Mirrored bans will need to have enough information attached that prove the player's behavior.

```

### What do admins want from the chat system

- FairlySadPanda was brought into the meeting as a special guest for this discussion.
- What we would want was discussed and put in this document (Link Removed)

### Trialmin process improvements

- Get the trialmins to stop pulling 12 hour shifts a day.
- Mentors need to actually do reviews.
- Mentors are not really the people trialmins immediately got to, they instead mostly go to the first available admin.
- Trialmins can be overwhelmed when brought into the admin team and coming into a voice chat with literally every other admin that they may hold in high regard or are scared of.
    - To solve this we bring them in incrementally.
    - We can have additional vcs that are used for orientations of trialmins by mentors.
- Make it clearer that actions are reversible, or require confirmation so they should not be scared to explore their tools. There are some buttons tho that will still fuck you over.
- Better Documentation is needed on tools, and general admin activities.

```admonish info "Conclusion"

We need to make sure that trialmins don't get overwhelmed by the sheer amount of new knowledge, and people they will meet when joining the admin team. Mentors should take care to given them a proper orientation and should take more care in interacting with their trialmin and writing the reviews.

Actions taken: Propermins will not swarm them upon joining. They will receive more orientation from their mentors.
```

### Rework on voting system for event feedback

- It will be standardized to 1-5  vote + "I did not see the admin intervention option".

### Discussion outside Agenda Items

N/A

## Overall Conclusion

- There were relatively few admin issues this week.
- Mirror bans will only come from trusted servers for inexcusable things and go through relatively thorough review. 
- What we want from the chat system was properly discussed and the contributor is fully aware of what we need. 
- Trialmins need more guidence and proper care from mentors. Some pain points like the usage of their tools, or documentation need to be addressed.
- Event feedback vote standardized to 1-5 vote + didn't see the event.
