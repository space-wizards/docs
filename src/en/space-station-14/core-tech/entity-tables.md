# Entity Tables

**Entity tables** are a powerful way of defining entities for container fills and spawners.
The system is made up of recursive sets of selectors, each of which can define custom behavior for choosing entities.

## Usage

You can get the spawns from a table using `EntityTableSystem.GetSpawns`. 
This function call only takes in an `EntityTableSelector` with an optional param for `System.Random`, allowing for deterministic applications.

As of the writing of this guide, EntityTables are primarily supported by two components, `EntityTableContainerFillComponent` and `EntityTableSpawnerComponent`.

`EntityTableContainerFillComponent` serves as a direct replacement for `ContainerFillComponent`.
It uses the same general syntax besides swapping out the list of `EntitySpawnEntry`s for a `EntityTableSelector`.

Similarly, `EntityTableSpawnerComponent` is a replacement for `RandomSpawnerComponent`.
However, they do not share the same variables.
This version only supports a table and an offset, and not the separate lists and chance variable of the old system.
The same effect can be achieved through the use of nested `GroupSelectors` with an overall `prob` definition and `weights` corresponding to the previous chances.

### Example Syntax

```admonish warning "Type Specification"
When writing EntityTables, you must use the `!type:[Class Name]` syntax when you specify a selector.

The one exception is `EntSelector`.
Simply specifying the ID will cause the linter to assume the specified selector is an EntitySelector.
This greatly reduces the yaml for large tables.
```

Here is a reusable entity table prototype:
```yaml
- type: entityTable
  id: LockFillTable
  table: !type:AllSelector # <-- This means that all the children will be selected
    children:
    - id: ClothingMaskBreath # <-- This is just a single instance of an entity
    - !type:GroupSelector # <-- This means that only one of the children will be selected
      children:
      - id: EmergencyOxygenTankFilled # <-- All selectors have a default weight of 1
      - id: OxygenTankFilled
        weight: 2 # <-- This means this entry is twice as likely to be selected
    - id: ToolboxEmergencyFilled
      prob: 0.5 # <-- This means there is a 50% chance that this selector will be used.
```

Here's an example of one in-lined into an entity prototype:
```yaml
- type: entity
  id: ClosetFilled
  components:
  - type: EntityTableContainerFill
    containers:
      entity_storage: !type:AllSelector
        children:
        - !type:NestedSelector # <-- This will recursively call GetSpawns on an EntityTablePrototype
          tableId: LockFillTable
        - id: ClothingMaskGas
          amount: !type:ConstantNumberSelector # <-- This will select exactly 3 of the specified entity
            value: 3
        - id: StrangePill
          amount: !type:RangeNumberSelector # <-- This will select between 2 to 6 (inclusive on both sides) of the specified entity
            range: 2, 6
```

## EntityTableSelectors

### Common Variables

All EntityTableSelectors have the following variables:

- **Rolls:** The number of times a given selector is run.
`Prob` chances will be run for every roll
- **Weight:** A weight used to determine which selector is chosen for `GroupSelector`
- **Prob:** Simple probability used to determine if a selector is ran.
Goes from 0 to 1

### EntSelector

- **Id:** The ID of the EntityPrototype you want to select.
Required.
- **Amount:** A `NumberSelector` corresponding to how many of `Id` do you want to select.
Defaults to 1 if nothing is specified.

EX:
```yml
root:
- id: PlushieLizard
  amount: !type:ConstantNumberSelector
    value: 5
    
# or

root: !type:EntSelector
- id: PlushieLizard
  amount: !type:ConstantNumberSelector
    value: 5
```

### NoneSelector

Returns nothing. 
This can be used in conjunction with `GroupSelector` for probability.

EX:
```yml
containers:
- storage: !type:NoneSelector
```

### AllSelector

`AllSelector` allows for basic control in choosing a list of selectors that you want to use in conjunction with each other.

- **Children:** A list of other EntityTableSelectors that will be selected from.

EX:
```yml
root: !type:AllSelector
  children:
  - id: PlushieLizard
  - id: ClothingMaskGas
```

### GroupSelector

`GroupSelector` serves as a replacement for EntitySpawnEntry's OrGroup.
Since only one of the children is chosen, a common usage is nesting multiple GroupSelector's within each other to adjust the chance of an item being picked without explicitly calculating Weights.

Similarly, an EntityTable with a GroupSelector as the root can be used as a generic pool.
This makes picking multiple items from the pool as simple as increasing the value of `Rolls`.

- **Children:** A list of other EntityTableSelectors, one of which will be chosen and selected from based on chance and the selector's `Weight` value

EX:
```yml
root: !type:GroupSelector
  children:
  - id: PlushieNar
  - id: PlushieRatvar
```

### NestedSelector

`NestedSelector` exists primarily to reduce duplication of yaml.
Since a table (or part of a table) can be specified as a prototype, using this allows you to reference it multiple times in many places.

- **TableId:** The string ID of a EntityTableSelector. 

EX:
```yml
- type: entityTable
  id: test
  table: !type:GroupSelector
    children:
    - id: PlushieLizard
    - id: PlushieNar
    - id: PlushieRatvar

- type: entity
  id: PlushSpawner
  components:
  - type: EntityTableSpawner
    table: !type:NestedSelector
      tableId: test
```

## ValueSelectors

### NumberSelectors

`NumberSelector` is just a generic way of specifying a numerical value for various selectors.

#### ConstantNumberSelector

- **Value:** Returns the specified value.

EX:
```yml
amount: !type:ConstantNumberSelector
  value: 4
```

#### RangeNumberSelector

- **Range:** Returns a value within the specified range (inclusive on both sides)

EX:
```yml
rolls: !type:RangeNumberSelector
  range: 6, 2019
```

## Custom Selectors

To implement a custom entity table selector, create a new class that inherits from `EntityTableSelector`.
Then, simply override `GetSpawns(System.Random, IEntityManager, IPrototypeManager)` and create your implementation.

You can add any datafields on the class but you cannot use dependency injection to add systems.
If you want to call a Manager or System, the easiest way to do it is to create a new `EntitySystem` that has a public API that handles the selection, then get the system via the supplied `IEntityManager`.

NumberSelectors work the same, simply using `NumberSelector` instead of `EntityTableSelector`. 