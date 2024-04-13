# Displacement Maps

People asked me for a quicky about how displacement maps work so uhhh...

Ok so in [PR #26709](https://github.com/space-wizards/space-station-14/pull/26709) I added displacement maps. Yippee. This allows you to deform a sprite based on another, specially-crafted sprite. How do we make these specially crafted sprites?

## Displacement map format

Displacement maps should work the same as [BYOND's](http://www.byond.com/docs/ref/index.html#/{notes}/filters/displace). I did not at all test BYOND's so there's a nonzero chance I misread their docs and they're like interpreted inversely or something. Whatever.

The basic idea is that each pixel of the displacement map specifies how much to "shift" the pixels at a position. It should be noted that, due to how GPUs work, this may not work as you may anticipate. Instead of specifying "Pixel X displaces to position Y", it actually specifies "Pixel X reads from position Y". i.e. if you specify a displacement of +1 pixel horizontally, the sprite will visually shift to the **left**, because they get their color from the texture pixel +1 to the right.

The red channel controls horizontal deviation, the green channels controls vertical deviation. A red and green value of 128 is "neutral", i.e. no difference. Greater red or green values cause displacements to be sampled to the bottom right, effectively meaning the sprite moves to the "top left".

The actual displacement value can be changed with a "size" parameter on the shader. Basically this size parameter is "how many pixels are shifted at the maximal pixel value". With a "size" of 4, a value of 255 would shift by 4 pixels. With a size of 127, each value on the channel is a one pixel shift (129 -> +1, 130 -> +2).

Oh yeah btw I decided to make it so that the alpha channel of the image is a simple mask. That means you can set alpha to 0 to completely cut out a pixel.

The blue channel is ignored, I personally used it to mark off "modified" pixels to make it easier to see what a displacement map is doing in an image editor.

## Actual shader

The actual displacement map shader in SS14 is located at `/Textures/Shaders/displacement.swsl`. It has three parameters: `displacementSize` is the size described above, and `displacementMap` and `displacementUV` are intended to be filled out with the `CopyToShaderParameters` system of a sprite component. See the PR I linked above as example.

## Displacement RSI load parameters

Remember to set the following in your RSI's `meta.json` because otherwise sRGB will eat your face and none of the math will make sense:

```json
"load": {
    "srgb": false
}
```

## Aseprite scripts

I wrote some Aseprite scripts to help with authoring displacement maps. You can find them in the `Tools/` folder of SS14's repo.
