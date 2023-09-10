# Toolshed

{{#template ../templates/wip.md}}

Toolshed is one of the three primary built-in debug tools (alongside `scsi` and View Variables.) for RobustToolbox, functioning as the game's development console. To use Toolshed, open the debug console or use the debug console in `devwindow`.

```admonish warning
Toolshed is not yet available on the client, so you need to use the `>` prefix command on the client in order to run its commands server-side.
```

Toolshed is a **pipeline shell**, and the primary method of performing complex actions is composition of commands. You can simply write multiple commands one after the other and as long as they are compatible, they will have their inputs successively fed to one another. For example, take the following **command run**:

```
entities with Item count
```

This is three commands, `entities`, `with`, and `count`. They together form a **command run**, a set of successive commands. You can use the `explain` command to provide information about a command run's flow. It's highly recommended you `explain` command runs you don't understand to get an idea of their flow.

```
{{#include toolshed/explain_example_1.txt}}
```
a
As the `explain` output might suggest, Toolshed is a strongly typed language. All commands have a type signature, and this signature can vary dynamically based on the type of the piped in value and on any **type arguments** provided.

For example, the `comp` command has the signature `IEnumerable<EntityUid> -> IEnumerable<T>`, where T is any user specified component.

```
{{#include toolshed/explain_example_2.txt}}
```

Toolshed also supports variables in which you can store values. You can use the `=>` command to do this. Variables can then be used anywhere a command accepts a `ValueRef`, which can be a block, constant, or variable. You can put `=>` in the middle of a command run as well to tee the value.
```
{{#include toolshed/explain_example_3.txt}}
```
