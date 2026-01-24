# Config File Reference

Config files are [TOML](https://toml.io/), a relatively modern and simple config file format.
By default, the server loads the config file from `server_config.toml` next to the executable. The client loads it from `GameControllerOptions.ConfigFileName` (defaults to `client_config.toml`) in the [User Data Directory](../../robust-toolbox/user-data-directory.md). 

Config files store "CVars", which is short for "console variable" but may also mean "config variable" depending on how much you care about being accurate to Quake or something. It doesn't really matter. Hey it's short to write.

## TOML Crash Course

TOML is basically just INI but somewhat more well-specified and hipster. You put headings in square brackets and keys below that. We do not use more advanced TOML stuff than shown here (since it sucks):

```toml
[net]
port = 12345

[game]
hostname = "honkhonk"
maxplayers = 64

[log]
enabled = true
```

When a CVar is referred to as `net.port`, that means put `port = foo` under the `[net]` header. For cases where you directly refer to a cvar in full (such as the `cvar` command) you write out the full name (like `cvar net.port`).

## CVar reference

if you want to find a reference of all CVars available in the game/engine, your best bet is to check the game and engine code: [`CCVars.<category>.cs` for Space Station 14](https://github.com/space-wizards/space-station-14/blob/master/Content.Shared/CCVar), [`CVars.cs` for Robust](https://github.com/space-wizards/RobustToolbox/blob/master/Robust.Shared/CVars.cs). It should be pretty easy to read.

## Ways of specifying CVars

* You can put them in the server or client config file and have it be loaded automatically.
* You can use the `cvar` command to view and set CVars at runtime. Note that not all CVars support changing them live: effects may include it working fine, server exploding, or nothing happening.
* You can pass `--cvar foo.bar=123` as command line argument to the client or server to override a CVar at start time. This also overrides any values set in config files.
* You can use the `ROBUST_CVARS` environment variable, which is semicolon-separated like so: `ROBUST_CVARS=foo.bar=1234;foo.baz=hello there`. You probably don't want to accept any insecure input into this, since it's pretty basic and can't be escaped properly.
* You can specify CVars via multiple environment variables with the `ROBUST_CVAR_` prefix (note the lack of plural from above). For example `ROBUST_CVAR_game__hostname=foobar`. A double underscore (`__`) is replaced with a `.`.
