# Adding a Simple Bike Horn

{{#template ../templates/outdated.md}}

This tutorial goes over the **entity component system** system and several other key topics in the SS14 codebase by demonstrating how one would implement a clown horn from scratch. You can try copying the steps yourselves, or you can just read along.

## Entities, components, and systems

While Space Station 14 is written in C#, an object-oriented programming language, it uses a different data model to represent items in game. This data model is called the *entity component system* (ECS). (*Why do we do this? See [ECS](../robust-toolbox/ecs.md)*)

### Entities

Each item in game is represented by an *entity*. Players, bananas, stun batons, are all represented by entities. An entity is represented by an integer. No two entities share the same integer representation.

By themselves, entities only distinguish one item from another. Without any components, an entity has no behavior.

### Components

*Components* have two primary functions:

1. **Label specific entities as having specific behavior.** For example, in one particular game, the entity represented by the integer 37629 contains a `NukeComponent` and a `ActivatableUIComponent`. This means that this entity behaves like a nuke, and also has a user interface that can be raised by activating it.

2. **Store data required to process its behavior.** For example, a `NukeComponent` may have a data field `Timer` that represents how much time is left until the nuke detonates.

Still, components do not contain any logic for processing this behavior. Behaviors are implemented in entity systems.

### Systems

An *entity system* (often abbreviated to "system") contains logic that implements behaviors for specific components. While there may be multiple entities with `NukeComponent` in one game, there is only one `NukeSystem`. The single `NukeSystem` is responsible for processing all entities with `NukeComponent`.

Entity systems implement behavior by defining *event handlers* or by implementing a per-tick *update* method.

As an another example, consider the `FoodComponent`. A programmer might make `EatingSystem` to handle eating food. `EatingSystem` listens to the `OnUseInHand` event - whenever `OnUseInHand` is heard/triggered, `EatingSystem` checks if there is a `FoodComponent` in the object that was used. If there is, then it lowers the value of `nutritionLeft` and plays a munching sound.

That's the jist of ECS. If you're interested in learning more about it, then check out [Your mind on ECS](../robust-toolbox/ecs.md). The ECS approach really is powerful and allows us to avoid spaghetti code, despite the complexity of SS14.

```admonish info
You don't have to perfectly understand the ECS architecture at first. It can be daunting for both new programmers and those used to traditional OOP. However, the overall 'feel' and advantages of the architecture should become clear as you use it more.
```

## How do I make an Entity and give it Components?

SS14 uses a system we call **prototypes**. These are "entity presets", essentially. They are similar to *prefabs* in Unity, or a subtype of `/obj` or `/mob` in BYOND. 

Entity prototypes define *which components are on the entity, and what data those components hold*. It also defines basic data like the entity's name, description, and prototype ID (used to spawn it). 

An example is shown below:

```yaml
- type: entity
  parent: BaseItem
  id: Skub
  name: skub
  description: Skub is the fifth Chaos God.
  components:
  - type: Sprite
    sprite: Objects/Misc/skub.rsi
    state: icon
  - type: Item
  - type: ItemCooldown
  - type: EmitSoundOnUse
    sound: /Audio/Items/skub.ogg
  - type: UseDelay
    delay: 2.0
```

This is written in **YAML**, a data language similar to JSON, and is located in the folder `Resources/Prototypes/Entities/Objects/Fun/skub.yml`. All prototypes must be in the `Resources/Prototypes` folder and should be organized into the proper folder. 

If you want more pointers on YAML, check [YAML Crash Course](../general-development/tips/yaml-crash-course.md) and [Serialization](../robust-toolbox/serialization.md).

The entity prototype shown is "Skub", which looks like this in game:

![skubexample.png](en/assets/images/ss14-by-example/skubexample.png)

As you can see in the YAML, it has many components, including `EmitSoundOnUse` and `ItemCooldown`. It is up to the coders to determine what data components hold and how systems give them behavior.

To spawn the items in game from a prototype, you can press **F5** to open the **Entity Spawn Panel**. There is also a way to spawn prototypes in code.

## Okay, now I want to honk!

Your goal is to make a **Clown Horn** that **honks** when you use it. This requires us to have a component on the entity with a sound to play and system that plays that sound after it's used in hand (clicked, or activated with Z).

```admonish info
Normally, you would want to search through the codebase and ask some other coders to see whether a component/system that does this already exists. In this case, ```EmitSoundOnUse``` *does indeed exist* in the main SS14 codebase. But for the sake of this tutorial, we'll pretend it doesn't and try to implement it ourselves!
```

**To start off**, let's make a simple clown horn prototype. I will make a new file called ```clown_horn.yml``` and add it to the ```Resources\Prototypes\Entities\Objects``` folder.

![](https://i.imgur.com/qR0QzqA.png)

Might want to organize that into the "Fun" folder later, but organization is up to you and your codebase!

Now let's fill out the prototype with a basic clown horn. Because we don't yet have a dedicated SS14 prototype editor, many people usually just copy a similar prototype and modify it to their needs.

```yaml
- type: entity
  name: clown horn
  parent: BaseItem
  id: ClownHorn
  description: It goes honk honk!
  components:
  - type: Sprite
    sprite: Objects/Fun/bikehorn.rsi
    state: icon
```

Here we have a basic entity with a single component: `SpriteComponent`. Check out [the RSI spec](../specifications/robust-station-image.md) if you're unfamiliar with the RSI system, but the gist is that we have two fields for `SpriteComponent`: the RSI path relative to `Resources/Textures` (in this case the folder is named bikehorn.rsi) and the icon state.

One thing to note is that prototypes support parenting. In this case, `BaseItem` is our parent and contains a variety of components that are universal to all items. Thus, our clown horn will have those components too: basic components like `Item`, `Pullable`, and `Physics`. Parents aren't required at all, but they're useful in certain cases, like here.

Now, let's compile and check out our item in game:

![](https://i.imgur.com/dHigBbc.png)

It sure is beautiful, but we appear to have lied! The bike horn does not yet honk honk. To remedy this, we'll have to create a new component to hold the data, such as the sound to play, and an EntitySystem which handles actually playing the sound.

## Creating our component

To make our component, we'll need to make a new class, let's call it ```PlaySoundOnUseComponent```. But wait a second....

![](https://i.imgur.com/s9O13qH.png)

Where do we put it? To answer this question, we have to think broad. We have to think about the **client** and the **server**.  

### Client-Server Paradigm

If you haven't read [Codebase Organization](../general-development/codebase-info/codebase-organization.md) already, it might be worth a read. But for this tutorial, there are only two things you need to understand:

- The SERVER and CLIENT execute SEPARATELY.
- The server should handle most logic to prevent exploits. Anything on the client can be altered by a malicious user.

With that in mind, our logic for our clown horn should look like this:

- Client sends "I use this item" to server.
- Server receives this, checks if it makes sense, and sends "play honk" to all clients in range.
- Client receives this and plays "honk".

This sounds rather complicated to implement from scratch. Thankfully, we have some premade code that helps us! Namely, the event `UseInHandEvent` which is raised on the server when an item is used, and the function `SoundSystem.Play()` which plays a sound to clients in range.

Those helpers can be thought of as handling **client click -> server** and **server -> client sound** for us. so all we need to do is have a component on the server which routes one into the other. 

### A basic implementation of a component

```admonish warning
In the Space Station 14 codebase, Components & EntitySystems alike (along with other classes) go inside folders directly under the `Content.Server`, `Content.Shared`, or `Content.Client` projects. There are folders for `Atmos`, `Botany`, `Research`, `Storage`, and a lot more. If a suitable folder doesn't exist, create one! Never put files directly into the top directory of the project.
```

Under the `Content.Server` project, there's a folder called `Sound`. This folder contains an aptly named `Components` folder. That seems like a good place to put our new component (and in fact, this is where the real `EmitSoundOnTriggerComponent` is located). Let's call our version `PlaySoundOnUseComponent`. Note: if you just copy paste this code in, it may not work, as you'll need to import various classes. Your IDE can do this for you.

Now let's just make the most basic component possible:

```csharp
// Content.Server/Sound/PlaySoundOnUseComponent.cs

namespace Content.Server.Sound;

[RegisterComponent]
public sealed partial class PlaySoundOnUseComponent : Component
{
}
```

All components must inherit from the `Component` class. If you want your component to be read in YAML, you'll have to add `[RegisterComponent]` above your class. Furthermore, all components must be marked `sealed` and `partial` for engine reasons. You don't have to worry too much about what they mean.

In our prototype above, you might recall that we added `Sprite`, not `SpriteComponent` to the ClownHorn prototype. That's because component 'names' are autogenerated using the class name. In this case, our component's name is `PlaySoundOnUse`, which is generated by just removing `Component` from the class name.

Now, let's go ahead and add PlaySoundOnUse to our prototype.

```admonish info
You must remove the `Component` part of the class suffix when using them in the prototype yaml. So `PlaySoundOnUseComponent` would be resolved as `PlaySoundOnUse` in the `components:` list in the yaml definition.
```

```yaml
- type: entity
  name: clown horn
  parent: BaseItem
  id: ClownHorn
  description: It goes honk honk!
  components:
  - type: Sprite
    sprite: Objects/Fun/bikehorn.rsi
    state: icon
  - type: PlaySoundOnUse
```

Well, this is boring; not only does our component not have any data, but it doesn't do anything either!

Let's add some data to our component. As you may have noticed above, the `Sprite` component on our bike horn has two fields listed: `sprite`, and `state`. Whatever you put in these fields will be passed into the component when it's created, and then our EntitySystem can use that data to do something.

In our case, we'll probably want a field called `sound` on our component, which stores a path to the sound to play when the entity is activated. It's pretty easy to do that:

```csharp
// Content.Server/Sound/PlaySoundOnUseComponent.cs

namespace Content.Server.Sound;

[RegisterComponent]
public sealed partial class PlaySoundOnUseComponent : Component
{
    [DataField]
    public string Sound = string.Empty;
}
```

All you need to do to create a field that can be modified in YAML is to add the `[DataField]` attribute, which holds the name of the field, and give it a default value, in this case `string.Empty`. Now, we can add our sound to our bike horn prototype:

```yaml
- type: entity
  name: clown horn
  parent: BaseItem
  id: ClownHorn
  description: It goes honk honk!
  components:
  - type: Sprite
    sprite: Objects/Fun/bikehorn.rsi
    state: icon
  - type: PlaySoundOnUse
    sound: /Audio/Items/bikehorn.ogg
```

Now we're getting somewhere! One thing to note is that the path here is relative to the `Resources` directory (which `SoundSystem` always assumes), and we're also assuming that the `Resources/Audio/Items/bikehorn.ogg` file is real. If you check, it is! But if a sound isn't present that you need, you can always add it yourself somewhere in the `Audio` folder.


## Creating our EntitySystem

Let's finally add some flavor to our bike horn by.. making it actually honk. As said previously, we'll need an `EntitySystem` which hooks into the `UseInHandEvent` and calls some code from there. Let's create our EntitySystem `PlaySoundOnUseSystem` in the same `Content.Server/Sound` folder:

```csharp
// Content.Server/Sound/PlaySoundOnUseSystem.cs

namespace Content.Server.Sound;
    
public sealed class PlaySoundOnUseSystem : EntitySystem
{

}
```

You'll notice that here, our system inherits from `EntitySystem`. This automatically registers it as a proper EntitySystem in the game and allows us to use some useful dependencies and override some methods to add behavior.

In order to subscribe to an event being raised, we'll need to override the system's `Initialize` method; this method is called when the EntitySystem is created.

In this method, we'll add a `SubscribeLocalEvent` call, and I'll explain the details after the fact.

```csharp
// Content.Server/Sound/PlaySoundOnUseSystem.cs

namespace Content.Server.Sound;

public sealed class PlaySoundOnUseSystem : EntitySystem
{
    public override void Initialize()
    {
        SubscribeLocalEvent<PlaySoundOnUseComponent, UseInHandEvent>(OnUseInHand);
    }
}
```

There's a lot going on in that method call! Basically, we're telling the game:

*"Whenever a UseInHandEvent is raised on an entity that has the PlaySoundOnUse component, I want you to call my OnUseInHand method."*

You've probably noticed that this code actually gives you an error, *because the method OnUseInHand doesn't exist yet*! Let's add that method. This is called an **event handler**, and event handlers require a specific set of arguments:

- The UID (unique identifier) of the entity the event was raised on
- The component that was specified in the subscription, so you can access its data and use that to change behavior
- The event itself, which contains useful data like the entity who activated the item.

If you're using an IDE, it might allow you to automatically create this method using *Alt+Enter*.

Here's what our class will look like now, with our new method:

```csharp
namespace Content.Server.Sound;

public sealed class PlaySoundOnUseSystem : EntitySystem
{
    [Dependency] private readonly SharedAudioSystem _audio = default!;
    
    public override void Initialize()
    {
        SubscribeLocalEvent<PlaySoundOnUseComponent, UseInHandEvent>(OnUseInHand);
    }

    private void OnUseInHand(Entity<PlaySoundOnUseComponent> ent, ref UseInHandEvent args)
    {

    }
}

```

We're almost there. Now, the method `OnUseInHand` will be called when we activate the item, and we can play our sound there.

Also, we've added `[Dependency] private readonly SharedAudioSystem` to class. It will allow us to play audio in modern way (instead of using obsolete `SoundSystem.Play`) further.

```csharp
private void OnUseInHand(Entity<PlaySoundOnUseComponent> ent, ref UseInHandEvent args)
{
    _audio.PlayPvs(ent.Comp.Sound, ent.Owner);
}
```

The `PlayPvs` method is useful for playing sounds. It has two arguments:

1. The sound to play.

In this case, we just pass it our `sound` field on our `PlaySoundOnUseComponent`. 

2. The source entity 

This is an optional argument that is used for positional audio. In our case, we want the sound to come from the horn, so we pass in the horn's Uid (which is the `Owner` property of the entity). If this arugment is not given, the sound is played globally and will be audible to all players.

If you compile the game and spawn our bike horn using the **F5** Entity Spawn Menu, you can try activating it in hand and--incredible! It plays the sound properly! Hopefully! If not, you might have messed something up in the YAML, or missed a method in the EntitySystem.

Also, `PlayPvs` automaticly manages distance filtering, so you don't have to worry about it.

## We're done here

With that, this tutorial is finished! If you want to continue experimenting with your newfound clown horn, here are some ideas:

- Try to implement clown horn using existing components. You can refer to skub.yml up this page
- Add a delay to the clicking through adding ```ItemCooldown``` to your prototype, and raising the `RefreshItemCooldownEvent`.
- Adjust the volume/variation of the sound played (see the `PlayPvs()` function's `audioParams` argumernt).
- Make the sound play when the bike horn is stepped on as well
    - This one is kind of hard and involves adding a lot of new data! Look at glass shards for an example.
- Make the bike horn do damage on attack using MeleeWeaponComponent
- Make the bike horn edible using FoodComponent and SolutionContainerComponent
- Add support for playing a random sound from a SoundCollection or SoundSpecifier rather than a single sound (the real EmitSoundOnUse does this, if you need pointers) 
- Dive into explosion code and give it a 5% chance to explode on each honk!

The world's your donk packet, and you've got a sizzling hot fire ready to cook it!
