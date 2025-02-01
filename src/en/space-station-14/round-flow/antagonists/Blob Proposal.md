# Blob Proposal

| Designers | Implemented | GitHub Links |
|---|---|---|
| TiniestShark | :x: No | TBD |

## Overview

The Blob is a Major Conversion Antagonist with the goal of replicating and evolving until it can ultimately consume the station. A strange biohazardous organism that arrived on the station through the infestation of vermin, or a meteor impact carrying its core, the Blob is a Round start antagonist that must find a safe place to establish its core and expand. 

This is an intended re-imagining of the original Blob to better support a more interesting style of play both for the crew of the station and the Blob itself. The Blob is no longer simply spreading, but evolving in its quest to perfect itself and consume the galaxy.

This is a condensed version of the main doc found here as I try to condense and focus this down (Although the original doc has much more ADHD rambling on my thought process if needed): https://docs.google.com/document/d/1JTyuuHHEphncsvq3ubqJ9hwMzDlBHUfSY0dehHIBRww/edit?usp=sharing

### Gameplay Loop

The Blob will begin the round as an infected Mouse or Mothroach and placed somewhere at random on the station alongside other roundstard vermin. From there the Blob has approximately five minutes to find an ideal location on the station to place its Core, its base building and the center of a Blob's infestation. The Blob from this point assumes the POV of a free floating camera/cursor similar to the Station's AI with its vision based on the sight range of its Blob Tiles and Units. The Core will begin to slowly create Blob Tiles around itself while The Blob will begin to place Blob tiles manually, using resources for each one placed, to expand itself outward. If the Blob clicks on an occupied tile, the surrounding Blob will attack whatever is in the tile if it is not able to spread into it, beating down walls to open the area up.

If the Core is destroyed: The Blob loses the round and Evac will be called allowing the crew to leave. As well: all Blob tiles, units, and buildings will begin to degrade in health until they die.

The Blob starts with a pool of resources it spends in order to place Blob tiles, build buildings, and spawn units. It has a maximum initial storage of 100 resources, and can expand this reservoir with Storage Blobs. The Core creates its own resources passively but this can be increased by building Resource Blobs, which generate 1 resource with each 'pulse' of a Core or Node. The Blob must also start placing Nodes to solidify it's influence over an area. It will then research upgrades that boost its base stats and spreading potential until it can achieve its final evolution, while also working to fight off the crew when its inevitably discovered.

After the Blob has been confirmed on station: the Emergency Shuttle will be unable to be called. If the shuttle has already arrived: It will be unable to leave. Only Escape Pods will be launched if the Blob wins. (Though if necessary the shift change Evac can come as normal as an emergency evac that will spawn off station)

In order to win, the Blob must research four tiers of "Evolution", which it reaches through putting down a certain number of nodes and then spending the amount of resources needed to research the upgrade.

### Abilities

The Blob has a number of basic controls and abilities to make their job of spreading and consuming much easier.

