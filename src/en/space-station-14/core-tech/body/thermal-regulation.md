# Thermal Regulation

## Design

## Engineering

### Components

#### ThermalRegulatorComponent

A server-side component that, despite being labelled an Organ component, is once again actually a mob component - most biological mobs will attempt to keep themselves at a given temperature.

This component covers the metabolism rate of this pseudo-organ, the causes of heat (metabolism, shivering), ways to lose heat (radiation, sweating), the target body heat, and how far the mob's body heat can diverge before regulation kicks in.

### Systems

#### ThermalRegulatorSystem

This server-side EntitySystem is the organ-like system for allowing mobs to try and maintain their preferred body temperature. 

Each tick of the system, each mob with the ThermalRegulatorComponent adds a small amount of heat to its entity that reflects its metabolism. After this, will check to see if it is too hot or too cold - if its actual temperature is too far away from its desired temperature - coverned by being outside of the value of its ideal temperature plus or minus its thermal reglation temperature threshold, a value set on the mob's ThermalRegulatorComponent. If it's too high, the mob will sweat, dropping its temperature slightly. If it's too cold, it shivers, raising its temperature further.

## YAML