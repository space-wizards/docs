# All About Puddles [Willhelm, Unapproved]

![](https://i.imgur.com/FOtrsvs.png)


# Part 1: [Wet Floor Sparkles](https://github.com/space-wizards/space-station-14/pull/11941)

The wet floor sparkle effect is intended to give janitors feedback that they are finished mopping in an area, because:
    - The puddle will evaporate on its own, and
    - The puddle is too small for their mop to pick up.

This gives us two conditions for triggering the sparkle effect:
1. Puddle is below a certain threshold
2. Puddle is evaporating

(WFET = Wet Floor Effect Threshold)
|| Is Evaporating|Is Not Evaporating |
|----------|----|----|
|**Is Above WFET**|Original puddle sprite | Original puddle sprite|
|**Is Below WFET**| Wet Floor Sparkle Effect| Ideally a baked-on "stain" look. 

Defining this `WetFloorEffectThreshold` and how it is handled can be tricky. For now I am settling for keeping it coincidentally the same as (or approximately equal to) the default `MopLowerLimit` of 5 units defined on `AbsorbentComponent` which mops use. However, I want to allow for the flexibility to define either threshold through (YAML) prototyping in the future. This might look like a sponge that can pick up the last 5u of puddle, or prank-enabling space lube which might turn into barely-visible sparkles even at a size of 20u.


# Part 2: Puddles that Stain

## Examples
Note: We would need reagent-based puddle properties (evaporation etc.) for this to be done robustly.
- Blood
- Slime
- Wine?
- Others?

## Intended (Future) Behaviour

- Large blood puddles should slip players, and remain wet for a very long time. Possibly all round if never mopped. 
- Blood puddles too small to slip players should dry into a stain.
- Stains should have to be re-hydrated back into puddles for effective cleaning (e.g. use a wet mop or sponge)  
- Puddles that stain should also leave footprints if mobs step through them while still wet


## Implementation
- Blood puddles could have a higher slipThreshold (eg 20 units), which means it would take a larger-than-average puddle to be able to slip someone.
- Blood puddles could evaporate at 1 unit per 60 to 30 seconds (e.g. a puddle starting at 50u would take 15-30 minutes to reduce by 30 and become non-slippery.)
- For our purposes, let's define "stain" as any puddle which:
    - Cannot slip players
    - Does not evaporate
    - Remains visible
- Stains keep their PuddleComponent, EvaporationComponent, SlipperyComponent, and all other components -- but behaviour is controlled with toggles similar to the existing EvaporationToggle. 
- Drying into stain could have its own system comparable to EvaporationSystem, or it could be built within EvaporationSystem. Ideally it should turn EvaporationToggle off when a puddle dries into a stain, and turn it back on when the stain gets rehydrated.
- Stains could have special VisualSystem behaviour within PuddleVisualSystem that makes them appear darker and "baked-on."


# Other

- Randomized slipping? Have some puddles always slip when run over, but for others it's a dice roll?
