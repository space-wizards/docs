# Salvage Department Design Document

This document describes the design and purpose of the Salvage department, a subdepartment of Cargo.

## Concept

Space Station 14 is an immersive sim built upon tropes of what life on a futuristic mega-corp research station would look like. A famous trope in this area is that of the [Asteroid Miner](https://tvtropes.org/pmwiki/pmwiki.php/Main/AsteroidMiners); an underpaid, expendable prospector sent out into the dangers of space to harvest whatever valuable resource is deemed necessary. The prospector is faced with harsh working conditions, manual labor and improvisational challenges, returning back to the safety of a station with the satisfaction of a job well done.

The *Salvage Specialist* role is the embodiment of this trope in SS14. 

## Gameplay Appeal

Salvage should appeal to players seeking a fantasy of excelling in hazardous environments. In keeping with its inspiration, players should expect moments of consistent danger that require a combination of procedure and improvisation to overcome. In turn, players get to derive a sense of accomplishment surviving and succeeding in the inherently demanding tasks.

Gameplay should alternate between moments of high and low tension - keeping players constantly under pressure is ill-advised, and this ensures players gets moments to breathe and engage in social aspects of the game. The lower tension should *still be part of the gameplay loop*; players should not feel like they are underperforming by not constantly keeping the pressure up. 

Salvage should aim to provide the following experience: 
- **Hard work not for the faint of heart:** Salvagers should feel like they are *cool* for braving the mundane and strange dangers of space.
- **Opportunities for meaningful skill expression:** Having an understanding of the equipment, tasks and execution of Salvage's work should give benefits that are easy to observe and impact the player's results. 
- **Moments of rest:** The gameplay loop should naturally have breakpoints from high-pressure situations to ensure Salvagers aren't constantly in a monotonous "work mode". 
- **Fair consequences for choices:** Players should rarely feel that they are cheated into a bad position through random chance. They should be informed enough that they can point at what choice they made that resulted in a poor result.

Salvage may not appeal to players looking for a calm experience with low stakes. While players should have options in how strongly they wish to challenge themselves, Salvage should be designed to operate with a higher base level of lethality compared to other roles.

## Defining Design Goals

### Power Fantasy Gameplay

The core goal of Salvage is enabling players to feel "cool". Salvage's design achieves this through content that frames the player as undertaking dangerous challenges and overcoming them. This is communicated through the aesthetics of the environment, but also by exposing players to hazards in the course of Salvage's work. Even inexperienced players should get to have this fantasy.

When the gameplay draw comes from overcoming challenges, it necessitates consequences for failure to provide valuable contrast to success. The lethality of space (and what one may encounter in it) is part of Salvage's inherent draw. However, careful attention needs to be paid to ensure unskilled players aren't gatekept from engaging with Salvage's content. When designing for Salvage, consider mechanics that provide safety nets in case of failure, or appropriate forewarning for dangerous content. It is key that experienced Salvager players are not be able to abuse these safeguards.

### Gameplay Through Basic Verbs

Salvage's gameplay should be derived from general gameplay verbs. Players should not be expected to master deep, intricate mechanics or interfaces uniquely specific to Salvage. Instead, Salvage should build upon gameplay verbs the player is already going to be familiar with from other parts of the game, such as movement, combat, tool interactions and player interactions. Doing so keeps Salvage approachable for new players and gives cross-experience in other parts of the game. It also reinforces Salvage as a job reliant on manual labor.

Where Salvage derives its complexity is via the environments these verbs are applied in. The challenge should come from requiring player to understand which of the basic gameplay verbs is best to apply for a specific situation, and how they well execute it. The difference between an expert and a novice Salvager is not having different knowledge of the options available, but the upside/downsides of the choices they make and how they act upon them. 

This is assisted by the wide variety of verbs on offer. Players get a chance to experiment and find which solution works best for a given scenario. How do you get through a wall? Welding it down? Smashing it with a pickaxe? Using an explosive? Can you recognize other factors in the environment that favor one option over another? This type of creative problem-solving should be core to how Salvage challenges players. 

## Defining Mechanics

### Extra-Vehicular Activity (EVA)

EVA work is defined as being on the outside of the station using a space-protected suit. Treating space as dangerous is a core aspect of emulating the space station experience, and therefore any role that regularly interfaces with it has a base element of risk.

Salvage being a primarily EVA-based role opens up gameplay features that other jobs do not regularly interact with. Engineering will spend some time on the outside of the station but have little reason to step off the safety of the station catwalks, and while Security may move through space more haphazardly they only do so if there is a relevant threat to prioritize. This leaves a niche for Salvage as a job that has EVA work and zero-g traversal as core components. 

The difference in movement through zero-g, high consequence of making mistakes and inherent risk of the vacuum of space aligns with Salvage's stated goal of feeling hazardous and enabling skill expression. It also creates a contrast when Salvagers return back to the breathable atmosphere of the station, indicating the low-tension section of the gameplay loop.

### Instance Locations & Random Generation

There are inherent limitations to confining gameplay to a station. Due to wanting players to develop a sense of familiarity with stations over time, the number of stations in the game will always remain low. Station environments in SS14 are also fairly static by default. While events during a round may influence this, the size of stations results in the overall layout and theme remaining largely the same. 

The open space surrounding the station provides opportunity to utilize instantiated locations. These environments would not have the same game design requirements as a full station needing to support other roles. They can instead focus on catering to specific challenges, and provide variation in location themes and environmental storytelling. Space debris, asteroids, derelict shuttles and similar sci-fi tropes are suitable locations that can be instantiated independently of the station. 

This creates an opening for Salvage to have a niche in randomly generated environments as a gameplay draw. Familiarity with layouts is not important for these instance locations, which allows random generation to pose varied navigation challenges and unpredictable situations. 

### On-Station Tasks

While Salvage's core is on the outside of the station, Salvage must have tasks to perform on-station as well. Breaking up the high-tension gameplay outside the station is a necessity to not make the role exhausting to play. It also provides a greater opportunity for Salvagers to socialize with crew. Tasks should be as a result of, and have feedback on, Salvage's off-station gameplay. 

Tasks on-station should not be avoidable by Salvagers. It should always be easier for Salvage to go onto the station and collaborate with the crew than it would be for Salvage to resolve them themselves. This ensures Salvage has a positive relationship with the crew and keeps Salvage from being isolated. The equipment and resources Salvagers find has to be balanced with this in mind. 

The tasks should generally require collaboration that align with other roles' gameplay loops. Other players then become engaged with the content Salvage brings to them and creates positive connections with Salvage. In addition, these tasks should mesh with the general gameplay loop of cargo as a whole. This makes the progression from cargo technician to salvager natural and integrates them into the department.

### Resource Generation

Resource generators are defined as roles that spawn new materials during a round. They offset resource consumption and can create scarcity for certain high-value items. A resource generator's ability to function plays a key part in the gradual degregation of the station as the round goes on.

Instantiated locations lend themselves well to introducing new resources into the round. This, along with the trope inspiration, makes Salvage a natural fit as a resource generator. 

Departments should still be able to function without Salvage's production. However, they should be working at a lower capacity as a result of needing to generate the resources elsewhere. These other methods of generating Salvage's resources should exist but be less efficient. Salvage's contribution to the station is a timesave for other players, allowing them to focus on their core gameplay loops instead of resource gathering.

Resource generation is a defining feature of Cargo. This, together with its theme as a department that interfaces with the world outside the station, is why Salvage is a subdepartment of Cargo. 

## Pitfalls To Avoid

As a consequence of the aspects described in this document, there are certain directions Salvage could take that should be avoided. When designing new features for Salvage, avoid the following:

- Isolationism. When Salvage operates on the outside of the station, they should not be unreachable by the rest of the station crew. There may be brief moments where a Salvager and their team are positioned in an awkward location, but this should be kept temporary. Salvage should not have options that make them self-reliant and their gameplay should encourage interacting with station crew to complete tasks and use their services.
- Easy sabotage/round removal features. By working in space, Salvage has some inherent advantages to the job for antagonistic activities (e.g. EVA, salvage tools). Equipment must be evaluated in the context of antagonists/griefers getting their hands on them. 
- Overabundance of materials. It should be possible for a designer to know what resources a Salvager can and does bring in over the course of a round. Salvage should not make resource management redundant, and in turn other mechanics should not make it possible to entirely bypass Salvage's contributions. 
- Single point of failure for core gameloops. While a lack of Salvage work should be felt by the station, other roles should not be unable to progress their core gameplay loops if Salvage is not performing. In the event that Salvagers are dead/missing, it should be possible for other players to take over performing Salvage work without difficulty.
- Harvesting gamerloot. Instanced locations and random generation lends itself well to providing randomized rewards. While Salvagers should be able to find interesting things for themselves as part of their work, this should not be a primary motivator. Speeding through content to reach "loot" should be discouraged to prevent forgoing station-supporting gameplay.
- Disconnected gameplay. Salvage's gameplay loop should overlap with the gameplay loop of the average cargo tech. This means salvage should be creating or acquiring resources, then distributing resources or items to the crew in a way that promotes interaction. In addition, salvage's content shouldn't be accessible only to salvagers. Salvage content should be shared with the crew, so long as doing so doesn't detract from Salvage's EVA job duties. 
