# The Creature
**Type:** Midround Solo Antagonist (Ghost Role)
**Status:** Draft — values TBD pending playtesting

---

## Summary

A stealth-based predator that hunts crew and department pets from maintenance tunnels. Fills a gap in the current Wizden midround roster — no existing upstream antag uses stealth/ambush as a primary mechanic. Existing midround threats (Dragon, Ninja, Lone Op, Wizard, Xenoborgs, Rat King, etc.) are either overt or large-scale; The Creature is intimate and personal.

**Gameplay identity:** Hit-and-fade. Sting a target, drain blood, retreat before crew can respond. Punishes reckless play; rewards map knowledge and patience.

---

## Design Goals

- Make maintenance feel dangerous again — maint is currently treated as a safe loot corridor for passengers
- Add a stealth archetype currently absent from upstream midround pool
- Increase midround variety
- Generate emergent crew behavior (buddy system, patrols, paranoia) without admin involvement

---

## Objectives

| Objective | Description |
|---|---|
| **Eat 3 department pets** | Must consume Ian, Poly, Momo, or other map-assigned pets. Forces The Creature to leave deep maint and enter department areas. |
| **Consume X units of blood** | Tracked via Drink Blood ability. Scales with player count at spawn time. Requires repeated engagement across the round. |
| **Survive** | Standard survival objective. Reinforces the retreat-and-hide loop. Gives Security a valid win condition. |

> **Pet edge case:** If a map has fewer than 3 pets, the objective count adjusts to match available pets. A fallback target (e.g. station mice) may be needed — TBD.

---

## Abilities

| Ability | Description | Design Purpose |
|---|---|---|
| **Passive Stealth** | Visibility float from fully invisible (at rest) to fully visible (active). Moving, attacking, and using abilities increase visibility; each tick it decays back toward invisible. | Core identity. Rewards patience, punishes recklessness. |
| **Drink Blood** | Channeled action on an adjacent target. Drains blood, heals The Creature, and increments the blood objective counter. Requires standing still for the channel duration. | Sustain loop tied to objective. Creates a vulnerability window during use. |
| **Sting** | Short-range attack that stuns the target for a set duration. Moderate cooldown. | Setup tool for Drink Blood. Creates the Sting → Drink → Retreat sequence. |
| **Attack** | Standard melee. No wide-swing. Applies a brief stagger. | Combat fallback if cornered. No wide-swing discourages open-hallway fighting. |
| **Eat** | Action option. consumes valid animals - crew are blacklisted, similar to dragon | Completing eat pet objective |
| **Speed** | Faster than standard crew. | Enables disengagement. The Creature should be able to choose to flee a bad fight. |
| **Door Pry** | Can force doors open at a significantly faster rate than crew with a crowbar. Produces a sound cue. | Allows station navigation without access cards. Sound cue is a discoverability breadcrumb. |
| **Body Drag** | Can drag incapacitated or dead crew with reduced speed penalty. | Repositioning for safelu drinking blood. Evidence removal. Horror moment generator. |

---

## Stealth Visibility Detail

Visibility is a float with a minimum (fully invisible) and maximum (fully visible). Thresholds determine visual state, uses existing steath and stealthOnMove component / systems.

Actions that raise visibility: walking, attacking, using any ability.
Visibility decays passively each game tick while The Creature is not acting.

All specific float values, thresholds, increment amounts, and decay rates are TBD pending playtesting.

---

## Upgrade System (BONUS - NOT MVP)

