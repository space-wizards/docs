# Entropy in technology research process

| Designers       | Implemented | GitHub Links |
|-----------------|---|---|
| Fildrance		  | :x: No		| TBD		   |

## Overview

Main objective of changes 
 - Make technology researching process less 'dull' and more involving
 - Make the choice of technologies feel important, and make people actually think what they are doing with points
 - Add more meaningful departments interactions with sci
 - Make generating loads of science points viable and positive thing (currently after very small gap -
  it realy does not matter how much you generate, you can buy everything within minutes)
 - Make another way engineers can use extra power they produce for the good of the station (hopefully its not goint to be the only way extra power can be used)

As people got used to science research process it appears that the process of 'buying' technology is pretty blunt overall - you push the button, 
you recieve recepie at protolathe. It feels like process can be improved largely and we can 'squeeze' a little bit more gameplay from it 
using very minor changes.


## Core changes

### Entropy stages and direct research cost
Main change in department work is going to be pretty simple - now technology cost is not plain, it is
going to scale up with every research scientists going to pick. Every technology is going to increase 
'Entropy stage' of the **research server** - an integer number that influences every tech cost. 
Tier 1 technologies will increase Entropy stage by '1', Tier 2 - by '3', Tier 3 - by '9'.

#### with 5000 cost tech

| technologies researched count | next research cost |
| --- | --- |
| | |

#### with 10000 cost tech

| technologies researched count | next research cost |
| --- | --- |
| | |

#### with 30000 cost tech

| technologies researched count | next research cost |
| --- | --- |
| | |


### Ways to mitigate rising research costs

There will be 2 major ways to decrease entropy stage to actually fight back cost creep:
* first is by salv team finding 'right' encrypted disk
on scraps. Disk can decrease Entropy stage by random flat number when inserted into server - (from 0 to 25). Entropy stage could not be less then 0. (future feature for when skill 
chips gonna be added - disks gonna be able to also increase level, only RD can see what disk 'actually is doing' 
by reading extra description).
* second is by constructing Anti-Entropy Engine - device which uses power from station network to decrease Entropy stage.

Anti-Entropy Engine is 
* a constructable device
* t1 engineering research costing 10 000 points
* require HV wire to operate 
* will draw power from network to charge based on settings (slider 5-100 kw draw)
* changing draw rate will require confimration and going to stop charging (but not drawing power) to prevent fast charge rate change abuse
* uses 1 'charge' per 1 Entropy stage to decrease
* requires 20 000 kw in total per 1 charge
* players can set required amount of charges (1-10) to be stored 
* after storing set amount of charges, power draw is disabled and device is ready to be used. Usage is instant.

| power draing | time to charge |
| ---		   | ---			|
| 100kw		   | 20 sec			|
| 50kw		   | 40 sec			|
| 20kw		   | 1m 40 sec		|
| 10kw		   | 3m 20 sec		|
| 5kw		   | 6m 40 sec		|

# Watch where you click

To make technologies that players pick to be researched even more meaningful, researching now will take server time. 
Server is going to be able to research only 1 technology at a time, time will be specified per technology. 
Deeper tech going to take more time, tech that costs more is going to take more time, but also there is going to be exceptions
for game balance purposes (Explosives going to take x2 time).

To make working with research time feel more fluently, researches going to combine into queue. 
Points will be consumed/returned based on adding/removing techonolgies to research to queue, 
Entropy stage is going to be recalculated and applied on adding to queue (so trying to collect many points and queue all 
reasearches is not better then using points as they come).

To (kinda) counteract randomness by which technology options are provided, technologies can be rerolled for random new ones for a flat price of 2000 points, so players could really
choose - to research something not so useful and get rid of it (but it will help in advancing to new tier), or reroll tech and hope something they
are searching for will appear. (maybe add some ways to drop reset cost for 1-2 uses?)

To counteract research times RnD server is going to have gas port - it could 'eat' some cold gas and lower time to research tech. 
Consumption will not be too much, but with lower temperature, research time is going to go down exponentially.
When provided with frezon, research time is going to be instant.

#### tech research time samples

| technology | base research time | using -173°C gas|using -233°C gas|using -273°C gas|
| --- | --- | ---| ---| ---|
| | | | | |

# Not only nerfing

As most of the points in this list seems just nerfing and giving people obsticles and 'something to do', to bring some butter to the bread, 
limit of only 1 discipline with t3 being able to be researched is going to be lifted in favour of 2 t3 technologies. It will be hard thing 
to do considering amount of Entropy stages the first t3 is going to give, but its a good endgame that maybe could entertain people even during 
4+hour shifts.

# Why the entropy

So our RD server takes abstract data and creates technology. It can be considered a lab rat AI (created only for research and not for thinking or talking ofc)
that knows all about our usual tech, but using this data combined with tons of alien/anomalous data it can try to mash numbers togather to create new useful 
for us ways to use conventional tech (gravity gun etc). If it AI that want to be simple but fast, it is going to use quantum computing - hence, work (better 
in our case) with cooling!

And entropy as a merit of of energy dispersal, going to bring problems into our little lab rat AI brain.