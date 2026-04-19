# Telescience

| Designers | Implemented | GitHub Links |
|-----------------|---|---|
| Mehnix | :x: No | TBD |

| Feature | Importance | Complete |
| ----------------- | --------- | -------- |
| Teleframe           | Core     | Done 
| Reality Fractures   | Core     | Partial
| Effects / Incidents | Semi-Core| No
| Upgrades            | Optional | No
| Anomalous Shards    | Optional | No

## Overview
  
This proposal introduces Telescience, a new research method for the Science Department focused on the use of the Teleframe. The Teleframe can be used to traverse great distances, create beneficial and detrimental effects upon the station and its crew, and generate science. This proposal outlines the Core Concepts of Telescience, its thematic and gameplay design principles, and its general functionality.

 Telescience introduces the following core concepts:

**The Teleframe**: A Round-Start and buildable set of structures centralised on a **Teleframe Core**, a structure which is capable of teleporting almost anything nearby it or its selected Target either to the Target (Sending) or from the Target to itself (Receiving).
-  *Teleframe Consoles* are connected by the Player to a Teleframe Core via a multitool. This structure allows the Player to set a teleportation Target, either through directly inputting coordinates, or selecting a linked Teleport Beacon.
-  *Teleport Beacons* are items that the Player can create and link to a Teleframe Console, when anchored it will be selectable by the Player from that Teleframe Console to act as a Teleportation Target, even if the beacon is on a seperate moving grid or another map entirely.
- Teleframe Cores can have a random chance upon teleportation determined by their Incident Chance characteristic to cause **Teleportation Incidents**. Which cause Anomalous Effects on the surrounding environment.
-  *Teleframe Upgrades* are researchable structures that can be built by the Player directly adjacent to the Teleframe Core, modifying its base characteristics, or providing new special features.

**Reality Fractures**: Anomaly-like entities that create minor but noticable Anomalous Effects on their surroundings. They are usually entirely invisible and make no sound unless pulsing. They can most easily be detected and destroyed using Bluespace Depthcharges.

-  *Bluespace Depthcharges* are items the Player can create, that upon teleportation will detect Reality Fractures within a large radius and state the distance from themselves. Within a shorter radius, they will generate science and the cost of damaging the Reality Fracture.
- If the exact location of the Reality Fracture is found, an Anomaly Synchroniser may be Anchored underneath it and activated, which will reveal the Reality Fracture, allowing it to be scanned and studied similar regular anomalies, however they will continually degrade in this state.
- Destroyed Reality Fractures produce more potent Anomalous Effects upon their destruction. With intensity scaling with how efficiently it was destroyed, the fewer Depthcharges used, the more efficient.
- Destroyed Reality Fractures drop **Anomalous Shards**, which are capable of replicating the Anomalous Effects of the the Reality Fracture, or that of Teleportation Incidents. These can also be scanned and catalogued for additional science.

**Anomalous Effects**: The overall effects produced by Teleportation Incidents and Reality Fractures which are responsible for providing risk and additional reward of using the Teleframe.

- Anomalous Effects scale from Minor, to Moderate, to Major, to very rare Malefic effects, representing the impact the effect has on its surroundings. These effects may be Beneficial or Detrimental. They may occur at the teleportation Target or Source (the Teleframe Core).
- These effects may be instantaneous, status effects, or semi-permenant.

### Themes
The Teleframe aims to replicate many of the tropes of Teleporters within fiction, while leaning on the inherent dangers shown in Transporter Malfunctions of *Star Trek* or the Perils of the Warp of *Warhammer*. The teleframe can be calibrated to take you anywhere in the same map if you know the coordinates, and anywhere else you can reach with a Teleport Beacon. Letting you extract those lost in the depths of space, beam down to entirely seperate planets, and warp to shuttles in the middle of FTL space.

