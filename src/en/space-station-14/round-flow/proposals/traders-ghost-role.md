# Traders
<!-- Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar. -->

<!--
`Designers` should be the names that you use on GitHub and/or Discord. This is optional but strongly recommended, since:

- This acknowledges credit where it is due
- People who are confused about the written intent can use this information to contact the authors

`Implemented` is the status of the feature.

Github links can include multiple PRs, if relevant.
-->
| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| DigitalThaumaturge | DigitalThaumaturge | :x: No | TBD |

## Overview
<!-- A very short, maybe three sentence summary of what this proposal is about. A high level "overview" or "what this adds". -->
The trader is a mid-round ghost role that is largely crew-aligned. Each trader is given a unique shuttle (like the visitor) that is equipped to function as a mobile shop. Traders get a randomized inventory of items, and in order to access these items, an item must be placed into the trader's vault. Traders have an open-ended objective: to make as much profit as possible without getting banned from the station, and must haggle, barter, and set prices on their own terms to fulfill this goal.

## Background
<!--
Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game.
Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.
-->
Every time someone goes to the lengths to set up a shop in SS14, everyone else seems to love it from both a mechanical and roleplay sense. Having done so myself, haggling with people over exchange prices or spesos and defending your shop from threats is probably the most fun thing I have done in this game.

In addition, at the moment there is a lack of crew-affiliated ghost roles that encourage unique gameplay. Visitors are pretty much just a way to respawn. Station pets don't do much until you cognizine them. Mothroaches and mice are glorified spectators with food mechanics. Derelict borgs are probably the most interesting ghost role, but they are apparently just a bit too common at the moment.

## Features
<!-- Give a description of what game mechanics you would like to add or change. This should be a general overview, with enough details on critical design points that someone can directly implement the feature from this design document. Exact numbers for game balance however are not necessary, as these can be adjusted later either during development or after it has been implemented, but mention *what* will have to be balanced and what needs to be considered when doing so. -->
Traders spawn on a trader shuttle, with some new machines that help them handle transactions and protect both their inventory and their spoils. These machines only allow access to people with the trader's specific DNA, meaning the trader does not have to worry about getting robbed blind during a snack or drink break. When a trader spawns, an announcement is given that a trader is approaching the station.

Traders have built-in flash protection to prevent them from ever becoming a revolutionary.

### Machines:

Bluespace Vault:
A large, indestructible machine that cannot be manually unanchored. All of the items that the trader accepts as payment end up here, and traders can freely retrieve and deposit items from it. Traders can also add items from the vault to their lockboxes' inventories, recycling payments into products. The only items this cannot store are "trash" items (whatever can go in a trash bag) and objective items.

Bluespace Lockbox:
Multiple indestructible machines that cannot be manually unanchored. Each contains a different "category" of items that can be bought from the trader, such as clothes, materials, weaponry, etc., and is filled with a random selection of those items when the trader spawns. For one of these products to be dispensed, a different item must be slotted into the lockbox as payment, and this item will be stored in the trader's vault when the product is selected. Lockboxes have a limit to how much they can stock, and if a trader wants to refill them back up to this limit, they have to use their Restock Radio, which is covered below.

Traders can select an item from the lockbox's inventory to be displayed above it as a hologram. This allows them to showcase their stock without compromising its safety.

Restock Radio:
A hand-held device that the trader has in their pocket when they spawn. Activating it on the Automated Trade Station refills the trader's lockboxes back up to their inventory limits. Has a 15 to 20 minute cooldown in between each use.

Bluespace Cart:
A draggable item that can be linked to a lockbox with a network configurator to perform that lockbox's function on the go. Useful if the trader can't find a good place to dock with the station, but can only be linked to one lockbox at a time. Convenience of location at the expense of selection.

Nanotrasen Trade License:
A wall-mounted display, and the only one of the trader's unique machines that is not accessed via DNA match. Instead, the trade license's access is limited to members of Command. On use, it disables the trader's other machines for the specified amount of time, banning them from trading, restocking, or even accessing their vault until the timer is up. This should only be used if a trader is being too disruptive — it essentially puts them in "sale jail."

