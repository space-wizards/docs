# Reactions

Reaction prototypes define recipes with ratios of reagents required to cause a chemical reaction.  Below are the reaction yaml config values:

`type`: The prototype type. Should always be `reaction`.
`id`: Unique id used by the game to identify the reaction. In `PasacalCase`
`reactants`: A list of reactants required for the reaction to occur. Each reactant specifies it’s ratio and if it’s a catalyst. See the example below for more info.
`products`: A list of reagents created as a result of the reaction. They will be add to the solution container the reaction occurs in if there is room.
`effects`: A list of effects and their properties. Each effect corresponds to a C# class that implements IReactionEffect. See the example below for more info.

```yaml
- type: reaction
  id: PotassiumExplosion
  reactants:
    Water:
      amount: 1
    Potassium:
      amount: 1
  effects: # Reaction effects
    - !type:ExplosionReactionEffect
      # Ranges used when 1 potassium + 1 water react (A unit reaction)
      devastationRange: 0.05
      heavyImpactRange: 0.1
      lightImpactRange: 0.15
      flashRange: 0.2
      scaled: true # Scaled proportionally to amount of potassium and water
      maxScale: 30 # Explosion strength stops scaling at 30 potassium + 30 water

```

Here’s another example. This one has a catalyst, and some chemical products, but no reaction effect. Note that reactants are only catalysts if directly specified, and will be consumed otherwise.

```yaml
- type: reaction
  id: PolytrinicAcid
  reactants:
    SulfuricAcid:
      amount: 1
    Chlorine:
      amount: 1
      catalyst: True # False if not specified
    Potassium:
      amount: 1
  products:
    PolytrinicAcid: 3
```