- **Spread** *(Left Click)*: Clicking on a tile spreads Blob to selected tile. Tile must be connected to existing Blob. Each placed tile takes resources based on type. Can be placed under Crew.
- **Attack** *(Right Click)*: Attacks selected entity with nearest Blob tiles.
- **Delete Blob** *(Alt Click)*: Allows Blob to delete misplaced or unnecessary Blob tiles or Buildings for a small refund (40%) (Weak tiles are not refunded).
- **Core Relocate**: Available until Anaphase: Allows Blob core to swap its position with a target node. Replaced with...
- **Split Consciousness**: Replaces Relocate during Anaphase. Blob spends 100 resources to turn target node into a new Core. The new Core will be an open ghost role and will assist the Blob in taking control of the station. Both Blobs share a resource pool, evolve together, and command the same units. Secondary Blob can be a different variant than the first.
- **Rally Neaby Units** *(Shift + Middle Mouse Click)*: Commands all Nearby Units to move towards target location. Units will attack anything in area or in path. Acts as a "Point" command for Ghost controlled Units. Functions as 'soft' control groups rather than moving all Units the Blob owns at once.
- **Detonate Spore** *(Q)*: Commands selected Spore to manually explode (Spores will be highlighted while Alt is held so the Blob can easily see which one its targeting). Exploded Spores deal damage in a radius around them and spread Weak Blob. Also works on Blob Zombies so the Blob can stop griefers if needed.
- **Mutate Blobbernaut** *(X)*: Choose target factory to spawn a Blobbernaut. Selected factory is damaged in the process. Costs 80 resources. Only available after Metaphase.
- **Upgrade Blob** *(Ctrl + Click)*: Click on a Blob tile to upgrade it to a Strong Blob Tile. Click again to upgrade it to a Reflective Tile.
- **Swap Blob** *(Left Click)*: Changes Strong Blob Tile to Bloblock. Has a short doafter to prevent spamming.
- **Evolve** *(V)*: Upgrades Blob to next tier of Evolution. Each Evolution takes time to complete.
- **Jump to Node** *(Numpad 7 + 9)*: Quickly moves the Camera to the next or previous Node in sequence.
- **Jump to Core** *(Numpad 8)*: Quickly moves the Camera to the Blob's Core.
- **Grapple** *(Z)*: Commands the nearest Blob Grapple to latch onto a target entity. Using again on the same tower releases.

### Blob Tiles

Blob Tiles are the Blob's primary method of spreading throughout the station. Each tile costs a small amount of resources, allowing a Blob to either slowly spread out by spending their resources constantly, or saving up for a rush of Blob. Blob Tiles are capable of attacking, dealing damage depending both on the type of tile and the strain of the Blob. Blob Tiles can be destroyed by the crew through damaging them with any weapons on hand.

- **Normal Blob** | *Cost: 5 | Health: 30*: Main tile of the Blob. Spreads influence outwards, allows buildings to be placed down, and passively damages mobs that walk onto it. Entities that walk onto Blob Tiles are slowed by 30%. Degrades into Weak Blob if outside the influence of a Node/Core. Will attack nearby mobs when pulsed by a Core/Node
- **Weak Blob** | *Cost: 2 | Health: 15*: If the Blob attempts to spread outside the influence of a Node/Core, they will only spread Weak Blob at a reduced cost. Weak Blob has half health and damage of a regular Blob Tile, and only slows by 15%. Buildings can still be placed on Weak Blob. Also deals damage to mobs standing on top of it.
- **Strong Blob** | *Cost: 8 | Health: 250*: Upgraded from Normal Blob. Strong Blob Tiles are solid walls that can take much more damage before being destroyed. Fireproof and block air flow in the event of station fires.
- **Reflective Blob** | *Cost: 8 | Health: 150*: Upgraded from Strong Blob. Reflective Blob Tiles are solid like Strong Blob, but have less health. In exchange: They are able to reflect laser shots from the crew (90% Reflect Chance).
- **Blob Locks/Membrane** | *Cost: 0 | Health: 250*: Variant of Strong Blob. Blob Locks/Membrane are doors the Blob can establish to fortify an area, while still letting their units through. Useful for chokepoints, and for letting units into space.

### Blob Buildings

Blob Buildings are what the Blob must use to gather strength and fight the station. All buildings aside from the Core must be built on Blob Tiles. Any buildings within the influence radius of a Node/Core will regenerate health over time, and lose it slowly when not.

