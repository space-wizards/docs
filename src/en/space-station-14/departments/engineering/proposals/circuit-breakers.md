# Circuit breakers and fuses for electrical components

This is a rough outline for circuit breakers, fuses, and related components for the electrical systems.

The idea is to give Substations and APCs a maximum current draw based on the amount of power each component is meant to handle, and safeguards to prevent too much power draw in any specific area, in the form of circuit breakers (APCs) and fuses (Substations).

For APCs, with less load, a built in circuit breaker would automatically turn off the APC in question if there is too much power draw, whether from too many devices, or large machines exceed the load limit for the APC. 
For Substations, which generally carry a heavier load, one time use fuses will prevent overloads, and will need to be replaced in order to restore power to everything downstream of the substation.
