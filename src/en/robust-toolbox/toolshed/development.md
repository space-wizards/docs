
# Development

This section is intended for developers who want create their own Toolshed commands and largely consists of a lot of examples.

## Creating a New Command

To create a new Toolshed command, you have to create a new class that:
* Inherits from `ToolshedCommand`
* Is annotated with the `ToolshedCommandAttribute`
* Has one or more (non-static) methods that are annotated with the `CommandImplementationAttribute`. 

A minimal working example that defines a `foo` command would be:
```cs
[ToolshedCommand]
public sealed class FooCommand : ToolshedCommand
{
    [CommandImplementation]
    public void Bar()
    {
    }
}
```
The name of the command in the previous example is taken automatically from the name of the class, the method's name doesn't matter. I.e., the `FooCommand` class gets mapped to `foo`. Alternatively, the command name can be specified using the class attribute, e.g., `[ToolshedCommand(Name = "foo")]`.

## Arguments & Return Values
To define a command that returns some value that can then be piped into another command, you just have to give the method some return value. To give the command some arguments you just add arguments to the method. For example,
```cs
[ToolshedCommand]
public sealed class FooCommand : ToolshedCommand
{
    [CommandImplementation]
    public string Bar(string text, float number, EntityUid entity, BodyType physicsBodyType)
    {
        return $"{text}, {number}, {entity}, {physicsBodyType}";
    }
}
```
```
> foo "A!" 42 10 Dynamic
A!, 42, 10, Dynamic

> foo "A!" 42 10 Dynamic | join ", suffix" 
A!, 42, 10, Dynamic, suffix
```

Any method argument that does not have an attribute (and is not an `IInvocationContext` type) is assumed to be a normal command argument will attempt to be parsed from the command string by Toolshed. Optionally, these can also be explicitly annotated with the `CommandArgumentAttribute`.

Toolshed also supports methods with optional and `params []` arguments. E.g.,
```cs
[ToolshedCommand]
public sealed class SumCommand : ToolshedCommand
{
    [CommandImplementation]
    public int Sum(params int[] values)
    {
        return values.Sum();
    }
}
```

## Argument Parsers
Toolshed can parse any type of argument that has a corresponding `TypeParser<T>` implementation. For example, string arguments are parsed by the `StringTypeParser : TypeParser<string>` class. The parser is responsible for generating console command auto-completion options & hints. If a type is not yet supported, you can always just create your own parser.

If you want more control over how one of your arguments is parsed, or more control over auto-completion suggestions, you can also use the argument's attribute to specify that it should use a [custom parser](#custom-type-parsers).

## Piped Input Arguments
In order to create a command that can accept input values that get piped in from another command, you have to give the method an argument annotated with the `PipedArgumentAttribute`. For example, this creates a simple addition command:
```cs
[ToolshedCommand]
public sealed class AddCommand : ToolshedCommand
{
    [CommandImplementation]
    public int Add([PipedArgument] int x, int y)
    {
        return x + y;
    }
}
```

```
> i 2 | add 3
5
```

## Invertible Commands

In order to create a command whose behaviour can be inverted by prefixing it with the "not" keyword, you have to give the method has a `bool` argument that is annotated with the `CommandInvertedAttribute`. For example, this is a simple command that looks for a specific number in a sequence:
```cs
[ToolshedCommand]
internal sealed class ContainsIntCommand : ToolshedCommand
{
    [CommandImplementation]
    public bool ContainsInt([PipedArgument] IEnumerable<int> input, int value, [CommandInverted] bool inverted)
    {
        var result = input.Contains(value);
        return inverted ? !result : result;
    }
}
```

```
> i 1 to 5 | containsint 2
true

> i 1 to 5 | not containsint 2
false
```

## Invocation Contexts

If you want to create a command that writes output to the console or that can read & write Toolshed variables, you need to have a method that takes in an `IInvocationContext` argument. This argument can also optionally be annotated with the `CommandInvocationContextAttribute`. E.g., this is a simple command that will give out one-time greetings:
```cs
[ToolshedCommand]
public sealed class HelloCommand : ToolshedCommand
{
    [CommandImplementation]
    public void Hello(IInvocationContext ctx)
    {
        if (ctx.ReadVar("greeted") is true)
            return;

        ctx.WriteLine("Hello World!"); // Or WriteMarkup, or WriteError
        ctx.WriteVar("greeted", true);
    }
}
```
Currently the most common invocation context is the `OldShellInvocationContext`, where each player will have their own context that persists across disconnects & reconnects, but not server restarts. The context is also not networked, so commands executed client-side & server-side will use different invocation contexts.

## Dependencies

