# AppearanceSystem Compliance

| Designers | Implemented | GitHub Links |
|---|---|---|
| SlamBamActionman | :warning: Partially | TBD |

## Overview

Currently there is no reliable way to trace in what ways an entity's sprite is modified. An entity can be modified by component systems on *itself*, by components on *child entities* (even without it being explicitly tracked as a child entity), by components on *any other entity* or just *systems in general*. The only reason why sprites are properly replicated across clients currently is because all those disparate systems are all included in the data the client is being sent. This may work to get matching 1:1 sprite parity in the moment, but recording the sprite state of an entity becomes increasingly difficult.

Since SpriteSystem works fully clientside you can only determine the sprite of an entity indirectly, i.e. every client needs to get relevant data and then recreate the sprites and any modifications to it on its own. This is good! Updating and tracking the exact sprite and frame serverside would take an unconsciable amount of resources, so letting the client sort that out is much better. The problem is that, due to the laissez-faire attitude to sprite modification, it is currently not always possible to determine the sprite of an entity, at least not without using systems that handle hardcoded edge-cases that require specific child entity setups or that introduce unwanted functionality to an entity when all you want are the sprite's visuals.

### Unwanted functionalities 

One such example is [ClientClothingSystem](https://github.com/space-wizards/space-station-14/blob/10877ebbf975ac2c75a13f3b6ef146166acce049/Content.Client/Clothing/ClientClothingSystem.cs). To set clothing sprites on an entity it requires that the entity 1) has an InventoryComponent, and 2) it has equipped an entity with the desired clothing sprite in the correct inventory slot. This means that to create the preview character in the game's pre-round lobby there is an entity character created with an inventory that gets the actual items equipped.

This isn't too egregious in this usecase, but it's an example of how some visualization is hard tied to game logic. And it causes a ripple effect, since some systems have to create workarounds.

In the end-of-round screen the character icons are made to be visual copies that match the character sprite in the moment the round ends, using `SpriteView`. Needing to use `SpriteView` is necessary here since you can't reliably copy clothing visuals otherwise, but this implementation both results in the characters showing visual changes that probably should not be replicated over (such as taking damage making the sprite flash red), and also characters disappearing from the list once the round is over since the character entities have become unloaded:

![image](https://github.com/user-attachments/assets/6c03a77f-af0c-4fe0-815b-39a0a873b878) ![image](https://github.com/user-attachments/assets/8670a04a-5b2d-4bc7-8fe6-12489f4fd2b0)

This is just one example of a system that causes problems by editing one entity's sprite based on other entities and systems. 

### AppearanceSystem, and its flaws

[AppearanceSystem](https://github.com/space-wizards/RobustToolbox/blob/b0d17e95276fba31027bb8d45345c5cdf9e16c3c/Robust.Client/GameObjects/EntitySystems/AppearanceSystem.cs) is a way to make the visualization synchronization between server and client a bit easier and more generic. The system relies on `AppearanceComponent` for entities and its property `AppearanceData`. Instead of game logic systems setting the sprites directly based on component properties, they instead set enum key-value pairs in `AppearanceData` corresponding to either states or property values. Specific visualizer systems (i.e. systems that subscribe to the `OnAppearanceDataChanged` event) can then use that data to apply sprite changes. This decouples game logic from visuals, and if another entity want to copy the visuals they only need to copy the base sprite, the visualizer systems and the entity's `AppearanceData`.  

At least, this is how it works in theory. Unfortunately this method of ensuring replicatable visuals has had the following problems:
- There is no check to prevent game logic systems from editing the sprite directly. That means you can have changes to a sprite that aren't evident from the `AppearanceData`.
- There is no check for ensuring that game logic is not included in a visualizer system, nor is there one to ensure `OnAppearanceDataChanged` isn't subscribed to outside visualizer systems.
- There is no way to know what visualizer systems are acting on an entity. Since there is no way to determine what is and isn't a visualizer system, you either have to hard-code which components to copy over, or copy every single component over (including game logic ones).

There are also some minor issue like how there's no consistent naming scheme for visualizer systems (e.g. "SystemNameVisuals" vs. "SystemNameVisualizer"), and how there is a "helper class" named `VisualizerSystem` that is just a normal EntitySystem that requires implementing subscribing to `OnAppearanceDataChanged` but doesn't do anything beyond that.

### Proposed Solution, Overview

In a perfect world, the process of setting and copying an entity's sprite would be the following:

Setting a sprite: 
1) An entity is spawned in and has a default prototype with sprite data set; this is effectively the "base" to start from.
2) A game logic system (`ExampleSystem` & `ExampleComponent`) performs its functions and, as a result, requires the sprite to change.
3) The game logic system sets a key-value pair in the entity's `AppearanceComponent.AppearanceData`, and ensures the entity has `ExampleVisualizerComponent`. This raises the `OnAppearanceDataChange` event.
4) The `ExampleVisualizerSystem`, which subscribes to `OnAppearanceDataChanged` for any entity with an `ExampleVisualizerComponent` on account of inheriting `VisualizerSystem`, reads the event.
5) `ExampleVisualizerSystem` applies sprite changes via its logic based on the `AppearanceData` as input.

