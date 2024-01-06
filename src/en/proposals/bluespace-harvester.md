# New machine of fun and destruction: Bluespace harvester
Assembles like a normal car, takes up 3x3 tiles,
and draws a large amount of electricity directly from the generator via HV wires.
It can produce useful items and is also an item of sabotage.

## Research and creation
Her board is available in production after learning the T2 technology "Bluespace Mining",
after which the board recipe in the "circuit printer" is unlocked.
Further it will be assembled like a normal machine,
after completion it can also be taken back apart with the loss of all the points earned by it.

## Points
The machine produces points through electricity consumption,
the number of points depends on the current level of work with a limit of 20.
The higher the level, the more danger, points and electricity consumption.
The optimal power source is Tesla or Singularity (Possibly TEG, not very good at running it)

| Level | Consumption | Points | Points (Emagged) | Danger points | Danger points (Emagged) |
| ----- | ----------- | ------ | ---------------- | ------------- | ----------------------- |
|   0   | 500W        | 0      | 0                | 0             | 0                       | 
|   1   | 1kW         | 4      | 8                | -1            | -1                      | 
|   2   | 5kW         | 8      | 16               | -1            | -1                      | 
|   3   | 50kW        | 12     | 24               | -1            | -1                      | 
|   4   | 100kW       | 16     | 32               | -1            | -1                      | 
|   5   | 500kW       | 20     | 40               | -1            | 0                       | 
|   6   | 1MW         | 24     | 48               | -1            | 4                       | 
|   7   | 2MW         | 28     | 56               | -1            | 8                       | 
|   8   | 3MW         | 32     | 64               | -1            | 12                      | 
|   9   | 5MW         | 36     | 72               | -1            | 16                      | 
|  10   | 7MW         | 40     | 80               | 0             | 20                      | 
|  11   | 9MW         | 44     | 88               | 4             | 24                      | 
|  12   | 10MW        | 48     | 96               | 8             | 28                      | 
|  13   | 12MW        | 52     | 104              | 12            | 32                      | 
|  14   | 14MW        | 56     | 112              | 16            | 36                      | 
|  15   | 16MW        | 60     | 120              | 20            | 40                      | 
|  16   | 20MW        | 64     | 128              | 24            | 44                      | 
|  17   | 40MW        | 68     | 136              | 28            | 48                      | 
|  18   | 80MW        | 72     | 144              | 32            | 52                      | 
|  19   | 100MW       | 76     | 152              | 36            | 56                      | 
|  20   | 200MW       | 80     | 160              | 40            | 60                      | 

Scoring is also affected by whether the machine is hacked or not,
I will mention this separately in the chapter on sabotage. 
The formula looks like this: `CurrentLevel * 4 * isEmaggedComponent ? 2 : 1`

**All accumulated points are lost when the machine is disassembled.**

## Buying
For a certain number of points, the machine is able to create a special box 7 meters from the center.
It will appear with a special effect and sound. There are 4 categories, each belonging to a different department and direction.

|    Name       |  Cost |     Department    |
| ------------- | ----- | ----------------- |
| Biological    | 7500  | Botany & Medicine |
| Technological | 10000 | RnD               |
| Industrial    | 12500 | Engineering & RnD |
| Destruction   | 15000 | Security          |

They mostly contain useful items.
But with a rare chance can get things that can not be obtained in any other way in the game,
or very rarely.

Everything is calculated so that the knocking out of these things was not too frequent,
the optimal work of the miner - level 10. This is 40 points per second,
it is an average of one box in 5-10 minutes.

With a 10% chance a special box in its category with a star may appear.
It is equally likely to contain either something VERY useful (Or just funny) or something VERY dangerous.
It will be closed to command access.
For example, either the Singularity or a toy version of it may fall out of the Industrial Category special box.

**These boxes are distinguishable from normal boxes, so the station will decide whether to risk it or not. And prepare in advance for the consequences**

## Danger points
Generated when the Harvester starts running at danger level 11 or higher (At demag it becomes 6 or higher).
And when the Harvester is operating at a safe level, the points start to decrease. Also points will appear if the harvester restarts,
i.e. it no longer has enough energy to work at a certain level, it will generate 75 points and go to level 0. After that it can be turned on again

When the Harvester accumulates more than 175 of them,
the Harvester will attempt to create rifts with a chance of 8% (At demag becomes 3%).
This does not depend on whether the Harvester is enabled or not.
if you disassemble the harvester, it will instantly create a rift out of the current danger points.

## Rifts
1 to 3 portals appear, and the harvester's hazard points are equally divided between them. At the harvester itself they are reset and start to accumulate again.

Each portal creates a random flesh monster every 30 seconds and can also be destroyed. But once every 0-5 seconds,
the portal tries to "buy" up to 3 monsters from its list if it hasn't spent all its points.
Each monster has its own cost. And the more points the portal has, the more dangerous creatures it can create.