Toolshed commands support normal `EntitySystem` & manager dependency injections. So if your command needs to work with entity transforms, you can just give your class a normal dependency field, i.e.,
```cs
[Dependency] private readonly SharedTransformSystem _sys = default!;
```
The base `ToolshedCommand` class already provides the `ToolshedManager`, `ILocalizationManager`, and `IEntityManager` dependencies. It also defines some helpful `IEntityManager` proxy methods (e.g., `TryComp<T>`, `Spawn`, etc). So in general, you can just write code like you normally would within an `EntitySystem`.


## Multiple Implementations & Subcommands

So far, all of the examples have defined a command with a single implementation method. Commands can have more than one implementation, however each implementation must take in a different piped type. For example, this would result in a valid command that can take in either an integer or float:
```cs
[ToolshedCommand]
public sealed class ToStringCommand : ToolshedCommand
{
    [CommandImplementation]
    public string Impl([PipedArgument] int x)
    {
        return x.ToString();
    }
    
    [CommandImplementation]
    public string Impl([PipedArgument] float x)
    {
        return x.ToString();
    }
}
```

However, one of the limitations of Toolshed is that the combination of command name & piped input type must be unique. So you cannot define two implementations that take in the same piped type, but have different arguments. I.e., this is **not** a valid way of defining a command that takes in either a map or entity coordinate:
```cs
public sealed class TpCommand : ToolshedCommand
{
    [Dependency] private readonly SharedTransformSystem _sys = default!;

    [CommandImplementation]
    public void Teleport([PipedArgument] EntityUid uid, EntityCoordinates entCoords)
    {
        _sys.SetCoordinates(uid, entCoords);
    }

    [CommandImplementation]
    public void Teleport([PipedArgument] EntityUid uid, MapCoordinates mapCoords)
    {
        _sys.SetCoordinates(uid, _sys.ToCoordinates(mapCoords));
    }
}
```

This limitation is mainly due to the fact that Toolshed would have no way of figuring out which command or arguments it should be attempting to parse. Instead, if you wanted to introduce these kinds of variations of a command, you need to use **subcommands**. 

In some sense commands with subcommands are just normal commands that associate each implementation with its own unique name. These can be specified via the `CommandImplementationAttribute`. Note that if a command contains **any** named implementations, then all of them must be given a name. As an example, our earlier command could be fixed by naming the implementations:
```cs
public sealed class TpCommand : ToolshedCommand
{
    [Dependency] private readonly SharedTransformSystem _sys = default!;

    [CommandImplementation("ent")]
    public void Teleport([PipedArgument] EntityUid uid, EntityCoordinates entCoords)
    {
        _sys.SetCoordinates(uid, entCoords);
    }

    [CommandImplementation("map")]
    public void Teleport([PipedArgument] EntityUid uid, MapCoordinates mapCoords)
    {
        _sys.SetCoordinates(uid, _sys.ToCoordinates(mapCoords));
    }
}
```
This would define then define the "tp:ent" and "tp:map" commands.


## Generics

Toolshed commands have some support for C# generics, though there are a few limitations. The most common use case is when you want to define a method that takes in some arbitrary piped input type and should use the type of the input as the generic argument. In that case, you just give your generic method the `TakesPipedTypeAsGenericAttribute`. E.g., this is part of how the actual addition command is defined:
```cs
public sealed class AddCommand : ToolshedCommand
{
    [CommandImplementation, TakesPipedTypeAsGeneric]
    public T Operation<T>([PipedArgument] T x, T y) where T : IAdditionOperators<T, T, T>
    {
        return x + y;
    }
}
```

The `TakesPipedTypeAsGeneric` attribute also supports extracting the generic type even if it doesn't directly correspond to the type of the piped argument. E.g., if the piped argument is an `IEnumerable<T>`, it can still extract the generic type `T` from the piped value. For example, this is what the append command does:
```cs
[ToolshedCommand]
public sealed class AppendCommand : ToolshedCommand
{
    [CommandImplementation, TakesPipedTypeAsGeneric]
    public IEnumerable<T> Append<T>([PipedArgument] IEnumerable<T> x, T y)
    {
        return x.Append(y);
    }
}
```

However, in more complex situations this will likely fail. E.g., a signature like `Foo<T>([PipedArgument] Dictionary<int, List<(T, string)>> input)` will probably fail to extract `T` from a given piped input value. 

There is also no support for automatically determining multiple generic arguments from the piped input. If you want commands that use more complex generics, you will generally need to define a command that has explicit type arguments.

## Type Arguments

If you need to create a command that uses multiple generic arguments or has generics that can't automatically be inferred from the piped input, you need to use explicit type arguments. When writing out a shell command the type arguments look just like regular arguments, but they always precede any other argument and are used to determine the types for a generic implementation. 

