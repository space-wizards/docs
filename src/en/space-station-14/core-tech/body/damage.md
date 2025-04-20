# Damage

# Design

Mobs gain and lose damage during gameplay. A Body does not track its own damage; instead, it adds and removes damage from its mob.

No-matter what the context of the damage is or what it's called, all damage is just damage. Genetic damage is just a label, as is heat damage or airloss damage. 1 damage is equal between all three of these things, and mob state thresholds only care about total damage.

## Dealing damage to a Body

The body does not get damaged directly. Instead, the mob the body is inside gets damaged by any of the ways Space Station 14 can manage it.

## Damage Types caused by the Body Itself

Metabolized reagents can cause any damage type to the body. Otherwise:

* Asphyxiation (Airloss) - This is usually caused by the lungs being able to stay saturated (i.e. the lungs not having enough breathable air). This is healed when a respiring mob is able to saturate its lungs after respiring.
* Bloodloss - this is caused by having too little blood in the body. Generating new blood will heal bloodloss.

Note that hunger and thirst do not cause damage.

## Damage Modification 

A mob's species determines what types of damage that mob can take and the multipliers that are applied to that damage. For example, moths in general have a multiplier on heat damage, and skeletons are immune to all normal sources other than brute and heat (but can still take other sorts of damage if that damage is listed as ignoring resistances).

## Damage healed by the Body

The body will heal itself automatically via metabolism. The body always can heal some amount of damage on its own. For example, a body will eventually stop bleeding and will eventually recover airloss and bloodloss damage. Bodies often can heal small injuries to common damage types itself, to avoid repetitive trips to medbay. However, for very serious forms of damage, the Body will rely on its metabolism system to metabolize reagents that have healing effects.

## Damage healed in other ways

There are a number of items and abilities that confer healing; the most important in the context of practicing medicine are items such as bruise packs, that heal some amount of damage on use on a target.

# Engineering

## Components

### DamageableComponent

This is the core of how mobs handle damage. It has a **DamageContainerPrototype** that can modify the types of damage it can take, and a **DamageModifierSetPrototype** which puts modifiers - both linear and multiplicative - on damage received.

Otherwise the component stores the damage the mob has taken - both generally and in each type of damage.

The actual effect of damage on mobs can be found on the mob page.

### HealingComponent

HealingComponent is attached to items that change the amount of damage on a target mob on use. Despite its name, HealingComponent makes an item deal damage - the difference is that this damage is _negative_ damage. Like other damage-causers, it uses a DamageSpecifier to define what damage it causes.

HealingComponent also can help with bleeding and missing blood.

HealingComponent can optionally lock healing to specific damage containers - e.g. make it so a brute pack can't heal a cyborg by limiting its effect to "Biological". 

## Prototypes

### DamageContainer

Used to categorize types of damageable entities into subgroups. Each subgroup is only capable of being damaged by a given set of damage groups plus a given set of specific damage types.

### DamageModifierSet

A set of pairs of damage types and multipliers of those damage types, and a set of pairs of damage types and flat damage modifiers for that damage type. Used to change the amount of damage a damageable entity actually takes when taking damage.

### DamageGroups

Groups a set of damage types under a given group. Used to categorize types of damageable entities - see DamageContainer.

### DamageType

Defines a particular damage type, such as "Cold".

## Systems

### DamageableSystem

Handles damaging mobs. 

DamageableSystem interacts with a bunch of universal damage modification CCVars - this is to allow for playtests that modify damage generally up or down. These CCVars cover specific causes of damage such as projectiles.

The system handles some peripheral actions, such as healing a mob on its rejuvenation, and coping with irradiation damage sources to translate that into radiation damage. However, the most important thing the system does is TryChangeDamage.

#### TryChangeDamage

This is the most important function in DamageableSystem. TryChangeDamage follows a set of steps to attempt to change the amount of damage a damageable entity has. 

The process for applying damage to a mob is as follows:

