# Metabolism

Metabolism in SS14 is very different to metabolism in SS13. In SS13, reagents simply had a proc `on_mob_life` that was called to determine what should happen. Our system is much more modular and allows for things like different organs metabolizing different reagents, and species-specific metabolisms, as well as overdoses or underdoses without any hassle.

## Organs & Metabolizers

In SS14, organs are entities with a `MechanismComponent` (mechanism just being a catch-all term for 'organ'.) Organs also have other components that give them decoupled behavior; `StomachComponent`, `CirculatorComponent`, `RespiratorComponent`, and so on. However, the important one here is `MetabolizerComponent.`

Metabolizers (organs with that component) define a list of 'metabolism groups' that they metabolize. 'Metabolism groups' are things like 'Narcotic', or 'Food', or 'Medicine'. This allows us to define how organs metabolize different chemicals.

This is on `OrganHumanStomach`. Meaning, the stomach processes any reagents with a `Food` metabolism, or a `Drink` metabolism:

```yml
  - type: Metabolizer
    # mm yummy
    maxReagents: 3
    metabolizerTypes: [Human]
    groups:
    - id: Food
    - id: Drink
```

Metabolizers can only process so many reagents at once, to avoid the common situation in SS13 where stacking a ton of poisons on one entity would damage it significantly more than just one concentrated poison.

Metabolism rate is defined on the organ. Generally, its once per second, and chems are taken from the bloodstream.

## Species

Defining how different species react to different chemicals is quite easy. Metabolizers are tagged with 'organ types', which is essentially a species marker, but localized to the organ (so if you swap out your heart for a gorilla heart, you'll metabolize medicines/poisons/etc in the same way a gorilla does). Then, you can use the `OrganType` condition to check. Here's an example in the codebase, of theobromine (a chemical found in chocolate):

```yml
  metabolisms:
    Poison:
      effects:
      - !type:HealthChange
        conditions:
        - !type:ReagentThreshold
          min: 1
        - !type:OrganType
          type: Animal # Applying damage to the mobs with lower metabolism capabilities
        damage:
          types:
            Poison: 4
```

As the comment suggests, to humans this chemical does nothing, but to animals (things with animal organs) it can be deadly.