# Server Hosting Tutorial

Hosting a local sandbox server for playing around is easy, but setting up a large production server supporting hundreds of players is a bit harder. This guide is organized into "levels" corresponding to difficulty.

## Level 0: Local Sandbox Server

```admonish danger title="DO NOT MODIFY THE RESOURCES FOLDER IN PRE-PACKAGED SERVER BUILDS"
Really don't, it wont work. Attempting to do so anyway will **void your support**.
The only modifications you can do to a packaged server build is with the ``server_config.toml`` file.
If you wish to modify your server to add your own content. You will need a [proper development environment](./setting-up-a-development-environment.md) with your changes and then [package your own custom build.](#level-2-server-with-custom-code).
```

1. Download and install the [.NET 8 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/8.0). You only need "x64" under "run console apps" not "hosting bundle" from the downloads page.
2. Download the latest version of the server from [our builds page](https://wizards.cdn.spacestation14.com/fork/wizards), for your operating system. If you are looking for another fork, ask that fork if they have a server builds page. Otherwise refer to the [Custom Code](#level-2-server-with-custom-code) section below.
3. Extract that to a directory somewhere.
4. Run `run_server.bat` (Windows) or `Robust.Server` [via terminal on macOS/Linux](#running-the-server-on-macos-or-linux))
5. Open your Space Station 14 Launcher and click on ``Direct Connect To Server`` and type in ``localhost`` and click connect. You can also add it as a favorite if you click the ``Add Favorite`` button.
6. When there is a new update. Go back to the second step, and copy over the ``data`` folder and ``server_config.toml``if you modified it.

If you prefer video guides, [here is one](https://youtu.be/IDBqrAGZ3cA)!

## Level 1: Invite Your Friends

You will need to do some extra steps if you want other people to be able to connect and play.

### Port Forwarding

The server needs network ports to be forwarded so that people can connect. By default, the game server uses two ports:
* UDP `1212` is used for main game netcode. This is necessary for the *client* to be able to connect to the server. This can be configured with the `net.port` configuration variable.
* TCP `1212` is a HTTP status API. This is also necessary for the *launcher* to be able to connect to the server. You do not need this to connect with a bare client. This can be configured with the `status.bind` configuration variable (which takes in a string like `*:1212` or `127.0.0.1:3000`).

For more information about how to forward your ports, see: [Port Forwarding](../../server-hosting/port-forwarding.md)

After you have port forwarded, you can use [this site](https://www.whatismyip.com/) to retrieve your public IP address. If you have both an IPV4 and IPV6 try both if one fails.

Give this to your friends and tell them to direct connect to it. If port forwarding was done correctly they should be able to connect.

```admonish info
If have an IPV6 address (looks kinda like this ``fd11:5ee:bad:c0de::ab3:3d03``) make sure to include square brackets (``[fd11:5ee:bad:c0de::ab3:3d03]``) when in the direct connect menu.
```

### Configure Your Server

You can configure settings in the server by editing the config file, `server_config.toml`. The config file is TOML which is basically INI ~~except better specified, somewhat more powerful, easier to misuse, and more annoyingly opinionated (comments NEED their own line)~~.

Settings have one key they fall under and then the name. So if I say `game.lobbyenabled` it goes under the `[game]` header like so:
```toml
[game]
lobbyenabled = true
```

Got that? Good.

**Some sane defaults you might want to set for your server if you actually intend to host this properly:**

```admonish warning
Please read through the comments here so you have a solid grasp of what you're doing.
```

```toml
[net]
# Reducing tickrate to 30 is basically unnoticeable
# but reduces server, client and network load dramatically.
tickrate = 30

[game]
# Changes the name of the server as it appears in the lobby and launcher.
hostname = "Foo Station"
# Enables the lobby instead of straight up throwing clients into a game.
lobbyenabled = true

[auth]
# Enforces authentication so that ALL connecting clients must have a proper account.
# Otherwise, guest logins are allowed.
# Possible values here are: 0 (optional), 1 (required), 2 (disabled)
mode = 1
```

See [Config File Reference](../tips/config-file-reference.md) for a somewhat more thorough guide on server configuration.

### Admin Privileges

By default, no admin privileges are set. A privileged administrator can give out permissions to other admins with the `permissions` console command in-game, but that has a chicken-and-egg problem. To get initial `+HOST` administrator permissions to your server, you can use one of the following three methods:

```admonish danger
`+HOST` privileges are **extremely dangerous** to give and should only be given to people who already have access to your computer or server.

**Giving somebody `+HOST` allows them to completely take over your server and/or computer.** 
```

* If you connect to the game server over localhost (IP `127.0.0.1` or `::1`), the game will automatically give you full host privileges. This can be disabled with the `console.loginlocal` CVar.
* If you set the `console.login_host_user` CVar to your user name, you will be given host when you connect.
* You can use `promotehost` command from the server console (e.g. `promotehost PJB`) to temporarily give a connected client host.


## Level 2: Server With Custom Code
You need to [set up a development environment](./setting-up-a-development-environment.md) in order to produce a server build for custom code. After you do that, you need to generate the server build by running:

You first build the packaging tool using:

`dotnet build Content.Packaging --configuration Release`

Then you can use Content.Packaging to do the hard work. The command below will package the server using hybrid-acz (so that the launcher can download your custom content) for linux systems. If you wanna do for Windows instead replace ``linux-x64`` to ``win-x64``

`dotnet run --project Content.Packaging server --hybrid-acz --platform linux-x64`

```admonish info
Note that if you are running an older server before Content packaging was a thing, or need to use the legacy script (not supported anymore) then use this instead
`python Tools/package_server_build.py --hybrid-acz`
```

Check the `release/` folder for a packaged server for your custom codebase.


## Level 3: A "Production" Server

This will not, of course, handle automatic restarts (in case of a crash) or updates like the watchdog would. This also won't list your server publicly on the hub as advertising defaults to off. If you wish to have your server listed on the hub please read `Bare Server Configuration` below.

For other services such as `SS14.Watchdog` you ALSO need the [ASP .NET Core 8 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) (included in .NET 8 SDK).

### Setting Rules
By default, the server ships with no rules. To set custom rules for your own server:

1. Fork the project if you have not already (which means also [setting up development environment](./setting-up-a-development-environment.md))
2. Add a guidebook file with your rules in the `Resources/ServerInfo/Guidebook/ServerRules` directory. Follow the format of `DefaultRules.xml`
3. Add a guidebook prototype entry in `Resources/Prototypes/Guidebook/rules.yml`. Pointing to the newly created guidebook text file file you made.
4. Set the `server.rules_file` CCVar to the ID you set in the guidebook prototype you made in the previous step.

### Public Hub Server - Getting your server on the launcher's list

1. Read  the [hub server rules](../../community/space-wizards-hub-rules.md) before putting your server on the hub. Advertising to the hub constitutes acceptance of the hub rules.

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
If you get an error attempting to advertise please read [the troubleshooting bellow](#Troubleshooting)

### Bare Server Build Configuration

If you *do* want to set up a more permanent server, you will have to re-host the client downloads somewhere. Anywhere accessible via a plain URL is fine.

You will want to edit the server config file (`server_config.toml`) to add the following to it:

```toml
[build]
# Download locations of the entire client build in a zip, as a HTTP (or HTTPS) URL.
download_url = ""
```

### Performance Tweaks

Here are some settings you probably want to enable on your server to improve performance:

Environment variable to enable full dynamic PGO, which drastically improves performance at the cost of marginally higher startup time:
```
DOTNET_TieredPGO: 1
DOTNET_TC_QuickJitForLoops: 1
DOTNET_ReadyToRun: 0
```

Environment variable to enable AVX operations across the codebase. Depending on your processor, this might hurt performance instead of improving it, otherwise it may improve atmos performance.
```
ROBUST_NUMERICS_AVX: true
```

You can set environment variables from the watchdog, see below.

## Level 4: Production Watchdog Server

This is for people running their own codebase and server and/or those who want a more robust hosting solution.

[`SS14.Watchdog`](https://github.com/space-wizards/SS14.Watchdog/) (codename Ian) is our server-hosting wrapper thing, similar to TGS for BYOND (but much simpler for the time being). It handles auto updates, monitoring, automatic restarts, and administration. We recommend you use this for proper deployments.

### Installation
[`Refer to this`](https://docs.spacestation14.com/en/server-hosting/setting-up-ss14-watchdog.html) for instructions on building and configuring Watchdog.

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

Note that `SS14.Watchdog` specifies *most* of it for you if you have configured it with auto updates (depending on update provider). It notably cannot provide `engine_version` or `fork_id` version, so you're best off specifying the former in build.json (your build system should be non garbage for this) and the latter in a config file.

## Level 5: Big Production Server
Things that aren't necessary for small/private servers, but strongly recommended for forks or larger production servers.

### Advanced Port Forwarding

You can slap the HTTP status API behind a reverse proxy if you want. This is recommended for production servers since then you can do HTTPS (slap it behind nginx and turn on HTTPS). Note that if you do this you have to set the `status.connectaddress` config variable to specify the UDP address the main netcode should connect to. This has to look like this: `udp://server.spacestation14.io:1212` (for our server, obviously substitute with your params). 


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
* [Config Reference](../tips/config-file-reference.md)
* [.NET 8 Runtime](https://dotnet.microsoft.com/download) (Also included in full .NET 8 SDK)
* [ASP.NET Core 8 Runtime](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) (Also included in full .NET 8 SDK)
* [SS14.Watchdog](https://github.com/space-wizards/SS14.Watchdog/)
* [Official Builds](https://central.spacestation14.io/builds/wizards/builds.html)
* [Wizard's Den Infrastructure Reference](../../community/infrastructure-reference/wizards-den-infrastructure.md) (server specs)
* [Public Hub Server Rules](../../community/space-wizards-hub-rules.md)
* [Port Forwarding](../../server-hosting/port-forwarding.md)