To make your command require type arguments, you have to override the command's `TypeParameterParsers` property. This should return an array of types that inherit from `TypeParser<Type>`, and will be used to actually parse the type arguments from the command string. As this is a class-wide property this means that **all** implementations or subcommands must require the same number of type arguments. You can also combine explicit type arguments with the `TakesPipedTypeAsGenericAttribute`. Note that the automatically inferred type argument must always be the last type argument of that function.

For example, these two commands make use of explicit type arguments to print a C# style method invocation syntax:
```cs
[ToolshedCommand]
public sealed class FooCommand : ToolshedCommand
{
    public override Type[] TypeParameterParsers { get; } = [typeof(TypeTypeParser), typeof(TypeTypeParser)];

    [CommandImplementation]
    public string Foo<T1, T2>(int x)
    {
        return $"Foo<{typeof(T1).Name}, {typeof(T2).Name}>({x})";
    }
}

[ToolshedCommand]
public sealed class BarCommand : ToolshedCommand
{
    public override Type[] TypeParameterParsers { get; } = [typeof(TypeTypeParser)];

    [CommandImplementation, TakesPipedTypeAsGeneric]
    public string Bar<TExplicit, TAuto>([PipedArgument] TAuto x)
    {
        return $"Bar<{typeof(TExplicit).Name}, {typeof(TAuto).Name}>({x})";
    }
}

```

```
> foo string int 123
Foo<String, Int32>(123)

> i 123 | bar string 
Bar<String, Int32>(123)

> f 1.23 | bar String 
Bar<String, Single>(1.23)
```

## Automatic Type Conversions

As mentioned elsewhere int the docs, Toolshed will perform some automatic type conversions. Most notably, any command that expects an `IEnumerable<T>` will also accept being piped a `T`, as Toolshed will automatically converted it into an `IEnumerable<T>` with one element.

Toolshed will also automatically cast any type that implements the `IAsType<T>` interface. E.g., `Entity<T>` implements `IAsType<EntityUid>`. So Toolshed will allow you to pipe an `Entity<T>` output into a method that expects an `EntityUid` input.

## Custom Type Parsers

If you want to create a method that uses a custom parser, you can specify a custom parser via the an argument's `CommandArgumentAttribute`. This is useful if you want more control over the parsing or console auto-completion options/hints. 

For example, the following defines a method that uses a custom parser to get an integer from a binary string. Though in this specific case, you could just as easily have made the command take in a string and done the conversion within the command's own method, though then the argument would need to be wrapped in quotes (all string arguments need to be wrapped in quotes).
```cs
[ToolshedCommand]
public sealed class FromBinaryCommand : ToolshedCommand
{
    [CommandImplementation]
    public int FromBinary([CommandArgument(typeof(BinaryParser))] int value) => value;
}

public sealed class BinaryParser : CustomTypeParser<int>
{
    public override bool TryParse(ParserContext ctx, out int result)
    {
        var binaryText = ctx.GetWord();
        try
        {
            result = Convert.ToInt32(binaryText, 2);
            return true;
        }
        catch
        {
            result = 0;
            return false;
        }
    }

    public override CompletionResult? TryAutocomplete(ParserContext ctx, CommandArgument? arg)
        => CompletionResult.FromHint("<binary number>");
}
```

```
> frombinary 10101
21
```


## Permissions

```admonish warning
This section is specific to SS14, as RobustToolbox does not come with a command permission implementation.
```

All Toolshed commands need to specify some permissions in order to be executable, and there is an integration test that checks that this is the case (`AdminTest.AllCommandsHavePermissions`). The permissions for commands defined in the engine are specified in `/Resources/toolshedEngineCommandPerms.yml`, while Content commands can be given permissions by annotating the command class with the usual attributes (`AnyCommandAttribute`, `AdminCommandAttribute`). Permissions can't be specified per-subcommands, all subcommands must have the same permissions.


## Auto-Completion, Hints, & localization

Every Toolshed command should have a localized description. The key for the localized string is based on the (sub)command name. E.g., `foo` or `foo:bar` uses "command-description-foo" or "command-description-foo-bar". If the command name contains non-ascii characters, it will instead use the name of the class. E.g., the addition command (+) is defined in the `AddCommand` class, thus it uses "command-description-AddCommand".

Toolshed will automatically generate help strings for commands in the form of the method's signature. The auto-generated help string can be overridden by defining a localized string. E.g., the foo command's help can be overridden by defining a localized string with the key "command-help-foo".

### Argument Hints

Most of the Toolshed argument parsers will automatically generate console-completion hints while writing the arguments for a command. E.g., while writing the argument for a method like `Foo(int myNumber)` it will generate the hint `[myNumber (int)]`. If you want to override the auto-generated hint, you can do so by defining a localized string with the key "command-arg-hint-foo-myNumber". If you want more control over the hint or auto-completion suggestions, you can use a custom parser.


## Error Reporting

TODO

## Command Blocks

TODO 