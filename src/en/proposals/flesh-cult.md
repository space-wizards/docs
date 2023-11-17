# New Game mode: Flesh cult
A new game mode in which flesh cultists, feeding on station personnel and using special skills to mutate organs and body parts, must secretly prepare a ritual to summon a flesh heart, and guard it until it awakens and completely takes over the station.

## Appearance
Flesh Cult is an independent game mode, chosen by player vote or by the administration.
In this mode, at the beginning of the round, some crew members (except slimes and dion) become flesh cultists. At the beginning of the round, for every N players on the server, 1 cultist appears among them. Anyone can be a cultist except heads and securitu. 

Every time a new player joins after the game starts, he has a chance to become a cultist.

## Abilities
All Cultists have access to a special personal resource called **Flesh Points** (hereafter referred to as FPs). They can be obtained from certain abilities, and can be spent to mutate a certain organ and body parts

**Internal Mutation** - Altered internal organ. It is a subtle change, and mostly gives weak passive effects. The idea is that the features are tied directly to the organ, which will allow useful cultist organs to be transplanted to other passengers in the future.

**External Mutation** - Altered body part. In the current implementation is a non-removable item that occupies a certain inventory slot. Ideally then re-implement on the modified body part, but we decided not to touch it before the implementation of surgery.
All external mutations change the appearance of the character, making him more visible to others, and in return give powerful and active abilities.

Some mutations may only be available to certain roles or races. (special mutations for the clown!)

For each organ or inventory slot, there are several mutation options that you will only be able to choose from. These options are conceptually divided into 3 categories, but are listed together in the game:

- **Shaper**:
Mutations in this category focus on base support and construction.
- **Hunter**:
Mutations of this category focus on mobility and ranged combat.
- **Butcher**:
Mutations of this category focus on survivability and melee combat

The following are some examples of mutations. This list will be edited in the future.

Internal Mutations. Have mostly small passive effects, and can be safely obtained without fear of disclosure.
| Brain mutation's | | |
|---------|--|--|
| | Automatic | A basic mutation given to all cultists. When hunger is low, turns the bearer into a flesh monster. Gives the active ability **"Start Mutation"**, allowing you to open the mutation interface, where you can spend FP to buy mutations. Selecting a mutation triggers a long doafter with meaty sounds and special effects.|

| Stomach mutation's | | |
|---------|--|--|
| | Automatic | Allows only meat and organs to be eaten. Faster starvation. Doesn't need water. Heals from blood. Gives the active ability **"Feast"**, which allows you to gib a corpse with a delay. If the corpse was a sentient meat humanoid, the cultist gains 10 FP|

| Lung  mutation's | | |
|---------|--|--|
| Spoiled lung | Low cost | Gives the ability to healing from miasms. |
| Void Breath | High cost | Gives the ability to breathe in space. |

| Eyes  mutation's | | |
|---------|--|--|
| A cult's view | Low cost | Gives you the ability to recognize other cultists. (UI icons) |
| Second eyelids | High cost | Gives protection from flashes and welding. |


External Mutations. These mutations can be hidden by some clothing, but for the most part, their presence will reveal you as an antagonist. For this, you gain powerful active or passive abilities.
| Hands  mutation's | | |
|---------|--|--|
| Formation Tentacles | Low cost | The bearer gains the **Tentacles of Formation** ability. This ability is immediately applied to the active hand. If the active hand is free, a doAfter is triggered, at the end of which the hand is occupied by an unremovable tentacle. The player gains the Flesh Shaping ability If there is a tentacle in the active hand, a doAfter is triggered, after which the tentacle and the ability disappear. - Gives the effect of insulating gloves. - Prevents you from wearing gloves when active. - Tentacles have medium damage but high structural damage.|
| Bone Blade | High cost | The bearer gains the Bone Blade ability. This ability is immediately applied to the active hand. If the active hand is free, a doAfter is triggered, at the end of which the hand is occupied by an unremovable Bone Blade. If there is a blade in the active hand, a doAfter is triggered, after which the blade disappears. - Prohibits wearing gloves when active. - Removes handcuffs when in use. - The blade deals good damage in close combat. |
| Bone shield | High cost | soon |
| Worm hand | High cost | ranged weapon soon |

| Legs  mutation's | | |
|---------|--|--|
| spider legs | High cost | Slot boots are engaged with non-removable "spider legs". Strongly increase movement speed and give protection against slipping. |
| Suction cups | Low cost | Slot boots are replaced by non-removable suction cups. Gives protection from slipping. The character passively drinks the blood on which he stands. |

More Mutation description soon

## Flesh Formation
With the **Tentacles of Formation** ability, you can spend OP to build some structures. It can only be installed on the meat floor. Installation takes a certain amount of time.

| Construction | Time| FP | Description |
|-|-|-|-|
| Flesh floor | | 0 | You can build anywhere. Butcher's floor is the base for the future base, because all other buildings can only be built on it.|
| Meat wall | | | |
| Meat door| | | Door. Should only open for the flesh faction|
| Flesh lamp| | 0| A decorative pulsating meat lantern. |
| Flesh furniture | | 0| Chairs, tables, furniture. It's all useless decor, so it's free. |
| Connecting Brain | | 5| Flesh telecom server|
| Tumor| | 5 | Tumor Mine. When passed nearby by a creature not of the flesh faction, it bursts, slowing those around it (imbuing ipecac maybe), releasing flesh mobs. Base Defense.|
| Jaws | | | Constantly absorbs oxygen and nitrogen, generating miasmas. |
| Sculpture | | 10 | Flesh Sculpture. Once set, grows for about 5 minutes, after which it creates the role of a ghost of a powerful meat monster.|
| Heart Embryo| | | Flesh Heart Embryo. Read more about the heart in the Cultists' Tasks block|

## Objectives
All cultists have 2 objectives from the beginning of the round:

The first task is to survive. Turning into an uncontrollable monster from starvation counts as death.

The second task is to create a heart of flesh and prevent it from being destroyed

**Growing a flesh heart is a multi-step and non-fast process:**
- First, you need to set up a flesh heart embryo using the flesh building mechanic. 
- The flesh embryo needs to be fed corpses by dragging them into the embryo. The size of the corpse affects the degree of saturation. It takes a big amount of flesh to feed! Once the embryo is finally fed, it grows into a heart of flesh.
- The heart of flesh has emerged! When it emerges, all heart embryos mutate into Flesh Sculptures. All Cultists are notified in private messages that the heart has been installed. The embryo's coordinates appear in their briefing. At this point, the station's announcement system lock onto it and notify all personnel of the exact location of the flesh heart. The heart of flesh begins a 10 minute countdown of time during which it grows.
Growth is accompanied by:
  - replacement of the floor and walls with meat versions, 
  - the periodic spawning of flesh monsters around the heart.
  - pumping nearby cultists with healing chemicals. 
- At the end of the 10-minute timer, the heart of flesh grows finally, makes a powerful pulsation that turns all living creatures of hostile factions on z-level into flesh monsters >:) and releases tendons. (or kills everyone)

**Destroying the heart** causes a powerful wave of energy that kills or turns all cultists into uncontrollable monsters, and causes an evacuation shuttle with a 5-minute delay
