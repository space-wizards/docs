# Body

What is a spessman? A miserable little pile of Containers!

Body is the group of underlying simulation systems that drives mobs that are person- or animal-shaped in Space Station 14. A sentient vending machine does not have a Body. A dead mothroach does.

## Top-Level Overview

A mob in Space Station 14 is a thing that a player can possess and play as. A mothroach, a sentient vending machine, and a Nuclear Operative Commander are all mobs. A damageable thing is something that can can take damage. A ghost isn't damageable, but a wall is. 

When damage is caused to a damageable thing, it gains damage. A damageable mob's state is controlled by the total damage it's taken. These are its "damage thresholds". Crossing these thresholds will cause the mob to transition its "mob state" - alive, crit, and dead. A mob can transition to and from alive and crit, and can transition from either to being dead, but once a mob dies its internal systems shut down, and it needs some help from outside - usually via a zap from a defibrulator - to stop being dead.

When a damageable mob has a Body, not all the damage it takes will come from external sources. The Body has internal parts, called Organs. These act semi-independently from the Body, doing things like metabolizing chemicals and handling breathing. These organs can help or hurt the Body. Blood, vomit, chemicals, and even the link between the Body's mob and the player are things that these Organs control. Some things that sound like they should be managed by Organs are driven by the Body, such as hunger and thirst.

When a mob with a Body gets hurt, sometimes it can heal the damage itself. But in general medical items and reagents step in to bring that mob's damage down. Sometimes the medicine is direct - for example, a bandage that heals a certain amount of damage. Sometimes the medicine requires the Body to metabolize it, and the healing is a damage-over-time effect.

The Body primarily contains two things. These are Organs and BodyParts. BodyParts are individual parts of the body, such as the head, each arm, and each leg. A Body always has one root body part - the torso. BodyParts can contain both other BodyParts and Organs.

The Body is built when the mob spawns based on a template - a "Body Protoype". A Body Prototype has a number of Slots. Slots are a BodyPart, the Organs that BodyPart contains, and the connections that the Slot has. For example, a human's torso might have a connection to the left arm, which itself has a connection to the left hand. Connections are uni-directional. As such, a Body can be thought of as a node tree of body parts and organs.

When a Body is dead, it begins to rot. Rotting is a staged process that turns a Body from a revivable mob into one that isn't coming back. Rotting can be slowed, but to halt and reverse rotting entirely requires reviving the corpse, which is done via healing the corpse's damage to below its death threshold and then reviving them with a defibrulator.

Most of the complexity that arises from Body arises from the internal chemical systems that powers Organ interaction, and the inconsistency between the use of these systems and gameplay systems directly coded onto the Body. The Body has the concept of a "bloodstream", which is the solution of blood inside the Body, and the "chemstream", which is the solution of chemicals that are inside the body. Manipulating these is the most common way a Body actually does anything in SS14. However, many things that a Body does are actually coded directly onto the Body's entity. This can make it very confusing to maintain.

After most of the Body code was written, a rebuild of underlying medical and chemical code was attempted for multiple years. This rebuild was not ultimately completed, and the incomplete Body system has thus been powering the underlying medical and associated gameplay systems in the meantime. There are some initiatives to complete the BodySystem work, which will allow for future gameplay such as surgery, complex injuries, and more variance in the average round in medbay.

## What's this BodySystem anyway?

BodySystem is the central hub of the Body namespace. BodySystem is the EntitySystem that covers what behaviours an entity with BodyComponent has.

In general, the underlying systems that power the Body behaviours are referred to as "BodySystem", "Body", and so on, although they are actually scattered far and wide across the codebase, in many different namespaces.

What BodySystem actually does is control how to build, modify and destroy a Body at runtime. Bodies are built off of BodyPrototypes that are specified in YAML. A Body is a Container of Containers, and those Containers are filled by Organs and BodyParts. A Body meets its ultimate end when it is gibbed, when its internal structure is replaced by a puddle of blood, chemicals and a pile of body part items.

A Body can have BodyParts added or removed at runtime.

A Body also keeps track of the number of legs it needs to move around with at full speed, even though this information is never actually used anywhere.

Outside of assembly and disassembly, BodySystem provides the API for external systems to actually find and alter BodyParts and Organs within the Body. Given the Body is a Container of Containers, the alternative is usually cumbersome looping and manual node tree searches to answer questions like "does Urist currently have any hands?".

The actual behaviours of any given Body beyond assembly and disassembly is instead provided by other components on the Body's mob, and the Organs the body contains.

## What BodyParts are Supposed To Do

BodyParts are supposed to be individual pieces of a body. These tend to map to limbs - the head, arms, legs, feet, torso, and hands of a mob. 

Each part is addable and removable other BodyParts. There is always a central BodyPart a Body has, called the "torso". BodyParts are contained in other BodyParts or the Body.

BodyParts can be symmetrical and ergo can have a "side" - left or right. They are also typed - a BodyPart might be a "LeftArm" or a "Tail".

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

Organs can sometimes be marked as "vital". A "vital" Organ cannot be removed from its host Body without killing the Body's mob, and the Body's mob cannot be revivied.

## What They Actually Do

BodyParts are almost completely unused after they are instantiated during the building of a mob's Body. There are commands to add and remove BodyParts from a mob - this can be used by an Admin to remove someone's hands, for example - but nothing in normal gameplay actually interacts with them outside of using them to organize the YAML needed to build a particular mob species. 

Organs are handled extremely inconsistently. 

* There are some functions of the overall Body that are controlled via "Organs". Breathing, eating and metabolizing chems are some examples. But these are often named inconsistently - breathing is handled by a "LungsComponent", but metabolizing reagents from the Body's chemical solutions is the "MetabolizerComponent". 
* Sometimes an organ is just there so that some other system does something if that organ is added or removed. For example, brain organs don't themselves control anything to do with the brain of a Body, but instead are just used as the entity chit for where a Player's mind ends up if the brain is ripped out of the Body.
* Implants are extremely similar to Organs in concept but do not share code. Implants are instead just stored inside a Container on the Body.
* Quite a few gameplay systems that interact with Body are not actually Organs. Movement speed, stamina and stunning are gameplay that is directly affected by Body - some chems increase stamina or movement speed - but are not actually tied into any organ in particular.
* Some gameplay systems that sound like they're Organs are actually not organs. The most notable of these is Hands, which despite being named after something a Body has is actually something that can be given to any mob. Another example is Eyes. Eyes even have their own damage model - via Blindable - that works on its own and only lightly interacts with Body. 
* Some organs that are implied to exist in-universe, like the mouth, just don't exist at all. The stomach, not the mouth, controls what a mob is capable of eating.

## Conclusion

Body is an incomplete, partially-functional domain of code that is internally inconsistent. It covers defining the shape and structure of mobs, and its internal logic attempts to define how the underpinnings of medical gameplay are supposed to work in code. In general it's advised to read Body code carefully before attempting to extend or modify it. The pages inside this category cover explorations of a number of namespaces that, along with Body, build out the behaviours of the average spessman.