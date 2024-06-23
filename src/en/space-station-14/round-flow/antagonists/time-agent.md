# Overview
    This proposal suggests the implementation of a new antagonist role, Time Agent, in order to add more variety and fun to possible encounterable gameplay. The role's theme revolves around undercover agents sent back in time or from the past to nudge the timeline in the direction that suits their goals best, be it by preventing certain events or by ensuring that they happen in the first place.


## Mechanics
	Chronodisc:
        Every agent starts with a Chronodisc item in their bag. All abilities require the Chronodisc to be present somewhere in the inventory or body of their owner. Every agent is attuned to their own Chronodisc, so one cannot use the Chronodisc of another for the purposes of time manipulation. (therefore, Security might be willing to place a repentant agent on parole by taking away and destroying their Chronodisc, effectively making them a normal crewmember; the Science department might also appreciate being given a Chronodisc, as it grants a nice amount of research points)

	Possibilities:
        By completing objectives - even optional ones - agents create opportunities for them to be able to use their abilities safely. Each agent starts with 1 possibility plus 1 additional possibility per Nudge Life objective at spawntime. The amount of possibilities the agent may have can freely dip into the negatives, but there are consequences to this listed below.

	Doom:
        By failing mandatory objectives or by excessively using possibilities, the total amount of possibilities an agent currently has decreases. This amount can decrease into the negative. When an agent's amount of available possibilities is negative, they become doomed. Dying while doomed prevents revival and resuscitation. While an agent is alive for a certain amount of time while doomed, they become vulnerable to Doom Events. The only way for an agent to escape doom is to bring the amount of possibilities they have back to the positive or, at the very least, 0.

	Doom Events:
        When a doomed agent is alive for a certain amount of time - the timer for which gets halved every time the agent continues expending possibilities while their counter is in the negative - things around them may malfunction in certain ways to cause their demise. Examples include getting shocked having a 90% chance of husking, getting hit by a stabbing/blunt attack having a 90% chance of piercing/bludgeoning the eyes & brain if the attack was on the head, getting hit by a stabbing/blunt attack having a 90% chance of piercing/bludgeoning the heart if the attack was on anything other than the head, damage taken from chemicals/diseases/ailments is increased tenfold, being affected by a chemical substance has a 90% chance to instantly cause an allergy to said substance, etc.


## Skills
	Assist the Future:
        Teleports the agent into a projection of the future - a temporary, empty dimension with a featureless humanoid figure at the center of it - for 8 seconds, where all performed actions will happen when summoned at a later time via Summon Past Assistance. The damage and other effects that the agent's past self might experience when summoned in reality will be dealt in a delayed manner, at a random time in the future after the summoning. There can be up to 3 instances of assistance created at a time, and when one is used, it's expended forever. The center of the temporary dimension’s floor glows the most, and is where Summon Past Assistance will be targeted.
            > No Target: There is no target at the center of the projection.
            > Target: The humanoid figure at the center of the projection can be used for actions such as melee attacks, injections, (un)dressing and so on.

	Summon Past Assistance:
        Expends 1 possibility. Summons the agent's past self - established by Assist the Future - to assist the present self. Can be used when incapacitated.

	Summon Future Assistance:
        Expends 1 possibility. Summons the agent's future self to assist the present self. Without targeting entities, the future self can stay in the present time for only up to 7 seconds - though the duration is chosen at random - but if it targeted someone during this time, it extends that limit by 1 more second. When Summon Future Assistance is used, a time loop is left unclosed. The agent must use Temporal Loop Memories (optional) and Assist the Past to close said loop. If the loop stays open for 15-20 minutes - chosen at random - 4-6 of the agent's possibilities get doomed and vanish. Much like with Assist the Future, Summon Future Assistance saves a log of all actions taken and events that happened that involved the agent’s summoned future self for later use during Assist the Past. Targeting an item will make the summoned future self pick it up regardless if it's Aggressive/Miscellaneous/Benevolent. Can be used when incapacitated.
            > Aggressive: The future self attacks the targeted entity, with the weapon in question - if any - being selected at random from the history of all weapons that the agent encountered thus far. If there are no visible entities on the targeted tile, the future self will target the closest visible person to the tile in a 7 tile radius that isn't the present self. If that still yields no valid results, the future self guards the targeted location for 7 seconds. If, within 7 seconds, a valid entity is seen by it, the future self runs to them and attacks. If a window was targeted, the future self uses a weapon robust enough to break it. If a disposal unit is targeted, the future self attempts to force it to eject its contents, etc.
            > Miscellaneous: The future self uses a flash or some other crowd control item - yet again, chosen at random - on the targeted entity. If there are no visible entities on the targeted tile, the future self will target the closest visible person to the tile in a 7 tile radius that isn't the present self. If that still yields no valid results, the future self guards the targeted location for 7 seconds. If, within 7 seconds, a valid entity is seen by it, the future self runs to them while trying to use the crowd control item they currently have. If a wall was targeted, the future self uses something to destroy it. If a disposal unit is targeted, the future self attempts to turn its power off.
            > Benevolent: The future self uses 1-2 brute-healing items on the targeted entity if the entity has higher brute damage than burn damage, 1-2 burn-healing items if burn damage is higher than brute damage, or uses the equivalent of Help Intent if the target has no burn damage and no brute damage. If there are no entities on the targeted tile, the future self will target the closest person to the tile in a 7 tile radius that isn't the present self. If that still yields no valid results, the future self guards the targeted location for 7 seconds. If, within 7 seconds, a valid entity is seen by it, the future self runs to them to do the things listed above. If a wall/window was targeted, the future self attempts to fix it with the appropriate tools & materials required. If a disposal unit is targeted, the future self attempts to activate it to send anything in it through.

	Assist the Past:
        Teleports the agent into a projection of the past - a temporary, empty dimension with featureless figures representing any mobs that were nearby at the time - for however many seconds the unclosed loop had lasted, where all performed actions had already happened before. The damage and other effects that the agent's future self experienced when summoned in reality will be dealt during the assistance in the projection. The center of the temporary dimension’s floor glows the most, and is where Summon Future Assistance was targeted originally.

	Temporal Loop Memories:
        The agent recalls the actions they must perform with Assist the Past to close the time loops created by Summon Future Assistance.

	United Synchronization:
        Can be cycled through freely. Multiplied uses of abilities incur multiplied amounts of possibilities, as is expected.
            > None: The default.
            > Past Only: Using Summon Past Assistance uses the ability twice if there are 2 or more Assist the Future loops currently prepared for closure.
            > Past & Future: Using Summon Past Assistance uses the ability as many times as there is Assist the Future loops currently prepared for closure. If the amount of prepared Assist the Future loops is less than 3, Summon Future Assistance is used however many times needed to bring the total number of summoned doppelgangers up to 3. Using Summon Future Assistance uses the ability thrice.
            > Future Only: Using Summon Future Assistance uses the ability twice.

	Rewind Bubble:
        Expends 4 possibilities. When blown, automatically pops in 21 seconds if not popped manually. (manual popping is simply done by using the ability again while a bubble is currently active)
            > Blow: Saves the state of the area in a 5 tile radius around the agent, as well as the agent's position.
            > Pop: Rewinds the saved area, as well as any items or mobs tagged/logged by the bubble, to the state everything was in when the bubble was blown. The agent's position, obviously, gets rewinded to their saved position as well.

