# Content Manifests

For various technical reasons, some data about your game is useful before the engine has loaded your code, or even started at all. This data can be specified in the `/manifest.yml` file at the root of your resources.

The current things that can be specified in the file are as such:

* `modules`: List of [engine modules](./robust-modules.md) to load. 
* `assemblyPrefix`: Name prefix of valid content assembly files to load. Must still be in the `/Assemblies/` directory in the VFS.
* `windowIconSet`: Directory that contains a set of window icons to load. Multiple should be provided for various sizes.
* `splashLogo`: Logo image to show in the window while the engine is loading.
* `defaultWindowTitle`: Default window title to show.
* `multiWindow`: Boolean for whether the game expects to be using multiple OS windows (through `OSWindow` etc). This flag (currently) disables the Steam Overlay to avoid any compatibility issues, as it's known to cause graphical issues and crashes with multiple OS windows active.
* `clientAssemblies`: List of assembly names (`Content.Client`, `Content.Shared`, ...) that will be loaded by the client from `/Assemblies/`. If not given, all assembly files in `/Assemblies/` are loaded.

## Complete Example

Taken from OpenDream at the time of writing, uses a lot of keys: 
```yml
modules:
- Robust.Client.WebView
assemblyPrefix: OpenDream
windowIconSet: /OpenDream/Logo/icon
splashLogo: /OpenDream/Logo/logo.png
defaultWindowTitle: OpenDream
multiWindow: true
```