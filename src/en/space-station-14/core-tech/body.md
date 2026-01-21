# Body

Body is the domain of mobs that are person- or animal-shaped in Space Station 14.

This is a topographical document, written to give the reader the "lay of the land" of the design and code that lives underneath. Please see the Body folder itself for detailed surveys of each component part of this metasystem.

**Last Update** X of X, 20XX

### Wait, what's an 'Entity'?

Sometimes the word "entity" is used below. This essentially means "a specific thing". For example, "mouse (123)" is a _specific_ mouse. There might be twenty mice on the station, and each are entities in their own right, because they all have their own unique ID.

### What's a 'Container'?

Entities have to live somewhere. When they live in some other Entity - for example, when Urist's gun is inside Urist's backpack, which is being worn by Urist - the entity they live inside uses a Container to store them.

## Top-Level Design

### What is a Mob?

A mob in Space Station 14 is an entity that a player can possess and play as. A mothroach, a sentient vending machine, and a Nuclear Operative Commander are all mobs. 

Most mobs can be "damaged". These are called "damageable".

### What's a 'Damageable' entity?

A damageable entity can can gain damage.

In many games, a thing might have a certain amount of "health", and dies when its health reaches zero. In Space Station 14, this is flipped arounnd. A completely healthy entity has 0 damage - it is **undamaged**.

When damage is caused to a damageable entity, it **gains damage**.

When an effect "repairs" or "heals" an entity, it really is just **reducing damage**.

### How do damageable mobs work?

Mobs have three **mob states** they can be in:
* Alive - the mob is currently not crit or dead. 
* Crit - the mob has taken enough damage to stop operating fully. This is usually an "unconscious" state, where mob itself can possibly reduce its own damage to return to being "alive".
* Dead - the mob has taken enough damage to shut down entirely. Dead mobs cannot restore themselves to being crit or alive and need help from outside sources. 

The dead state also can start a biological mob **rotting**, a timer that eventually makes the mob completely unhealable - it is an inert corpse.

As the definition of "alive" might hint at, the actual state a given mob is really in is decided by a lot more than their mob state. But for damage, mob state is at the core of the system.

If a mob takes a _really large_ amount of damage, the mob itself can be destroyed. This is called **gibbing**.

A damageable mob's **mob state** is controlled by the total damage it's taken. These are its **damage thresholds**. Crossing these thresholds in either direction will cause the mob to transition its state. 

A mob can move from alive to crit to dead easily by taking damage, but going backwards is different. A crit mob that has its damage removed will return to being alive. Once a mob has reached the dead state, it cannot return to being crit or alive without specific tools. For biological creatures in Space Station 14, this is the role of the **defibrulator** item and is called being **zapped**.

Not all mobs will use all three states. For example silicons - borgs - are either funcitoning or not, and therefore go from "alive" to "dead", reflecting that the borg shell that the brain is piloting has stopped functioning.

### The Body

Damage is tracked on the mob. But when a mob has a Body, its damage will be affected by internal entities inside the mob, not just by external sources.

When a mob with a Body gets hurt, sometimes it can heal the damage itself. Otherwise, medical items and reagents step in to bring the mob's damage down. 

Sometimes medicine is direct - for example, a bandage heals a certain amount of damage. Sometimes the medicine requires the Body to metabolize it, and the healing is a damage-over-time effect.

This is all orchestrated by the **Organs** of the Body.

Bodies are composed a **Body Part Root**, **Body Parts** and **Organs**.

### Body Part Root

The **Body Part Root** is usually described as the torso of the creature - it contains all the Body's entities inside of itself via a heirarchy. Many mobs only have a root body part - for example, mothroaches.

### Body parts

**Body Parts** are entities that act as individual parts of the body, such as the head, each arm, and each leg. The Body Part Root is also a Body Part. Body Parts can contain both Body Parts and Organs.

In principle, a body part is there to model things like "when Urist McHands somehow grows a pair of eyes in his left hand, and his left arm is chopped off, remove his left hand and those weird new eyes".

### Organs

Organs are entities that actually do things inside the Body. They do things like metabolizing chemicals, and handling breathing. These Organs can help or hurt the Body. Blood, vomit, chemicals, and even the link between the Body's mob and the player controlling them are things that these Organs control.

#### !!Important!!

At the moment, a lot of "Body" behaviour that sounds like it should be driven by an Organ is actually driven by some standalone system attached to the Body itself. Examples of this include stamina, hunger and thirst.

### How to Spawn Bodies

The Body is built when the mob spawns based on a template - a **Body Protoype**. 

A Body Prototype has a number of **Slots**. These contain a BodyPart, the Organs that BodyPart contains, and the **Connections** that the Slot has. For example, a human's torso might have a connection to the left arm, which itself has a connection to the left hand. 

Connections are uni-directional. As such, a Body can be thought of as a node tree of body parts and organs.

When spawning a Body, the Body itself is spawned as a container. This container contains the Body Part Root of the body, and that Body Part Root gains two containers, one for Body Parts and one for Organs. Those containers are then populated by the contents of the Body Part Root's slots. Instantiated Body Parts themselves will become a Container for their own Body Parts and Organs, and so on until the whole Body is spawned.

### Rotting

