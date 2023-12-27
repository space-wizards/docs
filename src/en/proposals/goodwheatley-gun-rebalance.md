# Gun Rebalance [Goodwheatley, Unapproved]

Right now every type of gun feels effectively the same, since they all share calibers and gun types have largely similar stats. This leads to unfun gun battles where the person who brought the gun with the better bullets will just win outright, and there's no diversity in what weapon you choose. Giving types of guns distinct statlines to follow and then adjusting guns within that type to veer from the statline in different areas creates more depth in gunplay and allows players to plan ahead and choose their gun based on what they expect to be fighting.

### The problems:
- Making guns share calibers was a mistake, since it's now impossible to isolate a gun for balancing
- Almost every gun in the game either hits like a wet noodle or shreds you to bits (mostly the former)
- Laser guns are just bad

### Features needed to properly implement balance:
- Armor Piercing (weapon ignores a set percentage of armor values on the target)
- Bullet Velocity (Represents how fast the bullet will move through the air, and how much damage it will deal when it hits a target. High Velocity bullets will have a higher velocity than standard bullets, which means they'll fly faster along their trajectory. Bullets that can penetrate objects/mobs have the option to lose velocity upon penetration, as well as bullets that can ricochet off walls. A bullet's velocity is directly tied to the damage it will deal when it hits a target, and a CVar toggling the ability for bullets to lose velocity over time should be implemented.)
- Laser Gun Firing Modes (i.e. for some energy weapons you can switch the type of laser it fires)

#### Features I'd like to have but aren't really necessary for balance:
- Bullet penetration (pierces through walls/vending machines/windows)
- Ricochets
- Homing bullets
- Autoejection (would be used on high fire rate/high mag capacity guns)
- Tactical Reloading (should it be allowed per gun or should it be a skill that can be used on any gun)
- Dual Wielding (Firing two guns at once, one in each hand. Can't be done with a gun that doesn't make sense to dual wield/would be overpowered. Dual wielding inherently adds 10 degrees of bullet spread to each gun.)

## Planned gun rebalances (All ballistic guns have unique calibers unless stated otherwise):

# ALL DAMAGE VALUES SUBJECT TO CHANGE

### Universal Changes

- All bullet damage is buffed across the board
- Large weapons have their item size increased, making it harder to carry more than one

### Pistols

#### Theme: Low-Medium damage, high fire rate, good accuracy (10-15 degree spread), large magazine capacity. Makes up for its below-average bullet damage through the high number of bullets it can shoot before needing to reload. Largely ineffective against armored targets unless you have specialized ammo.

**Mk 58:** Common security pistol, statline directly follows the pistol theme. 

Ammo Types:

* Standard ammo (20 Piercing damage, No armor piercing)
* AP ammo (small amount of piercing (20%), good enough to deal with makeshift armor)
* Rubber ammo (3 Blunt, 28 Stamina)

**Viper:** Bucks the large mag capacity trend in favor of higher bullet damage. Syndicate exclusive.

Ammo Types:

* Standard ammo (26 Piercing damage)
* AP ammo (22 Piercing damage, 30% armor piercing)
* IC ammo (12 Burn damage, applies one firestack on hit)
* EMP ammo (15 Piercing damage, causes a single-tile EMP on hit)

**Cobra:** Retains its unique gimmick of innate suppression and caseless ammo, massive drop off in fire rate (2/s) in exchange for boosted bullet damage. Syndicate exclusive.

Ammo Types:

