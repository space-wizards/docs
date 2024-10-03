# Overview
This proposal suggests the implementation of a new, mostly-neutral solo antagonist role, Time Agent, in order to add more variety and fun to possible encounterable gameplay. The role's theme revolves around undercover agents sent back in time or from the past to nudge the timeline in the direction that suits their goals best, be it by preventing certain events or by ensuring that they happen in the first place.


## Mechanics
#### Chronodisc:
Every agent starts with a **Chronodisc** item in their bag, as well as a compact medpack. The **Chronodisc** is an embeddable throwing weapon, and it can be rewinded/resummoned back into the agent's hand via **Rewind Chronodisc** by its original owner. It must be noted that the Science department, when word gets out that there is a Time Agent on the station, will be incentivized to hunt down said agent in order to claim their **Chronodisc** as it grants a rather nice amount of research points, so the agent is in turn incentivized to keep said **Chronodisc** safe.

#### Possibilities:
By completing objectives - even optional ones - agents create opportunities for them to be able to use their abilities safely. Each agent starts with 1 possibility plus 1 additional possibility per **Nudge Life** objective at spawntime. The amount of possibilities the agent may have can freely dip into the negatives, but there are consequences to this listed below.

#### Doom:
By failing mandatory objectives or by excessively using possibilities, the total amount of possibilities an agent currently has decreases. This amount can decrease into the negative. When an agent's amount of available possibilities is negative, they become doomed. Dying while doomed prevents revival and resuscitation. While an agent is alive for a certain amount of time while doomed, they enter a Doom State. The only way for an agent to escape doom is to bring the amount of possibilities they have back to the positive or, at the very least, 0.

#### Doom State:
When a doomed agent is alive for a certain amount of time - the timer for which gets halved every time the agent continues expending possibilities while their counter is in the negative - they enter a Doom State, causing them to become affected by a 10x multiplier to all incoming damage. Said multiplier affects damage received from both from combat and from DoT effects like harmful chemicals. Additionally, being in a Doom State causes a roll of the proverbial die every single minute (with random delays to avoid predictability) which has a 25% chance of causing the agent to die immediately, regardless of their current health. Instadeath caused by successful Doom State rolls is accompanied by one of several unique death messages, as well as various unique flairs accompanying the message in question: some blood decals, vomit decals, outright gibbing, loss of limbs; basically, whatever fits the theme of that specific death.


## Skills
#### Assist the Future:
Teleports the agent into a projection of the future - a temporary, empty dimension with a featureless humanoid figure at the center of it - for 8 seconds, where all performed actions will happen when summoned at a later time via **Summon Past Assistance**. The damage and other effects that the agent's past self might experience when summoned in reality will be dealt in a delayed manner, at a random time in the future after the summoning. There can be up to 3 instances of assistance created at a time, and when one is used, it's expended forever. The center of the temporary dimension’s floor glows the most, and is where **Summon Past Assistance** will be targeted.
* No Target: There is no target at the center of the projection.
* Target: The humanoid figure at the center of the projection can be used for actions such as melee attacks, injections, (un)dressing and so on.

#### Summon Past Assistance:
Expends 1 possibility. Summons the agent's past self - established by **Assist the Future** - to assist the present self. Can be used when incapacitated.

#### Summon Future Assistance:
Expends 1 possibility. Summons the agent's future self to assist the present self. Without targeting entities, the future self can stay in the present time for only up to 7 seconds - though the duration is chosen at random - but if it targeted someone during this time, it extends that limit by 1 more second. When **Summon Future Assistance** is used, a time loop is left unclosed. The agent must use **Temporal Loop Memories** (optional) and **Assist the Past** to close said loop. If the loop stays open for 15-20 minutes - chosen at random - 4-6 of the agent's possibilities get doomed and vanish. Much like with **Assist the Future**, **Summon Future Assistance** saves a log of all actions taken and events that happened that involved the agent’s summoned future self for later use during **Assist the Past**. Targeting an item will make the summoned future self pick it up regardless if it's Aggressive/Miscellaneous/Benevolent. Can be used when incapacitated.
* **Aggressive**: The future self attacks the targeted entity, with the weapon in question - if any - being selected at random from the history of all weapons that the agent encountered thus far. If there are no visible entities on the targeted tile, the future self will target the closest visible person to the tile in a 7 tile radius that isn't the present self. If that still yields no valid results, the future self guards the targeted location for 7 seconds. If, within 7 seconds, a valid entity is seen by it, the future self runs to them and attacks. If a window was targeted, the future self uses a weapon robust enough to break it. If a disposal unit is targeted, the future self attempts to force it to eject its contents, etc.
* **Miscellaneous**: The future self uses a flash or some other crowd control item - yet again, chosen at random - on the targeted entity. If there are no visible entities on the targeted tile, the future self will target the closest visible person to the tile in a 7 tile radius that isn't the present self. If that still yields no valid results, the future self guards the targeted location for 7 seconds. If, within 7 seconds, a valid entity is seen by it, the future self runs to them while trying to use the crowd control item they currently have. If a wall was targeted, the future self uses something to destroy it. If a disposal unit is targeted, the future self attempts to turn its power off.
* **Benevolent**: The future self uses 1-2 brute-healing items on the targeted entity if the entity has higher brute damage than burn damage, 1-2 burn-healing items if burn damage is higher than brute damage, or uses the equivalent of Help Intent if the target has no burn damage and no brute damage. If there are no entities on the targeted tile, the future self will target the closest person to the tile in a 7 tile radius that isn't the present self. If that still yields no valid results, the future self guards the targeted location for 7 seconds. If, within 7 seconds, a valid entity is seen by it, the future self runs to them to do the things listed above. If a wall/window was targeted, the future self attempts to fix it with the appropriate tools & materials required. If a disposal unit is targeted, the future self attempts to activate it to send anything in it through.

