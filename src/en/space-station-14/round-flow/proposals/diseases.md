# Diseases

| Designers | Implemented | GitHub Links |
|---|---|---|
| Pok | :warning: Partially | Part 1: space-wizards/space-station-14#40545 |

## Overview
This document describes the mechanisms of diseases and virology.

This document focuses on viral diseases, but the implementation should also support medical systems with progressive physical conditions.

The proposed implementation may resemble those in SS13, but differs to achieve the gameplay experience described [below](#Game-Design-Rationale).

Examples of differences:
* Vaccines require less time spent by a medical personnel in one place.
* Airborne transmission routes that account for viruses in the atmosphere, increasing engineering involvement.

## Background
This design doc aims to introduce a clear, maintainable foundation for diseases that integrates with existing medical workflows and expands the responsibilities of medical personnel. The initial scope focuses on readable mechanics, predictable player tools that can be iterated on in future PRs on mutations and virus creation.

## Game Design Rationale
### Local outbreak
A disease outbreak occurs due to a predictable event.

* Disease carriers can vary (corpse, artifact, expired food, etc.) depending on the desired gaming experience.
* Diseases occur in persons upon contact with a carrier, the nature of which depends on the type of disease. The method of infection can be anything, but it must originate from the event that acts as the carrier (gas from an artifact -> airborne transmission, dirt -> contact transmission) and take into account the appropriate methods of protection.
* Diseases caused by a local event should have a low chance of infecting others so as not to provoke a chain reaction spreading to most of the station. However, this chance should not be so low that medical personnel can ignore the disease and delay treatment or [containment measures](#protection-against-spread). 
* The danger of the disease can be regulated by the prevalence of the carrier (the rarer it is, the more dangerous it can be).

### Global outbreak
Global outbreaks arise from a random station‑level event.

* Usually, the trigger should be a random station event.
* Diseases caused by a station‑level event should have a high chance of infecting others, creating a chain reaction that can spread to most of the station. At the same time, this chance should not be so high that medical personnel are overwhelmed and unable to react with timely treatment or [containment measures](#protection-against-spread). 
* The danger of the disease can be regulated by the probability and time when the event usually occurs (the rarer and further in time, the more dangerous it can be).

### Diagnostics
Diagnostics is an important measure for combating disease; it can be either comprehensive or simply warn of the presence of disease. 

Some diseases may be hidden, countermeasures should exist, such as a reagent that temporarily reveals the disease to enable targeted treatment.

#### Partial diagnosis
Partial diagnostics should warn of the presence of illness but not indicate its type or treatment, motivating more detailed examination using specialized tools. 
These include HUDs, analyzers, and crew monitoring—simple standard medical tools.

#### Complete diagnostics
A complete diagnosis should provide comprehensive information about the disease, including its characteristics and stages of treatment. Therefore, it should be performed by a stationary machine in the medical department (the diagnoser). For convenience, it can accept samples collected beforehand (e.g., a swab).

### Protection against spread
Protection prioritizes targeted mitigations that let infected crew keep playing while reducing risk to others. Correlate spreadability with mechanical interestingness: the more compelling the disease loop (e.g., zombies), the more acceptable strong measures like quarantine become.

* Diseases with different types of spread should have their own reagent that greatly reduces the likelihood of spreading the virus while it is active. This lets infected crew keep moving while awaiting treatment. Some strong diseases may be resistant.
* Different types of infection should be blocked by different types of clothing. This increases immersion—less clothing means more points of contact with the disease. Specialized clothing (e.g., medical masks) may have their own protection values. Percentages should be determined during playtesting.
* Quarantine should be avoided as a priority containment measure in most cases, as it requires the crew to remain in isolation, which is not a pleasant experience.

## Roundflow & Player interaction
A sample crew gameplay loop during a virus outbreak.

### Local outbreak loop
1. Early tells: soft symptoms on affected workers prompt self‑care and reporting.
2. Mitigation: [protection against spread](#protection-against-spread), local cleaning, limited access to the dirty area.
3. Diagnosis: swabs and [complete diagnostics](#complete-diagnostics) confirm disease and stages.
4. Treatment: targeted therapy for patients, symptom suppression as needed. If not treated in time, the infection can slowly spread throughout the crew, which can lead to a [global outbreak](#global-outbreak-loop).

### Global outbreak loop
1. Early tells: soft symptoms on affected workers prompt self‑care and reporting.
2. Mitigation: [protection against spread](#protection-against-spread), local cleaning, limited access to the dirty area.
3. Diagnosis: swabs and [complete diagnostics](#complete-diagnostics) confirm disease and stages.
4. Treatment: targeted therapy for patients, symptom suppression as needed. If not treated in time, the infection can slowly kill the crew in the final stage.
5. Vaccine creation (optional): the Vaccinator clones a vaccine from inactive resistances. Healthy at‑risk crew are vaccinated to prevent new cases.
6. Resolution: after treatment, immunity rises, cases fall, [disinfection](#contact-infection) or/and [atmos corrections](#airborne-infection) finish the event.

## Features to be added
### Virology Department
Virology is needed as a place where medical personnel can focus on treating and diagnosing viruses and, in extreme cases, isolating the crew.

The implementation described in this document does not require a virologist, but does not completely rule out its appearance in the future if another design document describes the need for one.

To combat viral diseases, the medical department is equipped with a virology sub-department, which has the necessary equipment (diagnoser, vaccinator, and swab), two connected airlocks, and separate wards.

### Diseases
Diseases should cause discomfort (vomiting, brief stuns, etc.) to motivate players to seek treatment, but should not remove the carrier from play when immediate treatment is not possible. Not every disease must be harmful, benign or quirky effects can exist, but ignoring harmful diseases should entail increasingly serious consequences, such as damage or other negative effects.

Diseases can be viruses, infections, or special conditions of living beings; they can have symptoms, stages, and treatment phases.

Mechanics:
* The mechanics are based on disease prototypes and the carrier component. Each disease has a set of stages, a probability of progression, and infection parameters. On each tick, the system advances the stage with a specified probability, displays sensations, and attempts to trigger symptoms of the current stage.

#### Immunity
Immunity is represented on the carrier as the probability of blocking infection with a specific disease.

Species and animals may possess innate or acquired resistance that alters the probability of infection, to create desired gameplay situations.

#### Symptoms
Symptoms should clearly signal that a character is ill, drive the player toward medical tools and help, and shape risk for nearby crew without turning the carrier into a spectator.

Design goals:
1. Noticeable cues to the carrier and observers (emotes, sensations) so suspicion of illness does not require machines.
2. Frequency and intensity scale by stage with clear early tells. If ignored, consequences should escalate meaningfully.
3. Symptom channels reflect infection routes (cough/sneeze -> airborne, vomiting/slime -> contact, bleeding -> bloodborne) to teach responses.
4. Short stumbles or brief stuns are acceptable. Long stun chains or frequent item drops that stall the player are avoided unless a disease is intentionally high‑risk.
5. Symptoms can harm not only the carrier, but also those around them (e.g., spreading the virus more actively when sneezing), motivating the crew to suppress the symptom or cure the carrier.

#### Treatment
Treatment of the disease can be complete, reducing the stage, or at the symptom level. It all depends on the type of disease and what goal it pursues. 

Design goals:
1. Complete diagnostics inform targeted therapy, which is a reward for the time spent.
2. Blind treatment can be wrong; drugs should have side effects in small doses to punish random search. 
3. Treatment at the symptom level is temporary and should contain the harm from the disease until complete treatment, so it may require less effort.
4. Completing treatment grants immunity against this disease. Its strength depends on the disease type, but is usually high to prevent reinfection loops.

#### Contact infection
Contact infections spread via direct touch and contaminated surfaces. This path exists to promote hygiene, and active decontamination.

Mechanics:
* Through direct contact (hitting, touching), there is a chance of the virus being transmitted from the infected to the healthy.
* When in contact with a surface, the infected entity leaves a level of contamination on it.
* With each subsequent contact with the same surface, the level of contamination increases.
* The level of surface contamination can be cleaned with chemical agents, and also slowly decreases over time.
* A healthy person interacting with an infected surface reduces the level of contamination; at the same time, they have a chance of becoming infected, which depends on the remaining level of contamination and the characteristics of the virus.

Countermeasures:
* Clean contaminated surfaces using cleaning chemicals that can be used by cleaners or medical personnel.
* Cleaning items under running water (sink, shower).

#### Airborne infection
Airborne infections spread through exhaled aerosols and ambient atmosphere. This path makes masks, ventilation, and air‑quality management matter.

Mechanics:
* An infected entity generates a certain amount of virus in the surrounding atmosphere when they exhale.
* The concentration of the virus in the air around the source changes over time and distance.
* For airborne diseases, environmental conditions matter—the atmospheric conditions under which the virus can survive or multiply.
 * Example: miasma is a suitable atmosphere for reproduction. When this environment is eliminated, the virus gradually dies.

A simplified implementation uses a flat chance of transmission within a certain radius from a breathing infected person to a suitable healthy person.

Countermeasures:
* Eliminating harmful atmospheres in which viruses multiply. This is the job of an atmospheric technician, which leads to more interaction between departments.

#### Blood infection
Blood infections require blood-to-blood exposure. This path reinforces safety during blood transfusions.

Mechanics:
* Transmission occurs only when infected blood enters the bloodstream of a healthy entity.
* The probability of infection depends on the volume of blood and the characteristics of the virus.

Countermeasures:
* Cleaning and removal of blood.

### Vaccines
The primary purpose of vaccines is to reward medical treatment by preventing healthy personnel from becoming infected with this disease, rather than curing existing infections.

Vaccines are special reagents that add disease‑specific immunity by adding active entries to the carrier's resistances.

Resistance mechanics:
* After a complete cure, the host receives an inactive resistance entry for that disease. Inactive entries do not protect but are eligible for vaccine cloning in the [vaccinator](#vaccinator). The cloned vaccine, when administered, converts the matching resistance to active on the recipient.
* Active entries completely block infection with the specified disease but cannot be used to create vaccines.

Vaccine mechanics:
* Targeting: each vaccine dose contains a list of disease types (paths). It only affects those specific diseases.
* Effect on carrier: on internal application, for each matching disease the host gets an active resistance entry added to resistances. This prevents future contraction of those diseases and does not cure existing ones by itself.
* Stacking/merge: mixing vaccine reagents merges their target lists; multiple sources combine into one set of resistances.

#### Vaccinator
Similar to the [diagnoser](#complete-diagnostics), it is a way to obtain vaccines. It accepts samples for convenience and is stationary due to the utility of vaccines.

The Vaccinator is a stationary virology machine that synthesizes vaccine bottles based on a loaded blood sample. It distinguishes between inactive and active resistances in the sample.
