# Serialization
## The API
Each API-Surface (excluding Composition) of the SerializationManager has a generic variant, as well as a boxing variant.
Additionally, each has two more generic methods for directly invoking TypeInterfaces, one where you can provide the instance used, and another where you'll just need to provide the type and the manager will take care of fetching an instance to use.

### Common parameters
In this section, we will touch on parameters found on all APIs. Therefore, we will not mention them again when discussing the specific APIs.

#### NotNullableOverride
Due to reference types allowing a null-pointer, but current C#/CIL APIs making it impossible to tell if a generic reference type argument has been annotated as (not)nullable, we have added an override flag called `notNullableOverride` in the form of a `bool` parameter. **Set this parameter to true if you do not want the method to return null values!**

```admonish info
Correct usage of this parameter is now enforced by an analyzer. If you need to use it, or if you are using it incorrectly, your IDE should tell you.
```

#### SerializationContext
Can be used to provide a context instance if you so wish to. See [SerializationContext](#serialization-context) for more info on how to create a context.

#### SkipHook
All APIs also provide you with a `bool` parameter called `skipHook`, which can be used to skip invoking methods implemented using the `ISerializationHook` interface. **Take note however, this parameter is due to be deprecated.** This parameter is not available in Write,Validate and Composition-APIs!

### Read
When reading, you will have to provide:
- A type, either as generic type argument T or as the type parameter in the boxing variant
- A DataNode to read (duh)
Optionally, you will also have the option to provide an `instanceProvider`. This will be a delegate that will provide a value to be used to read into. This can be used to for example reuse instances of an object instead of allocating a new one. If this all sounds like gibberish to you, do not worry, you will likely not have to use this at any time coding for our game.

```admonish warning
The InstanceProvider should never EVER return a null value. This will throw an exception (in debug builds).
```

### Write
For writing, you will, again, have to specify:
- A type, either as generic type argument T or as a type parameter in the boxing variant. Take note however that here, one boxing variant exists that does not need the type to be specified, since it'll fetch it using object.GetType()
Optionally, you can specify an `alwaysWrite` flag to force for the entire object to be written to yaml. Otherwise, the serializer will omit field values that are equal to the default value specified.
### Validate
Validate is, i would argue, among the more simple APIs we provide. Here, you provide:
- A type, either as generic type argument T or as a type parameter
- A node to validate
In return you will get a ValidationNode providing information about the validity of the DataNode.
### Copy
Our Copy API is split up into two parts: CopyTo and CreateCopy.
With CopyTo, you will be able to copy values from one object to another. With CreateCopy, you will create a copy of the object you pass into it.

```admonish warning
If CopyTo fails to copy into the target object, it will override it using a call to CreateCopy.
```

### Composition
Here, composition is pushed across nodes using definitions associated to the type passed. This means that the type you pass determines how the datanodes you provide will be merged together. Currently, there is only a very limited amount of methods to customize this behaviour, especially on DataFields. However, we are working on it!

## Data Definitions
DataDefinitions are Structs or Classes with Field/Properties annotated to be DataFields. These DataFields are written and read to and from yaml, but are also used for copy, validation & composition operations. Going forward, i will simply refer to structs & classes as a "type".

Data definitions must have a parameterless constructor in order to be valid. (With the exception of [DataRecords](#dataRecords))

### Declaring a DataDefinition
```admonish note
There exists no risk in declaring a DataDefinition with multiple of these options at once. The duplicate registrations will simply be reduced so a single one.
```

`DataDefinition`s must be declared `partial` in order to work with our source generator for copying.

#### Directly
To make a class become a DataDefinition, you can add a [DataDefinition] attribute to the type like so.
```csharp
[DataDefinition]
public sealed partial class MyClass {}

[DataDefinition]
public partial struct MyStruct {}
```

#### All inheritors of a type
If you have a base type or an interface of which you want all inheritors to automatically become datadefinitions, you annotate the base type or interface with [ImplicitDataDefinitionForInheritors]. All currently annotated types can be found [here](https://github.com/search?q=org%3Aspace-wizards+%5BImplicitDataDefinitionForInheritors%5D&type=code), where you will probably find a lot of types/interfaces you've inherited/implemented before.
```csharp
[ImplicitDataDefinitionForInheritors]
public interface IContainer {}

[ImplicitDataDefinitionForInheritors]
public abstract class BaseType {}

// Container will be a DataDefinition
public sealed partial class Container : IContainer {}

// SomeStruct will be a DataDefinition
public partial struct SomeStruct : IContainer {}

// SomeType will be a DataDefinition
public sealed partial class SomeType : BaseType {}
```

#### All types annotated by specific attribute
If you instead have an attribute which you will add to all of your data definitions, add a [MeansDataDefinition] attribute to your own attribute. A prominent example of this is the PrototypeAttribute you've probably seen before:
```csharp
[MeansDataDefinition]
public sealed class PrototypeAttribute : Attribute {
    ...
}

// Any class tagged with [Prototype] will automatically become a data definition.
```

### DataFields
#### Types of DataFields
##### Regular
Any field or property on a data definition can be annotated with a [DataField] attribute.  
In the following, both properties and fields will simply be referred to as "field".  

```csharp
[DataField]
protected Color Color { get; set; } = Color.White;
```

The example above would translate into YAML like this:

```yaml
color: White
```

This attribute accepts an optional string key which can be used to define the key in YAML, instead of the camel-case version of the field name.  
**If one is not needed, it is preferred to not specify one.**

```csharp
[DataField("colorValue")]
protected Color Color { get; set; } = Color.White;
```

The example above would translate into YAML like this:

```yaml
colorValue: White
```

##### Include DataField
A DataDefinition gets written into and read from a MappingDataNode. Other than the regular datafield, the Include DataField will not get a value from a key of that MappingDataNode to read/write from/to the field, but will instead use the MappingDataNode of the entire DataDefinition to perform its read/write-operation.
This has specific implications on writing specifically: IncludeDataFields get serialized last, and the produced mapping will be inserted into the mapping of the datadefinition that was already produced. If a key already exists, the new value produced by serializing the IncludeDataField will be ignored.

```admonish note
This behaviour might become configurable in the future.
```

#### Custom Type Serializer
A custom type serializer can be specified if one doesn't exist by default or custom behavior is needed to serialize a specific type. To use one, pass it through the customTypeSerializer argument.
Both the DataField and IncludeDataField support custom type interfaces, but only the DataFieldAttribute is used in the following examples to make them a tad less bloaty.

```admonish warning
This type does NOT need to implement ITypeSerializer. You only need to implement the interfaces you need!
Any other behaviour that wont differ from the normal one does not need to be redefined! If an interface for a specific action does not exist, the normal behaviour will just be used!
```

```csharp
[DataField(customTypeSerializer: typeof(ConstantSerializer<DrawDepthTag>))]
private int DrawDepth { get; set; } = DrawDepthTag.Default;
```

##### Constants
When annotating an int field that represents a constant defined by [ConstantsForAttribute], a custom type serializer must be specified in [DataField]:

```csharp
/// <summary>
///     Tag type for defining the representation of rendering draw depth in
///     terms of named constants in the content. To understand more about the
///     point of this type, see the <see cref="ConstantsForAttribute"/>.
/// </summary>
public sealed class DrawDepth
{
    /// <summary>
    ///     The default draw depth. The content enum which represents draw depth
    ///     should respect this value, since it is used in the engine.
    /// </summary>
    public const int Default = 0;
}

public sealed partial class SpriteComponent
{
    [DataField(customTypeSerializer: typeof(ConstantSerializer<DrawDepthTag>))]
    private int DrawDepth { get; set; } = DrawDepthTag.Default;
}
```

##### Flags
To define int data fields that represent a flag enum annotated with a [FlagsFor] attribute, the process is the same but the serializer used is different.

```csharp
/// <summary>
///     Tag type for defining the representation of the collision layer bitmask
///     in terms of readable names in the content. To understand more about the
///     point of this type, see the <see cref="FlagsForAttribute"/>.
/// </summary>
public sealed class CollisionLayer {}

public sealed partial class PhysShapeRect
{
    [DataField(customTypeSerializer: typeof(FlagSerializer<CollisionLayer>))]
    private int CollisionLayer { get; set; }
}
```

#### Inheritance Behaviour
Two additional attributes may be used on a datafield to define how it is inherited, [AlwaysPushInheritance] and [NeverPushInheritance]. This is again both applicable to the DataField and IncludeDataField

**[AlwaysPushInheritance]** is used in cases where you want field entry data to be inherited even when mapped, such as the components of an entity prototype.

**[NeverPushInheritance]** is used to signal that a value in for example a prototype must not be pushed to inheriting prototypes, such as the abstract property.

### DataRecords

TODO

## Type serializer
The type serializer interfaces are a collection of interfaces for defining custom logic for actions on specific types. Sometimes, the expected node type will also be specified.
A class implementing at least one of these type serializer interfaces is referred to as a type serializer. If you want your type serializer to *always* be used, you can annotated it with the `[TypeSerializer]` attribute. Otherwise, the type can be used as a [custom type serializer](#custom-type-serializer).

**The static IoCManager.Resolve should not be used as the serializer might be running on a separate thread without an initialized IoC context.**

## Serialization Context
You can create a SerializationContext by implementing the ISerializationContext interface on a type. The type will the provide a SerializationProvider which it can use to register typeserializers on.
Currently used by the MapContext during map loading:
https://github.com/space-wizards/RobustToolbox/blob/025fa958549b4d63e4888a810f780c53e6fb89a9/Robust.Shared/Map/MapSerializationContext.cs#L17-L51

---

## Hamster

![](https://i.imgur.com/VPl1P8B.png)
