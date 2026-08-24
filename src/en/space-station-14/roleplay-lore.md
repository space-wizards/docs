# Roleplay/Lore

```admonish warning "Not a guide"

This is not a roleplaying guide. While some of the information may be of interest to players and admins, the intended audience are the developers and maintainers of Spacestation 14.

```

Spacestation 14 is a roleplaying game. Roleplay is an integral part of the game's core design.

The aim of this document is to provide a high-level view of how roleplaying is currently supported in the game and what kinds of design decisions and contributions would be valuable in further enhancing this part of the experience. The document provides examples of good practices, already existing features, and potential features that could still be implemented.

The golden rule applies: Not all of the ideas mentioned here are guaranteed to get maintainer approval. They only serve to give some direction and inspiration. Some ideas are only mentioned because they may be of interest to heavy roleplaying servers and downstream forks.

The recommendations presented in this document should be judged on an individual basis and against the [Core Design](core-design.md) and [Design Principles](core-design/design-principles.md) of Spacestation 14.

## Roleplaying levels

Each server has its own rules for the level of roleplaying they expect from players. As a convention, servers describe the intensity of roleplaying with abbreviations LRP, MRP, and HRP, for low, medium, and high roleplay. Admins enforce these RP rules. From a design perspective, we consider this a richness; we are happy that we get to cater to many different types of players. In turn, this also means that we need to take these different playstyles into account in our design decisions.

A player's access to a medium or high roleplay server can be restricted with a whitelist. Access can be granted based on playtime and endorsements from other players or admins.
  
**Recommendations:**

- Roleplaying levels should be clearly explained in the server hub.

- It is already possible to filter, search, and sort servers based on their roleplaying level.

## Roleplaying guidelines

Different servers have different guidelines for roleplaying. These are for players and admins to observe and are not in that sense a game development issue. Roleplaying guidelines should be easily accessible through the server rules.

Game systems and policy rulings are put in place to enable play. Sometimes policy problems can be solved with code, sometimes code problems can be corrected with policy. For example, imagine a situation where walls didn't yet have collision on them. "Guys, please, let's play as if the walls had collision, okay?" would be the policy solution in this situation.

While some problems cannot be solved with neither code or policy, hopefully it is clear what they are for, what they can do, and how they interplay.

## What can we do to improve the quality of roleplay in Spacestation 14?

How a round of Spacestation 14 caters to roleplaying is most importantly determined by the playstyle of each individual player. Other factors that go into it are server population, round length, work done by admins and game masters, and of course, the game mechanics and content of the game itself.

This document attempts to focus on the content and systems of the game, and how they can be designed to lower the barrier to roleplaying and to guide players towards a playstyle that more often than not incorporates some level of roleplaying. At the end of the day, it is down to the preferences of the players whether they choose to take part in this style of play. We are here to make it as attractive, natural, and supported as possible.

At the same time, it has to be said that LRP servers and playstyles do exist, and their existence should not be challenged through game design or balancing. Support for different playstyles should be maintained through server configuration options.

Generally speaking, when we are talking about roleplaying, we are talking about interactions between players, mediated through chat, emotes, and actions. The expectation is that we are doing these actions for someone else other than us, with the hope that they would in turn return the favor. This is the magic juice, the essence of roleplaying. It begins with wanting to play with others and caring about their input, their words, emotes, and actions.

When we talk about improving the quality of roleplay, we are talking about increasing the total amount of interactions and play-time where players engage with roleplay, and making those interactions as meaningful as possible. This is done in the hope that roleplay may create some great and memorable gameplay moments and improve the gameplay experience of a sizeable portion of our playerbase, and that it in turn attracts more players to join in.

Originally, I thought this work would primarily benefit players on medium and high-roleplay servers, but perhaps they already have everything they need to participate and find enjoyment in roleplaying. Perhaps this kind of document is mostly beneficial to low RP players and new players, where every small bit of support can potentially produce noticeable improvements in the roleplaying aspects they see in-game.

## Summary: What is needed for roleplay?

- A world, a setting that is communicated to players in sufficient detail

