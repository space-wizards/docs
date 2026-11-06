# Z-levels

## What are they

z-levels are a way to sandwich maps together done via ZMapNetwork. This entails:
- ZLevelMapNetworkComponent, meta component stored in nullspace.
- ZLevelMapComponent, added to component maps.
- ZLevelGridComponent, used to keep grids aligned via soft joints. These are done manually as physics does not currently support cross-map joints.
- ZLevelPositionComponent, used on entities with z-level heights — this is what also hooks into transform-lerping (see lerping.md)

These systems are also used:
- ClientZLevelSystem, this handles gluing lerping with TransformSystem.
- ZLevelGridSyncSystem, this is what runs the soft-joints for ZLevelGridComponent.
- ZLevelSystem handles the map-network + the physics itself.
- ZLevelPhysicsSystem does the meat of the work around entities traversing z-levels.

## CVars

These are under zlevel.* predominantly around controlling the fake "physics" side of it.

## Visuals

If you wish to affect the visuals then use ZLevelVisualsEvent — used for the projection offset if you wish for the z-levels to not be perfectly stacked, and a relevant overlay.
Overlays get the zlevel offset passed in via `OverlayDrawArgs` and know where they are in the stack, relatively speaking.

For world overlays you only want applied once, e.g. damage borders, night-vision, use PostZLevel as the space to avoid them accidentally being applied on every z-level render.

## Physics

This is handled in two main ways:
1. ZLevelGridSync runs soft physics between linked grids, preferring the smaller grid to move more towards the larger grid. Generally you should only need to set the CVars for this under zlevel.*
2. ZLevelPhysics handles the normal entity z-level interactions.

The physics handles 2 parts:
1. Integrating z-level physics velocities in the tick with substepping so high-velocities don't clip.
2. Handling "supports" / "highground" so entities can't drop a z-level where they wouldn't be able to intersect normally.
