# Combat Design Document

## Concept

Combat in SS14 is a core part of the experience, acting as a way to exert influence in the game world on the same level of importance as speech and interactions. It is by far the most brute-force method of doing so as the main goal of combat is to forcibly deprive another party of resources, whether that be health, time, opportunity or equipment. Because of this it is a natural enabler (and sometimes solution) for conflict, creating an underlying system for consequences that reverberates throughout the game.

Combat should be possible at a range from low to high lethality, with the latter risking consequences for participants that may last for the remaining duration of the round. You should not have to be good at combat to play SS14, but combat will be something every player has to engage with to some degree on the station, whether that be through being an active combatant, desperate self-defense or just fleeing the danger.

## Intended Experience

- Intent matches consequences; a friendly boxing match is easily recovered from, a deadly gunfight is not.
- Weapons matches lethality; a single punch can be shrugged off, a baseball bat hurts, several knife wounds kill.
- Equipment matches role; if your role isn't combat-oriented, your equipment and environment will reflect that. 
- Viable and variable choices; the game provides meaningful choices in the equipment and strategies you choose to bring to combat. 
- Reactable combat: you may not have time to do everything you want, but you should generally have time to respond with *something*. 
- Centered on strategy; understanding how to strategize on both macro and micro levels of combat is rewarded, with adapting to others' strategies on the fly being key to success.

## Responsibilities

- PVP Combat
    - Player versus player combat is ultimately intended to facilitate fun, in the form of exciting and interesting combat scenarios between intelligent and active combatants. It provides a unique avenue of skill expression that rewards strategizing, adapting to other players, as well as reaction time and execution.
    - Roleplaying is also largely reinforced by combat. The outcomes of any violent situation can push a narrative forward, create conflict between those involved, and generally allow for a richer experience for those who value it. The inherint randomness and chaos combat injects into a roleplay experience makes it an incredibly valuable asset to facilitate the kinds of experience we want players to have.
    - For players who don't wish to engage in PVP, the game has to provide options to offload engagements to those that do. This may not always be possible due to combat being both core to the game and forceful, but players must feel they have some control over the amount of PVP combat they engage in.
- PVE Combat
    - Player versus environment or player versus enemy combat provides players with a more controlled, predictable and metered experience while also allowing them to have bouts of action during their usual shift activities. 
    - This combat is also intended to be more approachable, and generally easier than PVP combat, simply because one side of the conflict is more predictable. We as game designers are also able to more easily control and facilitate PVE combat as it is often tied to predictable spawns in hostile environments, random events, or mistakes players make during a round. 
    - PVE combat can also often be the spark that ignites a blaze of PVP combat. A violent kerfuffle between a member of one department and an NPC enemy provides anyone an opportunity to exploit a vulnerable player. Also, certain departments must interrupt their usual routines to handle a PVE threat, which opens opportunities for antagonists to make their moves, which sometimes are PVP-oriented.
