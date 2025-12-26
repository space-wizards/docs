# Conventions

There are nearly infinite ways to program the same thing, but some ways will get your PR rejected.

In this page you'll learn all about the coding conventions we have chosen for the codebase, which you'll need to follow if you want to get your PR merged.

See [Codebase Organization](./codebase-organization.md) for guidelines on how files and folders are organized in the SS14 codebase.

Read the [Pull Request guidelines](./pull-request-guidelines.md) to learn how to make your code more reviewable by maintainers.

```admonish info
Keep in mind that some older areas of the codebase might not follow these conventions. These should be refactored in the future to follow them. All new code should try to follow these conventions as closely as possible.
```

# General Programming Conventions

These conventions are not really specific to Space Station 14, and you should be following these no matter what project you are working on. Any experienced programmer should know these by heart.

## Don't copy paste code

If you're every looking at another piece of code and think "I want to do the same thing as this": **DO NOT** copy paste it. Make a new function or some other kind of abstraction that allows you to re-use as much code as possible.

Copy-pasting code is a gigantic maintenance hazard as, in the future, if somebody needs to update the code you copied, they now have to do it in *two* places (and be aware that those *two places* even exist).

Of course, there are places where you may think you're "copy pasting" unavoidable code. For example, the basic structure for making an `EntitySystem` that does a thing always has a class definition, some dependencies, an `override void Initialize()`, and so on. This kind of "boilerplate" is fine to copy as there's really no way to avoid it.

## Don't use magic strings/numbers

These are kind of a subset of "don't copy paste code". A "magic" value is any case in which you have a value in your code, say a string or a number, and it needs to be *that* specific value because it has to be the same as some other value somewhere else.

The name of the game here is "make sure that if two values have to match, it's practically impossible for them not to be." Be that via compiler error, unit test failure, a guaranteed crash on startup, whatever.

In the simplest case, such magic values should simply be stored in a `const` or `static readonly` that gets referenced from multiple locations, so the C# compiler enforces they will always be the same. If you need to reference a prototype ID from C#, you should define the prototype ID in a `static readonly ProtoId<T>`, since our validation tooling ensures the IDs in those fields are always valid.

## Comments

- Comment code at a high level to explain *what* the code is doing, and more importantly, *why* code is doing what it is doing.

- When documenting classes, structs, methods, properties/fields, and class members, use [XML docs](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/xmldoc/). DataFields and Public methods should always be documented.
    - Example:
  ```csharp
      /// <summary>
      /// Resets the InteractCounter on the <see cref="FooComponent"/>.
      /// </summary>
      /// <remarks>
      /// This is a public method other systems can call to interact with FooComponent!
      /// Remember that public methods should always use docstring.
      /// </remarks>
      [PublicAPI]
      public void ResetInteractCounter(Entity<FooComponent?> ent)
  ```

### Why Not What

Some folks blindly adhere to "comment the why, not the what" and think that "code should be self-documenting and comments a last resort". Below we present a few examples that we hope will change your mind.

#### Example 1

```csharp
var fractionalPressureChange = Atmospherics.R * (outlet.Air.Temperature / outlet.Air.Volume + inlet.Air.Temperature / inlet.Air.Volume);
```

All of the variables are named in a self-documenting way (*R* gets a pass because that is the ideal gas constant, and physics conventions existed long before computers, so this is following convention). Obviously, the comment should *not* be:

```csharp
// Take R and multiply it by the ratio of outlet temperature divided by outlet air volume and add it to ...
var fractionalPressureChange = Atmospherics.R * (outlet.Air.Temperature / outlet.Air.Volume + inlet.Air.Temperature / inlet.Air.Volume);
```

Because this only explains what the code is literally doing, which you could have gathered from any cursory reading of the code. **However, you still have absolutely no idea what this code is doing and why**, even though the code is self-documenting.

You don't know where this magic formula came from, what it's trying to accomplish, or even if the formula is correct. Therefore, this needs to be documented:


```csharp
// We want moles transferred to be proportional to the pressure difference, i.e.
// dn/dt = G*P

// To solve this we need to write dn in terms of P. Since PV=nRT, dP/dn=RT/V.
// This assumes that the temperature change from transferring dn moles is negligible.
// Since we have P=Pi-Po, then dP/dn = dPi/dn-dPo/dn = R(Ti/Vi - To/Vo):
var dPdn = Atmospherics.R * (outlet.Air.Temperature / outlet.Air.Volume + inlet.Air.Temperature / inlet.Air.Volume);
```

