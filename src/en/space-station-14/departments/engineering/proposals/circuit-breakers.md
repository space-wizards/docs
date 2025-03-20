# Circuit breakers and fuses for electrical components

This is a rough outline for circuit breakers, fuses, and related components for the electrical systems.

The idea is to give Substations and APCs a maximum current draw based on the amount of power each component is meant to handle, and safeguards to prevent too much power draw in any specific area, in the form of circuit breakers (APCs) and fuses (Substations).

For APCs, with less load, a built in circuit breaker would automatically turn off the APC in question if there is too much power draw, whether from too many devices, or large machines exceed the load limit for the APC. 
For Substations, which generally carry a heavier load, one time use fuses will prevent overloads, and will need to be replaced in order to restore power to everything downstream of the substation.
# Interaction

A few ideas for interacting with the different overload circuits:

1. Bypassing, allow players to bypass the fuses and breakers, for example, if you are a scientist and want to power a lot of machines, or a big machine, and yourbreakers keep tripping, just bypass the breaker by cutting a breaker wire, or bypass a substation fuse by replacing the fuse with a simple strand of wire. this is not advisable though, as doing so can damage your equipment, or cause a catastrophic failure (think exploding substation.)
2. Upgrading, allow players to craft APCs/Substations with higher load limits, and better fuses for existing infrastructure
3. Antag interaction, give syndicate traitors the ability to either bypass a specific breaker (emag interaction, etc) or affect an entire circuit (power sinks can possibly affect breakers and fuses)
