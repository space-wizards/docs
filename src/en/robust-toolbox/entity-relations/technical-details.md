# Entity Relations Technical details

This document explains how exactly entity relations work under the hood.

## Definitions

- `EntityRelationsComponent` - engine component that stores a list of entities this entity is linking to/linked by. The networked and client/server side local lists are separated.
- `AutoGenerateEntityRelationsAttribute` - attribute applied to content components that automatically generates a system for handling entity relations.
- `AutoRelationField` - attribute applied to fields in content components to mark them for the code generator and allow them to be automatically cleared when the relation inside is deleted.
- `EntityRelationsSystem` - an engine system that provides the API methods to change specific flags in `EntityRelationsComponent`.
- **Content Component** - in this article will be reffering to a user-made component that has a `AutoGenerateEntityRelationsAttribute` and contains data fields with `EntityRelation` structs.

## Main pipeline

### Assignment

When asssigning an Entity Relation between two entities, `EntityRelationsComponent` is ensured on both and links to both entities are added to their internal lists.

### Deletion

When one of the entities gets deleted, it raises `EntityRelationDeleteEvent` that is automatically handled by the system that was automatically generated for each content component with `AutoGenerateEntityRelationsAttribute`. Here it checks if the relation exists and sets it to `null` if it matches.

### Content Component removal

When a Content Component is removed, it automatically clears all of relations that are stored in its fields.

This is done to prevent 'dead' relations that point only in one direction from appearing.

```admonish danger
[AutoGenerateEntityRelations] attribute does an automatic `ComponentRemove` subscription for the component it's applied to. If you really need to handle this event manually, you will have to implement Entity Relations handling manually.
```

### `EntityRelationsComponent` removal

There's also an edge case where the `EntityRelationsComponent` itself is removed on an entity. In that case a special `EntityRelationShutdownEvent` is raised, which sets all relations in all Content Components to `null`.

This also may be useful if an entity must be manually cut from the simulation entirely, for example to be explicitly saved without having to include the relations using `MapLoaderSystem`.


## Custom Entity Relations handling

### Use cases

Some of the common reasons why custom relation handling may be needed are:
- Additional action must be done when a specific Entity Relation is cleared
- `ComponentRemove` subscription is explicitly needed in content

To implement Custom Entity Relations handling, you must explicitly handle the 3 following events on your Content Component in your own system:
1. `EntityRelationDeleteEvent` - while handling this event, the component clear any references to the provided `Relation`.
2. `ComponentRemove` - must call `ClearRelation` EntitySystem proxy method on every `EntityRelation` field of the component
3. `EntityRelationShutdownEvent` - must set all `EntityRelation` fields to `null`.
