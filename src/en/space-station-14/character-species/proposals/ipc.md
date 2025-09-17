# Integrated Photonic Chassis
| Designers | Implemented | GitHub Links |
|-----------|-------------|-------------|
| Minemoder | :x: No      | N/A         |

## Overview
This proposal is for the Integrated Photonic Chassis Species. IPCs are an alien robotic race not bound to silicon laws. Where there would be skin and bone there is steel; where there would be muscles and joints there is myomer and linkages.

Though bound to a humanoid shape, appearances may still vary widely thanks to their robotic origins. IPCs fill the robotic niche, without being a narrowly focused silicon bound to laws.

## Background
The Integrated **Photonic** Chassis is inspired by SS13's and SS14's Integrated **Positronic** Chassis, though distancing itself for gameplay balance purposes.
There have been no tests for IPCs on Wizard's Den, though downstream servers do use IPCs. There is an interest to bringing IPCs upstream.

## Design
IPCs are meant to cover a player's desired niche of a robotic character, without being a law bound silicon. IPCs use different core mechanics than other organic species, though similar enough that it shouldn't be too jarring to play.

### Differences from SS13 and other SS14 forks
IPCs as per this doc use a Photonic brain rather than a Positronic brain. Mechanically, this brain is identical to every other species' brain. This is done to curb potential speciesism by having them be manufactured by NT, to prevent a gibbed IPC from instantly ratting out their murderer over binary, and because Diona already have a similar ability with nymphs.

IPCs will also not have any form of maintenance hatch. This means they will use a headset like every other species, and do not have a battery that can be replaced. The lack of internal encryption keys is for ease of use, if security needs to search or confiscate a key, they don't need any special tools to do so. They don't have a battery since that mechanic has been replaced.

IPCs are not immune to atmospherics issues or the cold, hard vacuum of space. They will need to take care to not walk into plasma fires, frezon leaks, or out into space without protection. This is done because circumventing half of the game's threats is is not good design.

## Core Visual Elements
IPCs are bipedal humanoids. While their silhouette is similar to a human or slimeperson, their bodies and limbs are visually distinct in that they are mechanical, and the iconic TV head. The sounds they make are robotic and mechanical in nature, similar if not identical to the sounds cyborgs make.

## Mechanics
### Death and Shut down
IPCs are mortal just as every other species is, and can die. Take enough damage, and the IPC will die.

IPCs do not have a critical state, instead they are either alive or dead. To compensate, they can take more damage before dying.

Unlike other species, IPCs need to worry about shutdowns. Shutting down is equivalent to dying, though without taking damage.

### Overheat
IPCs, like many other computers and machines, operate best within a narrow temperature range. Too hot, and the IPC shuts down to avoid critical damage; too cold, and the myomers struggle to expand or contract.

### Coolant
IPCs use a hydrocarbon based dielectric coolant with self sealing properties in place of blood.

This is to say, IPCs have a bloodstream, can bleed out, and will slowly stop bleeding like every other species. They do not, however, replenish coolant on their own. They can be injected with replacement coolant that chemists can synthesize, or the IPC can ingest and metabolize ethanol to create more coolant internally.

Low coolant levels lead to body temperature increasing, which if left unchecked will lead to the IPC shutting down due to overheating.

Being exposed to low pressure or the vacuum of space will cause coolant to boil off, leading to low coolant levels and thus overheat.

### Fueled
IPCs utilize an internal fuel cell to generate power.

The fuel cell uses oxygen and any flammable liquid at varying efficiencies such as welding fuel from maintenance, vodka from the bartender, or liquid tritium from atmos.

Should the IPC run out of primary fuel, the fuel cell will instead start burning coolant. If the IPC is not refueled, it will either shut down due to overheating from low coolant, or run out of coolant and shut down.

If the IPC does not have oxygen, they will suffocate and take asphyxiation damage, at a faster rate than every other species.

EMPs will not outright kill or shut down an IPC, though it will stamcrit them.

### Repairs
IPCs do not heal naturally and cannot use most medical chemicals or topicals.

IPCs can repair themselves using common tools and materials found on the station, though the process is very inefficient and time consuming. Other people can repair the IPC much more efficiently and faster.

The tools and materials needed for repair depend on the damage taken. Brute damage requires that the chassis or myomers be repaired, so steel and welders, or screwdrivers, wirecutters, and plastics. Heat damage requires electronics to be repaired, so wires and wirecutters. Caustic damage will also need steel and welders to replace the damaged chassis Radiation requires scrubbing of radioactive materials off of the IPC with sheets of plasma. Blindness and eye can be fixed with a crowbar and reinforced glass.

Genetic damage is a mechanical enforcement damage type, so IPCs will not be immune. They will need normal treatment just as every other species does.

If an IPC is dead they will need to be repaired above the death threshold and/or refueled. If the IPC is sufficiently refueled and repaired, their fuel cell can be jump started with a defibrilator.

Science's exosuit fabricator and the medical techfab can produce repair kits that act similar to the standard topicals.

### Metabolism
IPCs are capable of metabolism, and as a concession could metabolize medical chems until a medical rework is done.

They are also not intended to be immune to chemicals that would benefit them, or harm them. They can ingest desoxyephedrine or hyperzine for speed benefits. They can also suffer from razorium, be knocked unconscious by nocturine, or zombified by romerol. These examples are not meant to be definitive, and can be refined during implementation.

### Surgery
While not a feature yet, IPCs will have a need for surgical intervention when the time comes. The repairs explained above will become more intricate and directed. For example, instead of blunt damage being fixed with a welder and steel, the damaged part will instead need to be removed and repaired, refurbished, or replaced. The same applies to the internal components, or organs.

Their limbs will also be weaker than other species, and can be dismembered easier. Myomers, being closer to organic muscle than to robotic joints, will require surgical intervention to re-attach.