## Objectives
	Nudge Item: 
        > Place Item on a Certain Table: Awards 1 possibility. Can be optional.
        > Place Item in a Certain Box/Bag/Locker: Awards 1 possibility. Can be optional.
        > Ensure Item is in Inventory Until Certain Time: Awards 1-2 possibilities. Can be optional.
        > Ensure Item is in Certain Crewmember's Inventory at Certain Time: Awards 2-3 possibilities. Can be optional.

	Nudge Life:
        > Ensure Certain Crewmember is Alive at Certain Time: Awards 2-4 possibilities. Revokes 2-4 possibilities if failed.
        > Ensure Certain Crewmember is Dead at Certain Time: Awards 3-5 possibilities. Revokes 3-5 possibilities if failed.

    Objectives that can be optional also generate spontaneously similarly to Goonstation’s Spy Thief bounties and /tg/station’s Traitor objectives.


## Expected Gameplay
    The agent, at the start, is expected to act like a Traitor: blend in with the crew, avoid inventory searches and collect items that might be helpful later on. Unlike a Traitor, though, the agent isn't able to spawn in contraband to use for their goals - they must instead imagine possible circumstances and prepare themselves for them via Assist the Future. Examples are as follows:
        > Using handcuffs on the featureless target during Assist the Future, and then using Summon Past Assistance at a later date to cuff the targeted, freshly restrained individual while the present self of the agent is aggressive-grabbing them.
        > Using a medipen on the featureless target during Assist the Future, and then using Summon Past Assistance at a later date to save a targeted, bleeding out individual in a room the agent can't access on their own.
        > Using an explosive before dropping it on the floor during Assist the Future, and then using Summon Past Assistance at a later date to have the explosive be dropped in some important location.

    Of course, there might be times when the agent gets into some trouble - a room they were in was bombed, a Security Officer succeeded in detaining them, or there's just a heavy need for a distraction - and they were caught with their proverbial pants down, with no instances of the agent's past self applicable for the job. This usually means that they must resort to getting help from their future self via Summon Future Assistance. Examples are as follows:
        > Seeing a wall partially breached by a meteor in an area the agent cannot reach, and then using Summon Future Assistance to have the benevolent future iteration of the agent - clad in proper protective gear - repair the wall and thus halt the loss of air.
        > Seeing a Clown running away from a pissed-off crowd, and then using Summon Future Assistance to have a miscellanously-inclined future iteration of the agent stun the Clown, preventing their escape.
        > Getting caught off-guard by a Space Ninja and placed into crit, and then using Summon Future Assistance to have an aggressive future iteration of the agent attack the enemy to distract them while also using Summon Future Assistance again - this time benevolently - to have the second future iteration of the agent stabilize and heal the agent's present self.

    The usage of Summon Future Assistance, if the agent resorts to it, prompts a race against time to close the loop created by the ability. If the agent collects the necessary items - listed by using Temporal Loop Memories - and successfully closes the loop by using Assist the Past while performing the necessary string of actions listed by, yet again, using Temporal Loop Memories, they remain safe from being doomed. If they take too long, though, or perform the required string of actions within Assist the Past incorrectly... their minutes are numbered. Hubris had signed the agent's death warrant.

    Either due to having plenty of possibilities left to spare, or deciding to sacrifice themselves in a blaze of (delayed) glory, the agent might consider adjusting their United Synchronization ability or creating a Rewind Bubble, depending on what they might need. Both options are very risky, but risk and drawbacks are embedded in this role's DNA - it's up to the agent in question to choose to stray away from a safer path.

    And, in the end, ideally with all necessary objectives completed, the agent retires from the shift alongside the other surviving crewmembers. Them still being alive in spite of the many dangers of time is an impressive feat already.