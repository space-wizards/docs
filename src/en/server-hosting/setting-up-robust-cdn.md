# Setting up Robust.Cdn

[Robust.Cdn](https://github.com/space-wizards/Robust.Cdn/) is the dedicated server for providing manifest-based delta updates without server ACZ. 

The TL;DR of how `Robust.Cdn` operates is that it ingests directories of client zip files whenever you push a new build, then generates manifests and exposes the manifest and endpoint to do delta downloads. The games files are cached in an SQLite DB similar to how the launcher stores it.

## Prerequisites

You will need the ASP.NET Core 6 runtime installed.

## Building

Clone the code, then compile it with `dotnet publish -c Release -r linux-x64 --no-self-contained` The files will be dropped in `Robust.Cdn/bin/Release/net6.0/linux-x64/publish`. `Robust.Cdn` is the executable to run, but obviously copy everything else too.

## Server File Layout

You're going to want to put the server files somewhere on your uhhh, server. We put them at `/opt/robust_cdn`, with the following directory structure:

```
/opt/robust_cdn/
├── appsettings.json
├── run.sh
├── bin
│   ├── Robust.Cdn
│   ├── Robust.Cdn.dll
		.
```

The `run.sh` looks like this by the way, yes it's just that simple:

```bash
#!/bin/sh

exec bin/Robust.Cdn
```

The actual program files go in a subfolder, and we run it from the parent directory so you don't bulldoze the config files with updates or something.

## Configuration

The configuration file is `appsettings.json` in the current working directory you run the server program from. You need to change at least two configuration settings: the disk path of your game versions, and the update token to trigger updates. Maybe port too.

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  // change port for the server to bind to here
  "Urls": "http://localhost:27690/",
  "Cdn": {
    // See https://github.com/space-wizards/Robust.Cdn/blob/master/Robust.Cdn/CdnOptions.cs for all options.
    // Yes you can have comments in here by the way.
    // Change this update token so people don't uh... spam update checks on your server.
    "UpdateToken": "change this",
    // Increase this to reduce bandwidth usage for large downloads. Higher numbers need more CPU.
    "StreamCompressLevel": 5,
    // The file path of the SQLite database used by the server.
    // You can change this to put it on another drive or something if you want.
    // Personally we put it on our server's HDD instead of the SSD, but that's up to you.
    "DatabaseFileName": "content.db",
    // The directory path containing the versioned client builds to load and serve. 
    // See below for explanation
    "VersionDiskPath": "/var/lib/wizards-builds/builds"
  }
}
```

### Version disk

`Robust.Cdn` needs a directory containing builds to load, with the following layout:

```
/var/lib/wizards-builds/builds
├── 02030cfa0ed6511ec5527c5b7d1f8bcd46fe1435
│   ├── SS14.Client.zip
│   ├── SS14.Server_linux-arm64.zip
│   ├── SS14.Server_linux-x64.zip
│   ├── SS14.Server_osx-x64.zip
│   └── SS14.Server_win-x64.zip
├── 021d39be2876f991c5fd6e663760a921d29ac694
│   ├── SS14.Client.zip
│   ├── SS14.Server_linux-arm64.zip
```

It will look for `SS14.Client.zip` (configurable) in each subdirectory to the directory to specify. The subdirectory's name is the "version" of content. (Note: these are hashes because we use the Git commit hash as version "number". They are not tied to manifest or zip hashes in any way, and can be any string, really).

### Automatic detection of new versions

You can use something like the following to trigger `Robust.Cdn` to scan for new versions in the version directory:

```bash
curl -X POST -d "" -H 'Authorization: Bearer <token from the config file, change this>' "http://localhost:27690/control/update"
```

### API endpoints / build metadata

`Robust.Cdn` exposes the `/version/{version}/manifest` and `/version/{version}/download` endpoints that do the actual updating. These need to be specified in the `build.json` in your server files, which you probably want to just specify by modifying `gen_build_info.py` or something. The new metadata required is as follows:

```json
// (example from Wizard's Den servers)
// Robust.Cdn is available at /cdn and nginx serves static builds on /builds
{
    "download": "https://cdn.centcomm.spacestation14.com/builds/wizards/builds/{FORK_VERSION}/SS14.Client.zip",
    "hash": "49a7f54eb7e848c0a438bcfd3a198454d862e7d58d3e11c7ce60e281ddbd205d",
    "version": "e769ad27256300cfbbf10d641930d43990bff309",
    "fork_id": "wizards",
    "engine_version": "0.12.1.0",
    // These ones are new
    "manifest_url": "https://cdn.centcomm.spacestation14.com/cdn/version/{FORK_VERSION}/manifest",
    "manifest_download_url": "https://cdn.centcomm.spacestation14.com/cdn/version/{FORK_VERSION}/download",
    "manifest_hash": "8B175E9D944F54C1444E93E19C39EB255353392B316118B660F21DF68D56DC2D"
}
```

```admonish info
Note the ability to specify `{FORK_VERSION}` in the `build.json` file. This gets replaced by `version` from the JSON at runtime. This way the URL does not need to duplicate the version string, and the URL template can be changed via CVar while the entry in `build.json` stays the same. Other possible keys are `{FORK_ID}`, `{MANIFEST_HASH}` and `{ZIP_HASH}`. 
```

* `manifest_url` is the `/manifest` endpoint on `Robust.Cdn`. The version must be included in the URL for `Robust.Cdn` to work. 
* `manifest_download_url` is the `/download` endpoint. Same rules as above.
* `manifest_hash` must be the [manifest hash](../other-projects/launcher/delta-updates-and-manifests.md). This hash is automatically generated by `gen_build_info.py` now and should just work.

## Systemd Unit

We personally use systemd to start the server:

```ini
[Unit]
Description=Robust.Cdn

[Service]
Type=notify
WorkingDirectory=/opt/robust_cdn/
ExecStart=/opt/robust_cdn/run.sh
User=robust_cdn
Group=robust_cdn

[Install]
WantedBy=multi-user.target
```