#### Example 2

```csharp
if (HasComp<MindContainerComponent>(uid))
    return;

// more stuff
```

Obviously, this code skips "more stuff" if the entity represented by *uid* already has a MindContainerComponent. This code is as self-documenting as it gets, it literally just returns early if there is a MindContainer. What needs to be documented is *why* this code needs to skip *uid*s that already have a MindContainerComponent:


```csharp
// Don't let players who drink cognizine be eligible for a ghost takeover
if (HasComp<MindContainerComponent>(uid))
    return;
```

## Strings and Identifiers

Human-readable text should never be used as an identifier or vice versa. In one direction, that means no putting human-readable text (result of localization functions) in a dictionary key, comparing with `==`, etc... In the other direction, that means things like "never show `Enum.ToString()` to a user directly."

This avoids spaghetti when these inevitably have to be decoupled for various reasons, and avoids inefficiency and bugs from comparing human-readable strings.

Example:

```csharp
private void UpdateDisplay(Gender gender)
{
    // This can't be localized! And the capitalization is kinda weird!
    // Don't do this!
    GenderLabel.Text = gender.ToString();

    // This is good!
    GenderLabel.Text = Loc.GetString($"gender-{gender}");
}
```

### Invariant comparisons on human-readable strings

If you're doing something like a filter/search dialog, use `CurrentCulture` comparisons over human-readable strings. Do not use invariant cultures.

## Properties

In a property setter, the value of the property should always literally become the `value` given. None of this:

```csharp
public string Name
{
    get => _name;
    private set => _name = Loc.GetString(value);
}
```

## Properly order members in a type

When laying out the contents of a type, you should **always** put fields above all other instance members. When reading a piece of code, the best way to get familiar with it is to look at the data it operates on. If fields and other members are mixed randomly, it can be much harder to understand the code.

For this rule, auto-properties (e.g. `string FooBar { get; set; }`) are considered the same as fields, since they have an internal field. Non-auto properties (e.g. `string FooBar => _field.Trim();`) do not, so should not be mixed.

Bad:

```csharp
class FooBar
{
    private int _field;

    public void Update() {
        _field *= 2;
        Counter += 1;
    }

    public int Counter { get; set; }
}
```

Good:

```csharp
class FooBar
{
    private int _field;
    public int Counter { get; set; }

    public void Update() {
        _field *= 2;
        Counter += 1;
    }

}
```

# Project Conventions

These conventions are specific to Space Station 14. They may talk about code or systems that aren't relevant to other projects, or those other projects may simply have a different opinion about code style.

## File Layout

1. Start with [using directives](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/using-directive) at the top of the file.

2. All classes should be explicitly namespaced. Use [file-scoped namespaces](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-10.0/file-scoped-namespaces), e.g. a single `namespace Content.Server.Atmos.EntitySystems;` before any class definitions instead of `namespace Content.Server.Atmos.EntitySystems { /* class here */ }`.

3. Always put all fields and auto-properties before any methods in a class definition.

## Methods

### Line breaks of parameter/argument lists

If you're defining a function and the parameter declarations are so long they don't fit on a single line, break them apart so you have **one parameter per line**. Some leeway is granted for closely tied parameter pairs like X/Y coordinates and pointer/length in C APIs.

Bad:

```csharp
public void CopyTo(ISerializationManager serializationManager, SortedDictionary<TKey, TValue> source, ref SortedDictionary<TKey, TValue> target,
    SerializationHookContext hookCtx, ISerializationContext? context = null)
```

Good:

```csharp
public void CopyTo(
    ISerializationManager serializationManager,
    SortedDictionary<TKey, TValue> source,
    ref SortedDictionary<TKey, TValue> target,
    SerializationHookContext hookCtx,
    ISerializationContext? context = null)
```

## Constants and CVars
If you have a specific value such as an integer you should generally make it either:
* a constant (const) if it's never meant to be changed
* a CVar if it's meant to be configured

This is so it is clear to others what it is. This is especially true if the same value is used in multiple places to make the code more maintainable.

## Prototypes