- Some structure

- Interesting characters

- Freedom and goal-driven action

- Thoughtful players and a culture that develops them

- Time

## Roleplaying mechanics

Spacestation 14 is not a dungeon-crawler. It is not an action-RPG. Our characters have no skills, no level progression. But we do have characters, a world, and occasional combat. There's also crafting, some narrative structure, and a unique blend of immersive simulation. These are the game pieces that we work with to play the game. Now, let's go through the motions to see how we can improve these pieces and arrange them better for the purposes of roleplaying.

**Note:** Some of these design areas have their own design documents. It is a good practice that design documents mention if they have consequences for roleplaying, or design considerations from a roleplaying point of view. This document tries to summarize design decisions on the topic at a higher level and aims to work as a quick design reference and as an introduction into the topic. Additional details can be found in those other documents.

## Roleplaying culture

Roleplaying is a cultural, learned thing. Each server must decide what kind of roleplaying environment they want to cultivate. This can be a culture where roleplaying is allowed to happen, expected not to happen or a culture where roleplaying is required.

We should enable this learning and per-server cultural development to happen with the tools that we have.

**Recommendations:**

- Daily Tips should include tips for roleplaying.

- The game should be playable even if the player has no knowledge of roleplaying.

- We should aim to support varying levels of roleplaying, and help servers establish roleplaying guidelines that work for them and their players.

## The alternative to roleplaying

When players do not participate in roleplay, they do not engage with other players in-character, they may spend less time talking, and instead engage with them directly using actions and game systems. This can ruin immersion and foster powergaming. In a state of no roleplay, the following happens:

- People don't do their jobs.

- People powergame to gain items and access.

- People begin to hunt antagonists even more than they do now (validhunting).

- The station devolves into cops and robbers.

It is important to note that this can always happen, if there are no standards of play or admins to enforce them. Roleplaying is based on player freedom and creativity, and it can not be forced upon players with game logic or systems. But there can be game logic and systems that support the emergent appearance of roleplaying.

## Gameplay

Roleplaying is enabled by content. Without it, we are talking about a glorified chatroom. Complex, interconnected systems tend to generate interesting gameplay moments, conducive to roleplay.

**When designing new systems, take into account:**

- What kind of gameplay does this generate?

- How does this work together with other systems?

## Worldbuilding and mapping

The player is dropped into the world and expected to play their character in it.

**Recommendations:**

- Make use of mapping guidelines.

- Look for opportunities to do environmental storytelling.

- Add everyday environments that people are already familiar with, such as showers, toilets, and gardens.

- Create a variety of different spaces and locations: Isolated, connected, open, structured, chaotic. Variety creates opportunities for play.

- Develop systems for more advanced content-loading & map-generation.

- Add examine texts.

## Lore

What are mothmen, and why are they on the station with us? Would my character be curious about them?

- When adding new content, make sure it fits the lore of the rest of the game. 

- Include enough lore where it is needed. Make use of examine texts, books, and whatever objects are related to the content.

- It is acceptable that not all lore is present on the station. In a video game, there are many different, but also limited ways we can present lore to players. In the genre of space horror comedy, there are some things that by their nature must remain unexplained. 

- Players can develop their characters to have their own interpretations and reactions to the unknown.

- Players should be able to understand lore without having to read the design doc for the feature.

**Recommendations:**

- If there is no place in the game where the lore can be placed, an outline can be included in the pull request for future reference.

- A compendium of official lore should be collected, so it is available for reference and we may avoid conflicting entries.

- Each station should have a brief backstory that appears in the game lobby or that is discoverable on the map.

## Immersion

Immersion helps the players stay in-universe and in-character.

- Mapping should produce a coherent station layout. How many steps from a vending machine do I need to take to find a disposal unit?

- Immersion-breaking bugs are typically very noticeable.

- Sometimes we want to be zany, other times, a bit of silence may be appropriate. See the [Art guidelines](art.md) for a discussion on Theme & Style.

## Round flow

Every story has some structure to it. This forms the basis of the narrative that unfolds.

