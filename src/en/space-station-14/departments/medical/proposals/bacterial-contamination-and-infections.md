# Bacterial Contamination and Infections

| Designers | Coders | Implemented | GitHub Links |
| --------- | ------ | ----------- | ------------ |
| r3ndd     | r3ndd  | :x:         | TBD          |

## Overview

Currently there is almost no concept of sanitation or sterilization on the station. Doctors inject many people with the same needles over and over, medical gloves and masks serve a purely aesthetic purpose, and people interact with rotting and decaying flesh with no concern. This proposal establishes the concept of bacterial contamination and infection in SS14, which adds new mechanics and gameplay to Medical and can lead to minor chaos (a plague) if germ theory is ignored.

## Background

Outside of zombies there is no concept of pathogens in SS14. Some people are drafting [ideas for the eventual virology system](https://github.com/space-wizards/docs/pull/332), but I thought it would be good to add something simpler which will be compatible and maybe even lay some of the groundwork.

## Features to be added

### Contamination and transmission

Living creatures naturally carry bacteria on their skin. When injected with a syringe (excluding hyposprays/pens), there is a chance (30%) that the syringe will be contaminated with **bacteria**. Using a contaminated syringe on a container with water or blood will contaminate the container and liquid as well. Contaminated containers and liquids will spread contamination to other containers when transferred. Finally, rotting corpses and flesh serve as a guaranteed source of contamination for syringes and liquids. If resistant or super resistant bacteria are present on someone's skin they will cause contamination in the exact same way, except spreading that specific kind of bacteria (explained later).

To sanitize syringes and containers, they can be filled with any amount of a sanitizing solution: ethanol, bleach, space cleaner, or soap. Each instance of them being filled with a sanitizing solution has a chance (50%) of removing the contamination. Adding any of these sanitizing solutions to a contaminated liquid immediately removes the contamination. A future virology/surgery update may want to add an autoclave for mass sterilization of used medical supplies, but this proposal will not include it.

When a creature has an active infection they contaminate any syringes used on them, any containers or liquids they drink from, and food they eat. Eating or drinking from contaminated items causes infection. If a person gets contaminated liquid on their clothes they will contract an infection, unless a an external suit of some kind is being worn (e.g. biohazard, radiation, EVA). Interacting with or dragging rotting corpses causes infection unless wearing gloves. Being bitten by an infected creature also spreads the infection, so vermin control becomes relevant.

### Infection

Using a contaminated syringe on a creature will induce a bacterial infection, which lays dormant for a short period before adding poison damage over time. The bacteria will not be detectable directly with any sort of scan, though a later virology update may want to add a swab or blood test. However, a keen doctor will be able to recognize an infection by taking a history and monitoring poison damage. If a bacterial infection is suspected, doctors will be able to administer antibiotics (bactril) synthesized by Chemistry. Metabolized bactril will immediately remove the bacterial infection and halt additional poison damage, but it will not treat the existing poison damage.

When bactril treats a bacterial infection in a creature, there is a chance (30%) their skin will now carry **resistant bacteria** instead of the natural kind. Resistant bacteria behaves the same as normal bacteria, except it can no longer be treated with bactril and causes a higher rate of poison damage and persistent vomiting via gastrotoxin.

To treat resistant bacteria, chemistry must synthesize a more powerful antibiotic: floraxcin. Floraxcin is ineffective against normal bacteria, but it immediately treats resistant bacteria when metabolized. However, when floraxcin treats a resistant infection there is a chance (30%) the creature's skin will now carry **super resistant bacteria (SRB)**. Once again, SRB behaves just like normal bacteria, except it is very difficult to treat, causes an even higher rate of poison damage, and causes both persistent vomiting and internal bleeding.

To treat SRB, floraxcin must be administered for an extended period. Each second there is a 0.05% chance of being cured if at least 10u of floraxcin is present, however internal bleeding is accelerated if at least 20u is present. This corresponds to a 26% chance of being cured after 1 minute, a 45% chance after 2 minutes, and a 78% chance after 5 minutes.

## Game Design Rationale

This adds some new, fun dynamics to the medical system. Sanitation could be entirely ignored with the liberal use of antibiotics, but antibiotic resistance would become a big problem and plagues would be likely. If everyone is diligent about sanitizing their syringes (such as by doing a full pulls from an ethanol container) and wearing gloves when handling dead bodies, bacteria will not be a big issue. Of course, novice doctors and emergency situations will create opportunities for bacteria to spread. Experienced doctors also get a fun puzzle around figuring out if the source of poison damage is ingestion, medication overdose, bacteria, or something else. When it comes to treating SRB, there is the fun challenge of keeping the floraxcin dose within the narrow range while keeping the patient alive long enough for it to have its effect. Also, there is more of an incentive now for chemistry to turn various medicines into pills, as doctors may opt to use them in some contexts instead of syringes for everything.

Janitors also become important for the health of the station, cleaning up potential sources of contamination and exterminating mice that may be spreading disease.

Antagonists may consider manufacturing an SRB plague to create chaos, but it would require them to steal the antibiotics or break into chemistry, so keeping these secure becomes even more important. Also, unlike zombie invasions it is pretty easy for players to avoid infections if they are careful and wear protective clothing, with the exception of being bitten by infected animals.

## Roundflow & Player interaction

Chemistry may or may not include bactril as an initial chemical to synthesize, but it will need to be on their radar early in case there's an emergent infection. They will also want to provide medical with a sanitizing chemical for cleaning their syringes.
It is not clear yet if doctors will just periodically wash their syringes with ethanol, buy a bunch of syringes and treat them as disposable, or rely a lot more on pills when treating non-emergent, conscious patients.
SRB usually won't be present in a round if precautions are taken, but on the occasional rounds that it does arise it will be of a severity similar to botany's kudzu or science's mismanaged minor anomalies.

## Administrative & Server Rule Impact (if applicable)

There is the possibility of medical doctors and interns intentionally causing infections by not using sanitary practices, but this is a mild issue. The CMO may want to keep the floraxcin locked away and either directly administer it or closely monitor its use, as well as keep track of crew members who have had resistant infections. This should prevent most griefing that would warrant admin intervention.

# Technical Considerations

The two antibiotics can be added as two new synthesizable chemicals.
The premise of bacteria being on skin is just for descriptive purposes and is not how it will actually be implemented. Contamination of syringes will just be a check done in the syringe logic to see if the entity has no bacteria component (i.e. basic, natural bacteria), a resistant bacteria component, or a super resistant bacteria component. If the syringe becomes contaminated it will gain a bacterial contamination component.
I plan to implement most of this contamination logic as an event system similar to the forensic system's DNA transfers and make minimal changes to the injector system itself, as I want to reuse this contamination logic across a lot of different entities and their interactions (containers, food, liquids, dead bodies).
