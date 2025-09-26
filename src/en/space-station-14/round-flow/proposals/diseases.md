# Diseases

| Designers | Implemented | GitHub Links |
|---|---|---|
| Pok | ⚠️ Partially | Part 1: space-wizards/space-station-14#40545 |

## Overview
This document describes the mechanisms of diseases and virology.

## Background
We aim to introduce a clear, maintainable foundation for diseases and a virology role that integrates with existing medical workflows. The initial scope focuses on readable mechanics, predictable player tools, and performant systems that can be iterated on in future PRs on mutations and virus creation.

## Game Design Rationale

## Purpose
Diseases should create station-scale challenges that encourage teamwork rather than rewarding solo lab loops. They exist to drive investigation, communication, and coordinated response across departments.

## Core design principles
1. **Readable, actionable problems**. Provide clear signals so players know what to investigate and who to call.  
2. **Meaningful tradeoffs**. Every response has costs and benefits (see examples below).  
3. **Support coordination**. UI and tools should reduce guesswork and focus play on cooperation.

## Mechanical tradeoffs (examples)
* Wearing PPE against viruses instead of more desirable items or avoiding infection altogether.
* Deploy a narrow vaccine cloned from the first recovered patient now, versus wait to gather more samples to merge resistances into a broader vaccine.

## Signals and tooling
Provide clear, actionable information to support decisions.
1. Quick identification (HUD/console).
2. Detailed diagnostics in the department (diagnoser).

### Gameplay to avoid
* Prolonged solo lab isolation with little crew contact. Core progress depends on live samples, ward triage, distribution, and inter-department requests.
* Unbounded pandemics that overwhelm the station. Bounded severity, tunable spread, and accessible treatments.
* Excessive or indefinite quarantine. Quarantines are situational and mechanically costly; mitigations (PPE, cleaning, vaccines) are preferred.

## Roundflow & Player interaction
### Work in virology
This is the work of the medical department, mainly prioritized by virologists.

