# Ship guns [Veritius, Unapproved]
this isn't finished

## Different kinds of turrets
### Gimbal
Gimbal turrets can rotate around an axis, allowing faster response rate as the ship itself does not have to move. Gimbal turrets are usually less powerful than their mounted counterparts.

### Mounted
Mounted turrets are mounted to a grid, requiring the ship itself to be oriented to fire. Mounted turrets are significantly more powerful than their gimbal counterparts.

### Lasers
Laser turrets are infinite ammo (as long as you have enough power) but low damage and completely ineffective against armor. Their instant travel rate makes them well suited to shooting down slower projectiles.

### Autocannons
Autocannons are good for close quarters combat, and have very large ammo supplies. They do significant damage, but don't penetrate armor very well.

### Torpedoes
Torpedoes are extremely slow moving projectiles with very large payloads, usually designed to defeat armor or damage internal spaces.

#### Payloads
Torpedoes may be loaded with payloads (such as chemical payloads)

### Railguns
Railguns are extremely powerful weapons that have a slow fire rate, are usually single shot, but do immense damage, move very quickly, and go through armor like it isn't there.

#### Shells
Railguns may be given special shells, but most notably, a storage shell that has EntityStorage. This means you can fire rotting corpses at other ships. And you thought launching corpses into enemy fortifications stopped being a valid strategy centuries ago. You could probably get in the shell yourself, but the G-forces will probably be less than helpful.

## Armor
I think an armor mechanic would be helpful. Though I don't have the expertise to code this.
Something like different walls being better at stopping projectiles. Like regular walls being worse than reinforced walls.

## Energy Shield
FTL13 shields? Thingy around the grid, it can stop kinetics but not torpedos. It can also stop beam (continious)

Shields require plasma (piped) and power to run.
EMP Shells or continious shooting can break a chunk of shield
<!-- add more stuff here -->

## Modular ship guns
In short: **no**. I don't think this can be made anything but nerdbait. Go play [FTD](https://store.steampowered.com/app/268650/From_the_Depths/) instead.

## funny table
This is a table of different kinds of turrets and what role they'd play and on what kind of ships you'd mount them. (i probably fucked up the ship names and shit, i'm not a naval nerd pls no bully)
| Weapon Type | Light Gimbal                  | Heavy Gimbal            | Light Mounted     | Heavy Mounted       | Superheavy                |
|:-----------:| ----------------------------- | ----------------------- | ----------------- | ------------------- | ------------------------- |
| Laser       | Point defense/shuttle weapons | Fighter/shuttle weapons |                   |                     |                           |
| Autocannon  | Fighter weapons               | Corvette weapons        | Frigate weapons   | Destroyer weapons   |                           |
| Torpedo     |                               | Frigate weapons         | Corvette weapons  | Destroyer weapons   | Super-dreadnaught weapons |
| Railgun     |                               |                         | Destroyer weapons | Dreadnaught weapons | Super-dreadnaught weapons |


## ship to ship combat gameplay
Ships could either be designed with broadside cannons or one main cannon infront (this would require the ship to turn)

Ships can try and "track" other ships and maintain bearing, you can either add or remove degrees if its a small one (because kinetics dont fly at the speed of light)
<!-- add more stuff here -->


## Implementation

### Energy Shield
Same as FTL, thing which wraps around the station. Maybe could get the station hitbox, scale by .4(?) and have it be a "priority" on missile/kinetics hitreg
Shield has it's own hp and strength ie how much will it dampen the dmg from `0`-`4`

Each 'health point' is 100, damage formula: 
```
d = damage
m = missile/kinetic/whatever damage (replace with v)
h = shield strength
d = (m/h) - m
```

### Missiles
Missiles can either aim _inside_ the ship or outside (hull) Armor and shield calculations still apply

### Misc
Penetration mechanic based on object speed (v), maybe make shield slow the kinetic/missile(?) (cannot slow down railgun though, only armor can)
