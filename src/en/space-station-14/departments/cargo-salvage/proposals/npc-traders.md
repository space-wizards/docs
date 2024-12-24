# NPC Traders

| Designers | Implemented | GitHub Links |
|---|---|---|
| Compilatron, Warpzoned | :x: No | TBD |

## Overview

This proposal is for the addition of NPC trading shuttles that sell specific items at reduced prices, along with a rebalance of cargo to suit.

## Background

An issue brought up not too infrequently is the limited use of shuttles, and the linear nature of cargo. The only shuttle the station gets round-start is the cargo shuttle, which, besides when stolen by salvage, only ever travels between the station and ATS.

There's also the frequent discussion of cargo rebalancing to incentivise different playstyles or to make certain methods of making money more or less viable. But I think all such suggestions are done in good faith to try and make cargo more interesting.

The idea of NPC traders is intended to provide more variety to a cargo shift - and provide more opportunities for skilled players to optimise their gameplay around them. This also encourages cargo to be proactive, and purchase items from traders they come across even if they don't need them now, as they might need them in the future when the trader is gone.

Some might suggest these should be player controlled - but I'm of the opinion these traders should be NPC controlled to ensure they are reliable enough for players to operate around them and try to take full advantage of them when they do show up.

## The Basic Premise

The basic concept of NPC traders is the introduction of traders, which offer a limited selection of crates for sale, depending on the type of trader, and at a better price than what ATS will offer. NPC traders will also offer bounties at a better rate than ATS.

The main catch is that any operation with a trader must be done on their grid. To view crates, purchase crates, view bounties and submit bounties, you will need to dock with their grid and view the onboard consoles.

### ATS Rebalance

To make traders viable, the default price for crates should be increased to compensate. This can be increased to the point that ATS is only useful for emergencies, or only by a slight amount so that traders are just a handy discount.

Some crates that are exotic or rare can be removed from ATS all together and made exclusive to their trader ship - such as lottery crates for the casino trader, figurine crates for the collector, artifacts for the 

### Trader Ships

Trade ships appear as an event which may or may not be announced to the crew - depending on whether they want to be known about. Traders come in various types - which will feature their own ship layouts, flight behaviours, items for sale and bounties. They may offer more exotic items, but their inventory is limited and does not restock. Trade ships also do not persist, and will FTL out after a random amount of time. They will not FTL out so long as a player is on board.

### Trader Stations

Trader stations are more permanent installations that provide larger inventories of items than ships, and will restock themselves periodically. Trader stations may appear round start, and fill the role of a more specialised, less convenient ATS.

### Trader design

Traders should have some freedom to express the type of trader it is - using motifs such as machinery, signage and layout to convey it's purpose. There are some elements that are mandatory:

- **Dock** for the cargo shuttle to dock to. These should try and match the standard "conveyor belt, dock, wall, dock, conveyor belt" design, but can be simplified if needed.

- **Private bounty terminal** which shows the trader's own bounties, and allows them to be claimed

- **Private sales terminal** which shows the trader's crates for sale, and allows them to be purchased

- **Pallets** for teleporting purchased crates and claiming bounties

- **Cargo Hold** which stores crates for sale. A malicious actor could steal them if desired.

- **Guards** in the form of NPCs or turrets. They should be placed in areas which the players should not access, such as the cargo hold or cockpit. They can be always aggressive, or only be aggressive when a player attempts to sabotage their grid or attack them. Guards should never need to leave their grid.

In addition, shuttles will need:

- **Shuttle console** for an NPC or player to pilot the vessel

- **Thrusters and Gyroscope** providing full 4 directional control

## Flight Behaviours

Flight behaviours are stored in the ship and will automatically fly in accordance with their behaviours. These may be defined in a similar manner to mob AI. The execution of these behaviours may be automatic (drone vessels), or require a mob NPC be piloting the vessel. 

| Behaviour | Description                                                                                                |
| --------- | ---------------------------------------------------------------------------------------------------------- |
| Halt      | Hold position. By default, automatically triggered when approached for docking.                            |
| Fly to    | Fly to a grid and wait at a fixed distance.                                                                |
| Orbit     | Fly to a grid and slowly circle around it at a fixed distance.                                             |
| Wander    | Fly to a random position nearby.                                                                           |
| Avoid     | Actively move away from a grid. Used by black market traders to avoid any shuttles trying to dock with it. |

