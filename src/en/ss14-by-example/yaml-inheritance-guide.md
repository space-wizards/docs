# YAML Inheritance Guide
### Inheritance Rules

There are different ways DataFields get merged or overwritten when inheriting from another prototype in YAML and they can be a little confusing.
Let's look at a few examples:
```yml
# Define a few tags for testing purposes.
# Normally these should be in tags.yml.
- type: Tag
  id: TagA1

- type: Tag
  id: TagA2

- type: Tag
  id: TagB

- type: entity
  abstract: true
  id: ParentA
  components:
  - type: Tag
    tags:
    - TagA1
    - TagA2
  - type: MeleeWeapon # turn the entity into a weapon
    damage:
      types:
        Heat: 10

- type: entity
  abstract: true
  id: ParentB
  components:
  - type: Tag
    tags:
    - TagB
  - type: PointLight # make it glow
    color: green
    energy: 10

- type: entity
  abstract: true
  id: ParentC
  components:
  - type: Sprite
    sprite: Objects/Fun/Plushies/hampter.rsi # change the sprite folder only, but not the state

# A simple item with a lizard sprite.
# A sprite needs both the 'sprite' datafield, which contains the path to the rsi folder the image file is in,
# and the 'state' datafield which is the name of the .png file itself.
- type: entity
  parent: BaseItem # This parent has a bunch of components giving it physics, a fixture and allowing us to pick it up..
  id: TestItem1
  name: test item 1
  description: lizard
  components:
  - type: Sprite
    sprite: Objects/Fun/Plushies/lizard.rsi
    state: icon # this state name is the same for all basic plushie sprites

# The lizard sprite rsi is inherited first from TestItem1.
# The rsi is not overwritten by the hampter because it already exists in the first parent.
# So the resulting entity has a lizard sprite.
- type: entity
  parent: [ TestItem1, ParentC ]
  id: TestItem2
  name: test item 2
  description: lizard

# If we inherit in this order the rsi path will be taken from ParentC first.
# TestItem1 will then add the state Datafield, but not overwrite the rsi.
# The result will be a hampter.
- type: entity
  parent: [ ParentC, TestItem1 ]
  id: TestItem3
  name: test item 3
  description: hampter

# This time we manually overwrite the inherited rsi.
# The inherited state remains unchanged.
# The result will be another hampter.
- type: entity
  parent: TestItem1
  id: TestItem4
  name: test item 4
  description: hampter
  components:
  - type: Sprite
    sprite: Objects/Fun/Plushies/hampter.rsi

# This item will inherit the tags from ParentA, but not from ParentB.
# So it will have TagA1 and TagA2.
# The item will have both the PointLightComponent and the MeleeWeaponComponent and the corresponding DataFields set in the parents.
- type: entity
  parent: [ TestItem1, ParentA, ParentB ]
  id: TestItem5
  name: test item 5
  description: lizard

# To fix this and make the entity have all 3 tags we have to redefine the list manually.
- type: entity
  parent: [ TestItem1, ParentA, ParentB ]
  id: TestItem6
  name: test item 6
  description: lizard
  components:
  - type: Tag
    tags: # this overwrites the inherited list
    - TagA1
    - TagA2
    - TagB
```
  

To summarize the inheritance rules:
  1. A prototype can have one or multiple parents.
  2. A DataField that is not set in YAML gets its default value from its C# definition. In C# all variables have a default value if not specified otherwise, for example `public bool SomeVariable;` will always be `false` (in other programming languages you may get random bits).
  3. If you inherit from multiple parents, then components and their DataFields are inherited individually.
  4. The order of inheritance matters: Each DataField will be taken from the first parent that has it set in YAML.
  5. You can overwrite inherited DataFields by reassigning a new value in the child.
  6. If a DataField is overwritten, then the whole instance of the variable is reassigned. This means data types like lists (for example for tags) won't get merged, but replaced. However, you can change this behaviour for individual DataFields using the `AlwasPushInheritance`attribute (see further below for a detailed explanation).
  7. You cannot remove components that are inherited from a parent. You will have to make another abstract parent without that component instead to avoid copy pasting everything. 

```admonish warning
Common Mistake:
Rule 6 often gets overlooked for tags. If you add a new tag to an EntityPrototype make sure that
- the new list of tags for that entity contains all tags that were previously inherited.
- any child prototypes that have their own tags explicitly list the new tag as well.
```

### Abstract Prototypes
If you got a base prototype that should not a fully functioning prototype on its own, but used for inheritance, then make sure to mark it as `abstract`. This will make sure it cannot be spawned by any means, it will be hidden from the F5 spawn menu, and will be ignored by integration tests.
Example:
```yml
# A simplified plushie that inherits from BaseItem and has incomplete SpriteComponent DataFields.
- type: entity
  abstract: true # should not be spawned since this prototype is incomplete
  parent: BaseItem
  id: BasePlushie
  components:
  - type: Sprite
    state: icon # all plushie sprites have the same state name
  - type: EmitSoundOnUse # make it squeak when used
    sound:
      collection: ToySqueak

# A plushie that can be spawned in the game.
- type: entity
  parent: BasePlushie
  id: PlushieBee
  name: bee plushie
  components:
  - type: Sprite
    state: plushie_h # add a state (the sprite path is inherited from BasePlushie)

# And another one.
- type: entity
  parent: BasePlushie
  id: PlushieLizard # Weh!
  name: lizard plushie
  components:
  - type: Sprite
    state: plushie_lizard
```

