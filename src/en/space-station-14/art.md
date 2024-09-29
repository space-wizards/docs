# Art

```admonish warning "Disclaimer"
Keep in mind, all of these rules are general guidelines. 
A sprite can look good and fit well even if it doesn't necessarily follow all of these guidelines to the letter.

These are meant primarily as a resource for new contributors to understand the general aspects that they should be shooting for.
This isn't the stick by which to measure all new or existing art.
You shouldn't be modifying perfectly good sprites solely to shift them from one perspective to another or just to reduce the color count.

These aren't metrics for measuring the objective quality of art, but rather just notes for keeping consistency within the game's visual style.
```

## Theme & Style

### Keep it Grounded
* Although SS14 takes place in the future, the general aesthetic is far from the extravagant techno-elegance of a lot of modern Sci-fi.
Common household items and machines shouldn't look very different from what we have today.


* Keeping designs simple is completely fine.
If you're depicting a simple box or desk object, don't fall into the trap of over-detailing your sprite with bolts, lights, and various technological stigmata.
Some things just look dull, and that's OK!


* It's okay to reference other media in terms of art.
Lots of antagonists and designs take strong inspiration from TV shows, other games, and movies.
However, **keep references subtle**!
They shouldn't stick out an inordinate amount and shouldn't be commonly found.
If someone can identify an obvious pop culture reference, it should be fairly rare so as to not distract from the tone and atmosphere. 

### Contrast Between Boring and Fantastical
* While many elements of SS14 are quite grounded and boring, there are many different fantastical things as well.
For these rarer and more less realistic things, playing up the relative different to the surrounding is important.
This is a large part in the comedic tone of SS14.
* * A wizard in a tower can be sagely and wise, but a wizard waiting to pick up his mail plays into absurdist humor in a beneficial way.
* * A gross or weird alien can be emphasized through contrast with the environment. 
This aids in depicting futuristic items, as they appear even more advanced through their contrast with the things around them.


* When creating art for extremely fantastical or out of place things, it may be beneficial to intentionally push the style.
Using especially vibrant colors or baking in glows into the sprite can give extra emphasis to something that _should_ look out of place.

### The Future Never Looked so Old
* While the setting is unquestionably in the future, the aesthetics of SS14 commonly and routinely reference older technology.
The station is lit with buzzing incandescent bulbs, people send faxes to one another, and computers are still fat consoles with big glass screens.
This retro appearance is an important factor of the visual identity of SS14: _embrace it_.


* When creating new assets or features, playing on existing real world technology can create an intuitive understanding.
Instead of depicting some kind of generic 'credit chip,' using paper bills is immediately recognizable.
If you're trying to communicate the purpose of something, creating a visual association with something the player is likely familiar with can help them intuitively understand its function.
* * If you're make a sci-fi generator, making it look similar to a real-life generator helps people understand it without close examination.
* * Don't worry about the logistical side of retro technology.
Any amount of ancient tech can be hand-waved away with budget restrictions and lazy scientists.
Adhering to a personal concept of lore is secondary to serving the style.

### Readability and Game Sprites

* Keep the size of assets **proportional** to similar objects. 
Obviously items will look over-sized compared to mobs, but making sure that the entire canvas isn't filled by a small object helps establish a relative scale.
It can be confusing when an item that looks small when held appears significantly larger when dropped to the ground.


* **Clothing** shouldn't cover excessive amounts of a mob or areas that shouldn't be covered by that region.
Glasses shouldn't engulf an entire head and a hat shouldn't come down to the shoulders.
Clothing should ideally have minimal overlap with other items so as to reduce visual clutter when many items are worn.


* Mobs and direction-sensitive structures should contain **directional sprites** (directionals) for all 4 cardinal directions.
When making directionals, the height of the asset should remain relatively constant and all details should be preserved for a consistent visual shape.
Likewise, the color and placement of shadows should also shift to better depict the item turning in 3D space.

## Technique

### Perspective

* **Structures** in the game world should be in a 3/4 perspective.
This includes various machines, furniture, and decor.
A 3/4's perspective means that they are angled straight forward with the viewer looking down on them from above. 
This gives you a clear view of the top as well as the front of the object.


* **Mobs**, **clothing**, and **items** are rendered in a flat perspective. 
A flat perspective can be thought of as looking at the image straight-on at eye level.
This maximizes detail while minimizing any perspective-based distortion.
When perspective is necessary for conveying something properly, use 3/4s.


* **Floor tiles** and **ground** textures similarly lack any particular perspective.
The actual floor itself should be a simple birds-eye perspective but any small detailing like stones or pits can employ a more conventional flat perspective.


* **Walls** and wall-like structures (windows, grilles, etc.) are rendered in a exaggerated top-down style typically referred to as _classic_.
Walls shouldn't have any kind of 3/4 perspective and, while the sides may be technically visible, the focus is on the "top" of the wall.
This isn't to say you're seeing inside of the wall into some kind of inner lattice structure, but rather it's more of a flat texture.
Walls are very difficult and strange in their form so it's best to just look at existing walls for inspiration.


* Similarly, **wall-mounted structures** are additionally rendered in a flat perspective.
This is most visible in things like posters and aids in readability.

### Color
* Avoid many overlapping palettes, or _gradients_ of many similar colors, prefer small, distinct palettes.
Make sure the individual colors in a sprite have enough contrast to be discerned in game.
Remember, sprites in game are a lot smaller than your editor: err on the side of high-contrast.

