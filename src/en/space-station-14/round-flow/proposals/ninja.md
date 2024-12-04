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
- The second restriction is making it so the Space Ninjas can no longer tend to their own wounds - This includes applying topicals, injecting syringes, consuming pills, and drinking liquid chemicals, as it would be preferred that they are not even spotted during their mission. To compensate, Space Ninjas will now have increased passive regeneration as well as faster bloodloss recovery that far exceeds what normal crewmates could ever achieve due to their bio-engineered bodies.

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

- Steal X spesos - A strongbox for Cargo containing all their deposited spesos will be located in the vault, the Space Ninja is tasked with stealing a designated amount - An alternative to "Steal X technologies".
- Upload the law board - An AI law board with a Spider Clan-oriented law set, the Space Ninja is tasked with uploading it to the AI upload console - An alternative to "Detonate your spider charge".
- Hack Si-XXXX - The Space Ninja's kill-target equivalent, they are tasked with hacking a specific cyborg, turning it into a zealous Spider Clan tech-priest that obsesses over hoarding all manners of electronics and machines.

## Objective Changes

- All stealing objectives can now only be performed with a specialized item that is dropped by the ninja upon death, unlike previously where they only used their gloves - This allows the crew to regain their losses.
- Make an announcement - The communications computer objective now revolves around the Space Ninja sending a Spider Clan Announcement from it, the contents of said announcement being up to their discretion. Like before, it requires the use of turned on space ninja gloves, the one key difference being that now the EMAG interaction is instantaneous, overriding all access restrictions as well as unlocking Spider Clan as an announcement sender. (Replaces "Call in a threat", the new objective keeping the threat-calling functionality is still in discussion)
- Hack X - 1-3 of the Miscellaneous Interactions machines is picked to be hacked by the Space Ninja. Note that you can still hack machines that aren't included in your objectives. (Replaces "Set Everyone to Wanted")

## Miscellaneous Interactions

- Hacking the criminal records computer is now one of the many miscellaneous actions the Space Ninja can do in order to frustrate the crew - The error announcement will now only be sent by the criminal records computer on the Security channel, opposed to the previous station-wide Central Command Announcement.
- The crew monitoring server is now prone to being hacked by the Space Ninja, doing so will disable everyone's sensors until deconstructed and reconstructed.
- The station records computer is now prone to being hacked by the Space Ninja, doing so will delete a small % of random personnel from it accompanied by a station-wide announcement.
- The camera router is now prone to being hacked by the Space Ninja, doing so will kill a large % of its connected cameras and render them useless.

# Balance Changes

Changes mostly geared towards fixing previously outright broken mechanics, as well to accomodate the new additions.

## Nerfs

These nerfs are intended to make previous go-to combat tactics less prevalent, hence incentivizing a more varied playstyle.

- [Fix ninja stunlocking](https://github.com/space-wizards/space-station-14/pull/33244)
- All Space Ninjas are now bio-engineered humans, making it so they don't get specie-specific attributes such as tail-dragging.
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

- The katana dash is considerably quieter, at the cost of a longer recharge duration.
- Grants the ability to wield the energy katana for a hard-hitting swing, at the cost of a slower slash rate. *When wielding the energy katana, the Space Ninja's reflect probability also increases.
- When phasing, the Space Ninja's cloak will act similarly to that of stealth boxes', but in a much more potent manner - Running will slightly weaken the stealth field by increasing the distortion's strength, whereas staying still will fade it to the point of near-full invisibility, walking won't weaken nor strengthen the distortion's effect.
