# Setting up Robust.Cdn

[Robust.Cdn](https://github.com/space-wizards/Robust.Cdn/) is a dedicated server for hosting and serving game build files for Space Station 14 servers. It covers both management of game server builds as well as client delta downloads, and is recommended for any serious permanent server host.

```admonish warning
This page assumes a decent amount of pre-existing experience with various Linux sysadmin concepts. And don't blindly copy paste shit. I don't have the time or energy to baby proof this guide, so you'll need to properly read and understand everything listed here.
```

## Overview

The standard publishing workflow for Space Station 14 looks like so:

1. Builds are periodically created by a CI system like GitHub Actions.
2. Build files (client and server zips) are sent to a central server. Server builds get indexed and configuration injected for client CDN, client files are ingested so they can be downloaded by the launcher.
3. Game servers (via SS14.Watchdog) get notified of update, and automatically download new server builds from central server.
4. Injected game server configuration is used to inform clients where they can download files.

Robust.Cdn is the glue that wires most of this together:

* Receiving new builds directly from GitHub Actions.
* Serving game server builds for access by game servers (watchdog).
* Automatically notifying watchdogs of the new update.
* Providing client delta downloads.

## Concepts

Robust.Cdn currently serves two core functions:

* Managing server manifests
* Managing client delta downloads

The **server manifest** is effectively the list of available game server versions. This is used by the watchdog to download new server updates.

The **client delta downloads** or "**client CDN**" is used by game clients to download new files on update, downloading only what is necessary.

```admonish info
It is possible to run Robust.Cdn without making use of the server manifest support. In fact before 2.0, Robust.Cdn only did client CDN. See the rest of the documentation for details.
```

A **fork** is a single "stream of development" of the game. For example, Space Station 14 upstream (Wizard's Den) and Rouny's Marine Corps would be considered two different forks. Robust.Cdn can manage multiple forks at once, independently.

A **version** or **build** is just a single version of the game on a fork. It is always the intent that the most recent version is used by servers, but Robust.Cdn serves older versions as well.

## Installation

We provide official container images of Robust.Cdn via GitHub Container Registry. Otherwise, we also have instructions for manually publishing the project via the .NET SDK.

### Container image

The latest stable image of Robust.Cdn is `ghcr.io/space-wizards/robust.cdn:2`. Information about the container:

* Listens on port 8080
* Default UID/GID is 1654
* Important volumes to mount:
  * `/app/appsettings.json`: primary config file.
  * `/builds`: contains server/client build zip files.
  * `/manifest`: contains SQLite database for server manifest operations.
  * `/database`: contains SQLite database for client content downloads.

Here is an example ``docker-compose.yml``, please modify it to your needs.

```
services:
  robust_cdn:
    image: ghcr.io/space-wizards/robust.cdn:2
    container_name: robust_cdn
    user: 1654:1654
    volumes:
      - ./appsettings.json:/app/appsettings.json
      - ./builds:/builds
      - ./manifest:/manifest
      - ./database:/database
    ports:
      - 8080:8080
    restart: unless-stopped
```

### Manual compilation

If you hate containers, you can manually publish Robust.Cdn and deploy the files yourself. For this you will need Git and the .NET 8 SDK. The server that will run the build needs the matching ASP.NET Core Runtime installed, but does not need the SDK itself.

Clone the git repo, then publish:

```
git clone https://github.com/space-wizards/Robust.Cdn.git
cd Robust.Cdn
dotnet publish -c Release -r linux-x64 --no-self-contained
```

The finished build will be dropped in `Robust.Cdn/bin/Release/net8.0/linux-x64/publish`. You can copy these into some random location you fancy like `/opt` and run `Robust.Cdn` from there. For example:

```
/opt/robust_cdn/
├── appsettings.json
├── bin
│   ├── Robust.Cdn
│   ├── Robust.Cdn.dll
    .
```

The actual program files go in a subfolder, and we run it from the parent directory so you don't bulldoze the config files with updates or something.

You can then run Robust.Cdn automatically with the following systemd service definition:

```ini
# /etc/systemd/system/robust-cdn.service
[Unit]
Description=Robust.Cdn

[Service]
Type=notify
WorkingDirectory=/opt/robust_cdn/
ExecStart=/opt/robust_cdn/bin/Robust.Cdn
User=robust_cdn

[Install]
WantedBy=multi-user.target
```

```admonish warning
For the love of Miku and all that is holy, do not run the CDN from directly within the build directory. Please.
```

## Configuration

Robust.Cdn is an ASP.NET Core app, so it supports configuration both via config file and other sources such as environment variables. You can see [ASP.NET Core's documentation](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/?view=aspnetcore-8.0) for a more in-depth overview.

Most configuration of Robust.Cdn is done via the `appsettings.json` config file. Here is a complete reference of its contents:

```admonish danger
You should go over this config file in full to understand what you are setting up.
```

```json
{
  // Log level configuration, you can leave these as default.
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning",
      "Robust": "Information"
    }
  },

  // Contains configuration primarily for manifest operation,
  // but is also needed for CDN operations to configure available forks.
  "Manifest": {
    // The location on disk where builds should be stored.
    // Omit this when using official container images.
    "FileDiskPath": "/var/robust-cdn/builds",

    // Database file that contains information for server manifest functionalities.
    // Omit this when using official container images.
    "DatabaseFileName": "/var/robust-cdn/manifest.db",

    // The set of available forks Robust.Cdn should serve.
    "Forks": {
      // Configuration for a single fork. The key here is the ID of the fork, which will be used in many locations.
      // YOU SHOULD MAKE THE FORK ID COMPLETELY GLOBALLY UNIQUE TO AVOID ISSUES.
      // DON'T JUST WRITE "TEST" HERE.
      "test": {
        // A token used to publish new versions to this fork.
        // ***YOU SHOULD CHANGE THIS TO BE A NEW UNIQUE VALUE***.
        "UpdateToken": "foobar",

        // Configuration to notify SS14.Watchdog instances of new updates. Multiple can be specified.
        "NotifyWatchdogs": [
          {
            // The base address of the watchdog.
            "WatchdogUrl": "http://localhost:5000/",

            // The specific server instance on the watchdog to notify.
            "Instance": "syndicate_mothership",

            // The ApiToken specified in the watchdog config for this instance.
            "ApiToken": "Honk"
          }
        ],

        // Set to true to make this a "private" fork.
        // Private forks limit access of server builds, which is desirable for servers with secret content.
        // See below for details.
        "Private": false,

        // Username and password combinations to access server files for private forks.
        // Ignored if not a private fork.
        "PrivateUsers": {
          "foobar": "baz"
        },

        // How many days to keep around old build files.
        "PruneBuildsDays": 90,

        // Nice human readable display name of this fork.
        // This is displayed on locations such as the HTML builds page.
        "DisplayName": "Test Fork",

        // Link destination on the HTML builds page.
        "BuildsPageLink": "https://example.com",

        // Link text on the HTML builds page.
        "BuildsPageLinkText": "Test Fork LINK"
      }
    }
  },

  // Configuration primarily for client CDN.
  "Cdn": {
    // Database file that contains information for server manifest functionalities.
    // Omit this when using official container images.
    "DatabaseFileName": "/var/robust-cdn/content.db",

    // Increase this to reduce bandwidth usage for large downloads. Higher numbers need more CPU.
    "StreamCompressLevel": 5,

    // "Fallback" fork for migration functionality from Robust.Cdn 1.x.
    // This can be omitted for new installations.
    "DefaultFork": "test"
  },

  // Root URL that your Robust.Cdn server is globally accessible as.
  // This is necessary for correct generation of build metadata.
  "BaseUrl": "https://<robust-cdn-url>/",

  // The base path that Robust.Cdn is exposed under.
  // You should set this when reverse proxying Robust.Cdn behind a subpath.
  // See also further notes down below.
  "PathBase": "/",

  // Valid host names for clients to use to connect to Robust.Cdn.
  // You can just leave this as-is.
  "AllowedHosts": "*",

  // Change port for the Robust.Cdn to bind to here.
  // Omit this when using official container images.
  "Urls": "http://localhost:27690/",
}
```

## Setting up publishing

### GitHub Actions

If your fork's repository is hosted on GitHub, the easiest way to automatically publish new builds to Robust.Cdn is via the GitHub Actions configuration available in the codebase. This is how official Wizard's Den builds are published.

1. Edit `Tools/publish_multi_request.py` to modify the "configuration parameters" at the top of the script:
  * `ROBUST_CDN_URL` should be the URL at which Robust.Cdn is accessible.
  * `FORK_ID` should be the ID of the fork you configured in `appsettings.json`

2. Create an Actions secret on your GitHub repository with name `PUBLISH_TOKEN`, containing the `UpdateToken` specified for your fork in `appsettings.json`.

3. Make sure the "Publish" workflow is running, or trigger it manually.

This should be everything you need!

### Custom

For people looking to do custom publishing workflows without GitHub actions, please refer to the API reference of the "publish" endpoint.

## Watchdog configuration

Configuration SS14.Watchdog to use your new Robust.Cdn for getting builds is pretty easy. In the instance configuration, enter something like this:

```yml
UpdateType: "Manifest"
Updates:
  # Replace with your own Robust.Cdn URL and fork ID.
  ManifestUrl: "https://<robust-cdn-url>/fork/<fork>/manifest"
```

You will likely also want to set up `NotifyWatchdogs` in Robust.Cdn's fork configuration, so it notifies SS14.Watchdog when a new version is available. Check the reference up above.

## Builds HTML page

Robust.Cdn generates a simple HTML web page to allow people to manually download the latest server builds. This page is available automatically at `/fork/<fork_id>`.

For example: [Wizard's Den builds](https://wizards.cdn.spacestation14.com/fork/wizards/).

### Custom PathBase

If you can't have subdomains for some reason (seriously, you should use subdomains if you can), you will want to mount multiple services behind the same domain with a reverse proxy such as nginx. When you do this you need to set `PathBase` in the config file to make links in the HTML builds page work. Other API functionality is not affected by this.

For example, if you want to host the CDN under `https://example.com/cdn/`, you should configure it as such:

```json
"BaseUrl": "https://example.com/cdn/",
"PathBase": "/cdn/",
```

**Make sure your reverse proxy is configured correctly**: it should be passing the full path to Robust.Cdn, i.e. not cutting off the path prefix itself. If using **nginx**, this is achieved as such:

```nginx
# Note the trailing slash!
# bad
proxy_pass http://127.0.0.1:8080/;
# good
proxy_pass http://127.0.0.1:8080;
```

## Private forks

A fork can be marked as "private". This prevents Robust.Cdn from giving unauthorized people access to server builds, which is desirable for forks with secret content. Access is restricted via HTTP Basic authentication. Usernames and passwords for this can be configured in the fork configuration.

To give the watchdog access to these builds, you can configure it as such in the instance update configuration:

```yml
UpdateType: "Manifest"
Updates:
  # Replace with your own Robust.Cdn URL and fork ID.
  ManifestUrl: "https://<robust-cdn-url>/fork/<fork>/manifest"
  Authentication:
    Username: foobar
    Password: baz
```

## Builds file layout

Robust.Cdn stores and expects build zips in the `FileDiskPath` directory (`/build` when using container image). Files in this directory have a pretty simple structure of `<fork>/<version>/<file>.zip`. For example:

```
/var/robust-cdn/builds
├── wizards
│   ├── 02030cfa0ed6511ec5527c5b7d1f8bcd46fe1435
│   │   ├── SS14.Client.zip
│   │   ├── SS14.Server_linux-arm64.zip
│   │   ├── SS14.Server_linux-x64.zip
│   │   ├── SS14.Server_osx-x64.zip
│   │   └── SS14.Server_win-x64.zip
│   ├── 021d39be2876f991c5fd6e663760a921d29ac694
│   │   ├── SS14.Client.zip
│   │   ├── SS14.Server_linux-arm64.zip
```

## Example reverse proxy configs

You likely want to run Robust.Cdn behind a reverse proxy of some kind. There are a few things to make sure of:

* When using multi-request publishing, you should set the maximum client body size to fit the entire client download at once.
* When using one-shot publishing, you should set the request timeout high enough (usually more than a minute or two).

Here are some example configurations for your reverse proxy:

### Nginx

This example is intended to go into an existing `server` block of your configuration (TLS termination, server name, etc...)

```nginx
# gzip JSON responses.
gzip on;
gzip_types application/json;

location / {
    # Increased max body size for multi-request publishes. Not necessary for oneshot publishes.
    client_max_body_size 512m;

    # Do not buffer request bodies inside nginx, especially important for multi-request publishes.
    proxy_request_buffering off;
    # Disable buffering of outgoing responses.
    proxy_buffering         off;
    # Ensure request and response can be streamed via HTTP 1.1.
    proxy_http_version      1.1;
    # Increased read timeout to avoid timeouts on the publish API endpoint.
    # Not strictly necessary for multi-request publishes, but cannot hurt.
    proxy_read_timeout      120s;

    # Boilerplate reverse proxy config.
    proxy_set_header   Host $http_host;
    proxy_set_header   X-Real-IP $remote_addr;
    proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header   X-Forwarded-Proto $scheme;

    # Update port here.
    proxy_pass         http://localhost:8080;
}
```

### Caddy

This is an example Caddyfile to go into an existing block for the domain with the CDN

```
# Increased max body size for multi-request publishes.
request_body {
        max_size 512MB
}

reverse_proxy localhost:8080 {
        flush_interval -1
}

encode zstd gzip
```

## Troubleshooting

### 504 gateway timeout during publish

Increase your reverse proxy's response timeout. In nginx this is controlled via `proxy_read_timeout`.

### Connection errors during publishing (multi-request publish)

Make sure you have your reverse proxy's max body size set high enough to allow 

### 404 not found error on CDN API while publishing

Make sure you are using the latest version of Robust.Cdn. Version 2.2.0 added a new publishing mechanism that is used by the upstream infrastructure.

## Migration from Robust.Cdn 1.x

If you were hosting an existing installation of Robust.Cdn from before multi-fork/server manifest support was added (1.0), this part of the guide will help you migrate.

As part of multi-fork and manifest support, the following changes will need to be made to your setup, at the bare minimum:

* `Cdn.UpdateToken` in configuration has been moved to fork configuration.
* `Cdn.VersionDiskPath` has effectively been changed to `Manifest.FileDiskPath`. **Note that the file layout is different, you will need to manually move the builds one folder down to be underneath the fork folder (see above).**

Robust.Cdn will automatically migrate your existing CDN content database so that all version information stored within gets assigned a fork. You must set `Cdn.DefaultFork` in the configuration so it knows what fork to assign these versions to. Existing URLs (for replays etc) will keep working after this, as configuring `Cdn.DefaultFork` will make the CDN internally map the old `/version/{version}/*` URLs to the new ones under the specified fork.

After making the above changes, newer Robust.Cdn can still be used with the old publishing workflow (using `gen_build_info.py` and all the other scripts). Just make sure to account for the change in file structure and such. Obviously we recommend moving to the new built-in publishing system as soon as possible, however.

### Ingesting existing server manifest contents

You can manually ingest your existing server manifest into the manifest database with the following Python script. Note that this is only really necessary if you care about being able to easily access old server versions via the HTML page or such, skipping this step

This is very janky and you'll need to publish at least one build normally for the JSON server manifest to be re-cached and become available. But hey, it works. If the script doesn't work because you don't have `dateutil` available, on Python 3.10+ you can remove the dateutil code by replacing `dateparser.parse` with `datetime.fromisoformat`.

```py
#!/usr/bin/env python3

import sqlite3
import json
import re

from datetime import datetime, timezone
from dateutil import parser as dateparser

JSON_FILE = "manifest.json"
DB_FILE = "manifest.db"
FORK_NAME = "wizards"

def main():
    data = json.loads(open(JSON_FILE, "r").read())
    db = sqlite3.connect(DB_FILE)
    cur = db.cursor()

    cur.execute("SELECT Id FROM Fork WHERE Name = ?", (FORK_NAME,))
    fork_id = cur.fetchone()[0]

    for name, build in data["builds"].items():
        time = dateparser.parse(build["time"])
        time = time.astimezone(timezone.utc)

        cur.execute(
            "INSERT INTO ForkVersion (Name, ForkId, PublishedTime, ClientFileName, ClientSha256, Available, EngineVersion) VALUES (?, ?, ?, ?, ?, TRUE, '')",
            (name, fork_id, time, file_name(build["client"]["url"]), bytes.fromhex(build["client"]["sha256"])))
        version_id = cur.lastrowid

        for rid, server in build["server"].items():
            cur.execute(
                "INSERT INTO ForkVersionServerBuild (ForkVersionId, Platform, FileName, Sha256) VALUES (?, ?, ?, ?)",
                (version_id, rid, file_name(server["url"]), bytes.fromhex(server["sha256"])))

    db.commit()


def file_name(url: str) -> str:
    return url.split("/")[-1]

main()
```

## Robust.Cdn API reference

This part of the guide will explain all of Robust.Cdn's API endpoints that you can use and interface with.

### Authentication

Some API endpoints may require authentication:

* Fork control endpoints such as publish need `Authorization: Bearer <updateToken>`, with the `UpdateToken` specified in the fork configuration.
* Endpoints to access server files require Basic authentication if the fork is configured as private.

### Publishing

There are two separate APIs to publish: "one-shot" and "multi-request". The one-shot API is under `/fork/{fork}/publish`, while the multi-request API is under `/fork/{fork}/publish/{start,file,finish}`. We recommend the multi-request publishing API, and it is also what the official publishing scripts use.

### GET `/fork/{fork}`

Gets a nice human-readable HTML page about the last builds available.

### POST `/fork/{fork}/control/update`

Instructs the client CDN to re-scan for new files. You can manually run this when not using Robust.Cdn's server manifest support and only using the client CDN. You will need to put the files in the correct layout as specified below.

This require authentication.

### GET `/fork/{fork}/manifest`

Gets a JSON list of every server build available for a fork.

### POST `/fork/{fork}/publish`

Publishes a new version to the CDN in a single API request. This is as opposed to the "multi-request" API described below. 

It expects a JSON body with the following information:

```json
{
  "version": "<version>",
  "engineVersion": "<engine version>",
  "archive": "<builds archive URL>"
}
```

The version is the new version number you are publishing. This can be anything. Engine version is the version number of the engine to use.

The archive is must be URL to a zip that Robust.Cdn will download containing the build zip files (client and server).

This require authentication.

### POST `/fork/{fork}/publish/start`

Start a new publishing operation that involves multiple subsequent API requests. The initial JSON request body is as follows:

```json
{
  "version": "<version>",
  "engineVersion": "<engine version>"
}
```

The version is the new version number you are publishing. This can be anything. Engine version is the version number of the engine to use.

If a publish is already undergoing on under the given version number, it is aborted and you are given a clean slate.

This require authentication.

### POST `/fork/{fork}/publish/file`

Add an extra file to an in-progress publish.

The file contents are provided in the request body as `application/octet-stream`. Additional metadata should be provided in the following HTTP headers:
* `Robust-Cdn-Publish-File`: the name of the file being published. Usually this is something like `SS14.Client.zip` or `SS14.Server_win-x64.zip`.
* `Robust-Cdn-Publish-Version`: the version number being published to (provided before).

This require authentication.

### POST `/fork/{fork}/publish/finish`

Finishes publishing a new version started before.

```json
{
  "version": "<version>"
}
```

The version is the new version number you are publishing.

If the publish fails validation (for example, missing client files), the publish will be aborted and must be restarted from zero.

This require authentication.

### POST & OPTIONS `/fork/{fork}/version/{version}/download`

Client CDN download endpoint for a version. See [Delta Updates](../other-projects/launcher/delta-updates-and-manifests.md) for details.

### GET `/fork/{fork}/version/{version}/file/{file}`

Downloads a server or client build zip from a version. File is the file name.

### GET `/fork/{fork}/version/{version}/manifest`

Client CDN manifest endpoint for a version. See [Delta Updates](../other-projects/launcher/delta-updates-and-manifests.md) for details.

### POST & OPTIONS `/version/{version}/download`

Fallback endpoint that maps to the `DefaultFork`, if configured. This is for URL compatibility with old Robust.Cdn setups.

### GET `/version/{version}/manifest`

Fallback endpoint that maps to the `DefaultFork`, if configured. This is for URL compatibility with old Robust.Cdn setups.
