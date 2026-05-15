# Zombies Game Mode

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| ketufaispikinut (sword_cat on discord), others (todo: put their names here) | idem | :x: No | TBD |

## Overview

The humble zombie is a round start antagonist focused on infecting the station, slowly but surely. The crew should struggle against the infected horde; it should be an experience of strained survival as the whole station collapses under the zombie apocalypse. Zombie antags should almost always cause evacuation away from a now-unlivable station.

## Background

We currently have zombies on Wizden, most downstreams have zombies and a lot of SS13 servers had some sort of implementation of zombies. This game mode has received mostly good player feedback and is rather well liked, but still lacks a design doc, and has some rough edges. This document seeks to describe how zombies should develop in the future: a zombie round should reverse the usual hunter-hunted relationship of antagonists and crew members as the last survivors desperately try to fend off the infected in the best zombie horror movie fashion.

## Features

At the beginning of a Zombies round, the infection will be spread to a few random patients zeroes. It should then slowly spread, disrupting station activities, until the remaining survivors must go into hiding, build barricades and arm themselves: the station shouldn’t be able to easily ignore the zombie virus.

The infection spreads through exchange of bodily fluids; of course, this means that infected individuals will pass on the infection through bites (as it should be and is in most zombie media). Due to how combat works in SS14, having a bite infect a player 100% of the time would feel rather bad: despite zombies infecting on bites, the crew should still be somewhat able (either trough protection or luck) to fend of zombies using melee weapons.

Once infected, players will be granted a relatively short grace period before displaying symptoms (we should maybe wait for some sort of virology before introducing visible symptoms) and eventually turning. It should be possible for crew members to tell infected-but-not-zombified-yet individuals from sane crew members. The infection should zombify fast enough as for it to be an actual danger during a round.

Upon turning, players lose basic abilities such as talking and operating machinery. They pretty much get reduced to biting machines who must now roam the halls of the station to infect more individuals.

Newly-infected zombies should still be entertained by the game; we don’t want them ghosting. We should thus introduce classic zombie games tropes such as:
 - Mutant zombies (fast, pouncer, brute, etc) each with their strengths and weaknesses (brute zombies are way stronger but can’t infect living individuals, fast zombies are extremely weak to brute, etc). Zombies should still work better in hordes, though. We don’t want a magic invincible berserker zombie that can run through crowds of survivors and murder & infect them all. Each mutation should be designed to either assist other zombies or to work well in hordes.
 - Survivor detection / pinpointer ability to detect remaining survivors when only a few are left. Stragglers hiding in lockers or in secluded areas should not be safe from the infected. Having each and every (player-controlled) zombie suddenly home in on the remaining survivors would be absolutely terrifying.

One way to implement mutations would be trough giving different initial infected different strains of the virus; this would encourage all initial infected to infect the most individuals possible instead of having only one II turn and the other sabotage the station while quaffing dylovene (initial infected should *not* be able to stay unturned for the whole shift, so if this is not enough, then the poison damage from the infection could massively ramp up trough time).

Another way for mutations to function would have them be completely random, and more common as the infection advances. Zombies could get a random mutation after a certain amount of time alive, with it being faster & less rare when more are infected.

Zombies should also get new objectives to reflect their goals as an ever-expanding apocalyptic force, those mainly being zombies winning once Central Command becomes infected.

The zombie’s objectives should pressure the crew to try to maintain a safe zone (another zombie trope) around Evac, and make zombies try to confront the remaining survivors there.

Finally, to mirror events such as the end of the game *Death Road to Canada*, military reinforcements (e.g. CBURN) should be dispatched to prevent the infected from reaching the rest of the world (Evac) and provide support to the struggling crew members who made it this far. These ghost roles will also provide entertainment for round-removed players.

## Game Design Rationale

The zombie is the conversion antagonist by excellence; where Nuclear Operatives destroy the station trough infiltration, zombies come from the station itself yet prove to be a threat on the same level (if not more dangerous) as the Operatives. It should challenge the player’s ability to balance between hiding, traversing an infected station without being caught, salvaging armor and weapons and working in a small team to fight against a way bigger undead force.

While revolutionaries are simply replacing the station’s leadership, zombies represent the total collapse of any central organization as most become infected.

A singular zombie should almost always be no match for an armed crew member in one-on-one combat; zombies should have their victory in combat through either horde power or via infecting crew members, and then having them eventually turn after the fight has concluded.

