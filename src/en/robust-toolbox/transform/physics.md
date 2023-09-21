# Physics

RobustToolbox's physics engine is based off of [Box2D](https://box2d.org/documentation/). It's encouraged that you familiarise yourself with the docs if you intend to do engine work.

The main changes are:
- **C# semantics**: RobustToolbox's version was originally based off of the Farseer port of Box2D.
- **Multithreading**: The contact constraints solver and the manifold generations are run in parallel internally.
- **Broadphase**: This is largely custom to fit SS14's needs though still uses the b2DynamicTree structure.
- **PhysicsComponent**: This has been tweaked to fit better with the rest of RobustToolbox, e.g. the eventbus and networking.

An entity with physics is comprised of a PhysicsComponent and a FixturesComponent. JointsComponent may also be present as well though is only present when an entity also has physics joints. FixturesComponent stores the fixtures, which are essentially sub-bodies within the entity, JointsComponent stores the joints, and PhysicsComponent stores everything else.

# How the physics pipeline works
1. All of the physics controllers are run. This applies any external forces to the physics sim such as player inputs for movements, top-down tile friction, etc.
2. At this point each physics map is stepped. The first part is to find all of the broadphase contacts for all the entities that have moved or are otherwise relevant (via TouchProxies). We check for some basic details to determine if 2 bodies can collide, e.g. their collision layers / masks, via PreventCollideEvent, joints disabling it, etc.
3. We now check over all of our contacts and determine which no longer overlap in broadphase and cull them.
4. Narrowphase is now run. For all contacts that are still relevant we determine if they actually overlap which is expensive. This is run via ManifoldManager. If overlap starts or stops a StartCollideEvent / EndCollideEvent is issued.
5. For all awake bodies on a particular map we create what are called islands. The easiest way to think of this is we take out an awake body and then pathfind through all of its contacts and joints as much as we can. Then, we repeat this process for the next awake body until we have all of the islands we need.
6. Each island now has all of its bodies solved.
7. Once solving is done we apply the data back onto the TransformComponent of every body and issue MoveEvents all at once.

# Commands

`physics <overlay>` provides many useful overlays for debugging physics.

`showchunkbb` shows all of the grid fixtures.

# Continuous Collision Detection (CCD)

The physics engine does not support CCD at this time but may at some point in the future once it's decided what to support.

# Useful CVars

**angsleeptol**
The maximum angular velocity a body is allowed to have to be eligible for sleeping

**linsleeptol**
The maximum linear velocity a body is allowed to have to be eligible for sleeping

**sleepallowed**
Are physics bodies allowed to sleep. Not recommended to turn this off.


# PhysicsComponent
This holds of all of the physics data for a particular entity. One way to think of how Box2D bodies work is that they are comprised of smaller bodies, the Fixtures (e.g. one fixture for an arm hitbox, one for the torso, etc.), and PhysicsComponent is the overall entity.

**Mass:**
The overall mass of a body. This comprises the mass of all of its fixtures.

**InvMass:**
Inverse mass. This is used in the solver internally as it's faster than using Mass.

**Inertia:**
How much force is required to rotate a body.

**InvI:**
Inverse inertia.

**LocalCenter:**
This is the centre of mass for a body. This is calculated based on the position of all the fixtures relative to the body assuming no rotation. `physics com` shows this for grids and for bodies.

**FixedRotation:**
Setting this to true prevents the body's angularvelocity from changing.

**LinearDamping:**
This is the percentage (where 0.2 corresponds to 20%) that a body's LinearVelocity decreases every tick.

**AngularDamping:**
This is the percentage (where 0.2 corresponds to 20%) that a body's AngularVelocity decreases every tick.

**Restitution:**
How much "bounce" a body has on collision. 1.0 corresponds to full bounce and 0.0 is no bounce. This is mixed between both bodies in the contact.

**Friction:**
How much friction applies for a contact; this is also mixed between the two bodies. Note that this does not correspond to top-down friction which is artificial and does not involve contacts.