When a Body is dead, it begins to rot. Rotting is a staged process that turns a Body from a revivable mob into one that isn't coming back. Rotting can be slowed, but to halt and reverse rotting entirely requires reviving the corpse, which is done via healing the corpse's damage to below its death threshold and then reviving them with a defibrulator.

Rotting is a system that lives outside of the Body domain, although some Body systems do affect rotting.

### The Bloodstream and Chemstream

Most of the complexity that arises from Body arises from the internal chemical systems that powers Organ interaction. Mobs have a **Bloodstream**, which is the solution of blood inside the mob, and the **Chemstream**, which is the separate solution of chemicals that are inside the body. Manipulating these is the most common way Body Organs actually do anything. 

## Current State of Design

After most of the Body code was written, a rebuild of underlying medical and chemical code was attempted for multiple years. This rebuild was not ultimately completed, and the incomplete Body system has thus been powering the underlying medical and associated gameplay systems in the meantime. There are some initiatives to complete the Body work, which will allow for future gameplay such as surgery, complex injuries, and more variance in the average round in medbay.

### BodySystem

BodySystem is the EntitySystem that covers what behaviours an entity with BodyComponent has.

In general, the underlying systems that power the Body behaviours are referred to as "BodySystem", although the actual code is scattered far and wide across the codebase, in many different namespaces.

What BodySystem actually does is control how to build, modify and destroy a Body at runtime. Bodies are built off of BodyPrototypes that are specified in YAML. A Body is a Container of Containers, and those Containers are filled by Organs and BodyParts. A Body meets its ultimate end when it is gibbed, when its internal structure is replaced by a puddle of blood, chemicals and a pile of body part items.

A Body can have BodyParts added or removed at runtime.

A Body also keeps track of the number of legs it needs to move around with at full speed, even though this information is never actually used anywhere.

Outside of assembly and disassembly, BodySystem provides the API for external systems to actually find and alter BodyParts and Organs within the Body. Given the Body is a Container of Containers, the alternative is usually cumbersome looping and manual node tree searches to answer questions like "does Urist currently have any hands?".

The actual behaviours of any given Body beyond assembly and disassembly is instead provided by other components on the Body's mob, and the Organs the body contains.

## What BodyParts are Supposed To Do

BodyParts are supposed to be individual pieces of a body. These tend to map to limbs - the head, arms, legs, feet, torso, and hands of a mob. 

Each part is addable and removable other BodyParts. There is always a central BodyPart a Body has, called the "torso". BodyParts are contained in other BodyParts or the Body.

BodyParts can be symmetrical and ergo can have a "side" - left or right. They are also typed - a BodyPart might be a "LeftArm" or a "Tail".

BodyParts can sometimes be marked as "vital". A "vital" BodyPart cannot be removed from its host Body without killing the Body's mob, and the Body's mob cannot be revivied. This makes sense - every defibrilator in the universe can't bring back a Urist with a missing head.

## What Organs Are Supposed To Do

Organs are supposed to be individual agents inside a Body that do things. A few examples of Organs might include:
* The stomach
* The heart
* The liver
* The brain
* The spleen
* The eyes
* Each hand

and so on.

Organs allow for an Entity with a Body to do things that go beyond just being a corpse lying on the floor. For example, lungs are an Organ. The lungs breathe in gas from the atmosphere around the mob, the lungs saturate with breathable gas, and when saturated heal any airloss damage the Body's mob has taken. When the lungs do not have enough gas, they desaturate and cause airloss damage.

Organs are self-managing, ticking by on their own, but tend to obey the Body's metabolism rate. Metabolism is the speed by which the Body does things like digest food or convert chemicals in the bloodstream, and speeding up or slowing this down alters the speed Organs do things.

## What They Actually Do

BodyParts are almost completely unused after they are instantiated during the building of a mob's Body. There are commands to add and remove BodyParts from a mob - this can be used by an Admin to remove someone's hands, for example - but nothing in normal gameplay actually interacts with them outside of using them to organize the YAML needed to build a particular mob species. 

Organ behaviours are defined somewhat inconsistently, and sometimes not at all. For example:

* There are some functions of the overall Body that are controlled via "Organs". Breathing, eating and metabolizing chems are some examples. But these are often named inconsistently - breathing is handled by a "LungsComponent", but metabolizing reagents from the Body's chemical solutions is the "MetabolizerComponent". 
* Sometimes an organ is just there so that some other system does something if that organ is added or removed. For example, brain organs don't themselves control anything to do with the brain of a Body, but instead are just used as the entity chit for where a Player's mind ends up if the brain is ripped out of the Body.
* Implants are extremely similar to Organs in concept but do not share code. Implants are instead just stored inside a Container on the Body.
* Quite a few gameplay systems that interact with Body are not actually Organs. Movement speed, stamina and stunning are gameplay that is directly affected by Body - some chems increase stamina or movement speed - but are not actually tied into any organ in particular.
* Some gameplay systems that sound like they're Organs are actually not organs. The most notable of these is Hands, which despite being named after something a Body has is actually something that can be given to any mob. Another example is Eyes. Eyes even have their own damage model - via Blindable - that works on its own and only lightly interacts with Body. 
* Some organs that are implied to exist in-universe, like the mouth, just don't exist at all. The stomach, not the mouth, controls what a mob is capable of eating.