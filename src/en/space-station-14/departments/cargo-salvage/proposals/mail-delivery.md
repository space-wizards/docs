# Cargo Mail Delivery

| Designers | Implemented | GitHub Links |
|---|---|---|
| ScarKy0 | :x: No | TBD |

## Overview

This design doc is meant to introduce the concept of mail deliveries to the cargo gameplay loop. Allowing cargo to deliver mail to specific people on the station in order to gain some bonus money.

## Background

Currently cargo's main way of earning money is the bounty system and selling random objects around the station. This can lead to situations such as other departments not cooperating or some bounties simply being not possible to make within a reasonable timeframe, as well as getting repetitive after a while.
While those issues can be fixed by making changes to the bounty system (like lowering the bounty skip cooldown) that feels like a bandaid fix to the fact cargo has basically only one way to earn money.

Delivering mail is meant to serve as a secondary option of income cargo can take care of during their shift.
This is meant to serve several things:
- Allow new players to get accustomed to learning cargo easier. Currently a new cargo tech might have no idea how to complete bounties or earn money properly. A simple task of delivering mail can help teach the station layout and introduce to the game.
- Add gameplay variety to cargo. Cargo as it stands has a rather simple gameplay loop. You print a bounty, you deliver the invoice to a department and then you sit at cargo until you're told it is ready for pickup. Not only is this repetitive but several bounties can also be completed on the spot, which makes cargo generally boring gameplay wise.
- Encourage player interaction. Simple mail deliveries can greatly help with interactions between cargo and other players/departments.
- Add a little bit of chaos to the station. Mail ultimately can grant some silly random items to the recipient, and what is more fun than finding a bike horn or some bananas to annoy others with?

## Features to be added

### Mail Teleporter

The Mail Teleporter is the main thing controlling the flow of mail to the station. It should be mapped somewhere within cargo (being station or ATS).
While connected to power and enabled, it will generate mail on top of itself every few minutes up. Anyone with cargo access can toggle it on and off to prevent further mail from spawning.

### Deliveries

Deliveries refer to anything that can spawn using the Mail Teleporter. The main focus here is Letters and Packages.
On spawn, deliveries get assigned a random player in the crew manifest. When collected by the desired recipient they must scan their fingerprint on the delivery to open it, granting them a little reward and cargo some bonus money.
If a non-recipient is to try to open a delivery, it will instead beep and say they are unable to open it. This however can be bypassed by tearing the delivery open (for letters) or smashing it open (for packages). Doing so will invoke a penalty on cargo, taking away from their funds, but will still grant the player whatever was inside.

#### Letters

A small item, usually containing spam mail, birthday wishes (maybe even with money!) and similiar.
They can be torn open using a Verb if the current holder is unable to open them. Obviously giving cargo a penalty (as stated above) but granting the user the contents.

#### Packages
A big item that occupies both hands. They are supposed to contain things slightly more of value or items that can be useful to your average player. (Tools, Cakes, Plushies, rarely minor contraband and pipebombs)
When on the ground it can be smashed open with any weapon to break the seal, allowing access to whatever is stored inside, still granting cargo a penalty.

### Future Expansions

#### Syndie Uplink Items

Deliveries don't have to stop at just letters and packages. There is also the possibility of a cargo-only uplink item that is a rigged package, potentially spawning something hostile or exploding.
There could also be some way to sneak items into packages, having the recipient leave their sweet fingerprints on the contents and allowing for a way to frame them.

#### Custom Mail

Ever wanted to give your arch-nemesis a threatening letter, but never wanted to give it in person? There is potential for a way to create custom letters/packages and allow cargo to deliver them for you.

### Main things to consider:
- Delivery items need to have a timer that starts upon being taken out of the teleporter. When the timer runs out the money earned should be significatly lowered, either gradually or instantly. This encourages cargo to actually deliver the mail instead of leaving it at the front for others to check.
- Deliveries that are losing value due to not being delivered should grant less of a penalty to cargo when they do eventually get opened, someone stealing and keeping mail just to sabotage cargo when they find a moment to smash it open should not bring huge penalties.
- Items granted by deliveries cannot hold big value to them, as to not make breaking packages open and selling their contents more profitable than delivering them.
- Cargo should have a reason to not allow their deliveries to be stolen, as that obviously not only makes them lose out of money, but also gives them a penalty if the seal is broken by a 3rd party.

## Game Design Rationale

Currently cargo is oriented around the bounty system (except salvage, who is mostly seperate from the main cargo loop). A mail system allows for more interaction between players as well as lowers dependancy on bounties.

Cargo is already meant to interact with other departments, this plays into that fact and gives them a little something to do in the meantime. Ideal situation could be delivering a package to a botanist at the same time as you want to grab a bounty from them. Or a new player player grabbing a bunch of deliveries and getting to explore the station and meet other players as they deliver them.

## Roundflow & Player interaction

At the start of the round, a cargo technician visits the ATS (or wherever the mail teleporter will be mapped) and grabs letters into their bag and a few packages. Upon checking the manifest they may also pick some bounties to deliver to that person at the same time. The cargo tech brings the mail to the recipient, who then unlocks it and grants cargo some bonus money and gets something small in return.
In the case the delivery is simply never opened, it will slowly lose all value and become free game for whoever finds it and decides to open it.

Interactions with other players are key here, both sides benefit while being able to get to interact more with each other. Cargo should not simply leave mail at their front door and get someone to pick it up whenever they walk past. The penalty timer is meant to have them deliver it instead. Leaving the packages at front ready for pickup also means a random passerby may tear them all open and lead to big penalties, further discouraging this method while giving cargo a reason to worry about protecting their mail.

Additionally, mail is not meant to be a free item generator for cargo to use to flex drip they get. Losing money for opening mail that doesn't belong to them means they it is almost never worth it to open a package while not the recipient, other than possibly sabotaging cargo if they slip up.