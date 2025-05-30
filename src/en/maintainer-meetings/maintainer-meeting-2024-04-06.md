# Maintainer Meeting (6 April 2024)

:::info
**Time:** 6 April 2024 18:00 UTC

**Attendees:**
- Vasilis
- Overseer (bot) (playing Wii shop music)
- EmoGarbage
- ElectroSR
- PJB
- Chief Engineer
- Lank
- Julian
- ShadowCommander
:::

## Require Reviews before merging | Sloth
> remove the dismiss review stuff from github:
> * I check other people's reviews are done anyway
> * adds time to pr turnaround and I gotta do a lot
> * moony pushed for it iirc but she not here

* **Can we even turn this off? If we can sure turn it off I guess**
* Use the [userscript](https://github.com/DrSmugleaf/dismiss-all-reviews) smug made until then.

## Power state networking | Sloth
> [c#26472] how do we handle power prediction for stuff like this instead of just bandaiding it
> * do we add a separate shared component like "SharedApcPowerReceiver" that gets networked on power changes
> * do we just add a networked field on the component or smth
> * also applies to batteries (powercelldraw sorta works around it)

* **Yeah just make a component bool for it**
    * **Whoever codes it gets to figure out where to put it** 

## Remove MapGrid TileSize | Electro
> We should kill MapGridComponent.TileSize
> * It would make quite a few commonly used transform & map system methods faster by not having to fetch the component
> * I doubt its even fully supported, chances are  half of the engine would explode if it were sent to something other than 1

* **Removing it is probably fine**
* **Double check with OpenDream**
* **Whispers of wanting to move grid to content anyways, fair since it's highly SS14-specific**

## Design Docs

### Off-station ghots roles | Doru991
* https://github.com/space-wizards/docs/pull/63

**Opinions:**

- **Verdict: barely even counts as calling it a ghost role anymore**
- Ghost bar is neat from Goon.
- Highly-involved off-station ghost role like the derelict station doesn't make much sense. Might as well be a different game server where people don't get an hour of investment interrupted because nukies finally blew up the station.

### Shade Antagonist | UbaserB
* https://github.com/space-wizards/docs/pull/100 💯
* **Verdict: closed**
* Doesn't sound like it makes much sense. Seems too reliant on roleplay and even then doesn't seem particularly enjoyable for either party. I foresee three situations in which this goes:
    * LRP, targeted player doesn't go along with it, gets minorly annoyed by Shade until shade rage quits.
    * LRP, targeted player does go along with it, makes full use of their antag pass (do they get an antag pass??? Are our admins going to weep??), their reward for going along with it is getting round removed
    * MRP (even there it's a stretch), players go along with it, heavy RP, player eventually gets round removed
* There's really nothing in it for targeted player except antag card, minor annoyance, RP opportunities and eventual round removal. Being a traitor gives you all the positive effects.
    * Which, btw, target player NEEDS to opt into this. They can just tick traitor instead
* For the shade itself there is too little gameplay and basically nothing to do. Too reliant on targeted player.
* Some people suggested adapting the idea of possession to a revenant ability

### Wall Worm | Ilya246
* https://github.com/space-wizards/docs/pull/121
* Make sure the worm is on the "side" of the wall, not inside. This limits their movement to be *along* the wall so they can't just noclip through a wall the moment anybody attacks them. Allow them to switch on airlocks and stuff I guess.
    * Maybe make noclipping through walls an ability
* Otherwise seems fine. Mostly just comes down to implementation and balancing details.

### Cargo Postal Update | Hanzdegloker
* https://github.com/space-wizards/docs/pull/145
* Honestly this shouldn't be a design doc in the first place, it's too simple (couple random tat items) to really be objectionable
* Packages should just be wrapping paper from SS13 IMO
* Mail dropoff boxes: are there multiple across the station or is this an object at cargo? If the former, teleportation would be bad so just make it use disposals mailing.
* Make the mail event more interesting maybe: on Delta-V cargo gets a money reward if the mail is opened by the correct recipient (ID-locked envelope, technology). Incentivizes cargo to not just steal all the mail contents themselves and actually deliver it.
* Otherwise looks good

## Current freezes

## Current admin issues
- Ahelp relay does not tell you whether the player has disconnected or not. [23716](https://github.com/space-wizards/space-station-14/issues/23716)
- Ahelp window should tp you to the last character if the player is disconnected [20189](https://github.com/space-wizards/space-station-14/issues/20189)
- Specific admin actions can only be performed on logged in players(e.g. Erase) [23796](https://github.com/space-wizards/space-station-14/issues/23796)

## Early Access Roadmap
- **nothing on this roadmap matters except early access trailer and admin issues.**
- A trailer for Steam
    - ask enrico about the trailer
- [**game admin items**](https://github.com/space-wizards/space-station-14/issues/23246) [c#23985](https://github.com/space-wizards/space-station-14/pull/23985)
- gamemodes/antags
    - dynamic [c#16548](https://github.com/space-wizards/space-station-14/pull/16548)
    - wizard (keron)
- Steam account linking
    - before early access
- The game runs like shit how do people play this
    - "IDK but maybe when I fix the watchdog you can figure it out easier" | 09/09/2023
    - "I only played VRChat since last time and VRChat runs like shit so I don't know how people play this" | 23/09/2023
    - "" | 21/10/2023
    - Miros runs fine | 16/12/2023
        - I am 5 parallel universes ahead of you
    - We have a new Minecraft server it runs fine now (SS14 runs fine, really)
    - Here lies Minecraft long live Satisfactory
    - PJB is skiing
    - It's fine :tm:

Crashes / Critical bugs: (when are we moving these to GitHub)
- Crashes the server reliably.
- Something that bricks your client often (needs a client restart).
    - Example: Blackscreens the client until you reconnect.
- If something ruins the round and is disabled because of it.
    - Example: Communal lung bug.
- Client crash [Getting gibbed/deleted crashes your client](https://github.com/space-wizards/space-station-14/issues/26366)
    - Immovable rod gibbing?

=> till next time
like and subscribe
smash that button
~~did you know only 6% of contribs join this meeting?~~ According to YouTube's statistics, 

## PJB personal roadmap
- Audio rework DONE NO WAY
- Fix infra
- Watchdog rework: testmerges, **better way to get traces from game servers**
- Fix perf oh god
- PJB is reading about window scaling

OwO