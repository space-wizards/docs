# Server Replay Recording

The game server can automatically record a full replay of every round played. Replays are output as single zip files that can be loaded by the game and launcher.

## Server Configuration

### Build Configuration

Your server muts have a full build configuration/CDN (not just ACZ) configured. Otherwise, old replays will cease to work as the game cannot be downloaded by the launcher anymore.

### Replay CVars

You will want to set the following CVars:

`replay.auto_record`: Set this to true to enable the system!

`replay.max_compressed_size`: The approximate maximum size of a replay before recording gets automatically stopped, in kilobytes. It defaults to 256 MB, but you may want to raise this a bit depending on your expectations.

`replay.directory`: The directory in the server's data in which replays are saved. Defaults to `replays/`.

`replay.auto_record_name`: The file name in the replays directory that replays will be saved to. Defaults to `{year}_{month}_{day}-{hour}_{minute}-round_{round}.zip`, the values between braces automatically substituted when the recording starts.

`replay.auto_record_temp_dir` Temporary directory that replays reside in while being recorded. When the recording is done (at the end of the round) the file will be moved to the final location in `replay.auto_record_name`. Defaults to an empty value, which disables this part of the system (replays will be written directly to their final location).

Those are all the CVars you need to set it up. Your replays folder will get a bunch of zip files. You can put these zip files on a static file server and it should™️ work. Be warned that if you do use a static file server, you may want to use `replay.auto_record_temp_dir` to avoid the replays being downloadable while the round is being played live.

## Wizard's Den Configuration

This will be an overview of how we set up this system on Wizard's Den game servers. You may use this as inspiration or you may disregard it entirely.

For starters, we don't want to store replays on the game server boxes themselves. We have a large amount of storage on our central server (centcomm), so keep them there. Also in the interest of robustness, game servers do not have the ability to delete replays once they are done.

At a high level, we export an NFS share from our central server that the game servers write into. When the recording is done, the game server moves it into another directory on the NFS share, and a script on the server moves the replays into their final position (accessible by nginx, inaccessible by the game server)

The (storage) folder structure looks like this:

```
/hdd/replays
├── permanent
│   └── lizard
│       └── 2023
│           ├── 07
│           │   └── 20
│           │       └── lizard-2023_07_20-01_09-round_12345.zip
│           └── 08
│               └── 20
│                   └── lizard-2023_08_20-01_09-round_12345.zip
└── temp
    ├── done
    └── recording
```

The NFS export looks like this on centcomm (using bind mounts to export the folder):

```
/nfs/ss14_server/replays
├── done
└── recording
```

On the game servers, that's mounted as `/nfs/replays`. We symlink `data/replays` in the game server instances TO `/nfs/replays`, so the game server will write there instead. We have `replay.auto_record_temp_dir` set to `"recording"` and `replay.auto_record_name` set to `"done/lizard-{year}_{month}_{day}-{hour}_{minute}-round_{round}.zip"` (server name prefix configured differently per server).

The replays are already on the server when writing stops, so when the game server renames the files to the final position it'll be pretty quick (compared to if it had to copy from local disk before renaming).

This setup will get you replays in the `done/` folder, but that still keeps them accessible to the game servers afterwards. As a bit more isolation, we use a **systemd path unit** to run a script when a file is moved into the `done/` folder, and move it again into its final place at `permanent/`.

The systemd units and Python script involved are pretty simple, and look like this:

```ini
# ss14-transfer-replays.path
[Unit]
Description=Detect new finished replay files.
After=hdd-replays-temp.mount hdd-replays-permanent.mount
Requires=hdd-replays-temp.mount hdd-replays-permanent.mount

[Path]
PathExistsGlob=/hdd/replays/temp/done/*.zip

[Install]
WantedBy=paths.target
```

```ini
# ss14-transfer-replays.service
[Unit]
Description=Transfer SS14 game replays into final location.

[Service]
Environment=PYTHONUNBUFFERED=1
ExecStart=/opt/transfer_replays.py
User=ss14_server
Group=ss14_server
```

```py
#!/usr/bin/env python3
# /opt/transfer_replays.py

import os
import os.path
import re
import shutil

SOURCE_DIR = "/hdd/replays/temp/done/"
DEST_DIR   = "/hdd/replays/permanent/"

REPLAY_FILE_NAME_RE = re.compile(r"([^-]+)-(\d{4})_(\d{2})_(\d{2})-\d{2}_\d{2}-round_\d+\.zip")

def main():
    for file in os.listdir(SOURCE_DIR):
        src_replay = os.path.join(SOURCE_DIR, file)
        final_rel_path = calculate_final_replay_path(file)
        final_path = os.path.join(DEST_DIR, final_rel_path)

        dir = os.path.dirname(final_path)
        os.makedirs(dir, exist_ok=True)
        print(f"{src_replay} -> {final_path}")
        shutil.move(src_replay, final_path)


def calculate_final_replay_path(name: str) -> str:
    """
    Takes in a replay name like "lizard-2023_07_20-01_09-round_12345.zip"
    Returns the relative path to move it to, like
    "lizard/2023/07/20/01/09/lizard-2023_07_20-01_09-round_12345.zip"
    """

    match = REPLAY_FILE_NAME_RE.match(name)
    if not match:
        # Can't let files like these just sit, because then this script would keep spinning. Move em to a lost+found.
        print(f"Warning: unable to parse file name '{name}'. Moving to lost+found")
        return f"lost+found/{name}"

    server = match.group(1)
    year = match.group(2)
    month = match.group(3)
    day = match.group(4)

    return f"{server}/{year}/{month}/{day}/{name}"

if __name__ == "__main__":
    main()
```

Then finally we just have some nginx configuration to serve the static files.