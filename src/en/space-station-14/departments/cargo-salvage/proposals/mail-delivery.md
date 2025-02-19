# Cargo Mail Delivery

| Designers | Implemented | GitHub Links |
|---|---|---|
| ScarKy0 | :x: No | TBD |

## Overview

This design doc is meant to introduce the concept of mail deliveries to the cargo gameplay loop. Allowing cargo to deliver mail to specific people on the station in order to gain some bonus money.

## Background

Currently cargo's main way of earning money is the bounty system and selling random objects around the station. This can lead to situations such as other departments not cooperating or some bounties simply being not possible to make within a reasonable timeframe.
While those issues can be fixed by making changes to the bounty system (like lowering the bounty skip cooldown) that feels like a bandaid fix to the fact cargo has basically only one way to earn money.

Delivering mail is not meant to replace bounties, simply work as a small side thing that can be done in case all bounties are currently being stalled.

## Features to be added

The main things needed are the mail teleporter, as well as letters and packages.

Letters and packages spawn inside of the mail teleporter, which can be opened by anyone with cargo access to drop the currently held items.

Said items then have to be delivered to a randomly picked crewmember on the station (protected by some filter, so Operator Gamma doesn't suddenly receive mail). On delivery the desired crewmember opens it using their ID and cargo gets a small amount of money.

If a package is delivered, on opening it should also grant the target some silly item or food for sure, maybe very rarely minor contraband or things like a pipebomb.

Possible means of this to be expanded could include a rigged package that could work as a cargo syndie-only item, as well as an ability to make custom packages as a more discreet way of transporting items secretly to others.


Main things to consider:
- Delivery items need to have a timer that starts upon being taken out of the teleporter. When the timer runs out the money earned should be significatly lowered, either gradually or instantly. This encourages cargo to actually deliver the mail instead of leaving it at the front for others to check.
- A delivery opened by a non-recipient should bring some sort of downside. Possibly taking away money from cargo so they cannot use this as a free item generator of sorts.

## Game Design Rationale

Currently cargo is oriented around the bounty system (except salvage, who is mostly seperate from the main cargo loop). A mail system allows for more interaction between players as well as lowers dependancy on bounties.

Cargo is already meant to interact with other departments, this plays into that fact and gives them a little something to do in the meantime. Ideal situation could be delivering a package to a botanist at the same time as you want to grab a bounty from them. Or a syndicate cargo tech delivering a fake package with a comically timed pimebomb to explode when opened.

## Roundflow & Player interaction

At the start of the round, a cargo technician visits the ATS (or wherever the mail teleporter will be mapped) and grabs letters or a package to deliver. Upon checking the manifest they may also pick some bounties to deliver to that person at the same time. Upon delivery cargo gets a few spare spesos to spend on bonus steel or similiar while the recipient maybe gets a bike horn to annoy security with.

Interactions with other players are key here, both sides benefit slightly as well as get to interact more with each other. Cargo should not simply leave mail at their front door and get someone to pick it up whenever they walk past. The penalty timer is meant to have them deliver it instead. Leaving the packages at front ready for pickup also means a random passerby may open all of them and lead to big penalties, further discouraging this method of delivering mail.

Additionally, mail is not meant to be a free item generator for cargo to use to flex drip they get. Losing money for opening mail that doesn't belong to them means they it is almost never worth it to open a package while not the recipient, other than possibly sabotaging cargo if they slip up.

# Technical Considerations

Mainly a new DeliveryComponent, DeliverySpawnerComponent and a DeliverySystem to manage spawning and interacting with the packages. Impact on performance is most likely going to be minimal.