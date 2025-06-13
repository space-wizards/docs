# Blob Proposal

| Designers | Implemented | GitHub Links |
|---|---|---|
| TiniestShark (Sprite Artist) | :x: No | TBD |

## Overview

The Blob is a Major Conversion Antagonist with the goal of replicating and evolving until it can ultimately consume the station. A strange biohazardous organism that arrived on the station through the infestation of vermin, or a meteor impact carrying its core, the Blob is a Round start antagonist that must find a safe place to establish its core and expand. 

This is an intended re-imagining of the original Blob to better support a more interesting style of play both for the crew of the station and the Blob itself. The Blob is no longer simply spreading, but evolving in its quest to perfect itself and consume the galaxy.

### Gameplay Loop

The Blob will begin the round as an infected Mouse or Mothroach and placed somewhere at random on the station alongside other roundstard vermin. From there the Blob has approximately five minutes to find an ideal location on the station to place its Core, its base building and the center of a Blob's infestation. The Blob from this point assumes the POV of a free floating camera/cursor similar to the Station's AI with its vision based on the sight range of its Blob Tiles and Units. The Core will begin to slowly create Blob Tiles around itself while The Blob will begin to place Blob tiles manually, using resources for each one placed, to expand itself outward. If the Blob clicks on an occupied tile, the surrounding Blob will attack whatever is in the tile if it is not able to spread into it, beating down walls to open the area up.

If the Core is destroyed: The Blob loses the round and Evac will be called allowing the crew to leave. As well: all Blob tiles, units, and buildings will begin to degrade in health until they die.

The Blob starts with a pool of resources it spends in order to place Blob tiles, build buildings, and spawn units. It has a maximum initial storage of 100 resources, and can expand this reservoir with Storage Blobs. The Core creates its own resources passively but this can be increased by building Resource Blobs, which generate 1 resource with each 'pulse' of a Core or Node. The Blob must also start placing Nodes to solidify it's influence over an area. It will then research upgrades that boost its base stats and spreading potential until it can achieve its final evolution, while also working to fight off the crew when its inevitably discovered.

After the Blob has been confirmed on station: the Emergency Shuttle will be unable to be called. If the shuttle has already arrived: It will be unable to leave. Only Escape Pods will be launched if the Blob wins. (Though if necessary the shift change Evac can come as normal as an emergency evac that will spawn off station)

In order to win, the Blob must research four tiers of "Evolution", which it reaches through putting down a certain number of nodes and then spending the amount of resources needed to research the upgrade.

## Blob Mechanics/Features to be Added

### Abilities

The Blob has a number of basic controls and abilities to make their job of spreading and consuming much easier. Due to the amount, these should be broken up to ensure newer players arn't overwhelmed and that the UI isn't clogged up with buttons. Each action also has a corresponding hotkey to give more experienced players an easier method of control and allow some actions to need UI elements (Actions like Alt-Clicks should have a popup when the corresponding key is held).

- **Spread** *(Left Click)*: Clicking on a tile spreads Blob to selected tile. Tile must be connected to existing Blob. Each placed tile takes resources based on type. Can be placed under Crew.
- **Attack** *(Right Click)*: Attacks selected entity with nearest Blob tiles.
- **Delete Blob** *(Alt Click)*: Allows Blob to delete misplaced or unnecessary Blob tiles or Buildings for a small refund (40%) (Weak tiles are not refunded).
- **Core Relocate**: Available until Anaphase: Allows Blob core to swap its position with a target node. Replaced with...
- **Split Consciousness**: Replaces Relocate during Anaphase. Blob spends 100 resources to turn target node into a new Core. The new Core will be an open ghost role and will assist the Blob in taking control of the station. Both Blobs share a resource pool, evolve together, and command the same units. Secondary Blob can be a different variant than the first. Also provides a chance for Players to learn the Blob with a more experienced Blob already having a fairly cohesive setup if they've lasted this long.
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

Blob Tiles are the Blob's primary method of spreading throughout the station. Each tile costs a small amount of resources, allowing a Blob to either slowly spread out by spending their resources constantly, or saving up for a rush of Blob. Blob Tiles are capable of attacking, dealing damage depending both on the type of tile and the strain of the Blob. Blob Tiles can be destroyed by the crew through damaging them with any weapons on hand. Blob Tiles can be walked on but deals passive damage over time. Since movement is no longer tile based and the crew is able to stack together, it's less feasible to have the Blob block off every tile it occupies. This change also prevents the Blob from easily locking off individuals or bodies from the crew to prevent retrieval, and also means the Crew can see into the Blob more easily in any areas not blocked by Strong Blob.

A Blob is encouraged both to spread to take more territory, but also consider the space they occupy to block off Crew paths more efficiently and set up choke points. While the crew will not be directly blocked off by all tiles, the pervasive slow from a Blob's wider territory will make up the difference.

