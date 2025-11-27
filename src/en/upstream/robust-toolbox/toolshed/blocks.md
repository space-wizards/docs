# Blocks

Blocks are **command runs** that are wrapped in curly braces. Much like variables, command blocks can be used in place of a command's normal arguments. For example, this command:
```
i 2 * { i 3 + 4 }
```
is effectively equivalent to
```
i 2 * 7
```

This quite useful for overriding the normal order of operations, or for combining together commands where the output of one is information that needs to be specified as an argument instead of as a piped input. Note the `explain` command currently does not explain the contents of command blocks, it simply treats them as if they were regularly specified arguments.

Some commands explicitly require a block to be provided **as** the argument, and cannot use normal arguments. The simplest example is the `map` command, which simply repeatedly evaluates a block for each input value:
```
> help map

map - Maps the input over the given block.
Usage:
  <value (IEnumerable<TIn>)> → map <block (Block<TIn,TOut>)> → IEnumerable<TOut>
```
This command is particularly useful if another command only takes in a single `TIn` and has no `IEnumerable<TIn>` support. For example, this command doubles then increments all values in a sequence using a command block that only takes in a single integer at a time:
```
> i 1 to 4 map { * 2 + 1 }

3,
5,
7,
9
```
Note that this is just an example, as there actually are specific maths commands for multiplying or adding single numbers to a sequence (`i 1 to 4 */ 2 +/ 1`).

As another example, the `sortby` command requires a block that takes in a type `T` and returns some other type that is comparable to itself  (`TOrd : IComomparable<TOrd>`). You could use this to do something like sorting entities based on the number of components they have:
```
entities with MobState sortby { allcomps count }
```

Blocks can be nested and combined together. For example, this command teleports all mobs to the mob that has the fewest components:
```
entities with MobState tp:to { entities with MobState sortby { allcomps count } first }
```
Though in practice you might want to split this command up to make it more readable:
```
entities with MobState => $mobs
var $mobs sortby { allcomps count } first => $destination
var $mobs tp:to $destination
```

Some commands that require blocks may also define block-local variables. I.e., variables that are only defined within the block, and that are often read-only. For an example, see the [Emplace command](./commands/emplace.md).