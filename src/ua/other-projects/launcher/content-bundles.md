# Content Bundles

```admonish warning
In progress, not final yet
```

The launcher has the ability to directly launch "content bundles" without connecting to a server. Content bundles are self-contained zip files that contain content that will be loaded by the game client. Content bundles also have the ability to base themselves off a regular content version downloaded, in which case those assets will be downloaded and mounted first.

The original use case for content bundles is replays in Space Station 14. The bundle contains the replay data, along with the necessary metadata to make the launcher download the appropriate game version to load it with. This facilitates distributing replays as a simple zip files that can be easily dropped into the launcher by admins or players.

Content bundles are a general-purpose system, so they may also be useful for distributing other things.

## Format

Content bundles are regular zip files. [You know the ones](https://en.wikipedia.org/wiki/ZIP_(file_format)).

The contents of the zip file are directly mounted at the root of the game's VFS. `/foo.txt` will be accessible as `/foo.txt` by the game.

If a base build is specified (see below), the content for the base build will be downloaded and loaded as well with the content bundle. Such base build content has priority over the content bundle, so it is not possible to replace files in the base build.

A special file `/rt_content_bundle.json` is interpreted by the game to get out some basic metadata necessary for the operation, such as the engine version to load. 

### `rt_content_bundle.json`

Here's the JSON data that can be in the `rt_content_bundle.json`:

```json
// JSON comments aren't accepted by the launcher, they're just for helping document it.
{
  // Required: the version of the engine to use.
  "engine_version": "0.124.0.0",
  // Optional: remote build to download as a base.
  // If not specified, no remote build is downloaded.
  "base_build": {
    // These properties are basically equivalent to what's returned via the server's HTTP /info API.
    "fork_id": "wizards",
    "version": "2f6d909e443ecb501b916b69a2996acb351cc216",
    "download_url": "https://cdn.centcomm.spacestation14.com/builds/wizards/builds/2f6d909e443ecb501b916b69a2996acb351cc216/SS14.Client.zip",
    "hash": "a306c7b16b6bca9d7bd56a017c6fb50ba6205bd9f58b40752fe9ed9bd21ed195",
    "manifest_download_url": "https://cdn.centcomm.spacestation14.com/cdn/version/2f6d909e443ecb501b916b69a2996acb351cc216/download",
    "manifest_url": "https://cdn.centcomm.spacestation14.com/cdn/version/2f6d909e443ecb501b916b69a2996acb351cc216/manifest",
    "manifest_hash": "1657E0BD25D640946453E11F1B7E95D5FAF5B4E1087330D0692BAB2EFD1E6F00"
  }
}
```

## Side-loading security

Content bundles theoretically make it pretty damn easy to side-load cheats into the game along with the rest of the official server content. You could theoretically make a content bundle that simply contains extra cheat code in `/Assemblies/` and otherwise just loads the latest version of whatever server you're connecting to.

To mitigate this, [Content Manifests](../../robust-toolbox/content-manifests.md) allow limiting the list of assemblies that will be loaded from `/Assemblies/` via the `clientAssemblies` property. Since content bundles are always loaded *after* the game contents, they cannot replace any files and servers can limit the assemblies loaded to the ones they provide.

## Authentication

Content bundles run with authentication **disabled**. The launcher will not give the client an authentication token, so therefore it's impossible to connect to authenticated servers with a content bundle (for whatever you were gonna try..?)

(Yes I know I just wrote the whole section about side-loading up there. I changed my mind and don't want to delete it. Reee)