- **Normal Blob** | *Cost: 5 | Health: 30*: Main tile of the Blob. Spreads influence outwards, allows buildings to be placed down, and passively damages mobs that walk onto it. Entities that walk onto Blob Tiles are slowed by 30%. Degrades into Weak Blob if outside the influence of a Node/Core. Will attack nearby mobs when pulsed by a Core/Node. Only one tile can attack a mob at a time so a person in the middle of the Blob doesn't get deleted by one pulse (And to better spread out damage).
- **Weak Blob** | *Cost: 2 | Health: 15*: If the Blob attempts to spread outside the influence of a Node/Core, they will only spread Weak Blob at a reduced cost. Weak Blob has half health and damage of a regular Blob Tile, and only slows by 15%. Buildings can still be placed on Weak Blob but will degrade over time. Also deals damage to mobs standing on top of it. Weak Blob both allows a Blob to scout and harass the crew for a cheaper cost, while also providing a visual indicator of the Blob's area of influence.
- **Strong Blob** | *Cost: 8 | Health: 250*: Upgraded from Normal Blob. Strong Blob Tiles are solid walls that can take much more damage before being destroyed. Fireproof and block air flow in the event of station fires. 
- **Reflective Blob** | *Cost: 15 | Health: 150*: Upgraded from Strong Blob. Reflective Blob Tiles are solid like Strong Blob, but have less health. In exchange: They are able to reflect laser shots from the crew (90% Reflect Chance).
- **Blob Locks/Membrane** | *Cost: 0 | Health: 250*: Variant of Strong Blob. Blob Locks/Membrane are doors the Blob can establish to fortify an area, while still letting their units through. Useful for chokepoints, and for letting units into space. Visually function as a signifier of Blob troop movement, or made to look as such.

### Blob Buildings

Blob Buildings are what the Blob must use to gather strength and fight the station. All buildings aside from the Core must be built on Blob Tiles. Any buildings within the influence radius of a Node/Core will regenerate health over time, and lose it slowly when not. Blob buildings give the Blob its economic focus and should be a primary focus for the Blob as the round goes on in order to properly gather its strength and maintain its offensive. 