In the Universe of *Space Station 14* the Teleframe is thematically designed around the idea of punching holes through the fabric of reality and into the underlying Bluespace, linking two points together to push or pull entities through it. Teleportation Incidents represent the unstable Bluespace energies flowing back out into reality, and either rationalising themselves into Anomalous Effects, or even simply pulling through thingss from entirely seperate points in the universe that may have been lost in space for eons.

Reality Fractures meanwhile represent places where the fabric is thin or damaged, allowing these energies to seep through naturally. This leads to effects that some would brush off as simply "Space Madness". With it taking a more perceptive mind to realise there is something more to the strange disturbances.

The discipline of Telescience therefore studies these Fractures and their effects, deliberately triggering them via Bluespace Depthcharges teleported from Nanotrasen's standard issue *Experimental Teleframe Core*, and observing the response on both sides of reality. Then, potentially finding use for the crystalisation of these Anomalous effects for the station at large beyond simply the knowledge those observations provide. Naturally however such experimentations will be far from safe.

## Background
While Science provides benefit to the station in the form of their researched technologies and the ability to make new things, the tools with with they do research rarely themselves provide much benefit to the station.

Anomalies are almost always a direct threat to the station, with only Rock and Electric Anomalies capable of providing limited use. Some Artifact effects, such as generating materials, can provide benefit, however they are often limited in their ability to be exploited.

For the most part, they are tools whose primary purpose is to generate science points. Other effects are often secondary at best. Which can leave little room for skill expression beyond the ability to most efficiently generate points or make the most of what secondary benefits there are.
  
The Teleframe is built inversely to this, an incredibly powerful mobility tool that also happens to be able to be used in scientific research. With that scientific research also producing Anomalous Shards capable of strange effects.

## The Teleframe
The Teleframe Core is the structure responsible for teleportation, it is directed by the Teleframe Console it is connected to.  A Teleframe Core may be connected to multiple Teleframe Consoles, but each Teleframe Console may only connect to one Teleframe Core.

While Teleframes are intended to be most associated with Telescience, there is potential for other implementations, such as Syndicate Teleframes.

Similarly, Teleframe Cores should not be limited to only being a structure, Console and Frame could theoretically be combined into a single item. Although such a device would need to be heavily restricted.

### Function
Teleframe Cores have characteristics that determine how they function. Upgrades or Events may modify these characteristics:
- Teleport "To" and "From" Entities (required)
- Teleport and Scatter Radius (required)
- Charge and Recharge durations (optional)
- Idle and Active Power draw rate (optional)
- Teleport Start, Finish, and Fail Effects (optional)
- Teleport Incident Chance and Multiplier (optional)

To Teleport, the Player can either input a set of coordinates, the same as those used by a GPS, or select a previously linked Teleport Beacon. For Teleportation to be allowed the following conditions must be met:
- There must be a Teleframe Core linked to the Teleframe Console.
- The Teleframe Core must be powered and charged.
- Valid Coordinates must be input. Coordinates outside a maximum range should be denied, to prevent teleporting millions of tiles.

If these conditions are met the Player can initiate Teleportation, choosing to either "Send" (Source to Target) or "Receive" (Target to Source). 
The Teleframe should produce a Radio Message indicating Teleportation has been initiated, the coordinates of the target of this teleportation, and which station beacon it is closest to.
An initiated Teleportation event will create two "Teleport Entities" at the Source (the Teleframe Core) and Target and begin the process of Charging. It may also produce a Teleport Start effect alongside this.
A Teleframe Core should charge for a set time before teleportation occurs, allowing time for those at the target to react, and those teleporting to get into position if needed.
Whilst charging, the Teleframe Core may enter an Active State, drawing a higher level of power than its Idle State, and so put a notable strain on the station's power supply. 
A further series of checks should be made by the Teleframe Core at the start and end of the charging period. If these fail, teleportation will fail to complete.
- If the Target is in free space (no tile beneath), a "Send" Teleportation will fail. Receive Teleportation will function. This prevents teleporting things into deep space never to be seen again, but still lets you retrieve someone who might be lost in space.
- If the Target is inside a wall, Teleportation will fail.	Teleporting into walls is awkward.
- If either Teleport Entity is destroyed or EMP'd, Teleportation will fail.	A Teleport Entity may be deleted by a Singularity, or an Opponent may wish to prevent Teleportation occuring.
- If the Teleframe Core loses power for any reason, Teleportation will fail.

