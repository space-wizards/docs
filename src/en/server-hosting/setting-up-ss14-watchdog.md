# Setting up SS14.Watchdog

```admonish info
Before jumping in the deep end here, you may want to *at least* go through hosting a vanilla server and learn how to administrate it.

It may also be useful to familiarize yourself with [setting up a developer environment](../general-development/setup/setting-up-a-development-environment.md), as you will need at least `dotnet` installed to compile the Watchdog, and Python installed to run certain server build scripts.

It is also worth going through the custom codebases section, especially if you intend to use any of these with a custom codebase.
```

<!--
  The following is a weird mixture of stuff.
  Some of it's partially migrated from the previous iteration of the hosting guide.
  Some of it's new.
  Some of it's sort of altered slightly.
-->

<!--
  Thanks I hate it
-->

[`SS14.Watchdog`](https://github.com/space-wizards/SS14.Watchdog/) (codename Ian) is our server-hosting wrapper thing, similar to TGS for BYOND (but much simpler for the time being). It handles auto updates, monitoring, automatic restarts, and administration. We recommend you use this for proper deployments.

## Setup Process

### 1. Check Prerequisites

You need to have:
+ .NET 6 SDK
+ ASP .NET Core 6 Runtime

Both of these can be found at the [.NET 6 download page](https://dotnet.microsoft.com/en-us/download/dotnet/6.0).

On Linux/MacOS use your favourite package manager (apt, dnf, pacman, brew etc)

### 2. Build

The following set of commands should build the Watchdog on a Linux system. You'll have to adjust it according to your actual system, of course.
```
# Download the SS14.Watchdog repository and any submodules/etc.
git clone --recursive https://github.com/space-wizards/SS14.Watchdog

# Switch into the SS14.Watchdog directory.
cd SS14.Watchdog

# Build the Watchdog.
# The result is placed into: SS14.Watchdog/bin/Release/net6.0/linux-x64/publish
dotnet publish -c Release -r linux-x64 --no-self-contained
```

The contents of `SS14.Watchdog/bin/Release/net6.0/linux-x64/publish` can then be copied to some other place.


### 3. Run

Assuming you've followed the structure laid out above, you simply need to have a terminal at the "main directory", and run `bin/SS14.Watchdog`.

## Watchdog Configuration

The watchdog configuration is split into two major sections:

+ Global elements, shared across all instances (servers).
+ Per-instance elements.

### Serilog, AllowedHosts

These shouldn't usually need to be changed, and are too complex to describe here.

### BaseUrl

This represents the external URL of the Watchdog.
This is passed to the instances automatically so that they can check in with the Watchdog.
It's also used in update modes which require clients to connect to the Watchdog for assets.

```yml
# Usually what you want, unless being used for client ZIPs.
BaseUrl: "http://localhost:5000/"
```

### Urls

This controls on which interfaces the Watchdog hosts, which may be important in some cases.
In particular, this can be used to expose the Watchdog outside of localhost without a reverse proxy, as so:
```yml
Urls: "http://*:5000"
```

See the relevant documentation for more details: https://docs.microsoft.com/en-us/aspnet/core/fundamentals/host/web-host?view=aspnetcore-6.0#server-urls

Be sure to adjust BaseUrl accordingly!

### Instances

Each instance is a separate game server, so the terms "instance" and "server" can be used semi-interchangably.

```yml
Servers:
  Instances:
    example:
      # This is intended to be the "human" name of the instance.
      # In practice, this is occasionally used in logging.
      # It doesn't affect game.hostname, for example.
      Name: "Example"

      # This is the API token for external access.
      # (As opposed to the API token used internally between the Watchdog and game server.
      #  That is randomly generated.)
      ApiToken: "you should choose a better token"

      # Somewhat misleadingly, this is the port of the game server on localhost.
      # This will NOT be automatically synchronized with the real port in the config.
      ApiPort: 1212

      # The update type and further options control where the server software is acquired from.
      # This example is for the official server builds.
      UpdateType: "Manifest"
      Updates:
        ManifestUrl: "https://central.spacestation14.io/builds/wizards/manifest.json"

      # The server is expected to ping the Watchdog occastionally.
      # (The aforementioned BaseUrl is passed to the server to facilitate this.)
      # This confirms the server has not, say, crashed.
      # If it has crashed, the server is forcibly restarted.
      # However, startup can a bit of a long process on some systems.
      TimeoutSeconds: 60
      # If enabled, if a freeze occurs, data on the state of the server is saved for analysis.
      # DumpOnTimeout: true
      # TimeoutDumpType controls how this is set, but I'm not sure on the details.

      # The program used to run the server can be set from here.
      # Note that realistically, this shouldn't need to be changed unless you are:
      # A. Trying to perform more advanced diagnostics (i.e. attaching a debugger)
      # B. Doing something very different from running a Space Station 14 server
      # RunCommand: "./wrapper.sh"

      # Environment variables can be set from here.
      # See for example Performance Tweaks in the Server Operator's Handbook.
      # EnvironmentVariables:
      #   ROBUST_NUMERICS_AVX: "true"
```

### Server Instance Folder

<!-- Mirrored Sloth's July 7th 2022 change (but added backticks around example directories) -->
The watchdog will automatically create a folder structure for each server instance. This is at `instances/<instanceId>`, e.g. `instances/wizards_den` / `instances/wizards_den_two`, relative to the current working directory when executing the watchdog.

Each instance folder has the following files and folders:

* `binaries/`: Is used to store client binaries when using the "Local" update type, see below.
* `bin/`: Contains the actual extracted server binaries.
* `data/`: Stores server data like player preferences.
* `config.toml`: Is the config file the server will load (the watchdog overrides the default location, `server_config.toml` next to the .exe, to avoid it getting deleted when the server resets).
* `data.json`: Contains watchdog information. If you changed the update type and are getting errors, delete this.

<!-- Mirrored Sloth's July 7th 2022 change (but adjusted cross-reference) -->
```admonish info
Note that although the watchdog handles server updates you may still want to setup the config.toml as per the server operator's handbook.
```

## Controlling The Watchdog

There are two key situations when the watchdog needs to be controlled.

Firstly, the watchdog will only update when it is either explicitly notified to check for an update, or when it is restarted.

Secondly, you may want to simply force a server to be restarted.

These tasks can be achieved with the following commands:

`curl -v -X POST -u myInstance:ApiToken http://localhost:5000/instances/myInstance/restart`

`curl -v -X POST -u myInstance:ApiToken http://localhost:5000/instances/myInstance/update`

## Update Types

### Manifest Update

```admonish info
The server still won't automatically be notified of updates, so see above for instructions.
```

For vanilla servers, the "Manifest" update type and the standard manifest URL is enough.

```yml
Servers:
  Instances:
    example:
      # (skipped...)
      UpdateType: "Manifest"
      Updates:
        ManifestUrl: "https://central.spacestation14.io/builds/wizards/manifest.json"
```

You will have to manually move files around and extract the server binaries.

Note that you should not move around or attempt to delete the files of a running server.

### Git-based Updates

```admonish danger "Here be dragons!"
Git-based update method is unmaintained. While it's the easiest to get started we can't really help you if it breaks. You are mostly on your own.
```

```admonish warning
Using Git-based updates in the intended manner may be in various states of "broken" because of various ways in which the repository can get into a state best described as, well, *broken*.
This shouldn't apply if you're just shipping precompiled updates to the server using Git, but that's also messy and not the intended way things were meant to work.
```

SS14.Watchdog can compile and update the server when commits are pushed to a branch of the Git repository that contains the source to your fork.

```
This requires the server to have the necessary parts of the developer environment.
Also, you still need to write a Git hook or somesuch to ensure that the Watchdog is notified of the updates, or otherwise cause it to periodically check for updates.
```admonish info


```yml
Servers:
  Instances:
    example:
      # (skipped...)
      UpdateType: "Git"
      Updates:
        # BaseUrl: The URL of the Git repository to watch.
        # This is distinct from the Watchdog-wide BaseUrl.
        BaseUrl: "https://github.com/moonheart08/outer-rim-14/"
        # Branch: The branch to watch.
        Branch: "master"
        # Hybrid ACZ: When enabled, the game server hosts the client zip rather than the watchdog.
        # As of the introduction of delta updating this is now the better way to handle this.
        HybridACZ: true
```

### Jenkins Updates

This is an ancient method, but it should still work.

```yml
Servers:
  Instances:
    example:
      # (skipped...)
      UpdateType: "Jenkins"
      Updates:
        BaseUrl: "http://localhost:9938"
        JobName: "Star"
```

### "Dummy" Update Provider

<!-- Nobody needs to know.
```admonish info
The "Local" update provider is the originally intended way to do what this update provider does.
However, since it's creation the game server itself has taken over what independent functionality the update provider had, and there are other disadvantages making Local more complicated to setup - so basically it's just worse.
```
-->

The "Dummy" update provider will fake an update whenever it is queried, and otherwise simply assume that a server has already been extracted to `bin/`.

As the Watchdog does not automatically periodically check for updates, the fake updates shouldn't get in the way.

To configure this, use the following update configuration in your `appsettings.yml`, in the entry for your server instance:

```yml
Servers:
  Instances:
    example:
      # (skipped...)
      UpdateType: "Dummy"
```

### Custom Auto Updates

Not supported, but it should be relatively trivial to edit the code for `SS14.Watchdog` to add support for whatever update mechanism you need. See `UpdateProvider.cs`.

## Update Types (DIY Edition)


### "Dummy" Update Provider, DIY Updates Edition

Before trying this, ensure you're familiar with how to use the "Dummy" Update Provider in general.

It is relatively simple to configure things in such a way as to allow for updates. The following instructions are for Unix-likes, but the idea should be comprehensible in any case.

Start with configuring as so:

```yml
Servers:
  Instances:
    example:
      # (skipped...)
      UpdateType: "Dummy"
      RunCommand: "./currentServer"
```

The basic premise of this mechanism is to use symbolic links to switch over which directory is actually used.

As such, three scripts, `switchTo`, `switchTo1` and `switchTo2`, are needed:

`switchTo`:
```
#!/bin/sh
rm currentServer switch inactiveBin ; mkdir -p $1
ln -s $1/Robust.Server currentServer ; ln -s $2 switch ; ln -s $3 inactiveBin
echo Switching to $1
curl -v -X POST -u myInstance:spooky http://localhost:5000/instances/myInstance/update
```

`switchTo1`:
```
#!/bin/sh
./switchTo bin1 switchTo2 bin2
```

`switchTo2`:
```
#!/bin/sh
./switchTo bin2 switchTo1 bin1
```

Once these are made executable (`chmod +x switchTo*`), and one of them is run, running `./switch` after that will toggle between the two directories.

As such, the workflow is to remove everything in `inactiveBin`, then extract a new server there, then run `./switch` to confirm it.

Before clearing and extracting a new server build to `inactiveBin`, be sure to make sure the server has actually restarted from any previous update and is actually no longer using that directory.

### DIY Manifest Server

This is a quick script useful in setting up a DIY server for the Manifest update type described in the "For Vanilla Servers" section.

It assumes you have some arbitrary static HTTP server, and you just need a script to output the JSON with an updated date (so you can just transfer two files to said static HTTP server and trigger an update).

```python
import json, datetime
nowish = datetime.datetime.now().isoformat()
print(json.dumps({"builds":{nowish: {"time": nowish, "client": {"url": "", "sha256": ""}, "server": {"linux-x64": {"url": "http://localhost:9283/SS14.Server_linux-x64.zip", "sha256": ""}}}}}))
```

## Systemd service

To allow the service to automatically start up with the server, you can make a service file. It will look something like this.

Of course, change it to the actual directory of your watchdog.

```/etc/systemd/system/SS14.Watchdog.service```
```toml
[Unit]
Description=SS14 Watchdog
After=network.target

[Service]
ExecStart=/path/to/SS14.Watchdog
WorkingDirectory=/path/to
Restart=always
# This is used for git method to not fail instantly.
Environment="DOTNET_CLI_HOME=/tmp"

[Install]
WantedBy=default.target
```
Now reload your systemd daemon and enable the service as you normally would.

```
systemctl daemon-reload
systemctl enable --now SS14.Watchdog
```

## General Troubleshooting

### Server keeps restarting every 30 seconds

This means the server isn't communicating with the watchdog correctly and the watchdog is forced to assume that the server is locked up or similar. This happens if `BaseUrl` in the watchdog configuration is set incorrectly or otherwise inaccessible by the game server.

### `System.IO.FileNotFoundException: Could not load file or assembly 'Mono.Posix.NETStandard, Version=1.0.0.0, Culture=neutral` (...)

Current working theory is that this is caused by improper dotnet publish options.
The below set of test results should help explain.

```
dotnet publish -c Release -r linux-x64 --no-self-contained SS14.Watchdog -o test
 RESULT: Mono.Posix.NETStandard.dll included, System.dll not included (as expected)

dotnet publish -c Release -r linux-x64 SS14.Watchdog -o test
 RESULT: Mono.Posix.NETStandard.dll included, System.dll included

dotnet publish -c Release SS14.Watchdog -o test
 RESULT: Mono.Posix.NETStandard.dll not included, System.dll not included
```

Since Watchdog uses `Mono.Posix.NETStandard.dll` to mark executables as executable on Linux and Mac OS X, it's important to have it around on those OSes.

## Old Example Config

(This section has been extracted from an older version of this guide with slight modification in case it is still of use. It may be outdated.)

Example from our official servers (obviously tokens redacted):

```yml
Serilog:
  Using: [ "Serilog.Sinks.Console", "Serilog.Sinks.Loki" ]
  MinimumLevel:
    Default: Information
    Override:
      SS14: Information
      Microsoft: "Warning"
      Microsoft.Hosting.Lifetime: "Information"
      Microsoft.AspNetCore: Warning

  WriteTo:
    - Name: Console
      Args:
        OutputTemplate: "[{Timestamp:HH:mm:ss} {Level:u3} {SourceContext}] {Message:lj}{NewLine}{Exception}"

  Enrich: [ "FromLogContext" ]

  # Uncomment to have watchdog log to Loki
  #Loki:
  #  Address: "{{ loki_addr }}"
  #  Name: "{{ server_id }}"
  #  Username: "{{ loki_user }}"
  #  password: "{{ loki_pass }}"

AllowedHosts: "*"

# API URL that your watchdog is accessible from.
# This HAS to be set so the game servers can communicate with the watchdog.
# If you don't want the watchdog to be publically accessible, do `http://localhost:5000/` here.
BaseUrl: https://builds.spacestation14.io/watchdog/

Servers:
  Instances:
    # ID of your server.
    wizards_den:
      # Name of the server
      Name: "Wizard's Den"
      ApiToken: "foobar" # API token to control this instance remotely like run updates, restart server.
      ApiPort: 1212 # API port OF THE GAME SERVER. This has to match the 1212 HTTP status API (described below). Otherwise the watchdog can't contact the game server for stuff.
      
      # Auto update configuration. This can be left out if you do not need auto updates. Example is for our officially hosted builds.
      # See above for alternatives.
      UpdateType: "Manifest"
      Updates:
        ManifestUrl: "https://central.spacestation14.io/builds/wizards/manifest.json"
        
      # Any environment variables you may want to specify.
      EnvironmentVariables:
        Foo: bar
```