## Trader Types

Traders come in a number of varieties, selling different goods, providing different bounties and flying in different ways. This list is to provide inspiration for trader types that might be found.

(Some flavourtext implies the traders will interact with the places they visit, but they should not. It's just meant to be implied they are doing such.)

#### Bulk Goods Trader
**Sells:** Material crates
**Buys:** Ores
**Behaviour:** Flies to the vgroid or ATS
**Can be station:** Yes

A generic bulk goods trader. They should have large cargo bays and plenty of crates to sell. They'll either be looking to sell at the ATS, or prospecting the vgroid.

#### Botany Trader
**Sells:** Plants, Textiles, Seeds
**Buys:** Botanical chemicals
**Behaviour:** Orbits to the vgroid
**Can be station:** Yes

A flying garden. They should have hydroponics bays, gardens and maybe a small ranch. They'll be looking to find some exotic creatures or plants to grow.

#### Kitchen Trader
**Sells:** Food
**Buys:** Plants
**Behaviour:** Orbits the station
**Can be station:** Yes

A kitchen or resteraunt. They should have a kitchen, dining areas and a generally fancy appearance. They'll be looking to trade with a station full of hungry spacemen.

#### Medical Trader
**Sells:** Chemicals, Medicine
**Buys:** Plants, Chemicals
**Behaviour:** Wanders
**Can be station:** No

A mobile hospital or chemistry lab. Should have a sterile appearance. They'll be searching for people in need of rescue.

#### Collector Trader
**Sells:** Figurines, plushies, books, toys
**Buys:** Figurines, plushies
**Behaviour:** Wanders
**Can be station:** No

A renowned collector - looking to trade the rarest collectables. Can have a variety of appearances, from a library, a gamer basement or a high class hall of artifacts.

#### Science Trader
**Sells:** Artifacts, researched items
**Buys:** Artifact fragments, tech disks, anomally cores
**Behaviour:** Orbits derelicts
**Can be station:** No

A research vessel - like SS14 but much much smaller. They'll have laboraties and can be in various states of disrepair - ranging from brand new to covered in vines, meat floors and rocks. They'll be out looking for artifacts to research.

#### Engineering Trader
**Sells:** Tools, Construction Materials
**Buys:** Raw Ores
**Behaviour:** Flies to derelicts
**Can be station:** No

A mobile construction vessel. They should have various machinery and equipment for salvage and repairs, and a heavy industrial appearance. They'll be flying to derelicts to prospect them.

#### Weapons Trader
**Sells:** Weapons, ammo, armor
**Buys:** Materials, researched items
**Behaviour:** Orbits ATS
**Can be station:** No

A legal weapons trader - likely affiliated with Nanotrasen. They should be hardy but not militarised, sort of like an armored truck in space. They'll be looking to trade their wares.

#### Casino Trader
**Sells:** Lottery crates
**Buys:** N/A
**Behaviour:** Random
**Can be station:** Yes
A flying casino offering everyone they find a chance to win big! Should have a casino feel with gambling tables, slot machines and perhaps a bar. Let's go gambling!

#### Black Market Trader
**Sells:** Contraband items
**Buys:** Organs, weapons, suspicious items
**Behaviour:** Wanders, avoids docking attempts
**Can be station:** No

An illegal black market trader, trying to stay under the radar and make good money. They'll try and stay nonchellant, but will avoid docking attempts if approached, so you'll have to EVA over. You're not a cop, are you?

#### Syndicate Trader
**Sells:** Syndicate contraband, trades only in TC
**Buys:** Syndicate objective items, providing TC
**Behaviour:** Disabled IFF, orbits station, avoids docking attempts, announces presence and location via Syndicate comms
**Can be station:** No

A boon for traitors, a threat to Nanotrasen, a stealthy trader vessel covered in syndicate livery. They'll be difficult to reach, but offer various syndicate traitor items at discount. Just don't piss them off - how do they know YOU'RE not a Nanotrasen agent?