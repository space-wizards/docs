# Space Ninja V2

| Designers | Implemented | GitHub Links |
|---|---|---|
| Warpzoned, Doru991 | :warning: Partially | TBD |

## Overview

This proposal is aimed towards addressing some issues that Space Ninjas currently possess, as well as adding some extra flavour and other miscellaneous content.</p>
<p>New abilities have been added, and existing ones have been tailored to better fit with the stealth-based gameplay the Spider Clan so endorses. The Space Ninja now also come with an extra assortment of apparel, both useful and cool-looking.</p>
<p>The Space Ninja's weapons have gotten a slight nerf, to compensate, new weapons and armament interactions have been added.

## Background

Currently, albeit being an extremely fun mid-round antag role and definitely one of the better ones, Space Ninjas aren't correctly geared towards what they should be the best at: Stealthing - Which is what this document hopes to address, mostly to add some more uniqueness to antagonist roles since a lot of them can be played by just killing everything in your way, and this includes Space Ninjas.

## Spider Clan Code

All Space Ninjas will now have a Spider Clan Code they will have to live by, and this thus affects gameplay substantially by imposing certain restrictions.

- The already existing one, being the inability to shoot ranged weapons, will be included in this Code.
- The second restriction is making it so the Space Ninjas can no longer tend to their own wounds - This includes applying topicals, injecting syringes, consuming pills, and drinking liquid chemicals, as it would be preferred that they are not even spotted during their mission. To compensate, Space Ninjas will now have increased passive regeneration as well as faster bloodloss recovery that far exceeds what normal crewmates could ever achieve due to their bio-engineered bodies. Do note that others can still inject and apply whatever to them, however.
- The vow to not kill past a certain % of the total crew, breaking this results in an automatic redtext.

# New Items & Abilities

New content that revolves around both a higher quality of life and a more immersive playfield.

## Flavour Additions

- The Space Ninja now comes with an adequately themed satchel, as well as a katana sheath.
- The Space Ninja's pinpointer will now act as software for the brand new space ninja PDA instead of being its own gadget, the agent ID card will also be within the aforementioned device.
- Equipping the space ninja helmet is now an instantaneous toggle action that comes with the space ninja suit.

## Ability Additions

- The Space Ninja can now fabricate ninja caltrops, a variant of ninja throwing stars with an emphasis on piercing damage and bleeding, once deployed, that is, dropped on the ground, they will progressively get more and more camouflaged to the point of near-invisibility. Upon being stepped on, the caltrops will stick to the victim and perform continous bloodloss damage until taken off.
- The ninja visor can now alternate between normal vision and night vision.

# New Objectives & Mechanics

Gives the Space Ninja more to do and tinker with, so that all rounds don't play out the same.

## Objective Additions

- Steal X spesos - A bluespace wallet is given to the Space Ninja, as well as a new strongbox for Cargo containing all their deposited spesos is added to the vault, they will be tasked with stealing a designated amount (Automatically picked once the do-after begins, similarly to stealing technologies) - An alternative to "Steal X technologies".
- Steal the Station AI - A Spider Clan-themed intellicard is given to the Space Ninja, they are tasked with hijacking the AI with it (And holding onto, as putting the AI back into its core invalidates the objective entirely) - An alternative to "Detonate your spider charge".
- Hack Si-XXXX - The Space Ninja's kill-target equivalent, they are tasked with hacking a specific cyborg with their space ninja gloves, turning it into a zealous Spider Clan tech-priest that obsesses over hoarding all manners of electronics and machines.

## Objective Changes

- All stealing objectives can now only be performed with a specialized item that is dropped by the ninja upon death, unlike previously where they only used their gloves - This allows the crew to regain their losses.
- Make an announcement - The communications computer objective now revolves around the Space Ninja sending a Spider Clan Announcement from it, the contents of said announcement being up to their discretion. Like before, it requires the use of turned on space ninja gloves, the one key difference being that now the EMAG interaction is instantaneous, overriding all access restrictions as well as unlocking Spider Clan as an announcement sender. (Replaces "Call in a threat", consequently removing its threat-calling functionality)
- 1-3 of the Miscellaneous Interactions machines is picked to be hacked by the Space Ninja. Note that you can still hack machines that aren't included in your objectives.

## Miscellaneous Interactions