- **Core** | *Health: 400* : The brain of the Blob. Generates 1 resource a second on its own while pulsing nearby buildings every 10 seconds. Supports buildings in its influence radius. If destroyed: The Blob loses.
- **Node** | *Cost: 60 | Health: 200*: The nerves of the Blob. Spreads Blob around itself automatically and supports buildings in its influence radius. Blobs around node attack automatically and will take out any non-blob walls around it. Additionally restores any Weak Blob in its radius to Normal Blob. Nodes are the major signifiers of Blob Presence and required both to hold its territory down, and also to evolve. Cannot be built within four tiles of the Core or another Node. Pulses nearby buildings at the same rate as Core.
- **Resource Pool** | *Cost: 40 | Health: 60*: Produces resources over time (1 every four seconds). Cannot be built within three tiles of another Resource Pool. Generates 1 extra resource when pulsed.
- **Spore Factory** | *Cost: 50 | Health: 200*: Creates Blob Spores over time with a cap of three per factory. Takes five resources per Spore at a rate of seven seconds taken for each spore. Cannot be built within four tiles of another Spore Factory. Creates a Spore when pulsed up to building cap.
- **Storage Blob** | *Cost: 40 | Health: 30*: Increases max resource capacity by 50. Cannot be built within three tiles of another Storage Blob. If a Storage Blob is destroyed: The Blob's resources will tick down to its new cap if it is above its current cap rather than being lost all at once. Maximum storage is 300 resources.
- **Spore Cannon** | *Cost: 80 | Health: 300 | Damage: 2*: A support tower that fires fast, weak blob projectiles at enemies. Slows targets with a stacking speed debuff (15% with each hit, stacks with Blob's natural slowdown. Total speed debuff capped at 90%) as they're covered in Blob. Functions to dissuade lone attackers from assaulting Nodes or specific locations, and assists in harassing combatants attempting to outrange the Blob. Fires an extra bolt when pulsed. *Unlocked during Prophase*
- **Blob Grapple** | *Cost: 60 | Health: 200 | Damage: 1*: A support tower that fires a Blob tendril that grapples onto the first thing it hits and prevents it from moving (Can hit Walls, Entities, or Mobs). Grapples can travel through Strong Blob. Blob can spread Blob Tiles from point of grapple's impact. Intended to give Blobs a way to spread back onto the station if they're disconnected for any reason, or to grab and hold down Shuttles for its units to attack and overtake. Grapples can be destroyed by Crew. Spreads Blob at grapple point when pulsed.

### Pulsing

A "Pulse" is a radial signal the Blob emits every ten seconds minimum with a maximum life span of thirty seconds. The Core and the Blob's Nodes will emit a pulse that radiates outward to the edge of its area of influence, or its current spread of Blob. The pulse expands outward from the Core/Node at a rate of one tile a second and activates an effect on every building it hits. Pulsing is also how a blob heals itself and its buildings while expanding its Blob passively. Pulsing will also upgrade Weak Blob to Regular Blob in the Blob's radius.

Pulsing can trigger a Building's effects outside of their normal rotation, with the primary beneficiary being its resource pools. The closer the building to a Core/Node, the sooner and more frequently it gets pulsed. If the Pulse reaches a tile the Blob has not spread onto, it will spread onto it. The Blob can only spread one to two tiles outward per pulse, per Core/Node. As the game goes on and the Blob's territory grows larger, pulses will take longer to reach the edge of its area of influence, making the delay between new pulses longer and providing less benefit over time to the Blob, forcing it to rely more on its constructed economy.

A Core/Node that has reached its maximum range of influence will only expand one tile outward of Weak Blob with every Pulse if there is no other Blob to place/replace.

### Unique Buildings

Unique Buildings are specific structures that are created when the Blob consumes specific station objects or machines. These are mainly to highlight what the Blob has taken from the crew and to clearly show the crew where the objects have gone.

- **Captured Nuke** | *Health: 100*: If the Blob manages to spread onto a Nuke, it creates a Captured Nuke. This is a reinforced Blob tile that prevents the Crew from arming the Nuke. When destroyed, the Nuke is freed and able to be armed by the Crew once again.

### Units

While the Blob is able to fight directly through its tiles, it has access to a roster of Units it can create to assist in reinforcing its position, pushing into new territory, or simply harassing the Crew.

- **Spore** | *Cost: 5 | Health: 40 | Damage: 4 (25 Structure)*: Low Tier Unit. Floats through air, attacks weakly, and explodes when killed. Can drift through space without being harmed. Spread Weak Blob in a radius around them when they explode, and can be commanded to explode manually. Also function as Ghost Roles for Players to take. Cannot be exploded manually by Ghost players. (AI should attempt to mob players rather than kite to ensure they blob crew when they die)
- **Blob Zombie "Blombie"** | *Cost: 1 Crew | Health: 60 | Damage: 15*: Medium Tier Unit. Created when a Spore takes over a dead crew member (5 second Doafter). Controlled by downed Player, or by AI if the player has disconnected or taken another role. Acts as a regular mob, chasing down Crew and attacking when AI. Has resistances from armor crew member was wearing. Spores on head "pop" when killed, allowing Crew's body to be retrieved and revived. Blob Zombies cannot harm the Blob.
- **Blobbernaut** | *Cost: 80 | Health: 300 | Damage: 40 (80 Structure)*: High Tier Unit. Expensive, powerful bruiser. Attacks deal heavy Blunt damage with additional damage based on Blob Strain. Blobbernauts have a low attack speed to emphasize their bruiser role, and leaves them open to being swarmed if not supported by other units. Regenerates health steadily while on Blob Tile, halved on Weak Blob. Ghost role for Players, AI if uncontrolled. If a Blobbernaut's factory is destroyed, they begin to decay steadily until they die. Immune to pressure/temp changes, but has trouble maneuvering in zero gravity.

### Damage Resistances

- **Blunt/Brute**: The Blob is a solid mass of matter, making most blunt weaponry deal little damage.
- **Cold**: The Blob has adapted to survive in space, making it resistant to low pressure environments/cold temperatures.
- **Piercing**: Due to the Blob's strange composition; bullets will either fly through it or pierce and deal little damage. Blob Units take normal damage from Pierce to not make guns useless.

### Damage Vulnerabilities

- **Slash**: Bladed weapons deal full damage against the Blob, giving the crew a clear avenue of damage if other sources are not readily available.
- **Fire**: The Blob's composition makes it vulnerable to Heat damage, meaning that Welders and Flamethrowers will deal additional damage to it alongside Laser based weaponry.
- **Structural**: The more concentrated the Blob is in an area, the more resistant it is to normal methods of attack, but the weaker it is to structural damage. Strong Blob and Buildings take additional Structure damage.

### Weapons against the Blob:

- **Laser Weapons**: The main dealers of Heat damage the crew has access to. Lasers will be useful all around weapons for fighting the Blob, just be wary of Reflective Blob.
- **Flashes**: Flashes will clear Weak Blob in a small radius around the user, and prevent Normal Blob from attacking momentarily so a crew may escape its clutches. Ideal defensive tool.
- **Flashbangs**: Flashbangs can be used to clear Weak Blob Tiles in a wide radius and weaken regular Blob tiles into Weak Blob, just warn other crew members before throwing! Does not affect Strong or Reflective Blob.
- **Flamethrowers**: Chemists can work with the crew to create Flamethrowers for use against the Blob. This will need to be done with caution so crew members don't just set each other on fire.
- **Shuttle Weapon**s: Powerful, stationary weapons that can be used to hold down positions or make heavy pushes into the Blob's territory. Can be hard countered by Reflective Blob. 
- **APEs/Emitters**: While these don't deal much damage, they do still deal some Heat damage which allows them to provide basic point defense in a pinch.

### Strategies that should be mechanically discouraged:

- **Plasma/Trit Fires**: The Blob can erect Strong Blob walls to block off the potential hazard area, and air scrubbers will be destroyed as it spreads. Mass Fires will be more of a hazard to the crew than the Blob itself.

- **Welderbombs**: The Blob has an inherent resistant to explosives and fire so this will only end up damaging and harming the Crew more than the Blob. This will also prevent nearby Crew from refilling welders they may be using for defense.

### Evolution (Blobolution)

In order to give the Blob a more specific objective to achieve and a way to power themselves up in their fight against the crew: The Blob has access to four tiers of "Evolution" that directly increase its spreading potential and resource generation. Evolutions do not modify the Blob's health or damage. These are intended to emulate an RTS player advancing up their tech tree and growing in power. Each tier also comes with a stationwide alert so the Crew is able to keep track of the Blob's overall progress towards its objective.

| Level | Required Nodes | Node Cap | Range of Influence (Tiles) | Resource Generation | Research Time (Seconds) | Cost |
|---|---|---|---|---|---|---|
| Base Level **"Interphase"** | 0 | 3 | 3 | 1 | 0 | 0 | - The Blob's starting level. If the Blob is discovered at this point it will have a use of Core Relocate to escape and regroup.
| 1st Evolution **"Prophase"** | 2 | 4 | 4 | 2 | 10 | 50 | - After researching Prophase: the station will receive an alert that a class five biohazard has been detected on station and must be dealt with if they wish to escape/survive and the hunt for the Blob will begin if the crew has not already discovered it. *Unlocks Spore Cannons*
| 2nd Evolution **"Metaphase"** | 3 | 5 | 5 | 2 | 15 | 100 | - Metaphase should be roughly where skirmishes between the Blob and Crew are occuring regularly in a back and forth between pushes from both sides while the Blob begins to unleash its deadliest minions. *Unlocks Blobbernauts*
| 3rd Evolution **"Anaphase"** | 4 | 6 | 7 | 3 | 20 | 150 | - Anaphase is where the Blob's strength is at its peak requiring the Crew to adopt the heaviest measures possible to really begin making meaningful pushes against the Blob. This is also the point where they can request codes for the station's Nuke if all seems lost. *Unlocks Split Consciousness.*
| 4th Evolution **"Cytokinesis"** | 6 | Infinite | Infinite | Infinite | 300 | 200 | - The ultimate goal of the Blob. Takes much longer to research than every previous tier and comes with a stationwide alert that the Blob is close to reaching critical mass. This is the make or break moment for the round as the Crew must defeat the Blob before it completes its evolution or they will lose. After the research has finished: the round will end and the Blob will gain infinite resources and have all caps on its abilities removed and its tiles will spread rapidly on their own. Any Escape Pods will launch to allow some method of escape, but anyone trapped on the station is doomed to be consumed. 

### Blob Objectives (Blobjectives)

The Round will end in Victory for the Blob if it:
 - Researches all <ins>four</ins> tiers of its Evolution.

The Round will end in a loss for the Blob if:
 - The Crew finds and destroys the Blob's Core.
 - The station's Nuke is armed and detonated, killing both the station and the Blob.

### Ideal Round Flow

**Early Game:** The Blob makes its way onto the station as a mouse (or mothroach) with a five minute timer until it ruptures into a Blob Core. Once it has found a suitable place away from prying eyes or cameras it can establish its base of operations by spreading Blob Tiles and creating buildings to start its economy. Once it has a functional starting base and begun to create Spores and built up some defenses, it will begin to research its first Evolution.

If the Blob is detected early it can attempt to spread Blob Tiles underneath the player that discovered them to slow and damage them before they get a chance to call for help. If worst comes to worst: The Blob has one use of Core Relocate, which allows it to move its Core to another point on the station so it may re-establish itself.

**Mid Game:** Once the first upgrade has been purchased and the crew alerted to its presence, the push and pull begins as the Blob fortifies its positions and begins to spread out to establish more nodes and resource pools. Its Spores will begin actively fighting and pushing back against the crew, or being used to subvert station defenses to let the Blob spread to other positions while also taking dead crew members to reinforce its numbers. The Crew will need to be actively planning and strategizing at this phase in order to push back against the Blob. Nodes will be primary targets to weaken the Blob directly and should be the target of crew pushes rather than a straightforward rush to the Core.

**Late Game:** The Blob is close to its final Evolution and its defenses will be put to the test as the crew will have had substantial time to plan for more advanced strategies, or just had time to arm the crew to the teeth. The Blob can no longer relocate its Core at this point, so if the crew has a handle on its position at this point they can make a confident push to end the Blob once and for all. It will however gain the ability to spawn a companion Blob to assist it, doubling its danger if they coordinate properly. If the crew is actively losing however: they'll have the option of calling or faxing Centcom to ask for the codes to the station's nuke to detonate it in a final desperate attempt to stop the Blob. If this happens: The Blob will need to aggressively push towards the Nuke to stop the crew before it's able to detonate. Any additional Antagonists that have made their way on station may either choose to ue the Blob's presence to accomplish their own objectives, fight against it on their own, or form an uneasy alliance with the crew if the Blob blocks their objective. This is also where the Blob's strength, spread potential, and resource generation will be at its peak.

**Round End:** The Round ends either in a nuclear detonation, the crew managing to destroy the Blob's Core, or the Blob researching its final evolution. If the Crew destroy the Blob's Core: the Escape Shuttle will be automatically called on a short timer to allow the survivors to escape. If the Blob researches its final Evolution: the round immediately ends and enters post-game. Escape Pods will launch and the Blob will begin rapidly consuming what's left of the station with its infinite resources.

### The Blob Side (Ghost Roles)

The Blob is the overarching entity the crew will be facing against, but is not necessarily alone in its quest. Spores and Blobbernauts act as Ghost Roles for Players to occupy if they are round removed for any reason. The Blob will speak to its units via its Blobmind on :o. Spores and Blobbernauts should coordinate with the Blob in its attempts to strategize, either in defending key points, pushing against the crew's defenses, or helping it find new ways to spread. Spores especially will benefit from a ghost role as they can float out to new locations on their own and ask the Blob to detonate them if they find an ideal spot, spreading Weak Blob and letting the Blob place a Node if it so wishes while allowing the simpler AI Spores to run point defense.

If a player on the crew's side is killed and taken by a Spore: They become a Blob Zombie on the Blob's side. Players can still /ghost if they don't wish to fight on the Blob's side, but Blob Zombies can be rescued and revived which will help incentivize them to keep playing. Since Blob Zombies 'pop' when killed, it also discourages Players from rushing back to the Crew just to be revived. Blob Zombies can also speak on :o. If crew members are freed from the Blob and revived: they will remember all details from their infestation, but not any point of their death. Their dreams cannot be saved unfortunately.

### Mid-Round Potential

To keep the Blob from being too predictable as to when it can appear: The Blob has options for arriving as a mid-round antagonist.

**Blob Meteor (Blobeteor):** During a standard meteor shower: one of the meteors was a Blob Core launched by a Blob that had completed its final Evolution. This event won't trigger until a player chooses the Blob Ghost Role, where the Blob will then impact the station with a group of Meteors and begin to spread. Due to the attention a meteor shower will bring: this Blob will start with an extra Node, Factory, and Resource Pool, while also having the advantage of spacing to discourage an early assault. (Ideally each individual Meteor is one of the Blob's buildings with a small gathering of Blob Tiles)