The infection shouldn’t be easily curable, and existing cures should not be too potent: players shouldn’t be able to become fully immune trough medicine (looking at you, ambuzol+) alone, they should need to either return to medbay to get cured or do treatments of dubious quality (when discomed arrives, removing limbs should prevent the spread of the infection). This should foster players trying to salvage better armor from the station (such as bio suit, coats, etc).

## Roundflow & Player interaction

### Early game

On a normal zombie round (one that is not caused by nuclear operative intervention), a few players should be picked as Initial Infecteds. These patients zeroes start as regular crew members, infected yet asymptomatic. As the round moves forward, they will slowly (slower than normal infected crewmembers) begin to show symptoms before fully turning. Unlike normal zombies, Initial Infecteds should still retain basic abilities (such as garbled speech) to designate themselves as natural zombie leaders.

While in their grace period, initial infected players *could* have methods to infect other players. These methods shouldn’t feel random to infected crew members (we don’t want a random infection chance when near the II, for instance). Finding proper ways for the IIs to spread the infection "naturally » would probably be really hard though.

Initial Infecteds will be encouraged to sabotage the station as to make it easier for them to infect as many as possible and make it harder for the crew to resist. IIs should however *not* be able to stave off the infection forever. They should always eventually turn, and, of course, be immune to any cure to the virus.

### Going into hiding

Zombies should slowly kick in until they eventually overtake the station. Survivor players should then be encouraged to hide, build bases or try to maintain safe zones while trying to equip or assemble a cure as fast as possible, playing a game of deadly hide-and-seek with those playing as the zombie horde. 

The crew could thus build a somewhat zombie-proof zone through things like electrical fences, grids, barricades, etc. Of course, no area should ever be 100% safe from the horde. 

As mentioned before, zombies should also have *some* way to locate survivors when only a few stragglers are left alive; we don’t want them to wander aimlessly trough the station’s halls; while this makes sense from an external point of view, playing as a zombie without someone to bite is extremely boring and thus this should be avoided. They could thus get an innate nukeops-like pointer, basic directions toward survivors, "leader » zombies or something similar.

In general, zombies should get stronger and stronger the more the round advances, to prevent endless stalling by the crew. Mutations should be more common, stronger, zombies should do more damage or the infection could have a shorter incubation period. Of course, this should be balanced around the remaining number of cremwates vs the size of the infected horde. Think of it as rubber banding to constantly keep the round fun for both the zombies and the uninfected.

Crew members should look for armor & clothes such as riot armor, biologic suits, winter coats, etc: with enough protection, you should be virtually immune to basic bite infections. You should be able to defend yourself from one zombie with a baseball bat and proper clothing without always getting infected.

There should be some ways for crew members to know if another is infected or not; be it trough description symptoms (such as the character looking feverish) or random coughing, having someone on your team suddenly display those symptoms should give pressure the crew and make it so the zombie virus isn’t just a sudden transformation into a mean green biting machine with little to no symptoms beyond damage.

### Last stand

Once a certain percentage of station staff is infected, an evacuation shuttle should be automatically called and the round should devolve into a mad rush to secure evac, as both the crew and the infected horde need to make it to central command. This is where the round should climax, as every soul, living or not, on the station tries to make it on the shuttle.

To ensure no one hides behind and to reinforce the "last stand" vibe, the escape pods could be disabled or made harder to access.

At this point, a CBURN squad could be automatically dispatched by centcomm to defend the evacuation shuttle. This would have two benefits: 

 - It would provide interesting ghost roles for the many players who will get round-removed on zombie rounds (think of the poor zombified Pun Pun stuck in space, far from everyone, or the numerous zombies killed with no chance of ever being revived).
 - The military trying to sort infected individuals from those still healthy would make for great RP occasions (trying to hide the symptoms of the zombie virus as a simple fever, etc).

### In other game modes

As for the nuclear operative’s romerol bundle, it simply needs to work like a real zombie game mode - it plays fairly well in the zombie apocalypse theme, since a frequent trope of this genra is biological warfare / semi-intentional medical disasters and nukies are pretty much doing exactly that. 

## Administrative & Server Rule Impact (if applicable)

None, I hope :)

# Technical Considerations
- Mutations, if any, will be a pain to implement.
- Other features should be relatively easy to implement, or at worst just tedious (such as going around and rebalancing infection rates).