Teleportation Failiure should be accompanied by a failiure effect and message diagnosing the reason for failiure.
If the charging period completes successfully, Teleportation will occur:
- All valid entities within the Teleframe Core's Teleportation Range will be teleported either to or from the Target, and should be Scattered slightly by the Teleframe Core's Scatter Radius Characteristic so they do not appear on top of each other.
- Entities should not be teleported if they are not valid, which is under any of the following circumstances:
	- The Entity does not have physics.
	- The Entity is Anchored.
	- The Entity is on the Teleframe Core's Blacklist (EG: Unanchored Walls and Windows, Singularities and Teslas).

After Teleportation of all entities has concluded, a Teleportation Incident may then occur based on the Teleframe Core's Incident Chance Characteristic. Teleportation may also be accompanied by an effect of some kind, such as a Bluespace Flash.	

Afterwards, the Teleframe should recharge for a set period of time before it can be used again. During this period, the Teleframe Core can continue to remain in an Active state, drawing a large amount of power. If insufficient power can be provided, recharging should be halted until it can.

Once Recharging has completed, the Teleframe Core returns to its Idle state, and may be used again. 
>Jane Salvager has gotten herself lost in space without a jetpack, although she does have an Astronav Cartridge to know her coordinates. She shouts her coordinates over the radio.
John Scientist has access to the Science Department's Experimental Teleframe Core, using its console he plugs in those X and Y coordinates and presses "Receive".
The Teleframe Core creates a distortion as it connects to the targeted location, and after a few seconds of charging Jane is teleported back onto the station in a flash of light. The experience leaves both of them light headed as a minor Teleframe Incident occurs.
The Teleframe Core then enters a state of recharging, and won't be able to be used again a period of time.

### Peripherals
Peripheral items and structures support the use of the Teleframe but are not mandatory for its function.
Chief amongst these is the Teleport Beacon. The Teleport Beacon can be created by the player at round-start, when linked to a Teleframe Console and then anchored it would be selectable as a target.  This has immediate uses:
- A player could have a teleport beacon set up on the ATS to allow immediate extraction of purchased goods
- A Teleport Beacon set up on a seperate map such as an expedition would allow traversal to and from to extract looted goods.
- A Syndicate agent could set up a Teleport Beacon on the Evacuation shuttle, and have their stolen contraband teleported to them even after the shuttle has evacuated, bypassing an evac shuttle search.

Upgrades
Upgrades would represent special chips that unlock new functionality or improve the baseline characteristics of the Teleframe. For Teleframes, these would be inserted into Teleframe enhancement structures that could be built adjacent to the Teleframe Core. These upgrade chips could also be placed into other structures to improve their function, such as increasing the speed of a Lathe, or having it provide a small amount of science when an object was printed.

Upgrades would be important to mechanically improving the process of Telescience, or using the Teleframe in general by increasing its recharge and charge times but making incidents more intense, making it less likely to experience incidents but increasing charge times, or increasing its chance of incidents in exchange for more science production.

Research
- Further Research in the Science department can unlock new Teleframe-related technology, from new modules to equipment.
- The Handheld Teleframe Console would allow a user to access a teleframe remotely, with it possessing a built-in Teleport Beacon letting them target themselves on the move.

## Telescience
Telescience follows the theme of the Teleframe's ability for traversal and extraction. There are two ways to engage with Telescience.

The first being through the gameplay perspective. Teleporting a Bluespace Depthcharge to a random location on the station and seeing if it detects anything, then triangulating the position through several further teleports to nearby locations, before finally hitting the exact location of the target. This method encourages a level of mechanical skill, and the satisfaction of sniping a Reality Fracture without ever having seen it purely from mathematically deducing its coordinates.

