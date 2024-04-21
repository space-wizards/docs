# Dungeons

Dungeons are procedurally generated structures constructed from templates.

## Quickstart

To generate a dungeon:
1. Have a map, either space or planet (via the `planet` command) ready
2. Have a preset in mind, then run the dungeon command. This has autocompletion to help. `dungen <MapId> <preset> <position X> <position Y> [Optional seed]`. This will then run a job to generate the dungeon.

You should note that at the moment planets keep any visited areas loaded so if you load the dungeon on an area that's been visited before it will mix with the biome entities. To prevent this load it somewhere else (the easiest way to determine is zoom out and see what loaded tiles).

## How it works
DungeonPresetPrototype

V

DungeonRoomPackPrototype

V

DungeonRoomPrototype

### Dungeon templates
Dungeon rooms specify what map to use and the tile offset into the map. This keeps the map count down, makes loading faster, and allows all rooms to be visible at once.

When making a new template you should make sure to save it as a map and that the map has the gridcomponent.

### Dungeon preset
The dungeon preset has a list of areas that can be occupied via room packs. It also has a whitelist of rooms to use.
The dungeon preset is fixed and has no RNG involved.

### Dungeon room pack
These comprise a list of rooms inside of a fixed bounds. This bounds is matched to the room pack areas specified in preset.
These are randomly selected to be used for the preset as long as the areas match.

Note that the rooms inside of a pack should not touch each other; the generator will form connections between them.

### Dungeon rooms
These specify a bounds for the area they match inside of a room pack.
As outlined above they also specify the map and what part of the map their contents comes from.

### Additional notes
Presets, room packs, and rooms can be used inside of any valid rotation.

Generation is only deterministic to the degree that the same configuration on the same commit will give the same dungeon between runs. If new prototypes are added then this will adjust the room selection.

## Making new content
Adjusting the prototypes requires simple yaml changes. You should make a map ingame and check the coordinates are correct and to see what your layout would look like.

Making new rooms requires a saved map file and prototypes created specifying the offset into the map to be used. Look at the existing DungeonRoomPrototypes to see what the yaml looks like.

There is a template that can be used below. **Note that there is no limit to size or rooms.**

[dungeon_template.yml](../../../../assets/misc/dungeon_template.yml)

## Mapping suggestions

* At the time of writing there is no automatic cabling so if you wish for the dungeon to be powered it's recommended you attach wires at the middle points on each edge for your rooms (still inside of the bounds).

