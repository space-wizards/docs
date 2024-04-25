# Gun Overhaul

| Designers | Implemented | GitHub Links |
|---|---|---|
| WarMechanic | :x: No |  |

## Background

Started a thread of gun discussion on DeltaV Discord because I didn't like how I couldn't cycle shotguns like I could rifles. 
Proposed a series of changes in relation to making guns modular and more mechanical, encouraging gun maintenance and mastery, and rebalancing combat to be slower and more tactical - which in turn provides more room for text chat and RP.

However, DeltaV has no maintainers at the moment which means I need to bring my ideas upstream. Given that LRP and MRP are different contexts, some of these ideas may be incompatible but I wish for everything to be configurable, and it'll help with compatibility too.

Some changes fall under different categories, so the overhaul shouldn't be done in a single pull request.

## Overview

### backend

this section is a stub, BallisticAmmoProvider, MagazineAmmoProvider and ChamberMagazineAmmoProvider all feed bullets into guns and would probably be better separated as Chamber, MagazineSlot and Ballistic

### Mechanical Guns

Right now, both ballistic and energy weapons point at enemies and do damage. There *are* some implications that differentiate ballistic and energy weapons like projectile speed and ignoring windows, but these differences aren't very significant.

The first pillar to this series of proposed changes is aimed not only at giving guns more mechanics, but making ballistic and energy weapons more tactile and feel distinct from one another.
Both ballistic weapons and energy weapons can be stripped, and cleaned or modified to suit the user's needs through construction processes. Energy weapons in particular will allow their power cells to be stripped and replaced in the field.


### The Ammo Belt system

At the moment, the only way to feasibly transfer high quantities of bullets is to use ammo boxes and magazines, and individual bullets will take up a single inventory slot regardless of actual size.
Back when I attempted Roblox development, I had a design in place for a bullet handling system in a gridventory but I never had time to implement it.

The gist was that bullets of the same calibre could be stored in individual cells regardless of type in a bullet **stack**. 
Bullet inventory interactions are conceptualised as 'holding' an infinite number of nearby bullets for convenience of inventory management, which we will refer to as the bullet **heap**. 
Dragging the cursor across empty cells would 'paint' stacks from the heap that link together to form organised **belts**. 
Bullet belts served a function of inventory organisation by allowing you to partition a space for 30 assault rifle bullets, but they could also be arbitrarily linked to **belt-fed weapons**.


### Guns are ranged weapons!

The second pillar pertains to gun balance and investigates ranged combat in SS14. 
At the moment, ranged combat often revolves around kiting and dodging opponents' bullets which is input intensive. 
Without prior context, it can be quite boring to watch a captain and a blood red chase eachother. 

Changing how guns are used in combat by applying movement speed restrictions to guns and making them two handed will slow down the pace of combat to make survivability more cover and concealment dependent.

# Note

I need help with formatting this stuff, this is an info dump of all my ideas.

## Mechanical Guns

- Provide support for 'ChamberMagazineAmmoProvider' component to recognise 'BallisticAmmoProvider' component on pump action shotguns.

- Implement gun modification by allowing players to deconstruct and swap parts in slots (barrel, stock, power cell etc) on guns which then modifies its properties, like how players can wear clothes with components.

- Greyscale gun components so they're recolourable.

- Implement the concept of part condition and providing means for players to clean their firearms. Using a gun with lower condition will lead to mechanical malfunctions.

- Implement the concept of magazine-stripping for firearms and the double feed malfunction.

- Implement the concept of magazine-seating for firearms and extraction failure.

- Implement the concept of weapon heat for laser weapons which ties to the condition system, and barrel melting.

- Implement the concept of gun safety and accidental discharges, which are incurred when taking damage or exposed to explosions while a gun is in your inventory.

- Disable the ammo UI for all guns (except the WT550) to encourage mechanically diagnosing your gun. Instead add an ammo UI to all magazines.

- Add configuration for condition and jamming mechanics.


## Ammo Belt system

- Implement the concept of bullet stacks and belts. Bullet stacks will always have worse storage efficiency when compared to ammo boxes.

- Conceptualise inventory interactions with bullet stacks and belts such that you can 'hold an infinite number of bullets in your hand' - hold a bullet heap that actually just links to nearby bullets. Send inventory transactions to the server only when needed. 

- Implement belt linking, turning the bullet heap in your hand into multiple linked bullet stacks.

- Implement belt merging, which allows you to evenly mix bullets of different belts together into your bullet heap.

- Implement fast and precise bullet un/loading of magazines.

- Implement belt-fed weapons, which arbitrarily link to a belt within a certain radius.



## Guns are ranged weapons!

- Allow every gun to be wielded such that interacting with a wielded gun open/closes the bolt rather than unwielding it (see L6 saw for poor interaction)

- Improve gun accuracy and incur a movement penalty while wielding a gun. Movement penalties do not apply to space combat.

- Shoving a gun wielder will immediately unwield their gun.

- Implement the concept of deviation, which is inaccuracy separate from a gun's mechanical spread.

- Investigate the gridventoy space guns take up (Why does a Kammerer take up less volume than a WT550? Why can you fit a Lecter in a satchel?)



## Ballistic Weapon changes

- Add a verb to magazines that inserts it into a gun in your offhand.

- Increase the fire-rate and bullet velocity of ballistics across the board. Configurable via parts.

- Zero or significantly reduce the damage that ballistic weapons do to metal or reinforced structures.

- Remove fully loaded magazines from fabrication and instead rely on printing of ammo boxes.

- Change all guns in the armory to start unloaded, and relocate missing ammunition to a separate safe.

- Change the colour of .50 slugs to green



## Laser Weapon changes

- Allow lasers to be blocked by smoke.

- Allow invisible entities to ignore lasers.

- Entire laser guns can no longer be placed in rechargers, power cells need to be stripped to be recharged/replaced.

- Double the fire rate and capacity and halve the damage of laser rifles to improve their suppression ability.



## Additions

- Add a .50 door breaching charge that breaks open doors and lockers.

- Add higher capacity magazine options to research that have lesser storage efficiency.

- Add a pistol grip for the Kammerer that is made with plastic.

- Add a side saddle compatible with all shotguns that has an inventory for shotgun shells.

- Add a gun modification that re-adds the ammo UI.

- Add tools specific to cleaning guns, or a generic gun cleaning kit.

- Add parts relevant to stripping guns.

- Add barrels of various lengths.



## Other stuff

- Expose impulseStrength variable in CauseImpulse such that gun recoil is not hard coded.

- Potentially animate in-hand icons to better represent gun interactions, improving tactility.

- Replace the sprites of bullets to solid bullets rather than bright tracers, and add a displacement map to them for a supersonic effect. 

- Add tracer bullets to replace the above, allow them to be recoloured.
