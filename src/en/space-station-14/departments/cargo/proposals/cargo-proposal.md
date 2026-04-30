# Cargo Rework Proposal

## Overview

This rework is intended as a foundational reinterpretation of Cargo’s gameloop that focuses on creating a more dynamic back and forth with the station and its flow of resources. Emphasis will be placed on Cargo’s interaction with other departments and the ability for the station to quickly acquire materials and resources will be limited to encourage improvisation, pro-active thinking and gameplay, and add to the level of unpredictability a round may face. Cargo’s gameplay should be simple on the surface but more malleable than most departments through station hazards and antagonists due to the importance of their job on station.

## Theming & Aesthetics

The Cargo department is a group of civilians responsible for maintaining the station’s resources and supply lines. Compared to other departments thematically staffed by trained and learned crew members; cargo leans into blue collar and improvised aesthetics with a lack of dedicated equipment. The department is divided between Cargo itself and Salvage as a sub-department with Cargo being responsible for the movement and delivery of Goods and Materials, while Salvage are responsible for gathering materials through breaking down ships.

In terms of visuals: Cargo’s primary colors are Yellow-Tan and Brown, with Salvage having purple added to distinguish their sub-department. The basic cargo outfit is a yellow vest on top of a grey jumpsuit to emphasize their civilian disposition, they have few dedicated tools unique to their department and primarily acquire more by their dealings with other departments or the things they are able to purchase on the market. This creates an “Everything in the kitchen sink” aesthetic where their base look is frequently blended with other departments or groups. They are last in line for fancy new tech and that should be reflected in their design.

> IE: The Ripley is their primary form of moving heavy cargo. The Ripley is a large, unarmored mech with a thin canopy, and two large claws for holding large objects. While there is technically a Mk 2 Ripley, this would be a new version specifically made by Science. If Cargo wished to upgrade Ripley on their own, it would be the addition of scrounged materials like welded plates to increase its armor, purchased tools crudely swapped between arms and likely some degree of paint to keep its color scheme.

Cargo itself is divided into three main roles:

- Cargo Technician: The primary member of Cargo’s crew. The Cargo Technician is an entry role with easy to understand mechanics and meant to guide the player around to other departments to get a sense of how the station operates, what departments typically need, and in general how the economic flow of the station functions. Cargo Technicians will be primarily responsible for moving deliveries back and forth between departments, gathering bounties for sale, and operating on orders of the Quartermaster. Comparable to Retail Employees or Warehouse Workers in job terms.

- Salvage Specialist: The secondary member of Cargo’s crew and the ones responsible for the secondary Salvage department. Salvage Specialists handle the flow of raw resources through stripping and salvaging shuttles, frequently heading back into the station between pulls to assist with duties. Comparable to a Ship Breaker or Miner.

- Quartermaster: The Head of the Cargo department. The Quartermaster is responsible for guiding Cargo’s priorities between what to focus on between department orders, the limited stock, and what should be coming in on any given shipment. They have a unique tool in the form of the Digiboard which allows them to view the current item catalogue anywhere on station. Comparable to a Store or Floor Manager.
  
# Design Breakdown

This section will break down the major parts of Cargo and their intended operation. This system should be paired with some increased level of resource consumption on station, or the lessening of many resources that let departments operate for most if not all shifts without the need for resupply.

As Cargo is the direct supplier of materials on station, balance must be carefully considered at all levels of its implementation. Supply lines will always be a priority target for Antagonists and this should be a considered design choice, but something possible to work around. Points of failure should account for this factor and include alternative methods of being worked around or allowing Cargo to improvise in some manner.

## Item Catalog and Ordering

The catalog will be restricted to a baseline offering of simple/emergency supplies at a marked up price with the bulk of the catalogue re-worked into a rotating series of offerings that Cargo (and anyone with a departmental console) can both see and purchase. These offerings will be ideally thematically cohesive and most importantly: Limited. 

