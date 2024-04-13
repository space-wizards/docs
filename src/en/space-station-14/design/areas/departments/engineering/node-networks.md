# Node Networks

This is not my system, it's a documentation of someone else's.
<!--And this isn't my write-up, I just ported it from HackMD-->

`Node`s, `NodeContainer`s and `INodeGroup`s are the trinity of pieces that make up the 'connectivity layer' in SS14. This is used for pipes and wires (power).

The table of contents of this should provide a high-level overview of the system.

## `NodeContainer` : The component in entities that interact with the node system

`NodeContainer` is the component that whatever device you're building will be interacting with to access the node system.

`Content.Server.GameObjects.Components.Atmos.Piping.Pumps.BasePumpComponent` should be considered the "reference code" for a component that needs to use Nodes in a way that isn't *too* complex, but requires thought due to it not being as "universally connected" as a WireNet device.

## `Node` subclasses : Defines connectivity between itself and other nodes

A `Node` is a specific connection point on an entity.

A `Node` instance is a specific connection point, and the behaviour of that instance defines how that connection point connects to other nodes.

For example, each side of a pump is a separate `PipeNode` that only connects in that direction, but both sides of a pipe are a single `PipeNode` that connects in both directions.

But `AdjacentNode` doesn't have any way to define such a direction, and just connects to all adjacent nodes of the same type.

All `Node`s have a property called `NodeGroupID`, exposed in the prototype as `nodeGroupID`, that determines compatibility between `Node`s and the type of `INodeGroup` that it uses.

Implementing `GetReachableNodes` controls the discovery of `Node`s, while calling `RefreshNodeGroup` is a way to manually force a refresh of this node.

Note that `AdjacentNode`'s code doesn't actually check `NodeGroupID` - this check is performed by the `Node` base class in `GetReachableCompatibleNodes`. This implies `GetReachableNodes` in general does not need to perform this check, so only perform the necessary checks, such as with `PipeNode` which can only ever connect to other `PipeNode`s because.

I am unsure if having an asymmetric connection will cause problems in practice, so try not to create a situation where this can occur. (i.e. something that acts like `PipeNode` next to `AdjacentNode` - `AdjacentNode` will connect to `PipeNode` but not vice versa)

To actually use the `Node` for anything useful, the `Node` needs to either be fed information about it's parent network via the `INodeGroup`, which has overridable functions for when nodes are added and removed, or whatever is accessing it needs to use it's `NodeGroup` property, which has no update callbacks and always has a type of `INodeGroup`.

Though this should be clear already: `Node`s within an entity do not automatically connect to each other unless this is forced to occur via their connection behaviour (directly or indirectly, like via a player connecting a pump to itself).

Finally, again, if you just need "connect to adjacent entities of the same group" behaviour, use `AdjacentNode` as shown below:

```yml
  - type: NodeContainer
    nodes:
    - !type:AdjacentNode
      nodeGroupID: Apc
    - !type:AdjacentNode
      nodeGroupID: WireNet
```

## `INodeGroup` : Represents a connected group of `Node`s, and contains group behaviour

`INodeGroup` instances represent a connected group of `Node`s.

This implies that any `Node` in the group is connected to any other `Node`. (Not necessarily directly, but not going through any "explicit separators" such as pumps in the PipeNet system.)

The `INodeGroup` implementation is chosen via the `Node`'s `NodeGroupID`. See `NodeGroupFactory.cs` (described below) for more details.

Note that all `INodeGroup` implementations at present extend `BaseNodeGroup`.

## `NodeGroupFactory.cs` : Creates `INodeGroup`s for `Node`s and houses the `NodeGroupID` enum

`NodeGroupFactory.cs` contains the network types in the `NodeGroupID` enum.

`NodeGroupID`s are mapped to `INodeGroup` implementations via the NodeGroup reflection attribute (such as `[NodeGroup(NodeGroupID.Pipe)]` in `IPipeNet.cs`).

Multiple `NodeGroupID`s may be mapped to one `NodeGroup` implementation.

`NodeGroupFactory` (accessed via IoC as INodeGroupFactory) has one member of importance, `MakeNodeGroup`. (There is also `Initialize`, which is called from the server EntryPoint, and is used to scan for classes using reflection.)

`MakeNodeGroup` creates a new `INodeGroup` from a `Node`, getting the type from `Node.NodeGroupID`.

## Appendix: Some Power Group IDs:

+ `Apc`: APC Extension Cables -> `ApcNetNodeGroup`
+ `MVPower`: MV Wire -> `PowerNetNodeGroup`
+ `HVPower`: HV Wire -> `PowerNetNodeGroup`
