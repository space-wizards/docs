# Robust Modules

Robust modules are optional modules that games can request to load. These modules are separate from the main engine download because they are too bloody huge. They are still all first-party, just not bundled with Robust by default.

## Using modules

To specify which modules your game needs, you need to specify the list in your [content manifest](./content-manifests.md) file like so:

```yml
modules:
- Robust.Client.WebView
```

The launcher will automatically detect the presence of these modules in the manifest file, and make sure they are installed and available.

## Available modules list

### Robust.Client.WebView

Implements support for rendering web content such as HTML pages in windows and UI controls. We really do not recommend you touch this with a 10 foot pole for game UI in new games, it was created to allow OpenDream to run SS13's HTML-based interfaces.

Currently, [Chromium Embedded Framework](https://en.wikipedia.org/wiki/Chromium_Embedded_Framework) is used as implementation for this, but this may be subject to change in the future if we ever explore better alternatives.

This can take more than a hundred megabytes of disk space to install because of how huge CEF is. God have mercy.

## Module Versions

Because of the aforementioned problem that *modules are huge*, we do not release new modules for every single Robust version. Instead the Launcher picks the newest module version available (module version numbers match engine versions) that is *older or equal to* the current Robust version.