The second method of Telescience is through the roleplay perspective. While Reality Fractures are invisible their pulses provide evidence of their existence, nearby players will notice oddities around them that have more in-world meaning than "Anomaly near bar". By interviewing the nearby crewmembers the scientist can deduce a nearby Reality Fracture may be present, and if they remain on-site or work with the affected crewmembers when a Depthcharge is teleported, they may be able to spot where the Reality Fracture is as it is revealed from a scan. Here, there is roleplay and cooperation to discover a Fracture based on its effects rather than purely gameplay deduction.

>Jane Bartender has noticed the walls in the dining area are slowly rusting over, as filth spreads seemingly from nowhere. She calls over John Scientist to see if he can make heads or tails. John Scientist brings a GPS with him, and gets the coordinates near to where Jane heard a strange pulsing sound. Requesting a coworker load a depthcharge onto the teleframe and send it, they both observe as a Reality Fracture appears in Jane's room. Homing in on its exact position, they excise the Fracture from a safe distance with a direct hit, and watch as the Supercritical Meltdown fills the room with drunk mothroaches and ammonia.

### Reality Fractures
Reality Fractures are the source of science points for Telescience. They function similarly to Anomalies, possessing periods of inactivity followed by pulses that create a variety of Anomalous Effects.

Unlike Anomalies, Reality Fractures are silent and invisible, only producing, at most, a brief sound when pulsing.
Additionally, there are not "Types" of Reality Fractures, instead each Reality Fracture has a randomly generated set of Minor to Moderate Anomalous Effects that it may activate on pulsing.

Reality Fractures typically remain stable indefinitely if not interacted with by the Player. 

Reality Fractures can be created round-start in a dormant state that activate over time, as a side effect of generating anomalies or allowing them to go supercritical, as a rare result of Major Anomalous Effects, and other seperate events during the round. There should be a maximum number of Reality Fractures that can exist at any one time based on crew population.

Destroying Reality Fractures results in them entering a supercritical meltdown, this meltdown is weaker the more times the Reality Fracture was scanned. Meltdowns result in a series of Anomalous Effects being produced, Supercritical Meltdown intensity is also affected by the Incident Multiplier of the Teleframe used, especially if the killing blow to the Reality Fracture happened to also cause a teleportation incident which can stack the effect even further, such stacking would be the only way to create potential Malefic anomalous effects or shards that can alter the flow of the entire shift. 

To destroy a Reality Fracture with no effects, one can alternatively use an Anomaly Synchroniser. If anchored and activated directly on the location of the Reality Fracture, it will link to it and make it visible. Allowing it to be interacted with like a normal anomaly. When connected to an Anomaly vessel it will drain all Science Points out of the Reality Fracture, and upon running out it will disappear harmlessly.

### Gaining Science
Bluespace Depthcharges are the primary method of detecting and destroying Reality Fractures. These can be created by the Player round-start. A Bluespace Depthcharge has a large detection radius and a smaller scanning radius. When teleported it will report over radio the distance from itself to all Reality Fractures within its detection radius, and gain science from all Reality Fractures within its scanning radius. Each Reality Fracture would be provided a unique ID to keep track of it if multiple were detected.

The amount of science gained from scanning a Reality Fracture is inversely proportional to how close the Bluespace Depthcharge is. A Reality Fracture on the edge of the scanning radius will provide far less science than a direct hit. A Scanned Reality Fracture will also immediately pulse, unlike regular pulses this will also briefly reveal the Reality Fracture, allowing someone on the scene to potentially identify its location. Scanned Reality Fractures receive damage whenever they are scanned, and will eventually be destroyed.

Bluespace Depthcharges do not immediately provide their science to a server, instead, they must be collected and returned to the Science Department, with the science points directly deposited in a server similar to a Research Disk. The Bluespace Depthcharge is not destroyed however, and can be continually reused.