- **Roundstart** - All players begin at their designated job. This could be different and more randomized.

- **Conflict** - Usually mediated by the antagonists, although we could add other roles that are in opposition to the station, but not directly hostile towards it. Official CentCom inspectors, for example. Perhaps there should be more clowns at roundstart.

- **Station goals** - Roundstart crew objectives or commands given by a station event, this would ask the station to do something noteworthy, eg. deliver some complex item or technology to CentCom.

- **The shuttle is called** - The crew can decide to leave when they want. Some antagonists may be able to interfere with this, but it's ~~probably~~ most definitely against server rules to delay round end too much.

- **Alternate round endings** - Crew victory without shuttle call has been theorized, but the conditions for such a victory can only be clearly defined for a handful of game modes.

- If the crew survives long enough, the gamemode effectively turns into endless, players come and go, until eventually they decide to leave without much celebration. Hopefully the crew has had enough time to roleplay to their heart's content.

**Recommendations:**

- Do not mess with the round structure. Players should be the ones who decide when the round ends.

- Validhunting should not be rewarded with an early shuttle call or automatic round end.

- Develop late-join job selection and add variety to ghost roles. Allow players to fill their role and get up to speed.

- Automatic event-spawning and late-join antagonists should be configurable and controllable by game masters and admins.

- Develop systems that ask players to coordinate and play together, for example expeditions, artifacts, and station events.

- Add randomness to roundstart conditions.

## Character

- Appearance
- Clothes
- Race, gender, age
- Job
- Traits
- Examine text
- Backstory
- Knowledge and skills: what does my character know?
- Values and attitudes: how does my character feel about..
- Starting items

**Recommendations:**

- Add more ways to flesh out the player character, so that players may remember who they are and know their own character, and derive how they might act in any given situation.

- Develop the character simulation and interactions fully. Simulations for hunger and thirst are a good example of this.

- Do not add metaphysical character development systems such as experience points and levels. Certain antagonist roles, like cultists, may have natural progression through recruitment, and some jobs, like scientists, may have content unlocks through a progression of technology levels, but otherwise, such level-up mechanics have no place in this game.

## The job system

This is a massively important part of the game and one that heavily affects play. For roleplay, it is often considered the minimum required effort to play your role. We can use the job system to encourage roleplaying by creating situations where characters meet and tasks where you are asked to work together.

- What content is there to explore in each job?

- How do the jobs interact with each other?

- Are you allowed to leave your job and hang out in the bar? Are you allowed to leave your job and go explore maintenance?

- What steps do you have to take before leaving your job?

- Is the job system too restrictive? Should there be wider job descriptions for low-population rounds?

- Can the HoP's job be automated somewhat to allow faster job changes?

Some players might feel there aren't enough roles where they get to play a big role and make large-scale, meaningful, round-altering choices. The solution would be to add such roles. This could mean expanding the Bridge and adding more jobs that interact with decision-making or implementation of station goals. Or it could mean adding factions that interact with the station crew in non-hostile ways, for example merchants, a prisoner transfer or a more advanced alien race.

**Recommendations:**

- Add more co-department and in-department systems.

- Create guidelines for leaving mid-game. It should be clear if a brain-dead mob might still return, and what to do with their body in the meantime.

- Encourage tighter communication and cooperation, especially in low-population rounds.

- Create more RP-heavy roles and systems.

- Explore improvements to mid-round joining and the HoP's console. Allow players to get up to speed when they join a round.

## An example of game design, guidelines, and player expectations

The following is an example of a situation where game systems and roleplaying guidelines come together and create an environment that guides player decisions.

If you have maintenance access, is there any roleplay-related reason why your character shouldn't be going into the maintenance tunnels? If there is, and you want to adhere to roleplaying logic, perhaps you shouldn't go there. Otherwise, why not?

A player might hold the perhaps naive opinion that if you have access to maintenance, there shouldn't be an OOC roleplaying guideline restricting you from making use of that access to go and explore maintenance. This is just an example of a situation where the player's game design sensibilities and the server rules might not align. Either way, there are IC and OOC ways your decision might be corrected, either by security or by admins, depending on how strict they are and what the server rules actually are.