- **Core** | *Health: 400* : The brain of the Blob. Generates 1 resource a second on its own while pulsing nearby buildings every 10 seconds. Supports buildings in its influence radius. If destroyed: The Blob loses.
- **Node** | *Cost: 60 | Health: 200*: The nerves of the Blob. Spreads Blob around itself automatically and supports buildings in its influence radius. Blobs around node attack automatically and will take out any non-blob walls around it. Additionally restores any Weak Blob in its radius to Normal Blob. Nodes are the major signifiers of Blob Presence and required both to hold its territory down, and also to evolve. Cannot be built within four tiles of the Core or another Node. Pulses nearby buildings at the same rate as Core.
- **Resource Pool** | *Cost: 40 | Health: 60*: Produces resources over time (1 every four seconds). Cannot be built within three tiles of another Resource Pool. Generates 1 extra resource when pulsed to assist in early game.
- **Spore Factory** | *Cost: 50 | Health: 200*: Creates Blob Spores over time with a cap of three per factory. Takes five resources per Spore at a rate of seven seconds taken for each spore. Cannot be built within four tiles of another Spore Factory. Creates a Spore when pulsed up to building cap. (Needing resources but being faster lets a Blob have more agency in the speed of buildup of their army, while also encouraging them to build up a strong economy)
- **Storage Blob** | *Cost: 40 | Health: 30*: Increases max resource capacity by 50. Cannot be built within three tiles of another Storage Blob. If a Storage Blob is destroyed: The Blob's resources will tick down to its new cap if it is above its current cap rather than being lost all at once so an unaware player isn't immediately out of luck and less skilled players who were hoarding still have a chance to spend. Maximum storage is 500 resources.
- **Spore Cannon** | *Cost: 80 | Health: 300 | Damage: 2*: A support tower that fires fast, weak blob projectiles at enemies. Slows targets with a stacking speed debuff (15% with each hit, stacks with Blob's natural slowdown. Total speed debuff capped at 90%) as they're covered in Blob. Functions to dissuade lone attackers from assaulting Nodes or specific locations, and assists in harassing combatants attempting to outrange the Blob. Fires an extra bolt when pulsed. *Unlocked during Prophase*
- **Blob Grapple** | *Cost: 60 | Health: 200 | Damage: 1*: A support tower that fires a Blob tendril that grapples onto the first thing it hits and prevents it from moving while slowly dragging it towards the Blob (Can hit Walls, Entities, or Mobs). Grapples can travel through Strong Blob. Blob can spread Blob Tiles from point of grapple's impact. Intended to give Blobs a way to spread back onto the station if they're disconnected for any reason, or to grab and hold down Shuttles for its units to attack and overtake. Grapples can be destroyed by Crew. Spreads Blob at grapple point when pulsed.

### Pulsing

A "Pulse" is a radial signal the Blob emits every ten seconds minimum with a maximum life span of thirty seconds. The Core and the Blob's Nodes will emit a pulse that radiates outward to the edge of its area of influence, or its current spread of Blob. The pulse expands outward from the Core/Node at a rate of one tile a second and activates an effect on every building it hits. Pulsing is also how a blob heals itself and its buildings while expanding its Blob passively. Pulsing will also upgrade Weak Blob to Regular Blob in the Blob's radius.

Pulsing can trigger a Building's effects outside of their normal rotation, with the primary beneficiary being its resource pools. The closer the building to a Core/Node, the sooner and more frequently it gets pulsed. If the Pulse reaches a tile the Blob has not spread onto, it will spread onto it. The Blob can only spread one to two tiles outward per pulse, per Core/Node. As the game goes on and the Blob's territory grows larger, pulses will take longer to reach the edge of its area of influence, making the delay between new pulses longer and providing less benefit over time to the Blob, forcing it to rely more on its constructed economy. This gives the Blob a bonus when its first starting out in case of an early crew offensive or early discovery before it can properly get a chance to set itself up.

A Core/Node that has reached its maximum range of influence will only expand one tile outward of Weak Blob with every Pulse if there is no other Blob to place/replace. This also helps the crew see the range of the Blob's influence so they can properly set up defenses or plan as needed.

### Unique Buildings

Unique Buildings are specific structures that are created when the Blob consumes specific station objects or machines. These are mainly to highlight what the Blob has taken from the crew and to clearly show the crew where the objects have gone. These can also provide unique functions depending on the structures taken over to give a Blob specific strategic targets.

- **Captured Nuke** | *Health: 100*: If the Blob manages to spread onto a Nuke, it creates a Captured Nuke. This is a reinforced Blob tile that prevents the Crew from arming the Nuke. When destroyed, the Nuke is freed and able to be armed by the Crew once again.

### Units

While the Blob is able to fight directly through its tiles, it has access to a roster of Units it can create to assist in reinforcing its position, pushing into new territory, or simply harassing the Crew. The Blob shares it sight with its units so they can scout areas the Blob cannot reach. Blob units cannot harm the Blob. Units are intended to each fill specific, complementary roles both to encourage a Blob to combine their abilities with one another, and also for players taking ghost roles to team up with one another to take advantage of these bonuses.

- **Spore** | *Cost: 5 | Health: 40 | Damage: 4 (25 Structure)(10 Caustic on detonation)*: Low Tier Unit. Floats through air, attacks weakly, and explodes when killed. Can manuever with ease in Zero G and in Space, and are immune to pressure damage. Spread Weak Blob in a radius around them when they explode, and can be commanded to explode manually. Also function as Ghost Roles for Players to take. Cannot be exploded manually by Ghost players. (AI should attempt to mob players rather than kite to ensure they blob crew when they die). 
- **Blob Zombie "Blombie"** | *Cost: 1 Crew | Health: 60 | Damage: 15*: Medium Tier Unit. Created when a Spore takes over a dead crew member (5 second Doafter). Controlled by downed Player, or by AI if the player has disconnected or taken another role. Acts as a regular mob, chasing down Crew and attacking when AI. Has resistances from armor crew member was wearing. Spores on head "pop" when killed, allowing Crew's body to be retrieved and revived. Blob Zombies also function as a "soft" delivery mechanism to ensure the crew can retrieve bodies. Due to not being a reliable unit to produce and to keep a Blob from trying to locking them off for being too important: these function as the all-rounder in a Blob's army with no particular advantages/disadvantages. Their ability to "pop" and spread territory also encourages this factor while still giving the Blob a reason to pursue making Blob Zombies so players can stay in the game.
- **Blobbernaut** | *Cost: 80 | Health: 300 | Damage: 40 (80 Structure)*: High Tier Unit. Expensive, powerful bruiser. Attacks deal heavy Blunt damage with additional damage based on Blob Strain. Blobbernauts have a low attack speed to emphasize their bruiser role, and leaves them open to being swarmed if not supported by other units. Regenerates health steadily while on Blob Tile, halved on Weak Blob. Ghost role for Players, AI if uncontrolled. If a Blobbernaut's factory is destroyed, they begin to decay steadily until they die. Immune to pressure/temp changes, but has trouble maneuvering in zero gravity. Intended to be the signal of the turning point in a Blob's power when it's unlocked due to their raw strength and breaching potential.

### Damage Resistances

- **Blunt/Brute**: The Blob is a solid mass of matter, making most blunt weaponry deal little damage. This renders most easily-accessible weaponry less useful so the Crew will need to work to arm up rather than only grabbing crowbars/toolboxes/extinguishers/etc.
- **Cold**: The Blob has adapted to survive in space, making it resistant to low pressure environments/cold temperatures. (This also heavily discourages a crew from spacing the station to fight the Blob)
- **Piercing**: Due to the Blob's strange composition; bullets will either fly through it or pierce and deal little damage. Blob Units take normal damage from Pierce to not make guns useless, but dissuade the crew from just raiding the armory the second the Blob's confirmed.

### Damage Vulnerabilities

- **Slash**: Bladed weapons deal full damage against the Blob, giving the crew a clear avenue of damage if other sources are not readily available. 
- **Fire**: The Blob's composition makes it vulnerable to Heat damage, meaning that Welders and Flamethrowers will deal additional damage to it alongside Laser based weaponry.
- **Structural**: The more concentrated the Blob is in an area, the more resistant it is to normal methods of attack, but the weaker it is to structural damage. Strong Blob and Buildings take additional Structure damage so the crew always has a clear avenue of breaching the Blob in case it gets in a position to spam Strong Blob.

### Evolution (Blobolution)

In order to give the Blob a more specific objective to achieve and a way to power themselves up in their fight against the crew: The Blob has access to four tiers of "Evolution" that directly increase its spreading potential and resource generation. Evolutions do not modify the Blob's health or damage. These are intended to emulate an RTS player advancing up their tech tree and growing in power. Each tier also comes with a stationwide alert so the Crew is able to keep track of the Blob's overall progress towards its objective.

Nodes are the central point of a Blob's Evolution as it needs a certain amount to unlock its next Evolution. This comes with a cap to a Blob's maximum Nodes so it can't simply camp and build all the ones it needs to rush Evolutions and win, but is still generous enough to let a Blob plan ahead. Nodes being a required structure for the Blob, and also its central necessity for holding down territory, means that Nodes are now priority targets for the Crew, giving them specific points of attack rather than to simply swarm the Blob wherever it appears. This means the Crew always has a clear method of meaningfully harming the Blob as opposed to simply treating the Blob as a mess to clean up. The Crew will be encouraged both to set up points of defense outside of a Node's influence, work together to push into Blob territory, and can easily see a Blob's economy to attack it.

Conversely: The centraliztion of the Blob's expansion means that Blobs now have clearer areas to focus on rather than needing to keep track of all angles at all times. A Blob has hotkeys to easily take them to their most important structures, and can play with the knowledge that it's much harder to be taken by surprise due to their centralization. This also makes it easier for players less familiar with RTS games to know what to focus on as the Blob, while still giving them the enjoyment of being an all spreading and consuming entity. It's also much easier to plan its defenses around central points than needing to cover every angle possible.

Evolution is also intended both to give a sense of progression to a round while simultaneously giving players less familiar with the Blob or RTS games a chance to gradually integrate the Blob's mechanics into their overall strategy. A Blob cannot simply spam Blobbernauts right at the start of a match with a crew that has less potential to deal with them. As the Blob evolves: So too do its capabilities and potential for harm. 

| Level | Required Nodes | Node Cap | Range of Influence (Tiles) | Resource Generation | Research Time (Seconds) | Cost |
|---|---|---|---|---|---|---|
| Base Level **"Interphase"** | 0 | 3 | 3 | 1 | 0 | 0 | - The Blob's starting level. If the Blob is discovered at this point it will have a use of Core Relocate to escape and regroup.
| 1st Evolution **"Prophase"** | 2 | 4 | 4 | 2 | 20 | 50 | - After researching Prophase: the station will receive an alert that a class five biohazard has been detected on station and must be dealt with if they wish to escape/survive and the hunt for the Blob will begin if the crew has not already discovered it. *Unlocks Spore Cannons*
| 2nd Evolution **"Metaphase"** | 3 | 5 | 5 | 2 | 30 | 100 | - Metaphase should be roughly where skirmishes between the Blob and Crew are occuring regularly in a back and forth between pushes from both sides while the Blob begins to unleash its deadliest minions. *Unlocks Blobbernauts*
| 3rd Evolution **"Anaphase"** | 4 | 6 | 7 | 3 | 50 | 150 | - Anaphase is where the Blob's strength is at its peak requiring the Crew to adopt the heaviest measures possible to really begin making meaningful pushes against the Blob. This is also the point where they can request codes for the station's Nuke if all seems lost. *Unlocks Split Consciousness.*
| 4th Evolution **"Cytokinesis"** | 6 | Infinite | Infinite | Infinite | 300 | 200 | - The ultimate goal of the Blob. Takes much longer to research than every previous tier and comes with a stationwide alert that the Blob is close to reaching critical mass. This is the make or break moment for the round as the Crew must defeat the Blob before it completes its evolution or they will lose. After the research has finished: the round will end and the Blob will gain infinite resources and have all caps on its abilities removed and its tiles will spread rapidly on their own. Any Escape Pods will launch to allow some method of escape, but anyone trapped on the station is doomed to be consumed. 

### Blob Objectives (Blobjectives)

The Round will end in Major Victory for the Blob and Major Loss for the crew if:
 - Researches all <ins>four</ins> tiers of its Evolution.

The Round will end in a Minor Victory for the Blob and Minor Loss for the Crew if:
 - The Shift change shuttle comes and goes, taking any remaining crew with it.

The Round will end in Minor Loss for the Blob and Minor Victory for the Crew if:
 - The station's Nuke is armed and detonated, killing both the station and the Blob.

The Round will end in a Major Loss for the Blob and a Major Victory for the crew if:
 - The Crew finds and destroys the Blob's Core.

In order to prevent the Blob from stalling out a round by not researching it's final upgrade (In case there arn't Admins who can help by spawning Cburn, ERT, or giving the crew Nuke codes): The Shift Change Evac Shuttle will arrive at its normal time, but will only spawn off station in order to prevent infection from the Blob. The Split Consciousness ability also lets a second Blob force the Evolution. The additional ghost roles from Spores also allow a social pressure from the additional members of the Blob's team.

