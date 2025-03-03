# Cargo Mail Delivery

| Designers | Implemented | GitHub Links |
|---|---|---|
| ScarKy0 | :x: No | TBD |

## Overview

This design doc is meant to introduce the concept of mail deliveries to the cargo gameplay loop. Allowing cargo to deliver mail to specific people on the station in order to gain some bonus money without the need to only run bounties.

## Background

Currently cargo's main way of earning money is the bounty system and selling random objects around the station. This can lead to situations such as other departments not cooperating or some bounties simply being not possible to make within a reasonable timeframe, as well as getting repetitive after a while. Times where most bounties are unachievable beyond simple ones (such as botany, but those take a while!) and the inability to skip due to a long cooldown happen often.
While those issues can be fixed by making changes to the bounty system (like lowering the bounty skip cooldown) that feels like a bandaid fix to the fact cargo has basically only one way to earn money.

Delivering mail is meant to serve as a secondary option of income cargo can take care of during their shift.
This is meant to serve several things:
- Allow new players to get accustomed to learning cargo easier. Currently a new cargo tech might have no idea where to gather items for bounties or which things they can buy to reinvest into a bounty. A simple task of delivering mail can help teach the station layout and introduce to the game while also leaving space for other technicians to explain how the job works.
- Add gameplay variety to cargo. Cargo as it stands has a rather simple gameplay loop. You print a bounty, you deliver the invoice to a department and then you sit at cargo until you're told it is ready for pickup. Not only is this repetitive but several bounties can also be completed on the spot, which makes cargo generally boring gameplay wise.
- Encourage player interaction. Simple mail deliveries can greatly help with interactions between cargo and other players/departments.
- Add a little bit of chaos to the station. Mail ultimately can grant some silly random items to the recipient, and what is more fun than finding a bike horn or some bananas to annoy others with?

## Features to be added

### Mail Teleporter

The Mail Teleporter is the main thing controlling the flow of mail to the station. It should be mapped somewhere within cargo.
While connected to power and enabled, it will generate mail on top of itself every few minutes. Anyone with cargo access can toggle it on and off to prevent further mail from spawning.
The amount of deliveries spawned should depend on the amount of players on the station, with a minimum amount to ensure a steady flow of mail. Ideally moments where cargo is overflowing with mail, or getting too little to be able to make use of it, should never happen.

Mail Teleporter is one of a kind machine, with only QM having a spare board to construct it, just like how cargo sell computers can be destroyed. This encourages actually taking care of it as to protect it from destruction by either having cargo keep a closer eye on it or putting it in a more secure area. In case an additional one is built, it should not generate additional mail, only split the existing amount between all available teleporters. This is to ensure cargo cannot simply create a mail farm.

### Deliveries

Deliveries refer to anything that can spawn using the Mail Teleporter. The main focus here is Letters and Packages.
On spawn, deliveries get assigned a random player in the crew manifest. When collected by the desired recipient they must scan their fingerprint on the delivery to open it, granting them a little reward and cargo some bonus money.
If a non-recipient is to try to open a delivery, it will instead say they are unable to open it due to their fingerprint not matching. This however can be bypassed by tearing the delivery open (for letters) or smashing it open (for packages). Doing so will not grant cargo any points, as well as will damage anything inside of the delivery, but will still grant the unintended recipient the contents.

#### Letters

A small item, usually containing spam mail, birthday wishes (maybe even with money!) and similiar.
They can be torn open using a Verb if the current holder is unable to open them.
Letters are not meant to contain expensive items, usually sticking to some silly things (joints, spam, pills, etc.) or more rarely things of interest (research disks, pins, etc).

#### Packages

A big item that occupies both hands. They are supposed to contain things slightly more of value or items that can be useful to your average player. The loot table can include things like tools, plushies toys, food as well as some funny things like pipebombs or rarely contraband. What needs to be kept in mind is that the "evil" or "funny" options need to be very unlikely as to not make people scared of opening packages, that would beat the entire point of the design. Last thing we want is someone being afraid of opening a package in case it explodes.
When on the ground it can be smashed open with melee attacks to break the seal, allowing access to whatever is stored inside and obviously not granting cargo any money.

#### Fragile Deliveries

Fragile deliveries serve as a small modifier to add onto already spawned ones. A fragile delivery will break upon being thrown or hit, leading to it losing a major portion of it's value when delivered. Mail being fragile should be indicated on the sprite, as well as have a unique examine text.
The main point here is to add a little bit of variety to mail as to not keep it boring and too simple. While delivering items isn't the most exciting thing ever, it shouldn't be boring either.

#### Priority Mail

Same as above, this serves as a small modifier for newly spawned mail. Instead of being broken on dropping, instead this delivery is on a timer.
The exact time by which a piece of mail marked as priority needs to be delivered can be viewed on examine, showing time within the shift, rather than a countdown. If that time is passed, the mail will lose value and earn cargo less.
Obviously, this should also be indicated by a change on the sprite.

### Future Expansions

Not meant to be full ready ideas or direction for the future, simply possible ways this can be improved to show mail has potential to be expanded on in the future.

#### More Modifiers

Fragile and Priority mail shouldn't be the only things that can affect deliveries. If more variety is needed, this system can be made more exciting by adding possible new modifiers. Letters that grow legs and beg you to not be delivered as that ends their life? Things like these can be added in the future.
A good example of such implementation could be that whenever a package there is a low chance it will receive a modifier. Such modifier will add onto the value, make the item pool more interesting but also make the package itself more annoying to handle. The following are only possible examples.
- Burning: The package releases intense heat into the atmosphere around it, but grants 2x spesos.
- Everlasting Sorrow: The package cries when carried, causing the carrier to slip on water if they're not careful for 1.25x spesos. Would mix great with being fragile.
- Glued: It cannot be dropped by itself without destroying it and must instead be "stripped" off the carrier for 1.25x spesos.
- Drunk: Constantly injects small amounts of ethanol into whoever holds it, making them drunk while in inventory for 1.5x spesos.

## Game Design Rationale

Currently cargo is oriented around the bounty system (except salvage, who is mostly separate from the main cargo loop). A mail system allows for more interaction between players as well as lowers dependency on bounties, while also allowing new players to learn basics of the game.

Cargo is already meant to interact with other departments, this plays into that fact and gives them a little something to do in the meantime. Ideal situation could be delivering a package to a botanist at the same time as you want to grab a bounty from them. Or a new player player grabbing a bunch of deliveries and getting to explore the station and meet other players as they deliver them.

## Roundflow & Player interaction

At the start of the round, after getting prepared a cargo technician visits Mail Teleporter and grabs letters into their bag and a package. Upon checking the manifest they may also pick some bounties to deliver at the same time. The cargo tech brings the mail to the recipient, who then unlocks it and grants cargo some bonus money and gets something small in return.
In the case the delivery is simply never opened, or the recipient is dead/missing, it can be simply opened in cargo and the contents sold for very limited profit.

Interactions with other players are key here, both sides benefit while being able to get to interact more with each other. Cargo should not simply leave mail at their front door and get someone to pick it up whenever they walk past. Leaving the packages at front ready for pickup also means a random passerby may tear them all open and lead to cargo losing out on the major rewards, further discouraging this method while giving cargo a reason to worry about protecting their mail.

Ideally, mail is not meant to be a free item generator for cargo to use to flex drip they get. Forcefully opening packages should not generate more value than delivering them, making sure it is never worth it to open a package unless you're the recipient. Gambling should be done with the grand lottery and not randomly spawned in mail. 