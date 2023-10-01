# Maintainer Meeting Notes - Date: 11 Dec 2021
=
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

DrSmugleaf  
Vera  
PJB  
Acruid  
ShadowCommander  
ElectroSR  
Silver


# Do we support grid overlap | metalgearsloth
- Sloth got ganked by ideaguys again
- For planets
- Imagine the effort
- Check if Tomeno is in the meeting
- Sloth: Ignoring planets and assuming they're just coded somehow, what level of grid interactivity do we support on a """planet""". i.e.
- do we support multiple shuttles overlapping
- are cars grids,
- do we support a grid shuttle flying over a car. - what if a mob leaves the shuttle?
- How do we handle collision between the planet and cars or the likes?
- If sloth codes it
- Acruid already coded it and clusterfack removed it why live
- Shuttle flying over car? No, driving a car over the planet is fine.
    - No pseudo-z level
    - No 3d with layering like that.
- Do we want tile based vehicles?
    - CM does an entity tank, way easier
- How do we layer multiple grids on top of each other
    - Any time you want to query for a grid in a point in space you are returning an IEnumerable of grids
    - Way to get foreground/background grid?
    - How do we get the grid, keep them separate and not mix them up
    - Keep a z-index and sort the results to distinguish the grids
    - NO default grids
    - Acruid: Promote grids to entities so they float in space like Godot/Unity
    - Make MapManager a system, collection of grids is entities.
        - Grid ids are an alias to the entity that holds the grid data.
        - Replace grid ids with entity ids.
        - Removing grid ids can be done now "easily" tm.
    - Do it like Rimworld which keeps track of the ground underneath the floor as separate grids on the same chunk.
    - Do we want to support smaller grids (like space engineers)? We can but it scales with an integer and the default is 1 > can be fixed
    - If someone really wants to support grid vehicles yes but it's a lot of work and effort, entities is easier, if anything should be a long term goal.
- Collision: Normal collision between vehicle and wall, really complicated box2d does not handle it.
    - Use different collision groups maybe.


# Pulling tile sized entities through airlocks | ShadowCommander
- How should this be made easier
- For players we made the hitbox circular, what do we do for lockers or girders?
- Do we make entities trail behind you like in RPGs?
- Make them less than tile sized.
- Current pulling mechanics or something different?
    - Either make all have hexagon/octagon hitboxes or change hitbox dynamically when pulling.
- Follow pulling?
    - No
