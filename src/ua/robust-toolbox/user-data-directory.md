# User Data Directory
The User Data Directory is used by both the client and server to store permanent mutable data. 

The user data directory can be accessed and written to by content via `IResourceManager.UserData`. It is also used by some other things, such as config file saving on the client.

## Server

The directory is chosen in this order:
1. If `--data-dir` is passed as argument to the server when starting it, like `./Robust.Server --data-dir /foo`, the passed directory is used.
2. The directory `data` next to the server executable is used.

## Client

The directory is chosen in this order:
1. If `--self-contained` is passed as argument to the client when starting it, the directory `user_data` next to the client executable is used.
2. The data directory selected as a user-global, OS-appropriate location:
    * `$UserDataDirectoryName` defaults to `Space Station 14`, but can be overriden by non-launcher Robust games by specifying `GameControllerOptions.UserDataDirectoryName`.
    * Windows: `%APPDATA%/$UserDataDirectoryName/data`.
    * macOS: `~/Library/Application Support/$UserDataDirectoryName/data`
    * Linux: `$XDG_DATA_HOME/$UserDataDirectoryName/data`, `XDG_DATA_HOME` is assumed to be `~/.local/share` if unset.

When connecting to servers on the launcher, there is currently zero storage isolation between servers. Do not store any server-confidential data in client-side userdata, as it may be accessible to any other servers.

## Integration Tests

In integration tests (both client and server), the user data dir is a fake in-memory file system supposed to roughly emulate real disk behavior. It is not persisted in any way. 




