# Server Hosting Tutorial

Hosting a local sandbox server for playing around is easy, but setting up a large production server supporting hundreds of players is a bit harder. This guide is organized into "levels" corresponding to difficulty.

## Level 0: Local Pre-built Server

This is for people who are just testing and bug-hunting the game. This server would have **no custom or modified code** and would merely act as a sandbox allowing you to spawn in things until you track down what an issue is. Or just goof around.

This assumes that you have not completed the [Development Environment guide](../setup/development-environment.md) as that's not required for something as basic as this.

1. Download and install the [.NET 8 Runtime](https://dotnet.microsoft.com/download).  
   Make sure you install the x64 version under "run console apps" and not "hosting bundle".
2. Download the latest version of the server from our [builds page](https://central.spacestation14.io/builds/wizards/builds.html), for your operating system. If your operating system isn't listed or you want to run custom code, read [Level 1](#level-1-local-custom-code-server).
3. Extract the `.zip` file.
4. In that folder you extracted, depending on your operating system you will run:
   - **Windows**: `./run_server.bat`
   - **MacOS/Linux**: `./Robust.Server` (This is an executable)
5. Open your Space Station 14 client and click `Direct Connect To Server` and type in `localhost` and click `connect`.
6. If you ever want to update your server, just download the server and repeat the same steps from 2 onward.

## Level 1: Public Server

Lets say you want to have a private community server or a server to run play-tests through.

The purpose of this is to give you the ability to run a play-test, not for you to run a production server. This will skip over everything that isn't strictly needed for a developer to test out their changes or for a small group to have fun playing privately.

```admonish danger
This will be skipping over some stuff that is _very_ important to server administrators, and if you're planning to host a real server that's listed on the hub, you will need to read a lot more.
```

To get your public custom code server running, do:

1. Have a [Local Custom Server](#level-0-local-pre-build-server) that is deployed and running.
2. Enable port forwarding on the server/host.
   - **UDP `1212`** is used for SS14's net-code. This is necessary for the _client_ to be able to connect to the server. This can be configured with the net.port configuration variable.
   - **TCP `1212`** is the HTTP status API. This is also necessary for the _launcher_ to be able to connect to the server. You do not need this to connect with a bare client, but if you are doing a public play-test, you will need to support the launcher. This can be configured with the `status.bind` configuration variable (which takes in a string like `*:1212` or `127.0.0.1:3000`).
3. Set some sane configuration variables in `server_config.toml`. Here is the suggested defaults:

   ```toml
   [net]
   # Reducing tickrate to 30 is basically unnoticeable
   # but reduces server, client and network load dramatically.
   tickrate = 30

   [game]
   # Changes the name of the server as it appears in the lobby and launcher.
   hostname = "Foo Station Public Play-test"
   # Enables the lobby instead of straight up throwing clients into a game.
   lobbyenabled = true

   [auth]
   # Enforces authentication so that ALL connecting clients must have a proper account.
   # Otherwise, guest logins are allowed.
   # Possible values here are: 0 (optional), 1 (required), 2 (disabled)
   mode = 1
   ```

4. Give your client administrator permissions through one of these three methods:
   - Connecting to the server over localhost (ip `127.0.0.1` or `::1`), you will automatically be given `+HOST` privileges.
   - Set the `console.login_host_user` CVar to your username.
   - Run `promotehost [username]` on the server to temporarily give `+HOST` permissions to the connected client.
5. Now, you can share the ip address of the server, and play-testers can connect directly to the server.

```admonish danger
`+HOST` privleges are **extremely dangerous** and it's equivelent to giving them physical access to the server/computer/host.

This will let them take over your computer.
```

## Level 2: Server With Custom Code

You will need a local [development environment](../setup/development-environment.md) in order to create a server with custom code or for some foreign architecture/operating system.

If you just want to quickly run and kill the server, you can [follow the development environment guide to start the server and client](../setup/development-environment.md#4-starting-ss14).

If you want to actually simulate how your code would run in an actual server environment with release optimizations, you can build and package it up like Space Wizards does for the official builds.

```admonish note
If you are running an older server before Content packaging was a thing, or need to use the legacy script (not supported anymore) then use this: `python3 Tools/package_server_build.py --hybrid-acz`
```

1. Have a [development environment set up](../setup/development-environment.md).
2. In that directory, run the packaging tool to build the repository:
   ```bash
   dotnet build Content.Packaging --configuration Release
   ```
3. Now, you can build it for your specialized target. (Platforms supported are: `linux-x64`, `linux-arm64`, `win-x64`, `osx-64`)
   ```bash
   dotnet run --project Content.Packaging server --hybrid-acz --platform linux-x64
   ```
4. Now, you can go into the `/release` directory and it should have a `SS14.Server_[platform].zip` which you can deploy following [Level 0](#level-0-local-pre-built-debuggingsandbox-server).

```admonish note
We're intentionally skipping over the `--hybrid-acz` flag, which is explained in a different guide. All you need to know here is that `hybrid-acz` allows the client to download your custom content from the server over-the-wire.
```

## Level 3: A "Production" Server

If you're planning to host a public server this is the bare minimum you'll need to do to have a small-to-medium sized public server.

This is not perfect, as it does not handle automatic restarts (in the case of a crash) or automatic updates, nor will it by default advertise on the hub. This is the manual option, as we would recommend using the next level.

### Setting Rules

By default, the server ships with the rules that are used on Wizard's Den servers.

To set custom rules for your own server:

1. Add a file with your rules to the `Resources/ServerInfo/` directory.
2. Set the `server.rules_file` CCVar with the base name of your rules file (just the file name without the leading path).

### Getting Your Server on the Hub

By default, your server will not advertise to the hub. To change, this, you need to edit your config.

1. Read the [hub server rules](../../community/space-wizards-hub-rules.md) before putting your server on the hub. Advertising to the hub constitutes acceptance of the hub rules.

2. Pick tags for your server based on the [standard tags](../../robust-toolbox/server-http-api.md#standard-tags).

3. Add the following lines to your [server configuration](../tips/config-file-reference.md):

   ```toml
   [hub]
   advertise = true
   # Uncomment to change the server URL advertised on the master server list.
   # Use this if you want an ss14s:// URL or have configured the server behind a reverse proxy or any of that.
   # Defaults to "ss14://[public server IP]:networking port"
   # server_url = "ss14://..."
   tags = "" # comma separated list of tags
   ```

### Bare Server Build Configuration

If you want to set up a more permanent server, you'll need to re-host the client downloads somewhere (such as a CDN). Anywhere accessible via a plain URL is fine.

1. You will want to edit the server config file (`server_config.toml`) to add the following to it:

```toml
[build]
# Download locations of the entire client build in a zip, as a HTTP (or HTTPS) URL.
download_url = ""
```

### Performance Tweaks

There are also many tweaks that can be made to increase performance.

Here are some settings you probably want to enable on your server to improve performance (at the cost of marginal startup time):

Add these to enable full dynamic PGO:

```
DOTNET_TieredPGO: 1
DOTNET_TC_QuickJitForLoops: 1
DOTNET_ReadyToRun: 0
```

Add these to enable AVX operations, which depending on the processor may help or hinder performance.

```
ROBUST_NUMERICS_AVX: true
```

## Level 4: Production Watchdog Server

[`SS14.Watchdog`](https://github.com/space-wizards/SS14.Watchdog/) is an integrated solution for people who are trying to have a production-ready SS14 server deployment. It's similar to TGF for BYOND, and handles things like auto-updating, monitors, automatic restarts, and administration features.

This is highly recommended for production deployments.

### Installation

[`Refer to this guide`](https://docs.spacestation14.com/en/server-hosting/setting-up-ss14-watchdog.html) for instructions on building and configuring Watchdog.

### Server Instance Folder

The watchdog will automatically create a folder structure for each server instance. This is at `instances/<instanceId>`, e.g. instances/wizards_den / instances/wizards_den_two, relative to the current working directory when executing the watchdog.

Each instance folder has the following files and folders:

- `binaries/`: Stores client binaries when using the "Local" update type, see below.
- `bin/`: Contains the actual extracted server binaries.
- `data/`: Stores server data like player preferences.
- `config.toml`: Is the config file the server will load (the watchdog overrides the default location, `server_config.toml` next to the .exe, to avoid it getting deleted when the server resets).

```admonish info
Note that although Watchdog handles server updates, you may still want to setup the `config.toml` as per the [Bare Server Configuration](#bare-server-build-configuration) section.
```

### Update types

Watchdog supports 4 different types of update types:

1. Jenkins
2. Local
3. Git
4. Manifest

If you wish to obtain more information you can browse the `SS14.Watchdog` repository to see how they work.

```admonish note
TODO: Explain the update providers better and explain hybrid ACZ.
```

#### 1. Jenkins Updates

```admonish note
This section is unfinished... Ask in the Discord for help.
```

#### 2. "Manual" Local Updates

You can use the watchdog with local files, and have it automatically generate the necessary build information. This will also host the client binaries for you.

To configure this, use the following update configuration in your `appsettings.yml`, in the entry for your server instance:

```yml
UpdateType: "Local"
Updates:
  Version: "foobar" # Version string to use.
```

The watchdog will automatically host client binaries. Where does it pull them from? The `binaries/` folder in your server instance folder! Note that for this to work, the watchdog HAS to be publicly accessible via `BaseUrl` in the config file.

You can edit the `Version:` specified in the config to tell the launcher that it should update the game next time you connect.

You will have to manually move files around and extract the server binaries.

#### 3. Git

This provider has 3 options available

- BaseUrl: This is the url for the repository, i.e. https://github.com/space-wizards/space-station-14
- Branch: The branch to checkout from the repository. This defaults to master
- HybridACZ: `true` or `false`. You most likely want to keep this `true`

#### 4. Manifest

TBC

#### Custom Auto Updates

Not supported, but it should be relatively trivial to edit the code for `SS14.Watchdog` to add support for whatever update mechanism you need. See `UpdateProvider.cs`.

### Server Build Configuration

The launcher needs to download the client binary to be able to run the game. It gets information about this client binary from the game server via an info API.

The information returned from this API is configured in two ways: `build.json` and `build.*` configuration variables.

`build.json` is a file that gets put next to the server executable automatically by the build system. This is how the server knows what the build info is when just downloading a bare server zip. (note that this is NOT done by `package_release_build.py`, since it relies on extra build information. `gen_build_info.py` does it in a separate step)

The second option is by specifying configuration variables (from command line or config file, both work):

```toml
[build]
# "Identifier" of your codebase. This is used by the launcher to manage installations.
# Try to keep this unique between different codebases.
# Nothing will break if you don't (or if there's a malicious actor),
# but the launcher WILL be forced to redownload files more often than otherwise necessary.
fork_id = ""

# Version string of the current build running on the server.
# This just prompts the launcher to redownload if it's different.
version = ""

# Version of the engine to download.
# Engine versions are hosted by us and will probably stay up forever.
# At least, as long as they are not found to be vulnerable to any security exploits, then we may pull them.
engine_version = ""

# Download locations of the entire client build in a zip, as a HTTP/HTTPS URL.
download_url = ""

# SHA256 hash of client zip files specified above.
hash = ""
```

Note that `SS14.Watchdog` specifies _most_ of it for you if you have configured it with auto updates (depending on update provider). It notably cannot provide `engine_version` or `fork_id` version, so you're best off specifying the former in build.json (your build system should be non garbage for this) and the latter in a config file.

## Level 5: Big Production Server

Things that aren't necessary for small/private servers, but strongly recommended for forks or larger production servers.

### Advanced Port Forwarding

You can slap the HTTP status API behind a reverse proxy if you want. This is recommended for production servers since then you can do HTTPS (slap it behind nginx and turn on HTTPS). Note that if you do this you have to set the `status.connectaddress` config variable to specify the UDP address the main netcode should connect to. This has to look like this: `udp://server.spacestation14.io:1212` (for our server, obviously substitute with your parameters).

### PostgreSQL Setup

SS14 uses an SQL database to store server data like player slots. By default, an **SQLite** database is automatically used which is sufficient for local testing and small servers. If you want the ability to share the database between multiple servers or such however, the server also supports connecting to **PostgreSQL**.
Support for MySQL/MariaDB isn't currently planned, but we will accept contributions.

Relevant configuration properties, along with default values:

```toml
# Server config file
[database]
# Database type to use. Can be "sqlite" or "postgres" currently.
engine = "sqlite"

# Path to store the database at when using SQLite. Note that is NOT a disk path.
# This is relative to the server data directory, which is specified by --data-dir when starting the server from the command (or automatically set by SS14.Watchdog)
sqlite_dbpath = "preferences.db"

# PostgreSQL database configuration, should be self explanatory.
pg_host = "localhost"
pg_port = 5432
pg_database = "ss14"
pg_username = ""
pg_password = ""
```

The game server automatically does migrations when it starts up, you do not have to do them manually.

### Prometheus Metrics

SS14 supports hosting a metrics server that [Prometheus](https://prometheus.io/) can scrape, with which you can then make fancy graphs in [Grafana](https://grafana.com/) or such. You can find our Grafana dashboards [here](../../community/infrastructure-reference/grafana-dashboards.md), in case they happen to be useful.

To configure this, you can use the following config variables:

```toml
[metrics]
enabled = true
# Address to bind the metrics server to, use "*" for all local interfaces
host = "localhost"
# Port to bind the metrics server to
port = 44880
```

You can then scrape this with the following Prometheus config (for example):

```yml
global:
  scrape_interval: 1s
  evaluation_interval: 1s

scrape_configs:
  - job_name: "wizards_den_us_west"
    static_configs:
      - targets: ["localhost:44880"]
```

### Loki Logging

SS14 also supports pushing structured log data to [Loki](https://grafana.com/oss/loki/). Because this is modern DevOps crap the website doesn't say what it actually does but when combined with Grafana you can go and look at and filter logs in a debatably more sane way than bare text files.

No, you do not need Promtail set up for this to work. SS14 pushes directly to Loki.

To configure this, you can use the following config variables:

```toml
[loki]
enabled = true
# HTTP address of the Loki server.
address = "http://localhost:3100"
# Name of this server, gets included in all log messages.
name = "wizards_den_us_west"
# Parameters for HTTP Basic authentication, if you have Loki configured behind it.
# If left out, no authentication will be attempted.
# username = ""
# password = ""
```

## Troubleshooting

### Unable to advertise to hub / people cannot connect

People aren't able to connect to your server OR you get the following error in your server console:

```
[ERRO] hub: Error status while advertising server: [UnprocessableEntity] "Unable to contact status address"
```

This means your server is not accessible from the outside internet. Make sure you have followed the guide to [Port Forwarding](../../server-hosting/port-forwarding.md).

### SS14.Watchdog

#### Server keeps restarting every 30 seconds

This means the server isn't communicating with the watchdog correctly and the watchdog is forced to assume that the server is locked up or similar. This happens if `BaseUrl` in the watchdog configuration is set incorrectly or otherwise inaccessible by the game server.

#### `System.IO.FileNotFoundException: Could not load file or assembly 'Mono.Posix.NETStandard, Version=1.0.0.0, Culture=neutral` (...)

Current working theory is that this is caused by improper `dotnet publish` settings.
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

### Running the server on MacOS or Linux

Open a terminal in the unzipped build directory (it should have the Robust.Server file in it.)
Type `./Robust.Server` then hit enter. If you see a bunch of stuff being printed to the screen and it doesn't say error, then the server is running.

### Additional Troubleshooting

[Troubleshooting](../tips/troubleshooting-faq.md#server)

## Useful Links

All of the important links on this page in one convenient place.

- [Configuration File Reference](../tips/config-file-reference.md)
- [.NET 8 Runtime](https://dotnet.microsoft.com/download) (Also included in full .NET 8 SDK)
- [ASP.NET Core 8 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) (Also included in full .NET 8 SDK)
- [SS14.Watchdog](https://github.com/space-wizards/SS14.Watchdog/)
- [Official Builds](https://central.spacestation14.io/builds/wizards/builds.html)
- [Wizard's Den Infrastructure Reference](../../community/infrastructure-reference/wizards-den-infrastructure.md) (server specs)
- [Public Hub Server Rules](../../community/space-wizards-hub-rules.md)
