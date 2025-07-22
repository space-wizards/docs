# Maintainer Meeting (19 July 2025)

```admonish info

**Attendees:**
- Myra
- Slam
- Orks
- Fildrance
```

This meeting was recorded:

{% embed youtube id="twL8VozEGac" loading="lazy" %}

## We have so many error messages, holy shit, the game is literally on fire (Slarti)
I likely won't make it to the meeting, but I don't want to keep this topic waiting for another 2 weeks, so I'll just write some stuff here so that you can read it.

We have an insane amount of error messages on the servers. I'm honestly surprised the game is still running.
![](https://hedgedoc.spacestation14.com/uploads/88b2e2ad-af31-47c2-8a9d-5c2f29350e3f.png)
42000 in the last 24 hours. These aren't new, but a long-existing problem, that has been ignored too long and got slowly worse over time. This is hugely problematic since it drowns out actually important error messages, for example [admin logs were often failing to save to the database](https://github.com/space-wizards/space-station-14/issues/38744) for two and a half weeks before anyone noticed.

First of all, every maintainer should know how to look at the error logs (I only found out recently):
Open Grafana -> Explore -> Select Loki -> Select a timeframe -> Run Query
If you don't have Grafana access you can ask PJB for it (you need to be 18 years old due to PII).
You can filter the logs by server and message type, the above graph is only errors, without warnings and info messages.

We also have the new [#codebase-alerts](https://discord.com/channels/310555209753690112/1391453457701011496) channel that relays error spikes from grafana, but it turns out to be absolutely useless because it's firing non-stop even after reducing the sensitivity.

We really have to reduce these and I already made issues for the most common ones, it would be great if a few of you could help looking into them:
- `Found Invalid Contact Index` [#38844](https://github.com/space-wizards/space-station-14/issues/38844)
- `User [redacted] tried setting local rotation directly without a valid mouse rotator component attached!` [#38399](https://github.com/space-wizards/space-station-14/issues/38399)
- `System.InvalidOperationException: Collection was modified; enumeration operation may not execute` from shuttle impacts [#38408](https://github.com/space-wizards/space-station-14/issues/38408)
- `	
Can't resolve "Robust.Shared.GameObjects.MetaDataComponent"` when networking deleted entities.

The last one is the biggest offender by far and I would like some technical discussion on how to best resolve this.
The problem is the following:
- We have a component with an `EntityUid` or `EntityUid?` as a networked DataField, storing a reference to an entity.
- Somehow, that entity is deleted (for example eaten by the singulo, gibbed, destroyed, recycled etc)
- The component gets dirtied and tries to network the uid. For that it has to get the entity's `MetaDataComponent` to find the corresponding `NetEntity` so it can be send to the client. If the entity is deleted this fails with an error.
- The current convention is that an `EntityUid` always belongs to an entity that still exists, so if it somehow gets deleted we would have to reset the datafield to null.
- This is a problem for probably hundreds of components that can all cause this error (although some are doing this more often than others).

A few possible solutions:
- Add a marker component to the entity we are referencing, and if that component is shut down we set the reference to null. An example [here](https://github.com/space-wizards/space-station-14/pull/38827). However, this adds a giant amount of boilerplate if we have to do this for hundreds of components. And it will become complicated in case multiple components are referencing the same entity.
- [WeakEntityReference](https://github.com/space-wizards/RobustToolbox/pull/5577): This is a new datatype the works as a reference to an entity that may or may not still exist. Code example [here](https://github.com/space-wizards/space-station-14/pull/38684). This has a lot less boilerplate, but we would still have to add resolves and API overloads everywhere, for almost all components that contain `EntityUids`, since entities can be deleted for any reason at any time. This means a major cleanup throughout the repository is needed. Additionally Electro mentioned that this has some performance overhead, so I would like to know how feasible it is to do this on a large scale.
    - It might be best to go this route to have methods to detect when entities are deleted when we don't want them to be. 
- The third option would maybe be to change the convention somehow, so that deleted entities are not being networked in the first place and we avoid the error altogether. I'm not very familiar with the PVS engine code, so I would ask PJB and Electro for feedback on which solution here is the best.
    - `Myra`, `Fil` Largely this should be left up to the head maintainers who are specialized in engine code. They're very good at this and we can certainly leave it in their hands. We should ask them to poke the folks who know engine code well so they can contribute. May want to make this whole thing a forum post

## Having some 'help wanted with THIS' board for contributors would be nice (Fil)

It feels like we dont really have any tools currently to highlight 'areas of the game' / 'tasks' / 'issues' that are of a priority to project, but are not handled by any maintainer in this moment of time. Yes, we are welcoming any good contribution by default, but there are things which we will most likely review and merge out of regular 'queue' of things, because they either bother us much more then regular stuff, or are part of already processed and planned designs. Strike teams were inteded to cover PART of it, but strike forces are centered around certain end goal, that means that routine stuff will be left hanging.
Should we wait for strike teams tooling first to discuss this? github issues and priorities on them can be used for this, but as one of our main communication channels is discord, maybe we could post '10 hottest tasks' there by bot? :(
- `beck`: this is a very fun idea! I think it would be fun. For strike team, is roombas do what your talking about? https://github.com/space-wizards/docs/pull/483. *From chat* Also as a maintainer I personally can never really say "your good to go on that idea" because I don't really have any power over knowing that it'll get past
- `Southbridge`: Workgroups are a great way to also help handle this as well, I also do like the concept of "10 hottest tasks"
- `Slam`: Workgroups would also be good since they can both be reactive and proactive to say where they want the game to go, or to make requests for things to go specific directions.
- `Fil` Some possible issues, the first is procedure and the second is how to actually find these documents/proposals/roadmaps since Github has bad UX. Generally being able to highlight and streamline the things we need or want changed which will have an easier time passing will help a lot. Might want to set up a system to label github issues which can then be scrapped by a bot periodically and posted into Discord. 
- `Several` Might also need to implement "strike teams" to handle specific areas of the project such as tutorialization
- `DarkIcedCoffee` A bot could easily grab all the work group threads and post them in one spot

## The Metashield is dead (Slam)

https://github.com/space-wizards/space-station-14/pull/38953

The Metashield is gone! Scary! 

This topic is included here to inform any maintainer who may have missed it. It will be impacting some aspects of the game more than others; of note is things like stealth items, antag objectives and gamemodes. Will likely be worth nudging Maintainer/Contributor focus towards to ~~finally~~ solve these design issues (don't start bikeshedding here).
- `Soutbridge` I forgot who mentioned this but this should start nudging contributors and maintainers to start making changes to stealth items so they're less likely to get metagamed. 
- `Slam` Some of the meta-shield details have been moved to the regular rules. 

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- Slarti
- Myra
- Scar
- Roomba
- Fildrance
- Southbridge
- Tiniest Shark
- Janet
:::

- [38778](https://github.com/space-wizards/space-station-14/pull/38778) Scurrets get emergency EVA suit access
  (Hotfixed into the last staging branch, so already in the game for 2 weeks, but not part of the stable review yet)
- [38596](https://github.com/space-wizards/space-station-14/pull/38596) Adjust uplink buy button to be under item icon
  - `Slarti`: Better, but still looks a little misplaced. The UI could use some more improvement in my opinion.
- [38667](https://github.com/space-wizards/space-station-14/pull/38667) Janitor Tool: Wire Brush
  -  `Fil`: not a blocker but having some neat sound effect with this one could have been really-really cool...
  - `Slarti`: It has a sound effect when the doafter is complete!
  - `Fil`: and doafter is painfully silent and long! Q_Q
  - `beck`: it would be cool if the sound played while doing the dofater!
  - `Tiniest Shark`: The base sound file was a minute long, I could probably add something easily. Just gotta ask how to add it in at the start.

- [38592](https://github.com/space-wizards/space-station-14/pull/38592) Vox scars
- [38650](https://github.com/space-wizards/space-station-14/pull/38650) Minor escape menu update
  - `Slarti`: The sandbox menu should be adjusted so that both have a similar style.
- [38808](https://github.com/space-wizards/space-station-14/pull/38808) Reducing the amount of space in the gogo hat
- [38549](https://github.com/space-wizards/space-station-14/pull/38549) Golden pai
- [38663](https://github.com/space-wizards/space-station-14/pull/38663) Add Breach of Permanent Confinement to Space Law
- [35514](https://github.com/space-wizards/space-station-14/pull/35514) Branded lighters addition
- [36862](https://github.com/space-wizards/space-station-14/pull/36862) JumpBoots Attempt №2
  - `Fil`: not a blocker -> file name for sound effect seems pretty random, do we keep file names from original commit if we reference it in license? if we dont need it then probably would be better to rename file at some point :|
- [38824](https://github.com/space-wizards/space-station-14/pull/38824) New science unlock: the H.A.R.M.P.A.C.K
  - `Slarti`: I'll be keeping an eye on the balance and how players are using it. For now I made it available in both the sec fab and the protolathe to encourage science to do arsenal research. Might be powerful in the hands of antagonists.
  - `Southbridge`: The in-hands for entities in the HARMPACK hands make them invisible. This might be an issue? Might want to utilize displacement maps for these?
  - `Slam`: It might be good to implement a method to layer sprites to where they can clip sprite automatically, especially for in-hand sprites so spriters don't have to "cut out" the hand. It would be a huge quality of life saver for spriters when it comes to new features like this.
  - `Tiniest Shark`: Worth noting there are a lot of specific 'cut outs' on inhands to represent different styles of being held. A way of keeping that would be nice.
- [38670](https://github.com/space-wizards/space-station-14/pull/38670) Artifact glue reagent
  - `Fil`: needs info on how this will go, it sounds pretty busted and is quite easy to have A LOT of.
  - `Velken`: From playtesting on Vulture, it could really be made more difficult to create
- [38595](https://github.com/space-wizards/space-station-14/pull/38595) Added Vox Heterochromia
- [38243](https://github.com/space-wizards/space-station-14/pull/38243) Parroting Parrots part 1: Help maints! SQUAWK! Maints!
- [38984](https://github.com/space-wizards/space-station-14/pull/38984) Buff parrot learn rates and radio chatter
- [38889](https://github.com/space-wizards/space-station-14/pull/38889) Add VV button to the solution editor
- [38496](https://github.com/space-wizards/space-station-14/pull/38496) fix: wide swings with resistanceBypass now bypass resists
- [38425](https://github.com/space-wizards/space-station-14/pull/38425) Allow pAIs to emote like a borg
- [37824](https://github.com/space-wizards/space-station-14/pull/37824) reduced motion flash effect version 3
- [38813](https://github.com/space-wizards/space-station-14/pull/38813) feat: allow admins to interact under subfloors
- [38104](https://github.com/space-wizards/space-station-14/pull/38104) Operation Remove Gun Bloat
- [35344](https://github.com/space-wizards/space-station-14/pull/35344) Minigun inhands + HMG multihand and slow move speed
- [38902](https://github.com/space-wizards/space-station-14/pull/38902) Add Bolas to SecTech vendor
- [38888](https://github.com/space-wizards/space-station-14/pull/38888) Kobold/monkey AI holograms
  - `Slarti`: Character/Species design question: Should the AI look like a normal animal calling you via holopad? I think this takes away some of the AI's unique visuals, which is something we do have as a requirement for other species.
  - `Fil` i agree, that thing feels off, it should be obvious that AI is calling you and the thing is kinda tricks you in a bad way.
  - `Tiniest Shark`: The AI currently has a Corgi hologram for what it's worth. This was also merged before art approval was given (I probably should have tossed a concern on it). I really want to emphasize that "This was merged before art approval". I gave it post-humously but that was more in a rush
  - `Slam`: We may want to put this up to a vote. Will host a vote for this. Revert/Keep/Abstain 
- [37341](https://github.com/space-wizards/space-station-14/pull/37341) Make more objects spray paintable (Reviving #31328)
- [38464](https://github.com/space-wizards/space-station-14/pull/38464) Rotated turret wall panel sprites
- [32588](https://github.com/space-wizards/space-station-14/pull/32588) Component for clothes to suppress emotes and scream action in general, and the muzzle to suppress vocal emotes in particular
- [38937](https://github.com/space-wizards/space-station-14/pull/38937) Bottle Drink Inhands
- [38634](https://github.com/space-wizards/space-station-14/pull/38634) Hats (and glasses) for pets - Part 1 - Ian and McGriff
- [38971](https://github.com/space-wizards/space-station-14/pull/38971) make ocarina small
- [38972](https://github.com/space-wizards/space-station-14/pull/38972) Add contraband parent to war declarator
- [38906](https://github.com/space-wizards/space-station-14/pull/38906) Vox customization additions (+eyeshadows)
- [38427](https://github.com/space-wizards/space-station-14/pull/38427) make biogenerator not accept low-nutrient plants
  - `Fil`: wont it make harder to get rid of useless plants?
  - `Slarti`: You can always compost them.
- [38986](https://github.com/space-wizards/space-station-14/pull/38986) New holy books
- [39000](https://github.com/space-wizards/space-station-14/pull/39000) Remove the Qur'an
  - `Slarti`: Should we have any real religious items in the game? This is a very sensitive topic, especially if players are joking around with them. The current ones we have are the the tanakh, the bible, the druidic tablet, the communist manifesto, the satanic bible and the codex nanotrasimus. From these I think most are fine, but I'm not sure about the first one. We could also consider renaming the bible to "space bible" to move it further away from real religion.
  - `Janet`: ^ anything Actively Sacred should be avoided, but cultural/non-sacred markers of religion are fine, although one needs to be cognizant of the possibility of adding the ability to do hate crimes to the game, i.e. some religious garments should probably be markings or otherwise unremovable
  - `Slam`: We have also removed references to real-world events. Religion is a very specific real-world concept. We have space communism, but not actual communism, it's referencing the thing but it isn't actually the thing. Overall this should be a way to express your character and if our representation is offensive then it shouldn't be included. We certainly do want to have some variation and options rather than simply the christian bible, since before we had nothing. But we should also go through each of these and decide if it helps with expression or is inapropriate. 
  - `Fil`: Is this a blocker? `Slam`: No.
- [38295](https://github.com/space-wizards/space-station-14/pull/38295) Made the Mosin bayonet usable.
- [38700](https://github.com/space-wizards/space-station-14/pull/38700) Moproaches
- [38384](https://github.com/space-wizards/space-station-14/pull/38384) Give admin bags explosion resistance
- [38860](https://github.com/space-wizards/space-station-14/pull/38860) Inconsistent Produce Inhands Fix
- [39033](https://github.com/space-wizards/space-station-14/pull/39033) Carps Can No Longer Suicide
- [39032](https://github.com/space-wizards/space-station-14/pull/39032) Make diagonal windows prevent electrocution
- [38868](https://github.com/space-wizards/space-station-14/pull/38868) Wearable banana peels
- [38319](https://github.com/space-wizards/space-station-14/pull/38319) NPC spiders sometimes spin webs 🕷️🕸️
- [36425](https://github.com/space-wizards/space-station-14/pull/36425) Add supercritical sounds for ALL anomalies


Worth mentioning:
- [38918](https://github.com/space-wizards/space-station-14/pull/38918) Fix firelocks failing to drop fast enough
  - Roomba is a hero! (slarti)
      - the prs will continue until engineering and atmospherics morale improves
- [38953](https://github.com/space-wizards/space-station-14/pull/38953) Metashield Rules Update (Removal)
    - Just wanted to mention I moved this into staging as it was intended to be in stable. (Myra)
- [SS14-ISSUE-39050](https://github.com/space-wizards/space-station-14/issues/39050) Database FATAL error on db initialization server startup
    - Check to ensure if the fix has been made and cherry-picked into staging, otherwise this is a BLOCK (Myra)
        - Handled by me ~~Kono Dio Da~~ (Myra)

arf arf :3