* Standard ammo (32 Piercing damage)
* AP ammo (29 Piercing damage, 50% armor piercing)
* Penetrator ammo (can pierce through up to 2 walls (reinforced walls count twice), 26 Piercing damage)
* Radioactive ammo (Upon hitting the target, bullet discretely injects a small amount of Polonium into the target's chemstream)
* Soporific ammo (Injects tranquilizers into the target's chemstream, causing them to fall asleep after a short delay)

**Makarov:** The new standard issue nuke op pistol. Low mag capacity, low bullet damage, made relevant thanks to above-average accuracy and fire rate. Nuke ops exclusive.

Ammo Types: 
Shares a caliber with the Stetchkin, allowing the Makarov to chamber Stetchkin ammo.

**Stetchkin APS (new):** A 3-round burst machine pistol available to nuclear operatives. Bullet damage and fire rate are slightly lowered to compensate for the burst mechanic, but the base bullet damage is still superior to traitor/crew armaments. Subpar accuracy compared to other pistols. Nuke ops exclusive.

Ammo Types:

* Standard ammo (22 Piercing damage)
* HV ammo (20 Piercing damage, higher bullet velocity)
* AP ammo (20 Piercing damage, 40% armor piercing)
* Devastator ammo (Fragments upon hitting the target, leaving embedded bullet fragments (needs woundmed))
* IC ammo
* Freezerburn ammo (Deals 4 Piercing damage, 12 Cold damage and 18 Stamina damage upon hitting the target)

### Revolvers (All use the .45 ammo caliber, which has innate armor piercing (20%))

#### Theme: High bullet damage, low fire rate, high accuracy (5-10 degree spread), low mag capacity. The antithesis of the pistol.

**Inspector:** Due to being the detective-exclusive revolver, most ammo focuses on disabling targets, but the standard ammo is the same standard round used by Syndicate revolvers. Detective/Cargo exclusive.

Ammo Types:

* Standard ammo (30% armor piercing)
* High-Grade AP ammo (Can only be obtained by a Traitor Detective, exceptional armor piercing (80%) and higher base damage, 8 TC per box of speedloaders)
* Gutterpunch ammo (Low base damage, does some stamina damage, injects the target with a moderate amount of Ipecac, no armor piercing)
* Iceblox ammo (Deals cold and stamina damage, no armor piercing)
* Rubber ammo (3 Blunt, 36 Stamina)

**Predator (renamed Python):** The classic Syndicate handgun. Leans into the revolver theme even harder than other revolvers. Syndicate exclusive.

Ammo Types:

* Standard ammo (30% armor piercing)
* AP ammo (Great armor piercing (60%))
* Nutcracker ammo (Low base damage, massive structural damage)
* Heartpiercer ammo (Slightly lower base damage, good armor piercing (40%) bullet penetrates through first mob hit)
* Metalshock ammo (Low base damage (higher than Nutcracker), causes a localized EMP on hit)

**Reverse Revolver (new):** Traitor Clown exclusive version of the Predator, can only be fired normally by clumsy people and non-clumsy people will shoot themselves in the face (10x damage)

**Deckard:** Rare crew-sided revolver, trades accuracy (20 degree spread) for mag capacity (8), higher fire rate, and the ability to quickly assess how many bullets are left in the revolver. Nanotrasen exclusive.

**Mateba:** ERT/Death Squad exclusive revolver. High accuracy, improved fire rate, and no mag capacity reduction (7), this revolver is among the best sidearms godly favor can buy. Sidearm of the ERT Commander, Deathsquad standard issue.

**.357 Revolver (new):** After years of busted smuggling attempts, Waffle Co. has finally managed to get their infamous revolver onto Space Station 14 by hiding it in a box of moldy pizza inside a box of paperwork inside of a biohazardous materials disposal container. Above-average fire rate, reduced mag capacity (6), massive bullet damage and perfect accuracy. *Surplus crate exclusive.*

Ammo Types (.357 caliber, ammunition cannot be used by other revolvers):

* Waffle Co. ammo (Has a terrifying *60* base damage, higher velocity, and 50% armor piercing to boot.)

**Gyrojet Pistol (new):** The legendary admeme weapon, now made available for Syndicate agents (sort of). *Surplus crate exclusive.*

Ammo Types:

* Gyrojet ammo (Causes a small explosion when it hits something. The explosion is powerful enough to instantly kill an unarmored target with a direct hit, but someone standing 2 tiles away will be almost unscathed.)

### SMGs

#### Theme: Mediocre bullet damage, decent accuracy that rapidly degrades when continously firing (10-20 degree spread in semiauto, 20-30 degree spread in fullauto), high fire rate, high mag capacity, either fully automatic or can use burst fire.

**WT550:** An old, reliable, paramilitary SMG often seen used by Nanotrasen security forces. Has much better accuracy (5 degree spread) than other options, and accuracy will not degrade while firing automatically, but has low fire rate and bullet damage. Can use a 2-round burst setting.

Ammo Types:

* Standard ammo (20 Piercing damage)
* AP ammo (16 Piercing damage, 30% armor piercing)
* IC ammo (14 Burn damage, ignites the target on hit)
* Rubber ammo (3 Blunt damage, 28 Stamina damage)

**Vector:** A modern SMG that has largely phased out the WT550 in most security forces. Has average bullet damage, good fire rate, and decent accuracy (15 degree spread), but accuracy will rapidly decline (maxes out at 30 degree spread) if fired automatically. Has a 3-round burst setting.

Ammo Types:

* Standard ammo (22 Piercing damage)
* HV ammo (20 Piercing damage, higher velocity)
* AP ammo (18 Piercing damage, 25% armor piercing)
* Rubber ammo (2 Blunt damage, 22 Stamina damage)

**Atriedes:** Nuke ops surplus SMG. Takes the SMG theme to the extreme, with the extremely low bullet damage and horrid accuracy (30->45 degree spread) compensated by the above-average fire rate, large mag capacity, and extremely low price. Nuke ops exclusive.

Ammo Types:

* Standard ammo (14 Piercing damage)
* AP ammo (11 Piercing damage, 40% armor piercing)
* Match ammo (12 Piercing damage, higher velocity, -20% armor piercing, can ricochet off walls up to 2 times)

**C20R:** The SMG exclusively used by the Syndicate's nuclear operatives. Accuracy is decent but will quickly degrade as it fires (10->20 degree spread), but the much-improved bullet damage and above-average fire rate make up for it. Nuke ops exclusive.

Ammo Types:

* Standard ammo (24 Piercing damage)
* AP ammo (22 Piercing damage, 30% armor piercing)
* HP ammo (36 Piercing damage, -50% armor piercing, leaves shrapnel in the target that causes bleeding)
* Venom ammo (18 Piercing damage, injects 4 units of venom on hit)

### Rifles

#### Theme: Rifles have above-average bullet damage and above-average mag capacity, but have average fire rates and decent accuracy (10-15 degree spread). Great all-rounder.

**AKMS:** Above-average bullet damage and mag capacity, great fire rate compensated for by poor accuracy (20 degree spread).

Ammo Types:

* Standard ammo (30 Piercing damage)
* AP ammo (26 Piercing damage, 40% armor piercing)

**Lecter:** The rifle used by Security, conforms to the rifle theme. Armory/Cargo exclusive.

Ammo Types:

* Standard ammo (26 Piercing damage)
* HV ammo (22 Piercing damage, higher velocity)
* Rubber ammo (3 Blunt, 28 Stamina)

**M-90gl:** A rifle that fires in 3-round bursts and features an underbarrel low-bore grenade launcher. Has higher accuracy (8 degree spread) than the rifle standard. Nuke ops exclusive.

Ammo Types:

* Standard Ammo (28 Piercing damage, 30% armor piercing)
* Phasic Ammo (Will pass through any non-organic material until it hits a organic target. 20 Piercing damage, 70% armor piercing)

### Shotguns (Almost all combat shotguns share the 12g caliber)

#### Theme: High damage, low fire rate, accuracy that is frequently altered by the ammo being fired, and a small mag capacity that is further compounded by manually reloading individual ammo.

#### 12g ammo types:

There are two main types of 12g ammo, Shot and Slugs. Shot will launch a spread of pellets when fired, which have sizeable damage falloff and -25% armor piercing unless stated otherwise. Slugs will launch a single projectile with great accuracy when fired. (All values are subject to change)

* Buckshot (Shoots a spread of 6 pellets (12 Piercing) within 15 degrees)
* Syndicate Buckshot (Shoots a spread of 8 pellets (12 Piercing) within 12 degrees, 0% armor piercing)
* Slug (24 Piercing, 24 Blunt, -10% armor piercing, 10 degree inaccuracy)
* Syndicate Slug (30 Piercing, 30 Blunt, 10% armor piercing, 5 degree inaccuracy)
* Rubber Shot (Shoots a spread of 9 pellets (3 Blunt, 18 Stamina) within 45 degrees. Will bounce off walls once.)
* Beanbag (5 Blunt, 55 Stamina)
* Incendiary Slug (10 Burn, applies 3 firestacks on the target on hit)
* Dragon's Breath (Shoots a spread of 5 pellets (6 Burn, 6 Piercing, applies 3 firestacks) within 20 degrees) (Nuke ops exclusive)
* Cryoshot (Shoots a spread of 4 pellets (14 Cold, 35 Stamina) within 20 degrees)
* Meteorslug (10 Blunt, 10 Piercing, 60 Structural, 120 Stamina, throws mobs backwards on hit) (Nuke ops exclusive)
* Flechette (Shoots a spread of 6 pellets (8 Piercing, 8 Slash, 10 Stamina) within 12 degrees, no armor piercing reduction and greatly mitigated damage falloff) (Nuke ops exclusive)
* Pulse Slug (40 Burn, 80 Structural. Fires a Pulse laser insetad of a slug.)
* Shotgun Dart (Can be filled with up to 20u of any chemical) (Nuke ops exclusive)
* Frag-12 Slug (26 Blunt, detonates a light 1.5-tile explosion around it on hit) (Nuke ops exclusive)
* Penetrator Slug (Low base damage, but has complete armor penetration and will go through an unlimited number of mobs with no velocity reduction) (Nuke ops exclusive)
* Ion Shot (Shoots a spread of 3 pellets (5 Blunt) that EMP everything in a 1-tile radius on hit within 18 degrees)
* Laser Shot (Shoots a spread of 5 lasers (12 Burn) within 25 degrees)
* Improvised Shell (Shoots a spread of 12 pellets (6 Blunt) within 50 degrees)
* Flare Shell (5 Burn, applies 1 firestack on the target on hit)
* Confetti Round (Shoots out a burst of confetti and plays the "yippee" sound effect when fired. A box of them can be found in the Tactical Party Crate.)

**Bulldog:** The shotgun used by Nuclear Operatives, doesn't need to be pumped after every shot, has full-auto capability, and uses externally attached magazines to reload instead of an internal magazine. Nuke ops exclusive.

**Double Barrel Shotgun:** The Bartender's unique shotgun, can hold 2 shells and fire them both without cycling, but has no magazine whatsoever. Can be sawn off, drasticallly reducing the size of the gun at the cost of accuracy.

**Krammerer:** Also known as the riot shotgun, one of the most common shotguns on the station due to the stock of them in the Armory. Can hold 7 shells internally, must be pumped after every shot.

**Enforcer:** A unique shotgun orderable from ~~Prapor~~ Cargo that is chambered in 20g instead of the standard 12g. Designed for riot control and engaging multiple targets. 

Ammo Types:

* Flash Slug (Will flash everyone within 30 degrees of the shotgun user when fired.)
* Rubber Shot (Fires a spread of 15 pellets (3 Blunt, 36 Stamina) within 30 degrees)
* Shredder Shot (Fires a spread of 8 pellets (15 Blunt, 15 Piercing, -100% armor piercing) within 16 degrees)

**Combat Shotgun (new):** A shotgun available in short supply from the Armory and available through Cargo. Identical to the Krammerer except in appearance, and the functionality of not needing to be pumped to fire another shell. Cannot fit in bags.

**Tactical Breaching Shotgun (new):** A compact shotgun found in the Armory and the Warden's locker, intended to be used as a tool instead of a weapon. Made for special 10g breaching slugs that deal high structural damage to targets. Can hold 4 shells internally, doesn't need to be pumped after every shot. Security exclusive.

Ammo Types:

* Tactical Breaching Slug (8 Blunt, 100 Structural, perfect accuracy)

### LMGs

#### Theme: High bullet damage, high fire rate, high mag capacity, poor accuracy. The catch is that accuracy actually *improves* the longer the gun is fired (IC reasoning: Your character is compensating for the recoil & the initial recoil kick of firing the gun has died down), allowing skilled players to strategically position themselves and accurately gun down enemies. Syndicate exclusive.

**L6 SAW:** The LMG used by nuclear operatives. Completely conforms to the LMG theme (30->10 degree spread, reaches optimal accuracy after 1 second of continuous fire), auto ejects magazines when empty. Nuke ops exclusive.

Ammo Types:

* Standard ammo (36 Piercing damage)
* AP ammo (30 Piercing damage, 40% armor piercing)
* HP ammo (48 Piercing damage, -50% armor piercing)
* IC ammo (18 Piercing damage, applies a firestack on hit)
* Match ammo (24 Piercing damage, can ricochet off walls twice)
* Smartmatch ammo (Send your enemies to bullet hell with this extremely premium magazine, which contains bullets (24 Piercing damage, 20% armor piercing) that not only home in on enemies, but can ricochet off walls up to 3 times.)

### HMGs (All share the same ammo caliber)

#### Theme: LMGs taken to the extreme. High bullet damage, extremely high fire rate, massive mag capacity, decent accuracy (10-20 degree spread) that *doesn't* improve over time when firing. Will usually have an item size that prevents it from being put in a backpack, and will require two hands to fire. Syndicate exclusive.

**Minigun:** Two-handed minigun rarely seen on the station. Conforms to the HMG theme (15 degree spread). Admin exclusive.

Ammo Types:

* Shares a ammo caliber with M546 Osprey

**M546 Osprey (new):** A specialized minigun used by nuclear operatives. Usage requires a back-mounted ammunition feeder and a belt-mounted shock absorption harness. Will overheat from extended fire, slowing down fire rate and potentially causing a catastrophic failure in the firing mechanism. Above-average accuracy (10 degree spread), 1000-round capacity. Nuke ops exclusive.

Ammo Types:

* Standard ammo (40 Piercing damage, 30% armor piercing)
* AP ammo (32 Piercing damage, 75% armor piercing)
* HP ammo (54 Piercing damage, -50% armor piercing)

### Sniper Rifles (All use the same ammo caliber)

#### Theme: High bullet damage, low fire rate, low mag capacity, perfect accuracy. One shot, one kill.

Ammo Types:

* Standard ammo (70 Piercing damage, knocks the target down, 100% armor piercing)
* Penetrator ammo (60 Piercing damage, doesn't knock down or dismember, passes through everything it hits.)
* Soporific ammo (Deals no damage, organics hit will fall asleep for 30 seconds)
* Marksman ammo (50 Piercing damage, hitscan with one guaranteed ricochet, 100% armor piercing, stuns if they aren't wearing armor)
* Wallhack ammo (60 Piercing damage, 75% armor piercing, knocks down on hit, can go through up to 4 walls (reinforced walls count twice))
* Match ammo (70 Piercing damage, knocks down on hit, higher velocity, can ricochet off walls up to 3 times)
* Substandard ammo (40 Piercing damage, 50% armor piercing)

**Mosin:** A ancient surplus bolt-action rifle, you have to be really desperate to use this. Low bullet damage, extremely slow fire rate (you have to manually raise the bolt, eject the spent cartridge, and close the bolt to fire again), low mag capacity, and substandard accuracy. Starts loaded with substandard ammo, works with speedloaders.

**Hristov:** The standard sniper rifle in nuclear operative arsenals. Takes magazines, comes with a 1-6x scope, bolt-action. Nuke ops exclusive.

**Longshot (new):** A premium sniper rifle designed for extremely long-range engagement. Takes magazines, comes with a 1-6-10x scope, semi-automatic, extremely loud when firing (will stun anyone nearby who isn't wearing proper ear protection when it fires unsuppressed (the rifle comes with a small suppressor attached)), bullets fired have additional velocity added.

### Grenade Launchers

#### Theme: Low fire rate, low mag capacity, great accuracy. Launched grenades will deal damage in a wide area, with a focus on anti-personnel damage. They can be used as decent anti-structural weapons if you're desperate.

**China Lake:** A single-shot break-action grenade launcher used by nuclear operatives. The high-bore grenade rounds are devestatingly strong, but have to be manually ejected to load a new round in. Nuke ops exclusive.

Ammo Types:

* Blast Round (The standard ammuntion for the China Lake)
* Flash Round (Flashes everyone within 5 tiles when it detonates)
* Frag Round (Anti-personnel round, will launch deadly fragments and cause a minor explosion when it detonates)
* Breach Round (Below-average explosion radius & damage, does significant structural damage)
* Modular Smoke Round (Disperses smoke in a 5-tile radius when it detonates, can have up to 100u of chemicals injected into it (they won't react while contained in the grenade) that the smoke will carry)
* Modular Foam Round (Disperses foam in a 4-tile radius when it detonates, can have up to 100u of chemicals injected into it (they won't react while contained in the grenade) that the foam will carry)
* Sticky Round (Same strength as the Blast Round, will stick to whatever it hits and then detonate after a adjustable amoutn of time. Can be linked to a remote signaler for instant detonation.)
* Armageddon Slug (Will fire a massive shotgun slug that does 60 Piercing and 60 Blunt, has 70% armor piercing, and will penetrate through every mob it hits and a single wall.)
* Doomsday Round (Fires a spread of 40 pellets (12 Piercing, 30% armor piercing, will penetrate through 1 mob, can ricochet off walls once) within 45 degrees)

**C32R MGL (new):** A 6-shot (1.5 fire rate) low-bore grenade launcher used by nuclear operatives. Automatically cycles after every shot, spent rounds will need to be manually emptied. Cannot use the same rounds as the China Lake, but can load low-bore rounds and regular grenades as ammo. Nuke ops exclusive.

Ammo Types:

* Uses rounds that have identical functions to the China Lake's rounds, but with reduced power

**Riot Launcher (new):** A specialized grenade launcher used by security forces. Must be manually reloaded after every shot, uses same bore as C32R. Security/Cargo exclusive.

Ammo Types (these are the ones available to the crew):

* Crowd Dispersal Round (Disperses smoke containing pepper spray within a 3 tile radius when it triggers)
* Flash Round (Will flash everyone within a 2 tile radius when it triggers.)
* Paint Round (Will cover everyone within 1.5 tiles with a highly visible orange paint when it triggers. This paint will leave orange footsteps and can only be washed off in a sink/washing machine or by spraying space cleaner on yourself.)
* Baton Round (Will stun for 1.5 seconds and deal 5 Blunt damage & 60 Stamina damage (so they're slowed when they get back up) to whoever it hits.)
* Smoke Round (Disperses smoke within a 4 tile radius when it triggers.)
* Metal Foam Round (Disperses metal foam in a 2-tile radius when it triggers)

### Rocket Launchers

#### Theme: Low fire rate, must be reloaded after every shot, excellent accuracy. Launched rockets will deal high damage in a small area, with a slight focus on anti-structural damage. It's still an extremely effective anti-personnel weapon if your aim is good and you're willing to waste a ton of TC. Syndicate exclusive.

**MPRT-7 (renamed RPG-7):** Conforms to the Rocket Launcher theme ~~because it's the only one in the weapon class~~. Nuke ops exclusive.

Ammo Types:
* 84mm HE Rocket (Causes a low-yield anti-personnel explosion on hit.)
* 84mm HEDP Rocket (Causes an explosion that is extremely effective against robotic targets, surrounding structures, and nearby personnel.)
* 84mm EMP Rocket (Unleashes a high-frequency EMP on hit, causing severe burn wounds to anyone standing nearby and knocking out electronics in the area.)

### Energy Weapons

#### Theme: pew pew pew, the energy weapon. No longer fires hitscans, instead fires energy projectiles. Low fire rate, medium-high shot damage, varying magazine capacity, must be recharged instead of reloaded.

**Laser Gun:**
* 16 charges, laser does 20 damage, fire rate of 1.5

**Hellfire Laser Gun (new):**
* 10 charges, laser does 25 damage & applies two firestacks, fire rate of 1

**Pulse Pistol/Pulse Carbine/Pulse Rifle:**
* 20/50/400 charges, laser does 60 Stamina damage on Disable, 30 burn damage on Kill, and 40 Burn damage & 80 Structural damage on Destroy, fire rate of 2

**Laser Cannon:**
* 10 charges, 40 Burn damage, fire rate of 1

**X-Ray Cannon:**
* 12 charges, laser does 15 Burn and 15 Radiation damage, fire rate of 1, laser goes through walls

**Antique Laser Gun:**
* 10 charges, self-recharges a charge every 2.5 seconds, laser does 40 Stamina damage on Disable and 25 Burn on Kill, fire rate of 2

**Advanced Laser Gun:**
* 8 charges, self-recharges a charge every 5 seconds, laser does 20 Burn damage, fire rate of 1.5

**Ion Rifle (new):**
* 5 charges, laser causes a 2-tile EMP, fire rate of 0.5

**X-01 Multiphase Energy Gun (new):**
* 20 (Disable)/10 (Kill)/5 (Ion) charges, laser does 60 Stamina damage on Disable, 30 Burn damage on Kill, and causes a 1-tile EMP on Ion, fire rate of 2