#### Assist the Past:
Teleports the agent into a projection of the past - a temporary, empty dimension with featureless figures representing any mobs that were nearby at the time - for however many seconds the unclosed loop had lasted, where all performed actions had already happened before. The damage and other effects that the agent's future self experienced when summoned in reality will be dealt during the assistance in the projection. The center of the temporary dimension’s floor glows the most, and is where **Summon Future Assistance** was targeted originally.

#### Temporal Loop Memories:
The agent recalls the actions they must perform with **Assist the Past** to close the time loops created by **Summon Future Assistance**.

#### Rewind Chronodisc:
Expends 1 possibility. The agent rewinds the **Chronodisc** attuned to them back into their hand. If, at the time of rewinding, it was embedded in someone, the victim begins bleeding and the rewinding happens as normal.

## Objectives
#### Nudge Item: 
* Place Item on a Certain Table: Awards 1 possibility. Can be optional.
* Place Item in a Certain Box/Bag/Locker: Awards 1 possibility. Can be optional.
* Ensure Item is in Inventory Until Certain Time: Awards 1-2 possibilities. Can be optional.
* Ensure Item is in Certain Crewmember's Inventory at Certain Time: Awards 2-3 possibilities. Can be optional.

#### Nudge Life:
* Ensure Certain Crewmember is Alive at Certain Time: Awards 2-4 possibilities. Revokes 2-4 possibilities if failed.
* Ensure Certain Crewmember is Dead at Certain Time: Awards 3-5 possibilities. Revokes 3-5 possibilities if failed.

Objectives that can be optional also generate spontaneously similarly to *Goonstation*’s **Spy Thief** bounties and */tg/station*’s **Traitor** objectives.


## Expected Gameplay
The agent, at the start, is expected to act like a Traitor: blend in with the crew, avoid inventory searches and collect items that might be helpful later on. Unlike a Traitor, though, the agent isn't able to spawn in contraband to use for their goals - they must instead imagine possible circumstances and prepare themselves for them via **Assist the Future**.
``````admonish example "Examples:"
Using handcuffs on the featureless target during **Assist the Future**, and then using **Summon Past Assistance** at a later date to cuff the targeted, freshly restrained individual while the present self of the agent is aggressive-grabbing them.
Using a medipen on the featureless target during **Assist the Future**, and then using **Summon Past Assistance** at a later date to save a targeted, bleeding out individual in a room the agent can't access on their own.
Using an explosive before dropping it on the floor during **Assist the Future**, and then using **Summon Past Assistance** at a later date to have the explosive be dropped in some important location.
``````
Of course, there might be times when the agent gets into some trouble - a room they were in was bombed, a Security Officer succeeded in detaining them, or there's just a heavy need for a distraction - and they were caught with their proverbial pants down, with no instances of the agent's past self applicable for the job. This usually means that they must resort to getting help from their future self via **Summon Future Assistance**.
``````admonish example "Examples:"
Seeing a wall partially breached by a meteor in an area the agent cannot reach, and then using **Summon Future Assistance** to have the benevolent future iteration of the agent - clad in proper protective gear - repair the wall and thus halt the loss of air.
Seeing a Clown running away from a pissed-off crowd, and then using **Summon Future Assistance** to have a miscellanously-inclined future iteration of the agent stun the Clown, preventing their escape.
Getting caught off-guard by a Space Ninja and placed into crit, and then using **Summon Future Assistance** to have an aggressive future iteration of the agent attack the enemy to distract them while also using **Summon Future Assistance** again - this time benevolently - to have the second future iteration of the agent stabilize and heal the agent's present self.
``````
The usage of **Summon Future Assistance**, if the agent resorts to it, prompts a race against time to close the loop created by the ability. If the agent collects the necessary items - listed by using **Temporal Loop Memories** - and successfully closes the loop by using **Assist the Past** while performing the necessary string of actions listed by, yet again, using **Temporal Loop Memories**, they remain safe from being doomed. If they take too long, though, or perform the required string of actions within **Assist the Past** incorrectly... their minutes are numbered. Hubris had signed the agent's death warrant.

And, in the end, ideally with all necessary objectives completed, the agent retires from the shift alongside the other surviving crewmembers. Them still being alive in spite of the many dangers of time is an impressive feat already.