- Hacking the criminal records computer is now one of the many miscellaneous actions the Space Ninja can do in order to frustrate the crew - The error announcement will now only be sent by the criminal records computer on the Security channel, opposed to the previous station-wide Central Command Announcement. (Goes by "Set everyone to wanted." if made an objective)
- The crew monitoring server is now prone to being hacked by the Space Ninja, doing so will disable everyone's sensors temporarily, the timer appears when examining the server and claims that it's due to it "undergoing maintenance". (Goes by "Disable the sensors." if made an objective - For the sake of reducing metagaming, there will also be a new event that temporarily disables the crew monitoring server with the exact same tooltip)
- The station records computer is now prone to being hacked by the Space Ninja, doing so will delete a small % of random personnel from it accompanied by a station-wide announcement. (Goes by "Delete the records." if made an objective)
- The camera routers are now prone to being hacked by the Space Ninja, doing so will fry a large % of its connected cameras and render them useless, these can be fixed by applying 2 LV cables. (Goes by "Fry the X cameras." if made an objective, as well as one of the many existing routers is picked, and only hacking the correct one will yield a greentext - For the sake of reducing metagaming, there will also be a new effect to the solar flare event that also disables a large % of cameras from a random camera router, as per ArtisticRoomba's request)

# Balance Changes

Changes mostly geared towards fixing previously outright broken mechanics, as well to accomodate the new additions.

## Nerfs

These nerfs are intended to make previous go-to combat tactics less prevalent, hence incentivizing a more varied playstyle.

- [Fix ninja stunlocking](https://github.com/space-wizards/space-station-14/pull/33244)
- Removes the extended-capacity survival box from the ninja's satchel, as there's no longer any use for it.
- Lower the energy katana's one-handed damage.
- Lower the ninja throwing star's piercing damage to compensate for the newly added ninja caltrops.
- Lower the ninja throwing star's stamina damage.

## Buffs

Enhances some things on the Space Ninja's kit in order to make it less of a one-trick pony, as well as to fix some inconsistencies.

- Space Ninjas no longer have a need to eat nor drink.
- Space Ninjas now come outfitted with a ninja headset as per [Alwayswannahunt's PR](https://github.com/space-wizards/space-station-14/pull/32841) , green encryption key included.
- The space ninja gloves can now unlock access-restricted lockers and crates.
- The energy katana's slash rate is slightly faster than it was previously when one-handed to compensate for it's damage loss.
- The ninja throwing stars can now be stacked, as well as thrown in spreads.
- When phasing, the Space Ninja is able to discreetly steal from people.

## Miscellaneous Tweaks

Mostly new additions that weren't either complete buffs nor complete nerfs.

- All Space Ninjas are now randomly selected from a pool of specific species that don't offer a major gameplay shift as they're being spawned in. (These being: Humans, Dwarves, Reptillians, Arachnids, and Moths)
- The katana dash is considerably quieter, at the cost of a longer recharge duration.
- Grants the ability to wield the energy katana for a hard-hitting swing, at the cost of a slower slash rate. *When wielding the energy katana, the Space Ninja's reflect probability also increases.
- When phasing, the Space Ninja's cloak will act similarly to that of stealth boxes', but in a much more potent manner - Running will slightly weaken the stealth field by increasing the distortion's strength, whereas staying still will fade it to the point of near-full invisibility, walking won't weaken nor strengthen the distortion's effect.

# Example Scenarios

The Space Ninja spawns 40~ minutes in on an imaginary mid-pop station in both scenarios.

## Passive & Quiet (Longer)

Objectives:

- Steal 18000 spesos.
- Doorjack 24 doors on the station.
- Hack Si-1752.
- Fry the science cameras.
- Set everyone to wanted. 
- Detonate your spider clan charge in arrivals.
- Make an announcement.
- Survive.

The Space Ninja uses their jetpack to get onto the station, disposes of it, and steathiily teleports into maintenance, to which he starts doorjacking random, underutilized airlocks in order to progress the first of many objectives.

To gain accesses, they go around the station _very_ slowly whilst cloaked, as to not have their cloak's distortion effect visible, and unknowingly to the crew, starts stealing IDs one after the other.

Once he has the proper access clearance, he makes his way to robotics, and then into data, where he comes across the science camera router, after having it hacked and the cameras consequently fried, he quickly flees the scene through the window into space, unnoticed.

Afterwards, he makes his way to the vault, to which he has the accesses for, then it's as easy as it gets, as he only needs to insert the bluespace wallet into the strongbox for a bit, and then take it off.

Later on, he comes across the target cyborg, and waits until it is alone, shortly after the aforemention is true, they decloak, and order the cyborg to go with them (As per Law 2) and not speak, the borg complies, as from their eyes they were merely speaking to standard personnel, then once both are alone in a dark corner in maintenance, he hastily opens his panel and hacks him, successfully completing another of their objectives.

The latter 3 (Non-passive) objectives, being substantially louder than the rest, were left to be completed later, and now is the time. The Space Ninja, having a good grasp of the station's layout, heads on over to arrivals in order to complete both "Set everyone to wanted." and "Detonate your spider clan charge in arrivals.", as they know this station's arrivals also has a security checkpoint. Now, after both objectives are complete, the crew is fully aware of the Space Ninja's presence (If they weren't already due to the malfunctioning cyborg), and sets the alert level to red.

Now the Space Ninja knows it's time to finish off, and so, he bolts (Whilst invisible) to Bridge, but rather than utilizing the main communications console, he aims for the one in the Captain's quarters, and by teleporting into their room, they effectively complete all but one of their objectives without seemingly having been spotted by any of the crew, albeit their presence is now known, whether attention was paid to ;common or not.

## Aggresive & Loud (Quicker)

Objectives:

- Steal 11 technologies.
- Doorjack 23 doors on the station.
- Hack Si-6204.
- Disable the sensors.
- Delete the records.
- Steal the Station AI.
- Make an announcement.
- Survive.

Like previously, the Space Ninja uses their issued jetpack to get onto the station, and upon its disapol, they EMAG onto the AI Sat, and right away complete two of their objectives, these being "Disable the sensors." and "Steal the Station AI.", however, the crew is now extremely aware of their existence due to the AI alerting.

They then rush for another objective, this time around being "Doorjack 23 doors on the station.", unlike the previous Space Ninja, however, they doorjack any and all doors they come across, utilized or not, sometimes with people behind.

Then, as they are making their way towards the Head of Personnel's office, they spot the Captain, and as he's taken a hostile stance towards the intruder, he quickly falls fo the Space Ninja's blade, and subsquently, the victor gains immediate AA, which aids in the completion of "Delete the records." and "Hack Si-6204", to which they later complete.

Before long, the Space Ninja only has to do two more objectives, however, the crew is heavily armed and ready, as well as they have a pocket AI that's always screaming for help, and so it'll be much more difficult than if they had gone a more silent, slower route.

To the crew's dismay, the Space Ninja actually succeeds in the first, which was to "Steal 11 technologies.", and now all that's left is to "Make an announcement." Which he also hastily completes, due to having made quick work of the personnel securing Bridge, nearing his honor limit.
