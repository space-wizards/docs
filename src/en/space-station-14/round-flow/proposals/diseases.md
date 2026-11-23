# Diseases

| Designers | Implemented | GitHub Links |
|---|---|---|
| Pok | :warning: Partially | Part 1: space-wizards/space-station-14#40545 |

## Overview
Diseases should exist to create readable outbreak gameplay for medical and nearby support departments. The core experience is a telegraphed local outbreak that starts from a recognizable source, gives crew time to react, and rewards diagnosis, cleanup, and containment. The system should keep infected players in the round while making neglect, unsafe handling, and poor sanitation matter.

## Background
Previous SS13-style virology often fails in one of two directions: diseases are either trivial to solve, or the optimal answer is to sit in a room and wait for one specialist to finish the whole problem. Both outcomes flatten roundflow, reduce interdepartmental play, and make infection feel more like paperwork than a station crisis.

This document focuses on viral diseases first, though the underlying system should be able to support other progressive conditions later. The disease system should primarily serve medical and janitorial gameplay by creating readable hazards and response tools. It is not meant to justify omnipresent random contagion, nor should it require a dedicated virologist role to make outbreaks function.

## Game Design Rationale
### Design Pillars

#### Outbreaks start 
The baseline disease scenario should begin with a contaminated source that crew can point to: a filthy room, a corpse, rotten food, a blood-soaked workplace, an artifact, or bad air in a local area. Players should be able to form a story about why the outbreak happened and what needs to be fixed.

Local outbreaks are the main use case because they create clear goals for multiple departments. The station is more interesting when crew can trace danger back to a place, object, or unsafe practice than when infection appears to come from nowhere.

#### Symptoms
Diseases should announce themselves through sensations, emotes, visible messes, or readable environmental tells before they become severe. A player who gets infected should usually have a chance to realize that something is wrong, seek help, or take steps to protect others.

1. Noticeable cues to the carrier and observers (emotes, sensations) so suspicion of illness does not require machines.
2. Frequency and intensity scale by stage with clear early tells. If ignored, consequences should escalate meaningfully.
3. Symptom channels reflect infection routes (cough/sneeze -> airborne, vomiting/slime -> contact, bleeding -> bloodborne) to teach responses.
4. Short stumbles or brief stuns are acceptable. Long stun chains or frequent item drops that stall the player are avoided unless a disease is intentionally high‑risk.
5. Symptoms can harm not only the carrier, but also those around them (e.g., spreading the virus more actively when sneezing), motivating the crew to suppress the symptom or cure the carrier.

#### Quarantine
The preferred response to most diseases should be mitigation and treatment, not parking a player in a box until the problem is over. Hard isolation is acceptable only when the disease loop is intentionally severe enough to justify it, such as event or antag-driven global outbreaks.

#### Immunity
Immunity is represented on the carrier as the probability of blocking infection with a specific disease. Species and animals may possess innate or acquired resistance that alters the probability of infection, to create desired gameplay situations.

#### Treatment
Treatment of the disease can be complete, reducing the stage, or at the symptom level. It all depends on the type of disease and what goal it pursues. 

1. Complete diagnostics inform targeted therapy, which is a reward for the time spent.
2. Blind treatment can be wrong; drugs should have side effects in small doses to punish random search. 
3. Treatment at the symptom level is temporary and should contain the harm from the disease until complete treatment, so it may require less effort.
4. Completing treatment grants immunity against this virus. Its strength depends on the virus type, but is usually high to prevent reinfection loops.

These tools support local outbreaks first, but they also give future events, antagonists, and environmental hazards a structured way to create illness, progression, and containment gameplay.

#### Disease response
Medical should own diagnosis and treatment, but it should not solve every outbreak alone. Janitors should matter when contamination lives on surfaces and objects. Atmos techs should matter when air quality or local gas conditions affect survival and spread. Other crew should matter by reporting symptoms, wearing appropriate protection, and not feeding the hazard through unsafe behavior.

This keeps diseases tied to station simulation instead of turning them into a self-contained specialist job. The more the outbreak asks players to fix the source, not just the patient, the better it supports roundflow.

#### Player-to-player spread 
Player-to-player transmission should exist only when it creates understandable gameplay. Coughing on someone in an enclosed contaminated room, bleeding into a transfusion, or smearing infected filth across shared surfaces can work because the risk is legible and the counterplay is readable.

Passing by an infected player in a hallway and rolling bad luck is not good outbreak gameplay. If transmission between players cannot be seen, anticipated, or mitigated, it should be heavily limited or removed.

## Roundflow & Player Interaction
Diseases should primarily create short-to-medium response arcs that start small, ask the station to identify the hazard, and reward crew for acting before the problem becomes a station-wide crisis. The main loop is a local outbreak, with broader events treated as a secondary use of the same tools.

### Local Outbreak Loop
1. **A contaminated source appears.** The outbreak should begin from a readable hazard, as described under [Outbreaks start](#outbreaks-start).

2. **Exposed crew get early tells.** Symptoms should first communicate danger the way described in [Symptoms](#symptoms).

3. **Crew mitigate the source.** Initial response should rely on [Protection against spread](#protection-against-spread), not default to [Quarantine](#quarantine).

4. **Medical confirms the disease.** Screening should begin with [Partial diagnosis](#partial-diagnosis), while exact identification should require [Complete diagnostics](#complete-diagnostics).

5. **Patients are stabilized and treated.** Follow the principles outlined in [Treatment](#treatment), with suppression buying time for full care.

6. **The station closes out the outbreak.** Ongoing containment uses the relevant transmission route sections plus, if justified, [Vaccines](#vaccines) via the [Vaccinator](#vaccinator).

7. **The outbreak resolves or escalates.** If the source is not fixed, the incident can widen into the kind of broader crisis described in [Global Outbreaks](#global-outbreaks).

### How Transmission Should Play
#### Contact Spread
Contact diseases should primarily spread through contaminated surfaces, shared objects, and dirty work areas. This supports hygiene, cleanup, and careful handling as gameplay. Touching the source, then spreading it further through tools or surfaces, is more interesting than invisible proximity infection.

Contamination should accumulate where infected players or sources interact with the world, decay over time, and be removable through cleaning or washing. The danger comes from how long a dirty area is left untreated and how many people keep using it.

#### Airborne Spread
Airborne diseases should be strongest in enclosed or contaminated local spaces, through visible symptomatic emissions, or where environmental conditions let the pathogen survive. Masks, air correction, and avoiding bad rooms should be meaningful counterplay.

#### Blood Spread
Bloodborne diseases should require explicit blood-to-blood exposure, unsafe transfusions, or injury care performed without proper handling. This gives medical and first responders a clear safety rule to follow and lets the disease reinforce existing treatment mistakes or battlefield chaos.

## Global Outbreaks
Global outbreaks should be a secondary use of the disease system, not its default form. They are best suited to events or gamemodes that already justify their existence without diseases, such as zombie-style scenarios or other station-wide crises.

In those cases, the disease system adds stage progression, recognizable symptoms, containment tools, immunity, and optional vaccination. It gives the event more texture and response options, but it should not be the only reason the event is interesting.

Because global outbreaks are intentionally more severe, they can justify stronger spread, broader countermeasures, and occasionally quarantine. Even then, they should still favor readable escalation and clear player counterplay over invisible random infection.

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
* [Quarantine](#quarantine) should be the exception, not the default answer.

#### Vaccines
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
