# The Blob

| Designers     | Coders        | Implemented | GitHub Links |
| ------------- | ------------- | ----------- | ------------ |
| (SS13), ActiveMammoth | ActiveMammoth | No          | TBD          |

## Overview
The Blob is a major conversion antagonist which poses an existential threat to the station and its crew. It's an amorphous mass of ooze that rapidly expands to encompass an increasingly larger area until it has fully consumed the station or the station's nuke blows up. Crew will be forced to fight it to prevent it from spreading far enough that it reaches critical mass where it becomes unstoppable and seals the fate of every crew member still aboard the station.

It already exists in Space Station 13 and I seek to merely bring it to Space Station 14. SS14 is severely lacking in interesting ghost roles and needs more antagonist variety. I believe the Blob is a good answer to both of these problems. It has an interesting premise, gets the whole station involved and will have interesting mechanics for those who play as the blob and those who fight against it. Furthermore the Blob has the capability of converting dead crew members into its own forces which keeps players engaged rather than forcing them to spectate.

## Features
The Blob is not a round-start antagonist. Instead it will spawn discretely from a random midround event similarly to the Ninja or Dragon. Rather than having a predetermined spawn point, once the Blob's ghost role is selected by a player, they will be able to move around the map freely as if they're a ghost and select a tile that will serve as their spawn point. Alternatively, the player will spawn in at first as a Blob-infested mouse, which will transform into the Blob on the tile where the player chooses to sacrifice their mouse form. Either method allows for the Blob to pick where it wants to spawn which is an important part of the Blob's strategy.

The Blob will start out very weak and vulnerable. It has a limited set of resources at this beginning stage and its base passive growth is slow. At this stage the Blob wants to stay hidden from the crew as it begins to grow. If crew happen to find the Blob at this stage it can be easily killed if security is notified. This plays into the Blob being able to select its starting point. By determining where it starts, part of the fun is finding the best spot to begin - one that is well defended, far from crew presence and tucked away in the shadows hidden from prying eyes. This establishes a clear counter-play to the Blob: keeping an eye across the station. The AI will be one of the best weapons against the Blob as it can quickly spot them if they chose a poor hiding spot where the AI's cameras are looking.

The Blob is composed of a variety of generic and special Blob tiles which are placed down by its abilities. The first Blob tile will always be a Blob Core which serves as the brain of the Blob. If the Core is ever destroyed, the Blob will die. The Blob's primary goal should be to protect its Core by growing around it and covering up any vulnerabilities. This can be achieved by basic Blob tiles which will block movement of objects and projectiles which don't belong to the Blob. All Blob tiles are able to be damaged and individually destroyed. Crew will likely have to cut a path into the Blob in order to reach the Core and ultimately kill the Blob for good. If the Blob dies while other Blob tiles are still present, they become wilted and present no threat anymore.

The Blob can make direct attacks against adjacent entities through its generic blob tiles. Additionally the generic blob tiles will automatically expand and attack adjacent structures and objects. If the Blob player attacks an empty tile, the Blob will grow a generic tile there. Thus the Blob can't just grow wherever it chooses on the map but must expand as one immense mass. If Blob tiles are cut off from the Core, they should wilt until they're reconnected. The Blob's vision is limited to a range around its farthest reaching tiles. When making direct attacks or expansions the Blob must expend some of its Resource (proper name TBD). It starts with a small amount of its Resource and the Core passively produces Resource over time. This prevents the Blob just completely enveloping the station immediately by pacing out its growth and making them prioritize ways to accumulate Resource instead of just rampant unstable growth.

The Blob has special tiles as well beyond its generic tiles each with their own special purpose. All special Blob tiles replace generic Blob tiles by default and must be spaced out from each other by a unique amount depending on the type of tile. Spacing out prevents the Blob from making every tile a special tile, enforcing that most tiles are generic Blob tiles. Special Blobs also cost far more Resource typically than placing new generic Blobs.

- Blob Core
  - This tile is the brain of the Blob and must be protected at all costs for the Blob to remain alive.
  - While alive it is responsible for the activation of special Blobs within a certain range of tiles.
  - Any of the special Blobs outside of this range won't be activated unless they're covered for by another Core or Node Blob.

- Strong Blob
  - This Blob is a variant of the generic Blob that has more health, higher damage resistances, immunity to fire and blocks out the atmosphere.
  - Doesn't require to be spaced out from each other.

