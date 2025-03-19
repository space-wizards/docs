# Virology

| Designers | Implemented | GitHub Links |
|-----------|---|---|
| AjexRose  | :x: No | TBD |


## Overview
A replacement/reintegration of virology that hopefully isn’t as bad as before.

## Background
Diseases were removed a while back due to the fact that they were static threats, easy to counter in terms of avoiding infection, and being easy to cure with either having to drink a specific reagent or sleeping.
By making diseases less static, and being able to provide medical with both reactive and proactive measures to prevent outbreaks, we could see virology return back to space station 14.

## Features to be added

### Disease 2.0
A disease would be randomly generated with different symptoms, and methods of transmission. These diseases would have 3 primary factors
- Transmissivity (T-Score)
  - How easily can the disease infect a new person
- Severity (S-Score)
  - What the impact of the disease is on the host’s body
- Lethality (L-Score)
  - How deadly a disease can be if left untreated.
- Resistance (R-Score)
  - Determines how difficult a disease is to cure

When a disease event begins, it will randomly generate score points(collectively referred to as Disease Score) for each of these, before choosing symptoms.

----------------------------------------------

Example Workflow:
1. Disease Event Marker Begins
2. The randomized disease receives 5 T-score, 4 S-score, 1 L-score, 1 R-score
3. Disease randomly selects symptoms within parameters
4. Disease gains Coughing, loses 3 T-score, 1 S-score
5. Disease gains Vomiting, loses 1 T-score, 2 S-score, 1 L-score
6. Disease gains antibiotic resistance I, loses 1-R score
7. Randomly select crew to infect

----------------------------------------------

A weaker disease should be able to be flushed out on it’s own, much like real world diseases, in order to provide the possibilities of a quarantine being as effective in low stake outbreaks as they are in high stake

Certain symptoms should be exclusive to certain species, and other species should have unique symptoms (A slime wouldn't complain about heartburn because they don't have a heart, etc)

### New Tools
Now that a new disease is out and about, how does medical stop it?
Medical will first have to start off by diagnosing. Diagnosis begins by simply observing the patient, listening to them list their symptoms, finding the ones they don't know about. Afterwards, a doctor would interact with the Disease Catalog Console (Referred to as the DCC), and input known symptoms regarding the disease, along with a vial of infected blood.

Once all symptoms are inputted in, the computer’s system will check with the disease and all its symptoms. For each correct guess, it will provide a portion of a recipe for a randomly generated reagent that can act as a cure.
Doctors would also have access to petri dishes, which they would be able to use to store samples of the infection for later, or replicate the disease for testing, or even mutation.


### Randomized Reagents
For each disease a reagent can cure it, however the recipes are randomized, and are dependent on finding the proper symptoms for a cure.
All cures require a new reagent “Penicillin”, which can be made or purchased through cargo, as a key ingredient. Through penicillin and the Disease Catalog Console, medicine would be able to cure diseases.

----------------------------------------------

#### Example Workflow 1:
1. Infected blood vial is inserted into the DCC
2. Patient was suffering from severe coughing, and light chest pains
3. Doctor selects Coughing II and Chest Pains I on the DCC
4. DCC processes for a few seconds
5. DCC prints out a paper akin to:

—-------------------------------- 

COUGHING II: ETHANOL (5u), OXYGEN (5u)

SEVERE CHEST PAIN I: SUGAR (10u)

—---------------------------------

6. Chemist mixes 30u penicillin, 5u Ethanol, 5u Oxygen, 10u Sugar
7. Randomize Reagent Cure: EO-S-1 is created
8. Have infected drink reagent
9. Infected is cured

----------------------------------------------

#### Example Workflow 2:
1. Infected blood vial is inserted into the DCC
2. Patient was suffering from severe coughing, and light chest pains
3. Doctor selects Coughing II and Chest Pains I on the DCC
4. DCC processes for a few seconds
5. DCC prints out a paper akin to:

—--------------------------------

COUGHING II: ETHANOL (5u), OXYGEN (5u)

SEVERE CHEST PAIN I: SUGAR (10u)

—---------------------------------

6. Chemist mixes 30u penicillin, 5u Ethanol, 5u Oxygen, 10u Sugar
7. Randomize Reagent Cure: EO-S-1 is created
8. Have infected drink reagent
No Effect
Investigate a different patient for new or different symptoms
Repeat

----------------------------------------------

Different R levels would require more complex cures, a cure for a R-1 disease should not be able to cure a R-4 disease.

If a doctor applies a cure that is too weak constantly, a disease should have the chance to mutate to a higher R level.

