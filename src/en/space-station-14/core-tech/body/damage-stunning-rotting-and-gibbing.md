# Damage, Stunning, Rotting and Gibbing

When bad things happen to worse spessmen.

# Design

## Damage

For Body specifically, Damage is something that is applied to the mob the Body is part of, and the Body either heals or causes damage.

Damage is a large domain in its own right. In terms of the interaction it has with Body, the following is of note:

### Damage Modification 

A mob's species - and therefore its Body - determines what types of damage that mob can take and the multipliers that are applied to that damage. For example, moths in general have a multiplier on heat damage, and skeletons are immune to all normal sources other than brute and heat (but can still take other sorts of damage if that damage is listed as ignoring resistances).

### Damage Types caused by the Body Itself

Technically metabolized reagents can cause any damage type to the body. However, there are a few causes outside of the metabolization process:

* Asphyxiation (Airloss) - This is usually caused by the lungs being able to stay saturated (i.e. the lungs not having enough breathable air). This is healed when a respiring mob is able to saturate its lungs after respiring.
* Bloodloss - this is caused by having too little blood in the body. Generating new blood will heal bloodloss. Bloodloss and airloss have a badly-documented relationship, because losing enough blood is modelled to also cause airloss. See the respiration and metabolism pages for more information.

Note that hunger and thirst do not cause damage.

## Stunning

Other than damage, stunning is the big lever for combat in Space Station 14. Stunning someone is caused by causing them to hit their stamina threshold, usually via hitting them with a stun baton or a disabler shot too many times. Stamina is really the abstract concept of "non-lethal" damage.

Much like damage, once the threshold for a mob is hit, that mob enters "crit", a period of time during which they fall over and drop their items. At the end of this period the mob can stand back up.

Stamina damage is slowly healed, starting a short time after the mob took stamina damage. When leaving the stamina crit state, a mob is reset to having 0 stamina damage.

Despite stunning being conceptually linked to bodily functions (hitting someone with a pulse that makes them unable to continue using their muscles properly), stunning itself isn't driven by an Organ. Instead, it's driven by a component and its accompanying system.

## Rotting

## Gibbing

# Engineering

## Components

### DamageableComponent

This is the actual core of how mobs - and therefore Body - handles damage. It has a **DamageContainerPrototype** that can modify the types of damage it can take, and a **DamageModifierSetPrototype** which puts modifiers - both linear and multiplicative - on damage received.

Otherwise the component stores the damage the mob has taken - both generally and in each type of damage.

It's important to remember that, no-matter what the context of the damage is or what it's called, all damage is just damage. Genetic damage is just a label, as is heat damage or airloss damage. 1 damage is equal between all three of these things, and mob state thresholds only care about total damage. If someone who has a threshold to crit of 120 takes 119 airloss damage and takes a single point of brute, they're still going to fold over.

The actual effect of damage on mobs can be found on the mob page.

### StaminaComponent

This component drives stamina as a mechanic. There's a few levers that can be pulled to modify how stamina works for a given mob:
* Cooldown - how long it takes for stamina damage to begin healing naturally after being hit with it. This timer resets each time the mob takes stamina damage.
* The actual rate of decay
* The crit threshold. This is usually 100 stamina damage, but some drugs increase it.
* Stuntime - the amount of time a stam-crit mob will spend stunned.

## Systems

### DamageableSystem

The system that covers how to make Damageable entities do things has one incredibly important function:

#### TryChangeDamage

This is the core of a lot of the codebase's interaction with damage. It works by taking the following steps:

* If the entity isn't actually damageable, or it has its damage changes cancelled for some reason (via a cancellable event called BeforeDamageChangedEvent)...
* Apply the resistances, if the attempt to change damage doesn't ignore them. This involves looking to see if the damageable entity has a damage modifier set it can work off off; if it does, the damage is modified by the modifier. An event is then fired fof - DamageModifyEvent - to allow the damage to be modified further.
* Universal modifiers are added to the damage. (These are universal modifiers changeable via cvar).
* The damage itself is translated into a dictionary of damage specifiers
* This dictionary is used to apply damage to the Damageable component.
* Damage visualizer information is updated.
* DamageChangedEvent is emitted.

Otherwise the role of the system is to handle a few niche cases - for example, "healing" an entity completely when it is zombified or rejuvenated, or helping handle taking radiation damage (which doesn't have a "radiation" damage type, instead being split across multiple types without having a damage group itself).

### StaminaSystem