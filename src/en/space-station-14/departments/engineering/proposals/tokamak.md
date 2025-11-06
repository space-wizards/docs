# R-ANGL Tokamak Fusion Reactor

| Designers      | Implemented | GitHub Links |
|----------------|-------------|--------------|
| ArtisticRoomba | :x: No      | nuh uh       |

## Background
Currently, Upstream Atmospherics is lacking in interesting engine design or gas-based mechanics.

The Thermo-Electric Generator (TEG) is a great example of this, suffering from monotony.
While multiple interesting solutions exist to the TEG's problem due to the emergence of atmospherics devices, these solutions often result in an engine that rarely offers any interesting or emergent gameplay post-setup, especially with other departments. The standard gameloop is to pray that someone knows how to set up the engine and just wait until the shift ends - rarely does the chamber need to be refilled and a burn re-lit for more hot gas.

Note that even with the recent changes to the TEG encouraging dual-loop designs and punishing extremely basic single-loop designs, the TEG's core problems still remain.

A large component of the TEG's problem is the lack of interesting gases and the means to synthesize them. Tritium is synthesized as a by-product of burning plasma at specific conditions, leading to a free large heat boost that invalidates any sort of care for efficiency or optimization - the most people are worried about in that sense are making sure they didn't invert their burn chamber ratio.

Gas synthesis gameplay is generally boring. Frezon setups are largely copied from external sources or reconstructed from memory - there is no intuitive way for players to discover frezon synthesis. Additionally, the only two relevant gas reactions (tritium and frezon)

## Proposal
This proposal plans to introduce the R-ANGL Tokamak Fusion Reactor, a machine that gives engineers a relaxed pressure and temperature constraint environment in which the fusing of new gases can take place. Atmos techs have to manage new and interesting constraints associated with maintaining the environment, which happens entirely in the tile space, just like a standard burn chamber.

### Inspiration
The fusion reactor concept is largely inspired from SS13 Baystation's R-UST Fusion Reactor, which primarily serves as a means of generating power for the SEV Torch. The reactor has a magnetic confinement field that must be powered and brought online. Fuel is inserted and a massive laser is fired to start the reaction and keep it going.

The thing that was most attractive about the R-UST was the fact that it was a machine with reactions and operations happening entirely in the tile space. This is much different from the currently available downstream Hypertorus Fusion Reactor (HFR). The reactor is extremely cool, however it is more akin to a black box where gasses go in an out with not much player interaction apart from changing settings.

## Core Mechanics
### Magnetic Confinement
Gas is confined magnetically by a set of extremely powerful electromagnets located in a ring around the chamber as well as in the center.
This forms a donut in the chamber where only gas can reside, preventing it from touching the walls and interacting with them. Gases will flow naturally from unconfined to confined areas, allowing pressure and heat to build beyond the regular pressure limit of most atmospherics devices.

Gases can be extracted from the chamber via any extraction device residing in the confined section of the chamber, and inserted via any non-confined area in the chamber.
This allows any high temperature or pressure reaction to take place in the reactor, with Atmospherics Technicians left with the tasks of maintaining reactor confinement as well as the requirements of the desired reaction.

### Confinement Operation
As mentioned previously, confinement is generated and maintained by a series of electromagnets.

The current strength of the confinement is known as the _tesla field strength_ and is an all-around quantifiable value for the current health of the reactor's containment field.
Engineers can see this value, with UI elements detailing minimum safe values and how this can increase or decrease depending on the actions that can be taken by the player.

The confinement electromagnets require power and cooling. Their power requirements are proportional to the temperature of the electromagnet, with higher temperatures requiring greater power to maintain the same tesla field strength. This leads to the following:
- Engineers are encouraged to set up cooling for their electromagnets using standard space cooling loops or powered equipment.
- Batteries can be used to help compensate for a magnet whose cooling system has failed, keeping the field strength high before engineers take measures to lower the field strength (whether it be venting off pressure, bleeding off heat for use in the TEG or wasting into space, or decreasing the size of containment).

Higher chamber pressures require a higher tesla field strength in order to contain.
The size of the confinement can also be controlled by engineers, with larger confinements requiring a greater field strength.
This encourages engineers to seek better methods of cooling (whether it be spamming high-wattage thermomachines or taking advantage of the frezon decomposition reaction) in order to sustain high-pressure, high-volume reactors.

All-in-all, this leads to a balancing game where engineers are encouraged to toy with their reactor, enabling faster and hotter reactions.
It's important that the tesla field strength balancing game should be intuitive and follow the player's expectations, with proper feedback given as to what the player can do in order to raise or lower the field strength.