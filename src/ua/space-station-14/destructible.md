# Destructible

## How to make an entity destructible
Making an entity destructible is done by adding the Damageable and Destructible components to it in YAML.
The Destructible component is responsible for defining a list of thresholds that it has, each with a trigger (when it will activate) and a list of behaviors (what happens when it activates).

```yaml=
- type: entity
  id: Wall
  name: wall
  description: Keeps the air in and the greytide out.
  components:
  - type: Damageable
    resistances: metallicResistances
  - type: Destructible
    thresholds: # List of thresholds that this entity can reach
    # First and only threshold, defining a trigger and a list of behaviors
    - trigger: # This threshold's trigger
        !type:DamageTrigger # Triggers at a total amount of damage...
        damage: 300 # ... equal to or above 300
      behaviors: # This threshold's behaviors
      - !type:SpawnEntitiesBehavior # First behavior, spawns entities
        spawn:
          Girder: # Spawn girders...
            min: 1 # ... from a minimum of 1...
            max: 1 # ... up to a maximum of 1
      - !type:DoActsBehavior # Second behavior, activates a list of acts
        acts: ["Destruction"] # In this case the Destruction act
```

## How to add a new destructible trigger
All triggers implement the `IThresholdTrigger` interface.
New ones can be defined like so:

```csharp=
[DataDefinition]
public partial class DamageTrigger : IThresholdTrigger
{
    /// <summary>
    ///     The amount of damage at which this threshold will trigger.
    /// </summary>
    [DataField("damage")]
    public int Damage { get; set; }

    public bool Reached(IDamageableComponent damageable, DestructibleSystem system)
    {
        return damageable.TotalDamage >= Damage;
    }
}
```

## How to add a new destructible behavior
All behaviors implement the `IThresholdBehavior` interface.
New ones can be defined like so:

```csharp=
[DataDefinition]
public partial class PlaySoundBehavior : IThresholdBehavior
{
    /// <summary>
    ///     Sound played upon destruction.
    /// </summary>
    [DataField("sound")]
    public string Sound { get; set; } = string.Empty;

    public void Execute(IEntity owner, DestructibleSystem system)
    {
        if (string.IsNullOrEmpty(Sound))
        {
            return;
        }

        var pos = owner.Transform.Coordinates;
        SoundSystem.Play(Filter.Pvs(pos), Sound, pos, AudioHelpers.WithVariation(0.125f));
    }
}
```
