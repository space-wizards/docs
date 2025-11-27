# Sprites & Icons

`SpriteComponent` and `IconComponent` are the two primary rendering components for entities. `SpriteComponent` is for rendering of entities on the map, while `IconComponent` is a simpler way to represent an entity's icon in say the spawn panel.

## Texture Selection

There are two ways to select a texture:
1. A direct texture file (right now a PNG).
2. From an RSI, with a state ID. An RSI is our equivalent to BYOND's DMI format, containing a list of icons by key.

Loading from a texture is pretty easy. You just specify a path to a `.png` file in the VFS and you're good.

With an RSI, you need to specify the RSI itself in one variable, then the RSI state in another.

### `IconComponent`

`IconComponent` has 3 properties in a prototype:
```yml
- type: Icon
  texture: ""
  sprite: ""
  state: ""
```

`texture` is used to refer to a direct texture such as a PNG. `sprite` and `state` are used to refer to an RSI and the relevant state for it, respectively. These are mutually exclusive: you cannot use `texture` together with `sprite` and `state`.
.
### `SpriteComponent`

Ah this is where it gets fun. `SpriteComponent` does everything, shader support, layers, directions, animations...

The component uses multiple layers, sorta like overlays in BYOND. These layers are drawn in order, meaning that the last layer in the list will be on top.

You can specify layers in a prototype as a list under the `layers` key, so like this:
```yml
- type: Sprite
  layers:
  - texture: "a.png"
  - texture: "b.png"
  - ...
```

A layer in a prototype has the following properties:

* `texture`: same as for the `IconComponent`.
* `sprite`: same as for `IconComponent`. If this is not specified, a layer can fall back to the `sprite` property of the main prototype (more on this below).
* `state`: same as for `IconComponent`: the RSI state to use.
* `shader`: this is where it gets fun: the ID of a shader to use. [See here for documentation on shaders](./shaders.md).
* `scale`: Scale applied to the layer, as a vector 2 (2 floats separated by comma).
* `rotation`: Rotation applied to the layer, in degrees.
* `visible`: `true` or `false`, enables/disables the layer. This is useful if the layer gets re-enabled by code, such as the flame of a welding tool.

The main prototype also has some properties:

* `sprite`, `state` and `texture`. These function as quick short hands for the same properties on layers. If these are set, a layer is added with these as texture parameters. One thing to note is that **`sprite` functions for all layers, unless the layer specifies one itself.** So you can set the base sprite of the prototype to an RSI, and then each layer only needs a state specified.

* `scale`: scale applied to every layer.
* `rotation`: rotation applied to every layer, in degrees.
* `offset`: amount to offset every layer with.
* `drawdepth`: draw ordering of this sprite. This maps to the `DrawDepth` enum in code. Higher means the object will render above objects with a lower draw depth always.
* `color`: color multiplication applied to every layer. Use a hex color.
* `directional`: if true, the sprite will not rotate with the entity, but will change RSI direction to north/south/east/west or whatever. If false, these directions will be ignored and the sprite will rotate as normal. Disabling this is useful for top-down sprites that should rotate such as bullets.
* `visible`: makes the entire component visible or not.

All these properties can be changed at runtime with methods on the component.