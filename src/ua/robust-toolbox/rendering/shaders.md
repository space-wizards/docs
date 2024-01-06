# Shaders

[Shaders](https://en.wikipedia.org/wiki/Shader) are programs used to implement graphical effects that run on the [GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit). SS14 uses [pixel (fragment) shaders](https://en.wikipedia.org/wiki/Shader#Pixel_shaders) to implement per-sprite effects including stealth; and overlay effects, including space drugs, drunkenness, blindness, and singularity space bending.

# Defining a Shader
Each shader has a YAML prototype stored in `Resources/Prototypes/Shaders`. All shaders have fields:

- `type`: must be `shader`
- `id`: unique prototype ID (a string) that identifies this shader
- `kind`: either `canvas` or `shader` (see below)

## `canvas` Shaders
This is a shader with preset options, akin to Godot's `CanvasItemMaterial`. This shader has two required properties:

* `blend_mode`: The way the object is drawn over the scene. These are the same as the [equivalent for Godot](https://godot.readthedocs.io/en/3.0/classes/class_canvasitemmaterial.html). Barring the naming being slightly different. Possible values are `mix`, `add`, `subtract`, `multiply` and `premultiplied_alpha`
* `light_mode`: The way the object interacts with light. Again equivalent to Godot's, with the values being `normal`, `unshaded` and `light_only`.

For example, the `unshaded` shader, which is used to draw the lit portion of computer displays and indicators by masking lighting operations, is defined by:

```yml
- type: shader
  id: unshaded
  kind: canvas
  light_mode: unshaded
```

A canvas shaders is really just the default source shader (see `/Shaders/Internal/default-sprite.swsl`), with the lighting, blending, and stencil options applied.

## `source` Shaders
These are custom shaders written in the Space Wizard Shader Language (SWSL). `source` shaders have one required property:

- `path`: The path, with respect to the `Resources/` directory, of the SWSL shader source file.

For example:

```yml
- type: shader
  id: GreyscaleFullscreen
  kind: source
  path: "/Textures/Shaders/greyscale_fullscreen.swsl"
```

Custom shaders are typically stored in `.swsl` files in `Resources/Textures/Shaders`.

## SWSL
Space Wizard Shader Language (SWSL) is based on the  [Godot Shading language](https://godot.readthedocs.io/en/3.0/tutorials/shading/shading_language.html). Most of the compatibility differences between Godot and SWSL are handled automatically, except for the following differences:

- You MUST ensure that all numeric types (e.g. `float`, `vec3`) have a `highp` or `lowp` precision qualifier. See [this article on why](https://stackoverflow.com/questions/28540290/why-it-is-necessary-to-set-precision-for-the-fragment-shader).

- Avoid using any variable names that are reserved words in common shader specifications. Your computer may ignore them but they will break on other machines. [Check the keywords section (3.8) here](https://registry.khronos.org/OpenGL/specs/es/3.0/GLSL_ES_Specification_3.00.pdf)

Since this is a 2D game, only the fragment shader is used, i.e. the shader consists, at minimum, of:

```glsl
void fragment() {
    COLOR = vec4(r, g, b, a);
}
```

### Available Variables (Fragment Shaders)

| Name                | Type          | Description                            |
|---------------------|---------------|--------------------------------------|
| `FRAGCOORD`         | `highp vec4`  | The coordinates within the fragment. |
| `COLOR`             | `lowp vec4`   | The resulting pixel color. _(Think of it as the return value of the fragment shader.)_ |
| `lightMap`          | `sampler2D`   | The lighting map of the current fragment (applied automatically by `base-default.frag`)|
| `modulate`          | `highp vec4`  | The draw color (applied automatically by `base-default.frag`)|
| `SCREEN_PIXEL_SIZE` | `highp vec2`  | The size of one pixel, in local units.|
| `TIME`              | `highp float` | The number of seconds since game startup.|
<!--
| `projectionMatrix`  | `highp mat3`  | **TODO**                             |
| `viewMatrix`        | `highp mat3`  | **TODO**                             |
| `UV`                | `highp vec2`  | **TODO**                             |
| `Pos`               | `highp vec2`  | **TODO**                             |
| `TEXTURE`           | `sampler2D`   | **TODO**                             |
-->

## Stencil Test Parameters

Shader support stencil operations. This is an advanced rendering feature that can be useful for some things if you know what you're doing. The feature closely mimics the stencil parameters as exposed by OpenGL (and as far as I can tell, Vulkan too). See [The OpenGL wiki](https://www.khronos.org/opengl/wiki/Stencil_Test) if you need a reference.

Stencil parameters are defined in a separate `stencil` object. As an example:

```yml
- type: shader
  id: stencilDraw
  kind: canvas
  stencil:
    ref: 1
    op: Keep
    func: NotEqual
```

Indeed, stencil parameters are independent from the shader `kind`.

The options are:

* `ref`: The reference to compare / write as passed to the second parameter of `glStencilFunc`.
  * Default is 0.
* `op`: The operation to apply to the stencil buffer if the stencil test passes. You can only set the op on pass (`glStencilOp`'s third parameter).
  * Options are `Keep`, `Zero`, `Replace`, `IncrementClamp`, `IncrementWrap`, `DecrementClamp`, `DecrementWrap`, `Invert`
  * Default is `Keep`.
* `func`: The comparison function to use to see if the test passes. (`glStencilFunc`'s first parameter).
  * Options are `Always`, `Never`, `Less`, `LessOrEqual`, `Greater`, `GreaterOrEqual`, `NotEqual`, `Equal`.
  * Default is `Always`.
* `readMask`: Mask to use when reading from the stencil buffer (`glStencilFunc`'s third parameter).
  * Default is all 1's
* `writeMask`: Mask to use when writing to the stencil buffer (`glStencilMask`'s parameter).
  * Default is all 1's
  
# Overlays
An overlay applies a shader to an entire screen or viewport (as opposed to individual sprites). Drug effects, blindness, and singularity space bending are examples of overlays (written in C#) that load shader prototypes (defined in YAML) with may load custom shader effects (written in SWSL).

Overlays extend `Overlay`, for example:

```csharp
    public sealed class BlindOverlay : Overlay
    {
        [Dependency] private readonly IPrototypeManager _prototypeManager = default!;

        // Set this to true to get a ScreenTexture. Otherwise, it is null.
        public override bool RequestScreenTexture => true;
        
        // This needs to be set to the appropriate overlay layer.
        public override OverlaySpace Space => OverlaySpace.WorldSpace;
        
        // Store references to the shaders.
        private readonly ShaderInstance _greyscaleShader;
        private readonly ShaderInstance _circleMaskShader;

        public BlindOverlay()
        {
            IoCManager.InjectDependencies(this);
            // Load shaders from prototypes
            _greyscaleShader = _prototypeManager.Index<ShaderPrototype>("GreyscaleFullscreen").InstanceUnique();
            _circleMaskShader = _prototypeManager.Index<ShaderPrototype>("CircleMask").InstanceUnique();
        }
        
        protected override bool BeforeDraw(in OverlayDrawArgs args)
        {
            // If this returns true, this shader will be drawn. If this
            // method is not overriden, it defaults to returning true,
            // i.e. the shader is always active for everyone all the time.
        }
        
        protected override void Draw(in OverlayDrawArgs args)
        {
            // If your shader needs inputs (the pixels currently on the screen),
            // you must check that it is not null and pass it into your shader.
            if (ScreenTexture == null)
                return;
                
            _greyscaleShader?.SetParameter("SCREEN_TEXTURE", ScreenTexture);
            
            var handle = args.WorldHandle;
            var viewport = args.WorldBounds;
            // draw the greyscale shader
            handle.UseShader(_greyscaleShader);
            handle.DrawRect(viewport, Color.White);
            // draw the circle mask shader
            handle.UseShader(_circleMaskShader);
            handle.DrawRect(viewport, Color.White);
            // stop using this shader
            handle.UseShader(null);
        }
    }
```

The shader needs an area to draw in. Here, it's a white rectangle equal to the **WorldBounds.** Note that **WorldAABB** is not adjusted for rotation and is likely to break many shaders.

Finally, in order for overlays to actually be drawn, they need to be added to the overlay manager:

```csharp
[Dependency] private readonly IOverlayManager _overlayMan = default!;
_overlayMan.AddOverlay(your_overlay_here);
_overlayMan.RemoveOverlay(your_overlay_here);
```

If this overlay is supposed to be always active, add it to `PostInit()` in `Content.Client/Entry/EntryPoint.cs`.

# Testing and Debugging

```admonish warning
Test your shaders **both with and without compatibility mode**.
```

```admonish info
You can use the `/rldshader` command to reload the `.swsl` shaders without restarting the game. This means you can often use colour outputs to interactively debug shaders. 
```

Unlike programs written in C#, shaders are compiled by your graphics driver at *run time*, which means that even simple syntax errors in shaders will **only show up when you start the client**.

Therefore, it is important that you test your shader by running the client. Shader syntax errors will show up as exceptions (you'll need to do some looking to find the error message) while loading shader prototypes.

For certain classes of errors, the client will dump an `error.glsl` file with the post-processed shader that failed to load. Usually the shader compilation output log will also be shown and identify the problem, but you can also feed the `.glsl` file to a tool like 

[glslang](https://github.com/KhronosGroup/glslang).

## External Tools
* [renderdoc](https://renderdoc.org/) - An excellent tool for debugging rendering and shaders.
