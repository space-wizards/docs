# Entity Coordinates

EntityCoordinates are a new and hip way to represent an entity's position **relative** to another entity. They consist of an EntityUid, an X coordinate and a Y coordinate.

Unlike GridCoordinates, these coordinates aren't bound to a specific grid: They can be used to represent the position of entities attached to the map, attached to a specific grid, attached to another entity, or entities without a parent.

Due to the nature of these coordinates, they can become invalid under certain circumstances,
like when the EntityUid is invalid or when its entity is deleted.

### Gotchas

- If an entity doesn't have a parent, their EntityCoordinates points to itself with offset 0.
This is the case with map entities, or entities that don't have a parent entity.

- When an entity becomes attached to a new parent (for example when entering a locker or buckling yourself to a chair) your EntityCoordinates now become relative to that entity.
In the case of lockers, disposals and chairs this means your new relative position is (0, 0) since you're standing in the same position as your parent.

- If you get a grid entity's EntityCoordinates and then call the `GetGridId()` method on it, you'll always get `GridId.Invalid`. This is because grids can NEVER have another grid as an ancestor, and `GetGridId` returns the grid Id the parent is on. In the case of maps, this is always `GridId.Invalid`. This also happens when you attempt to get the grid an entity without a parent or parented to the map is on.

- Entities in space have no parent grid, thus will return `GridId.Invalid` when calling `GetGridId()`. If your logic should work in space as well as on a grid, make sure you aren't relying on `GetGridId()` being valid.

- Most EntityCoordinates methods require you to pass `IEntityManager` and/or `IMapManager` as arguments. Since EntityCoordinates methods are very low level, performing IoC resolves for those would be very costly. Please try to cache these dependencies instead of resolving them every time you work with EntityCoordinates, as not doing so could hurt performance.