The limitation of purchasing power is an important consideration as part of the enjoyment of resource management. When you can simply purchase anything you need, in any quantity, at any time: there is little incentive or pressure put onto the players to be purchasing items outside of emergencies, specific requests, or simply because they’re bored. By limiting their ability to supply the station all at once, Cargo must be keeping an eye on the flow of the station to assess what items may be important to order and bring on, and the price mark ups of emergency supplies gives them an incentive to be constantly looking for deals while also keeping track of their current inventory.

Limiting the catalog both makes it more intuitive to navigate and helps highlight less conventional purchasing options. Rather than a difficult to navigate list that requires prior knowledge to navigate smoothly: the list is limited and rotating on a consistent basis.

Limitations also emulate an escalating round flow through access prevention/economic starvation. Resources are not always available so the station must plan ahead and use what they do have access to at any given time, slowly acquiring access to more options over the course of a round in limited quantities to expand what they’re capable of. This is a 50/50 split between the primary economic resources (Spesos) and the actual resources themself (Goods) as access to both must be balanced to create a meaningful roundflow. If Spesos are in limited restriction with goods unrestricted: this to surpluses of money being spent on nothing unless an emergency happens or boredom prevails.

By limiting resources and making re-supplying more difficult (but not frustratingly so),the station is encouraged to work with what it’s provided both at round start, and to be pro-active in checking the item catalogue throughout the round for what they might want.

> IE: If Science creates an anomaly, there is little incentive for the station to keep it around if it’s in an inconvenient place as Solid Plasma is relatively easy to order and acquire. If an anomaly ends up in an inconvenient spot but a Scientist wishes to keep it: They have little bargaining power vs. the rest of the station due to this resource’s easy acquisition. If Science is out of Plasma and they order more then they must wait until Cargo decides to go to the ATS and maybe deliver the crate itself to Science. This means a scientist has to kill a workable anomaly for the convenience of the rest of the crew and then wait until Cargo acquires the material, unless said scientist wants to get an EVA suit and jetpack out to the ATS themself.

This system will give antagonists or departments plausible deniability when purchasing items from Cargo. A group of revolutionaries purchasing guns is less immediately suspicious when it’s simply being proactive if they may not get a chance later.

Fun options should still always be available as they are still core to the Space Station experience (Although still shuffled around to create some degree of randomization).

## Station Item Delivery

Item deliveries come in regular shipments to the station, ensuring that the flow of cargo to the station is not dictated by Cargo’s urgency nor allowing it to be easily sabotaged to cut off the flow of items entirely. These shipments have a limited number of space per shipment so they are consistent in size and allow a steady expectation of what a shipment will contain, both to keep large quantities of items from being shipped in immediately and to keep the flow of items regular so Cargo is always engaged with the resource flow to the station.

This is intended to work in tandem with the limited catalogue, rather than limiting access, supply or space individually they are kept in a careful balance to not overload shipments with one type of item, ensure that departments are given agency in what is ordered and brought aboard, and keep shipments regular in spacing requirements to better allow for unique events.

Items should never be discarded if they are unable to be fit into a shipment as this discourages proactivity and puts more pressure on Cargo to be carefully managing shipments at all times. Purchased items should remain purchased and be set into a queue for future shipments. A department’s purchase should never be denied for reasons of space or refusal of cargo to allow it.

The system should also contain a degree of flexibility to ensure that they are always arriving regularly to the station, both in callouts to alert Cargo (or those with access to Cargo’s channels) to their arrival and their ability to dock at the primary docking ports of a station if Cargo’s dock is unavailable.

Telepads will continue to be a distinct upgrade for Departments to allow them to bring in items directly if need be. To keep this upgrade from circumventing the system entirely and to encourage its use more carefully: Telepads should have a cooldown between uses with distinct visuals to communicate this to the crew.

## Department Delivery

The act of delivering to departments should be simple on the surface, but have a high degree of malleability to the station’s or item’s conditions and allow for a reasonable level of optimization.

Delivery of items is divided between three distinct “tiers”:
1. Single transportation of crates through pulling them from point A to point B.
2. Small (3-4) Batched transportation of crates with minimal loss of movement.
3. Hazardous objects or heavy machinery needing specialized equipment to move safely.

