# Stunning, Rotting and Gibbing

When bad things happen to worse spessmen.

# Design

## Stunning

Other than damage, stunning is the big lever for combat in Space Station 14. Stunning someone is caused by causing them to hit their stamina threshold, usually via hitting them with a stun baton or a disabler shot too many times. Stamina is really the abstract concept of "non-lethal" damage.

Much like damage, once the threshold for a mob is hit, that mob enters "crit", a period of time during which they fall over and drop their items. At the end of this period the mob can stand back up.

Stamina damage is slowly healed, starting a short time after the mob took stamina damage. When leaving the stamina crit state, a mob is reset to having 0 stamina damage.

Despite stunning being conceptually linked to bodily functions (hitting someone with a pulse that makes them unable to continue using their muscles properly), stunning itself isn't driven by an Organ. Instead, it's driven by a component and its accompanying system.

## Rotting

Rotting is an important part of what happens to Bodies, but rotting itself actually lives outside of the Body codebase - it's closely tied into the Atmos codebase. This is because of two reasons:

1. Rotting actually happens to any "rottable" thing, not just corpses. The chef's new slab of meat to make burgers with rots, and the chef mechanically has ways to store meat to keep it fresh. This makes sense - a corpse is a source of meat, and meat is there to be eaten.
2. Rotting is tied into the atmospheric temperature and actually affects the atmosphere's composition in minor ways. In some old Space Station 13 forks, this included aping the "miasma" mechanic from Dwarf Fortress (where rotting bodies and meat emit horrible purple gas that makes people throw up). In SS14 this is a much more minor mechanic, but rotting bodies do end up relying on the wider atmosphere for some of their behaviour.

## Gibbing

Gibbing is the point where a Body ceases to exist. This is due to massive damage being taken by the Body, and in some ways can be considered the "final" mob state a Body can enter.

Gibbing is usually caused after an extremely large amount of damage has been taken, well in excess of the damage actually needed to kill a mob. (TODO: cite exactly how much damage this is).

When being gibbed - either by taking huge damage over a series of attacks or simply being landed on by a space shuttle - two important things happen:

* All of the bloodstream and chemstream solutions spill out onto the floor, creating a huge pool of liquid.
* Some or all of the organs of the Body are dropped as items. Not all organs will be converted into items. (TODO: reference where this is set).

# Engineering

## Components

### DamageableComponent

### StaminaComponent

This component drives stamina as a mechanic. There's a few levers that can be pulled to modify how stamina works for a given mob:
* Cooldown - how long it takes for stamina damage to begin healing naturally after being hit with it. This timer resets each time the mob takes stamina damage.
* The actual rate of decay
* The crit threshold. This is usually 100 stamina damage, but some drugs increase it.
* Stuntime - the amount of time a stam-crit mob will spend stunned.

### PerishableComponent

### RottingComponent

### GibbableComponent

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

TODO: write this

### SharedRottingSystem

### GibbingSystem

## YAML