Copying a sprite:
1) An entity (_A_) wants to copy the exact visuals of another entity (_B_).
2) _A_ looks up the prototype for _B_ and copies the SpriteComponent data from the prototype.
3) _A_ queries all `VisualizerSystem` components from entity _B_ and applies them to itself.
4) _A_ copies all `AppearanceData` from _B_, which triggers any relevant `VisualizerSystem` to perform their logic, setting sprites in `SpriteSystem`.

This would result in a flow of operations that looks like this:
![image](https://github.com/user-attachments/assets/3ffcd550-d56a-4cbf-a9b6-ec3b43b7fc21)

Any change to `SpriteSystem` must go through `VisualizerSystem`s first, which in turn only act on data from `AppearaceSystem`. 
__You should be able to derive the exact appearance of an entity based on VisualizerSystems and AppearanceData alone.__

In comparison, this is how the flow of operations looks currently:
![image](https://github.com/user-attachments/assets/ebd0aaa8-ba73-4fdd-9585-45b5fc9ff594)

The red arrows show "destructive" operations where you either can't know for certain whether an edit to a sprite has been made, or it requires iterating over all systems for all objects to be fully certain that you have copied visuals fully.

### Proposed Solution, implementation

To achieve the overview, the following implementation would be required:

- Any game logic system that modifies sprites is split up into a game logic system and a VisualizerSystem. The game logic sets AppearanceData instead of modifying the sprites directly.
- All VisualizerSystems are connected to VisualizerComponents (e.g. `ClothingSystem` have `ClothingVisualizerSystem` and `ClothingVisualizerComponent`; the system handles the visual logic, and the component indicates an entity should run the system).
- SpriteSystem/SpriteComponent may not be accessed outside of VisualizerSystems, to prevent game logic systems modifying sprites.
- VisualizerSystems must be connected to a VisualizerComponent; this is enforced with the Attribute tag `[VisualizerComponent]`.
  - This tag is also what allows easy copying of visualizers between objects, as the copying entity can check for all components with the tag.
 
Entities are free to modify the `AppearanceData` of other entities. `AppearanceData` should not be used to store game logic and should be kept as lightweight as possible; only data used to modify the entity's base prototype sprite should be included.

The use of VisualizerSystems and components, as well as access to SpriteSystem, can be mechanically enforced in the codebase. There would need to be attention paid during code review to ensure there is no game logic performed inside of VisualizerSystems.
 
### Issues

This implementation does have its downsides:
- You end up with a lot more systems and components!
  - This could be mitigated with attention to file sorting and multiple game logic system sharing a single visualizer, similar to how [WieldableSystem](https://github.com/space-wizards/space-station-14/blob/10877ebbf975ac2c75a13f3b6ef146166acce049/Content.Shared/Wieldable/WieldableSystem.cs) handles all game logic components adjacent to wielding.
- Ensuring visualizer system order isn't clear!
  - This could possibly be mitigated with the use of the `after:` keyword when subscribing to the `OnAppearanceDataChanged` event, so that for example the rotation caused by lying down overwrites the rotation caused by waddling.

### Animations

Animations (especially looping ones) would require syncing the start time/offset of the animation frame, so that if a new client loads the animating entity it can accurately set the sprite's animation. This needs to be replicated across multiple systems such as lights and movement as well.

### Examples of concrete uses

- Remembering sprites at point in time
  - End of round sprites
  - Photography
- Reliable chameleon projector
- Copying character appearances
  - Changelings
- Easier maintainability / Less hardcoded systems
