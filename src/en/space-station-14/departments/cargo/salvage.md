# Salvage

> _There's gold in them thar ~~hills~~ asteroids._ — Space Mark Twain

## Concept

Salvage is one of the material lifelines of a station in deep space, where prepared materials are expensive and limited in supply, but asteroids, wrecks, and other space debris are abundant.

Salvage is primarily engaged with by the role of the *Salvage Specialist* in the Cargo department.
Their challenge revolves around departing the safety of the station's interior towards a hostile outside, absent of power, atmospherics, medicine, and everything else that enables the station crew to live a somewhat normal life.
Their goal is to traverse this harsh environment to retrieve and process material goods for the station, allowing it to avoid depleting valuable stockpiles or spesos.
In return, the Salvagers get to experience challenges at a higher frequency than found on the station, along with the satisfaction and respect gained from overcoming them.

## Design Pillars

### Pillar 1: Space hates everyone equally

Salvage, fundamentally, should engage with the same space mechanics that those on the station are subject to.
The Salvage environment is built as part of the same world as the station, but existing outside its protective bubble that usually isolates crew from mechanics such as barotrauma, asphyxiation, and hostile mobs.
While the crew's encounters with these dangers come primarily from unexpected emergencies, Salvage Specialists is made to actively engage with them as part of their work. 
Despite this difference in exposure, the mechanics remain the same.
Just as a Passenger needs EVA protection when the station's hull is breached into space, a Salvage Specialist needs EVA protection to handle the exterior environment.

> Do not: Salvagers access a virtualised environment that wields wholly unique mechanics that are isolated from the station.

> Do: A site accessed by a Salvager is within visible range of the station, and wields mechanics such as atmospherics and power against anyone that accesses it.

### Pillar 2: Raw ingredients, not prepared products
What distinguishes Salvage from other forms of resource acquisition is that the resources it procures are not immediately available to use, either in the form of raw materials that require refinement or Salvage lacking the equipment to utilize them.
This is one of the key [forcing functions](https://en.wikipedia.org/wiki/Poka-yoke) that prevents Salvage from forming a closed loop that isolates it from the station.
By mandating that the flow of Salvage touches base with the station to exchange with other game loops, Salvage remains attuned to the condition of the station should their raw ingredients be disrupted from transformation into usable resources.

> Do not: Salvagers retrieve immediately useful items, and access resources that can be immediately put to use without intervention of the station.

> Do: After retrieving resources, Salvagers need to touch base with the station to deposit their raw ingredients, and potentially get something useful out of the exchange.

### Pillar 3: Maximally dynamic environment

Whereas stations are designed to provide a stable foundation for gameplay until they inevitably get disrupted by the progression of the round, Salvage is thrust immediately into unknown gamestates that resemble the on-station environmental threats as a baseline.
Players interacting with Salvage need to be able to read these gamestates, formulate a plan, and execute the plan, just as those on station do.
Much of the on-station dynamicity is caused by the multitude of agents congregating on it; lacking this, Salvage gameplay has to rely on other systems to generate variety in its scenarios.

> Do not: Sites accessed by Salvagers pose a fixed problem that can be memorised and solved optimally.

> Do: Sites accessed by Salvagers are randomised, and require on-the-fly plan formulation to retrieve resources from.

> Do not: Sites accessed by Salvagers only rely on a few mechanics to pose a threat to Salvagers, and only a few mechanics to impede resource acquisition.
> Salvagers can prepare for every possible challenge with a single inventory.

> Do: Sites accessed by Salvagers make full use of the game's diverse sandbox that offers many factors to consider in planning and execution.
> Salvagers may need to prioritise what toolset they'll bring to face challenges with.

### Pillar 4: The station still anchors you

While at surface level, isolated from the threats of the station, the station should still remain a touchpoint for Salvage to rely on.
Correspondingly, Salvage should still be able to be disrupted by threats that disrupt the station.
Power outages should be able to disrupt the ability to pull sites, unstable atmospherics should be able to threaten the air supply of a Salvage player, and a disrupted Medical department should be able to threaten a Salvage player's ability to recover from acquired injuries.

> Do not: Sites are accessible by Salvage without any resource consumption.

> Do: Salvage requires powered machinery drawing from the station's power supply to access sites.

> Do not: Salvagers can fully recover from damages on their own.

> Do: Salvage needs to touch base with the station's engineers to repair mechanical components of their operation, and with the station's medical department to fully recover from any acquired injuries.
> Salvagers can still bandage over problems to lessen their severity, using similar "ducttape" mechanics to the crew, such as inflatable walls, portable generators, or bandages.

### Pillar 5: Resource management still challenges

While Salvage is meant to provide resources to the station, the quantity and quality of resources should not be able to remove resource management as a concern for itself or the station.
While a general collection of resources can work with some considerations, the station should still be able to run out of resources if a large amount of a single type is required.
Salvage engaging with the needs of the station as they come up can pull resource gathering towards needed resources and away from resources triaged as less important.

> Do not: Salvagers are able to fill the entirety of the station's needs with every possible type of resource, and fully defeat the gradual decay of a station over the course of a round.

> Do: Salvagers need to decide what resources to gather, with consideration for how they're gathered and what the station needs.

> Do not: Core mechanics of other roles rely on Salvagers' output to the point of being completely unable to progress without it.
> Progression may slow to a crawl and the lack of resources potently felt, but can be offset by suboptimal or limited methods such as Cargo purchases, on-station recycling, or workarounds.
