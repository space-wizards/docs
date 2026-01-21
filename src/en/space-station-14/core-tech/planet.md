# Lighting

This section explains how lighting works for "planetmaps". Overlays draw directly to the lighting render target which gets re-used for the engine-side lighting that's applied.

## Enlarged light target

First an enlarged light target is retrieved and is used for rooves and tile emissions. This is to ensure we can blur properly with off-screen pixels. We apply the default clear color to this render target.

![Enlarged light target](..\..\assets\images\planet\render0.png)

## Rooves

We draw the specified roof color (typically black) onto any tiles that are flagged as being rooves, as well as any tiles that have entities considered to be rooves on them.

![Rooves](..\..\assets\images\planet\render1.png)

## Tile emissions

Similar to rooves except without the per-tile data and drawn for any entity on-screen that has the component.

![Tile emissions](..\..\assets\images\planet\render2.png)

## Blur

At this point we apply a blur after the above overlays as we want to blur more than the default lighting amount.

![Blur](..\..\assets\images\planet\render3.png)

## Sun shadows

This one is a bit trickier. For every entity on-screen we take their "shadow points" (stored on the component) then extrude these by the sun's shadow direction. This gets us a polygon (typically a diamond shape with 6 points) which we draw the relevant color onto the screen with.

There is also an annotated screenshot below to better show what happens to a singular entity.

Note: This is drawn to a stencil first to make sure the colour's inconsistent and so we can ignore overdraw.

![Stencil](..\..\assets\images\planet\render4.png)

![Final](..\..\assets\images\planet\render5.png)

![Extruded](..\..\assets\images\planet\render5-annotated.png)

## Final note

Yes I realised I forgot to clear the old clear color when writing these docs.