Item Categories:
Clothing (Costume pieces and rare clothing sets.)
Raw Materials (Low amounts of these, so as not to step on cargo's toes. But if the salvs are slacking...)
Personal Defense (Low-powered guns, ammo, and some melee weapons. Lets Security get in on the fun.)
Protective Clothing (Hardsuits and other clothing items with unique abilities)
Tech (Mostly things that science can research, but potentially a bit earlier than usual.)
Food (Mostly ingredients to allow the chef to make some new dishes, with the odd Arnold's pizza.)
Experimental (Implants, other weird stuff.)

Traders only have four lockboxes, meaning that some of the categories will not be available for purchase that round.

### Goals

Traders spawn with one objective: to make profitable deals and have the most spoils in their vault and/or inventory at the end of the round. There are no mechanics tied to this objective, and the pricing is entirely subjective.

The game plan is ultimately simple: dock with the station, and invite the crew into your shuttle to peruse your wares, with you present behind the counter to determine prices. They have to set the prices and, through RP, make deals to sell them. That's it! How they go about this is up to the player.

There is exactly one specific interaction traders have with antagonists: their machines can be broken into with an Authentication Disrupter, which makes them accessible to all.

### Optional Feature: Brands
In this feature, shuttles would have identifiable branding, and the traders might even be locked to a specific species dependent on the brand. In addition, one of the categories would stocked with items unique to that brand. 

### Optional Feature: Contraband
In this feature, traders would occasionally have contraband items distributed in with their stock, such as having a single item of chameleon clothing in their clothing lockbox, or perhaps a hypopen in their experimental lockbox.

Although they are free to sell this to anyone aboard the station, since they are not crew, they risk being banned via their sale license if they make too many risky deals. Sure, you can arm all the passengers to the teeth, but if security traces all those guns back to you, you're going to be in time out for a while.

### Optional Feature: Thievin' Traders
In this feature, a separate ghost role for an antagonistic trader would sometimes appear. This trader would spawn with (item-only) thief objectives, the pickpocketing ability, and the pacifism implant. They would have to accomplish their objectives without any of the thief's original tools ... but with the full power of their shop's random inventory and their business skills. Every man has his price, right?

Putting an item into your Vault would count as stealing it, and the Vault would accept any item. 

## Game Design Rationale
<!--
Consider addressing:
- How does the feature align with our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosphy?
- What makes this feature enjoyable or rewarding for players?
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- How does it enhance player cooperation, competition, or emergent gameplay?
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?
-->
With their randomized inventory, traders are Chaotic. Haggling over the price of a Mosin is Seriously Silly. Haggling and bartering over the trader's player-determined prices are massively rooted in Player Interaction/Agency.

With their unique game plan, desire for profit, and focus on player interactions, traders would be very interesting to not only play as, but also to have around to buy from.

Finding a way to buy helpful items from a trader by trading away valuable but less useful items would lead to a lot of new strategies, and ones that would be dependent on who's playing the trader in question. It would be a unique business relationship.

Overall, traders would add a lot of dynamic interactions to the round they appear in.

## Roundflow & Player Interaction
<!--
Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
- Which department will interact with the feature? How does the feature fit into the [design document](../space-station-14/departments.md) for that department?
-->
Traders would be an early-to-mid round ghost role that would only appear about every four rounds at maximum. With their unique stock of items, they could potentially speed up the pace of a round by providing the crew with equipment that they would not normally be capable of acquiring early on.

Traders should never be fully able to replace cargo, which is mostly enforced through their randomized inventory. Cargo is slow and often neglectful, but it is ultimately consistent. With traders, you never know what you're going to get, on either side.

Traders would introduce a bit of a unique allegiance within SS14: since their primary customer and source of income is the crew, they should want the crew to prosper and the station to run, making them effectively crew-aligned. However, since their primary motivation is based on profit, they should be allowed a bit of indirect antagonism via allowing them to sell supportive items to bad actors. It's a trade off, though, since your risk having your shop shut down for a while, decreasing profit.

## Administrative & Server Rule Impact (if applicable)
<!--
- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
- How are the rules enforced mechanically by way the feature will be implemented?
-->
The most troublesome feature is giving traders contraband and/or weaponry, as they would be able to use it freely. However, traders should be rare enough and randomized enough that any griefing a trader could do would be contained to only about one round at most.

Mechanically, traders are a bit lax, except for having to put an item into their Vault to dispense something from their stock. However, this is important to allow for unique pricing on the part of each trader. 
## Technical Consideration
<!--
- Are there any anticipated performance impacts?
- Does the feature require new systems, UI elements, or refactors of existing ones?
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
-->
New code would need to be written for the trader's unique machines, and each would need a UI (probably adapted from the lathe or vendor menus) that displays their contents. In the lockboxes' cases, a section would need to be added that shows the item currently inserted as the price.

The trade license would need a UI, but that likely could be adapted from the one for jailing prisoners.

A method to display items within containers would need to be added so customers could be given a preview of what is inside the lockboxes.

Traders themselves would be a simple ghost role, created through the event system. They would be weighted to be somewhat rare.

The trader's unique shuttles would need to be mapped, similarly to the visitor's unique shuttles.

Items that exist specifically to be sold by the trader would likely only be added later, and as separate pull requests.