A skilled Scientist could use the coordinates of the teleport location, combined with multiple teleported Bluespace Depthcharge detection results to triangulate the position of a Reality Fracture, allowing a final Depthcharge to strike directly on the target for maximum science gain. Although proper communication, and a second member on the scene to immediately identify the potential location of the Reality Fracture would be more efficient if a rough location was already known.
  
## Anomalous Effects
Anomalous effects are the generic term for the various effects produced by Teleportation incidents, Reality Fractures pulses, Supercritical Meltdowns and other events. They are essentially the chaotic element of Telescience, similar to Artifact Effects. 

Anomalous Effects have four categories:
- Minor Effects: Mostly harmless, mildly beneficial, and very localised effects with short term or trivial impact on the shift.
	These Effects can be caused commonly by Reality Fracture pulses or teleporter incidents, they are every-day affairs.
	Spawn 5-10 of a random ore, give a brief burst of speed, create strange sounds, make the player vomit, create a flashbang effect, create a strong gravitational pull or push for a few seconds, Rust and Dirt the surrounding walls and tiles, create a spill of a common reagent, cause people to start bleeding slightly.
- Moderate Effects: Mildy harmful or reasonably beneficial, somewhat localised effects with short term or notable effect on the shift.
	These effects are rarely caused by Reality Fracture pulses or teleporter incidents. 
	Moderate effects: Heal surrounding players, spawn 1-3 stacks of 10 of a rare material such as gold, create a random selection of low value cargo crates, spawn a space carp, shatter nearby glass, create a small explosion of mild damage, scatter teleportation participants over a large area, create a spill of a poison or medical ingredient.
- Major Effects: Considerably harmful or very useful, with long term or significant effect on the shift.
	These effects are caused by Reality Fracture Supercritical Meltdowns, or rarely by Teleframes with high Incident Multipliers
	Major effects: Spawn a small horde of valuable materials or money, spawn a high-value cargo crate, replace an organ with that of a different species, shoot lightning, spawn a goliath, give someone an anomalous infection, create a loud and unstable crystal item that will explode violently in 30 seconds. Create a spill of space lube. Cause several Moderate or Minor Anomalous Effects all at once.
- Malefic Effects: Existentially threatening or Round-altering effects that can change the entire dynamic of the shift. 
	These effects are caused exclusively under worst-cased conditions of Supercritical Meltdowns from teleframes with high incident multipliers.
	Immediately turn the nearest person into a Wizard, create a portal that after a few seconds calls forth several zombified monsters, creates a highly radioactive item that, after 2 minutes will spawn a singularity. Create an item that will repeated create lighning, after 2 minutes it spawns a Tesla ball. Spawn several new anomalies and reality fractures, after 5 minutes cause every anomaly and reality fracture on the station to supercrit. Repeatedly spawn major, moderate, and minor anomalous effects for a minute, integer overflow the station's cash reserves for one minute.

To summarise, only Minor and Moderate effects should be able to occur without direct player input. Reality Fractures for example are not the same as anomalies, they are not designed to be immediately obvious in their effects. Instead tapping into the idea of "Space Madness", where strange effects occur without obvious source, and the crew can't be entirely why. If an anomalous effect produces a sea of dangerous monsters that leave several dead, there was a player that was at least somewhat responsible for it, even if it was simply that they got unlucky.

### Anomalous Shards
Anomalous Shards are in effect the continuation of xenoarcheology's originally promised artifact shards. Each shard contains one or more anomalous effects that can be activated by using the shard. This effect has a cooldown before re-use and finite number of uses before going dormant. A dormant Anomalous Shard would need to be restored with Artifact Glue, then re-activated by activating an internal "trigger", the same as an artifact. At which point it would be able to be used again.

Undesired Anomalous Shards can be ground down for Artifexium.

In general, the more intense the shard's anomalous effect, the more likely it will have minor sub-effects. For example, a shard that can create silver ingots may also make everyone nearby vomit.

Events may cause random mundane items to inherit the properties of an Anomalous Shard. The Chef's kitchen knife may suddenly gain the ability to turn meat into flesh creatures.
