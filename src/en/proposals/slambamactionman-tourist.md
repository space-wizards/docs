# Tourists

| Designers | Implemented | GitHub Links |
|---|---|---|
| SlamBamActionman* | ⚠️ Partially | Travel Camera: space-wizards/space-station-14#24085<br> Visitor Job: space-wizards/space-station-14#23972<br>Tourist Role: TBA|

*Based on a [Discord thread](https://discord.com/channels/310555209753690112/1193309894879744151) by yourpaldeebs

## Overview

**The Tourist** is a mid-round ghost role visiting the station on a holiday trip, with benign, non-antagonistic objectives to complete during their stay. These objectives are easier to fulfill when collaborating with the station, encouraging the Tourist to ask small favors and requests from crew that can lead to interesting roleplay. Examples of objectives are; being let into department areas, see certain items, and take photos of specific crew members with their camera. Additionally antags can exploit the role as a cover story to get access to areas and pass undetected. The Tourist essentially provides a low-risk passenger role that is harmless to the station and enables roleplay, but also makes antags less metagameable via its design and tools.

## Background

This proposal originates from this [Discord thread](https://discord.com/channels/310555209753690112/1193309894879744151) by yourpaldeebs.

In the current state of the game, many antag roles can be identified by metagame aspects that can only be explained by them being an antag. Examples of this are StealthOps Nukies or infiltrating Traitors not appearing on the crew manifest, or DNA Scramblers giving a Traitor a new name. This can make these playstyles very difficult against powergaming players and therefore quite limiting; the Tourist role is meant to remedy that.

For the Tourist player themself, the role is meant to push for opportunities to roleplay and also add a bit of cheeky yet ultimately harmless spice to the station. The Tourist is *not* an antag, and it is important that their goals do not encourage antagonistic behavior. Instead their goals are meant to push for social interactions with crew in a low-stakes environment for the player. The Tourist also appropriately fits into the Standard Operating Procedure that visitors to the station are meant to be welcome.

## Gameplay

The Tourist spawns with a randomly generated name and appearance in the Arrivals map. 
They spawn with the following:
- Hawaiian "tourist" clothes
- A backpack, containing:
  - A few randomly selected clothing items (similar to [DresserFilled](https://github.com/space-wizards/space-station-14/blob/03f0257ae9b0c3d2d349bd2bcc4670a7ac92e139/Resources/Prototypes/Entities/Structures/Furniture/dresser.yml#L50)).
  - A survival box.
  - A pair of Sunglasses.
  - A Polaroid Camera, a new Tourist objective item described further below.

The Tourist does not spawn with an ID/PDA and does not start with a headset.

It is important that the Tourist does not possess any items that uniquely identify them as a Tourist. Crew should not be able to distinguish a Tourist from someone impersonating one; the tell should be the behavior of the character rather than any verification or metaknowledge. The Camera is a partial verification item as a Tourist always spawns with one, however as described further below there are other ways to obtain the item.

The Tourist gets assigned some amount of objectives from the list below, some of them with multiple targets:

- **Visit:** The Tourist must have visited certain locations on the station. This could be certain departments (Security, Engineering) or specific sub-areas in low-security deparments (Morgue, Cargo Bay, Robotics). Areas should not be high-security areas; Vault, Armory or Head Offices are examples of these.
- **Get Drunk in Bar:** The Tourist must have gotten drunk in the bar. Like Visit but with an extra objective.
- **Photograph Crew:** The Tourist must have used their Camera item on a randomly selected crewmember. Camera described further below.
- **Photograph Item:** The Tourist must have used their Camera near a specific item; the item *can* be held by a person or be worn, but being inside a container does not count. The item may be restricted, but should not require major larceny to photograph if the owner is unavailable or unwilling. (e.g. Node Analyzer/Seclite vs. Hand Teleporter/R&D Server)
- **Stamp Collecting:** The Tourist must end the round with a paper in their inventory that has X different job stamps on it. Generic stamps such as Approved/Denied do not count, but non-Command jobs such as Chaplain, Clown or Syndicate do.
- **Eat:** The Tourist must have eaten a specific kind of dish. This dish should not rely on too exotic/unreliable ingredients (Carps/Spiders/Xeno/Amanita) but still require effort from the Chef (certain burgers, pies, pancakes and cakes). Only available if a Chef is on the station.
- **Pet:** The Tourist must have given a specific station pet a pet. Functionally quite similar to Visit, but less static.

The Tourist is *not* able to spawn as an antag. That instead falls onto existing antags, who may choose to fake being a Tourist for the benefits it provides. A Tourist may become an antag during the course of the round via external factors (e.g. via a conversion antag).

### The Travel Camera / Polaroid Camera

The Travel Camera is an item that the Tourist spawns with and is semi-exclusive to the role. Its main functionality is to help fulfill the Photograph objective, however it can also be used as a minor defensive tool should the Tourist be at risk of harm. 

The Travel Camera acts very similar to a Flash with reduced stun duration, and contains 10 charges. The Travel Camera can not be refilled (you only brought a single roll!), so Tourists are discouraged from spamming it and to instead use it to fulfill their objective, with any leftover uses being free for roleplay/defense.

The Travel Camera is also rare maintenance loot and available in the Syndicate Uplink, to ensure that it can not be used as a way to verify whether someone is a normal Tourist or not. If proper photography functionality is implemented the Camera may find use in other jobs as well (e.g. Detective). The uplink Camera is the same as a maintenance/Tourist camera. The Camera can NOT be used by Head Revs to convert crew.

The Travel Camera is also a cosmetic item, in that it can be equipped in the tie slot to hang around the Tourist's neck.

## Additional Changes

HoP will have a new job role available to them: Visitor. The Visitor has the same access rights as a Passenger (Maintenance), but with a different job icon. This keeps them distinct from Passengers (useful for Command and crew). The Visitor job role can also be used by admins for events. (2024-02-07: This has now been implemented and merged into the game)

## Possible Expansions

The Tourist could in the future be split into multiple different kinds of Tourists that have more specificity/theme to their objectives; food bloggers, station inspectors, springbreak groups, veterans. For now, the ClothesMate/AutoDrobe allow the player to choose their flavor of roleplay instead.