### Prototype data-fields
Don't cache prototypes, use prototypeManager to index them when they are needed. You can store them by their ID. When using data-fields that involve prototype ID strings, use ProtoId<T>. For example, a data-field for a list of prototype IDs should use something like:
```csharp
[DataField]
public List<ProtoId<ExamplePrototype>> ExampleTypes = new();
```

### Enums vs Prototypes
The usage of enums for in-game types is *heavily discouraged*.
You should always use prototypes over enums.
Example: In-game tool "kinds" or "types" should use prototypes instead of enums.

## Resources

### Sounds
When specifying sound data fields, use `SoundSpecifier`.
You should avoid defining sound paths directly and instead use `SoundCollectionSpecifier` whenever possible.

<details>
  <summary>C# code example (click to expand)</summary>

```csharp
[DataField]
public SoundSpecifier Sound = new SoundCollectionSpecifier("MySoundCollection");
```

</details>

<details>
  <summary>YAML prototype example (click to expand)</summary>

```yaml
# You can define a sound collection like this
- type: soundCollection
  id: MySoundCollection
  files:
  - /Audio/Effects/Cargo/ping.ogg

# And use it like this
- type: MyComponent
  sound:
    collection: MySoundCollection
```

</details>

### Sprites and Textures
When specifying sprite or texture data fields, use `SpriteSpecifier`.

<details>
  <summary>C# code example (click to expand)</summary>

```csharp
[DataField]
public SpriteSpecifier Icon = SpriteSpecifier.Invalid;
```

</details>

<details>
  <summary>YAML prototype example (click to expand)</summary>

```yaml
# You can specify a specific texture file like this, /Textures/ is optional
- type: MyComponent
  icon: /Textures/path/to/my/texture.png

# /Textures/ is optional and will be automatically inferred, however make sure that you don't start the path with a slash if you don't specify it
- type: MyComponent
  icon: path/to/my/texture.png

# You can specify an rsi sprite like this
- type: MyOtherComponent
  icon:
    sprite: /Textures/path/to/my/sprite.rsi
    state: MySpriteState
```

</details>

<details>
  <summary>RSI meta.json (click to expand)</summary>

- The order of fields should be `version -> license -> copyright -> size -> states`.
- JSON should not be minified, and should follow normal JSON quality guidelines (egyptian brackets, etc). All new JSON files should be indented at 4 spaces. Existing files should be changed to 4 space indent if you are modifying them (fix as you go). You should never be using tab for indent.

Example:

```json
{
    "version": 1,
    "license": "CC-BY-SA-3.0",
    "copyright": "Taken from tgstation at commit https://github.com/tgstation/tgstation/commit/547852588166c8e091b441e4e67169e156bb09c1",
    "size": {
        "x": 32,
        "y": 32
    },
    "states": [
        {
            "name": "icon"
        },
        {
            "name": "equipped-BACKPACK",
            "directions": 4
        },
        {
            "name": "inhand-left",
            "directions": 4
        },
        {
            "name": "inhand-right",
            "directions": 4
        }
    ]
}

```
</details>

### EntityUid in Logs
When using `EntityUid` in admin logs, use the `IEntityManager.ToPrettyString(EntityUid)` method.

<details>
  <summary>Admin log with entities example (click to expand)</summary>

```csharp
// If you're in an entity system...
_adminLogs.Add(LogType.MyLog, LogImpact.Medium, $"{ToPrettyString(uid)} did something!");

// If you're not in an entity system...
_adminLogs.Add(LogType.MyLog, LogImpact.Medium, $"{entityManager.ToPrettyString(uid)} did something!");
```

</details>

### Optional Entities
If you need to pass "optional" entities around, you should use a nullable `EntityUid` for this.
Never use `EntityUid.Invalid` to denote the absence of `EntityUid`, always use `null` and nullability so we have compile-time checks.
e.g. `EntityUid? uid`

## Components

### Component data access modifiers
All data in components should be public.

### Component property setters
You may not have setters with any logic whatsoever in properties. Instead, you should create a setter method in your entity system, and apply the `[Friend(...)]` attribute to the component so only that system can modify it.
Your component may use properties with setter logic for *ViewVariables integration* (until we have a better system for that).

### Component access restrictions
The `[Access(...)]` attribute allows you to specify which types can read or modify data in your class, while prohibiting every other type from modifying it.

Components should specify their access restrictions whenever possible, usually only allowing the entity systems that wrap them to modify their data.

