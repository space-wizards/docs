# Damage, Stunning, Rotting and Gibbing

When bad things happen to worse spessmen.

## Damage

For Body specifically, Damage is something that is applied to the mob the Body is part of, and the Body either heals or causes damage.

Damage is a large domain in its own right. In terms of the interaction it has with Body, there are two areas of note

### Damage Modification 

A mob's species - which is part of its Body domain - determines what types of damage that mob can take and the multipliers that are applied to that damage. For example, moths in general have a multiplier on heat damage, and skeletons take no damage from any source other than brute and heat.

### Damage Types caused by the Body Itself

### DamageableComponent

This is the actual core of how mobs - and therefore Body - handles damage. It has a **DamageContainerPrototype** that can modify the types of damage it can take, and a **DamageModifierSetPrototype** which puts modifiers - both linear and multiplicative - on damage received.

Otherwise the component stores the damage the mob has taken - both generally and in each type of damage.

It's important to remember that, no-matter what the context of the damage is or what it's called, all damage is just damage. Genetic damage is just a label, as is heat damage or airloss damage. 1 damage is equal between all three of these things, and mob state thresholds only care about total damage. If someone who has a threshold to crit of 120 takes 119 airloss damage and takes a single point of brute, they're still going to fold over.

The actual effect of damage on mobs can be found on the mob page.

### DamageableSystem

## Stunning

Other than damage, stunning is the big lever for combat in Space Station 14. Stunning someone is caused by causing them to hit their stamina threshold, usually via hitting them with a stun baton or a disabler shot too many times. Stamina is really the abstract concept of "non-lethal" damage.

Much like damage, once the threshold for a mob is hit, that mob enters "crit", a period of time during which they fall over and drop their items. At the end of this period the mob can stand back up.

Stamina damage is slowly healed, starting a short time after the mob took stamina damage. When leaving the stamina crit state, a mob is reset to having 0 stamina damage.

Despite stunning being conceptually linked to bodily functions (hitting someone with a pulse that makes them unable to continue using their muscles properly), stunning itself isn't driven by an Organ. Instead, it's driven by a component and its accompanying system.

### StaminaComponent

This component drives stamina as a mechanic. There's a few levers that can be pulled to modify how stamina works for a given mob:
* Cooldown - how long it takes for stamina damage to begin healing naturally after being hit with it. This timer resets each time the mob takes stamina damage.
* The actual rate of decay
* The crit threshold. This is usually 100 stamina damage, but some drugs increase it.
* Stuntime - the amount of time a stam-crit mob will spend stunned.

### StaminaSystem

## Rotting

## Gibbing

