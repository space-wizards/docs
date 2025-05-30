# Robust Station Image

The **RSI** (Robust Station Image) format is intended to be a flexible, open, and readable way <!--Insert more marketing bull that sounds good here!--> to define icons inside sprite sheets in the same vein as the BYOND `.dmi` format. An RSI is considered an "icon", and it can contain "states" which are sub sections of said master icon. These states can define custom flags, animations, and directional icons out of the box.

An RSI is a folder with a name that ends in `.rsi`, and contains a `meta.json` and one or more PNG files according to the names of states.

The image metadata (what defines states, animations, etc...) is stored in the `meta.json` file as JSON. The actual sprites are stored in sprite sheets as PNG files in the folder. Each unique state corresponds to a sprite sheet with the same name.

## JSON

The root of the JSON file contains the following values:

Key | Meaning
--- | -------
`version` | A simple integer corresponding to the RSI format version. This can be used to identify what version an RSI is and allow the implementation to correctly enable backwards compatibility modes when needed.
`size` | The dimensions of the sprites inside the RSI, stored as an associative list of `{x: ?, y: ?}`. This is _not_ the size of the PNG files that store the sprite sheet. It is used to correctly crop the individual sprites out of the sprite sheet files.
`states` | A list of _states_ that store the actual meat of the RSI, see below.
`license` | Required. A valid [SPDX License Identifier](https://spdx.org/licenses/) applying to this work.
`copyright` | Required. Other arbitrary copyright info such as name, source, ...
`load` | Special loading parameters that will change how the sprites are interpreted by the engine.
`metaAtlas` | Boolean that indicates whether the sprite is added together to a larger atlas at load. Enabled by default, this should be disabled for large, rare RSIs.

### States

A state is a container for metadata for a specific sprite sheet. They store data related to their sprite sheet like delays of animations and directions. A state has an accompanying sprite sheet.

States have one field that can be used to distinguish them:

Key | Meaning
--- | -------
`name` | The name of the state. Can only contain lowercase alphabetic, numerical, and some special (`_-`) characters.

States cannot have the same identifying value. Two states with the same name may not exist.

Other than the identifier, a state has three other fields in relation to the actual sprites as seen in game:

Key | Meaning
--- | -------
`flags` | An associative list of `key: object` for defining extra data. There is currently no usage yet. Optional.
`directions` | A number corresponding to the amount of directions a state has. This should be a `1`, a `4` or an `8`.
`delays` | Can be left out. If defined, a list of lists of delays for an animated icon state. Each list in the list corresponds to a direction. The delays are floats and represent seconds.

States are always ordered alphabetically by their corresponding file name.

#### Directions

There are currently three supported direction types: `1` (no directions), `4` (North South East West), and `8` (North South East West plus diagonals).
These directions are ordered (for layout in the `delays` field and ordering in the sprite sheet) in the following order:

* South
* North
* East
* West
* South East
* South West
* North East
* North West

#### Sprite sheet

The PNG file accompanying a state is always the name of the state. For example, a state with name "hello" would be `hello.png` on disk.

The file contains the individual states resolved with the directions and delays of the state. The size of the file is always a multiple of the RSI's `size`. Sprites are ordered from the top left to the bottom right, always going horizontally first. The amount of sprites per row or column is always made to be as equal as possible, favoring rows to be longer than columns if the amount of states is not able to be divided perfectly.

Sprites are written grouped by direction, then writing each icon in a direction in order, so with 4 directions, ALL south states get written first, then north states, etc...

### Example JSON

Note that in practice the JSON writer probably writes the most compact JSON possible to reduce file size.

```json
{
    "version": 1,

    "license": "CC0-1.0",
    "copyright": "GitHub @PJB3005",

    "size": {
        "x": 32,
        "y": 32
    },
    "states": [
        {
            "name": "hello",
            "flags": {},
            "directions": 4,
            "delays": [
                [1, 1, 1],
                [2, 3, 4],
                [3, 4, 5],
                [4, 5, 6]
            ]
        }
    ]
}
```

### Loading Parameters

The `load` key allows various load parameters that change how the engine loads the sprite. Keys are as such:

Key | Meaning
--- | -------
`srgb` | Boolean that indicates whether the sprite is interpreted as sRGB by shaders and such. Default `true`.


## Design Goals

* Editing an RSI must be possible without proper tooling. This means no binary metadata or metadata inside PNG files.
* It must be easily diffable on GitHub.
* It must not bloat Git history too much when changes are made (prevent large file rewrites).
* One PNG One Image
