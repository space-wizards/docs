# Station Powered Energy Stimulation System - aka the "Big Laser"

| Designers | Implemented | GitHub Links |
|---|---|---|
| Compilatron | :x: No | TBD |

## Overview

The "Station Powered Energy Stimulation System" (which will be referred to as the "SPESS") is an engineering machine which serves the function of producing spesos or materials in exchange for power and sufficient cooling.

## Background

As of currently, there are a few ways engineers can boost a station's power production, but there is no reason to do so since excess power is voided. This means that a 400kw singularity and a 6MW TEG are interchangeable as far as powering the station goes.

The solution existed in 13, in the form of the Power Transfer Laser, a machine which would beam energy off into deep space in exchange for money. The purpose of the PTL is to reward engineers for going above and beyond - exchanging extreme amounts of power for money. 

However, the PTL suffers from being a one dimensional machine. Although the source of power may differ, the PTL doesn't offer any interactivity besides pumping more power into it. The SPESS intends to diverge from this by offering it's own mechanics to optimise for.

## Features to be added

### Reflectors

Reflectors are reflective panels which can be finely angled to any direction desired. They reflect energy beams such as lasers, emitters or the SPESS. They have utility in eccentric singularity/tesla setups, to redirect emitter lasers towards containment field generators, or for the too-be-mentioned SPESS. They come in two variants.

- Mirror reflectors, which reflect projectiles like a mirror, flipping the trajectory along the panel's normal.
- Prism reflectors, which direct all projectiles into the same direction

### The "Station Powered Energy Stimulation System" (SPESS)

The SPESS is a multi-part machine, similar to the particle accelerator. It should be included on stations round start, and should be positioned in a location external to the station, which allows easy EVA passage behind it to prevent interference. Alternatively, it can be provided as a crate of flat pack machines for engineering to deploy themselves.

The SPESS must feature a binary gas connection for a coolant to pass through, a HV connection for power and a control computer as separate parts. Additional parts can be included for fluff.

The SPESS has two operating modes, Power Transmission and Resource Extraction modes. These serve different purposes.

#### Basic Functionality

The SPESS is intended to be used in conjunction with reflectors to orient it's beam towards different targets for different functions. The beam can be enabled once it is properly aligned, and the SPESS will begin warming up, increasing in power until fully online.

The SPESS has a configurable power consumption - with higher power consumption producing more resources depending on the mode it is in. Resource production rates should scale logarithmically with power consumption, thus increasing power draw will have diminishing returns - but still increasing production. This is intended to make balancing the SPESS easier - to make simple setups viable, while still rewarding more advanced setups.

The SPESS produces heat when operating, scaling directly with power consumption. This heat is transmitted to the binary atmospheric ports. The temperature of the coolant will impact the SPESS depending on it's operating mode. As the cooling requirements scale with power consumption, a low power SPESS will only need a basic radiator setup, while a high power SPESS will need exotic coolants such as frezon.

#### Power Transmission Mode

Power transmission mode is similar to the traditional power transmission laser concept - with some extra caveats. It's basic premise is to produce spesos in exchange for energy.

In power transmission mode, the SPESS must be aligned to a distant power relay station. The relay station does not need to be a physical structure, it is a point in space which must be targeted.

Once the SPESS is properly aligned and activated, it will begin transmitting power to the relay. This will reward spesos to the console, which can be claimed at the console.

Coolant heat will reduce the efficiency of the laser beam. Energy consumption remains the same, while the power transmitted will be reduced. Efficiency scales linearly, 100% efficiency approaching 0 kelvin and 0% efficiency at 500 kelvin.

Spesos rewards will also slowly increase so long as the beam strength remains consistent. This is to encourage not only making a lot of power, but a reliable power source. This takes the form of a spesos production multiplier, increasing from 1x to 2x linearly over half an hour. This multiplier is lost if the beam power drops off.

#### Resource Extraction Mode

Resource extraction mode is the second operating mode of the SPESS. It provides a new method of producing basic or advanced resources, either to supplement or entirely replace mining depending on the situation.

In resource extraction mode, the SPESS must be aligned to the vgroid. Once the SPESS is properly aligned and activated, it will begin drilling the vgroid for resources. This will produce ores from the SPESS, which can then be collected and refined. This process **does not damage the vgroid**, both to allow the vgroid to still be exploited normally, and to avoid adding unnecessary server load from calculating the destruction of ores which will almost never be seen.