Blood consumed via Drink Blood accumulates in a persistent pool. Between hunts, The Creature can spend blood from this pool to purchase upgrades from a radial menu (similar to the Ninja's UI). This creates a meaningful decision loop: spend blood on upgrades now, or bank it toward the blood objective.

Each upgrade has three ranks (+1, +2, +3). Purchasing rank 2 requires rank 1, and so on. Each rank costs progressively more blood. All specific blood costs are TBD.

### Upgrade Tree

| Upgrade | +1 | +2 | +3 |
|---|---|---|---|
| **Predator's Strike** *(Attack damage)* | Minor damage increase | Moderate damage increase | High damage increase; attacks apply a brief slow |
| **Quickness** *(Movement speed)* | Slight speed increase | Moderate speed increase | Near-sprint speed; visibility increase per tile is reduced |
| **Shadow** *(Stealth — faster decay rate)* | Faster passive visibility decay | Significantly faster decay | Near-instant decay when standing still |
| **Venom** *(Sting — stun duration)* | Slightly longer stun | Longer stun; small damage on sting | Long stun; sting injects minor bleed |
| **Ravenous** *(Drink Blood — channel speed & heal)* | Faster channel | Faster channel; increased heal per tick | Fastest channel; overheal cap added |
| **Pry Mastery** *(Door Pry speed)* | Faster pry | Significantly faster pry | Near-instant pry; no longer produces a sound cue |
| **Iron Hide** *(Damage resistance)* | Minor resistance to all damage | Moderate resistance | High resistance; The Creature can drag bodies at full speed |

### Design Notes

- The upgrade menu should only be accessible while The Creature is fully invisible (stationary and below threshold A), preventing mid-combat purchases.
- Pry Mastery +3 removing the sound cue is a deliberate late-game power spike that rewards completing objectives — it should only be reachable if The Creature has been hunting actively.
- No upgrade should push any single stat into "unkillable" territory. The intent is to broaden The Creature's options, not create a mandatory optimal path.
- Consider whether upgrades should be visible to admins in the antag panel for post-round review.

---

## Intended Round Flow

1. **Early:** Spawns in deep maint fully invisible. Player scouts pet locations, camera positions, etc. No pressure to engage immediately.
2. **Mid:** Begins hunting. Isolated crew in maint are prime targets. Pet kills leave discoverable evidence (blood decal, sound cue). Crew survivors can report sightings.
3. **Late:** Crew is now aware. Security patrols maint; AI watches cameras. The Creature must adapt routes or accept higher-risk department incursions. If objectives are done, it hides and waits for round end.

---

## Crew Counterplay

**Individual:** Don't go into maint alone. Bring a weapon — a stun baton can interrupt a Drink Blood channel. Flashlights help in dark maint sections.

**Security:** Patrol maint, respond to missing persons/pet reports, arm crew if threat level warrants.

**AI:** Monitor maint cameras for stealth shimmer or door pry cues. Bolt doors to restrict movement.

**Medical:** Fast treatment of blood loss victims prevents death from repeated taps.

**Engineering/Atmos:** Seal maint hatches to restrict The Creature's movement network.

---

## Design Pillar Alignment

| Pillar | How The Creature satisfies it |
|---|---|
| **Just a Spark** | Cannot end rounds alone. Crew reaction (lockdowns, panic, overreaction) generates most of the chaos. |
| **Escalation** | Each successful hunt raises tension and crew awareness. Blood objective scales with pop. |
| **Full-Time Job** | Stealth degrades when inactive in open areas; objectives require active predation. No path to victory through crew-blending or passivity. |
| **Back and Forth** | Must expose itself to attack when striking. Cannot stay aggressive indefinitely — must retreat and wait. |
| **Discoverability** | Leaves evidence: missing pets, blood trails, pried doors, shimmer sightings from survivors. |

---

## What This Is Not

- **Not a murderboner.** Sustained combat breaks stealth; Security can coordinate to kill it.
- **Not a major antag.** No station-wide threats, no infrastructure attacks, no explosives.
- **Not a conversion antag.** Victims do not become allies or infected.
- **Not an NPC.** Ghost role only — human unpredictability is the point.

---

## Open Questions

- **Spawn rate:** Suggest starting comparable to Space Ninja or Revenant and adjusting from playtesting.
- **Appearance:** Visual design unspecified. requires new sprite(s) and sfx, stealth handled by existing code.
- **Multi-antag interaction:** Should spawn weight be reduced when a major roundstart antag is already present? Likely yes.
- **Partial completion:** Is 2/3 objectives a partial win, or all-or-nothing? Current lean: all-or-nothing, Survive included.
