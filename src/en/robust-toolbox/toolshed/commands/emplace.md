# Emplace command

The `emplace` command is a command that takes in some enumerable and repeatedly executes a command block while providing some special read-only variables that are local to that command block. The variables that are provided depends on the input type, though the actual value itself is always available via the `$value` variable. In particular, if given entities it will define local variables that give access to some of the properties of that entity including:
* The entity's map coordinates `$wx`, `$wy`
* The entity's prototype `$proto`
* The entity's name `$name`
* The entity's description `$desc`
* Whether the entity is paused `$paused`
Similarly, an `ICommonSession` will provide the session's attached entity `$ent`, username `$name`, and `NetUserId` via `$userid`.

For example, this simple command will just return the y-coordinates of all entities:
```
entities emplace { var $wy } 
```
In general, the `emplace` command is useful if you want to use the properties of entities as the arguments for some other toolshed command.

# Do command

The `do` command is similar to the emplace command. It takes in some enumerable and command string, and will then try to repeatedly evaluate the command string (as if it had been typed into the console), possibly after having performed some string replacements.

The `do` command mainly exists for backwards compatibility with non-toolshed commands, which do not support toolshed variables. For example, as of the time of writing the `say` command is not a toolshed command. So if you wanted to make your own character say the positions of all mobs, you would need to use the `do` command:
```
entities with MobState do "say $WX $WY"
```

The list of string replacements differs from the variables made available in the emplace block. In particular, the current value is `$SELF` instead of `$value`. When given an entity, the following string replacements are made:
* `$ID` is replaced with the current EntityUid.
* `$PID` is replaced with the executing player's attached EntityUid.
* `$WX`, `$WY` is replaced with the entity's map coordinates.
* `$LX`, `$LY` is replaced with the entity's local coordinates.
