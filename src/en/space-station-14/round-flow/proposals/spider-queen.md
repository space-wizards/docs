# Spider Queen

| Designers | Implemented | GitHub Links |
|------------|-------------|--------------|
| Shaddap1 | :x: No | [Design Doc PR](https://github.com/space-wizards/docs/pull/533) |

## Overview
A mid-round ghost-role major antagonist focused on stealth, ambush, brood expansion, and territorial control. The Spider Queen survives and grows by feeding, weaving webs, cocooning victims, spawning broodlings, and upgrading a wide range of mechanics. Crew counterplay centers on teamwork and environmental control.  I believe this design sticks to the central theme of a spider queen while operationalizing the best mechanics and attributes of other similar antagonists such as the Rat King and Dragon, and provides a new and interesting antagonist that will contribute meaningfully to roundflow.

## Background
The Spider Queen is inspired by a mix of xenomorph, dragon, and rat king. The design prioritizes stealth, strategy, and slow escalation rather than immediate overt crisis.  It is designed to be a sister-antag to the Rat King while featuring a more comprehensive scope and more diverse mechanics and playstyles.

## Features to be added
- Two new Team Antagonists, the Spider Queen and Broodling.
- Spider Queen abiltiies and mechanics
### Core Loop
- The Spider Queen expands upon the existing spider infestation event. When the event triggers, there is a 25% chance that a Queen will spawn alongside ordinary spiders, similar to Rat Kings. Optionally, it could be called in by Spider-Clan ninjas when they hack the comms console.
- Feed on animal protein (mice, roaches, pets, crew) to gain **biomass**.
- Use biomass to produce **webbing** and **venom**, which drain biomass passively over time.
- Weave webs and cocoon victims to store food and expand territory.
- Feed on cocoons 2–3 times for biomass recovery.
- Lay **broodling eggs** or upgraded **egg-sacs** (1 or 3 broodlings respectively).
- Form hunting parties with broodlings to ambush isolated crew.
- Can lay one expensive **Queen Egg**; if killed, this becomes a ghost-role spawn for a successor Spider Queen after a 30-second incubation delay if the egg is not destroyed.

### Broodlings
- Hatch from eggs after a short delay.
- Defensive AI near Queen; aggressive toward crew.
- Default AI similar to space carp but rat servant style commands could be implemented.
- Ghost-role eligible, using the standard raffle system similar to dragon carp.
- Broodlings are tankier and faster than space carp. A single crewmember can handle one, but a swarm requires a coordinated response.

### Resources, Abilities, and Upgrades

**Resources**
- **Biomass** – primary resource; gained from feeding.
- **Webbing** – converted from biomass; used for webs and cocoons.
- **Venom** – converted from biomass; fuels venomous bites.

**Queen Starting Abilities**
- *Weave Webs*: Toggle; movement slowed, webs placed per tile; costs webbing. Biomass is not drained to replenish webbing while toggled off.
- *Venom*: Toggle; bites inject venom; costs venom. Biomass is not drained to replenish venom while toggled off.
- *Cocoon Target*: Do-after; wraps downed targets in a thick cocoon.
- *Lay Egg / Egg-Sac*: Eggs hatch broodlings after an incubation delay.
- *Feed on Cocoon*: Long do-after; yields extra biomass from cocooned victim and incentivizes the Queen to not gib players.
- *Pry Door* and *Pull Mob*: Basic mobility and victim relocation (upgradable).

**Queen Upgrades**
- **Web Mutations** *(mutually exclusive)*  
  - *Nanofilament Webbing*: Lower opacity, harder to see.  
  - *Glycoprotein Recombination*: 10% chance to stick blunt/slash weapons, requiring them to be pulled out like knives thrown into walls.  
  - *Keratin Composite Filament*: Web traversal inflicts pierce/slash damage like flesh kudzu.  
- **Venom Mutations** *(mutually exclusive)*  
  - *Caustic Glands*: Adds caustic damage.  
  - *Aphasia Toxin*: Temporarily mutes victims.  
  - *Virulent Neurotoxin*: Slows and briefly sleeps targets.  
- **Other Upgrades**  
  - *Egg-Sacs*: Eggs spawn 3 broodlings.  
  - *Hunting Pounce*: Leap to target; stam-crit and disarm on hit. Long cooldown.  Similar to vulpakin pounce.  
  - *Insulated Carapace*: Immune to electric shock. Essential for AI counterplay. Allows Queen to bite and break LV, MV, and HV cables.  
  - *Armored Carapace*: Increases brute resistance.  
  - *Chromatophores*: Camouflage or invisibility while stationary.  Custom shader would be dope.  
  - *Enhanced Photoreceptors*: Night vision (planned system).  
  - *Enhanced Hydraulics*: Faster door pry and mob pulling.  
  - *Mass Scaling (Passive)*: Biomass spent increases Queen size (Small/Medium/Large), affecting sprite size, speed, and noise. Small queens move silently and can hide under tables. Larger Queens are louder and slower but tougher.

### Resource Economy and Management
- **Biomass**: Gained from animal kills; consumed by webbing and upgrades.  
- **Webbing**: Regenerates by draining biomass; capped (~30 tiles).  
- **Venom**: Regenerates by draining biomass; capped (~100).  

**Placeholder Values**
- Biomass cap: 100  
  - Mouse/Roach: +10  
  - Pet: +20  
  - Cocoon Feed: +50  
  - Ruptured Egg: +5  
- Web cost: 1 tile (2 for low-opacity, 3 sticky, 4 thorny).  
- Web regen: Every 3s → 2 biomass → +1 tile.  
- Egg: 20 biomass; Egg-Sac: 40; Queen Egg: 90.  
- Venom Bite: Normal 1/5 pool, Caustic/Mute 1/4, Paralytic 1/2.  
- Venom regen: 5 biomass → +20% of pool.  

All values are preliminary and will require testing.

## Round resolution
Crew victory occurs when all Spider Queens and eggs are destroyed.  
Queen success is measured by survival and brood strength.  
The end-round summary lists brood size, whether a Queen Egg was laid, and survival.

## Game Design Rationale
The Spider Queen adheres to SS14’s core design principles:
- **Chaos**: Webs, cocoons, and brood interactions create unpredictable situations.  
- **Seriously Silly**: Combines horror tension with getting to watch the clown being devoured by spiders.
- **Dynamic Environment**: Webs and nests alter station condition.
- **Player Interaction**: Encourages multi-department cooperation (Security, Engineering, Medical).  
- **Player Agency**: Crew and Queen both retain counterplay choices, Queen gameplay requires extensive decision making, resource management, strategy, and skill expression.

The design ensures escalation over time, promotes teamwork, and avoids “guaranteed chaos” by relying on player decisions rather than overly impactful abilities.   

## Roundflow & Player Interaction
**Early** – Hide, feed, and establish the first nest.  
**Mid** – Hatch broodlings, expand territory, hunt, and purchase 1–2 upgrades.  
**Late** – Multiple nests, large brood, several upgrades, Queen Egg laid, crew freaking out.  

Departments involved:  
- **Engineering**: Burns webs with welders, rebuilds maintenance.  
- **Security**: Engages broodlings and Queens, escorts engineers.  
- **Medical**: Treats toxins and rescues crew from cocoons.
- **All Crew**: Potential snacks

- A typical round might look like this:
  - Spider queen spawns at around 20 minutes in
  - Early phase
  - Keeps to maints, trying to avoid detection from crew.  Tries to find an isolated and infrequently visited section of maintenance.
  - Runs into a crewmember, should be able to crit them provided they are not well armed.
  - Drags them to a safe location, webs them up in a cocoon, and feeds.
  - Buys an upgrade, lays a few eggs, and weaves some webbing to protect them.
  - A paramedic comes looking for the dead crew member at the behest of AI
  - Spider Queen smartly hides, waiting for the paramedic to try to free the crew member from the cocoon or attack the eggs.  Lays webbing at escape routes before ambushing paramedic.
  - Cocoons paramedic, but is likely outed on radio first.  Broodlings hatch.  Spider Queen quickly feeds on paramedic and departs for a new section of maintenance to hatch more broodlings
  - Queen is well protected/upgraded enough to abduct station pets or unarmed crew members for additional biomass and upgrades.
  - Mid phase
  - Sec is actively searching for the Spider Queen
  - Spider Queen balances staying mobile enough to evade direct confrontation with finding biomass sources, creating nests, hatching more broodlings, and buying upgrades
  - Now strong enough to raid unprotected departments and flee back to maintenance
  - Late phase
  - Most of the crew is aware and responsive to the Spider Queen threat.  Easy victims are difficult to find.  Confrontation is necessary.
  - Spider Queen assaults the medbay with her brood, seeking to drag victims into maintainance and leave her brood and webbing behind to fight and delay pursuit.
  - Sec responds and dies and/or succeeds in dealing critical damage to the Queen
  - The Spider Queen escapes with a victim, bleeding, with death immminent in the next few minutes
  - She quickly cocoons her prey, feeds, and flees a bit further to lay a hidden Queen Egg.
  - The Queen moves across the station, far away from the egg, to draw security away.
  - The Queen is tracked down and killed, but the Queen Egg begins to hatch.
  - The threat is lowered, but the station is still armed, and security will be searching maintenance for any more eggs and broodlings
  - The new Spider Queen hatches and begins the process from the beginning, with the added threat of additional armed security patrols and more cautious victims
  - She manages to feed from a few left over corpses and raises a small army but is found by security and killed.
  - During the chaos of the past 20-40 minutes, syndicate agents, thieves, and other antagonists may have taken advantage of the chaos to accomplish their objectives.
  - The disruption caused by the Spider Queen was major but not round-ending, demanding a coordinated crew response to resolve the crisis.

Queens should rely on stealth and selective combat. They should not be able to solo a squad of security officers.

## Administrative & Server Rule Impact (if applicable)
- Goal is survival and expansion, not griefing.  
- Prohibited: round-ending sabotage (singulo/tesla releases, mass plasma fires).  
- Ghost roles use the standard raffle. A successor Queen should ideally go to a different player.  
- Playtime requirement recommended due to mechanical complexity.

## List of Sprites
- **Spider Queen:**
  - Small size 
    - Alive, crit, dead
  - Medium size 
    - Alive, crit, dead
  - Large size 
    - Alive, crit, dead
  - Probably needed eventually: Living animation for alive sprites
  - Optional: Visual changes to alive sprites for certain upgrades: armored carapace, insulated carapace, camoflauge, etc.
- **Broodling:**
  - Alive, crit, dead
  - Probably needed eventually: Living animation for alive sprites
- **Eggs:**
  - Broodling egg
    - Alive, ruptured, OPTIONAL: hatching animation?
  - Spider Queen egg
    - Alive, ruptured, OPTIONAL: hatching animation?
- **Webbing:**
  - Monofilament webbing: lower opacity, thinner strands (harder to see)
  - Sticky webbing: probably sort of goop visible on the web
  - Thorn webbing: Spikes or spines visible on the web
- **Icons:**
  - Action bar icons
  - Upgrade menu icons (can be same as action bar probably)
  - Biomass resource icon (can borrow from changeling?)
  - Webbing resource icon (can probably use existing spiderweb sprites, would be nice if it updated to purchased web upgrade)
  - Venom resource icon

# Technical Considerations
- **New Systems**: WebTypeComponent, CocoonComponent, BroodLeashSystem, ResourcePools, QueenEggIncubatorSystem, QueenActions.  
- **Reused Systems**: Spider content, knife-stick mechanic, flesh kudzu behavior, Vulpakin pounce.  
- **Performance**: Broodling cap may be required.  
- **UI**: Resource bars and simple upgrade menu (similar to uplink/grimoire).  
- **Sprites**: See above list
- **Audio**: Briefing audio, custom hisses/screeches, egg hatching noises.
- **Testing**: Extensive playtests needed for web burn behavior, biomass balance, and venom regeneration.