```admonish info "Noise"
Noise and other similar effects can be valuable for adding texture to an image.
Don't be afraid of including mild noise or texture into a sprite!
Use multiple layers to be able to compare and reverse changes easily.
```

* Try not to go overboard with too many different hues.
Sticking with a few primary tones (_department colors are a good use for this!_) and accenting them with neutral tones helps create a cohesive asset that doesn't look busy.


* Don't use **darken**, **burn**, or **gradient** tools for half-tones when shading.
Darker shades of color should be intentionally chosen from your palette.
Using gradients of color can make sprites look muddy and make them difficult to edit in the future.


* Don't overuse **hue-shifting** when creating shades for your palette.
Using it sparingly can lend greater intensity to your darker tones, but overuse can create an overly cartoonish appearance that looks overly fantastical.
The color of an object should still read clearly when shifting is applied: 
* * An apple should be red, not a deep magenta
* * A blue shirt shouldn't be a deep purple in its shadows
* * Regular industrial steel shouldn't be tinted cyan and blue

### Lighting
* Sprites are usually lit from the **top**. 
For standalone object sprites, the light source may be slightly angled to either side, but generally a centered light from above is how most sprites are lit.


* Avoid **high-contrast** lighting. 
Although the primary light source is coming from the top, make sure the ambient light is accounted for.
Objects should be lit in the context of being in a _well-lit room_.
Shadows shouldn't be pitch black and highlights shouldn't be bone white.


* Be mindful of the **luster** of a surface when adding lighting to your sprite.
How shiny is your material?
Cloth surfaces are generally quite matte whereas metal usually has long reflections along its length.
Make sure the amount and contrast of the lighting being applied is appropriate for the surface being depicted.
* * Applying a uniformly glossy lighting across lots of sprites can lead to a 'buttery' appearance that harms readability.
* * Less is more!
A simple sprite with minimal lighting is preferable to an over-worked sprite that reads poorly and sticks out.


* Keep lights **temperature neutral**.
This relates a lot to the earlier point on hue-shifting.
Baking shadows with purple tints gives the impression of _blue ambient light_, when it's largely the opposite!
Keeping the temperature largely neutral ensures that when colored lighting does appear in game, it doesn't clash and creates weird tones.

### Outlines
* All sprites should have **colored outlines** around them.
This helps improve readability in the world and clarify the forms.
Make sure that the outline is colored according to the section it surrounds, instead of being a single flat color.
* * Outlining an entire sprite in black often looks plain and amateurish.
Using multiple colors in your outline gives a much better result.


* Don't include shading on your outlines.
The value of the outline should be consistent across the entire shape.


### Miscellaneous

* **Center** sprites within the canvas. 
This helps massively when displayed in-hand or inside the UI. 


* Avoid **anti-aliasing**, as this creates muddy edges and transparencies that look ugly and mess with the interaction outline shader.
Anti-aliasing artifacts are extremely pronounced at a low resolution.

## Technical Info

### Size
* The vast majority of Sprites are **32x32** pixels in size.
This is the size of a single in-game tile.
When making multi-tile sized objects or machines, you may need to adjust the sprite's size to 64x64 or even larger (note that the meta.json in the RSI will need to be adjusted to account for this).


* When it's necessary to mix sprite sizes, such as using 64x64 pixel inhands for particularly large items, simply make a separate RSI with the same name and the `_64x` suffix in order to denote the relationship between the two.


* Do not use `SpriteComponent.Scale` to increase the fidelity of sprites.
A 64x64 sprite with a "0.5, 0.5" scalar factor applied will indeed be equally sized to a 32x32 sprite but with increased resolution.
However, the mixing of pixel sizes looks extremely messy and with certain settings is completely unreadable.


* Similarly, avoid the use of `SpriteComponent` scaling in order to depict size.
Either respriting to a smaller size or using technical elements that preserve the size of individual pixels (displacement maps) are far better method for portraying size.


### Licensing
* the `meta.json` file requires the author to supply both a license and a copyright.
The copyright is simply the provenance of the art within the file, specifying the specific codebase and commit that the asset was taken from.
The license is a specific copyright license used for assets.


* The following are valid licenses for the project: "CC-BY-3.0",
  `CC-BY-4.0`,
  `CC-BY-SA-3.0`,
  `CC-BY-SA-4.0`,
  `CC-BY-NC-3.0`,
  `CC-BY-NC-4.0`,
  `CC-BY-NC-SA-3.0`,
  `CC-BY-NC-SA-4.0`,
  `CC0-1.0`
* * `CC0-1.0` denotes public domain assets.
* * Assets with the `BY` discriminator must be attributed.
* * Assets with the `NC` discriminator denote non-commercial assets. 
**WARNING: These assets may be disallowed from use in the repo in the future.**
Use NC assets sparingly.
* * Assets with the `SA` discriminator are share-alike and must be distributed under the same license.


* When porting assets from SS13 servers, it's important to check and preserve the license that the sprites are coming from.
This information typically isn't readily available, but it can usually be found in the README.txt file for the project.
* * When in doubt about the ability to use a file, try joining the discord and asking.


### Miscellaneous

* Make sure all images are encoded in RGB color.
Using indexed color or grayscale color encoding can make it difficult to modify assets in the future.


* Keep RSIs as generally limited as possible.
An RSI should be all the appropriate sprites for a general object.
Multiple variations of an object are fine (different versions of an ID card), but refrain from creating overly large RSIs with 30+ files in them.


* When appropriate, split up sprites into layers and use visualizers to enable changes. 
You don't need to create multiple sprites for every combo of open door when you can just have separate open door layers and other layers that work independently.
