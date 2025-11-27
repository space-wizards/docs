# Automatic Client Zip (ACZ)

**Automatic Client Zip (ACZ)** is the system that allows the game server to serve game files itself. This makes it possible for the launcher to directly connect to a game server with zero extra infrastructure for asset downloading.

ACZ's core functionality is the ability to serve game assets with the [Delta Updates](../other-projects/launcher/delta-updates-and-manifests.md) system. There are three ways in which ACZ can load the client assets to serve:

* "Magic" ACZ: client files are read directly from a development environment.
* "Hybrid" ACZ: client files are read from a bundled zip file created when the server build is packaged.
* "Full Hybrid" ACZ: client files are served as in Hybrid ACZ, but content can add additional files at server startup.

All versions of ACZ are built on the [Asset Packaging](./asset-packaging.md) system. Some familiarity is recommended.

## Magic ACZ

Magic ACZ is intended for development environments. It scrounges around your development environment to load game resources and the client assemblies. The same core packaging logic is used as when packaging game client files for full publishes.

Magic ACZ can be extended by replacing the default implementation used to package the files. This can be done by calling `IStatusHost.SetMagicAczProvider()`. You can look at the code for `DefaultMagicAczProvider` to see what the default implementation does.

Magic ACZ is automatically used if no `Content.Client.zip` is found next to the server executable. If there is, Hybrid ACZ is used instead, see below.

## Hybrid ACZ

Under Hybrid ACZ, the game server loads the game files from a `Content.Client.zip` file that is placed next to the executable. This file is intended to be bundled with the server during packaging.

Hybrid ACZ can be extended with Full Hybrid ACZ, see below.

## Full Hybrid ACZ

Full Hybrid ACZ gives you the ability to add additional files on top of Hybrid ACZ.

```admonish example
OpenDream uses Full Hybrid ACZ. Base engine client files are bundled in `Content.Client.zip`, while resource files from the loaded codebase are added on top after startup.
```

Use `IStatusHost.SetFullHybridAczProvider()` to use Full Hybrid ACZ. Note that Full Hybrid ACZ is only used if a `Content.Client.zip` is detected, otherwise Magic ACZ is still used. Both types of providers can be set at once.