Coolant temperature impacts what materials are extracted. Temperatures above 500 kelvin produce no resources at all. Different materials should have different temperature ranges that they are extracted at - with higher returns the closer they are to the target temperature. These ranges should be generous, especially for common resources. Common resources should be more abundant in hotter temperature ranges, while rarer resources should require colder coolant and more precise temperatures.

This behaviour is intended to provide some interactivity with the SPESS. A basic setup will hover around a temperature range of 250-500 kelvin and extract common materials passively, while an advanced setup can incorporate freezers, frezon and adjustable radiator loops to hone in on specific materials.

#### Hazards & Safety

The SPESS is a very dangerous machine if not properly managed. Standing in the beam will rapidly heat any mobs it comes into contact with - which can quickly ash them. It can melt walls, burn objects and destroy machines. The SPESS itself includes various safety mechanisms to prevent a catastrophy.

- The SPESS beam should feature an obvious, clear bloom effect around it, allowing it to be "seen" even off screen, especially by those on EVA.
- The SPESS beam is visible on mass scanners with a distinct red line, so shuttles can clearly see it.
- The SPESS beam takes time to warm up, and is visible before it is hot enough to cause damage, giving time for those in it's path to move out of the way.

The SPESS itself has a few failsafe mechanisms that trigger automatically. These are largely intended to prevent griefing.

- If the SPESS cannot be supplied enough energy to power itself, it will shut down to prevent acting as a power sink.
- If the SPESS beam changes it's hit position (such as if the reflector has it's angle changed, a shuttle gets in the way or an entity steps in front of it), it will shut down after a few seconds if the obstruction remains. This should still be enough time to crit a careless player, but not kill them - but also prevent fast moving objects shutting down the SPESS incidentally.
- If the SPESS overheats (past 500 kelvin) it will shut down. This is beyond the range where the SPESS will function in either operating mode - and is to inform engineers that their cooling is insufficient.
- If the SPESS has no coolant it will shut down. This is to prevent cheesing the SPESS by providing no cooling.
- If a failsafe is triggered, it will remain locked out for 10 seconds before it can be turned on again. This is to encourage an engineer to address the problem instead of trying the same thing over and over.

As with most safety features, the SPESS's failsafes can be overridden by an emag. If emagged, the following behaviours are changed:

- The SPESS will no longer shut down if it can't gather enough power, allowing it to act as a power sink.
- The SPESS will not shut down if it's hit position changes.
- The SPESS will not shut down if it overheats, but will explode after overheating for too long.
- The SPESS can be immediately turned on again if any failsafe is triggered, no longer having a cooldown. The warmup delay will still apply.

#### Diegetics

It is important that the SPESS is easy to understand without requiring a full in depth explanation of it's concepts - and there should be focus on how these concepts are properly communicated. Some of these notifications should be presented via UI, while others can be presented via in-world visuals and motifs.

- Any mapped SPESS should include a reflector in front of it and a reasonable field-of-view via window, to help show players how the SPESS interacts with reflective surfaces.
- SPESS should include animations for it's warmup, possibly including a progress bar on the body of the machine - similar to the TEG - to show it is working.
- SPESS' heat mechanics should be visually portrayed, with the body of the machine gaining a warm or cool tint as it operates. A similar effect should also be applied to the TEG if implemented.

#### Additional notes on UX
Engineering a notoriously poorly communicated department - but this should not be the standard. UX designers should take care to properly communicate the status and of the SPESS and any issues it has, to reduce frustration when working with a new machine.

Any error or failsafe trigger should be logged and displayed on the SPESS console, for an engineer to review and take into consideration. Care should be taken for failsafe triggers to also check for context and provide hints as to what the root issue is and nudge them towards the solution. These errors should be easy to understand and avoid jargon. A few suggestions as follows.

**If there's an overheating error and there is not enough coolant:**
"Failsafe triggered due to overheating, ensure enough coolant is present" *Conveys the issue in easy to understand terminology and offers a solution* :heavy_check_mark:
"Overheating error" *States the issue but doesn't offer insight into the underlying cause* :x:
"Insufficient coolant, increase thermal mass" *uses technical jargon which deters players* :x:

**If the SPESS triggers it's targeting failsafe:**
"Failsafe triggered due to obstructed beam, ensure beam path is clear of any objects" *Conveys the issue and states what the solution is* :heavy_check_mark:
"Obstruction detected" *States the issue but is extremely vague. Where's the obstruction? Why is that an issue?* :x:
"Shutdown due to occluded emissions" *Uses jargon for no reason other than confusing the player* :x:

**If the SPESS triggers it's power failsafe:**
"Failsafe triggered due to lack of power, reduce power draw or increase power production" *Conveys the issue and states what the solution is* :heavy_check_mark:
"Insufficient power" *Although stating the issue, doesn't encourage an engineer to respond. Some engineers may just keep trying to turn it on until the problem solves itself.* :x:
"Low voltage error" *Voltage isn't a concept in the game. Although it makes sense realistically, this may confuse players as to the mechanical meaning.* :x:

## Game Design Rationale

The main intent of the SPESS is to raise the skill ceiling of engineering, and offer a new way for engineering to interact with the station as a whole. Currently, there is not much reason to optimise or refine any power source besides with the intent of powering the station - but the SPESS provides a goal for engineering to work towards and encourages engineers to experiment with and improve power generation.

The SPESS opens opportunities for cargo, science and engineering to work more closely together, buying equipment for new power sources, then using that equipment to produce more energy to produce more resources for more equipment. This encourages a back and forth between departments as they exchange components for resources.

There is a focus on making sure the SPESS is intuitive, with it's complexity coming from the systems it interacts with. The concept of a laser beam, the danger it poses and the heat it produces is easy to visualise and comprehend. Focus should still be placed on properly ensuring the mechanics of the SPESS are conveyed to players intuitively, via diegetic motifs and proper use of UX.

The SPESS also provides a new hazard, in the form of an easily communicated hazard "big fucking laser beam", which is a danger to the crew and a potential tool for traitors. The inclusion of safety systems is designed to punish carelessness without being easily abused. There are also plenty of strategies the SPESS can allow, such as using the SPESS as a murder weapon, power sink or weapon of mass destruction.

The SPESS also indirectly introduces new hazards by it's existence. Engineers are encouraged to experiment with and upgrade their engines in order to increase power production - which in itself introduces new risks for players, with most engines being dangerous hazards themselves - and opening opportunities for antagonists to exploit these dangers.

## Roundflow & Player interaction

The SPESS will likely see use by engineering once the station's power demands have been satisfied, and engineering is feeling comfortable with their power situation. Care should be taken when implementing it on lower pop maps, and may be excluded if it's existence would spread an engineering department too thin.

The SPESS itself includes mechanism to discourage it's use if there is insufficient power available. The listed power failsafe is directly intended to discourage using the SPESS without a sufficient power grid, and a minimum power requirement is included to ensure that the SPESS isn't used unless a reliable power source is already available.

## Administrative & Server Rule Impact (if applicable)

The SPESS inherently produces a new risk for players as it's a kill beam along a straight line. There are mechanical methods of limiting the grief potential of the SPESS, but poor implementations of these mechanics may allow for griefing, using the SPESS to kill or destroy areas of the station. An emagged SPESS does have the ability to round remove people, especially those vulnerable to burn damage, if they step into the SPESS beam. If these features prove too powerful, the damage the SPESS causes will need to be rebalanced.

The SPESS also poses a job abandonment risk, as it may encourage engineering to focus too heavily on power optimisation rather than other maintenance duties. This should be considered carefully with the implementation and presentation of the SPESS, ensuring it is a secondary objective compared to keeping the station intact.

## Technical Considerations

The SPESS involves long range raycasting - which depending on implementation, can have a performance impact. This may be taken into account and the implementation may be changed if this proves too taxing.

The addition of reflectors may require a refactor of the reflector and hitscan weapons system to work properly, as well as their aesthetics to take into account reflections and transitioning between grids cleanly.

The SPESS will need it's own UI for itself to control it's functions and communicate it's status properly. As this is a multi-part machine, individual components will need their own UI. It's anticipated that there will be UI for the following components:

- SPESS console
    - Status readout. This serves to provide listings of any errors or faults with the SPESS, as mentioned in "Additional notes on UX". These should persist and be logged even after failure, so they can be reviewed at any time.
    - Power demand selector, at a minimum a combobox. This is used to select the SPESS's power demand.
    - Power switch. At a minimum a toggle button, but ideally, a diagetic circuit breaker switch would be ideal for the purpose.
- Reflector
    - Angle selector. At a minimum a combobox, but ideally an angle dial which allows players to drag a 360 dial to the desired angle while "snapping" to angle fractions, but still allow manual entering of angles for finer control. If implemented, this dial control should also be implemented for the solar control console.

