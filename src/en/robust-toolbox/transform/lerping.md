# Lerping + Corrections

## Lerping

With ss14 being tick-based we need to render entities in-between ticks. To do this we apply lerping for the following scenarios:
1. Our local entity we need to lerp from tick A -> tick B
2. For remote entities we lerp from tick A -> tick B. Due to the state buffer this will often be 1+ ticks behind. However if tick B does not exist and we receive tick C instead we use that as the target rather than jumping a tick.
3. With z-levels we need to be able to lerp cross-parent and also use z-position — essentially updating the lerp's source position to a new one.

If the correction is large or we otherwise want a snap (e.g. containers, teleports) we need to be able to cancel the lerp entirely.

Something else that makes it a pain is handling multiple transform updates inside one tick, most notably physics substepping, so we need to know what the transform was at the start and end of a tick is.

For the z-level related mechanics to it see z-levels.md

## Correction
If mispredicts happen then the above instantly snaps — this necessitates smoothing errors out.

## CVars

Ideally you don't need to touch these but the net.interp* values handle the interpolation distance and corrections.

## How it works

Transform itself purely keeps simulation state and nothing to do with rendering. All of the rendering values are handle via the client's TransformSystem.

Everything gets handled in 2 spots:
1. ClientGameStateManager handles dropped ticks — if tick B is missing we lerp from tick A -> tick C. This is done via interpolation lookahead.
2. TransformSystem.FrameUpdate handles the remaining data.

In TransformSystem we cache all snapped moves so we know when we need to ignore lerping, but if there are no snaps then we try and figure out if we need to:
- Snap due to interp distance being too far
- Re-parent the entity (grid-traversal and z-levels predominantly — TryCreateEndpoint)
- Handle corrections

Most of the complexity comes from handling prediction, specifically ignoring any rollback / replay transform states and only comparing about the start / end states of a tick.