## Crew Mechanics

The Blob is an overwhelming hostile force that requires the Crew to properly coordinate and work together in order to defeat. Mechanically this is encouraged through the Blob's new evolution system: Having Nodes be the primary targets/bases of the Blob gives the Crew direct targets to attack rather than any section of the Blob. Weak Blob leading to Normal Blob also helps the crew find these points of opportunity much more easily, and a Blob's stronger point defenses further encourages the mindset of "Work Together". The natural slower periods between Blob Evolutions gives the crew some level of breathing room to discuss plans or work towards their goals without putting a constant level of pressure on them to be engaging the Blob at all times like its previous iteration.

### Weapons against the Blob:

- **Laser Weapons**: The main dealers of Heat damage the crew has access to. Lasers will be useful all around weapons for fighting the Blob, just be wary of Reflective Blob.
- **Flashes**: Flashes will clear Weak Blob in a small radius around the user, and prevent Normal Blob from attacking momentarily so a crew may escape its clutches. Ideal low-tier defensive tool for wayward crew members, and helps clear an unprepared Blob from an area.
- **Flashbangs**: Flashbangs can be used to clear Weak Blob Tiles in a wide radius and weaken regular Blob tiles into Weak Blob, just warn other crew members before throwing! Does not affect Strong or Reflective Blob. Provides clear AoE utility that the crew will want so they'll be less likely to go for standard damaging grenades.
- **Shuttle Weapon**s: Powerful, stationary weapons that can be used to hold down positions or make heavy pushes into the Blob's territory. Can be hard countered by Reflective Blob. 
- **APEs/Emitters**: While these don't deal much damage, they do still deal some Heat damage which allows them to provide basic point defense in a pinch.