**Blob Vermin:** A swarm of creatures from the ventilation system carried an extra visitor among their ranks. This is treated as a normal Vermin invasion event, letting the Blob steathily make its way on station to establish its base of operations and spread. Can be either a Mouse, Snail, Snoth, or Mothroach.

## Additions

These are intended to be bonuses to the Blob's primary functions to help mix things up and add flavor to a round, but are not necessary for the base antagonist to function.

---

## Blob Strains

Blob Strains are variations either to specific mechanics the Blob is capable of, or the properties of said mechanics. Before the Blob places their core they are given the option of choosing a specific strain of Blob to alter their overall strategy either through damage types or specific abilities. Blob players do not have to pick one if they do not wish and it will be recommended for first time players to choose the default Blob option in order to get used to how the Blob functions at its baseline first.
- Strains should be designed with specific positives and/or negatives to make for more interesting alterations to strategy. Alternate damage types especially should carry some downside that ties into the theme they're meant to evoke.
- This will add a straightforward way to give the Blob more specific themes without the need for any major reworks in terms of its base mechanics. Given the amount of giant virus creatures in fiction, there's a lot of avenues to take.

**Values and Strains are not final and can be adjusted/added/removed as needed**

| Name | Attack Effects | Positives | Negatives |
|---|---|---|---|
| Basic Blob | 20 Brute, 2.5 Caustic | N/A | N/A |
| Blazing Oil | 5 Brute, 20 Burn, Lights targets on fire | When hit with burn damage - emits a burst of fire. Immune to fire. Passively heats environment it occupies (But not enough to ignite plasma/trit or ash crew members) | Water deals damage to Blob. Strong Blob is Waterproof |
| Cryogenic Liquid | 10 Brute, 10 Cold, 2.5 Burn | Immune to Cold. Passively chills environment it occupies. Releases Frezon when burned. | Takes 25% more Fire damage |
| Electromagnetic Web | 5 Brute, 25 Burn, 20% EMP Chance | Causes EMP if killed by melee, bullets or lasers. | Takes 25% more Fire damage, and full brute |
| Networked Fibers | 20 Brute, 15 Burn | Can only expand manually (by clicking). Can only expand next to core or nodes. Manual expansion near core/node movies it to that tile. Core regenerates 2.5 times faster than other strain types. Nodes and core produce extra resources instead of producing blob tiles. Blob Tiles do not become weak outside of areas of influence (Weak blob from Spores remain weak until moved over) and are cheaper to place. | N/A |
| Pressurized Slime | 15 Brute, 10 Oxy, 25 Stam | Releases water when hit or killed, 50% Brute resist. | N/A |
| Reactive Spines | 5 Brute, 25 Armor and Bio-Resist ignoring Brute Damage | Attacks nearby area when hit with melee attacks | N/A |
| Regenerative Material | 5 Brute, 17.5 Toxin | Blob Regenerates 3 times faster than normal, Factories produce one more spore, pools generate 1 extra resource, restores Blob in areas of influence faster | Damage resistances reduced by 50% |
| Replicating Foam | 22.5 Brute | Expands when burned but not immune to fire. Chance of bonus expansion | Takes 50% more brute damage |
| Shifting Fragments | 22.5 Brute | When damaged, always swaps positions with a nearby Blob | N/A|
| Synchronous Mesh | 17.5 to 30 Brute damage based on nearby blobs. | Spreads damage between nearby blob tiles | Takes 25% more damage from Fire. Damage spreading can kill tiles around main damaged tile |
| Nocturnal Infestation | 5 Brute, 10 Toxic, 10 Respiration damage, injects 2u Nocturine | Spores harvest sleeping/crit targets for 5 additional resources. | Takes 25% more Brute Damage. |
| Reptilian Devolution | 22.5 Brute | Injects targets with 5u of Weh Juice on hit | N/A |
| Cacophonous Laughter | 17.5 Brute | Blob tiles lose slow and become slippery, attacks inject 3u Happiness, Spore Cannons fire pies. Blob Zombies laugh. | Takes 25% more damage from fire. |
| Hematological Nightmare | 15 Slash, 2.5 Toxic | Injects 2.5u of Razorium on hit | Takes 25% more Slash damage. Bleeds when hit |
| The Overmind | 5 Blunt | Spore cannons cheaper and stronger. Factories spawn 5 spores maximum at reduced cost. Blobbernauts cheaper and revive after a period if corpse is not gibbed. | Blob damage significantly reduced, much more reliant on mobs/static defenses |
| Malignant Tendrils | 15 Brute, 7.5 Slash | Areas of Blob influence doubled, tiles expand out faster and weak blob is restored quicker | Pulses are 2X Slower, takes 50% more Brute damage |
| Feast or Famine | 17.5 Brute | Resource Pools have double generation speed. | Pools degrade and lose health over time. Time to death roughly equivilant to time it would take to produce enough resources for two pools |
| The Hungering Horror | 20 Caustic 2.5 Burn | Crew members are abducted by Spores and taken to Resource Pools to be dissolved and absorbed over 20-30 seconds. Absorbed crew give 30-40 bonus resources to the Blob. Extra DoT while standing on Blob Tiles. | Blob Zombies disabled, takes full Cold damage |
| The Beast | 20 Brute | Spores turn dead crew members into Mini-Nodes. These do not count towards Blob's evolution, but can support buildings while turning Weak tiles into Normal tiles. Crew taken by Blob cannot be revived. Blob can use converted Mini-Nodes to talk to the Crew. | Blob Zombies disabled, takes 25% more Slash damage |

## Unit Variations

Evolutions could include unique and alternate upgrades to encourage even more variation in a Blob's strategy and give Blobs greater freedom. Will need outside discussion and assistance to develop.
 - IE: The Blob researches Metaphase and chooses between Blobbernauts or more powerful Spore Cannons. Ideally it would be between only two options to not overwhelm a Blob Player with choice, but should still feel meaningful towards their overall development.
