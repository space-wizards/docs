# Toolshed Examples

This guide covers some basic examples of toolshead commands.

## Interacting with entities

Most of the time that you are interacting with toolshead you are manipulating entities in some way.

### Basics
`ent` is a toolshed command that allows us to return an entity with the provided ENTID. By pipeing the output of the command, we can use it to various things on the entity. Some examples include:

```
> ent 12345 delete
```
Will delete the provided entity

```
> ent 12345 replace PlushieBee
```
Will repalce the entity with the provided prototype, for example, turn it into a bee plushie

```
> ent 12345 comp:ensure Mindshield comp:rm Electrified comp:rm Airtight
```
Will check if the entity has the "Mindshield" component and add it if needed, then remove the Electrified and Airtight components

### Targeting yourself

`self` will always return the entity currently controlled by you.

```
> self rejuvenate / Will heal your character
```

### Entity Queries and Filters

`entities` and `nearby` will return either all entities that exist on the server or entities within a provided tile radius of the input entity. Keep in mind that these require the QUERY permission.

```
> entities
```
Will return a list of all entities on the server

```
> self nearby 20
```
Will return all entities in the 20 tile radius of your character

```
> ent 12345 nearby 3
```
Will return all entities in the 3 tile radius of entity 12345

```
> entities with ZombifyOnDeath visualize
```
Will open an UI with all of the infected people on the station, from which you can either VV or TP to them
```
> self nearby 20 replace PlushieBee
```
Will replace every entity in a 20 tile radius with the provided prototype (in this case `PlushieBee`)

```
> entities prototyped CableApcExtension delete
```
Will delete all LV power cables on the server

The most important commands for filtering the output are as follows:

```
named "STRING"
```
Takes in a list of entities and will filter entities based on their name, this command is compatible with the wildcard `.*`

```
> entities named ".*cable"
```
Will return all entities that end their name with the string "cable"

```
> entities named ".*power.*"
```
Will return all entities that contain the string "power" in their name

```
with [component]
```
Takes a list of entities and only returns entities that have the specified component

```
> entities with MobState
```
Will return all mobs on the server

```
actor:controlled
```
Takes in a list of entities and will return all entities that are currently controlled by a player

```
> entities actor:controlled tp:to self
```
`self` can also be used as an argument - this will teleport all players to your location

```
select [N]
```
Takes in a list of entities and will randomly select n entities from the input

```
select [N%]
```
Takes in a list of entities and will select a percentage of the input

Combining filters together we can do as follows:
```
> entities actor:controlled select 5 tp:to self
```
Will teleport 5 randomly selected players to the entity you are currently controlling.

## Fun commands

### THE BEES WILL CONTINUE UNTIL MORALE IMPROVES:
```
> self rep 10 spawn:on "MobAngryBee" nearby 10 prototyped MobAngryBee select 1 tag:add "DoorBumpOpener" do "makeghostrole $ID \"Queen Bee\" \"Lead the bees!\"" do "rename $ID \"Queen Bee\"" nearby 10 protoyped MobAngryBee not with GhostRole do "makeghostrole $ID \"Angry Bee\" \"You are an angry bee and you want some pizza.\""
```
This command can be split into multiple parts for easier understanding:

- We start off by getting our current character with `self`
- Then for that character we execute the command `spawn:on` 10 times: `rep 10 spawn:on "MobAngryBee"`
    - The `rep 10` part repeats the command ten times, and the `spawn:on` command will spawn a provided prototype MobAngryBee on the provided entity - here that's self
- Then we want to fetch everything in a ten tile radius and filter off the bees we spawned with `nearby 10 prototyped MobAngryBee`
- Once we have all of our bees, we select one of them using `select 1` and add the tag `DoorBumpOpener` using the command `tag:add`
    - Tags are like components that contain no data, `DoorBumpOpener` allows for opening airlocks by walking into them, just like a player would
- Next, for the same one bee, we execute the legacy command `makeghostrole` - the first argument is the ID, the second one is the name, the third one is the description. It's important to use the \ symbol before the quotation mark to ensure it is escaped properly.
- Finally, we rename our bee to "Queen Bee"
- Then we fetch all nine other bees and also turn them into ghost roles, just like we did with the Queen Bee

Now, a way more efficient way to do this would to have two separate commands, one for the Queen Bee and one for the Angry Bees. This is just a demo of how complex toolshed can get.

### GHOSTULARITY:
```
> entities with Singularity comp:ensure MobState comp:ensure MovementIgnoreGravity comp:ensure InputMover comp:ensure MobMover do "makeghostrole $ID \"Singularity\" \"FUCK\""
```

This command will turn all singulos on the server into player controlled ghost roles

### Bee plushie grenade

Have you ever wanted a bee plushie grenade? You can have one with this simple command!
```
> self spawn:on "GrenadeStinger" do "rename $ID \"bee plushie grenade\"" do "vvwrite /entity/$ID/ClusterGrenade/FillPrototype \"PlushieBee\""

```
You can replace the `FillPrototype` of cluster grenades with any valid Prototype. Keep in mind that any explosives you spawn this way will be activated by default, so you might not want to use it to spawn thirty Holy Hand Grenades.

### Put the station into debt

Salvage keeps powergaming? Put the station in debt with this one simple solution!
```
> stations:get do "vvwrite /entity/$ID/StationBankAccount/Balance 1000"
```

Make sure to replace the 1000 with the balance you want to set
Alternatively, you could go into F7 > Objects > Stations, check the stations ENTID and then do
```
vv /entity/ENTID/StationBankAccount
```

## Scripts and You

Scripts can be used to automate certain tasks or commands. To create a new script, you will need to create a new file in your Space Station 14 Data directory. On Windows you should be able to find it under %appdata%, in Space Staion 14/data

The file name should be whatever you want the script to be called. You can edit it with any text editor, just make sure to save it as a file with no extension.

Admins will often have a script to customize their ghosts. Here is an example of one:

```
> self not prototyped AdminObserver do "aghost"
> self comp:ensure ShowCriminalRecordIcons comp:ensure ShowJobIcons comp:ensure ShowJobIcons comp:ensure ShowMindShieldIcons comp:ensure ShowSyndicateIcons comp:ensure Grammar comp:ensure Identity
> self do "vvwrite entity/$ID/Ghost/color '#00D2AD'"
> self do "vvwrite entity/$ID/Description \"GHOST GANG!!\""
> self do "vvwrite entity/$ID/Grammar/Attributes[gender] Male"
```

- The first line makes sure you are an admin ovserver
- Next, we make sure to add any of the components that are helpful for adminning if needed. These show up the job icons, antag icons, mindshields. The `Grammar` and `Identity` components are used later for customizing the aghost
- The third and fourth line set the ghost color and description using `vvwrite` with a path and a value
- The last line changes the pronouns to show up as He whenever someone inspects the ghost.

When you want to run the script in game, all you have to do is use the exec command. If you called the above script "admin", you would run the command `exec /admin`