If a doctor applies a cure that is too strong constantly, the host should suffer as a result, encouraging accurate medical treatment.

### Mutation
A disease is not stagnant in it’s nature. Randomly, whether it be in a petri dish or in a host, a disease should evolve. In this state, a disease should gain, or lose certain disease scores. This means a disease would be able to gain or lose symptoms.

Medical would have access to a bio-mutator. This mutation device would allow virologists or doctors to create a safe space to mutate diseases without having to irradiate or plasma burn themselves.
A bio-mutator would be able to use several resources from the station in order to create different kinds of mutations in diseases.
- Uranium
  - Increases the rate of mutation for a disease
- Plasma
  - Increases the chances that a mutation will be more extreme, both in the loss and gain of disease score.
- Bananium
  - Increases the chance for rarer and more siller symptoms

### Resistance
Mentioned earlier, a disease would have a Resistance score. Resistance score can be used to antibiotic resistance, which has gameplay from the earlier mentioned difficulty in creating a curing reagent. A R-Score of 1 could make a disease have “Antibiotic Resistance I”, which would be a non-complex cure, even penicillin on its own may be able to cure it. A R-Score of 5 could have “Antibiotic Resistance V”, which could need a cure so complex you would need the entire station to devote its resources unto making it.

However, that’s not the only resistance a disease can have. A disease could be heat resistant, meaning that a fever or a sauna couldn't cook the disease into uselessness, and you wouldn't be able to easily destroy samples in petri dishes. A resistance to the cold could mean players wouldn't be able to freeze a disease to prevent mutations

In some cases a disease could even have vulnerabilities to heat and cold, or other reagents. While reducing it’s resistance, having vulnerabilities can allow diseases to have even more symptoms

A disease should never be totally immune to everything, it should always have a weakness.

### Proactive Measures
Now, what does a virologist do while there are no disease outbreaks? They help the station in preventing them of course! 
A virology lab would start out with a fridge containing several inert samples, extra petri dishes, and a bio-mutator.
Once a disease is well mutated, they can test on monkeys, space fauna, or ethically sourced humanoid volunteers/the clown. They can then gather blood from the infected test subjects and gather the fragments of cures, for when an actual outbreak begins, there are parts of the puzzle already available.

### Immunity and Vaccination
Crew should have a randomized chance to be immune from whatever disease outbreak occurs, and that immunity should be utilizable by virology to create vaccines. When a immune member of crew is found, a vial of their blood and a vial of infected blood would be placed in a Vacci-Fab, if the crew member is truly immune and simply not infected, then the vacci-fab would print a randomly generated reagent recipe for creating a vaccine.

The complexity of the vaccine should pair with the Antibiotic resistance level (ie, the harder it is to cure, the harder it should be to vaccinate against)

A vaccine however, is not the cure, and should not be treated solely as such.

### Cross Departmental Interaction
#### Science
Science should be able to research technology for virology, allowing them to print more petri dishes or bio-mutators on their own.
In addition a set of research technology could be available in the civilian branch called “Symptom Catalog Update”, which when researched, randomly selects a random amount of symptoms to provide more information on. This information can be found in the DCC, and ranges from pre-providing the symptom’s reagent component, or giving a DNA string of anyone who may be immune to a disease with that symptom.
This should be researchable multiple times, but should never provide every answer.
#### Cargo
Cargo should be able to order medical more penicillin and virology supplies, along with hazmat suits for when outbreaks occur.
Salvage would be able to yield exotic new disease specimens from salvaged debris
####  Service
Certain diseases when in petri dishes should be able to thrive and die from certain reagents that are not possible for chemistry to synthesize, like booze from the bar or mushrooms from hydroponics.

## Game Design Rationale
Consider addressing:

How does the feature align with our Core Design Principles and game philosphy?
What makes this feature enjoyable or rewarding for players?
Does it introduce meaningful choices, risk vs. reward, or new strategies?
How does it enhance player cooperation, competition, or emergent gameplay?
If the feature is a new antagonist, how does it fit into the corresponding design pillars?
Roundflow & Player interaction
Consider addressing:

At what score in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
Which department will interact with the feature? How does the feature fit into the design document for that department?

