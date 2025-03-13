# Secdog Unit Ghost role

## Design Goal

The Goal of adding the Secdog unit to add core gameplay loop variety to the security department. Currently, 3 of the roles are nearly identical (Cadet, Secoff, Det)
with only Det having a minor variation in loadout and some added utility for forensics. All three focus on patroling, detaining, and generally dealing with antagonists with Warden and HOS being the exceptions. A Secdog unit would add great variety for sec players while also opening many roleplay opprotunities with a low MVP cost (as corgi/cerb and their behaviors already exist in code at least in part). The Main goal for the person playing the Secdog is to give a security role where they are not expected to verbally interact with crew, which can be draining, irritating, demoralizing, etc. This gives security a way for players who need a break from the negative human interaction side of the department a way to continue playing there. Allow ghosts to occasionally assist security if they choose, as current ghost roles are, at best, neutral toward the station in most cases.

## Secdog Officer Role

The Secdog units are something most people are familiar with in real life, and their role will mirror that public perception. No more than one (1) Secdog officer slot should be made available as an early game ghost role with a long reoccurance time (ideally there should only be one active at a time per station). Secdog Unit will spawn at the normal security officer spawn location and be equipped with a few canine specific items (detailed later). Secdog Officers will be mechanically incentivized to accompany security officer, as they will cover gaps in each others abilities to keep the station safe.

#### Pros / Abilities

* Bite: Medium damage bite attack
* Lunge: Dash attack which force-drags the target for a short duration. Slows the dog significantly for the same duration, even if they miss.
* Signal: Whistle-like callout / bark to notify handler of contraband.
* Drag: Dogs can drag bodies and other objects like other humanoids.
* No Slip Paws

#### Cons

* Unable to talk or use radio(dog speech)
* Unable to detain or arrest (only bite)
* Limited resource (Ghost role not guaranteed, and hard to replace if killed)
* No suit sensors
* No ranged weapon options
* No ID card


### Ability breakdown

#### Lunge

The Secdog lunges in its current direction, if it makes contact with a mob, that mob is force-dragged by the secdog for a short duration. The dogs speed is reduced significantly when they hit a target or finish their lunge whichever comes first for the same duration. This ability would have a short cooldown (~5 seconds) to prevent spamming.

#### Signal

Functions identically to the security whistle, but with a barking sound effect, for alerting handler. This will use an action instead of an item, with a bark sfx instead of the standard whitsle sfx.

#### No Slip Paws

Secdog has no slip paws - self explanatory. Makes slipping less of an life threating problem for security when the dog is nearby.

### Secdog Inventory

Current dogs can be updated to be given support for all new appropriate items (Ian, Cerb, etc.), but doesnt need to be required for MVP.

* Secdog will have an suit slot. The Secdog unit default loadout will come with an Secdog armored vest that provides similar bonuses to the standard armored vest that security gets.
* Secdog will have standard mask and tank slots for breathing like ian and cerb currently (see corgi prototype)

#### Secdog Items

New entities to be implimented for Secdog use

* Secdog Hardsuit - spawns with the Secdog, occupies suit slot, only equipable by Secdog in MVP, other dogs in future. Provides similar bonuses (and drawbacks) as security hardsuit.
* Secdog Armored Jacket - spawns equipped to Secdog, occupies suit slot, only equipable by Secdog in MVP, other dogs in future. Provides similar bonuses as security armored vest. Starts equipped by default.

### Other Notes

This proposal will require some new sprite and sfx assets:

Sprites:
* Secdog Hardsuit: icon + equipped overlay for Secdog
* Secdog Armored Vest: icon + equipped overlay for Secdog
* Secdog entity: Up/Left/Down and Dead
UI
* Lunge ability icon

Sfx:
* Secdog alert whistle
* Secdog bark (if desired to be unique from other dogs)
* Secdog growl - for lunge ability