- Need a custom constraint in the physics engine to keep a box behind you and aligned to get it through the door.
    - Do it like Zelda a Link to the Past (https://www.youtube.com/watch?v=A6r-625k-Bo)
- How to implement it: https://oraqia.wordpress.com/2014/07/05/tricks-for-2d-grid-based-character-collision-that-can-work-in-3d-too/


# IEntity removal and feature/code freeze | Vera
- [GitHub Link](https://github.com/space-wizards/space-station-14/issues/5733)
- FIX THE CODEBASE
- When do we stop the current feature/code freeze
    - What is exempt from this freeze: YAML, bugfixes, admin tools?
- What do we do with the stable branch after the freeze is over
- Pretty stable right now
- Feature Freeze:
    - Keep feature freeze going
    - Keep nullable entity uid, compile time checks
        - Vera: Replace invalid entity uid checks with nullable null checks instead (if it makes sense) for the most part.
        - Nullable entity uid does not hurt performance.
        - Use nullable entity uid instead of invalid, invalid is if someone weird gets deserialized.
- Engine changes are fine as long as the public API does not change


# ViewVariables refactor (Impromptu) | Acruid
- Do a custom class for the editor, a view like Unity (custom editor for a component).
- https://www.youtube.com/watch?v=RInUu1_8aGw
- MVP/MVVM pattern, build a presenter that pulls the data from the component and the system (lives in the system as a function or separate class).
- Use reflection to autogenerate those classes at runtime.
- Generates the UI components inside the class (if feasible).
    - Worse for performance.
- Component has data, system has functions, bind these together.
    - How do you bind the getter/setter for the UI fields (current VV does this (poorly)).
    - Example: get/set stack size, let VV know these are two separate functions with attributes or hardcode it into the view class.
    - The view class can also be a function, register them through reflection by having the entity system implement a generic interface for a component.
    - This interface specifies the functions required to view/set properties of components in methods.


# EntitySystem proxy methods vibe check | Vera
- [GitHub Link](https://github.com/space-wizards/RobustToolbox/blob/master/Robust.Shared/GameObjects/EntitySystem.Proxy.cs)
- Hide the aggressive inlining from PJB
    - Do not use aggressive optimization, that means it runs faster first few runs, JIT does this anyway after a few runs.
    - It can slow down your code long term.
    - Compiler details etc.
    - Use it in long-running methods that only get ran a few times.
    - It makes it skip some optimizations it otherwise would make if you are not careful.
    - The aggressive inlining is fine (but probably not necessary). Aggressive optimization though...
> The AggressiveOptimization option is meant for very specific cases and should only ever be used when sure that the method being annotated actually benefits from that (possibly running some benchmarks to confirm that). Despite what the name might suggest, this option will not "make your code faster", on the contrary it might very well make it slower in many situations. AggressiveOptimization means that the method will skip the tiered compilation and go directly to tier1. This can be beneficial for methods that are hot paths or long running, but only executed once, so that the tiered JIT wouldn't have time to kick in (for instance, for a complex app initialization method that is run at startup). But skipping the tier0 -> tier1 transition also means that a number of additional optimizations cannot be done by the JIT (eg. removing checks for the static constructor, or inlining static readonly fields). Because of this, in many cases applying this option might actually make your code slower. And regardless, the JIT will often skip tier0 anyway in many cases already (eg. in methods with a backwards branch), so it might very well be unnecessary anyway. Long story short: if you're not 100% sure, just don't use this option in your code.
- It surely has 100% test coverage
- Does it make sense for their names to be different than the ones on EntityManager
    - Rename EntityManager functions??!!


# Engine design SOLID and OOP (Impromptu) | Acruid, Vera
- Keep the APIs simple as possible, the names should be the same
- SOLID principles
- but what about WARMED (Write/Argue/Rewrite/uhh I forgor the rest) this
- Acruid: 2 classes depending on each other bad
- PJB: but consider:
    - Main loop needs to be able to shutdown
    - Main loop depends on everything
    - Multiple things (server shutdown command) need to be able to shutdown the main loop down
    - Not allowed under this model
- Acruid: Use an event to decouple them
    - Inject game manager to command, command calls shutdown on it.
- PJB: You only avoid the loop in abstract OOP terms, you still have a circular dependency linked by an intermediary class with a shutdown method and a shutdown event where the loop listens to the event and everything else calls the method.
- Constructor vs field reflection dependency injection.
    - Acruid: Constructor is only bad in a minimal amount of cases, it makes more sense conceptually so you don't need an Initialize method. Field reflection makes understanding the order in which dependencies need to be instantiated more difficult, for example in tests. It is already done for EntityManager.
    - PJB: It's unnecessary and constructor injection does not fix this, it's a general problem for testing.


# Documentation | Paul
- How do we organize it?
    - Content docs: Brought back by pressure from Moony, fandom wiki is worse than setting it up ourselves. Mediawiki moony has access.
        - Game guides
        - Tutorials
        - SS13 books open up an HTML window for in-game wiki: We aren't doing this.
        - How do we do it? IDK lol moony figures it out
        - EFR is working on book markup, pull wiki pages into the game, write it in markdown.
        - LIGHT THEME OR DARK THEME: moony sorts thi out
    - Content-dev docs
        - Device networks
        - YAML
        - How to interact with entities, components, systems and ioc managersç
        - Mapping docs
    - Engine-dev docs
        - Technical writeups to understand what's going on and the design behind it
    - Do not split content and engine docs, distinguish them properly on the wiki, we don't need 2 separate wiki (wiki.js doesn't make this easy, easier than hackmd)
- Paul found something better than wiki.js for docs
    - We don't know the name it's lost with time ask Paul.
    - We can use outline to replace hackmd, free to self-host, not open-source
- Autogenerated content
    - WikiJS seems to not support templates/macros
    - Dump chemical reactions into the wiki for example, Paul could not figure it out
        - We simply use mediawiki, use a script to parse the data and output the markdown (not possible in wiki.js) (may be possible in mediawiki)
        - Once again ask Paul
    - Moony: "autogen is possible on mediawiki p nicely"
        - JSON upload
- GitHub integration to PR to the wiki when?
    - Content wiki: Don't need it
    - Wiki.js docs: Supported, do it
        - Not compatible with secret docs, port that out and then do it


# Meme idea: UE4-like naming standard | PJB
- https://docs.unrealengine.com/4.27/en-US/ProductionPipelines/DevelopmentSetup/CodingStandard/
- https://www.tomlooman.com/unreal-engine-naming-convention-guide/
- Instead of FooComponent, FooC
- Instead of FooSystem, FooS
- DO IT
- MY KEYBOARD???
- LITERALLY DO IT NO BALL
- vera ain't writing the conventions for this, you people do it just type !conventions on discord and write there very easy very simple
- How far do we take it?
    - FooS, FooC
    - M for manager? MEntity
- Do it in content
- Maybe do(n't do) it in engine
- what about FooS and FooC
- Do suffixes instead so its sorted alphabetically
- One system can handle multiple components
- 1:1 component:system is ass
    - vera was right about atmospheresystem handling every pipe device

![](https://i.imgur.com/4Y2QbhU.gif)


# GitHub issues, feature requests (Mini Impromptu) | Acruid
- They are fine, keep them there unless we agree the feature is dumb then close it.
- Make them a discussion as features are not actionable, issues need to be actionable.
- This is a problem in the engine too.
- Make a bug template for engine issues.


# Admin Log Persisting (Impromptu) | Silver
- We haven't needed to look at old ones so far.
- With bans from years ago we need to look back.
- Keep them.
- At minimum keep every round of logs where someone was banned.
    - Or properly document the (perma)ban.
- Make a schema for logs.


# Roadmap
[Previous Roadmap](https://docs.spacestation14.io/en/maintainer-meetups/secret/2021-11-27-meetup)
- emergency shuttle
    - auto shuttle movement
- gamemodes/antags
    - dynamic
    - nuke ops
        - the nuke is done, nuke ops isn't yet
        - does not work outside dynamic
    - lings?
    - blob?
        - vera loves blob
    - cult?
        - make it as good as vg for pjb
- EL BODY SYSTEM
    - some refactors were done by mirror, still some left
    - surgery died in the war of 1992
- Salvage
    - prototype done by 20kdc and it is good
- Teleporters (Beam me up (Scotty))
    - telescience
- Singularity needs to ACTUALLY WORK
- body system but again
- body system (get smug to code it)
- __***ENGINE EDITOR***__
- Tutorial
    - we implement a wiki, peptide wrote some stuff in-game
    - In game guides
        - Waiting on pretty labels


# Project Zomboid
after I eat