### Interactions with the design principle
 - Chaos
   - curing an outbreak relies on medical being able to be through with their investgation and not getting symptoms mixed up with one another in order to create a cure.
   - Similarly to botany, when mutating a disease, medical plays a game of chance. With every attempt to get a useful mutation, they risk gaining a mutation that could lead to an outbreak.
 - Seriously Silly
   - Not all symptoms and diseases are 1:1 versions of the real world or sci-fi diseases. Equally silly diseases like one that makes you crave bananas or makes you talk like a machine, outbreaks of such diseases are comical in nature due to the sheer absurdity.
 - Dynamic Environment
   - A virology lab can be set up anywhere a person needs to, whether it be in a proper virology bay or in the maintence halls. You dont even need a petri dish or bio-mutator, as keeping a infected host like a mouse or a monkey alive long enough will result in mutations naturally occuring given enough time. 
 - Intuitive and Inter-Connected Simulation
   - The intention is for the UI of the involved machinery to help guide players through trying to find a cure/vaccine. UI on the DCC would mention needing infected blood and a selection of symptoms, the Vacci-Fab would tell players to bring infected blood and testing blood, diseases would always have a different appearence in petri-dishes to show mutations.
 - Player Interaction
   - Find a cure or vaccine for a disease is something that is quite literally impossible for a single player todo. They will always need to interact with other players to ask questions, draw blood, and test both cures and vaccines.
   - While mutating a disease is more isolated, players will still need to interact with other players for help if they want to achieve all of what disease mutation can offer.
 - Player Agency
   - Diseases creates a choice for players in numerous ways. For non-medical; if a outbreak starts, do they want to go and get tested for the disease and risk contracting it? If they do get infected, do they just hope the disease burns out on it's own and risk spreading it, or do they remain in medical?
   - For medical players, they have to chose on what they want to prioritize before and during outbreaks. Do they want to look for a cure, or a vaccine? Who needs to be examined first? Which members of crew will recieve the first doses of the cure? 
   - Before an outbreak, medical players have to figure out which symptoms they wish to research first, do they want to get the harmless and easy to mutate diseases, or the dangerous and difficult to mutate diseases?


### What makes Virology enjoyable/rewarding for players?
Virology is rewarding in which it can help bring a quick end to a crisis. It allows players from across the station and in medical to work together in solving a problem in a manner that isn't combat related.

### What meaningful choices (risk vs. reward, new strategies) does Virology introduce?
- Controlled Mutations
  - in a virology lab, players would have to make a choice on what mutations they would want on a disease? (as mentioned in player agency), this would mean medical would have to gamble on what possible diseases may appear in the future, and which symptoms they want to have information about first.
- Treatment
  - When a outbreak does occur, medical should always be given the option of devoting their time into a cure for the infected, or a vaccine for the uninfected. 

The strength of the disease and it's impact on infected hosts will change how both of those choses are made.

Antagonists will also have new options available as well during outbreaks, risking infection themselves to be able to do their objectives while other players are quarantining or in medical.

### Roundflow & Player interaction
[To be improved]
Here is a example of the stages of an outbreak if the station is able to resolve it, and with slight modification could count as the stages of vaccination too

1. Initial Infection: A small set of crewmembers are infected by the disease, they may consider it nothing, or not realize it
2. The Spread: The disease spreads to more members of crew, and people start to notice it
3. Diagnosis: Some players who are infected will go to medical as the disease progresses
4. Trial and Error: Medical inputs symptoms into the DCC, and tries several attempts to cure the outbreak
5. Success: Medical has found a viable compound to cure the disease. 
6. Mass Production: Chemistry and the station work together to make enough of the cure to provide to the whole station.

Here is a example of the stages of an outbreak that the station couldn't handle
1. Initial Infection: A small set of crewmembers are infected by the disease, they may consider it nothing, or not realize it
2. The Spread: The disease spreads to more members of crew, and people start to notice it
3. Diagnosis: Some players who are infected will go to medical as the disease progresses
4. Trial and Error: Medical inputs symptoms into the DCC, and tries several attempts to cure the outbreak
5. Mutation: the disease mutates, whether it be because medical used a cure too weak too many times, or it evolved on it's own to take more lethal effects
6. Further Spread: The disease now mutated, spreads amongst the crew faster
7. Casualties: Crew begin to die from the disease, slowly or quickly
8. Evacuation: Medical could not find a cure, and as a result a large amount of crew are dead or unable to leave medical. Evacuation is called.

Overall, a outbreak should not be too uncommon, at least one major outbreak every few rounds. It should be a rare occasion in which there is a extremely lethal outbreak that occurs.

## Administrative & Server Rule Impact (if applicable)
[To be improved]
Admins would likely have to deal with players who are purposely spreading any disease they can, or medical interns trying to min-maxx the most deadly disease for spreading

## Technical Considerations
[To be improved]

For the randomized reagents, the entire chemistry system would need to be refactored to make chemical reagents entities instead of prototypes
-INSERT UI EXAMPLES OF NEW MACHINES-
