# Net Entities

## Quick guide

If you use the sourcegen comp states (`AutoGenerateComponentState` / `AutoNetworkField`) then most of this is done for you.

If you need to network an EntityUid you should call `GetNetEntity` on the sender side (typically server) and `TryGetEntity` / `EnsureEntity` on the client side. If you're inside of a component state this should be `EnsureEntity<TComp>` but if it's a message you should use `TryGetEntity`.

There is a possibility the client fails to resolve an entity (as there would be with any PVS solution) sent via a message so if you want resilience around this you should use component states or otherwise redesign your code.

## Why EntityUid and NetEntity are different
Client and server can have different entities. Client spawns its own entities for effects such as hitscan lasers, item pickups, etc.

Previously we marked this entity with the 28th bitflag however in the interest of performance we want to place entities into an array instead which means this would require a significant amount of memory to accomplish.

As such the local EntityUid and the networked version will naturally desync as client and server have knowledge of different entities which is where NetEntity comes in.

## Migration

### Networking

EntityUid is no longer marked as NetSerializable. Any time it will try to get serialized NetSerializer will now thrown an exception.

If you wish to network an EntityUid or EntityCoordinates then EntityManager contains methods to do so:

- GetEntity
- GetNetEntity
- GetCoordinates
- GetNetCoordinates
- TryGetEntity
- TryGetNetEntity
- EnsureEntity\<T> (where T is the relevant component).

It also has version for HashSets and Lists. EntitySystems also have proxy methods for these.

You should avoid storing NetEntity on components long-term and opt to use EntityUid instead. NetEntity also won't serialize to yaml.

If you have an existing data structure that's a pain to migrate (for example DoAfterEvents) then placing the EntityUid DataField and NetEntity both on the event (marking the EntityUid as NonSerialized) is a suitable intermediary.

### Commands

Commands should be updated to use NetEntity instead as integers will be parsed as NetEntity instead of EntityUid.