Again, not all problems regarding roleplaying can be solved with code contributions. It is not about the maintenance access that your character canonically perhaps should or should not have. It's about playing your character in a way that is coherent, and so that your actions respect the rules of the server. These systems and guidelines should be formed in such a way that mistakes are allowed to be corrected and learned from.

## Goal-oriented action

Roleplay is often goal-oriented. Goals are a good thing to have, especially in a roleplaying game. Players should have freedom, but also a context where they get to decide between multiple valid and interesting options.

- Is your character on a quest, or a quest-giver?

- If you were to want something, what would you want and why?

- Make the hierarchy work for you: Ask heads of station to lead and to give direction.

- Sometimes having a goal requires first having a problem. Yes, the crew should sometimes create problems for each other, and the game design should enable this. It's good for roleplaying!

**Recommendations:**

- Add structures that ask the player to make requests towards other players, and goals for themselves.

- Add content that players want to experience, so that they may set goals that they want to achieve.

- Add problems for the crew to overcome.

## Roleplaying and the new player experience

New players don't know what they are doing. This doesn't mean we shouldn't spend some time designing for them. The main things to consider are controlled learning and expectation management. We are already dropping a ton of lore, worldbuilding, mechanics, and chat messages on them. On one side, you might think, the more guideposts and structure, the better. But we also want to showcase the chaotic side of things, and allow things to take their own shape.

**Recommendations:**

- New players should be guided towards LRP servers and easy LRP jobs.

- Add a place for server messages that are specifically meant for guiding new players.

- Encourage new players to ask questions and to tell others that they are new.

- Mappers should design spaces where new players can explore freely (as a sort of hidden tutorial). The CentCom arrivals are a good example of this.

- Information that would be useful to new players should be made available near arrivals. For example, a map of the station hanging on the wall, or a brochure of the station.

- Create spaces and activities where spectating is allowed and expected. This allows new players to learn by watching others. The television system is an excellent addition for this.

- Create an offline tutorial where new players can learn the basics.

- Communicate to new players that they should try out different levels of roleplay and game styles offered by different servers.

## Population size

- Create maps that are specifically designed to play better with different population sizes.

- Automatically select an appropriately sized map based on population size.

- Develop a measure for current active players. Try to measure what kinds of activities or playstyles players are currently engaged in. Make this information available to admins and game masters, so they may be better informed of how the round is progressing. For example, count how many have recently taken combat actions, how many are off-station, how many are chilling in the bar, etc.

## Game speed and round length

Roleplaying often requires a lot of typing and reading. This takes time. Moving slower sets a different pace for interactions. This could be enforced with slower movement speed and higher stamina consumption when running. This would put more of a time cost to traversing the station, and allow more time for social interactions to take place in the mean time.

A slower roleplaying pace has implications for round length. Heavy-RP rounds tend to be longer.

## Chat

- Make it clear who is speaking. Improve the readability of chat bubbles. Make longer messages appear for a longer time.

- Experiment with different visuals for the chat window. Allows players to customize the color schemes in more detail.

- Make characters go out of breath after running. Add a cooldown to chat messages based on the length of the message.

- Add accents and dialects.

## Actions and emotes

- As a general rule, actions should have some sort of visual animation or an emote tied to them. If someone performs an action, others should be able to see them doing it.

- The readability of action feedback that appears on the player mob should be improved, and some of this feedback should be written in the chat window.

- The usability and customization of the emote wheel should be improved. These features should be explained in the guidebook.

- Emote spam should be prevented, and players should have a way of muting emotes in their settings menu, in case there is a bug that causes emote spam.

## Combat

The combat in Spacestation 14 can be very fast paced. In shooter games, this is measured as time-to-kill.

Overall, actions are much faster than talking. This could be viewed as a balance issue. By the time you get to ask, "Hey, what are you doing?", the clown is long gone. On the other hand, applying justice can be swift as well.

The combat system should not be thought of as a separate entity from roleplaying, but another area where characters get to be played as themselves. All crewmembers do not need to be adept in combat or constantly seeking action.

