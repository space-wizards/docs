# Conventions

There are nearly infinite ways to program the same thing, but some ways will get your PR rejected.

In this page you'll learn all about the coding conventions we have chosen for the codebase, which you'll need to follow if you want to get your PR merged.

See [Codebase Organization](./codebase-organization.md) for guidelines on how files and folders are organized in the SS14 codebase.

Read the [Pull Request guidelines](./pull-request-guidelines.md) to learn how to make your code more reviewable by maintainers.

```admonish info
Keep in mind that some older areas of the codebase might not follow these conventions. These should be refactored in the future to follow them. All new code should try to follow these conventions as closely as possible.
```

## File Layout

1. Start with [using directives](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/using-directive) at the top of the file.

2. All classes should be explicitly namespaced. Use [file-scoped namespaces](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/proposals/csharp-10.0/file-scoped-namespaces), e.g. a single `namespace Content.Server.Atmos.EntitySystems;` before any class definitions instead of `namespace Content.Server.Atmos.EntitySystems { /* class here */ }`.

3. Always put all fields and auto-properties before any methods in a class definition.

## Comments

- Comment code at a high level to explain *what* the code is doing, and more importantly, *why* code is doing what it is doing. 

- When documenting classes, structs, methods, properties/fields, and class members, use [XML docs](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/xmldoc/)

### Why Not What

Some folks blindly adhere to "comment the why, not the what" and think that "code should be self-documenting and comments a last resort". Below we present a few examples that we hope will change your mind.

#### Example 1

```csharp
   float fractionalPressureChange = Atmospherics.R * (outlet.Air.Temperature / outlet.Air.Volume + inlet.Air.Temperature / inlet.Air.Volume);
```

All of the variables are named in a self-documenting way (*R* gets a pass because that is the ideal gas constant, and physics conventions existed long before computers, so this is following convention). Obviously, the comment should *not* be:

```csharp
	 // Take R and multiply it by the ratio of outlet temperature divided by outlet air volume and add it to ...
   float fractionalPressureChange = Atmospherics.R * (outlet.Air.Temperature / outlet.Air.Volume + inlet.Air.Temperature / inlet.Air.Volume);
```

Because this only explains what the code is literally doing, which you could have gathered from any cusory reading of the code. **However, you still have absolutely no idea what this code is doing and why**, even though the code is self-documenting.

You don't know where this magic formula came from, what it's trying to accomplish, or even if the formula is correct. Therefore, this needs to be documented:


```csharp
        // We want moles transferred to be proportional to the pressure difference, i.e.
        // dn/dt = G*P

        // To solve this we need to write dn in terms of P. Since PV=nRT, dP/dn=RT/V.
        // This assumes that the temperature change from transferring dn moles is negligible.
        // Since we have P=Pi-Po, then dP/dn = dPi/dn-dPo/dn = R(Ti/Vi - To/Vo):
        float dPdn = Atmospherics.R * (outlet.Air.Temperature / outlet.Air.Volume + inlet.Air.Temperature / inlet.Air.Volume);
```

#### Example 2

```csharp
        if (HasComp<MindContainerComponent>(uid))
        {
            return;
        }
        
        // more stuff
```

Obviously, this code skips "more stuff" if the entity represented by *uid* already has a MindContainerComponent. This code is as self-documenting as it gets, it literally just returns early if there is a MindContainer. What needs to be documented is *why* this code needs to skip *uid*s that already have a MindContainerComponent:


```csharp
				// Don't let players who drink cognizine be eligible for a ghost takeover
        if (HasComp<MindContainerComponent>(uid))
```

## Methods

### Line breaks of parameter/argument lists

If you're defining a function and the parameter declarations are so long they don't fit on a single line, break them apart so you have **one parameter per line**. Some leeway is granted for closely tied parameter pairs like X/Y coordinates and pointer/length in C APIs.

Bad:

```cs
public void CopyTo(ISerializationManager serializationManager, SortedDictionary<TKey, TValue> source, ref SortedDictionary<TKey, TValue> target,
    SerializationHookContext hookCtx, ISerializationContext? context = null)
```

Good:

