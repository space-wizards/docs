# Space Ninja

## Overview

The Space Ninja is a mid-round antagonist primarily focused on station disruption and sabotage, de-emphasizing crew lethality in favor of stealth and avoiding direct confrontation. Playing as the Space Ninja should feel "cool"; slipping past crew into restricted areas to complete objectives, doing silent takedowns on unsuspecting targets, and escaping danger as bullets fly past. For crew the Space Ninja should be a force that disrupts regular station work, but one that deterred by staying together with other crew.

## Background

Space Ninjas are a classic SS13 antagonist, and its inclusion in SS14 fills a niche of being a solo midround antagonist that doesn't directly focus on death and destruction, instead opting to cause issues for the station in other ways. Before this document was written, the role has been in the game for a long time and has largely been seen as an enjoyable antagonist for both the player and the crew. It features unique theming in the form of the "Spider Clan", a nefarious shadow cult that aims to... well, do evil ninja stuff. The specifics don't matter: You are a badass sci-fi ninja. Get the job done.

## Features

Some staples of the Ninja kit includes:
- Toggleable invisibility
- Teleportation, with some limitations
- Ability to stun singular targets
- High mobility, low resistances
- Built-in space protection
- No ability to use guns
- Cool sword & ninja aesthetics

Example objectives:
- Reach the R&D server in Science (generally in an off-limits area) and destroy researched Technologies
- EMAG doors around the station, enabling trespass and making spacing worse
- Reach a Communications Console (generally in the Bridge) and call in another, more dangerous antagonist
- Bomb a given location, destroying infrastructure
- Reach a Criminal Records computer (mostly in restricted Security & Sec Outposts areas) and sabotage the records data
- Survive

Since the Ninja's objectives are not intrinsically tied to the round ending, some objectives should include failsafes so the Ninja can't simply wait until the end of the round (when the station is empty due to Evacuation) to complete them. Examples of this could include an objective that locks out access once Evac arrives (e.g., the R&D server claims the tech has been uploaded to a remote server). 

## Game Design Rationale

The Space Ninja is meant to fill a role as a medium-impact antagonist focused on station sabotage, with elements of elusiveness rather than the direct confrontation that is often seen with other midround antagonists. It should test the player's ability to disorient the crew, plan attacks, and navigate through the station in ways that make pinning them down difficult. 

The Space Ninja should be the apex 1v1 combatant, but drop off *heavily* in effectiveness if up against more than one foe. This gives the crew a straightforward way to counter the Ninja by grouping up, but it has inherent downsides that slow down crew and make it harder to defend multiple locations. Additionally, the Ninja should encourage an ambush-heavy playstyle. To accomplish this, the Ninja should not have high resistances (making advancing on an aware target more punishing), and instead focus should be put on abilities that let it get the drop on people.

While the Space Ninja should promote ambush tactics, which necessitates a stealth element to the role, it's important to make the distinction that the Space Ninja is *not a "stealth antagonist"*. While the station should not be notified the moment a Ninja appears, achieving objectives should still involve overt actions that signal to the crew that a Space Ninja is on the station. This allows the role to make an impact through existence as the crew gets a chance to apply countermeasures (e.g., raising alert levels, arming for weapons, preparing for ambushes). Unlike other stealth antagonists that avoid detection through hiding in plain sight (e.g., Traitors, Revolutionaries, Changelings), the Ninja aims to simply avoid hostile forces altogether. The goal of an ambush should be to gain some equipment and/or disable an opponent to complete an objective or escape danger. 

Since the Space Ninja focuses on ambushes and avoidance, it is important to balance the role such that the tools meant to enable those tactics can't also be used for undesirable gameplay. Often, a move that disables an opponent can make it trivially easy to kill them as well, and tools that make it easier to escape dangerous situations can also make it easier to initiate combat scenarios. Crew should also feel that there are sufficient counterplay tactics against a Space Ninja that do not just result in a status quo. If a Ninja gets into a disadvantageous position, the avoidance mechanics should not be so strong as to prevent any consequence for misplay. The Space Ninja should not encourage lethal gameplay, but some lethality is still desired to some degree to make them an imposing antagonist, to let the Ninja deal with opponents that can't be ambushed/stunned, and to dispatch single targets within an objective area. Careful attention needs to be paid to how this lethality is implemented to avoid encouraging Ninjas to use its kit to become a "maints slasher" that murders lone crew indiscriminately.

### Design Pillars

At its core, the Space Ninja should aim to follow these design pillars:
- Feel badass, cool, and sleek to control, fairly easy to pick up and play.
- Favoring ambushes and 1v1 confrontations; when up against multiple strong opponents, the ninja should prefer escaping.
- Feel like a legitimate threat the station needs to deal with, with focus on station sabotage and disruption rather than mass lethality.
- Strong at the outset; the ninja should not need to scale in power to be effective, though some improvements can be made via station equipment and accesses.
- Counterable via teamwork and predicting where the ninja will move, forcing them into disadvantageous confrontations.

## Roundflow & Player Interaction

As a midround antagonist, the Space Ninja is the most effective once the round has progressed a bit. This allows the Ninja to counteract progress that has been made in the round, lets the crew settle in a bit and makes it possible to utilize some pre-existing chaos. 

Once the Ninja has completed its objectives, since it doesn't rely on station destruction (Nukies, Space Dragon, Zombies) or integrating into crew to evacuate to CentComm safely (Traitors, Thieves), the Ninja requires some alternate end condition. While a Ninja is disruptive, it should not on its own be enough to cause the station to evacuate and thus end the round (though crew may opt to do so anyway). This document does not propose what the alternate end condition is, though a continuous objective beyond "Survive" or a way to (optionally) exit the round once all objectives are finished are possible options. 

The crew is able to know what objectives a ninja can have, but this does mean the ninja can be susceptible to being ambushed themselves by crew, or if there's no other chaos going on crew are able to lock down areas heavily. To prevent this, the ninja should have some randomness in their objectives, so that crew can't reliably know the ninja will show up in specific locations.

## Administrative & Server Rule Impact (if applicable)

The main concern with the Space Ninja is the risk of using its abilities to cause more death than is desired for the role. Mechanics should be balanced such that the Ninja is discouraged from using its abilities to directly cause death and round removal of other players. 

## Technical Considerations

Since the Space Ninja is already implemented in the game and isn't a technically complex antagonist, technical considerations are not necessary.
