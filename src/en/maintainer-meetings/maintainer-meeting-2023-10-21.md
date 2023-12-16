# Maintainer Meeting (21 Oct 2023)

**Time:** 21 Oct 2023 18:00 UTC

**Attendees:**
- DrSmugleaf
- EmoGarbage
- ElectroSR
- KeronSHB
- PJB
- Visne
- Jezithyr
- Chief_Engineer
- notafet
- TheQuietOne
- faint

## Audioparams refactor | Sloth
- Take a component with a default variation for example, you can't have any inheritors also use it so you have to manually set it every time which is a pita, or alternatively just do it in code and bulldoze the existing audioparams on the component.
- Ideally we'd be able to specify volume / pitch or whatever on the audio file but also have a global way of setting variation or the likes
- One possible solution is removing audioparams from soundspecifier and leaving volume / pitch on it maybe?


## Cinematic trailer | Jezithyr
- Thread number one (#progress-report-writing): https://discord.com/channels/310555209753690112/1036668046623903815/1044457700026761216
- Thread number two (#maintainers-office): https://discord.com/channels/310555209753690112/1151546015330082867/1155994231417090069
- Thread number three (#contributors): https://discord.com/channels/310555209753690112/1164636218051543060/1164641450563227719
- Do we make a cinematic or gameplay trailer
    - **Gameplay trailer**, cinematic trailer would be nice
- [GitHub issue for trailers](https://github.com/space-wizards/space-station-14/issues/20478)
- **Have somewhere for people to submit replays and timestamps**


## UIControllers and UI reloading | Jezithyr
- [UIController docs](https://docs.spacestation14.com/en/robust-toolbox/user-interface.html#ui-controllers)
- Right now UIControllers listen to an event on the system
- Full state reloading is a pain in the ass, slower and clunkier than just UI
- Do we move UI code to a separate assembly
    - **Yes eventually**
- **Try making them EntitySystems**


## Medical and surgery | Jezithyr
- Wounds, damage is taken by DamageableComponent and handled by other components.
- New items/chemicals for medical should be frozen (any new ones would be removed once the refactor is done, specially around bleeding).


## Generic Entity\<T> monologue | DrSmugleaf
```cs
if (!Resolve(uid, ref comp))
    return;
    
Entity<BuckleComponent?, TransformComponent, PhysicsComponent?> ent;
var (uid, buckle, transform, physics) = ent;
if (!Resolve(ent, ref buckle, ref physics))
    return;

Entity<BuckleComponent> ent1;
Entity<BuckleComponent?> ent2 = (ent1, ent1.Comp);
```


## Entity relations | DrSmugleaf
- Some components have EntityUid fields that may hold deleted entities or entities without the required component anymore
- Entity relations or having a way to register these fields with a delegate would fix this
- How to handle dangling entity references held in components
- idk


## Admin logs archival and current round replays | DrSmugleaf
- **Make archival part of SS14.Admin**
- **Partition by date** (for persistent forks otherwise we would do by round id)
- Sending replays through lidgren requires tcp window scaling
- Easy way is open a link on the browser and then open the replay on the launcher


## UI styling tweaks | EmoGarbage
- Hud redesign
- Some things are ugly, don't fit how the game looks
- Action bar being on the side is slightly annoying
- Having clothing right above the hands gets in the way of putting storage there
- The whole UI theme is very blue which doesn't fit the theme of the resto f the game
- The font is very generic
- **Just do it get an UI designer**


## Early Access Roadmap
- **nothing on this roadmap matters except early access trailer.**
- A trailer for Steam
- gamemodes/antags
    - dynamic [c#16548](https://github.com/space-wizards/space-station-14/pull/16548)
    - wizard
- The game runs like shit how do people play this
    - "IDK but maybe when I fix the watchdog you can figure it out easier" | 09/09/2023
    - "I only played VRChat since last time and VRChat runs like shit so I don't know how people play this" | 23/09/2023
    - "" | 21/10/2023


Crashes / Critical bugs: (when are we moving these to GitHub)
- Crashes the server reliably.
- Something that bricks your client often (needs a client restart).
    - Example: Blackscreens the client until you reconnect.
- If something ruins the round and is disabled because of it.
    - Example: Communal lung bug.
      => till next time
      like and subscribe
      smash that button
      ~~did you know only 6% of contribs join this meeting?~~ According to YouTube's statistics, 