```cs
public void CopyTo(
    ISerializationManager serializationManager,
    SortedDictionary<TKey, TValue> source,
    ref SortedDictionary<TKey, TValue> target,
    SerializationHookContext hookCtx,
    ISerializationContext? context = null)
```

## Strings and Identifiers

Human-readable text should never be used as an identifier or vice versa. That means no putting human-readable text (result of localization functions) in a dictionary key, comparing with `==`, etc...

This avoids spaghetti when these inevitably have to be decoupled for various reasons, and avoids inefficiency and bugs from comparing human-readable strings.

### Invariant comparisons on human-readable strings

If you're doing something like a filter/search dialog, use `CurrentCulture` comparisons over human-readable strings. Do not use invariant cultures.

## Properties

In a property setter, the value of the property should always literally become the `value` given. None of this:

```cs
public string Name
{
    get => _name;
    private set => _name = Loc.GetString(value);
}
```

## Constants and CVars
If you have a specific value such as an integer you should generally make it either: 
* a constant (const) if it's never meant to be changed
* a CVar if it's meant to be configured

This is so it is clear to others what it is. This is especially true if the same value is used in multiple places to make the code more maintainable.

## Prototypes

### Prototype data-fields
Don't cache prototypes, use prototypeManager to index them when they are needed. You can store them by their ID. When using data-fields that involve prototype ID strings, use custom type serializers. For example, a data-field for a list of prototype IDs should use something like: 
```csharp=
[DataField("exampleTypes", customTypeSerializer: typeof(PrototypeIdListSerializer<ExamplePrototype>))]
public List<string> ExampleTypes = new();
```

### Enums vs Prototypes
The usage of enums for in-game types is *heavily discouraged*.
You should always use prototypes over enums.
Example: In-game tool "kinds" or "types" should use prototypes instead of enums.

## Resources

### Sounds
When specifying sound data fields, use `SoundSpecifier`.



<details>
  <summary>C# code example (click to expand)</summary>

```csharp=
[DataField("sound", required: true)]
public SoundSpecifier Sound { get; } = default!;
```
  
</details>

<details>
  <summary>YAML prototype example (click to expand)</summary>
  
```yml=
# You can specify a specific sound file like this
- type: MyComponent
  sound:
    path: /Audio/path/to/my/sound.ogg
  
# But this works, too!
- type: MyOtherComponent
  sound: /Audio/path/to/my/sound.ogg
    
# You can only specify a sound collection like this
- type: AnotherComponent
  sound:
    collection: MySoundCollection
 
```
  
</details>

### Sprites and Textures
When specifying sprite or texture data fields, use `SpriteSpecifier`.

<details>
  <summary>C# code example (click to expand)</summary>
  
```csharp=
[DataField("icon")]
public SpriteSpecifier Icon { get; } = SpriteSpecifier.Invalid;
```
  
</details>

<details>
  <summary>YAML prototype example (click to expand)</summary>
  
```yml=
# You can specify a specific texture file like this
- type: MyComponent
  icon: /Textures/path/to/my/texture.png
    
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
- JSON should not be minified, and should follow normal JSON quality guideliens (egyptian brackets, etc)

Example:

```json
{
    "version": 1,
    "license": "CC0-1.0",
    "copyright": "GitHub @PJB3005",
    "size": {
        "x": 32,
        "y": 32
    },
    "states": [
        {
            "name": "hello",
            "flags": {},
            "directions": 4,
            "delays": [
                [1, 1, 1],
                [2, 3, 4],
                [3, 4, 5],
                [4, 5, 6]
            ]
        }
    ]
}
```
</details>

### EntityUid in Logs
When using `EntityUid` in admin logs, use the `IEntityManager.ToPrettyString(EntityUid)` method.

<details>
  <summary>Admin log with entities example (click to expand)</summary>
  
```csharp=
// If you're in an entity system...
_adminLogs.Add(LogType.MyLog, LogImpact.Medium, $"{ToPrettyString(uid)} did something!");
  