### Strategies that should be mechanically discouraged:

- **Plasma/Trit Fires**: The Blob can erect Strong Blob walls to block off the potential hazard area, and air scrubbers and vents will be destroyed as it spreads. Mass Fires will be more of a hazard to the crew than the Blob itself.
- **Welderbombs**: The Blob has an inherent resistant to explosives and fire so this will only end up damaging and harming the Crew more than the Blob. This will also prevent nearby Crew from refilling welders they may be using for defense.
- - **Flamethrowers**: Flamethrowers often result in friendly fire more often than not, and the additional fact of Blob tiles now being floor instead of solid constant walls means that targetting them will be more difficult. Strong Blob being fireproof also means that Flamethrowers will only have utility against Blob units but there are already much better avenues of attack.

### Departmental Strategies/Roles:

- **Security**: Security should be the first line of defense against the Blob, helping to establish points of defense, coordinating with Command staff in order to set up defensive points, protecting key departments and staff, and distributing weapons to crewmates while fortifying areas ahead of the Blob. Riot Gear will be especially useful in combatting the Blob.
- **Cargo**: Cargo should be doing what they do best: Ordering weapons and supplies for the Station to fight back against the Blob. Ideally the less straightforward nature of the Blob compared to other antagonists will encourage the department to work with the rest of the Station to think of more unconventional methods of attack. Salvage will need to be on their A-Game gathering materials and ores for the Station, and the Blob's new methods of grabbing shuttles and wayward players means that the usual solo mindset of Salvagers is heavily discouraged. The Cargo Shuttle will be a key tool as well in scouting the edges of the station to find signs of the Blob's influence in case it uses its new spreading strategies to go around traditional defenses.
- **Medical**: Front line triage will be an incredibly important part of Blob defense, as the ability to quickly grab critical crew members and bring them to safety will keep the Blob from taking them to reinforce its numbers. Surgery (If implemented) will also be necessary to be used on recovered Blob Zombies to remove the remnants of their infestation to properly revive them.
- **Science**: The crew will need every advanced technology they can get in order to defeat the Blob, so Science will be similar to their iteration in WarOps: Quickly researching technology to gear the Crew up. The Blob's composition also encourages them to not focus solely the Arsenal branch, and at least secure Engineering research for better Welders. The Blob's widespread but sedentary nature also makes it feasible to use more unconventional strategies to fight it: Anomalies could be spawned and tossed into the middle of a wayward Blob base as it'll have limited methods of dealing with them. The RD's portal will also be as useful as ever in keeping a connected front line. Ideally they will also be producing flashes for point defense.
- **Engineering**: The Blob is an entity of mass destruction and will need to be slowed down in any way possible. Fortifactions and repairs will be a critical method of slowing down the Blob's spread and assault, or repairing spacing to keep the Blob from attempting to turn the environment against the crew. They should also be assisting Science and Security in producing heavier stationary weapons for powerful pushes into Blob territory.
- **AI/Silicons**: The Silicons of the Station can take a much more direct role in combating the Blob due to its nature as Non-crew. The AI's ability to keep an eye on all corners of the station will be highly necessary for spotting the Blob's attempts to spread in unconventional ways, or using its abilities to assist in reinforcing areas either on the front line, or in other areas to prevent Blob infiltration. Borgs will be able to assist in direct combat with welders, and their inability to be infested means they will be a prime unit for recovering crew members.

## Player Interactions/Round Flow

The Blob is a station-wide biohazard that effectively has Centcom cut the crew off from the wider system ecosystem in order to contain it. While the Blob won't interact with the crew directly by talking to them, it will instead aggressively push into the Station's environment and force every department and character to take up some role in its defense or perish.

### RP Potential

Panic and fear at the strange composition and behaviors of the Blob will generally be the most forward-facing forms of RP, reacting to the creatures spawning from it, Spores taking friends, Blobbernauts barreling into established defenses, etc. With the Blob having established periods of holding back and growing to fuel its evolution, the crew will be given more chances to re-group, re-organize, and play out the scenario as they attempt to figure out an ideal strategy to defeat the Blob, or process the situation they're trapped in.

The spread out nature of the Blob allows smaller groups to form their own parties and strategize against the Blob in their own ways. Lone fighters/tiders will be easily overwhelmed and caught by the Blob so the crew is incentivized to work in whatever groups they can scrounge up.

Ideally the Blob will allow for the more 'alien' aspects of a sci fi environment to flourish rather than the humanoid and communicable antagonists already in the game. Revolutionariess and Syndies can be talked to, Nuclear Operatives are terrifying but are just a group of terrorists that can be easily conceptualized, even mid-round antags like the Dragon are just a giant fish. The Blob is truly alien and cannot be reasoned, argued, or even spoken to and has cut them off from (almost) any possible rescue and must be stood against. 

Inversely: The Blob's new cohesion between its mechanics and units encourages an Overmind to properly communicate and guide its minions towards its grand evolutionary strategy, preferably in a grandiose godlike method. Converted Crew Members will also remember their time infested underneath the Blob when they are revived, encouraging the Blob to give them passing words for the Crew or to just taunt them with their fate. The Blob is a hostile, terraforming entity with a mob of horrid creatures under its control and should act as such. 

### Ideal Round Flow

**Early Game:** The Blob makes its way onto the station as a mouse (or mothroach) with a five minute timer until it ruptures into a Blob Core. Once it has found a suitable place away from prying eyes or cameras it can establish its base of operations by spreading Blob Tiles and creating buildings to start its economy. Once it has a functional starting base and begun to create Spores and built up some defenses, it will begin to research its first Evolution.

If the Blob is detected early it can attempt to spread Blob Tiles underneath the player that discovered them to slow and damage them before they get a chance to call for help. If worst comes to worst: The Blob has one use of Core Relocate, which allows it to move its Core to another Node on the station so it may re-establish itself.

**Mid Game:** Once the first upgrade has been purchased and the crew alerted to its presence, the push and pull begins as the Blob fortifies its positions and begins to spread out to establish more nodes and resource pools. Its Spores will begin actively fighting and pushing back against the crew, or being used to subvert station defenses to let the Blob spread to other positions while also taking dead crew members to reinforce its numbers. The Crew will need to be actively planning and strategizing at this phase in order to push back against the Blob. Nodes will be primary targets to weaken the Blob directly and should be the target of crew pushes rather than a straightforward rush to the Core. Its second Evolution is where itll begin to truly exert its power as it begins to spawn Blobbernauts to properly combat the crew as they arm.

**Late Game:** The Blob is close to its final Evolution and its defenses will be put to the test as the crew will have had substantial time to plan for more advanced strategies, or just had time to arm the crew to the teeth. The Blob can no longer relocate its Core at this point, so if the crew has a handle on its position at this point they can make a confident push to end the Blob once and for all. It will however gain the ability to spawn a companion Blob to assist it, doubling its danger if they coordinate properly. If the crew is actively losing however: they'll have the option of calling or faxing Centcom to ask for the codes to the station's nuke to detonate it in a final desperate attempt to stop the Blob. If this happens: The Blob will need to aggressively push towards the Nuke to stop the crew before it's able to detonate. Any additional Antagonists that have made their way on station may either choose to ue the Blob's presence to accomplish their own objectives, fight against it on their own, or form an uneasy alliance with the crew if the Blob blocks their objective. This is also where the Blob's strength, spread potential, and resource generation will be at its peak.

**Round End:** The Round ends either in a nuclear detonation, the crew managing to destroy the Blob's Core, or the Blob researching its final evolution. If the Crew destroy the Blob's Core: the Escape Shuttle will be automatically called on a short timer to allow the survivors to escape. If the Blob researches its final Evolution: the round immediately ends and enters post-game. Escape Pods will launch and the Blob will begin rapidly consuming what's left of the station with its infinite resources.

### The Blob Side (Ghost Roles)

The Blob is the overarching entity the crew will be facing against, but is not necessarily alone in its quest. Spores and Blobbernauts act as Ghost Roles for Players to occupy if they are round removed for any reason. The Blob will speak to its units via its Blobmind (or Overmind) on :o. Spores and Blobbernauts should coordinate with the Blob in its attempts to strategize, either in defending key points, pushing against the crew's defenses, or helping it find new ways to spread. Spores especially will benefit from a ghost role as they can float out to new locations on their own and ask the Blob to detonate them if they find an ideal spot, spreading Weak Blob and letting the Blob place a Node if it so wishes while allowing the simpler AI Spores to run point defense. They will also function as a soft "Learner's Role" for the Blob as they assist in one of its primary mechanics, while also providing a ghost role with a lower barrier of entry for players to take rather than the expensive Blobbernauts to help reduce friction between the player and the Blob.

Blobbernauts now no longer decay off of Blob so they are not punished for attempting to push out. Conversely: In order to ensure Blobbernauts that run off don't screw over a Blob: it's easier for a Blob to support them out of its territory. With their slower attack speed it's more encouraged for them to work in groups with either Spores to provide cover, or explode to spread Blob to heal itself or other Blobbernauts to compound their destructive force. Cheaper spreading for the Blob out of its areas of influence means they can also support Blobbernauts more easily who choose to go this route, further encouraging Teamwork on the Blob's side in more a direct manner. The Blob having more defensive emplacements also means they won't need to worry as much if a Blobbernaut groups up with a few other players and pushes against the crew.

If a player on the crew's side is killed and taken by a Spore: They become a Blob Zombie on the Blob's side (If the spore was Player controlled, this is treated as them dying). Players can still /ghost if they don't wish to fight on the Blob's side, but Blob Zombies can be rescued and revived which will help incentivize them to keep playing. Since Blob Zombies 'pop' when killed, it also discourages Players from rushing back to the Crew just to be revived. Blob Zombies can also speak on :o. If crew members are freed from the Blob and revived: they will remember all details from their infestation (both for RP purposes and so a Player's time on the Blob isn't felt as "wasted"), but not any point of their death.

