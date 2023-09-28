# Sandboxing

*or, how not to ruin your friend's sandcastle.*

Because we need to be able to download code from servers, but don't want that to allow servers to go full malware on people, SS14 employs sandboxing techniques so that content can't, well, go full malware on people.

## Current Implementation

Sandboxing is currently implemented with analysis of the content assemblies before they are loaded. Assemblies are first checked to be verifiable IL to ensure they do not do any *funny pointer stuff*. All referenced members (methods and fields) of the assembly are then checked against a whitelist. All APIs that could possibly be used to break sandbox are, of course, denied. 

## "Help I get a sandbox violation"

I will now list various advice with fixing sandbox violations if they crop up.

### Reference to `System.Activator` out of nowhere.

Internally, C# uses `Activator.CreateInstance()` if you instantiate a generic parameter like so:

```csharp
public static T Foo<T>() where T : new()
{
    return new T();
}
```

This *actually* compiles to:

```csharp
public static T Foo<T>() where T : new()
{
    return (T)Activator.CreateInstance(typeof(T));
}
```

As you can see, there is now a reference to `System.Activator`. We can't allow usage of this class directly since it can be very easily used to escape sandbox via e.g. the constructors on `StreamReader`.

To fix this, use `IDynamicTypeFactory.CreateInstance` or `ISandboxHelper.CreateInstance` instead. They verify that the type being constructed is a type defined in content, and is as such allowed.

### Unverifiable instruction

`stackalloc` in C# is unverifiable IL in all cases (yes, even when allocating to a `Span<T>` which is not unsafe) since the `localloc` instruction it uses is always unverifiable. Not a whole lot that can be done here sadly except "don't use `stackalloc`".

### Anything else

Of course the amount of not-whitelisted APIs is too large to count so for all of these I will defer to "ask on Discord if you can't figure out an alternative yourself".