- Reflective Blob
  - This Blob is a variant of the strong Blob that will greatly increase the chances of reflecting projectile attacks back towards their shooter.
  - Doesn't require to be spaced out and can only replace strong Blobs instead of generic Blobs.

- Resource Blob
  - This Blob produces a steady income of Resource over time.
  - This tile allows for accelerative growth as the more are placed down the faster the Blob will be able to grow and expand out its tiles.

- Node Blob
  - This Blob serves as an extension of the Core's abilities without being the actual Core.
  - This allows for the Blob to extend its reach further over the station as it grows beyond the initial edges of its borders provided by the Core.

- Factory Blob
  - This Blob creates Blob Spores passively over time up to a maximum.
  - Blob Spores are weak minion entities that serve the Blob and which the Blob can command and order around.
  - Blob Spores can exit outside of the main mass of the Blob allowing them to attack crew who're wise enough to stay away from the Blob.
  - Blob Spores explode into a cloud of poisonous gas when killed.
  - Blob Spores can take over the corpses of crew members, turning them into Blob Zombies.
  - Blob Spores can't be player-controlled but Blob Zombies are played by their body's owner or as a ghost role for anyone to take control of.
  - Blob Zombies are stronger than the Blob Spores as they utilize the health, armor and damage of the infected corpse.

- Blobbernaut
  - Not a Blob tile but a special minion unit the Blob can create by expending Resource as a direct action, spawning them on a Factory Blob.
  - Each Factory Blob can only spawn one Blobbernaut at a time.
  - Blobbernauts are much stronger than the Blob Spores in terms of health and damage but are slower.
  - They take damage over time if they leave the boundaries of the Blob, making them a purely defensive unit meant to ward off aggressors rather than go on the offensive.
  - They also slowly die if their Factory Blob from which they're spawned is destroyed.
  - Blobbernauts are always a ghost role.

The main Blob player, or the Overmind, can communicate with all of its minions through a Blob Hivemind chat which is only accessible to the Blob and its minions and is only understood as mere grumblings to any crew or other entities listening in. This allows for the Overmind to strategize with its minions and for its minions to act as extra eyes and ears to report on crew attempts to attack the Blob.

Ten minutes after the Blob spawns, or after the Blob grows over a specific percentage of the station, CentCom will make an announcement informing the crew of the Blob's presence on the station. While the Blob is still alive, the evacuation shuttle will not depart if it's already present and cannot be called otherwise; CentCom demands the Blob be dealt with lest it get aboard the evacuation shuttle and infect CentCom as well. This cements the Blob as a life-or-death major antagonist pitting them against the whole crew. Should the crew prove incapable of dealing with the Blob, CentCom will start the nuke timer either thirty minutes after the Blob spawns or after the Blob grows to double or more the percentage at which the announcement was made.

Once the Blob has grown large enough to encompass a certain percentage of the station, it will have reached a 'Critical Mass.' This is effectively the win condition for the Blob. At this point, all Resource costs are negated and automatic expansion rapidly increases, allowing for the Blob to endlessly expand over the station's infrastructure and crew. By this point the nuke timer should be counting down already; if the Blob is quick enough, they can destroy the nuke before it blows up to secure the ultimate victory, but either way the round is effectively over and the Blob will win even if the nuke does go off. If the nuke goes off before the Blob reaches Critical Mass, then it is a defeat; the Blob must reach Critical Mass to secure its victory.

The Blob should have multiple quality-of-life abilities such as one to return its camera over to the Core and the necessary abilities to rally and indirectly control its Blob Spores. The Blob should have one more ability that will allow it to swap its Core with any of the Nodes for a Resource cost. This allows for the Blob to reposition if its original Core location is under attack and in threat of being destroyed.

In Space Station 13, the Blob can choose between multiple different chemical types which it's composed of when it spawns and it can change the chemical for a Resource cost midround. This is a planned feature but I believe is unnecessary for the initial Blob to be out. Depending on how difficult this is to achieve in comparison to the other mechanics of the Blob this might change.

## Game Design Rationale
The Blob aligns with all of the core design principles in addition to being a historical antagonist being ported over from SS13 to SS14.

