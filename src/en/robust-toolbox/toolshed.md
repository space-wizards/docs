# Toolshed

{{#template ../templates/wip.md}}

Toolshed is one of the three primary built-in debug tools (alongside `scsi` and View Variables.) for RobustToolbox, functioning as the game's development console. To use Toolshed, open the debug console or use the debug console in `devwindow`.

```admonish warning
Toolshed is not yet available on the client, so you need to use the `>` prefix command on the client in order to run its commands server-side. Ommiting this will often result in an error stating that you lack permission to run the command even if this is not the case.
```

Toolshed is a **pipeline shell**, and the primary method of performing complex actions is composition of commands. You can simply write multiple commands one after the other and as long as they are compatible, they will have their inputs successively fed to one another. For those familiar with shells like bash, this is typically done with an explicit pipe symbol like '|'.  However in toolshed the pipe operator is optional. 

For example, take the following **command run**:
```
entities with Item count
```
which could also be written with explicit pipe operators:
```
entities | with Item | count
```
This is three commands, `entities`, `with`, and `count`. They together form a **command run**, a set of successive commands. In this case, the combined effect is to return the total number of entities that have the `ItemComponent`.


```admonish warning
For convenience some of the examples used throughout the documentation may use types or commands that are specific to SS14 (e.g., ItemComponent), even though Toolshed is a part of RobustToolbox and not tied to SS14.
```


## Subcommands

Some commands are grouped together into a "command" with "subcommands". These are just collections of related commands whose names consist of two parts separated by a colon, the command name, and the subcommand name. E.g., there are commands for adding, removing, ensuring, and checking for components, and these are all grouped together as part of the "comp" command:
* `comp:get`
* `comp:has`
* `comp:add`
* `comp:rm`
* `comp:ensure`

Currently, this is mainly an organisational convention. For users, subcommands behave just like regular commands. They have no special relationship to each other, and the "comp" command doesn't actually exist.

## Help

The `help` command can be used to show the description and generic signatures of commands. For example:
```
> help count

count - Counts the amount of entries in it's input, returning an integer.
Usage:
  <input (IEnumerable<T>)> → count → Int32
```

The usage block shows the syntax for all implementations of that command. In this case there is only one. The usage syntax consists of up to three parts per implementation:
* The name and type of the piped input argument. Here this is the `<input (IEnumerable<T>)> → ` part. This is omitted if there is no piped input.
* The command itself, with any prefixes & arguments . As the count command has no arguments, here this is just `count`.
* The type of the output that can be piped into other commands. Here this is the `→ Int32` part. This is ommited if the command doesn't return anything.

The syntax of the piped and command arguments is `<Name (Type)>`, where the argument name and type are taken from the C# method associated with that command. If a command argument is optional, it will instead use square brackets (i.e., `[Name (Type)]`. Some commands also accept infinitely repeatable arguments, which are denoted with ellipses (i.e., `[Name (Type)]...`).

For a a more complicated example lets examine the `with` command that was used in the previous section. It can take in either an entity or an entity prototype, so it has multiple implementations. It also requires one argument and supports prefixes:

```
> help with

with - Filters the input entities by whether or not they have the given component.
The behaviour of this command can be inverted using the "not" prefix.
Usage:
  <input (IEnumerable<EntityUid>)> → [not] with <component (Type)> → IEnumerable<EntityUid>
  <input (IEnumerable<EntityPrototype>)> → [not] with <component (Type)> → IEnumerable<EntityPrototype>
  <input (IEnumerable<ProtoId<T>>)> → [not] with <protoId (ProtoId<T>)> → IEnumerable<ProtoId<T>>
```

The syntax of each command arguments is `<Name (Type)>`, where the argument name and type are taken from the C# method associated with that implementation. If a command argument is optional, it will instead use square brackets (i.e., `[Name (Type)]`. Some commands also accept infinitely repeatable arguments, which are denoted with ellipses (i.e., `[Name (Type)]...`). Note that in general each implementation can have different numbers and types of arguments, though in this case each implementation has exactly one argument.

As the above help output explains, the `with` command can be given an optional "not" prefix to invert its behaviour. So if we wanted to get a count of all entities that do not have an item component, we could use `entities not with Item count`. If a command supports prefixes, the help page should say so.

### Argument names

The name of an argument in the command's syntax can also help resolve some ambiguities about the order in which arguments should be specified. For example, the `tp:to` command teleports one entity to another. If you were unsure about whether the destination entity is the piped input or the first argument, you can check the name of the argument printed by the help command.

```
> help tp:to

tp:to - Teleports the given entities to the target entity.
Usage:
  <teleporter (EntityUid)> → tp:to <target (EntityUid)> → EntityUid
  <teleporters (IEnumerable<EntityUid>)> → tp:to <target (EntityUid)> → IEnumerable<EntityUid> 
```

```admonish warning
Note that using the c# argument names to auto-generate help strings is relatively new, and some commands may have badly named arguments.
```


## Explain 

You can use the `explain` command to provide information about a command run's flow. It's highly recommended you `explain` command runs you don't understand to get an idea of their flow. It will break any valid command run into its constituent commands, and for each command it will provide:
* A short description of the command
* The specific input and output types in the context of the given command run.
* The command's signature, including the **name** and type of any parsed arguments.

```admonish warning
Note that the explain command only works on **valid** commands. It can't be used to troubleshoot invalid commands. If you are unsure about how to use a command, maybe use the `help` command instead.
```

The generated explanation can be useful for understanding how each command in a run transforms the data being piped around, and the command signature hopefully makes it clearer what each argument does. For example, explaining the command from the previous section yields:

```
> explain entities with Item count

entities - Returns all entities on the server.
Pipe input: [none]
Pipe output: IEnumerable<EntityUid>
Signature:
  entities

with - Filters the input entities by whether or not they have the given component.
Pipe input: IEnumerable<EntityUid>
Pipe output: IEnumerable<EntityUid>
Signature:
  <input> → with <component (Type)>

count - Counts the amount of entries in it's input, returning an integer.
Pipe input: IEnumerable<EntityUid>
Pipe output: Int32
Signature:
  <input> → count
```

Note that here the type of the piped input argument for the count command is `IEnumerable<EntityUid>`, unlike in the `help` example, which used generic type (`IEnumerable<T>`). The explain command will only ever show the type and syntax for the concrete command implementation that is relevant to the command run that is being explained.

## Common commands

This section briefly describes some simple commands that are commonly used to help construct more complex command runs. These may be used throughout the docs when providing examples for how to use other commands.

For a description of some other commonly useful commands, see the [commands section](./toolshed/commands.md). For some examples of how to string toolshead commands together see [toolshead examples](./toolshed/toolshed-examples.md)

### Constants

These commands are often used at the start of a **command run** to provide some initial value that gets piped into other commands:
* `i`, returns an integer. E.g., `i 2`.
* `f`, returns an float. E.g., `f 2.1`.
* `b`, returns an bool. E.g., `b true`.
* `s`, returns an string. E.g., `s "foo"`.
* `ent`, returns an EntityUid. E.g., `ent 123`.
* `fpi`, `dpi` returns Pi, in floating or double precision.


### Maths
Toolshed supports many kinds of math operations, including, but not limited to:
* Simple operations: `+`, `-`, `\*`, `/`, `%`
* Common functions: `sin`, `abs`,`min`, `pow`, `ceil`, etc.
* Vector operations (i.e., multiplying a list by a number): `+/`, `-/`, `\*/`, `//`, `%/`
* Bitwise operations: `&`, `^`, `bitor`, `~`, `&~` `^~`, `bitornot`
 
### Ranges & Sequences

There are a few commands that are useful for creating or manipulating lists/sequences:
* `count` returns the total number of items in a sequence
* `to` is used to create a range of numbers. E.g., `i 3 to 5` returns `[3,4,5]`
* `iota` is used to create a range of numbers up to some value. E.g., `i 3 iota` returns `[1, 2, 3]`.
* `rep` repeats the input value. E.g., `i 5 rep 3` returns `[5, 5, 5]`.
* `append` adds a number to the end of a sequence.
* `join` combines two sequences (or strings). Can also be used to prepend a single item.
* `first` selects the first element in a sequence
* `take` takes the first N element in a sequence
* `select` randomly selects N elements or a percentage of elements from a sequence


## Terminators

Command argument parsing can be interrupted using either the explicit pipe symbol `|` or terminator symbol `;`. The former is primarily useful if a command has optional or repeatable arguments, or to make some commands easier to read & understand. The latter is mainly useful because it drops the piped output value, which can be used to chain otherwise incompatible commands together. For example:
```
> f 2 * 1.5; i 1 + 1
2
```
Without the `;` the above command would fail to parse, as the `i` command does not accept any piped in values.

## Errors and invalid commands

Before toolshed will attempt to execute a command run, it first has to successfully parse it. If it fails to parse the command, it should try to print out a useful error message that points to the specific part of the command that toolshed failed to parse. Note that the `explain` command only works on a valid command run, and cannot be used to figure out why a command run is not working. 

```admonish note
Toolshed often spits out lengthy stacktraces upon a command being used incorrectly. But typically there is a clearer error message above the stacktrace in your console, though you may have to scroll up to see it.
```

For example, in one of the earlier examples, there is a `with` command that expects either an EntityUid or Prototype input. If we instead give it an integer it will inform us that there is no `with` command that takes in that type:

```
> entities count with Items

entities count with Items
               ^^^^
Could not find an implementation of the 'with' command given the input type 'Int32'.
Accepted types: 'IEnumerable<EntityUid>','IEnumerable<EntityPrototype>','IEnumerable<ProtoId<T>>'.

   at Robust.Shared.Toolshed.ToolshedCommandImplementor.TryParse(ParserContext ctx, Func`2& invocable, Nullable`1& method)
   at Robust.Shared.Toolshed.Syntax.ParsedCommand.TryParseCommand(ParserContext ctx, Func`2& invocable, Nullable`1& method, ToolshedCommandImplementor& implementor)
   at Robust.Shared.Toolshed.Syntax.ParsedCommand.TryParse(ParserContext ctx, Type piped, ParsedCommand& result)
   at Robust.Shared.Toolshed.Syntax.CommandRun.TryParse(ParserContext ctx, Type pipedType, Type targetOutput, CommandRun& expr)
   at Robust.Shared.Toolshed.ToolshedManager.InvokeCommand(IInvocationContext ctx, String command, Object input, Object& result)
   at Robust.Shared.Toolshed.ToolshedManager.InvokeCommand(IConsoleShell session, String command, Object input, Object& result, IInvocationContext& ctx)
   at Robust.Server.Console.ServerConsoleHost.ExecuteInShell(IConsoleShell shell, String command)
   at Robust.Server.Console.ServerConsoleHost.ExecuteCommand(ICommonSession session, String command)
   at Robust.Server.Console.ServerConsoleHost.ProcessCommand(MsgConCmd message)
   at Robust.Shared.Network.NetManager.<>c__DisplayClass109_0`1.<RegisterNetMessage>b__0(NetMessage msg)
   at Robust.Shared.Network.NetManager.DispatchNetMessage(NetIncomingMessage msg)
   at Robust.Shared.Network.NetManager.ProcessPackets()
   at Robust.Server.BaseServer.Input(FrameEventArgs args)
   at Robust.Server.BaseServer.<SetupMainLoop>b__67_0(Object sender, FrameEventArgs args)
   at Robust.Shared.Timing.GameLoop.Run()
   at Robust.Server.BaseServer.MainLoop()
```

## Searching for commands

You can combine the `cmd:list` to get a list of all commands. You can then combine this with the `search` commands to search through this list for a command you are trying to find. E.g.,
```
cmd:list search "awn"

spawn:at,
spawn:on,
spawn:attached
```