# FixturesComponent
Fixtures describe the shape and material properties of entities for purposes of collision detection and other behaviors. They are derived from [Box2D fixtures](https://www.iforce2d.net/b2dtut/fixtures).

Fixtures that are not `hard` do not cause an actual collison, but still raise a collision event. This is useful for implementing things like slipperiness.

Each fixture is a member of any number of collision layers (field `layer`). Each fixture also has any number of collision masks (field `mask`). Entity *A* collides with entity *B* if *A*'s `mask`s intersect with *B*'s `layer`s. A list of layers are defined in [Content.Shared/Physics/CollisionGroup.cs](https://github.com/space-wizards/space-station-14/blob/master/Content.Shared/Physics/CollisionGroup.cs).

# CollideOnAnchorComponent
This is a performance-related component. It toggles (on or off via datafield) a body's collision when its anchoring state changes.

# CollisionWakeComponent
This is a performance-related component. It turns a body's collision off when it's asleep and on a grid with no joints attached. This is primarily targeted at SS14.

# VirtualControllers
To apply continuous external forces to a sim, i.e. player movement, VirtualControllers should be used. These are run at the start and end of a physics step and allow you to make changes to physics bodies.

If you need to apply 1-off things, like a single impulse, you can just call the methods like ApplyLinearImpulse directly.

# Contacts
These are created whenever 2 bodies (specifically 2 fixtures) overlap via broadphase. The Enabled property is set to true or false as their narrowphases overlap. If their broadphases no longer overlap then the contact is returned to the pool.

# Joints
These apply constraints between 2 bodies, such as a DistanceJoint preventing them from moving too far from each other. Use JointSystem if you wish to create them.

# Events
Please note that the below events are not raised recursively for performance reasons. If your entity is sitting still relative to its parent but the parent is moving then no MoveEvent will be issued for example.

**MoveEvent:**
Raised any time the EntityCoordinates / LocalPosition for an entity changes. This also applies for parent changes.

**RotateEvent:**
Raised any time an entity's LocalRotation changes.

**EntParentChangedMessage:**
Raised when an entity's transform parent changes.

**CollisionChangeEvent:**
Raised whenever CanCollide is toggled on or off for a body. This is also raised when it spawns.

**PreventCollideEvent:**
Raised whenever 2 bodies attempt to overlap via broadphase. **This should only be used for blocking 1 specific entity from colliding and not for 2 groups of entities from colliding.** If you wish to block 2 entire groups then use collision masks / layers.

<!-- TODO All the fixture and bodytype events etc. -->

# Debugging

Below is a list of common issues and how to solve them:

Q. My movement seems slower than normal after a change.
A. Most of the time this means TileFrictionController is running before MoverController instead of after and the tile friction is being applied to the mob.

Q. My mob rubs up against something solid then teleports through.
A. This means the client thinks the body is hard-collidable but the server doesn't and you have a mispredict.

Q. My mob rubberbands up against something solid.
A. This means the server thinks the body is hard-collidable but the client doesn't and you have a mispredict.

Q. I can only move a little bit then get moved back to my spot
A. This is also a mispredict where the client thinks it can move but the server doesn't.

Q. My input is delayed
A. This is also a mispredict where the server thinks the client can move but the client doesn't.

# Glossary

**Constraints:**
A physics sim only applies forces and the likes to bodies with no consideration for whether the body should go through a wall. Constraints are what prevent this from occurring. Box2D doesn't use the term but contacts and joints are all constraints. Some other physics engines lump them in the same umbrella and use the term.

**Physics Island:**
We solve physics via islands instead of all bodies sequentiall for stack sleeping reasons. If parts of a stack could sleep while the rest was awake then it would take a long time to settle, if at all. When all bodies have to go to sleep at the same time it makes it much more stable.

**Sleeping:**
Physics bodies stop being processed, go to sleep, after a time for performance reasons. This behaviour can be adjusted (the velocity tolerance and the time to sleep) or toggled via cvar.