- Chaos
  - The Blob's mere existence on the station will devolve the station into pure chaos as the crew have to rapidly shift gears to deal with this existential threat, similarly to the presence of Nuclear Operatives.
  - The Blob has numerous weaknesses and strengths which ensure there's no perfect solution to defeating the Blob while the Blob has no perfect solution to defeating the crew; both sides can screw up.
  - How you choose to react to the Blob might vary:
    - you may rush to aid in containing it
    - you may be more self-interested in survival and decide to abandon ship before it's too late by building a shuttle or taking cargo's ship
    - you may continue your regular duties as if there's no problem with expectations that the rest of the crew has it handled, etc.

- Seriously Silly
  - The Blob's presence is a horrifying one: this hostile alien cancer that endlessly grows and infects everything around it and that's slowly spreading across the galaxy.
  - Given that Nanotrasen has it classified as a 'Level 5 Biohazard' implies that this isn't the first time Nanotrasen has dealt with a Blob before.
  - The Blob also explains the presence of the nuke on the station, which is itself very terrifying in the sense that a nuclear weapon is stored on board *just in case* of this monster showing up.
  - Yet the Blob is also silly in it being called 'the Blob' and the sheer grimness of it makes it funny in an out-of-character sense.
  - The Blob is really only scary in-character since it definitely, absolutely doesn't exist in real life.

- Dynamic Environment
  - The Blob is a very dynamic antagonist in both sides having to come up with a unique plan depending on the situation the station is in.
  - Tactics, proper equipment and player skill will all play an immense factor in the determination of who comes out on top.
  - The Blob changes the environment by becoming the environment.

- Intuitive Inter-Connected Simulation
  - The Blob isn't realistic in any capacity and isn't trying to be whatsoever.
  - The Blob's mechanics, while more complex and significantly different from the rest of the game, should be intuitive for players to understand easily even during their first round so long as it isn't cut short.
  - As it is only a midround ghost role event, nobody will be starting as it without any realization beforehand of what they're signing up for.
  - The Blob interacts with the other systems present in the game such as combat and chemicals.

- Player Interaction
  - The Blob has so much player interaction that I debated not even including this because I don't feel like I need to explain if you've read everything up to this point.

- Player Agency
  - The Blob has multiple options as do the players in how they respond to the presence of the other.
  - The Blob may decide to expand slowly at first to reserve its Resource up to the maximum capacity and then rapidly expand all at once or...
  - The Blob may try to be hyper-aggressive and kill as many crew as possible to lessen their enemies while stretching themselves thin and vulnerable, etc.
  - Players can choose between deciding to work together to contain it, escaping before they get killed, continuing their normal job, etc.
  - Once the Blob is able to change its chemicals, there'll be no one surefire meta approach to defeating the Blob as it can adapt to whatever methods the crew will be using.
  - And the crew, of course, can adapt to its methods as well.

The Blob provides enjoyment in being a unique experience in both playing as the Blob and fighting against it as even if you die, you will still be able to play, just for the other side. Since it'll be a significantly rare event, it won't become an annoying omnipresent round threat. The Blob starts out weak so it doesn't take over the round immediately; it escalates over time if the crew isn't dealing with it. The Blob has zero incentive to be friendly and the crew has no incentive to be friendly towards it because of the immense threat it poses to the station's existence. Due to the sheer size and scale of the Blob, the battle between it and the crew will take place over an extended duration of time and not be over in one small fight.

The Blob is easily discoverable once it spawns; part of the initial strategy of the Blob is finding the best place to hide. Counterplay involves what the crew or security should be doing anyways: keeping an eye out across the station for potential issues. Information for how to play and fight against the Blob should be easily found in guidebooks; the Blob, being a major antagonist, and not being a standard character, should have no administrative rules regarding how it is to be played aside from preventing friendliness. The Blob should be fun to play as and to lose as and the same for the crew; each side always has options available and alternative routes to take to achieve victory. The Blob enhances player cooperation as it forces the crew to band together as one to defeat this monstrous foe threatening them all.

## Technical Considerations
Yes.

The Blob is a very unique and complex antagonist in comparison to everything else. Blob gameplay is similar to RTS or real-time strategy games. It'll need new systems for the Blob tiles and may require some reworking of actions, new chemicals, etc. Most sprite work is already done since the Blob exists in SS13 so long as licensing isn't an issue. The Overmind of the Blob should be able to reuse the AI's point of view as the behavior is similar.
