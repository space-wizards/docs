# Entity Relations

## Deleted Entity Reference problem

Imagine this: a player spawns 2 portals, then one of the portals is closed. If the second portal wasn't informed about the deletion of the first one, second portal's component will store a reference to an entity that was deleted.

This is, obviously, a problem, since Robust Toolbox assumes that all `EntityUid` passed around the code are valid, therefore an invalid entity reference causes many, many errors to appear in case of an inproper data reset.

### The solution: Relations system

To solve the issue with invalid entity references, a terminating entity has to simply inform all other objects that reference to it that the `EntityUid` they are holding is about to become invalid.

That solution is called **Relations system** - entities are linked using event subscriptions with a marker component to solve invalid references.

### Old-school implementation

Previously, Space Station 14 was solving the issue with invalid entity references like this:
- Add 2 components to entities A and B that have to be linked together
- Store A `EntityUid` in B, and B `EntityUid` in A
- Add an event subscription to clear the reference of the opposite entity on component's termination for both entities

```csharp
[RegisterComponent]
public sealed partial class FooComponent : Component
{
    [DataField] public EntityUid? MyBar;
}

[RegisterComponent]
public sealed partial class BarComponent : Component
{
    [DataField] public EntityUid? MyFoo;
}

public sealed partial class FooBarSystem : EntitySystem 
{
    [SubscribeLocalEvent]
    private void OnFooShutdown(Entity<FooComponent> ent, ref ComponentShutdown args)
    {
        if (TryComp<BarComponent>(ent.Comp.MyBar, out var barComp))
            barComp.MyFoo = null;
    }
    
    [SubscribeLocalEvent]
    private void OnBarShutdown(Entity<BarComponent> ent, ref ComponentShutdown args)
    {
        if (TryComp<FooComponent>(ent.Comp.MyFoo, out var fooComp))
            fooComp.MyBar = null;
    }
}
```

This is a working way to solve the problem, and it is the most correct one since it allows to do run any code when a related entity is deleted, but the main issue with this solution is *boilerplate*. For every single link between 2 entities, or a link between one parent and multiple children entities, new components and systems and event subscriptions have to be made manually, which is slow, annoying, and may still introduce errors in case if the code was incorrect.

## Robust Toolbox's Entity Relations

Robust Toolbox solves the issue with boilerplate of Entity Relations system by using automated code generators and a general component for all relations.

### Storage

All Entity Relations are stored in `EntityRelation` structs. It's a wrapper around `EntityUid?` with restricted access - you can't create new EntityRelations manually, and have to use `EntityManager`'s API instead.

When a relation between two entities is assigned to a field, `EntityRelationsComponent` gets added to both entities. Inside, the said component stores all entities that reference the owner entity in a list, which allows to safely add and remove relations between two entities even if it's done multiple times through different components.

After the relation was set successfully, the resulting `EntityRelation` struct is stored in the entity that initiated the relation, allowing the code to safely access the entity stored inside by simply checking if it's null or not.

### Cleanup

When an entity with `EntityRelationsComponent` is terminating, it raises an event to all entities that relate to it in order to clean up a reference to that specific entity in all their components. After that, any entity system subscribing to the component and a cleanup event can fix the relations by setting the stored entity to null.

A system that handles the cleanup event can be generated automatically by applying the `[AutoGenerateEntityRelations]` attribute to the component and `[AutoRelationField]` to all data fields with `EntityRelation`s. You can also decide to not use an auto-generated system, you can handle the relation deletion event manually.

### Networking

By default, the state of `EntityRelationsComponent` is networked to all clients on each API method call. You can pass a `dirty: false` as a parameter to prevent the dirtying from happening, which may be useful for server-side code or conditional networking for clients.

### Component Shutdown

Components shutdowns are handled a bit differently from entity deletion.

When a component that contains some `EntityRelation`s is shutting down, it's important to clear all relations stored in it, so that related entities don't hold a reference that will never be destroyed.

`[AutoGenerateEntityRelations]` automatically generates a shutdown event for the component it's applied. This however, prevents content from implementing a custom shutdown event, so to solve that the `shutownEvent: false` parameter can be passed into the attribute to prevent it from generating the event automatically. In that case at the end of a custom shutdown method it's **highly recommended** to call the `FooComponent.ClearComponentRelations()` auto-generated static method to prevent permanent references from occuring.

When `EntityRelationsComponent` itself shuts down while the entity continues to run, it not only raises a deletion event for other entities to handle, but also raises a special Relation shutdown event on itself to clear *all* `EntityRelation`s from all fields. This allows to detach an entity from the simulation as safe as technically possible without deleting it.
