# NPCs

NPCs in SS14 use a hierarchical task network (HTN). The best reference to understand what this is from [gameaipro](http://www.gameaipro.com/GameAIPro/GameAIPro_Chapter12_Exploring_HTN_Planners_through_Example.pdf). The diagram on page 9 is especially useful.

## Quick Start

To get an NPC working:
1. Create a compound task. This comprises n branches where each branch comprises n tasks (compound or primitive) in sequence.
2. Add HTNComponent to an NPC.
3. Give a root task to the NPC. This must be a compound task.

Your NPC should now work.

## Blackboard
All of the relevant data for an NPC is stored on `NPCBlackboard`. This is a Dictionary<string, object>. Some data may be retrieved while planning as implemented as a switch case instead, e.g. if you wish to retrieve the coordinates of the blackboard's owner.

While planning in HTN effects may be applied to the blackboard which can potentially be rolled back, e.g. if the entity is moved during planning it may turn out the movemenet is not valid.

In practice this is stored on a temporary dictionary that may get cleared.

## Planning
The planner will try to decompose compound tasks until none remain and only valid primitive tasks are left. This also stores a record of what was traversed as a List<int>. The integer corresponds to what branch was taken for that compound task and the number of list entries is how far down we went with compound tasks.
  
If a plan is considered not to be valid then the state gets rolled back to the last decomposed compound task and it will try the next branch (and if that branch is not possible we recursively go up).
  
Effects are potentially returned from the `Plan` method on `HTNOperator`s. These also get re-applied during the plan's update for the same `HTNOperator` and are up to the relevant `HTNOperator` to re-use or discard this data.
  
A plan with a lower branch traversal (think like semver) is considered a better plan than one with a higher branch traversal.
  
You should also note that planning is time-sliced and may run across several ticks if it takes a particularly long time. At this stage it isn't multi-threaded.

## Tasks
A HTN is a tree comprising compound or primitive tasks. Compound tasks get "decomposed" further until only primitive tasks remain in the final plan.

**Compound tasks:**
- Have n branches.
- Each branch may have preconditions required to run.
- Each branch has n compound or primitive tasks

**Primitive tasks:**
- May have preconditions required to run.
- Have a "Plan" method that is only used during planning. This can potentially fail (outside of preconditions) and may also lead to further branch traversals.
- Have an operator which is the actual code that gets run during excecution.

You should note that tasks are fully re-useable across NPCs and the expectation is that common compound / primitive tasks are re-used where possible, e.g. for selecting a random wait time. This means NPC tasks are highly composable and even if an NPC may not be able to do a particular action, e.g. a xeno trying to pick up a gun, the branch just gets ignored and the next one is tried.
  
Something to note is that primitive and compound tasks are singletons and do not store any stateful data on themselves besides dependencies and what datafields may be required from the blackboard.
  
Tasks are implemented as follows in yaml, using turrets as an example:
```yaml
# -- Ranged --
# Tries to shoot a target in LOS in range.
- type: htnCompound
  id: TurretCompound
  branches:
  	# This is branch 0. If this branch is successful then the final plan will only include these 2 primitive tasks.
    - tasks:
        - id: PickRangedTargetPrimitive
        - id: RangedAttackTargetPrimitive
    # This is branch 1. This compound task gets pushed onto the stack and gets decomposed by trying each branch in order.
    - tasks:
        - id: IdleSpinCompound

# Spin to a random rotation and idle.
- type: htnCompound
  id: IdleSpinCompound
  branches:
  # This is branch 1, 0, as IdleSpinCompound is branch 1 on TurretCompound and this is branch 0 on IdleSpinCompound.
    - tasks:
        - id: WaitIdleTimePrimitive
    # Pick a new angle and spin there
  	# This is branch 1, 1.
    - tasks:
        - id: PickRandomRotationPrimitive
        - id: RotateToTargetPrimitive
        - id: SetIdleTimePrimitive
        - id: WaitIdleTimePrimitive


# Primitives
- type: htnPrimitive
  id: PickRandomRotationPrimitive
  # This is the actual code that gets run. It can be run during planning and also during an update. Some operators may only care about planning (such as this one) to select some data, whereas others may only care about running during update.
  operator: !type:PickRandomRotationOperator
  	# Operators will frequently take in a target blackboard key on where to retrieve their data.
    targetKey: RotateTarget
  
- type: htnPrimitive
  id: RotateToTargetPrimitive
  operator: !type:RotateToTargetOperator
    targetKey: RotateTarget
  
- type: htnPrimitive
  id: RandomIdleTimePrimitive
  operator: !type:RandomOperator
    targetKey: IdleTime
    minKey: MinimumIdleTime
    maxKey: MaximumIdleTime

- type: htnPrimitive
  id: WaitIdleTimePrimitive
  operator: !type:WaitOperator
    key: IdleTime
  preconditions:
    - !type:KeyExistsPrecondition
      key: IdleTime
```
  
## Updates
Most NPCs are updated when HTNOperators run; however, where complex systems are required, such as co-ordination between NPCs, then it is better to pass this off to a dedicated system and component. This also makes debugging easier.
  
## Collision Avoidance
This is handled via something called context steering.
Two arrays are made for n directions around the NPC (at the time of writing 12) and a weight is given to each direction on how desireable it is to go. This comprises an Interest array and a Danger array, with Danger being subtracted from Interest before determining the final movement direction.
  
A direction that moves closer to our goal (either a target or a pathfinding node) might be given a weight of 1 but a direction that moves towards an obstacle might be given a negative weight.
  
We also re-use this to avoid NPCs stacking as they have a danger weight added to directions that move closer to allies, as well as using it for combat movement (with a seek weight away from the target being given when melee is on cooldown).
  
See http://www.gameaipro.com/GameAIPro2/GameAIPro2_Chapter18_Context_Steering_Behavior-Driven_Steering_at_the_Macro_Scale.pdf for further reading.

## Pathfinder
Requests for pathfinding go through `PathfindingSystem`. These can be done async or via raising an event on the entity. These get deferred until the next Update and are run in parallel where their results are then dispatched synchronously (if they finished).
  
To look at the debug info for the relevant stages below information is available under the `pathfinding` command.
  
### Graph
For now pathfinding is only possible on grids. On certain events (e.g. static entities being spawned) this queues an update to the relevant chunk. Each graph that requires updates then queues these up and does the update infrequently (at the time of writing 0.45 seconds) as updating is expensive.
  
The graph update is as follows:
- Each dirty graph is updated sequentially, where each dirty chunk on the graph is updated in parallel.
- Each tile in the chunk is subdivided into 4x4 'breadcrumbs'. Each of these are like a mini-node on the graph and have the relevant data, e.g. collsiion mask, is there an airlock, is it breakable, etc.
- These mini-nodes are then combined, if they have the same data, on each tile into polygons. For example, a tile with just a wall on it will be 1 polygon, whereas one with 2 windoors on it may be 3 polygons (1 for the open space, and 1 for each windoor).
- This data is cross-referenced to the existing data. If it is the same then no changes occur. If it differs then we clear the existing data and any paths with this node are invalidated.
- All of these polygons are then connected to each other and we have a suitable graph that can be used for traversal.
  
### Portals
To connect 2 disparate polygons we require portals. These are created or removed via other systems and are handled outside of the update above. Portals don't have to be actual portals, for example docking ports create a portal from one graph to another which ensures the NPC can pathfind across them.
  
### Pathfinding
A* is used to get a path towards a goal and Breadth-First Search (BFS) is used to expand outwards.
  
Based on the relevant entity's pathflags a node may have different costs, e.g. if the entity can pry doors or not. When requesting a path you can pass these flags in.
  
## Commands
`npc` shows some buttons available that toggles other commands. This covers both NPC and pathfinding commands.
`showhtn` shows what NPCs are currently doing.