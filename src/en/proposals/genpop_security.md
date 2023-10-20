# Genpop Security
By ike709 with heavy inspiration from [AndrewMontagne & OracleStation 13](https://github.com/OracleStation/OracleStation/pull/419)

## Design Goal

This is a proposal to redesign the flow of throwing criminals in the brig and their subsequent release. Right now prisoners who aren't permabrigged usually have nothing to do during their sentence except hurry up and wait, and security officers usually have no reason to interact with the prisoner until their time is up and they need to be escorted out of security.

## Current Brig Experience

The current experience for brigging criminals looks something like this (your mileage may vary by map):

1. Criminal is arrested by security officer.
2. Criminal is brought to security and strip-searched.
3. Depending on the severity, the criminal is thrown into either an individual brig cell for a few minutes (which is the case for most criminals) or into the permabrig area which (depending on the map) usually allows permabrigged prisoners to interact and/or do things like gardening.
4. When a non-permabrigged prisoner's time is up, the cell door opens and they can collect their belongings, but they are still trapped in the security department due to airlock access until someone lets them out.

## Turnstiles

Turnstiles are a key feature in the new brig experience that I'm about to propose. Turnstiles are effectively one-way airlocks, allowing travel only in one direction while still allowing mappers or engineers to set normal airlock access requirements to move through them. Here's what they look like on Oracle, including the mapper overlay to show which direction players can move.

![turnstile](https://i.imgur.com/QStUhoA.png)

In this example a player with the relevant access requirements can only move from the north side to the south side of the turnstile. Even ignoring the rest of this design document, turnstiles would still be useful for things such as putting an exit in medbay or being able to leave the disposals room in maintenance.

## Proposed Brig Experience - Genpop

I propose that we completely nuke individual brig cells. All prisoners will now be thrown into a large secure area similar to the permabrig (called "genpop") where they can intermingle, kill eachother, or perform various other mapped-in activities like play arcade games or do basic botany.

Here's an example from OracleStation. Note the turnstiles, the prisoner processing room in the lower part, and the actual genpop prisoner area in the upper part (ignore the armory in the bottom left):

![genpop](https://user-images.githubusercontent.com/202160/35178888-91bb7eb6-fd87-11e7-9040-15a6ef93602c.png)

I highly recommend taking a look at the [OracleStation pull request](https://github.com/OracleStation/OracleStation/pull/419) as it has gifs for most of the things I've about to describe with words.

This is what the new experience for brigging criminals would look like:

1. Criminal is arrested by security officer.
2. Criminal is brought to security and strip-searched.
3. Criminal is given a prisoner ID with their name & the length of their sentence. This ID's access is required to pass through the "entrance" turnstile into genpop, to ensure the security officer processed them correctly.
4. Criminal is thrown into genpop with all the other prisoners via the "entrance" turnstile, regardless of their crime severity. Individual brig cells and a separate permabrig no longer exist.
5. The criminal's turnstile access is tied to their prisoner ID. Once their sentence has elapsed, they will now have access on their prisoner ID to pass through the "exit" turnstile from genpop back into the processing area. This means they can leave genpop with no intervention from security officers.
6. The criminal can retrieve their possessions from the locker in processing using their prisoner ID.
7. Using turnstiles, the criminal is able to exit genpop, processing, and the main security department entrance without needing a security officer to open doors for them.

## Gameplay Implications

Here's a non-exhaustive list of impacts these changes can have on gameplay, in no particular order:

- Players no longer need help opening airlocks to exit security when their sentence elapses
- Players now have things to do while they are brigged, whether it's ~~killing~~ interacting with other prisoners or the items/machines mapped in genpop
- Players could escape early by stealing or trading eachother's prisoner IDs
- Wardens are now incentivized to actually keep an eye on the brig and its prisoners to prevent fights/prison breaks/shenanigans
- The brig effectively no longer has a prisoner capacity limit, as individual brig cells are no longer needed
- Security officers can pass through genpop turnstiles at will with their ID access, allowing them to enter/exit genpop without prisoners tailing them to escape
  
