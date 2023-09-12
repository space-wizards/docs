# Reagents

Reagents are substances which comprise solution and which can react to create new Reagents.

Their definition consists of:
`type`: The component name. Should always be `reagent`.
`id`: Unique id for this reagent. Used in reactions and other locations to identify the reagents. For example `Iodine` or `WeldingFuel`. They are `PascalCase`.
`name`: Id with spaces for displaying in tooltips. E.g. `iodine` and `welding fuel`.
`parent`: What reagent to inherit properties from. Used for things like BaseDrink.
`desc`: A human friendly description of the chemical.
`color`: Hex color of the reagent. Used for mixing and chemical display in containers.
`spritePath`: A sprite specifying the icon used for the reagent, starting from `Textures/Objects/Consumable/Drinks`.
`physicalDesc`: Vague desscription potentially useful when identifying it.
`boilingPoint`: Temperature in Celsius, at which reagent goes from liquid into gas.
`meltingPoint`: Temperature in Celsius, at which reagent goes from solid into liquid.
`metabolisms`: A dict of MetabolismGroup->List\<ReagentEffect\> to apply when the reagent is consumed.

## Example of reagent definition

```yaml
- type: reagent
  id: Lemonade
  name: lemonade
  parent: BaseDrink
  desc: Drink using lemon juice, water, and a sweetener such as cane sugar or honey.
  physicalDesc: tart
  color: "#FFFF00"
  spritePath: lemonadeglass.rsi
  metabolisms:
    Drink:
      effects:
      - !type:SatiateThirst
        factor: 2
```

For more info see: [SS14 Content: Reagent folder](https://github.com/space-wizards/space-station-14/tree/master/Resources/Prototypes/Reagents) or [SS14 Content:ReagentPrototype.cs](https://github.com/space-wizards/space-station-14/blob/ca50a5f9934a399826306659f298f0098251e4eb/Content.Shared/Chemistry/Reagent/ReagentPrototype.cs)

## Reagent Effects & Conditions

`ReagentEffect`s are described in C#. For example, `SatiateThirst` and `HealthChange`. This allows you to easily reuse code that has similar effects. Many things use reagent effects--metabolisms, plant metabolisms, and reagent entity reactions (touch/injection-based effects). `ReagentEffect`s also have a `prob` field, which is the chance that the effect will run from 0 to 1. The reason these are so generalized is because many things that need the data can use them.

`ReagentEffectCondition`s are attached to each effect in the metabolizer list. By default, there are none; so they're always ran. However, you can easily add custom behavior to determine when an effect will actually occur. For instance, `ReagentThreshold` allows you to very easily define overdose behavior. Here's Methamphetamine:

```yml
  metabolisms:
    Poison:
      effects:
      - !type:HealthChange
        damage:
          types:
            Poison: 2.5
      - !type:HealthChange
        conditions:
        - !type:ReagentThreshold
          min: 10
        damage:
          types:
            Poison: 4 # this is added to the base damage of the meth.
    Narcotic:
      effects:
      - !type:MovespeedModifier
        walkSpeedModifier: 1.3
        sprintSpeedModifier: 1.3
```

This means that the overdose behavior HealthChange only occurs when there is at minimum 10u in your system. It has two different groups, 'Poison' and 'Narcotic'. These are both metabolized by the heart, generally.