* An event called BeforeDamageChangedEvent is raised; this is a cancellable event that will stop damage being taken if cancelled.
* Damage modification is applied, if the source of damage doesn't "ignore resistances" (this does mean that a vulnerable mob would take _less_ damage than usual for that damage type). Modification of damage is based on the mob's DamageModifierSet, and a DamageModifyEvent that is raised that can modify the damage elsewhere.
* Universal modifiers (the CCVars used for playtests) are applied.
* Damage is then applied to the mob.
* The effect of this damage rolls out - the DamageableComponent is fully updated to track the damage and a DamageChangedEvent is fired. If a mob can have its damage visualized (via an AppearanceComponent) this also gets updated -- allowing people to appear bloodied, and so on.

### HealingSystem

This system powers the activity of healing someone with an item. It does this via a set of steps when someone uses an item on a mob.

#### TryHeal

The process for healing someone starts with making sure that the healing source can actually heal their damage container - that is, a silicon cannot be healed by a brute pack, because the silicon does not have the Biological damage container.

After other interaction-based checks (is the target in range and actually damaged?) a do-after is triggered.

#### OnDoAfter

Once the do-after for healing a mob is completed, if the target is still a legal target of the healing:

* Try and modify the bleed amount the mob has, if the healing item modifies bleed amount.
* Try and modify the blood level the mob has, if the healing item modifies blood level.
* Try and change the damage of the mob by the specified amounts. Of note here, this healing can be scaled by the DamageableSystem's UniversalTopicalsHealModifier; this means that if a topical _deals_ damage, this modifier would also reduce that damage dealt.

# YAML

Sometimes Damageable is used to pre-set some damage to a mob. For example, the following entity is a corpse, findable during salvage:

```yaml
- type: entity
  parent: BaseMobHuman
  suffix: Dead
  save: false # mobs are currently not saveable.
  id: SalvageHumanCorpse
  name: unidentified corpse
  description: I think they're dead.
  components:
  - type: RandomHumanoidAppearance
    randomizeName: false
  - type: Damageable
    damage:
      types:
        Bloodloss: 49
        Asphyxiation: 76
        Slash: 56
        Blunt: 19
  - type: Inventory
    templateId: corpse
```

However, Damageable is more often used to flag something as being able to take damage, with a bit of customization about how taking that damage works

For example, this is the Damageable component on a cockroach.

```yaml
  - type: Damageable
    damageContainer: Biological
    damageModifierSet: Cockroach
```

The damage container here flags that the Damageable entity can take the following forms of damage:

```yaml
- type: damageContainer
  id: Biological
  supportedGroups:
    - Brute
    - Burn
    - Toxin
    - Airloss
    - Genetic
```

Cockroaches have a slightly non-standard damage modifier set:

```yaml
- type: damageModifierSet
  id: Cockroach
  coefficients:
    Blunt: 1.0
    Slash: 1.0
    Piercing: 1.0
    Cold: 1.0
    Poison: 1.0
    Cellular: 1.0
    Radiation: 0.0 # hehe funny cockroach immune to rads
    Caustic: 1.0
```

However, the damage modifier set does not match the damage container; this is because the actual types of damage are organized into groups. For example:

```yaml
- type: damageGroup
  id: Brute
  name: damage-group-brute
  damageTypes:
    - Blunt
    - Slash
    - Piercing
```

Damage type themselves are defined as such:

```yaml
- type: damageType
  id: Blunt
  name: damage-type-blunt
  armorCoefficientPrice: 2
  armorFlatPrice: 10
```

(Note that the "armor" tags above are because the spesos value of armor is tied into the armor's effectiveness, not for any actual purpose tied to damage).

Items that heal mobs directly, such as brute packs, will have a HealingComponent:

```yaml
- type: entity
  name: bruise pack
  description: A therapeutic gel pack and bandages designed to treat blunt-force trauma.
  parent: BaseHealingItem
  id: Brutepack
  suffix: Full
  components:
  - type: Tag
    tags:
    - Brutepack
  - type: Sprite
    state: brutepack
  - type: Item
    heldPrefix: brutepack
  - type: Healing
    damageContainers:
      - Biological
    damage:
      groups:
        Brute: -15 # 5 for each type in the group
    healingBeginSound:
      path: "/Audio/Items/Medical/brutepack_begin.ogg"
      params:
        volume: 1.0
        variation: 0.125
    healingEndSound:
      path: "/Audio/Items/Medical/brutepack_end.ogg"
      params:
        volume: 1.0
        variation: 0.125
  - type: Stack
    stackType: Brutepack
    count: 10
  - type: StackPrice
    price: 5
```