Single transportation of crates is the baseline. If a department or crewmember has ordered one crate, it is taken from the shipment by a Cargo Technician from the cargo bay to the department or crewmember in question. The Cargo Technician incurs a slight movement penalty for the ease of movement through the station with minimal burden.

Batched Transportation is the ‘middle tier’ option. In order to discourage Cargo from shuffling items between crates, or into the fewest amount of crates possible they are instead given an object that lets them stack up a small number of crates to quickly move throughout the station. This object ideally comes with some small cost to its operation throughout usage so Cargo can keep its speed and efficiency at an engaging pace.

Heavy Transportation necessitates the Ripley Cargo Mech. This lets a member of Cargo carry mass amounts of crates at once at a heavy reduction to speed and increase in their presence through sound. This is also necessary if heavy machinery is being purchased and brought onto the station as their weight reduces most movement to a crawl, or if the crate in question is hazardous and needs the delivering crewmember to be protected in some manner.

Delivery should be kept simple enough to be engaging for Technicians to be on the move frequently from Cargo to other departments. This keeps the act of delivery reasonably dynamic for station hazards or antagonists to interrupt, requiring Technicians to think quickly on their feet to keep their efficiency high. A hallway might be inaccessible due to spacing, pushing a Technician to find an alternate pathway either around the hazard to their destination or to enter maintenance to move directly towards it but open themselves up to ambush.

## Money Making/Bounties:

Bounties are a static but consistent way for Departments to earn money throughout the course of a round. To better support Departmental Economy and encourage departmental cooperation: Bounties are shifted between specific departments. Each Department has a handful of bounties that are available at all times, both to better guide Cargo members towards solutions for those bounties and to give Departments a direct incentive to fill out bounties. 

Bounties are split 50/50 between the Department in question and Cargo itself, with Cargo having a few bounties for itself as well to ensure they still have some degree of autonomy in their purchasing power (Or in the case of uncooperative departments). This also encourages Cargo to be directly communicating with Departments on the regular to keep their profits high and attending to Departmental needs as they arise. This also ensures Departments see the results of completed bounties and are rewarded for assisting Cargo directly.

Bounties are also shifted away from mass production and towards a thematic creation of kits to keep them better engaging (and lean into the thematic idea of Cargo as traders). Shortcuts should also be de-emphasized as they often become the dominant strategy when discovered. These kits should still lean into some production or spending of resources on station to ensure resource levels are always somewhere in Cargo’s considerations.

“Scavenger Hunt” bounties for items that cannot be produced can be easily found shouldn’t require large amounts of that item so a station isn’t depleted of it if a bounty for that item appears. 

Money can also be made through selling high value items, with future sales of that item reducing the value in half for each future sale. This is both to discourage “Factory” style gameplay, and allow Departments to have a way of earning money outside of bounties through selling rare items they are capable of producing.

## Mail

Mail will be a lesser but consistent money making option for cargo throughout the entirety of the round combined against Bounties as a burst of money when sold on shipments. It exists as a miniaturized version of Cargo’s ideal roundflow with an easy to understand objective.

Mail will arrive throughout the course of a round at the Mail Teleporter, where it can then be collected and distributed throughout the station as needed. Mail is divided between letters and packages, with special modifiers occasionally being added to make the act of delivery more exciting either through fragility, potential danger in explosions, or a sudden burst of value.

## Cargo Events

To keep a sufficient level of unpredictability throughout the round, events will occasionally pop up to both help and hinder Cargo’s efforts. These should carry some level of interactivity to keep them fresh throughout a player’s time in the department, inviting players to come up with fun solutions to problems rather than simply being an extra crate of supplies.

Events can affect any area of Cargo at any time either through their order console, special deliveries that need careful attention, shipments being subverted in some way, or things that manage to sneak their way onto a shipment. These should incur a reasonable level of friction that’s interesting to engage with even in a low level capacity.

If these events are affecting a shipment in any capacity, they should never replace a crate that was intended for arrival. Friction and frustration must always be implemented carefully to keep a loop interesting, removing capabilities outright with no level of chance for Cargo to interact merely creates a delay for the round and for any department or crewmember that might be relying on Cargo.
