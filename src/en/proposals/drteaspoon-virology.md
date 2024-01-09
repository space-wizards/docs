# Feature Design: Virology

## Overview
A simulation of RNA, plasmids and genomes. Medical virology department gets tools to extract virus RNA, investigate the virus, determine it's weakness and deliver not only cure but also vacine.
Using same tools, allow bad actors to synthesize and modify viruses to suit their needs.
Possibly even create positive/neutral effects usign viruses as a vector.

## Goals
Bring back virology into SS14 in fun and interactive way. Open as large design space that lets you simulate things from common cold to cronenberg zombie outbreak.
Some extra steps in making cure and vacine to give plausible deniablity for printing and carrying virus injectors.

## Gameplay

### Swabs
All starts from humble swab. When player uses the swab on a character, they can get one of the active viruses in the body (if multiple, one at random).
Player can then insert the swab to virus workstation to get to the actual meat of the new mechanic.

### Virus Workstation
Virus workstation provides UI to analyze and modify a virus.
When swab is inserted, window in the virus workstation are populated. This window has the whole RNA string, a long string of A,C,G and T symbols. We can call this the 'RAW' window. The string is interactable in a way that you can click anywhere on the string to place a marker. After placing the marker you can press analyze to start analyzing anything from begining of the RNA string to the marker. The length of the string 'selected' determines the duration of analyzing.

If the selected length is too small, the analyzer gives out error and you end up with no results. If the length contains one valid segment of RNA that serves some purpose, the segment and it's relevancy is revealed and the searchable area is moved to start from after that segment. This means you can work your way through the RNA efficient manner if you've worked on RNA this round and know segment lengths by heart (or by taking notes).
There are always same amount of segments that encode some key data with same length, but they can be in any order. **Order and genome to effect dictionary is randomized at start of the shift. Only thing that remains constant is that Symptoms[1]** The genome lengths are longer than nessesary to either enable variation and to create dead ends.

The segments are:

```admonishment {note} "{Infection Vector}"
 Segment that tells the game how to infect others. Has four valid states.
 - Infect by wet surfaces (share same glass, have their blood spill on you)
 - Infect by touch
 - Infect by air (radius)
 - Infect by dry surfaces (create short lived trail of touch triggers)
Genome length is 3.
```

```admonishment {note} "{Unactivated Symptom}"
This is to simulate coughing, detoriaration of health etc. The unescapable effect of the virus.
Genome length is 12.
```

```admonishment {note} "{Activation Condition}"
The goal the virus is trying to reach. This can be anything from specific heat treshold, particular gas in lungs or chemical in stomac. For zombie infection this is death of the victim.
Once activation condition is reached, the Activated symptom is applied to the victim and virus is considered `completed` and is no longer processed.
Genome length is 6.
```

```admonishment {note} "{Activated Symptom}"
The permanent effect of the virus. If your patient reaches this there is no curing them. For zombie infection this is the moment they turn into zombie.
Genome length is 12.
```

As you discover segments, you can also start hand editing by clicking the segment. This effectively text editing mode lets you copy a valid segment to your PDA notes or paste something from previous notes.

Final interaction on virus workstation is the synthezie button that lets you print out injector of the virus. This injector is not only used to iject the virus but also to use the other machines related to virology.

### Vacine synthezizer
When virus injector is inserted, creates vacine for the virus. Vacine only works if the target does not yet have the diseace. It effectively gives them the virus but marks the virus as `completed` instead of starting all of the symptoms normally.

### Cure analyzer
When virus injector is inserted, print out possible cures. The cures are actually string search of the RNA from small randomly generated dictionary of 10 length genomes. If any of those match, the virus can be cured by that particular method. If no cure is viable, a new cure is generated from random position of the current RNA.

### Immunities
Each species are given random 15 length genome string that makes them immune to any virus that expesses those 15 genomes in contigious segment.

## Structs
### VirusData
Contains RNA and decoded effects of the RNA. Has methods for decoding and encoding between RNA and the various enums and prototypes related to it.

## Enums
### Infection Vector
### Activation Condition

## Prototypes
### Symptom
Both activated and unactivated symptoms use same prototype structure. List of components to add or remove.

## Components

### VirusManager
This component handles storing the data of active and cured/completed viruses. 

### VirusContainer
Virus container stores data of single virus. Used in injector, analyzer, vacine synthesizer and infected solution containers. Contains just the RNA string.

### VirusInjector
Enables use of virus container on entities with solution container. Doesn't interact with the solution container but adds VirusContainer on the entity or adds to VirusManager component.

### VirusActivationCondition
Component to mark pending activation of a virus.

## Systems
### VirusManager
Handles the stages of virus in characters/mobs.

### VirusActivationManager
Responsible for checking when to move from unactivated virus to actived one. only checks for `VirusActivationConditionComponent`

### VirusInjector
Handles interaction with other entities.

### VirusManager
Handles the stages of virus in characters/mobs.

## Inspirations
Real world. Hex editing. The Thought Emporium
https://www.youtube.com/watch?v=20vwKHfbVvY&list=PLZLsjPxmF1BEI5CReoklVP4u84kMkjIZp

## Requirements
Just do it?

## Notes
```admonishment {note} "{[1]}"
While appears in other places along plasmid, ATG in real world RNA always appears at start of a protein. We can put some education and give slight hint to where the different segments are to experienced players.
```
