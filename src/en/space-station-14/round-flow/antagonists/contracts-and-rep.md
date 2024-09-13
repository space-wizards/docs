# Contracts and Reputation

| Designers | Implemented | GitHub Links |
|---|---|---|
| AjexRose | :x: No | TBD |

## Elevator Pitch

   Reputation is a system of risk and reward meant to replace the current objective based system that current antagonists utilize. However, it can be broadened for more uses.
Designed to give antagonists set "contracts" that can be completed or rejected. Completed contracts will increase the player reputation while also granting
them additional telecrystals. The higher a player reputation is, the more access to more powerful forms of contraband they have. 

## Reputation

  Reputation is a internal system that keeps tracks of what an antagonist has done. The more objectives an antagonist completes, the more reputation the antagonist has, and the more the antagonist has access to. 
A player's reputation when they press "c" or which ever button allows a player to view their objectives, they would be able to see their contracts and reputation. Reputation should range from 0 - 100, 
with 0 being the base reputation for a player while 100 is the highest reputation a player can earn.

There are 5 states of reputation, each state contains new benefits along with previous benefits. 
(this is subject to change depending on balancing and concerns)
| Rep Level | Contracts Veiwable | Objectives | Unlocked Purchasables |
|---|---|---|---|
| 0-20 "Unknown Agent" | 2 Contracts | Low Risk | Stealth Gear + Objective Items |
| 20-40 "Preferred Pawn" | 3 Contracts | Moderate Risk | Melee Weapons + Chemicals |
| 60-80 "Reputable Insider" | 3 Contracts | Moderate Risk | Side Arms + Explosives + Allies|
| 80-100 "Reliable Contact" | 4 Contracts | High Risk | Long Arms + More Powerful Explosions + Hardsuits |
| 100+ "Syndicate Operative" | 4 Contracts | High Risk | Station Destructive Items + High Power Weapons |

All traitors, no matter their reputation, can purchase additional ammo + surplus crates. 

## Contracts

  Reputation can be increased by completing contracts. These contracts act similarly to current objectives. However they contain two options. The first option would be a always available :x: option that when selected
removes the contract from the player and starts a 15 minute count down until a new contract is found. The second option is a :white_check_mark: option that only appears when an contract is completed. 
When selected the contract will dissapear, the player will be granted 5-10 reputation, additional telecrystals and enter a 5 minute refresh rate before a new contract is found.

## A Contractor's Work

Syndicate Objectives are classed under 3 different categories based on their difficulties.

Low Risk Objectives are objectives that should not get a traitor brigged for a long period of time
These objectives include but are not limited to;
- Plant Bug Objectives
  - Antagonist must plant a listening bug near a item, or location
- Minor Theft Objectives
  - Antagonist must steal minor items of a department and utilize syndicate fultons to extract them. 
- Assist Traitors
  - Ensure a traitor completes an contract. If the traitor rejects the contract, this contract will also reject, but will only take 5 minutes to refresh instead of the standard 15. 

Moderate Risk Objectives are objectives that should get a traitor brigged for a while
These objectives include but are not limited to;
- High Value Theft Objectives
  - Traitors must steal a high value object and use syndicate fultons to extract them.
- Place Tracker Objective
  - A syndicate tracker must be placed on a character person. Whether it be directly on them, in their pockets, or inside their bag. The tracker can be removed without uncompleting the contract
- Corporate Espionage
  - Utilizing a syndicate data-knife, a traitor must extract 1-3 researches from a science research console (Not the research server).
- Neutralize Targets
  - The traitor must kill a target, this target can be a member of crew or another traitor. The target does not have to be gibbed. If the target is revived, the contract remains complete.

High Risk objectives are objectives that should get a traitor brigged for a long time, permanently, or executed
These objectives include but are not limited to;
- Extract Target
   - a member of crew must be extracted using a syndicate sophont fulton (MGSV style)
- Siliconize Target
   - a member of the crew must be placed into an MMI unit. If the crew member's brain is extracted from the MMI unit before the contract completion button is selected, then the contract reverts to an incomplete state.
     If the brain is destroyed before the contract completion, this contract will auto-reject, but will only take 5 minutes to refresh instead of the standard 15. 
- Corporate Sabotage (Location)
   - A certain location needs to be bombed using C4 or other high powered explosives (location is selected by proximity to a warp-point or map-beacon)
- Corporate Sabotage (Machines)
   - A certain machine needs to be destroyed by the traitor. The machine can range from basic auto/protolathes to department specific machines like the sec techfab, ore processor, research server.
     Destruction counts by manual deconstruction or destruction via damage or explosion. The person who destroys the machine doesnt matter, it just needs to be gone.    
- Die A Glorious Death

## A Contractor's Tools

Traitors recieve a new set of tools labeled "Objective" and "Station Destruction" respectively.
These objective tools should never cost more then the contract value.

Objective Items
- Blood-Red Bug
   - A bug that can be placed on walls, in plant pots, or even in food. Has no effect on crew. Should make a beeping noise and have a slight glow to show where it is.
   - Is a tiny item
- Tracker Bead
   - A small bead which transmits its location should it be placed on a person. This person will always be on the crew monitor system as coords active.
   - Is a tiny item
- Syndicate Fultons
   - Black Fultons with a red horizontal strip. Shouldnt require linking to any sort of beacon, rather it deletes the item or crate thats been extracted.
   - It cannot extract humanoids or organic beings, dead or alive.
   - Is a medium sized item.
- Syndicate Sophont Fultons
   -  Black Fultons with a red horizontal strip. Shouldnt require linking to any sort of beacon, rather it deletes the humanoid or organic entity attached. Has a 1 minute timer unlike the standard 45 seconds, and makes loud beeping noises.
   -  If the person who is attached is awake, then they will not be able to move, but can free themselves with a 30 second do-after. Do-after can be cancelled with shoving.
   -  Cannot extract dead humanoids or organics
   -  Is a large item
- Data Knife
   - A knife with similar damage levels to the cybersun pen. Should be blatently obvious it is ~~a titanfall reference~~ contraband.
   - Is a small item.
- Black MMI
   - A syndicate MMI that when inserted into a chassis, automatically starts with emag'd laws.
   - It is a medium sized item

Station Destruction Items
A bit of a clarity, these items are mainly inspired by the existence of the "Delamination Crystal" from SS13. A purposeful way to cause a supermatter breach limited to antagonists which is extremely expensive.
It also reduces EMAG functionality

- The Anti-Matter Cascader
  - When inserted into the AME Controller, allows the controller to go beyond the safety limits to generate a large and destructive anti-matter explosion.
- The Particle Hyper-Acceleration Module
  - When inserted into the Particle Accelerator Console, allows the console to go beyond the safety limits to generate powerful singularity breaches and tesla-looses.