The Blob cannot speak to, or hear the Crew of the station's communications. Spores, and Blobbernauts can hear the crew speak, but cannot speak themselves. Spores just burble, and Blobbernauts growl, emit horrible gutteral noises or roar to spread fear, and Blob. Blob Zombies can still hear the Crew through their earpieces, allowing them to provide an interesting service to the Blob in spying if they so choose, but cannot speak over it. Ideally Blob Zombies will only be able to gurgle helplessly, with maybe the occasional "help me" or "Im sorry" managing to escape.


## Additions

These are intended to be bonuses to the Blob's primary functions to help mix things up and add flavor to a round, but are not necessary for the base antagonist to function.

---

## Mid-Round Potential

To keep the Blob from being too predictable as to when it can appear: The Blob has options for arriving as a mid-round antagonist.

**Blob Meteor (Blobeteor):** During a standard meteor shower: one of the meteors was a Blob Core launched by a Blob that had completed its final Evolution. This event won't trigger until a player chooses the Blob Ghost Role, where the Blob will then impact the station with a group of Meteors and begin to spread. Due to the attention a meteor shower will bring: this Blob will start with an extra Node, Factory, and Resource Pool, while also having the advantage of spacing to discourage an early assault. (Ideally each individual Meteor is one of the Blob's buildings with a small gathering of Blob Tiles)

**Blob Vermin:** A swarm of creatures from the ventilation system carried an extra visitor among their ranks. This is treated as a normal Vermin invasion event, letting the Blob steathily make its way on station to establish its base of operations and spread. Can be either a Mouse, Snail, Snoth, or Mothroach.

**Scientific Endeavor:** A Science Ship that had been studying the Blob FTL's to the Station to get supplies and repairs. Unbeknownst to them: The Blob has escaped containment and infested one of the scientists on their ship (Or all of them for something even more fun). The scientist will have five minutes to commit any sabotage they need to while also finding a place to set their core. After five minutes (or sooner if the Scientist chooses), the Blob ruptures out of the scientist's body and gibs them as the Blob begins to spread and take over the station.

## Blob Strains

Blob Strains are variations either to specific mechanics the Blob is capable of, or the properties of said mechanics. Before the Blob places their core they are given the option of choosing a specific strain of Blob to alter their overall strategy either through damage types or specific abilities. Blob players do not have to pick one if they do not wish and it will be recommended for first time players to choose the default Blob option in order to get used to how the Blob functions at its baseline first. Strains are not able to be swapped between and are intended to be specific builds the Blob chooses and has to build their strategy around.

Strains will provide variety to experienced Blobs looking for different strategies/ways to play while also giving the crew a new form of a familiar antagonist to engage with. In the same way as Nukies developing gimmicks, Strains will let a Blob mix up a round in a more spectacular fashion both to invoke the idea of a destructive, terraforming entity and also to encourage the Crew to not simply stick to one strategy. IE: A crew fighting the Blazing Oil Strain will take up the role of firefighters aggressively attempting to put down the scorching heat the Blob is spreading.

- Strains should be designed with specific positives and/or negatives to make for more interesting alterations to strategy. Alternate damage types especially should carry some downside that ties into the theme they're meant to evoke. These should ideally induce some specific changes to Blob/Crew strategy over the course of a round rather than simply a flavor of damage.
- This will add a straightforward way to give the Blob more specific themes without the need for any major reworks in terms of its base mechanics. Given the amount of giant virus creatures in fiction, there's a lot of avenues to take.
- This also provides an easy avenue of customization for downstream forks looking to find ways to make their own Blobs unique.

**Values and Strains are not final and can be adjusted/added/removed as needed. Honestly there's probably too many of them but they make decent examples**

