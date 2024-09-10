# Radial Meteor Shielding

Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar.

|AugustSun|✖️|TBD|

## Overview

Radial Meteor Shielding allows for the station's crew to protect parts of the station, using machines connected to the station's power grid. 
These machines must be anchored, and will consume significant power upon receiving hits from meteors, and to a lesser extent space debris.

## Background

Currently, there are no existing protections for the station against meteors or debris, save for physical barriers (i.e. windows, walls, etc.). While stations are generally mapped with these physical defenses around critical departments or features, these are stopgap measures that can be quickly destroyed through a variety of means. This is particularly exacerbated in rare meteor-focused game modes, such as Kessler or Survival, where a quick shuttle call is inevitable with no recourse for the crew. Thus, the Radial Meteor Shielding provides a solution for the crew, while not being a set-and-forget solution.

## Implementation

**In-Game Sprite**

As mentioned previously, the Meteor Shielding would be a powered machine. The suggestion of using the Containment Field Generator provides another use for spare Field Generators on station, which are often present, but rarely utilized. Otherwise, a new sprite would need to be created.

**Station Benefit**

When active, a wide space centered on the machine will be protected from meteors and debris, provided the station/station area supplies enough power to defend the area from each impact. This provides areas of the station with a method of defense against an event that typically causes significant damage, death and disruption to impacted areas of the station.

**Resource Requirement**

Meteor shielding would draw a small amount of power from the grid when not actively defending against meteors, signifying that the shield's systems are on. When actively defending against projectiles, the shield will drain stored power for each impact, depending on the type of projectile (meteors vs. debris).

To draw on the station's power, this machine can either be directly connected to a substation through a MV connection, or powered directly by being anchored directly to the grid via a HV cable.

## Gameplay Benefits & Risks

**Benefits**

Aside from the immediate benefit of mitigating unavoidable damage, meteor shielding provides a variety of new dynamics. In response to meteor damage, engineering teams typically have to spend resources in order to restore structural integrity, as well as department functionality. Meteor shielding can avert danger, but at the same time, should a station's power grid struggle, the shielding may drain available power from the station, potentially only stopping one or two meteors while leaving the rest of the station without power (causing substations and APCs to shut off until consistent power flow is restored).

As every station has a different layout, engineering teams must determine where shield placement will be the most effective, as well as which departments they need to prioritize for proactive measures. Additionally, they also must make the determination of whether or not the station is making enough power to support meteor shielding without interruption of power.

Additionally, specific to meteor-heavy game modes, the meteor shielding can be instrumental to giving the station a greater chance at survival as crews scramble to balance defense, reconstruction, and power management in the process.

**Risks**

Implementing meteor shielding will hinge around power draw and coverage. 

Making the power draw too low can lead to engineers setting up a grid of meteor shielding covering the station, leading to a significant benefit for little investment. Too high of a power draw will likely lead to longer power outages, causing more issues across the station (as well as potentially causing a singuloose/tesloose in the process).

Coverage of the shielding must be reasonably sized for similar reasons; too large, and the benefit becomes too large for the effort. Too small, and the crew is unlikely to put in the effort of setting up the shielding.