1. **Early response:** coordinate with chemists, stock up on personal protective equipment and cleaning supplies.
2. **Detection:** respond to reports of symptoms, collect samples using sample sticks, confirm diagnosis using a ([diagnoser](#diagnoser)).
3. **Mitigation:** organize triage and treatment, coordinate limited quarantine measures with security, request engineering services to ventilate or isolate the area, schedule cleaning.
4. **Prevention:** use a sample from a recovered patient to clone target [vaccines](#vaccines) and distribute them.
5. **Recovery:** lift quarantine, conduct follow-up observation.

## Desired player experience
* Medical leads the diagnostic and treatment loop.  
* Engineering and Atmos handle infrastructure responses.  
* Cargo and Chemistry provide logistics and reagents.  
* Crew make meaningful, situational choices: mask up, seek treatment, help with cleaning.  
* Antagonists may exploit confusion, but diseases are **not** griefy, unstoppable tools.

## Features to be added
### Virology
#### Role
The virologist is a separate role in the medical department, whose main task is to combat [diseases](#Diseases) by diagnosing, isolating infected individuals, obtaining medicines, and creating preventive [vaccines](#vaccines). In critical situations, close the department for quarantine.

#### Department
To combat viral diseases, the medical department is equipped with a virology sub-department, which has the necessary equipment diagnoser, vaccinator, and sample stick), two connected airlocks, and separate wards.

### Diseases
Diseases can be viruses, infections, or special conditions of living beings; they can have symptoms, stages, and treatment phases.

The mechanics are based on disease prototypes and the carrier component. Each disease has a set of stages, a probability of progression, and infection parameters. Infection may have an incubation period during which symptoms and spread are disabled. On each tick, the system advances the stage with a specified probability, displays sensations, and attempts to trigger the symptoms of the current stage.

#### Immunity
Immunity is represented on the carrier as the probability of blocking infection with a specific disease.

After complete recovery, the base immunity strength to the disease is applied. Immunity can also be pre-configured for each entity in the carrier component or [vaccines](#vaccines).

#### Stealth Flags
A characteristic of a disease that helps to conceal it. Some chemicals should reduce the stealth level of the disease, this is especially important for diseases with hidden treatment methods.

* **None:** default behavior.
* **Hidden:** do not show in HUD.
* **VeryHidden:** hide from HUD, diagnoser, and health analyzer.
* **HiddenTreatment:** hide treatment steps in the diagnoser.
* **HiddenStage:** hide stage in the diagnoser and health analyzer.

### Types of infection

#### Contact
The infected spreads the virus through direct contact with other entities and through contact with surfaces.

Mechanics:
* Through direct contact (hitting, touching), there is a chance of the virus being transmitted from the infected to the healthy.
* When in contact with a surface, the infected entity leaves a level of contamination on it.
* With each subsequent contact with the same surface, the level of contamination increases.
* The level of surface contamination can be cleaned with chemical agents, and also slowly decreases over time.
* A healthy person interacting with an infected surface reduces the level of contamination; at the same time, they have a chance of becoming infected, which depends on the remaining level of contamination and the characteristics of the virus.

Protective factors:
* Gloves (40%)
* Feet (20%)
* Outer clothing (20%)
* Inner clothing (10%)

#### Airborne
The virus spreads through the air: an infected person releases particles when they exhale, cough, etc.; healthy people can inhale them and become infected.

Mechanics:
* An infected entity generates a certain amount of virus in the surrounding atmosphere when they exhale.
* The concentration of the virus in the air around the source changes over time and distance.
* For airborne diseases, the environment parameter is important - under what atmospheric conditions can the virus survive or multiply.
* Example: miasma is a suitable atmosphere for reproduction; when this environment is eliminated, the virus gradually dies.

A simplified implementation allows for a simple chance of transmission within a certain radius from a breathing infected person to a suitable healthy person.

Protective factors:
* Mask (40%)
* Head (20%)
* Eyes (10%)
* Connected cylinder (75%)

#### Through blood
The infection is transmitted when infected blood comes into contact with the blood of a healthy person.

Mechanics:
* Transmission occurs only when infected blood enters the bloodstream of a healthy entity.
* The probability of infection depends on the volume of blood and the characteristics of the virus.

### Symptoms
Symptoms are configured as separate prototypes and tied to the stages of the disease. A symptom has a base chance of triggering per tick and a set of behavioral effects. Some symptoms can increase the spread of infection — for example, causing a one-time airborne “spread” that uses the radius and chance of the disease with symptom multipliers.

### Treatment
Treatment is defined by healing steps at the disease level or a specific stage. On each tick, the system attempts to apply the appropriate steps with their probability (default is 100%; can be used for treatment with reagents).

A step may lower the stage instead of a complete cure. Complete cure removes the disease and grants post-immunity. Individual symptoms may have their own steps that do not cure the disease but suppress the symptom for a specified period of time.

The main methods of treatment are:
* **Waiting:** cure after staying in the disease for a specified time (in ticks) with a certain probability of success.
* **Temperature:** requires staying below a specified body temperature for several ticks in a row.
* **Bed rest:** chance of recovery when in a hospital bed or lying down; the chance may increase during sleep.
* **Reagents:** recovery when a set of reagents is present in the bloodstream at or above the required levels (reagents are not consumed).

### Diagnostics
Diagnostics is built around two tools:
* Sample stick: used on a living object with a short delay; records a list of active diseases and their stages in a sample with the subject's name and DNA.
* Diagnoser: takes a sample and displays the diseases found, their current stages, characteristics, and descriptions/treatment steps in the UI. Can print paper reports; some characteristics will not be recorded in them.

#### Medical HUD and Console
Display an icon next to the infected person. If the disease is positive, it will be displayed in blue.

#### Analyzer
Shows the presence of the disease, its stage, and a hint in the tooltip: use the diagnoser for a detailed examination.

### Diagnoser
The diagnoser is a stationary medical console that accepts a disease sample and provides a detailed analysis for medical staff. It does not detect diseases on its own, a sample is required.

Inputs:
* Accepts a sample produced by the sample stick. Only one active sample is analyzed at a time. The sample preserves the subject's name and DNA.

Displayed information (subject to stealth flags):
* **Patient:** name and DNA from the sample metadata.
* **Detected diseases:** list of diseases found in the sample.
  * Name and description.
  * Stage and stage progress.
  * Incubation status if applicable.
  * Spread characteristics: infection type (air/contact/blood) and general contagion parameters.
  * Severity and notable symptoms for the current stage.
  * Treatment steps and hints.

Actions:
* Print report: prints a paper report with the current analysis; some fields may be omitted from printouts.
* Eject sample: returns the sample to the user without modification.

### Vaccines
Vaccines are a special reagent (`id: vaccine`) that add disease-specific immunity by writing active entries to the carrier's resistances.

Resistance mechanics:
* After a complete cure, the host receives an inactive resistance entry for that disease. Inactive entries do not protect but are eligible for vaccine cloning in the Vaccinator. The cloned vaccine, when administered, converts the matching resistance to active on the recipient.
* Active resistance completely blocks infection with the specified disease, but they cannot be used to create vaccines.

Vaccines mechanics:
* Targeting: each vaccine dose contains a list of disease types (paths). It only affects those specific diseases.
* Effect on carrier: on internal application, for each matching disease the host gets an active resistance entry added to resistances. This prevents future contraction of those diseases and does not cure existing ones by itself.
* Stacking/merge: mixing vaccine reagents merges their target lists; multiple sources combine into one set of resistances.

Notes:
* Resistance requires the disease to allow resistance.
* Normal metabolism applies; no special decay or booster mechanics exist beyond standard reagent behavior.

### Vaccinator
Vaccinator is a stationary virology machine that synthesizes vaccine bottles based on a loaded blood sample. It distinguishes between inactive and active resistances in the sample.

Inputs:
* Accepts an open reagent container (e.g., beaker) containing a blood sample. The machine reads detected strains and the donor's stored resistances (if present).

UI and actions:
* Culture Information: displays detected strains, analysis progress, and allows naming/printing release forms.
* Antibodies: lists disease resistances found in the sample with their state. Only inactive resistances can be used to clone a vaccine; active resistances are shown but not clonable.
* Clone Vaccine: available only for inactive resistances. Creates a glass bottle named after the target disease, filled with 15 units of [vaccine](#vaccines) that, when administered, activates that resistance on the recipient.
* Eject/Destroy: ejects the loaded container or safely discards its contents.
