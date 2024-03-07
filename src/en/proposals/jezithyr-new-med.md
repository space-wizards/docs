# NewMed
Modernized medical gameplay with a splash of Spacestation 13 flavor

| Designers | Implemented | GitHub Links |
|-----------|---|---|
| Jezithyr  | :information_source: Open PR | https://github.com/space-wizards/space-station-14/pull/19383 |

## Overview

"New Medical" or NewMed (Previously called WoundMed or MedRefactor) is the *full* implementation of Medical gameplay into SS14. 
NewMed aims to dramatically increase the depth of medical gameplay and simulation. It is designed around 4 core pillars: 
**Urgency of Action, Symptoms not Numbers, Depth without Complexity and No Magic Fixes**. With these in mind,
NewMed is a complete rewrite of the Humanoid Damage, Organ/Body simulation, and Current Medical Systems. The goal of NewMed is to bring the
chaos and intensity of a medical drama into the Medical Department of Spacestation 14. Additional, NewMed also seeks to add more back and forth flow to combat by 
naturally creating disengagement opportunities and incentives.


### Core Pillars
#### Urgency of Action:
- Capture the feeling of a high-intensity emergency room. Push players to make snap judgments without all the information, creating high pressure _**memorable**_ situations.
- Medical players will need to make the hard choices, who gets to live and who bleeds out on the floor... Triage will be an important skill for managing patents when shit hits the fan.
#### Symptoms not Numbers:
- Don’t give complete information on the current state of a patient. Doctors should need to diagnose the _**symptoms**_ and deduce what is causing them.
- Core stats should never directly measurable, instead rough thresholds should be given or they should abstracted behind multiple other values or descriptions. 
- For example: Instead of displaying 50 burn damage as a value, roughly describe the condition of the affected part.
#### Depth without Complexity:
- Most treatments should be simple enough for the average player/person to administer. The difficulty is figuring out which treatment to use based on the symptoms with the tools you have available.
- No Skill-checks or hidden mechanics, all the information needed for players to save themselves or others can be found in the guidebook and MediPDA App.
#### No Magic Fixes:
- Magic healing chemicals will be a thing of the past. Medical drugs will be moved into a new role, modifying/buffing/debuffing various body stats instead of directly healing.
- Everything has a cost and while ***some super-drugs may exist*** (Primarily for solo antag use), they have dramatic side-effects that make their use a strategic gamble.
- Injuries will take time to heal, bed rest or the right mixture of drugs can accelerate this but nothing will ever be instant.

## Summary of The Major Changes
### New Humanoid Damage model and changed MobState handling:
Previously damage was handled as a single hitpointPool that was then checked against MobStateThresholds to determine
if the player is dead/alive/crit. In the new system, damage is handled *per bodypart* and mobstate is handled by the newly introduced *consciousness system*.
Consciousness is a value that is tracked per body/player and it reflects how *alert* a player is, with lower consciousness 
representing being closer to passing out/falling asleep or dying. Various mechanics will affect consciousness, and ConsciousnessThresolds 
will determine *when* a player changes between mobstates.

### Wounds, Medical Conditions and Pain:
In addition to part specific damage handling, NewMed introduces part specific modifiers called *Wounds* and body specific modifiers called *MedicalConditions*.
Wounds are applied when a bodypart takes damage and apply debuffs to the body/bodypart. MedicalConditions are applied by 
medical simulation and other gameplay systems, medical conditions can be negative, positive or neutral. Wounds and some other gameplay systems can also apply
pain to the player. Pain has various debilitating effects depending on it's severity and if not managed correctly (via painkillers or other methods), 
can cause a player to pass out and in extreme cases just die.

### Healing, Treatments and Drugs:
All supported Bodyparts and most wounds passively heal overtime for a small percentage of their *current health value*, 
this means that the lower health a part is, the slower it naturally heals. To speed up healing or mitigate wound side-effects players can 
*apply treatments*. A treatment is a sequence of actions that may(or may not) require items or tools to perform. In addition to treatments players can also use
drugs/medications to accelerate healing but these have side-effects and negative reactions with other medications so a balance must be made.

### Surgery and Permanent Damage:
Once a Bodypart has taken a considerable amount of damage, future damage is taken into a second health pool called *Integrity*, this pool does not heal passive and
requires a surgical operation to restore. Similarly some extreme/advanced wounds will require surgery to treat as they will not heal on their own. 
Surgery is a game of risk/vs reward where surgeons will need to weigh the damage that the surgical procedure will cause against the benefits of the operation. 
And if that wasn't enough stress, surgeons need to make sure that pain is properly being managed with painkillers and *the patient does not wake up on the table mid operation*.

### Blood and Organ Simulation Overhaul:
Bloodstream and bleed simulation is going to be considerably changed. Bleeding is going to be *very scary* and players must act fast when dealing with serious bleeding injuries, 
however there will be new tools such as tourniquets (both improvised and manufactured), clotting chemicals, and rags/bandages. Bloodloss is also a more serious long-term issue that requires
an IV and appropriate blood/plasma donation to counter-act. Organ metabolism/simulation is also changed to use chemical reactions controlled by catalysts (called enzymes). 
Pulse, BloodPressure and HeartRate will be simulated and very important to measure when trying to diagnose a patient.

## The Detailed Explanations:

### Damage Handling and Wounds:
Each bodypart that supports wounds will have a woundable component. This component tracks the bodypart's condition using two values, Integrity and Health. 
Both of these values together act as the part's Hitpoint pool. The Health value slowly regenerates (this may be boosted by drugs/treatments) while the Integrity value does not.
Damage is applied to the health pool *first* and once it reaches zero, all future damage is taken as integrity. Once integrity reaches 0, the bodypart is gibbed
and a % of the damage overflow is applied to the adjacent parts. 

Due to the lack of targeting, _it is not currently possible to individually target bodyparts_. _Instead as a stopgap measure until targeting is implemented_, any damage that gets applied to
the ROOT bodypart (almost always the torso) will be spread using a random selection function that is slightly weighted towards the torso and head. When specific bodyparts/organs are destroyed,
such as the head/brain or torso, a player will immediately be set to dead as their body can no longer sustain consciousness/life.

Wounds are grouped in "WoundPools" that sort them in damage from 0-100, these woundpools are generic or species specific and can be reused. 
Each woundpool can be assigned with a specific damage type and scaling value. These are used to calculate which wound should be applied when 
receiving damage. Each wound is an entity that has it's behavior defined by components in their entityPrototype file,
and every wound has a severity value ranging from 0-100 that influences the componenet effects. All wound start at full severity 
and through either healing (if enabled), or treatments/surgery, their severity value can be decreased. Once a wound's severity 
value reaches 0, that wound is "healed" and is removed from the part, however wounds can optionally spawn a new wound as a "scar", when they are treated/healed.

### Mobstate Handling and Consciousness:



### Medical Conditions and Pain:


### Treatment, Surgery and Drugs:

### Body/Organ and Blood Simulation:
