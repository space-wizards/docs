# Station Air Recirculation (HVAC)

| Designers      | Implemented | GitHub Links |
|----------------|---|---|
| ArtisticRoomba | :x: No | TBD |

## Background

Currently, Space Station 14 Atmos handles air on a replenishment system: air is simply stale in a room and its upkeep is managed by scrubbing waste gases, and replenishing air if it's lost.

This is okay, but this system falls apart when atmospheres experience temperature and pressure upsets, as the air in the station is not recirculated.

## Proposal

This proposal plans to introduce a pressure-based recirculation system, where temperature controlled air can recirculate to maintain a stable atmosphere. Air will flow from a slightly higher pressure air vent (at 110.325 kPa for example) and move to lower pressure air scrubbers. This gas is then recycled, temperature-controlled, and reintroduced into the atmosphere through Distro.

This proposal also plans to move away from infinite gas reserves, to promote the usage of the station's recyclernet. Gas miners will be tuned to produce less gas, to ensure that the station's air reserves are not infinite.

## The Problem

Currently, air scrubbers **do not** regulate a room's pressure; they simply regulate the waste gasses in the atmosphere. This is a huge problem, as with a lack of pressure regulation, a room can easily become dangerous with a simple temperature change. Take the two examples below:

1. Heat-based temperature upsets. This includes things like fire anomalies, hyper-convection lathes, and lit plasma/tritium.
2. Cold-based temperature upsets. This includes things like ice anomalies, frezon, and room spacing.

In the event of a heat-based temperature upset, an air scrubber will simply scrub the high-pressure waste gasses and nothing else.
An atmos tech has to manually drag a station heater (a machine that some stations don't even have roundstart) and set it up in the area to fix the problem.
The solution most techs execute is to simply space the gas and refill the room with fresh air. The panic mode on scrubbers is not viable, as it simply operates too slowly compared to RCDing a hole into space.
**This is not viable given the current atmos roadmap (no infinite gas), as we are actively spacing useful gasses!**

In the event of a cold-based temperature upset, air will cool and lose pressure, causing more gas to replace the present vacuum.
This often leads to a room being made too cold for reptilians (and soon most other species given more time).
This also leads to more gas entering the room, which drains the station's air reserves (if the station's air reserves were not infinite) and creates a dangerous pressure bomb if the air were to be spontaneously re-heated.

Additionally, Atmos techs are largely discouraged from using the station's recyclernet, as recycled high-temperature or low-temperature gasses are free to mix with regular temperature gasses, which then get redistributed to the station, heating or cooling the entire station to dangerous levels, which is hilariously hard to undo, given the lack of a station-wide cooling system.


## Solution / Core Changes
### Gas Life Cycle
Under gas recirculation, gas is to follow a gas life cycle. This cycle is as follows:
1. Oxygen and Nitrogen flows from gas reserves to a gas mixer.
2. This gas mixer sends the air to a temperature-controlled mixing chamber, which cools or heats the gasses to standard temperature (293.15 K).
3. The mixing chamber sends the air to the station's distro.
4. An air vent pushes the distro air into the atmosphere at a slightly higher pressure than standard atmospheric pressure (above 101.325 kPa, for example this could be set to 115.325 kPa).
5. The higher pressure air naturally flows to a lower pressure air scrubber (which scrubs ALL gasses until it reaches standard atmospheric pressure, 101.325 kPa).
6. The air is removed from the atmosphere via the air scrubber and sent to the station's wastenet.
7. The station's wastenet sends the air to the station's recyclernet, which filters and recyclers the gasses back to the gas reserves.
8. The cycle repeats.

This allows proper flow-based atmospherics and the proper control of station temperature (and indirectly, pressure)!

### The Gas Mixing Chamber
The gas mixing chamber is a new system that will have to be enabled at the start of the shift. This system uses a series of radiators exposed to space and a burn chamber to heat or cool the air in the chamber dramatically. To explain it linearly:
- The chamber will have two radiator loops, one for heating and one for cooling.
- The air injector (from the gas mixer) is placed so that air has to flow across the radiator loops to reach the passive vent (which leads to distro).
- An air sensor will be linked to two air alarms, one controlling the hot loop and the other controlling the cold loop.
- The cold loop air alarm will be set to alarm when the tempreature is above 293.15 K, and the hot loop air alarm will be set to alarm when the temperature is below 293.15 K.
- The air alarms will send signals to signal valves on their respective radiator loops to control the flow of hot or cold coolant to the radiator loops.
- Gas will flow across the radiator loops, heating or cooling the gas to standard temperature, based on what is commanded (heating or cooling, based on the current temperature of the gas).

This system allows the cooling or heating of the station's air to standard temperature, which is then sent to the station's distro.

Below is a visual flowchart of the gas mixing chamber, describing a potential solution to the problem:

![image](https://github.com/user-attachments/assets/1f2c42a9-801b-48c6-bded-47537b7bac30)

### Moving Away from High-Pressure Infinite Gas
Previously, air reserves were infinite and can be replaced at any time.
This basically invalidated using the recyclernet to recycle air, as it was easier to just space the gas and replace it with fresh air.

With the proposed system of recycling gasses, the station no longer has to have an infinite supply of gas.

To promote the usage of the recycling system, gas miners will be tuned to produce much less gas.
Now, the station's air reserves are a less infinite resource. Atmos will be forced to reduce, reuse, and recycle the station's air.

This does go against the current approved design document for Atmos, which states that the station's air reserves should be finite and gas miners should be phased out.

However, we still want a small trickle of incoming gas for multiple reasons:
1. **To make Atmos independent from Cargo.**
   - With total reliance on Cargo for gas, Atmos is at the mercy of Cargo's incompetence or malice. A huge spacing could leave Atmos gas-negative and they can do basically nothing about it, as the only way to import gasses is through cargo.
     - This could be countered by increasing the capacity of air tanks, but we start running to realism issues with container volumes, which was already brought up with similar PRs. Additionally, I think this is a noobtrap/death spiral that should be avoided at all costs.
2. **To ensure burn chambers are still viable.**
   - Burn chambers should still be viable for power generation and frezon production. The station should recieve at least some gas, without invalidating the entire point of the reduced output of gas miners.
3. **To have a safety net to fall back on.**
   - Atmos is extremely integral to the station and a lack of gas could lead to a station-wide crisis. It is best to simply have a small trickle of gas to ensure that the station does not run out of gas, while promoting gas recycling.
     - I understand this is a repeat of Point 1 but I would like to get this point out on paper because I believe that it is important. Just like the AME (not an extremely perfect analogy), Atmos should have something to fall back on. Maybe make the gas miners take power from the station?
     - Hypothetical: "CE here. An atmos tech accidentally set up the recyclernet wrong and spaced all of the station's gas. Cargo has no money and we are unable to pressurize spaced areas." and shortly thereafter, "The emergency shuttle has been called."



### Required Changes
Major changes are required to station setups, but the core systems are already present in the game. The following changes are required:
- An air mixing chamber, with the necessary cooling/heating infrastructure, will have to be mapped to all stations. Some stations do not have an air holding chamber currently.
- Air scrubbers will have to be changed to scrub all gasses, not just waste gasses. Additionally, air scrubbers will need the PressureBound system added to enable the prevention of drawing gasses from a room past a certain pressure.
  - This change might be too breaking. An alternative "return vent" could be mapped to the station, which would allow the return of air to the station's recyclernet. This honestly makes more sense, as we're dealing with vent-based gas flow now, not scrubber-based gas management.
- The ExternalBound of air vents will have to be changed to allow the venting of air at a higher pressure than standard atmospheric pressure, to promote the natural flow of gas.
- A more complex air alarm may have to be implemented to handle the valve-based control of cooling and heating (perhaps a computer system?).
- Tests and observation will have to be done in order to tune gas miner values to ensure that the station's air reserves are not infinite, but still have a small trickle of incoming gas for burn chambers.

### Benefits (Arguments for the implementation)
1. **Proper atmospheric flow.**
  - This system allows for true, flow-based atmospherics (HVAC) which is a highly complex system, present in real life. This gives Atmos another level of depth and distracts away from sitting in the department waiting for something to happen.
2. **Station-wide temperature control.**
  - This system allows for the proper control of station temperature, which is currently a huge issue. Atmos currently has no easy way to modify the station temperature en-masse.
3. **Emergent gameplay based on the Ideal Gas Law.**
  - Savvy Atmos techs can take advantage of the Ideal Gas Law to create interesting solutions to station problems. For example, the station's temperature can be increased slightly to increase the effective pressure of the station's air, helping to alleviate a potential gas shortage before more gas is acquired.
4. **Centralization of station waste gas removal.**
  - Gas circulation means that all gasses, including waste gasses, are sent to the recyclernet, enabling recycling on a station-wide level, not a room-by-room level.
5. **Gives Atmos a proper system to manage and keep watch.**
  - Atmos now has to oversee the station's temperature and gas reserves, which requires constant monitoring and maintaining.
  - Engineering, in comparison, has the power of overseeing station power, a system which requires constant monitoring and maintaining (singulo gas tank refilling, tesla coil repairs).
6. **Moves away from infinite gas.**
  - This system moves away from infinite gas, which is a huge issue in the current atmos system and is a goal in the **Atmos Roadmap**.
  - As previously mentioned, Atmos techs can space and refill rooms with zero consequence of wasting gas. All problems with bad air can be inherently fixed by just replacing the room's air.
7. **Encourages the usage of Frezon gas in radiator loops.**
  - In the future, Frezon can be used as a highly effective working gas for use in radiator loops. Cooling and heating an entire station requires a lot of energy and work to be done. Normal gasses might not have thermal properties good enough for conducting heat fast enough.
8. **More agency for antagonists.**
  - Antagonists can now sabotage the station's air supply, which can lead to a station-wide crisis. This can be used to create interesting rounds and scenarios. However, the ease at which this can be accomplished presents greater issues, explained in Drawbacks.
9. **Encourages greater care with station atmos setups and adds value to gasses.**
   - With this change, all gasses are now extremely valuable. Spacing a room's air is no longer a viable solution, as the station's air reserves are no longer infinite. Atmos techs now have to take extra care and ensure that holes are fully patched before filling a room.
   - This will also lead to Atmos taking great care to ensure that further gas does not escape to space when moving between firelocks. This reinforces the usage of holofans.
     - Holofans should also see a slight buff to encourage their use and to compensate for the change removing the Firedoor Remote.
   - This change also encourages Atmos to spend more time ensuring their setups are correct, as a mistake could lead to wasting precious gas or dealing with an expensive-to-fix mess.
### Drawbacks (Arguments against the implementation)
1. **Potential for easy and devastating mass station sabotage.**
  - While it could be argued that this could lead to emergent gameplay and hostage roleplay, it could also lead to 5 minute rounds.
  - All air returns to a central location, so it is incredibly easy to simply replace all of the air with a harmful gas (carbon dioxide or pure nitrogen).
  - The entire station's temperature is controlled by two air alarms. It is very easy to sabotage these air alarms and deep fry or freeze the station.
    - This has some implications for the future Malfunctioning AI gamemode, as they can easily sabotage the station's air supply under Atmos' nose (superheating/supercooling), although this instantly outs the AI and the crew will work to kill the AI posthaste.
  - This has some counterarguments, though:
    - Mass station sabotage is prohibited by the rules. Familiarly, mass sabotage like this isn't exactly a huge undertaking, similar to someone snipping wires on a Tesla/Singularity containment.
    - Because of the flow-based nature of the system, it is possible to detect and fix the sabotage by simply undoing the sabotage. However, half the station could be dead by the time this is done. What are you gonna do? Un-steam half of the station?
  - This proposal introduces another source of mass station sabotage with a very neutral counterbalance. Right now, changes should be working towards the goal of making mass station sabotage before the 30-minute mark harder.
2. **Potential performance issues from mass gas flow.**
  - This system introduces a lot of gas flow by design, which could potentially cause performance issues. The atmospherics system should be properly tested to see if servers can properly handle the load, and optimized if necessary.
3. **Reduced oxygen available for burn chambers.**
  - With the tuning of Gas Miners, the station's oxygen supply is now less infinite. This could potentially lead to a lack of oxygen for burn chambers, which could be a problem for the station's power supply. We want to promote the usage of the Thermo-Electric Generator (TEG) as a power source, and this could potentially hamper that.
  - This could also hamper the production of Frezon, something we still want to promote.
  - Obviously, I'm just outlining this as a point that this is something that requires tuning. We want to make burn chambers possible for Frezon production and the TEG, whilst preventing the circumvention of the HVAC system. 

## Future Systems

In the future, the following systems could be implemented to further enhance the station's atmospherics simulation, to encourage the setup of whole-station HVAC:
1. **All lifeforms radiate heat into the atmosphere.**
  - Now that the station's air is temperature-controlled, lifeforms can radiate heat into the atmosphere. This encourages the setup of HVAC, as the station's air will naturally heat up over time, making the station stuffier over time.
  - To encourage this even further, we could introduce a system where lifeforms experience further discomfort if the station's air is too hot or too cold (rather than simply taking damage).
2. **All lifeforms sweat (or otherwise emit/exhale water vapor).**
  - Now that the station's air is recirculating and managed at a central place, lifeforms can sweat, which will increase the humidity of the station's air.
  - This could warrant the creation of a humidity system, which could be used to further enhance the depth of the atmospherics system.
  - This could also be used to create a system where lifeforms experience further discomfort if the station's air is too humid or too dry, which could give Atmos another aspect of air to manage.
  - This system could have parallels with the current presence of water vapor.
3. **Advanced programmable computers that can preform complex logic.**
  - Managing temperature and pressure is complex for air alarms. A computer system could be implemented to handle the valve-based control of cooling and heating station air.
  - This can also enable the precise regulation of pumps to control the specific power of heating and cooling.
    - This is **exactly** what modern thermostats and air conditioning units do in real life to increase efficiency and reduce energy consumption. Rather than running an AC compressor at full power, the compressor is run at a lower power to maintain a specific temperature.
  - This system has **huge** potential for emergent gameplay, as savvy Atmos techs can use applied mathematics (Ideal Gas Law, Thermodynamics, Specific Heat Capacity, Energy In/Out) to create complex solutions to station problems.