# Joker Roles

| Designers | Implemented | GitHub Links |
|---|---|---|
| mith | :information_source: Open PR | TBD |


## Overview

The core idea is adding a diverse selection of low-stakes roleplay-inclined gimmick jobs. At roundstart 1-2 (map dependent), will be randomly selected from the larger pool, will have a room bespoke to the job appear in a pre-established 'template room' on the station, and will become available for players to take.

## Background

Gimmick jobs are a pretty common thing in Space Man Games; various servers in ss13 have barbers, boxers, clerks, journalists, psychiatrists. In my opinion and experience these jobs are divisive; there's often a handful of people who enjoy them sometimes, and a much larger contingent of people who point out that the roles are dumb, often completely unintegrated into the larger mechanical ecosystem and amount to little more than a greyshirt in a costume. 

I think the key is novelty; these jobs are often fun to play or interact with once or twice, but quickly lose their luster. This proposal is intended to allow for the kinds of fun roles people want to play one time, but probably wouldn't play every round as, without creating role bloat or half-baked jobs that people just use as assistant+. This would also be a good, low-stakes way to trial new roles, or put in roles that are kinda stupid conceptually.

## Details

![lil_room.png](../../../assets/images/jokerroles/lil_room.png)

These little rooms right here, the kind that you have in hallways, often near arrivals, would be the mechanical basis of the implementation. Similarly to how tg13's holodeck works, the idea would be to, on roundstart, swap out the contents of the room with one of a number of pre-designed prefabs. The walls should also be included in the prefab, as this way windows, counters etc can be added or removed. If joker roles are disabled by config, or for some reason don't spawn, the room should default to a standard Vacant Office layout. I'd like to specify that I do like these rooms, and dont think this should replace all of them - maybe we could make a few more scattered about.

The rooms in question would be unique to the job. I'll include a list of joker roles I think we should have below, but some simple examines might be a veteranarian would have a simple surgery, some basic meds, some animal boxes and maybe a defib locker; a private investigator might have a desk with a bottle of whiskey, some glasses, a wardrobe with a couple outfits and forensic equipment, file cabinets, and detective-carpeting; a store clerk could have a shutterable windoor counter, sellable stock, a locker with some cash. In this way, each role would have their own slice of the station, with access to equipment they would be able to use in a way that feels integrated and intentional.

I can see two ways this could work across maps; firstly, the lower effort method, would be to have standard map-agnostic room templates with a matching footprint - all the mapper would need to do is ensure that the room matches the 'joker room' dimensions - say 6x4 or smth - and mark the room out somehow, and it would load the same room contents for each type of room across whichever station it's on. This would be low-maintenence and scalable, wouldn't ask much compromise from the mappers, and would (presumably) be simpler to implement.

The second implementation would be that a station mapper can opt to make a joker room template distinct from the default footprint, and would then create a bespoke version of each of the job-rooms that would fit into that template specifically. This would allow for more variety and freedom, with any given joker role having a few different room styles across different stations, but this could also work alongside the simpler method as a default.

In terms of job selection, this would work similarly to how station-dependent jobs work right now; players can access the full list of joker roles in the job preference menu, specify their interest in the role, at roundstart the jokers would be picked prior to job assignment, and the jobs would be entered into the selection process as normal, using a spawn point within the room. If a role goes untaken in the initial assignment, it'll be available on the join menu. The jobs will include their own access level - if possible, this access would be dynamic; only appearing on the HoP console on rounds where the relevant job is selected, this will control access to any lockers and doors in the room.

If mappers want to go Sicko Mode, template rooms could be placed in and around other departments with a selection of roles from the larger list they can select - for example psychiatrist, veterinarian or plastic surgeon rooms could spawn in or around medbay. If this were the case, I'd suggest limiting the numbers so if a role spawns in a department-specific position, a generic template would remain empty so as not to tip the scales.

Most of these roles equipment could be designed from existing clothing and items; while in some cases it might be fun to add new items for them, it absolutely wouldn't require any item bloat and could add some more use for items that don't see much use currently.

Seeing as some of the jobs are a little abstract, it would be good to include a *brief* flavour text on spawn to outline what the job is and, probably more importantly, what it isn't.

## Examples

Here's some ideas and brief concepts for some of the roles that I think would work well here.


_Clerk_

Room contains lockable storage for sellable goods of moderate utility, a safe, a desk with some basic paperwork supplies, and a front desk with a windoor and button-toggle shutters. Items in storage could be drawn from a random pool or fixed, but would be maint-loot tier; yellow gloves, syringes, crowbars, white medkits, toolbelts, plushes, nonlethal ammo. Intended playstyle would be trading and upselling until you're buying and selling items of genuine value with a safe full of spesos. Could spawn in pretty much any outfit, so long as it looks civillian.

_Plastic Surgeon_

Room would be a surgery with all the standard tools, and some basic meds. Anaesthetic tanks, medical records console, patient locker etc. This role would obviously only make sense when we've got newmed. Intended playstyle would be performing minor or stupid surgeries on-demand. Would spawn in some variant of the medical outfit, intended to distinguish the surgeon as private and independent from medbay at large.

_Boxer_

Locker room with a shower, seating, some bruise packs, change of shorts and gloves, sink with a mirror etc. In a larger joker template it could include a small boxing ring, but would be unfeasable if the room is as small as I'm picturing the defaults. Intended playstyle is the same as the current boxer really, would spawn in shorts and gloves.

_Magician_

Curtained room with cool carpets and lockers - might include a teleporting locker. Starts with a number of prank items, some chems for making smoke etc, magic wand, a small animal of some kind. Intended playstyle is basically a variant clown, putting on shows etc. Spawns with a top hat etc you know how a magician dresses.

_Gambler_

Carpeted room with some of those green tables, decent starting cash, dice, arcade machine maybe, small bar with drinks. Spawns in a hawaiian shirt with obnoxious sunglasses. Intended playstyle is gambling away that money obviously.

_Private Investigator_

Similar to detective office with different noir outfits and no gun. A desk with whiskey and glasses, CCTV monitor, forensic equipment, camera (when we get them), audio recorder, bureaucracy equipment, one of those emergency sec radios but not an earpiece, evidence bags etc. Intended playstyle is a second sleuth on the station, can be hired by crewmates or can simply try to do the detectives job for him, but critically is not a member of sec and isnt authorised to carry a gun or anything. Spawns in a suit maybe, something noir that isn't one of the detective's.

_Journalist_

This is basically already a thing on some maps; room with paper and desk, camera, outfits etc etc. You know how this one works.

_Veterinarian_

Stripped down doctors office with some bruise packs, ointment, and bottles of watered-down pills. A surgical table, some chairs for pet owners to sit in, animal boxes and wall defib. Intended playstyle being a doctor for animals. Spawns in something medbay-adjacent.

_Centcomm Liason_

Room is a fancy office with a wardrobe, nice desk, centcomm carpets, fax machine, camera console. Isn't a member of command and doesn't spawn with access, is there to monitor the station and report to centcomm, not to take command of the station unless it happens organically. Spawns in a centcomm outfit.

_Psychiatrist_

Room is a psych office. Again, this is a job we have currently that I think would benefit from not being a permanent fixture, but would function the same.


Anyway that's all I got for now. I put it in service cos its mostly service roles.