### Shared Component inheritance
If a shared component is inherited by server and client-side counterparts, it should be marked as *abstract*.

## Entity Systems

### Game logic
Game logic should *always* go in entity systems, not components.
Components should *only* hold data.

### Proxy Methods
When possible, try using the `EntitySystem` [proxy methods](https://github.com/space-wizards/RobustToolbox/blob/master/Robust.Shared/GameObjects/EntitySystem.Proxy.cs) instead of using the `EntityManager` property.

<details>
  <summary>Examples (click to expand)</summary>

```csharp
// Without proxy methods...
EntityManager.GetComponent<MetaDataComponent>(uid).EntityName;

// With proxy methods
Name(uid);

// Without proxy methods...
EntityManager.GetComponent<TransformComponent>(uid).Coordinates;

// With proxy methods
Transform(uid).Coordinates;
```

</details>

### Public API Method Signature
All public Entity System API Methods that deal with entities and game logic should *always* follow a very specific structure.

All relevant `Entity<T?>` and `EntityUid` should come first.
The `T?` in `Entity<T?>` stands for the component type you need from the entity.
The question mark `?` must be present at the end to mark the component type as nullable.
Next, any arguments you want should come afterwards.

The first thing you should do in your method's body should then be calling `Resolve` for the entity UID and components.

<details>
  <summary>Example (click to expand)</summary>

```csharp
public void SetCount(Entity<StackComponent?> stack, int count)
{
    // This call below will set "Comp" to the correct instance if it's null.
    // If all components were resolved to an instance or were non-null, it returns true.
    if(!Resolve(stack, ref stack.Comp))
        return; // If the component wasn't found, this will log an error by default.

    // Logic here!
}
```

</details>

The `Resolve` helper performs a few useful checks for you. In `DEBUG`, it checks whether the component reference passed (if not null) is actually owned by the entity specified.

This helper will also log an error by default if the entity is missing any of the components that you attempted to resolve.
This error logging can be disabled by passing `false` to the helper's `logMissing` argument. You may want to disable the error logging for resolving optional components, `TryX` pattern methods, etc.

Please note that the `Resolve` helper also has overloads for resolving 2, 3 or even 4 components at once.
If you want to resolve components for multiple entities, or you want to resolve more than 4 components at once for a given entity, you'll need to perform multiple `Resolve` calls.

### Extension Methods

Extension methods (those with an explicit `this` for the first argument) should never be used on any classes directly related to simulation--that means `EntityUid`, components, or entity systems. Extension methods on `EntityUid` are used throughout the codebase, however this is bad practice and should be replaced with entity system public methods instead.

### Dependencies On Other Systems
Inside an entity system, prefer a system dependency instead of resolving the system using the IoCManager. For example, instead of:

```csharp
var random = IoCManager.Resolve<IRobustRandom>();
random.Prob(0.1f);
```

Add an entity system dependency:

```csharp
[Dependency] private readonly IRobustRandom _random = default!;
_random.Prob(0.1f);
```

## Events

### Method Events vs Entity System Methods
Method Events are events that you raise when you want to perform a certain action. Example:
```csharp
// This would change the damage on the entity by 10.
RaiseLocalEvent(uid, new ChangeDamageEvent(10));
```
On the other hand, Entity System Methods are methods you call on systems to perform an action.
```csharp
// This would change the damage on the entity by 10.
EntitySystem.Get<DamageableSystem>().ChangeDamage(uid, 10);
```

Method Events are *prohibited*, always use Entity System Methods instead.
There's an exception to this, however.

You may use Method Events as long as they're wrapped by an Entity System Method.
In the example above, this would mean that `DamageableSystem.ChangeDamage()` would internally raise the `ChangeDamageEvent`, which would then by handled by any subscriptors...

```admonish info
Ensure events are unsubscribed from when systems are shutdown. Proxy methods like `Subs.CVar()`or `SubscribeLocalEvent` already take care of it, note that you do not need to unsubscribed inside managers, as their lifetime ensures that when they shutdown, the rest of the client / server is also shutting down, making unsubscribing not necessary.
```

### Event naming
- Always suffix your events with `Event`.
  Example: `DamagedEvent`, `AnchorAttemptEvent`...

- Always name your event handler like this: `OnXEvent`
  Example: `OnDamagedEvent`, `OnAnchorAttemptEvent`...

### Struct by-ref events
Events should always be structs, not classes, and should always be raised by ref. If possible it should also be readonly if applicable.
They should also have the [ByRefEvent] attribute.

In practice this will look like the following:
```cs
var ev = new MyEvent();
RaiseLocalEvent(ref ev);
```

### C\# Events vs EventBus Events
The EventBus should generally be used over C# events where possible. C# events can leak, especially when used with components which can be created or removed at any time.

C# events should be used for out-of-simulation events, such as UI events.
Remember to *always* unsubscribe from them, however!

### Async vs Events
For things such as DoAfter, always use events instead of async.

Async for any game simulation code should be avoided at all costs, as it's generally virulent, cannot be serialized (in the case of DoAfter, for example), and usually causes icky code.
Events, on the other hand, tie in nicely with the rest of the game's architecture, and although they aren't as convenient to code, they are definitely way more lightweight.

## UI

### XAML and C#-defined UIs
You should always use XAML over UIs defined entirely in C# code.
Extending existing C#-defined UIs is fine, but they should be converted eventually.

## Performance

### Iterator Methods vs returning collections
Always use [iterator methods](https://docs.microsoft.com/en-us/dotnet/csharp/iterators) over creating a new collection and returning it in your method.

Keep in mind, however, that iterator methods allocate a lot of memory.
If you need to reduce allocations as much as possible, use struct iterators.

### Sealed Classes
Your class must be marked as either `abstract`, `static`, `sealed` or `[Virtual]`. This is to avoid accidentally making classes inheritable when the shouldn't be and can improve performance slightly when accessing or invoking virtual members.

Use `sealed` if the class shouldn't be inherited, `[Virtual]` for the normal C# behavior (it mutes the compiler warning), `static` for classes that don't need to be instantiated, or `abstract` if it's meant for being inherited but not meant to be instantiated by itself.

### Events over updates
Where possible you should always have your system run code in response to an event rather than updating every tick. Your code may only take up 0.5% of CPU time but when 100 systems do this it's unnecessary.

### Variable capture
When using [lambdas](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions) or [local functions](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/local-functions) be sure to **avoid variable captures**.

If you're adding a method that takes in a [Func delegate](https://docs.microsoft.com/en-us/dotnet/api/system.func-2), be sure to have an overload that **allows the caller to pass in custom data** to it.

<details>
  <summary>Example of what not to do (click to expand)</summary>

```csharp
void DoSomething(EntityUid otherEntity)
{
    // This is BAD. It will allocate on the heap a lot.
    var predicate = (EntityUid uid)
        => uid == otherEntity;

    // This method doesn't allow us to pass custom data,
    // so we're forced to do a costly variable capture.
    MethodWithPredicate(predicate);
}

void MethodWithPredicate(Func<EntityUid, bool> predicate)
{
    // We do something with the predicate here...
}
```

</details>

<details>
  <summary>Example of what to do (click to expand)</summary>

```csharp
void DoSomething(EntityUid otherEntity)
{
    // This is good and much more performant than the example before.
    var predicate = (EntityUid uid, EntityUid otherUid)
        => uid == otherUid;

    // Pass our custom data to this method.
    MethodWithPredicate<EntityUid>(predicate, otherEntity);
}

// This method allows you to pass custom data into the predicate.
void MethodWithPredicate<TState>(Func<EntityUid, TState, bool> predicate, TState state)
{
    // We do something with the predicate here, making sure to pass "state" to it...
}
```

</details>

## Field Deltas

Field deltas allow you to send only specific fields of a component over the network instead of the entire state. This is done by adding `fieldDeltas: true` to your `AutoGenerateComponentState` attribute:

```csharp
[RegisterComponent, NetworkedComponent, AutoGenerateComponentState(fieldDeltas: true)]
public sealed partial class MyComponent : Component
{
    [DataField, AutoNetworkedField]
    public bool IsActive;

    [DataField, AutoNetworkedField]
    public int Value;
}
```

### When to use field deltas

Field deltas are great when:
- Your component has fields that change at different rates
- Only a subset of fields typically changes at once
- You have a bunch of networked fields and don't want to send all of them every time

A good rule of thumb: If you have 3+ fields and they often change independently, consider field deltas. For components with just 1-2 fields, it's usually simpler to skip them.

### Marking fields as dirty

When you change a field and want to network just that field, use `DirtyField` instead of `Dirty`:

```csharp
// Instead of this:
comp.IsActive = true;
Dirty(uid, comp);  // Would send ALL networked fields

// Do this:
comp.IsActive = true;
DirtyField(uid, comp, nameof(MyComponent.IsActive));  // Only sends IsActive
```

For a component with many fields where usually only one or two change at a time, field deltas can reduce network traffic by 80-90%. The more fields you have, the more you'll benefit from field deltas.

Even for components with just 3-4 fields, if they change independently (e.g., one field updates frequently, others rarely), field deltas can still be worth it.

Field deltas add a little overhead for tracking field changes, but this is usually outweighed by the bandwidth savings. The generator automatically handles most of the implementation complexity.

## TimeSpans

### Using TimeSpans

You should always use `TimeSpan` over `float` for defining static periods of time, such as intervals. Update loops should compare against `CurTime` instead of accumulating `frametime`.

### Handling paused entities

When working with `TimeSpan` fields that are modified during runtime (like timers or countdowns), you need to handle entity pausing properly. SS14 provides two important mechanisms for this.

### AutoGenerateComponentPause and AutoPausedField

The `[AutoGenerateComponentPause]` and `[AutoPausedField]` attributes work together to automatically adjust `TimeSpan` fields when an entity is unpaused:

- `[AutoGenerateComponentPause]` is applied to a component class and automatically generates code to handle unpausing.
- `[AutoPausedField]` is applied to individual `TimeSpan` fields within that component that should be adjusted when the entity is unpaused.

These attributes should **always** be used for `DataField` `TimeSpan` properties that are modified by other systems during runtime, such as timers or cooldowns.

<details>
  <summary>Example usage (click to expand)</summary>

```csharp
[RegisterComponent, AutoGenerateComponentPause]
public sealed partial class CooldownComponent : Component
{
    [DataField, AutoPausedField]
    public TimeSpan CooldownEnd;

    [DataField, AutoPausedField]
    public TimeSpan? OptionalTimer;
}
```
</details>

### TimeOffsetSerializer

The `TimeOffsetSerializer` is used for serializing `TimeSpan` values that are offset by the current game time.

- It automatically offsets a `TimeSpan` by the game's current time during serialization/deserialization
- If the entity is paused, it uses the time at which the entity was paused as the reference point
- It prevents unintentional saving of time offsets to maps during mapping (prototypes always serialize as zero)

Similar to `AutoPausedField`, the `TimeOffsetSerializer` should always be used for runtime-modified `TimeSpan` fields that represent absolute times rather than durations.

<details>
  <summary>Example usage (click to expand)</summary>

```csharp
[DataField(customTypeSerializer: typeof(TimeOffsetSerializer))]
public TimeSpan NextActivationTime;
```
</details>

## Naming

### Shared types
Shared types should only be prefixed with `Shared` if and only if there are server and/or client inherited types with the same name.

Example:
- If `FooComponent` only exists in shared, it doesn't need a prefix.
- If `BarComponent` exists in shared, server and client, the shared type should be prefixed with shared: `SharedBarComponent`.

## Physics

### Anchoring

Always use `TransformComponent` anchoring through the system methods.
You may use `PhysicsComponent` static body anchoring but *only* if you know what you're doing and you can defend your choice over transform anchoring.

## YAML Conventions

- Every component `- type` should be together without any empty newlines separating them
- Separate prototypes with one empty newline.
- `name:` and `description:` fields should never have quotations unless punctuation in the name/description requires the use of them, then you will use ''. For example:
```yaml
  name: 'Spessman's Smokes packet'
  description: 'A label on the packaging reads, 'Wouldn't a slow death make a change?''
```
- Don't specify textures in abstract prototypes/parents.
- You should declare the first prototype block in this order: `type` > `abstract` > `parent` > `id` > `categories` > `name` > `suffix` > `description` > `components.`
- Use inline lists for empty overrides and regular lists for everything else:
  ```yaml
  - type: entity
    parent: # Regular list
    - ClothingHeadBase
    - BaseSyndicateContraband
    id: ClothingHeadHatCatEars
    name: cat ears
    description: "NYAH!"
    categories: # Regular list
    - DoNotMap
    components:
    - type: Tag
      tags: [] # Inline list for empty overrides
    - type: Sprite
      sprite: Clothing/Head/Hats/catears.rsi
    - type: Clothing
      sprite: Clothing/Head/Hats/catears.rsi
    - type: AddAccentClothing
      accent: OwOAccent
    - type: StaticPrice
      price: 15000
  ```
- New components should not have an indent when added to the `components:` section.
  This
    ```yaml
    components:
    - type: Sprite
      state:
    ```
  Not this
    ```yaml
    components:
      - type: Sprite
        state:
    ```
- The same rule applies for any other list or dictionary, for example:
    ```yaml
    - type: Tag
      tags:
      - HighRiskItem # Correct indentation

    - type: Tag
      tags:
        - HighRiskItem # Wrong indentation
    ```
- When it makes sense, place more generalized/engine components near the top of the components list and more specific components near the bottom of the list. For example,
    ```yaml
    components:
    - type: Sprite # Engine-specific
    - type: Physics
    - type: Anchorable # Content, but generalized
    - type: Emitter # A component for a specific type of item
    ```

### YAML and data-field naming
`PascalCase` is used for IDs and component names.
Everything else, even prototype type names, uses `camelCase`.
`prefix.Something` should NEVER be used for IDs.

### Entities

Please ensure you structure entities with components as follows for easier YAML readability:

```
- type: entity
  abstract: true # remove this line if not abstract
  parent:
  - <nameofparent>
  id:
  name:
  components:
  <rest of file>
```

#### Entity Prototype suffixes

Use `suffix` in prototypes, this it's a spawn-menu-only suffix that allows you to distinguish what prototypes are, without modifying the actual prototype name. You can use it like this:
![](https://i.imgur.com/epkPR3Y.png)

And results in this:
![](https://i.imgur.com/JigMCuu.png)

## Localization
Every player-facing string ever needs to be localized.

### Localization ID naming
- Localization IDs are always `kebab-case` and should never contain capital letters.
- Localization IDs should be specific as possible, to avoid clashing with other IDs.
  This
    ```ftl
    antag-traitor-user-was-traitor-message = ...
    ```
  Not this
    ```ftl
    traitor-message = ...

## In-simulation or out-of-simulation

```admonish warning
This convention is *very* poorly enforced by our current codebase. Keep that in mind if you see something that seemingly violates it.
```

Broadly, all code in the game should be separated based on whether it is *inside* the "simulation" or *outside* it. The "simulation" is a encompassing term that basically means "the contents of the actual game".

For example, the following things are "inside" the simulation:
- Basically everything concerning entities: interactions, physics, atmos, etc.
- IC chat
- Round state (lobby, in-game, post-game)

The following examples are "outside" the simulation:
- OOC chat
- Adminhelp
- Admin votes
- Basically anything talking to an external service, such as the database or a Discord webhook

We always need locations in the code where these two sides of the codebase exchange data. (For example, a player connecting is initially handled out of simulation, but the simulation needs to be notified of new players to spawn them in somehow.) Exactly how this should be done depends on a case-by-case basis, and it can take effort to do properly, but it is vitally important for code architecture.

A thought experiment to think about this is "should this logic stop working if the game were to be paused by an admin." If such a pause button were to exist, we would like to completely stop the game logic (no time would progress, nobody could move, etc), but we'd still like people to be able to connect to the server, talk in OOC chat, ask an admin *why* the game is still paused, and so on.

```admonish info
The game server currently already automatically pauses like this when no players are online, to save resources. This isn't purely theoretical! But perhaps hard to observe at the moment.
```

Time in the simulation may accelerate or slow down relative to "real time", depending on server settings or performance issues. On the client, the simulation is constantly committing time travel as part of network prediction. The simulation doesn't actually *exist* on the client until connected to a server!

Here are some of the differences between how in-simulation and out-of-simulation code should be written:

| Thing you want to do | in-simulation | out-of-simulation |
|-|---------------|-------------------|
| "Default place" for singleton code. | Make an `EntitySystem` | Use a manager: make a new class, register it with IoC, and call it from `EntryPoint` or similar. |
| Check elapsed time | `IGameTiming.CurTime` | `IGameTiming.RealTime`, `(R)Stopwatch`, `DateTime`, etc.
| Send custom network messages | Networked entity events | Custom `NetMessage` |
