# Cloning Rework (aka: borging alternative)

| Designers | Implemented | GitHub Links |
|---|---|---|
| Velken | :x: No | TBD |

## Overview

Many players do not wish to be borged when they die/gibbed/rotten corpse, while borgs can be inresting, it is not for everyone. The current cloning system is either only available in Central Command or through a lot of work from salvage team, which, in both cases, are "too late" to matter.

This rework aims to give people more reason to interact with the Medical department and even add new possible objectives for antags, while not being an extremely powergamed cloning mechanic.

<sup>Values in this document are not final and are subject to change.</sup>

### Breakdown
Cloning is a way to re-introduce players back into a round, whitout them being turned into cyborgs or via ghost roles, but the cloning process is to be harder than the borging process, as to balance having full humanoid features (hands, slots for backpacks and suits, not being bound to silicon laws).

## The New Cloning System

Before someone can be cloned and inserted in a new body, they first must be scanned, which, with default tech, should take 7.5 seconds per person, using a "Body Scanner". Each medical deparment in a station should have at least 1 Body Scanner. A Body Scanner must be anchored to the ground, be powered and be connected to the "Gene Bank Server". When getting scanned, they must be alive and not in critical condition.

The Gene Bank Server stores all humanoid "Genetic Information" that has been scanned, similar to how a R&D Server stores all researched technologies. The Gene Bank has the following mechanics:
- When someone is scanned, their Genetic Information (GI) is saved.
  - Which is compatible with them and only them. Another person's brain could not be put in their body.
  - Only one copy of someone's GI can be stored per Gene Bank.
- The first time someone gets scanned, their GI is 100% stable, unless they have genetic damage when they are scanned.
  - Future scans have a 20% chance to reduce their GI stability by 1-2%.
- The Gene Bank must be kept cooled at range of -20ºC to 0ºC using pipe system (similar to hyper lathes).
  - The further from this range, the faster Genetic Information in that Gene Bank deteriorates, up to a maximum of 0.1% per second (GI is instantly deteriorated if temperature is above 190ºC or bellow -70ºC)
- Genetic Information loses Integrety, even if kept at the ideal temperature, by a rate of 0.01% per second.
  - Events can cause Genetic Information to lose Integrity at faster rate or by a flat amount.
- Genetic Information gets deleted from the Gene Bank once it reaches 0% Integrity.
  - CMO Access can be used on the Gene Bank to bring up an UI listing all GI and their Integrity %.
- Captain Access can delete GI entries from the bank.
  - The captain should refrain from doing so, being a last resort, such as, someone that has escaped Perma.
  - Deleting a GI entry leaves a log for security on the Gene Bank Server, similar to logs on vending machines, unless the wire was cut. 
  
A new body can be printed using the Body Printer. The Body Printer requires biomass (provided by Botany or bought by Cargo) to print a new body, in a slow process that takes 20 seconds, the printing process also releases Carbo Dioxide. A better printer can be built, unlocked with the same technology as hyper lathes, and must be cooled in the same manner.
- The new body is similar to the original one, except, it has no brain. The original brain must be inserted after opening the cranium.
  - Even if there is no brain, the cloned body will have similar biological needs as the original (breathing, eating, temperature, etc).
  - The printed body will have at least 1 genetic mutation (see next chapter), with more possible genetic mutations depending on how degraded the DNA is. Re-Printing the body will have different mutations. Using a Health Analyzer will list all current mutations.
  - Even if all Genetic Information is corrupted, the new body will have the same fingerprint ID for Security.

### Genetic Mutations

Genetic Mutations occur with the degradation of Genetic Information when a body is printed. All clones have the "Cloned Body" genetic mutation, even if at 100% GI Integrity.
At 90-99.9% GI Integrity, there is 1 extra mutation;
At 80-89.9% GI Integrity, there is 1 extra mutation and 25% chance of 1 extra mutation;
At 75-79.9% GI Integrity, there is 1 extra mutation and 50% chance of 1 extra mutation;
At 70-74.9% GI Integrity, there are 2 extra mutations;
At 60-69.9% GI Integrity, there are 2 extra mutations and 25% chance of 1 extra mutation;
At 50-59.9% GI Integrity, there are 2 extra mutations and 50% chance of 1 extra mutation;
At 25-49.9% GI Integrity, there are 3 extra mutations;
At 0.1-24.9% GI Integrity, there are 4 extra mutations.

All percentages of the mutations bellow stack by adding/subtracting between themselves before calculating into the main stats.
Mutations of opposite effects exclude each other from being applied on the cloned body.

The "Cloned Body" mutation has the effect of:
- 10% less maximum health;
- 10% increased hunger and thrist rate.

The varius mutations can be split in three categories, Negative, Neutral and Good mutations.
Certain mutations have lower weights of being chosen, those are marked with an *

Negative:
- Eyesight*
  - Reduce vision range by 2 tiles
- High Calory Intake
  - Increased hunger rate by 20%
- Dry Throat
  - Increased thrist rate by 20%
- Malformed Joints
  - Reduced sprint speed by 10%
- Frail Bones
  - Take 10% extra blunt damage
- Thin Skin
  - Take 10% extra slash damage
- Mute*
  - Cannot speak
- Frail*
  - Take 25% more stamina damage and has 5% less maximum health

Neutral:
- Accent*
  - Has different accent than original body had.
- Alterated Metabolism - species
  - Has stomach of a diffent species
- Uncontrollable Laughter
  - Randomly laughts
- Skin tone*
  - Random new base skin colour
- Size
  - 10% bigger or smaller size
- Blood Type - species
  - Changes blood to a blood of another species 

Good:
- Low Calory Intake
  - Decreased hunger rate by 20%
- Moisture Glands
  - Decreased thirst rate by 20%
- Flexible Joints
  - Increased sprint speed by 10%
- Sturdy Bones
  - Take 10% less blunt damage
- Thick Skin
  - Take 10% less slash damage
- Robust*
  - Take 25% less stamina damage and increased maximum health by 15%  
- Non-Conductive*
  - Act as if wearing insulated gloves

## Antag objectives

With cloning being available, Syndicate objective to eliminate someone would need to be changed accordingly, and some new ones could be added.

- The Objective "Kill or Maroon" would stay the same, as there is the option to maroon the target, preventing the brain from reaching medical or even deleting their cloned information (Using emag on Gene Bank lets you access it and delete ONE genetic information from it).

- The Objective "Kill" a targed would also track if the target has been cloned

- The Objective to protect fellow syndicate agent would track if they were cloned 

- Unique Uplink item for Medical staff Syndicates, injector that removes 1 random negative mutation (including, possibly, the "Cloned Body" mudation)

- Ninja would get new possible objective (which would take same slot as steal research) "Scramble the Gene Bank Server". Doing so, would decreased all genetic information by 10-30%, but no less than 25%.

- New Thief objective "Plant a sniffer in the Gene Bank Server". Start with said item in pocket if has this objective. To install, screwdriver the server and insert the device.
  - The device is only known to be installed in the server if someone opens the server with a screwdriver and inspects the server. The device can be re-crafted with 1 steel, 1 lv wire and 1 power cell.

## Interactions with other deparments

Other departments can have the following interaction with Medical in regards the cloning

- Botany
  - Provides biomass
  
- Cargo and Salvage
  - Salvage can find "Defragmentation Disks", which when used on the Gene Bank server, restore 10% Integrity to all Genetic Information saved in it
  - Cargo can buy biomass bulk order

- Science
  - Science can research and create Hyper Convection Body Printer, which is faster than the normal one and uses less biomass.
