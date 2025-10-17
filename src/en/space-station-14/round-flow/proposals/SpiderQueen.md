# Spider Queen

| Designers | Implemented | GitHub Links |
|------------|-------------|--------------|
| Shaddap1 | :x: No | TBD |

## Overview
A mid-round ghost-role antagonist focused on stealth, ambush, brood management, and territorial control. The Spider Queen survives and grows by feeding, weaving webs, cocooning victims, and spawning broodlings. Crew counterplay centers on teamwork, fire, and environmental control. The Spider Queen’s strength scales with biomass, web density, and brood coordination.

## Background
The Spider Queen expands upon the existing spider infestation event. When the event triggers, there is a 25% chance that a Queen will spawn alongside ordinary spiders. This evolution introduces a new mid-round ghost-role antagonist that turns the simple pest event into a large-scale infestation threat.

The Queen is inspired by a mix of xenomorph, horror-creature, and nest-building mechanics from SS13, but redesigned to suit SS14’s sandbox chaos, player agency, and emergent interactions. The design prioritizes stealth and slow escalation rather than immediate overt combat.

## Features to be added

### Core Loop
- Feed on animal protein (mice, roaches, pets, crew) to gain **biomass**.
- Use biomass to produce **webbing** and **venom**, which drain biomass passively over time.
- Weave webs and cocoon victims to store food and expand territory.
- Feed on cocoons 2–3 times for biomass recovery.
- Lay **broodling eggs** or upgraded **egg-sacs** (1 or 3 broodlings respectively).
- Form hunting parties with broodlings to ambush isolated crew.
- Can lay one **Queen Egg**; if killed, this becomes a ghost-role spawn for a successor after a 30-second incubation delay.

### Broodlings
- Hatch from eggs after a short delay.
- Defensive AI near Queen; aggressive toward crew.
- Default AI similar to space carp but can be replaced by servant-style leash AI.
- Ghost-role eligible, using the standard raffle system.
- Broodlings are tankier and faster than space carp. A single crewmember can handle one, but a swarm requires a coordinated response.

### Resources, Abilities, and Upgrades

**Resources**
- **Biomass** – primary resource; gained from feeding.
- **Webbing** – converted from biomass; used for webs and cocoons.
- **Venom** – converted from biomass; fuels venomous bites.

**Queen Starting Abilities**
- *Weave Webs*: Toggle; movement slowed, webs placed per tile; costs webbing.
- *Venom*: Toggle; bites inject venom; costs venom.
- *Cocoon Target*: Do-after; wraps downed targets.
- *Lay Egg / Egg-Sac*: Produces broodlings after a delay.
- *Feed on Cocoon*: Long do-after; yields biomass.
- *Pry Door* and *Pull Mob*: Basic mobility and crowd control (upgradable).

**Queen Upgrades**
- **Web Mutations** *(mutually exclusive)*  
  - *Nanofilament Webbing*: Lower opacity, harder to see.  
  - *Glycoprotein Recombination*: 10% chance to stick blunt/slash weapons.  
  - *Keratin Composite Filament*: Web traversal deals pierce/slash damage.  
- **Venom Mutations** *(mutually exclusive)*  
  - *Caustic Glands*: Adds burn damage.  
  - *Aphasia Toxin*: Temporarily mutes victims.  
  - *Virulent Myotoxin*: Slows and briefly sleeps targets.  
- **Other Upgrades**  
  - *Egg-Sacs*: Eggs spawn 3 broodlings.  
  - *Hunting Pounce*: Leap to target; stam-crit and disarm on hit.  
  - *Insulated Carapace*: Immune to electric shock.  
  - *Armored Carapace*: Increases brute resistance.  
  - *Chromatophores*: Camouflage or invisibility while stationary.  
  - *Enhanced Photoreceptors*: Night vision (planned system).  
  - *Enhanced Hydraulics*: Faster door pry and mob pulling.  
  - *Mass Scaling (Passive)*: Biomass spent increases Queen size (Small/Medium/Large), affecting sprite size, speed, and noise. Larger Queens are louder and slower but tougher.

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
- **Seriously Silly**: Combines horror tension with dark humor.  
- **Dynamic Environment**: Webs and nests alter station geography.  
- **Player Interaction**: Encourages multi-department cooperation (Security, Engineering, Medical).  
- **Player Agency**: Crew and Queen both retain counterplay choices.

The design ensures escalation over time, promotes teamwork, and avoids “guaranteed chaos” by relying on player decisions.  
Fire, coordination, and preparation remain strong counter-measures.

## Roundflow & Player Interaction
**Early** – Hide, feed, and establish the first nest.  
**Mid** – Hatch broodlings, expand territory, and purchase 1–2 upgrades.  
**Late** – Multiple nests, large brood, several upgrades, Queen Egg laid.  

Departments involved:  
- **Engineering**: Burns webs, rebuilds maintenance.  
- **Security**: Engages broodlings, escorts engineers.  
- **Medical**: Treats toxins and rescues cocoons.  
- **Cargo**: Supplies tools and welders for operations.  

Queens should rely on stealth and selective combat. Direct confrontation with armed Security is discouraged.

## Administrative & Server Rule Impact (if applicable)
- Queens must act strategically, not suicidally.  
- Goal is survival and expansion, not griefing.  
- Prohibited: round-ending sabotage (singulo/tesla releases, mass plasma fires).  
- Ghost roles use the standard raffle. A successor Queen should ideally go to a different player.  
- Playtime or experience requirement recommended due to mechanical complexity.

# Technical Considerations
- **New Systems**: WebTypeComponent, CocoonComponent, BroodLeashSystem, ResourcePools, QueenEggIncubatorSystem, QueenActions.  
- **Reused Systems**: Spider content, knife-stick mechanic, flesh kudzu behavior, Vulpakin pounce.  
- **Performance**: Broodling cap may be required.  
- **UI**: Resource bars and simple upgrade menu (similar to uplink/grimoire).  
- **Sprites and Audio**: Animated Queen sizes, broodlings, webs, and action SFX.  
- **Testing**: Extensive playtests needed for web burn behavior, biomass balance, and venom regeneration.
