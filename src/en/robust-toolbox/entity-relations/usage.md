# Entity Relations Usage guide

This document provides a general guide on how to use Entity Relations, without getting into details about how they work internally.

## Basic

A relation is defined by an `EntityRelation` struct, which can only be obtained through the `EntityManager` API (or `EntitySystem` proxy).

If an `EntityRelation` is stored in a component with `[AutoGenerateEntityRelations]` attribute, `[AutoRelationField]` attribute can be applied to the field to automatically generate a system that handles all necessary steps for handling deletion of the relation:

```C#
[RegisterComponent, AutoGenerateEntityRelations]
public sealed partial class FooComponent : Component
{
    [DataField, AutoRelationField]
    public EntityRelation MyBar;
}
```

### Setting a relation

To set the entity relation to some entity and store it in a component, you can do this in an `EntitySystem`:

```C#
private void OnUse(Entity<FooComponent> ent, ref UseInHandEvent args)
{
    SetRelation(ent.Owner, ref ent.Comp.MyBar, args.User);
}
```

In the example above, when an item with `FooComponent` is used in hand, it sets an entity relation from the item to the user entity.

When the user entity is deleted, the `EntityRelation` in `MyBar` field will be automatically set to `null`.

### Clearing a relation

To clear a relation to a certain entity, simply call the `ClearRelation` proxy method:

```C#
ClearRelation(ent.Owner,  ref ent.Comp.MyBar);
```

### Resolving a relation

`EntityRelation` struct is just a wrapper for `EntityUid?`, so in order to resolve it you just need to check the stored entity for null:

```C#
if (ent.Comp.MyBar.Entity != null)
{
    var uid = ent.Comp.MyBar.Entity;
    // From now on you can use the uid as usual
}
```

```admonish warning
After you resolve a relation, there are no longer any guarantees that the specified entity will remain valid throughout the execution of later code. Do not use the resolved `EntityUid` if somewhere inside the code it could be potentionally queued for deletion.
```

## Collections

Relations can also be stored as one of the basic C# collection types:
1. `List<EntityRelation>`
2. `HashSet<EntityRelation>`
3. `Dictionary<EntityRelation, T>`
4. `Dictionary<T, EntityRelation>`

In a component, they are defined just like the normal relation fields:

```C#
[RegisterComponent, AutoGenerateEntityRelations]
public sealed partial class FooComponent : Component
{
    [DataField, AutoRelationField]
    public List<EntityRelation> MyBars;
}
```

With collections, you can both 'assign' a collection of entities to a collection of relations, which effectively replaces all relations stored inside, and also 'add' new relations on top of already assigned ones:

```C#
private void SetFoo(Entity<FooComponent> ent, List<EntityUid> entities, EntityUid specialBar)
{
    // Clear all relations in MyBars, then Set relations to the provided entities.
    SetRelations(ent.Owner, ent.Comp.MyBars, entities);
    
    // Adds a relation to the list.
    AddRelation(ent.Owner, ent.Comp.MyBars, specialBar);
    
    // Adds a provided list of entities to the relations list.
    AddRelations(ent.Owner, ent.Comp.MyBars, entities);
}
```

### Collection options

As the first constructor argument the `[AutoRelationField]` attribute can accept a `EntityRelationCollectionOptions` enum. Available options are the following:
- `RemoveRelation` - fully removes the entry, including the additional data (key/value) in dictionaries. **Set by default**.
- `NullRelation` - sets a relation to null in `List<EntityRelation>`s and `Dictionary<T, EntityRelation>`s. Hashsets and key relation dictionaries behave the same way as `RemoveRelation`.

## Local relations

By default, Entity Relations are fully networked to be consistent between clients and server. For client-only or server-only features, all Entity Relation API has `Local` variations (e. g. `SetLocalRelation`).

```admonish danger
Before setting a local relation between two entities, both of them must have their `RemoveOnEmpty` flag in the `EntityRelationsComponent` set to false.
```

To ensure that local relations are supported for entities that combine both local and networked relations, use the following `EntityRelationsSystem` API method:

```C#
[Dependency] private EntityRelationsSystem _relations = default!;

[SubscribeLocalEvent]
private void OnFooInit(Entity<FooComponent> ent, ref MapInitEvent args)
{
    _relations.SetRemoveOnEmpty(ent.Owner, false);
}
```

This is needed because local relations are still stored in a networked component internally, therefore removing it on server when the networked relations are empty will break client-side local relations.
