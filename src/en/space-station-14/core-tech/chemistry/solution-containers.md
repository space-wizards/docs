# Solution Containers

To make an entity a solution container, give add a `SolutionContainerManager`. For example here is an empty stomach solution:
```yaml
  - type: SolutionContainerManager
    solutions:
      stomach:
      	maxVol: 200
```

and a full drink solution: 

```yaml
  - type: SolutionContainerManager
    solutions:
      drink:
        maxVol: 20
        reagents:
        - ReagentId: Cola
          Quantity: 20
```

`type`: The component type. Should always be `SolutionContainerManager`.
`solutions`: A map of solution name and the `Solution` described below.

Solutions have several fields, all of them optional.
`maxVol`: The maximum volume of solution it can hold. Once reagent Quantity sum reaches `maxVol`, no more reagents can be added. It's full.
`reagents`: List of `Reagent`s it should hold by default. Each `Reagent` has a string `ReagentId` and `Quantity` which is a FixedPoint2 (basically a float limited to two decimal places).

## Capabilities and specifying target solution

With introduction of `SolutionContainerManager` there is no longer a simple 1:1 mapping of entity and list of reagents. 
Each `SolutionContainerManager` can contain any number of solutions. To solve this problem instead of Capabilities flag, a set of Capability-like components are introduced. Each such capability has a a string `solution` that tells `SolutionContainerManager` which solution it targets.

Here is a list of them:
- `DrainableSolutionComponent` for solutions that can be easily removed through any reagent container. E.g. draining water from a water tank
- `DrawableSolutionComponent` for solutions that can be drawn with syringes. E.g. humans or syringe bottles with rubber caps.
- `ExaminableSolutionComponent` for solutions that can be examined by hand.
- `FitsInDispenserComponent` notes that the component fits in dispenser and tells ReagentDispenser/ChemMaster which solution to target.
- `InjectableSolutionComponent` for solutions that can be injected into with syringes. 
- `RefillableSolutionComponent` for solutions that can be added easily.

Other components like `DrinkComponent` or `FoodComponent` may have special predefined solutions they target and expect to see. For example a `DrinkComponent` will try to create `drink` solution if there isn't an easily accessed `DrainableSolutionComponent` already available.

## Example of Solution
Here is a full example of an entity with some Solutions:

```yaml
- type: entity
  id: DrinkColaCan
  name: space cola
  description: A refreshing beverage.
  components:
  - type: Sprite
    sprite: Objects/Consumable/Drinks/cola.rsi
  - type: SolutionContainerManager
    solutions:
      drink:
        reagents:
        - ReagentId: Cola
          Quantity: 20
        maxVol: 20
  - type: Drink    
```