# Variables

The outputs of toolshed commands can be stored in named variables using the assignment command `=>`. Variable names must begin with a `$`. For example, the following will define a simple int variable and repeatedly increment it a couple of times:

```
> i 1 => $x
1

> i 1 + $x => $x
2

> i 1 + $x => $x
3
```

The currently defined variables can be listed using the `vars` command:
```
> vars
more = ,
x = 4,
self = 3015
```

The `$self` and `$more` variables are special variables defined by the shell. `$self` points to the player's current entity, while `$more` is used if the output of a command is too large to print, in which case the remaining output can be requested by running the `more` command.


## `Var` Command

If you want to pipe the value stored in a variable into another command, you can use the `var` command, which effectively just reads out the value of a variable.

e.g.,

```
> var $x
3

> var $x * 2
6
```

## `Val` Command


As toolshed is a strongly typed, parsing a valid command run requires knowing the types of the values that will be returned by a command. Seeing as the contents of a variable may change as a command is executed, this means that some commands may fail to parse. In those instances, you can use the `val` command instead, though that requires you to explicitly specify the type.

```
> val int $x
3

> val int $x * 2
6
```