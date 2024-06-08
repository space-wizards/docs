# Config File Reference

Config files are [TOML](https://toml.io/), a relatively modern and simple config file format.

By default, the server loads the config file from `server_config.toml` in the same directory as the executable.

The client loads their config file from `GameControllerOptions.ConfigFileName` (defaults to `client_config.toml`) in the User Data Directory (which can vary by operating system).

Config files store “`CVars`”, which is short for “console variable” but may also mean “config variable”.

## TOML Crash Course

TOML is basically just `INI` but somewhat more well-specified.

You put headings in square brackets and keys below that. This is as complicated as it gets:

````admonish example

```toml
# This is a comment
[net]
port = 12345

[game]
hostname = "honkhonk"
maxplayers = 64

[log]
enabled = true
```
````

When a `CVar` is referred to as `net.port`, that means put `port = foo` under the `[net]` header.

For cases where you directly refer to a `CVar` in full (such as the `cvar` command in the in-game console) you write out the full name (like `cvar net.port`).

## Ways of Specifying CVars

There are multiple different ways of specifying CVars:

1. Put them in the server or client config file and have it be loaded automatically.
2. Passing `--cvar foo.bar=123` in as a command-line argument will override the `CVar` at launch time (including overriding config files).
3. Use the `cvar` command on the console and set `CVars` at runtime. Note that not all `CVars` support runtime changes.
4. Setting the `ROBUST_CVARS` environment variable (Ex: `ROBUST_CVARS=foo.bar=1234;foo.baz=hello there`).
5. You can use multiple environment variables with the `ROBUST_CVAR_(.+)` formatting. (Ex: `ROBUST_CVAR_game__hostname=foobar`, where `__` is replaced with a `..`).

## CVar References

if you want to find a reference of all CVars available in the game/engine, your best bet is to check the game and engine code:

- [`Content.Shared/CCVar/CCVars.cs`](https://github.com/space-wizards/space-station-14/tree/master/Content.Shared/CCVar/CCVars.cs)
- [`RobustToolbox/Robust.Shared/CVars.cs`](https://github.com/space-wizards/RobustToolbox/tree/master/Robust.Shared/CVars.cs)
