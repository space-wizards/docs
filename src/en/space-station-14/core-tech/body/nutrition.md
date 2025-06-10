# Nutrition (Hunger and Thirst)

Often thought of as service gameplay, both of these gameplay mechanics are ultimately related to the Body.

## Design

## Engineering

### Components

### StomachComponent

A server-side component that controls the digestion Organ. This component works with a specific Solution - representing the food and drink that the Body has ingested - and, after a lengthy wait for digestion (by default about 20 seconds) digests food and dumps the reagents into (by default) the chemstream of the mob. Like other tick-based organs, this controls its own tickrate. Stomachs have an EntityWhitelist of things they are capable of eating; this is what leads to the confusing design of "the stomach prevents moths eating pills", and other such complaints.

### Systems

### StomachSystem

This server-side EntitySystem covers the digestion system. 

Like other Organs this runs on a low tick rate. On each update tick, each chemical in the stomach's Solution is assessed. The StomachComponent itself keeps track of the total time each reagent has been inside the stomach. Once a reagent  has hit its digestion time - by default 20 seconds - the reagent gets placed into the Body's mob's chemstream.

The other role of the StomachSystem is to control if a Food or Drink item can actually be ingested. The Stomach has a SpecialDigestible EntityWhitelist, which allows tags to filter what the stomach is capable of eating. This reflects that stomachs, not some mouth organ, controls what a mob can eat.

## YAML