- Action, consequences and a driving force. 
    - Combat helps provide action to the game. Following [Bartle's Taxonomy of player types](https://en.wikipedia.org/wiki/Bartle_taxonomy_of_player_types), there isn't much in this game that otherwise caters to players in the *Killers* category. In other words, there are plenty of things which cater to the *Achievers*, *Socializers*, and *Explorers*, but the *Killers* out there would be missing a core part of what they look for in a gaming experience if not for combat.
    - The nature of combat having direct and indirect consequences for players means it provides a more intense experience overall. The bursts of combat is key point of immediate higher-risk action, even for roles that are not combat-focused. 
    - Without any combat in the game it acts more like a chatroom or requires the game to lean more heavily into its simulation aspects to make up for the lack of driving forces. While this may be enjoyed by some players, [the game is meant to feature elements of chaos](https://docs.spacestation14.com/en/space-station-14/core-design/design-principles.html#chaos) which combat handily provides. 
- Resource consumption.
    - Combat (and moreso the consequences thereof) is a significant resource consumer, providing meaning to resource generators' gameplay. This includes the resources used to facilitate combat, but also fixing the consequences (e.g. Engineering repairs and Medical treatment).

## Desired Gameplay

- Tactics trumps equipment, equipment trumps mechanical execution.
    - SS14 combat should primarily reward selecting the correct tactics for any given situation; do you push, flank, ambush, retreat? Getting the jump on an opponent, forcing them into a disadvantageous position and making them waste resources should be rewarded. Part of this is selecting the correct equipment and utilizing it correctly, but this should be secondary to tactics as to not create a combat system where the outcome is determined the moment the players select their equipment. Similarly, combat should allow snap decisions in the middle of fighting, but focus should not be on testing real-life mechanical execution. 
    - Combat can have all above elements to some degree; what is important is where the system puts emphasis. Some mechanical skill will be necessary with player movement and weapon handling, but the system shouldn't make it be main determining factor unless the other two are near equal. 
    - This is partially an accessibility accomodation as well, reducing the need for having high real-life motor skills to be efficient in SS14 combat. 
- Equipment using up resources is generally stronger than equipment that doesn't.
    - Resources can be ammunition, throwables, charges, grenades etcetera. The difficulty/cost of acquiring the equipment and its resource (if any) should generally match its strength, scaled by the role for which it is available to. 
- Teamwork results in something greater than a sum of its parts.
    - Coordinating with a team not only allows for greater fire power, but also enables strategies that would be impossible to execute solo. The game should have options that encourage teamwork, while still allowing occasional "clutch" plays from single actors who strategize correctly.
    - The game permits short and long term mutual assistance; players can quickly team up when opportunity presents itself, be in a more structured team, or indirectly supporting each other. The game should let the players do this dynamically, with the team being able to change on the fly. 
    - This teamwork is part of what makes certain areas of the station feel "safe". An area which contains your colleagues who you can expect will call for help or even assist in case you get attacked is an area you will be more likely to spend time in. On the other side of the coin, being somewhere alone means you'll be more exposed the dangers of combat.
- Other elements of the game should exist in a mutually beneficial cycle with combat.
    - Combat is one of the core areas where chaos can arrise in a round. The results of that chaos should create opportunities for other roles to shine.
    - Other areas of the game that are not combat-oriented should have something they can bring to combat scenarios, rewarding skilled play in other areas of the game, as well as solid preparation. 

## Undesired Gameplay

- Extreme lethality, even in low-stakes situations.
    - Real life conflicts can turn surprisingly deadly surprisingly fast. While we want to have some semblance of real-life consequences to combat, minor scuffles should be at best healed on its own and at worst require a quick in-and-out trip to Medical.
- Single best choice.
    - We want combat to be varied with regards to what kinds of equipment is available to those involved. There shouldn't be a "meta pick" in regards to weaponry, and instead we should aim to provide players with several interesting decisions when they apporach a combat situation. 
    - These decisions should also be methods through which players can express themselves. Players who play their characters in particular ways may opt for specific kinds of weaponry, and shouldn't necessarily be punished since it's not the "meta pick". Obviously, this excludes purposefully bad decisions; bad decisions should exist, but be clearly communicated. 
- "No Win" scenarios.
   - "No win" scenarios should be kept to a minimum whenever possible. Preperation and equipment should give a player the edge in combat, but there should rarely be situations where the other side is left with zero meaningful actions - though sometimes that action may be to run away. 
- Stalemates.
    - It can be fine if encounters end in ties, whether that be through both parties disengaging or both falling in combat. What should be avoided are situations where neither side can progress the combat. This could be seen if resource drain is slow or non-existent, such as having immense healing/defensive capabilities, or playstyles that encourage holing up in a single location with difficulty for the other side to breach through.
- Always at the forefront, for everyone.
    - The game should not encourage combat to always be the focus of attention. Not only do players need downtime between intense encounters to recover and gather themselves, but other non-combat parts of the game are detracted from if players feel they always need to be prepared and ready for combat encounters. Different roles may have different emphasis on combat (some which focus heavily on it), but overall SS14 is "a game with combat", not "a combat game".
