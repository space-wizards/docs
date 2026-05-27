# Expand pneumatic valves to have a GUI and inversible

| Designers | Implemented | GitHub Links |
|---|---|---|
| Sinbiosis | :x: No | TBD |

## Overview

Pneumatic valves currently have no GUI to configure things like threshold or gain. Pneumatic valves also can't be inversed (explained below). This PR seeks to implement both features and to make inversibility a toggle within the GUI.

## Background

Pneumatic valves are like transistors, but for pressure-based systems. The current implementation of these valves is limited and only acts like an NMOS transistor. The "inverse" of this is the PMOS transistor, which for the pneumatic valve, hence forth called the "inverse pneumatic valve", means it allows flow between input and output, but only when the control is 1 atm BELOW whichever port is the higher of the two. I.e. If output > input AND control - 1 atm < output then allow flow.  If output < input AND control - 1 atm < input then allow flow.

## Motivation

Having a GUI for the pneumatic valve can improve the intuitive usability of the valve. Additionally, being able to toggle the inversbility of the pneumatic valve can lead to a lot of FUN™.