// If you're not in an entity system...
_adminLogs.Add(LogType.MyLog, LogImpact.Medium, $"{entityManager.ToPrettyString(uid)} did something!");
```
  
</details>

### Optional Entities
If you need to pass "optional" entities around, you should use a nullable `EntityUid` for this.
Never use `EntityUid.Invalid` to denote the abscence of `EntityUid`, always use `null` and nullability so we have compile-time checks.
e.g. `EntityUid? uid`

## Components

### Component data access modifiers
All data in components should be public.

### Component property setters
You may not have setters with any logic whatsoever in properties. Instead, you should create a setter method in your entity system, and apply the `[Friend(...)]` attribute to the component so only that system can modify it.
Your component may use properties with setter logic for *ViewVariables integration* (until we have a better system for that)

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

```csharp=
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

```csharp=
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
  
```csharp=
var random = IoCManager.Resolve<IRobustRandom>();
random.Prob(0.1f);
```

Add an entity system dependency:

```csharp=
[Dependency] private readonly IRobustRandom _random = default!;
_random.Prob(0.1f);
```

## Events

### Method Events vs Entity System Methods
Method Events are events that you raise when you want to perform a certain action. Example:
```csharp=
// This would change the damage on the entity by 10.
RaiseLocalEvent(uid, new ChangeDamageEvent(10));
```
On the other hand, Entity System Methods are methods you call on systems to perform an action.
```csharp=
// This would change the damage on the entity by 10.
EntitySystem.Get<DamageableSystem>().ChangeDamage(uid, 10);
```

Method Events are *prohibited*, always use Entity System Methods instead.
There's an exception to this, however.

You may use Method Events as long as they're wrapped by an Entity System Method.
In the example above, this would mean that `DamageableSystem.ChangeDamage()` would internally raise the `ChangeDamageEvent`, which would then by handled by any subscriptors...

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
  
```csharp=
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

```csharp=
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
  
## Naming

### Shared types
Shared types should only be prefixed with `Shared` if and only if there are server and/or client inherited types with the same name.

Example:
- If `FooComponent` only exists in shared, it doesn't need a prefix.
- If `BarComponent` exists in shared, server and client, the shared type should be prefixed with shared: `SharedBarComponent`.

## Physics

### Anchoring

Always use `TransformComponent` anchoring.
You may use `PhysicsComponent` static body anchoring but *only* if you know what you're doing and you can defend your choice over transform anchoring.
  
# YAML Conventions

- Every component `- type` should be together without any empty newlines separating them
- Separate prototypes with one empty newline.
- `name:` and `description:` fields should never have quotations unless punctuation in the name/description requires the use of them, then you will use ''. For example:
```yaml
  name: 'Spessman's Smokes packet'
  description: 'A label on the packaging reads, 'Wouldn't a slow death make a change?''
```
- Dont specify textures in abstract prototypes/parents.
- You should declare the first prototype block in this order: `type` > `abstract` > `parent` > `id`  > `name` > `description` > `components.`
- New components should not have an indent when added to the `components:` section.
    This
    ```yaml=
    components:
    - type: Sprite
      state: 
    ```
    Not this
    ```yaml=
    components:
      - type: Sprite
        state: 
    ```
- When it makes sense, place more generalized/engine components near the top of the components list and more specific components near the bottom of the list. For example,
    ```yaml=
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
  
## Entities

Please ensure you structure entities with components as follows for easier YAML readability:

```
 	 type: entity
  parent: Base<nameofparent>
  id: 
  name:
  abstract: 
  components:
 		<rest of file>
```
      
### Entity Prototype suffixes

Use `suffix` in prototypes, this it's a spawn-menu-only suffix that allows you to distinguish what prototypes are, without modifying the actual prototype name. You can use it like this: 
![](https://i.imgur.com/epkPR3Y.png)

And results in this: 
![](https://i.imgur.com/JigMCuu.png)

# Localization
Every player-facing string ever needs to be localized.

### Localization ID naming
- Localization IDs are always `kebab-case` and should never contain capital letters.
- Localization IDs should be specific as possible, to avoid clashing with other IDs.
    This
    ```ftl=
    antag-traitor-user-was-traitor-message = ...
    ```
    Not this
    ```ftl=
    traitor-message = ...
