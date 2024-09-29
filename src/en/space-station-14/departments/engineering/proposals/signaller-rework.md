# Signaller Rework
```admonish warning "Attention: Legacy Documentation!"
This document is ported from before the game-area reorganization and has not been reviewed or updated.
It may not fit with the new design requirements.
```

| Designers | Implemented | GitHub Links |
|---|---|---|
| deltanedas | :x: No | TBD |

## Overview

This proposal is for a rework of signals to be very short range (2-5m maximum) and have a separate radio transmission system for long-range controlling of objects.

Linking would effectively be wiring now with its short range.

## Background

Currently you can link 2 items together and they can be used across maps with infinite range.

They can also be nonsensical like linking a door to a microwave. Why would either have long-range transmission?

With a radio transmission system these systems can be implemented more freely allowing for more in-depth gameplay.

## Radio Transmission

This would be the main part of the rework. Radio transmitters would be items that accept signals and send them over radio with a frequency.

Radio receivers then create signals when a radio wave of a certain frequency is received. These would then be linked to objects like doors or microwaves.

Radio frequencies would range be in the VHF range between 100 and 200 MHz, with 0.1MHz of precision. This allows for 1000 different communication channels, plenty for a single round.

In the UI for setting frequency this would mean you can have 100.0 MHz and 100.1 MHz be distinct.

Since radio uses authenticated encryption, signallers can't interfere with it if set to the same frequency.

## Transmitters and Receivers

Radio transmitters either could just be signallers themselves or a new item that can't be manually triggered.
If they are kept separate, the ui for setting frequency can be shared for both.

Since transmitters can't be manually triggered they would be cheaper to make so making circuits is easier.

Radio receivers would just be a reworked signal trigger, it doesn't make sense to have a door output linked to a grenade which will move around.

Signal triggers have a UI to change frequency to match the signaller/transmitter, then you put it in a grenade or have it linked to something nearby.

Signal triggers would also have a signal sink port for linking to nearby objects.

Communicating across maps would not be possible, but perhaps a tech could be added for a transmitter that can work across maps and over an extended frequency range.

## Interacting with objects

Objects with wire panels like airlocks can have a signaller inserted when the panel is open.

Things with no panel like lights or microwaves can have them space-glued on, which is visible by examining.

Objects can still be linked nearby of course, but with shorter range. Maps with auto-bolting airlocks would still be fine.

## Gluing

If an item matching a whitelist is glued to an object like a light, APE or emitter, it is allowed to use its signal ports.

Glued items can be examined by anyone, only removed by spraying some kind of solvent on it, maybe even space lube.

## Example setup

A signaller set to 133.7MHz is linked to an airlock's door status port.

To prevent the signaller from being disconnected by someone moving it, it is then inserted into the wire panel.

A signal trigger with the same frequency is placed in a modular chem grenade across the station.

When the door opens, HIGH is sent over radio and the grenade explodes.

For a light, the signaller is space-glued onto it. This might have a unique sprite layer.

## Implementation

Frequencies would just be ushorts, clamped between 1000 and 2000. Essentially 1 place of fixed precision.

Transmission would use device network, but not the device linking packets. These can have unlimited range but on a single map.

Signal triggers handle device network radio packets and only use them if they have the same frequency.

Device linking can then be changed to have a very short range (200m seems to be the default currently?) to promote usage of radio systems.

Should be easy to add a network that says a device can only communicate if it is glued onto it, which APE and stuff would use but not doors.

### What I Stole From

In TG I think it uses a similar setup but with a code as well as frequency.

I decided not to have a code to make the system less complex and a bit easier to mess with, you only need to guess a frequency not a code.

In TG it's also just the same item for receiving and sending, you attach a signaller to a grenade to have it trigger it.
I don't think this is the best way to do it.
