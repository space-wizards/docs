# Emplace command

The `emplace` command is a command that takes in some enumerable and repeatedly executes a command block while providing some special read-only variables that are local to that command block. The variables that are provided depends on the input type. In particular, if given entities it will create variables that give access to some of the properties of that entity including:
* The entity's map coordinates `$wx`, `$wy`
* The entity's prototype `$proto`
* The entity's name `$name`
* The entity's description `$desc`
* Whether the entity is paused `$paused`

For example, this simple command will just return the y-coordinates of all entities:
```
entities emplace { var $wy } 
```
In general, the `emplace` command is useful if you want to use the properties of entities as the arguments for some other toolshed command.

Some of the variables defined by the `emplace` command are listed in the `help` command:
```
> help emplace

emplace - Runs the given block over it's inputs, with the input value placed into the variable $value within the block.
Additionally breaks out $wx, $wy, $proto, $desc, $name, and $paused for entities.
Can also have breakout values for other types, consult the documentation for that type for further info.
Usage:
  <value (TIn)> → emplace <block (Block)> → TOut
  <value (IEnumerable<TIn>)> → emplace <block (Block)> → IEnumerable<TOut>
```

# Do command

The `do` command is similar to the emplace command. It takes in some enumerable and command string, and will then try to repeatedly evaluate the command string (as if it had been typed into the console), possibly after having performed some string substitutions.

The `do` command mainly exists for backwards compatibility with non-toolshed commands, which do not support toolshed variables. For example, as of the time of writing the `say` command is not a toolshed command. So if you wanted to make your own character say the positions of all mobs, you would need to use the `do` command:
```
entities with MobState do "say $WX $WY"
```