If a prototype that is a fully functioning entity on its own should only be hidden from the F5 spawn menu, but can still be spawned through other means in-game, then you should be using The `HideSpawnMenu` category.
Examples are mind entities, objectives, or visual effects like this one used for flashbangs:
```yml
- type: entity
  id: GrenadeFlashEffect
  categories: [ HideSpawnMenu ]
  components:
  - type: PointLight
    enabled: true
    radius: 5
    energy: 8
    netsync: false
  - type: LightFade
    duration: 0.5
  - type: TimedDespawn
    lifetime: 0.5
```
This is a simple pointlight that quickly disappears and deletes itself. We use `categories: [HideSpawnMenu]` to make sure it does not show up in the spawn menu, but it can still be spawned through code using the `Spawn(protoId, coords)` method or similar.
This will also exclude it from several integration tests, which may otherwise fail for such an entity.

### Making a prototype inheritable
The above examples were all for `EntityPrototype`s, but they work the same for any other type of prototype. You can define your own prototype in C# and make it store DataFields. To make it inheritable in YAML you will have to implement the `IInheritingPrototype` interface. This requires a  DataField for the parents and a bool for being abstract.
Example:
```csharp
using Robust.Shared.Prototypes;
using Robust.Shared.Serialization.TypeSerializers.Implementations.Custom.Prototype.Array;

/// <summary>
/// A simple inheritable prototype for testing purposes.
/// </summary>
[Prototype]
public sealed partial class InheritanceTestPrototype : IPrototype, IInheritingPrototype
{
    /// <inheritdoc/>
    [IdDataField]
    public string ID { get; private set; } = default!;

    /// <inheritdoc/>
    [ParentDataField(typeof(AbstractPrototypeIdArraySerializer<InheritanceTestPrototype>))]
    public string[]? Parents { get; private set; }

    /// <inheritdoc/>
    [NeverPushInheritance]
    [AbstractDataField]
    public bool Abstract { get; private set; }

    /// <summary>
    /// A string you can set in YAML.
    /// </summary>
    [DataField]
    public string Field1 = "Field1 default value";

    /// <summary>
    /// And a second one.
    /// </summary>
    [DataField]
    public string Field2 = "Field2 default value";

    /// <summary>
    /// A datafield with different inheritance behaviour.
    /// This List will be merged instead of overwritten.
    /// </summary>
    [DataField, AlwaysPushInheritance]
    public List<string> AlwaysInheritedField = new();

    /// <summary>
    /// A datafield with different inheritance behaviour.
    /// This one will never get inherited.
    /// </summary>
    [DataField]
    public string NeverInheridedField = "default value";
}
```

```yml
- type: inheritanceTest
  id: Parent1
  field1: foo

- type: inheritanceTest
  id: Parent2
  field2: bar

- type: inheritanceTest
  parent: [ Parent1, Parent2 ]
  id: Child
  # This will inherit both field1 being foo, and field2 being bar.
```

### AlwaysPushInheritance, NeverPushInheritance
These two attributes can change the inheritance behaviour for a specific DataField. This works both for DataFields inside Components and inside custom Prototypes.

`AlwaysPushInheritance` will make `List`s, `HashSet`s and `Dictionaries` get merged instead of overwritten.
```yml
- type: inheritanceTest
  id: Parent1
  alwaysInheritedField:
  - foo

- type: inheritanceTest
  id: Parent2
  alwaysInheritedField:
  - bar

- type: inheritanceTest
  parent: [ Parent1, Parent2 ]
  id: Child
  alwaysInheritedField:
  - weh
```
The `Child` prototype will have a `AlwaysInheritedField` DataField with a list containing all three strings `foo`, `bar` and `weh`. 
This comes at the downside of not being able to remove any entries from that list in any inheritors. Ideally in the future we will add a more powerful YAML syntax to allow us to select the inheritance behaviour on a case by case basis (see some discussion [here](https://github.com/space-wizards/RobustToolbox/issues/5141), [here](https://github.com/space-wizards/space-station-14/issues/43326) and [here](https://forum.spacestation14.com/t/move-tags-to-rt-add-proper-entity-prototype-syntax/22759)).
This also works recursively for any custom `DataDefinition`s, see for example the `Solution` DataField in the `SolutionComponent`.

`NeverPushInheritance` will make a DataField not get inherited at all.
```yml
- type: inheritanceTest
  id: Parent
  neverInheridedField: weh

- type: inheritanceTest
  parent: Parent
  id: Child
  # neverInheritedField will be the C# default "default value" again
```

So it's recommended to always take a look at a component's or prototype's C# definition to see which attributes their DataFields have and which inheritance behaviour they will follow.