**Recommendations:**

- Action delays and cooldowns should be configurable. High-RP servers should have access to variables that control the speed of various in-game actions.

- Develop more varied combat situations with mechs, cyborgs, and alien lifespecies.

- Add places where crewmembers can fight and engage in combat without needing to validhunt or grief each other.

## Antagonists

Antagonists play an important role in round progression. They are one of the ways to bring about an "inciting incident", something that kicks off the action of the round.

A common problem caused by the freedom that antagonists enjoy, is that everybody wants to be the bad guy. This leads to validhunting and an incentive to call the shuttle early. To counteract this, crewmembers should be enabled to explore the mechanics of the game as fully as possible, even if they didn't get to play the antagonist.

**Recommendations:**

- Make roleplay rewarding for antagonists. Traitor keywords are a good example.

- Add variety to antagonist gameplay. Support multiple playstyles.

- Do not remove worldbuilding elements in favor of convenience or the currently popular meta.

- Two mechanically similar antagonist roles (such as traitor and changeling) can be worth keeping, if they have different lore and enable different roleplaying styles.

- Allow antagonists to work together, or alone, or against each other.

## Is roleplaying overpowered?

Paranoia has always been an integral part of the Spacestation 14 experience. Roleplaying does not necessarily mean that paranoia among the crew is reduced. That is not the end result of it, or the reason to engage in it. Someone who you are roleplaying with may still be an antagonist. The question you should be asking is, why is this guy trying to get close to me?

**Recommendations:**

- Game modes and antagonists should be designed in such a way that they don't invalidate roleplaying as a playstyle.

## Guts and glory

What are the building blocks of good stories? What are the repeating patterns of life in space? Let's talk about life and death.

- The characters of a roleplaying game should feel alive. This is especially true at the end of their life.

- Death should be a rare but expected part of any crewmember's life. The balance of the game should be tuned towards danger, with passing moments of safety.

- Death could be slow and painful, or quick and visceral. Its effect is enhanced by the gameplay that preceded it. Allowing players to face deadly challenges is a big part of the fun.

- If the situation allows, players should be given some time to struggle before they die. The last moments before death are often the most memorable.

- There should be variability between moments of violence and moments of tranquility. Roleplaying takes time, and death should not needlessly interrupt it.

**Recommendations:**

- Add more and varied ways of death and destruction.

- Add systems pertaining to blood and viscera, such as dismemberment, organs, and surgeries. These features should be properly balanced and not something you always see when you enter the bar.

- Systems related to death, blood, and gore should be configurable for different styles of gameplay. Servers should be encouraged to include content warnings for blood and gore in their description.

## Creativity and Persistence

How can the crewmembers create something of value, and how can CentCom reap that value?

- Create a simplified mapping console that allows engineers to plan new sections of the station, or new stations entirely. Use the creations of crewmembers as a basis for new mapping projects.

- Encourage mappers to use real game events and outcomes as a basis for new mapping projects.

- Allow players to create characters for specific antagonist roles: if they roll the antagonist, they get to play as their specifically crafted villain.

- Create spaces and activities where players can showcase their creations.

- Allow players to create television skits and write newspapers, books, and social media feeds.

## Admin tools

The admin tools that are especially relevant to roleplaying are:

- Tools that allow admins to act as Game Masters

- Tools that are used to enforce server rules

**Recommendations:**

- Create tools that enable admins to do more expansive campaigns and events.

- Create a game master role with limited access to easy-to-use buttons and clear responsibilities. Make game master a playable, whitelisted role.

- Develop Game Director functionality that takes over when there are no admins online.

- Add a summary of pressed admin-buttons to the round-end screen.

## Player feedback

Roleplaying is one way of playing the game and is certainly important, but it is not the only way to play. Judging how well the servers meet players' expectations is hardly possible without doing some data collection.

**Recommendations:**

- Allow servers to collect player feedback and a place to show the results of these queries.

- Develop questionnaires to track how players feel about the quality of roleplaying on their server.