| Name | Attack Effects | Positives | Negatives |
|---|---|---|---|
| Basic Blob | 20 Brute, 2.5 Caustic | N/A | N/A |
| Blazing Oil | 5 Brute, 20 Burn, Lights targets on fire | When hit with burn damage - emits a burst of fire. Immune to fire. Passively heats environment it occupies (But not enough to ignite plasma/trit or ash crew members) | Water deals damage to Blob. Strong Blob is Waterproof |
| Cryogenic Liquid | 10 Brute, 10 Cold, 2.5 Burn | Immune to Cold. Passively chills environment it occupies. Releases Frezon when burned. Injects 5u of Frost Oil on hit  | Takes 25% more Fire damage |
| Electromagnetic Web | 5 Brute, 25 Burn, 20% EMP Chance | Causes EMP if killed by melee, bullets or lasers. Spores/Blobbernauts cause shock on hit. | Takes 25% more Fire damage, and full brute |
| Networked Fibers | 20 Brute, 15 Burn | Can only expand manually (by clicking). Can only expand next to core or nodes. Manual expansion near core/node movies it to that tile. Core regenerates 2.5 times faster than other strain types. Nodes and core produce extra resources instead of producing blob tiles. Blob Tiles do not become weak outside of areas of influence (Weak blob from Spores remain weak until moved over) and are cheaper to place. | N/A |
| Pressurized Slime | 15 Brute, 10 Oxy, 25 Stam | Releases water when hit or killed, 25% less damage from Fire. | 30% more damage from Slash/Piercing |
| Reactive Spines | 5 Brute, 25 Armor and Bio-Resist ignoring Brute Damage | Attacks nearby area when hit with melee attacks, Crew Pain is enhanced | N/A |
| Regenerative Material | 5 Brute, 17.5 Toxin | Blob Regenerates 3 times faster than normal, Factories produce one more spore, pools generate 1 extra resource, restores Blob in areas of influence faster | Damage resistances reduced by 50% |
| Synchronous Mesh | 15 to 30 Brute damage based on nearby blobs/units. | Spreads damage between nearby blob tiles. Spores/Blobbernauts also share lower/greater damage based on proximity to other Blobs/Units | Takes 25% more damage from Fire. Damage spreading can kill tiles around main damaged tile |
| Nocturnal Infestation | 5 Brute, 10 Toxic, 15 Respiration damage | Spores harvest sleeping/crit targets for 5 additional resources (Dead crew members still free). Injects 2u of Nocturine on hit | Takes 25% more Brute Damage. |
| Reptilian Devolution | 22.5 Brute | Injects targets with 10u of Weh Juice on hit | N/A |
| Cacophonous Laughter | 17.5 Brute | Blob tiles lose slow and become slippery, attacks inject 5u Happiness, Spore Cannons fire pies. Blob Zombies laugh. | Takes 25% more damage from fire. |
| Hematological Nightmare | 15 Slash, 2.5 Toxic | Injects 5u of Razorium on hit | Takes 25% more Slash damage. Bleeds when hit |
| The Overmind | 5 Blunt | Spore cannons cheaper and stronger. Factories spawn 5 spores maximum at reduced cost. Blobbernauts unlocked sooner and revive after a period if corpse is not gibbed. | Blob damage significantly reduced, much more reliant on mobs/static defenses |
| Malignant Tendrils | 15 Brute, 7.5 Slash | Areas of Blob influence doubled, tiles expand out faster and weak blob is restored quicker | Pulses are 2X Slower, takes 50% more Brute damage |
| Feast or Famine | 17.5 Brute | Resource Pools have double generation speed, Spore Factories produce Spores faster. | Pools degrade and lose health over time. Time to death roughly equivilant to time it would take to produce enough resources for 2.5 pools |
| The Hungering Horror | 20 Caustic 2.5 Burn | Crew members are abducted by Spores and taken to Resource Pools to be dissolved and absorbed over 20-30 seconds. Absorbed crew give 30-40 bonus resources to the Blob. Extra DoT while standing on Blob Tiles. | Blob Zombies disabled, takes full Cold damage |
| The Beast | 20 Brute | Spores turn dead crew members into Mini-Nodes. These do not count towards Blob's evolution, but can support buildings while turning Weak tiles into Normal tiles. Crew taken by Blob cannot be revived. Blob can use converted Mini-Nodes to talk to the Crew. | Blob Zombies disabled, takes 25% more Slash damage |
| Fetid Infection | 10 Caustic, 10 Toxic, 2.5 Burn | Factories/Resource pools steadily produce Miasma. Spores release Miasma when exploding. Miasma gives Blob and its units a very slow heal over time effect similar to Rat King | Takes 25% more Fire damage, Space cleaner reduces Normal Blob to Weak Blob |
| Engines of Creation | 20 Slash, 2.5 Caustic | Expands when burned but not immune to fire. Chance of bonus expansion when spreading manually. Expands after destroying objects. Eats items/Materials on Blob and gets bonus resources with each item consumed. | Takes 50% more Brute damage, EMPs stun all units/buildings/tiles for a short period |

## Unit Variations (Mutations)

Mutations would include unique alternate upgrades to encourage more variation in a Blob's strategy and give them more freedom in how they choose to adapt to the Crew's tactics. This would be a choice given to the Blob when they evolve to the next stage, and is applied once the research period is complete letting them choose between two distinct upgrades for each Phase. Preferably these should tie into some mechanical core of the Blob that provides a more horizontal upgrade. Vertical stat increases should be handled by the Evolution mechanic so this remains a distinct feature. Generally balanced between an Offensive upgrade vs. a Defensive/Economy upgrade

These should tie more into the idea of the Blob "Evolving" to respond to the threats it's facing as it attempts to take over the station. These are more specific bonuses to give to a Blob equivilant to a Nukie picking their tools, or a Wizard their spells. These help to give the Blob more specific ways to vary their strategy over the course of a round. Dealing with heavy armor? Piercing Blobbernauts. Economic issues from crew quickly clearing Blob tiles? Creeping Contamination. No gravity? Floating Filaments.

IE: The Blob researches Metaphase and gets to choose between:
- *Pressurized Glands*: Gives Blob Zombies a ranged attack similar to the Spore Cannon (Five ammo max, 2 damage, 10% slow per hit, regenerates 1 ammo every few seconds)
- *Creeping Contamination*: Spreading Blob costs 1-2 less resources per tile.
The Blob researches Anaphase and gets to choose between:
- *Floating Filaments*: Blobbernauts have greater air control in Zero G.
- *Split Spores*: Spore Cannons now fire a spread of three projectiles per shot in a spread pattern.

 **Alternate examples**

- *Reinforced Pathways*: Code/Node pulses now happen on a shorter, more frequent timer. Can be two pulses active at once.
- *Budding Factories*: Factory's Spore Cap upgraded by 2, Spores cost 2 less resources.
- *Fermenting Storage*: Storage Blob now produce resources at 1 every 6 seconds. Cannot be upgraded.
- *Mobile Factories*: Factories turn into Blobbernauts when ability is used. Blobbernauts now produce Spores at the same resource cost/rate/cap of the factory it was formed from. Upgrade is not retroactive
- *Rigid Tendrils*: Solid and Reflective Blob gain the Reinforced trait, but cost 1.5x more.
