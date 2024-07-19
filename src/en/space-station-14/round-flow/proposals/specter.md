# Specter Antagonist

| Designers     | Implemented | GitHub Links |
|---------------|---|---|
| EmoGarbage404 | :x: No | TBD |

## Overview

This proposal outlines a new antagonist called the Specter, which functions as a replacement for the revenant. 
The Specter's gameplay largely revolves around haunting and causing scary occurrences in an area in order to build up "fear" in players.
Fear functions as a resource for the Specter's various abilities, which they can unlock over time as a form of progression.

## Background

This antagonist is essentially a hard rework of the revenant.
It doesn't really share many traits at all with the current version of revenant but the theming is a hard overlap and that antag is on life-support already.

A large chunk of the haunting-related mechanics are inspired by / stolen from Goon's Wraith antag.

## Fear

Fear is a status condition that mobs can experience, akin to hunger.
It can be inflicted directly through attacks or indirectly through simply being close to an entity.
Fear starts decaying naturally over time a little bit after they have stopped accumulating it.
However, this decay increases with the level of the fear, so high fear levels decay quicker before slowing down.

There are several levels of severity, each having their own effects:

- **Normal:** The default state: No alert and no effect.
- **Uneasy:** No effect. Serves as a warning to the player.
- **Scared:** -25% melee damage to fear-inducing sources. 
- **Terrified:** -50% melee damage to fear-inducing sources, 5% movement speed increase, and 10% increased damage from fear-inducing sources.
- **Hysterical:** Inability to use weapons, 10% movement speed increase, and 25% increased damage from fear-inducing sources, susceptible to Specter's "Reap".

Fear can be actively countered by consuming some chemicals.
Common ones, like alcohol or nicotine, work only when Uneasy or Scared.
However, more advanced calming chemical work even when a player is Hysterical.
Sleeping can also be used to quickly drain built up fear.

Certain jobs, like the Psychologist and Chaplain, start with a small amount of general fear-resistance.

However, fear can also be made more potent by ingesting certain chemicals or having low health and stamina.

## The Specter

The Specter is a solo antagonist with the physical properties of a ghost.
It is typically invisible to living players, can fly through walls around the station, and is generally impervious to any kind of attack.
They can see both players and ghosts but are unable to use any form of conventional chat to communicate with them.
However, they are able to read both normal and deadchat.

They are able to see the fear level of player's through status icons.
The terrified and hysterical fear levels are marked with a slow and fast flashing respectively, in order to signal when objectives can be completed or souls can be claimed.

There are two primary resources that the Specter must manage: _power_ and _souls_.

_Power_ is the Specter's resource pool for a few different things.
Power is used both for activating abilities and as the Specter's health.

_Terror_ is used by the Specter to unlock abilities that are already revealed.
It is accumulated alongside Power when the Specter is nearby players with high amounts of fear.
Using abilities causes the specter to be briefly visible but still unable to take damage.
However, this allows people to throw salt or use the bible on them.

_Souls_ are the Specter's form of progression.
A soul is gained every time a _haunt_ is successfully completed.
At 3, 6, and 9 souls, the Specter gains more powerful abilities that can be unlocked.

The Specter is primarily counted through the use of holy items: salt and the Bible.
Stepping on salt forces the Specter into the "haunt" mode, making them vulnerable.
Using the bible on the Specter after it uses an ability causes the same effect.

### Haunting

Haunting is the Specter's main attack as well as the time when it's most vulnerable. 
A haunt can be started at any time as long as the Specter isn't standing in a wall and there are no players in line of sight.

When a haunt begins, the Specter becomes visible to everyone, loses access to their abilities, and can be hurt and killed.
While active, however, the Specter causes fear to build up for anyone nearby.

While in the haunt form, the Specter gains power and terror based on the fear of nearby players.
This pushes the Specter to regularly haunt while stalking a player in order to replenish their Power.

At any point, if the Specter gets close to someone whose fear is at the Hysterical level, the Specter can click on them to claim their soul.
This instantly kills the victim, rewards the Specter with a soul, and increases their max power by 50.

The haunt lasts for 60 seconds or until a soul is claimed.
Afterwards, there is a minute-long cooldown before another haunt can start.

## Objectives
- Claim 7-12 souls
- Raise 15-20 players' fear to Hysterical
- Raise 3-5 player's fear to Terrified or higher simultaneously
- Keep someone's fear at Terrified or higher for 3 minutes
- Generate 3000 power through fear (excludes baseline power generation rate)

## Abilities

#### Tier 0 Abilities 
Available roundstart at 0 souls.

- **Whisper:**: Sends a message to a target player, slightly increasing their fear.
- **Ectoplasm:** Secretes ectoplasm around the Specter in a small radius.
Slipping on the ectoplasm increases fear and stuns like soap.
- **Shudder:** Causes doors, windoors, and shutters to rapidly open and close, increasing fear for players nearby.
- **Flicker:** Causes lights to flicker, increasing fear very slightly in a large area.
Regular ghosts have this ability innately, allowing them to potentially aid the Specter.
- **Graveyard Mist:** Creates clouds of smoke that obscure vision and cause rapid fear buildup.
This is the same smoke as used for the shadow anomaly.
- **Disruption:** Used on a target player; causes nearby items to be flung at them, causing fear and low damage on hit.

#### Tier 1 Abilities
- **Paranoia:** Causes target player to be unable to decrease fear for 1 minute.
Additionally causes creepy popups.
- **Animus:** Imbues a target weapon with life for 30 seconds, causing it to try and attack nearby players.
- **Ghost Lock:** Causes all doors in radius to bolt for 10 seconds and play spooky slamming sounds.
Afterwards, they will unbolt.
- **The Station Bleeds:** Nearby vents, drains, and closed doors begin to seep blood, increasing fear in nearby players.
- **Quiet:** In target radius, temporarily turns off all lights, extinguishes all flames, and mutes players.
Players caught in the effect will gain fear over time.
- **Possession:** The specter possesses target item for 15 seconds.
While possessing, they can attack and cause fear to anyone they hit.

#### Tier 2 Abilities
- **Ruin:** Used on target player. 
Causes rapid aging and drains stamina over 15 seconds.
- **Necromancy:** Can only be used on target dead bodies.
Causes an NPC Wandering Spirit to spawn.
Wandering Spirits are non-aggressive but unkillable.
They will cause fear in those nearby while present until dispelled by a Chaplain or salt.
- **Void:** Can only be used when 5 tiles away from players.
Creates a black void that causes an extreme spike in fear when stepped through.
Lasts for 2.5 minutes.
- **Shriek:** Damages windows nearby and causes lights to shatter.
Causes fear for those in range.
- **Greater Animus:** Same effect as _Animus_, except it affects up to 5 items in range.

#### Tier 3 Abilities
- **Panophobia:** On target player, all fear gain is doubled for 1 minute.
- **Raise Ghoul:** Can only be used 5 tiles away from players.
Creates a ghoul mob ghost role that attacks players.
Causes passive fear buildup nearby as well as greater fear buildup on hit.
- **Take Form:** Claim target player's body for 1 minute.
When in this form, dealing damage to others causes fear to build up.
Can be identified in this state due to glowing eyes.
Dying while in Take Form kills the Specter.
- **Create Poltergeist:** Creates a poltergeist ghost role.
This has similar properties to the Specter except it only has the haunt ability.
Terror generated while it haunts will be transferred to the Specter.
Poltergeists do not regenerate health from causing fear.
- **Illusory Form:** Opens a menu for selecting a target player.
When beginning to haunt, you will take the appearance of that player with glowing eyes instead of appearing a the Specter.