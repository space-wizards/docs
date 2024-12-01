# ECS Events
Events are an extension to ECS which allows for lower complexity systems. Allowing, systems to have minimal areas of responsibility while interacting with low code coupling.

### Events, subscriptions and methods
Entity Systems use *event subscriptions* to receive callbacks when certain things happen.
For example, entities with a particular component subscribe to receive a callback when a component of a certain type gets initialized, etc.
Systems can also have public methods that other entity systems can call, and they may raise events to communicate things. Generally, public methods will take entity UIDs, components and data as arguments.

### Creation and use

Classes that inherit from EntitySystem, or an existing entity system, will automatically be created and used by the engine when the game is run.
These classes are [singletons](https://gameprogrammingpatterns.com/singleton.html), meaning that only one instance of the entity system exists at once.

### Lifetime
Entity Systems have different lifetimes on the server and the client:
On the server, the lifetime of entity systems is the same as the program.

But on the client, Entity Systems will be created and initialized upon connecting to a server, and shutdown then removed when the client disconnects from the server. For this reason, handle Entity System shutdown cleanup very carefully on the client.

### Inter-dependencies

Entity Systems can hold dependencies to other entity systems, using the `[Dependency]` attribute, just like with [IoC managers](../ioc.md). This is preferred over getting other entity systems manually and caching them in a system field, or getting dependant systems on the fly in methods.
Something to note, entity system dependencies can only exist in entity systems.

Example:

```csharp
public sealed class BarSystem : EntitySystem
{
    public void Doo()
    {
        // Some logic here
    }

    public void Hicky()
    {
        // Some logic here
    }
}

public sealed class FooSystem : EntitySystem
{
    // This will be automatically set when the system is created.
    [Dependency] private readonly BarSystem _barSystem = default!;

     // Regular IoC manager dependencies also work here
    [Dependency] private readonly IPlayerManager _playerManager = default!;

    public override void Initialize()
    {
        // This works in initialize, dependencies have been resolved already.
        _barSystem.Doo();
    }

    public void MyFunnyMethod()
    {
        _barSystem.Hicky();
    }
}

```


## Events
Events allow entity systems to communicate between themselves without explicitly coupling them.

There are two ways to raise (and subscribe to) an event in RobustToolbox; these are directed events and broadcast events.

### Directed events
Directed events are raised on a specific entity. If any number of event subscriptions match the event and one of the components on the entity, those will get called back. The order in which they're called back can be specified explicitly when subscribing to the directed event, if needed (see "Sorted events").
This kind of event is usually preferred; they are much more performant. All lifestage events are directed (see [lifestage](#lifestage-event)).

### Broadcast events
Broadcast events are raised without being bound to any specific entity (unless the event instance itself specifies it! But even in that case it's still not fully "directed").
Entity systems subscribe to these events. Subscribed entity systems get a callback each time the event is raised.

### Sidenote: Sorted events
Both directed and broadcast event subscriptions can specify an ordering.
More specifically, events can specify which types (entity systems) will handle the event before and after the subscribing entity system.

If the "before" and "after" arrays are null, the event handling will not take sorting into account for an entity system.
Sorted event subscriptions are less performant so should be used only when needed.

## Event patterns

Below are event patterns; these are common ways to program events. This is not an exhaustive list of event programing methodology. These can be deviated from when creating events but will cover most cases.


### Immutable events
These events are immutable - that is, the contents of the event, its fields, cannot be altered.

#### Immutable event patterns
- [**Lifestage**](#lifestage-event)
- [**Informative**](#informative-event)

#### Lifestage event
This kind of event is created by the engine. Lifestage events are always directed.
The events inform the subscriber of a component lifetime event.

- **ComponentAdd** - The component has been added to the entity.
- **ComponentInit** - The component has been initialized.
- **ComponentStartup** - The component has been started up.
- **ComponentShutdown** - The component has been shut down.
- **ComponentRemove** - The component is about to be removed.

#### Informative event
This kind of event informs the subscriber that something has happened.
For example: An event raised whenever an entity is anchored by a player, an event raised whenever a mob has died, ...

### Mutable events
These events can have both immutable fields and mutable fields.
Entity Systems and handlers are free to change the mutable fields to communicate things to the event raiser such as the result of an action, special data, etc.

#### Mutable event patterns
- [**Cancellable**](#cancellable-event)
- [**Handled**](#handled-event)
- [**Ensuring**](#ensuring-event)
- [**Method**](#method-event)
- [**Manually sorted**](#manually-sorted-events)

#### Cancellable event
Also known as "Attempt events".
These events are usually raised to allow other entity systems to cancel something from happening.
For example, when a player anchors a machine an implantation may raise an anchoring attempt event that others entity systems can cancel if the tile is occupied, if the player mob is incapable of anchoring, etc. These events' instance usually have a "Cancelled" mutable field that can be set to true by entity systems to cancel the action or event. Other entity systems are free to uncancel them, but this usually would be considered unnessary complexity.

Events that inherit `CancellableEntityEventArgs` are cancelable.

#### Handled event
These events are meant to be handled by a single entity system. They have a "Handled" mutable field which denotes whether they have been handled already or not. Other entity systems need to cooperate and only handle them if they have not been handled before. Handled events are a variant of the [*method event*]().

Events that inherit `HandledEntityEventArgs` are handled.

#### Ensuring event
This event is essentially a *handled event*, the only thing that changes is how entity systems deal with it. This kind of event performs an operation on an entity, *ensuring* that it will have a certain component. If it doesn't have it, it will be added by the entity system handling it.
This pattern works by raising a handled event, both directed and broadcast.
It works because directed events are always raised before broadcast events.

The directed subscription will always set the event as handled, and perform some operation.
The broadcast subscription, on the same entity system, does nothing if the event has been handled. If it hasn't been handled, however, it adds the component to the entity and manually calls the directed handler to perform the operation.

#### Method event

**THIS PATTERN IS HIGHLY COMPLEX**
In most cases methods on entity systems can be used instead.

This type of event can have "input" fields, which are immutable and set by the event raiser,
"output" fields, which are mutable and set by the event handler, and
"input/output" fields, which are mutable, and able to be set by the caller and receivers.

For example, stack splitting uses (*not anymore since the anti-method event revolt of 2021*) a (directed) event which has an amount as the input field, and a nullable entity for the newly created split stack as the output field.
However, broadcast events that follow this pattern are also very useful: to create a stack entity of a specific stack type, raise a broadcast event with the stack type as the input, and get an entity as the output.

This kind of event is perfect for certain complex cases, where multiple entity systems need to perform logic when an event is raised, similar to regular old method calls. This allows entity systems to communicate without any kind of coupling, while keeping things modular and extensible in a way that component logic would not be. This pattern can extend functionality without having to modify any existing code, as events can be intercepted, or subscribed to.

### Manually Sorted events

**THIS IS AN OLD PATTERN; EVENT SORTING COVERS MOST CASES OF MANUALLY SORTED EVENTS**

An event sorting system has been added after this was written. That system is designed to resolve the same issues that this system addresses. with less dev

Sometimes, event subscriptions need to be sorted into multiple priorities. Adding this to the underlying directed event system is not possible; however, a priority system can be created by hand, for an event.

Instead of creating a single event create two or more events.

- BeforeDooHickyEvent
- DooHickyEvent
- AfterDooHickyEvent

As the event names imply, these get raised in order, creating a neat priority system.
This patten can even mix with the *handled event* pattern to stop raising the next priority events if the prior one has been handled already.

## Event creation best practices
- Event class names should always end in "Event", never "Message" or anything else.

- If an event involves an entity and is broadcast, it should have a property/field that references the entity. `RaiseLocalEvent()` broadcasts the event by default unless otherwise specified. This is very important if broadcast subscriptions interact with an entity.

- Input parameters for the event should always be set in the constructor. Optional input parameters too, use optional arguments for those.

- Document event class properly. Write what it does, or what it's supposed to represent. If a property is meant to be an input and/or output parameter, specify so in a comment.
