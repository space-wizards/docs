
# Types

As the output of the `explain` and `help` commands might suggest, Toolshed is a strongly typed language. The type system is, **for the most part** that of C#'s, though toolshed adds some additional type rules for the convenience of both users and developers. I.e., the outputs of commands are actual C# types like `int`, `EntityUid`, or some `IEnumerable<T>`, and not just strings. All commands have a type signature, and this signature can vary dynamically based on the type of the piped value.

For example, the type piped into the addition command `+` determines the output type, and how the argument is parsed.
For example, `i 1 + 2` and `f 1 + 2.5` are valid commands, but `i 1 + 1.5` will fail to parse "1.5" as an int argument.

```
> explain i 1 + 1

i - Integer constant.
Pipe input: [none]
Pipe output: Int32
Signature:
  i <value (Int32)>

+ - Performs numeric addition.
Pipe input: Int32
Pipe output: Int32
Signature:
  <x> → + <y (Int32)>

> explain f 1 + 1.5

f - Float constant.
Pipe input: [none]
Pipe output: Single
Signature:
  f <value (Single)>

+ - Performs numeric addition.
Pipe input: Single
Pipe output: Single
Signature:
  <x> → + <y (Single)>

> i 1 + 1.5

i 1 + 1.5
      ^^^
The value 1.5 is not a valid Int32.
```

## Type Arguments

Some command arguments also take in **type arguments**. These arguments usually determine the output type or how some of the other arguments are parsed. **Type arguments** arguments are always specified before any other arguments, but otherwise appear like normal arguments. In the `help` and `explain` command signatures they show up as part of the command's name using the c# generics syntax, i.e., `<T>`, `<T1, T2>`.

For example, the `comp:get<T>` command has the signature `IEnumerable<EntityUid> -> IEnumerable<T>`, where T is any user specified component. The actual component type specified via a **type arguments**:
```
> help comp:get

comp:get - Gets the given component from the given entity.
Usage:
  <input (IEnumerable<EntityUid>)> → comp:get<T> → IEnumerable<T>
  <input (EntityUid)> → comp:get<T> → T


> explain entities comp:get Item

entities - Returns all entities on the server.
Pipe input: [none]
Pipe output: IEnumerable<EntityUid>
Signature:
  entities

comp:get - Gets the given component from the given entity.
Pipe input: IEnumerable<EntityUid>
Pipe output: IEnumerable<ItemComponent>
Signature:
  <input> → comp:get<ItemComponent>
```

## For users
### All values are a list of length 1 (`T -> IEnumerable<T>`)
Toolshed will automatically cast a lone value into a list containing only that value, if necessary. This lets you apply enumerable only commands to single values if necessary.

### Any collection of T is an `IEnumerable<T>`
This isn't technically toolshed specific, but it's useful to know that one can use a `List<T>`, `HashSet<T>`, `Dictionary<K,V>`, etc, as the input to any command taking an enumerable.

### `IEnumerable<T>` is boxed into `List<T>` on assignment.
When assigning an enumerable to a variable, Toolshed will automatically coerce it into a list to fully evaluate it and allow you to reuse it.
Within C#, using an `IEnumerable<T>` more than once is disallowed, hence this coersion. 

## For developers
### Co-variance and Contra-variance limitations.
Toolshed will refuse to do complex assignability checks for types with more than one co-variant or contra-variant argument, as to avoid combinatorial explosion from searching all possible types to use.

### `IAsType<T>` and implicit casting.
Toolshed will, for any type implementing `IAsType<T>`, consider T to be a valid implicit cast for that type.
For example, if `Foo : IAsType<Bar>`, Toolshed will use the IAsType implementation to obtain Bar from Foo if it'd allow it to successfully typecheck a command run.