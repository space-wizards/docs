# Atmos Roadmap
```admonish warning "Attention: Legacy Documentation!"
This document is ported from before the game-area reorganization and has not been reviewed or updated.
It may not fit with the new design requirements.
```

| Designers | Implemented | GitHub Links |
|---|---|---|
| notafet | :warning: Partially | https://github.com/space-wizards/space-station-14/pull/21954 https://github.com/space-wizards/space-station-14/pull/22358 https://github.com/space-wizards/space-station-14/pull/22468 |

## Background

Most atmos players currently agree that atmos is not very fun to play, for some of the following reasons:

1. There is little content to play after round-start setup. Part of the problem is that things like distro and TEG are "set up and forget".

2. Atmos can't actually rectify atmos problems in a reasonable amount of time. For example, if there actually is a plasma leak, scrubbers typically work too slowly resulting in the plasma inevitably being lit before it can be cleaned up.

3. Atmos techs don't play with the rest of the station, preferring to isolate themselves to produce a funny green gas that is only particularly useful for shuttle bombing. Mechanics like this violate the [fundamental design principles](../../../core-design.md). While these mechanics shouldn't be removed per-se, more focus should be given to mechanics that increase interactions with the station, like making sure the air is breathable and well-heated.

## Proposal

Make atmos more fun and intuitive to play by adding more devices, engines, and processes inspired by SS13 and/or quasi-realism.

**An atmos tech's primary job is to keep the station livable and breathable.** There are a lot of interesting real life challenges associated with making this happen, not in the least of which is that in space, every gas molecule wants desperately to escape into the cold of space. There is also the challenge of keeping the station appropriately temperature-regulated despite the cold outside and occasional plasma fires inside. There is the opportunity to create a lot of game play by recovering from a breach or a station fire.

## Core Changes

Using just the devices that already exist, there are some tweaks that can significantly improve gameplay in atmos by making it possible to effectively respond to events like fires or hull breaches.

- ~~**Globally increase MaxTransferRate** for devices that are not flow-based, e.g. pumps.~~ (implemented in [atmos speedup](https://github.com/space-wizards/space-station-14/pull/22372))

  - This solves problem (2). Among other things, it would make scrubbers and other devices actually useful for combating atmospheric problems. Currently players prefer to just space everything. Increasing this would provide a feasible alternative.

### Device Design Principles

Atmos devices should behave intuitively, as one might expect them to behave coming from real life experiences. This means that player should not need to care, or even be aware, about internal abstractions like the "pipe net". Devices should follow the basic principles that:

1. Energy and matter should be neither created nor destroyed.
2. Gas flows from high pressure to low pressure unless forced by a pump.
3. Temperature transfers from hot to cold. Going the opposite direction requires energy input.

These principles suggest changes to devices:

- Instead of having hard transfer rate limits, **scale transfer based on pressure differences.** This means driving gas flow as a result of pressure differences created using pumps external to the device.

    - This addresses an important issue concerning atmos intuition and accessibility. Players should not have to understand the internal workings of the pipe net system (e.g. a pipe is one big node, gases move between them). In real life, a fan or pump creates a pressure difference, and pressure differences drive gas flow. If someone blows on one end of a straw, they can expect it to come out of the other end, not get stuck in the middle of a pipe net.

- **Add soft clogging (aka pump efficiency curves).** Right now if you have two pumps in series, it is possible for the middle node to appear to be at 0 kPa because the second pump is faster. This leads to confusion and inaccessibility. When pumps get clogged, they also get "hard" clogged which means that they stop pumping altogether.

    - This lets us finally differentiate pressure and volume pumps. Pressure pumps are good at moving smaller quantities of gas across large pressure differentials, while volume pumps are better at moving more volume across smaller pressure differentials.

    - This also improves problem (2) by uncapping transfer rate.

- **Make heaters and freezers binary.** Just like how central heating and air conditioning circulate air through heat/cold coils, gases should flow across heaters and freezers in order to exchange temperature.

    - Heaters and freezers are the only "true" unary devices. Even vents/scrubbers which appear unary actually operate on flow from the tile atmosphere into the pipe net.

- ~~**Make heaters and freezers thermodynamically sound.** Keeping a station properly heated or cooled is actually a substantial real-life problem. Because of the existence of generators like the TEG, keeping things thermodynamically balanced is also a great way to prevent infinite power hacks.~~ (implemented as a part of [atmos speedup](https://github.com/space-wizards/space-station-14/pull/22372))

### Fast(er) Spacing

**Spacing should be fast(er).** Here, "fast(er) spacing" means `0.05 < atmos.mmos_spacing_speed < 1.0`.

At the time of writing, the current "slow" spacing has `atmos.mmos_spacing_speed = 0.05`. A `atmos.mmos_spacing_speed = 1.0` corresponds to the old "instant spacing behavior". This design doc advocates for spacing that is faster than what it is now, but not as fast as it used to be.

This should come with the necessary bits to make it work well in a balanced way, for example:

- Single tile double firelocks for special zones on the station that should be isolated from each other
- Mitigations for mass spacing like hardsuit puncturing (see below)

#### Arguments For (Pros)

- **Makes more intuitive sense.** Recent events has taught us that a door plug blowout even in Earth's atmosphere is quite serious. In space spacing should be fast because that's what makes more intuitive sense. It ruins your immersion if somebody can just casually waltz into space and surive just fine for two minutes.

- **Is better for [Intuitive and Inter-Connected Simulation](https://docs.spacestation14.com/en/space-station-14/core-design.html#intuitive-and-inter-connected-simulation).** Spacing should have serious consequences that that create engaging gameplay/decisions while still being intuitive enough to learn and create new emergent gameplay opportunities, e.g. "I can't go through this hallway because it's spaced, so I have to think of a way to survive by taking a detour through these maints." Spacing should be treated as a serious problem.

- **Is [more fun](https://docs.spacestation14.com/en/space-station-14/core-design.html#seriously-silly).** You should be able to be ejected out of the station at high speed due to the atmos canon effect.

- **Is better for [agency](https://docs.spacestation14.com/en/space-station-14/core-design.html#player-interactionagency).** Antagonists will have better ways to control how players deal with problems by creating opportunities for spacing. Engineers will have more agency to actually fix problems because the result of their actions (or inaction standing around not fixing anything) will have real consequences for the station. Though mass spacing will need to be discouraged to ensure a better experience.

- **Is easier for players to troubleshoot.** It is much easier to identify and fix a big leak than it is to quietly have air leak away and you can't even tell.

- **Doesn't break distro.** See [Areas are spaced too slowly for vents to ever stop](https://github.com/space-wizards/space-station-14/issues/20293)

## New Stuff

This list isn't meant to be exhaustive. Some of the ideas discussed here aren't fully fleshed out. Some of these call for porting mechanics from SS13 with changes as needed/appropriate.

- **A "substation" but for gas,** "gas manifold", distribution station, or whatever you want to call it. This would encourage distro to be at high pressure (for higher transfer rates) but then gas distribution stations scattered around the station would bring it down to a normal pressure that is released to vents. Adds antag complexity and gives atmos techs more control.

- ~~**Add gas condensation.** This would enable fractional distillation and permit conversion between gas and the equivalent reagent.~~ (implemented in [#22436](https://github.com/space-wizards/space-station-14/pull/22436))

- ~~**Space heaters** to correct local temperature problems.~~ (implemented in [#25250](https://github.com/space-wizards/space-station-14/pull/25250))

- **Make station air flow-based.** Currently, air vents release air when the pressure is too low, and by default scrubbers only scrub waste gases. So if for some reason the station gets cold, there's no easy way to cycle the air out and heat it up. Of course, one could set all the scrubbers to siphon, heat their distro, and then set the air alarm to fill. But that would just be describing a bad way of doing what real life HVAC systems have always been doing: keep the air flowing.

    - This addresses problem (2) by making it possible to better regulate station temperature.

- **Adding process-based alternatives to scrubbers and filters.** This calls for adding more gases and gas reactions. For example, with gas reaction-based scrubbing processes, scrubbers with limited uses, or physical processes.

    - This addresses problems (1) and (3) by adding more content that is directly related to the well-being of the station.

    - One of the most pressing challenges in the real world is "how does one separate different kinds of gas." Most current methods of gas extraction are based on chemistry (e.g. real life carbon dioxide scrubbers contain chemicals that react with CO2, pulling it out) or physical methods (e.g. fractional distillation, where one cools down air in different stages to get liquid nitrogen, oxygen, etc.) This creates a lot of opportunity for new game play mechanics and industrial processes. This would also give more opportunities to add gas-based reactions (i.e. more content).

    - This does not advocate for removal of scrubbers and filters, but rather makes it a mapper option, e.g. whether to use scrubbers at round-start or make atmos set up a system depending on the desired level of role-play.

    - When set up correctly, these should have much higher processing rates than scrubbers. This should give an incentive to set these up, e.g. on longer rounds, while still keeping scrubbers as an option.

    - This adds "optimization, tinkering, and creation of intricate builds."

- **Various QoL improvements** such as the RPD.

- **More engines**, but the specifics are left out of here to be their own design doc proposals.

## Wishlist

These proposals are for the long term future. Some of them require other proposals, e.g. to reduce the dependence on research/cargo, before they should be implemented.

- **Phase out gas miners for all upstream maps.** It doesn't make sense that all stations have free and plentiful sources of gas, otherwise this might as well be on a planet. This is a game that is literally set in space. It would make sense to keep a few specialty miners, e.g. for plasma, if a station is set on a plasma mining planet. But in general, all other gases should be imported via gas canisters. Miners should still be kept available for any forks that choose to use them.

    - This solves problems (1) and (3). Maintaining a livable atmos would involve work during the round beyond setting up distro to pipe gas from miners. It would help increase interactions with other departments, such as cargo and salvage as atmos needs to order gas.

    - Ensuring a appropriate round-start supply of gas would make the game playable without a functional cargo department.

    - This would discourage fighting fires or atmos problems by wholesale spacing a section. There is currently very little downside to spacing a section to get rid of problems because of an unlimited gas supply.

    - There is [overwhelming consensus on mappers for this](https://discord.com/channels/310555209753690112/770682801607278632/1162179968915210280).

    - As an interim or for very low pop-count maps, keep miners but make them mine gas at low temperature that has to be heated up before use. This preserves a bit of an incentive for atmos players to not space a section at the first sign of trouble.

- **Add maximum temperature and pressure limits for most devices** such as pipes and canisters. It does not make sense that one can contain the surface of the sun in their pipes. Adding limits would encourage designing processes and systems that work within reasonable constraints.

    - Some "sub-optimal" setups are really unintuitive and wouldn't work in real life due to temperature and pressure limits.

    - There are some concerns about being able to run burn chambers and the TEG. The screenshot below demonstrates a TEG that is capable of powering an entire large-sized station (256.8 kW current output, the peak output is quite a bit higher) with a maximum pressure excursion of 1600 kPa. It shows that pipes that burst at reasonable pressures are entirely consistent with having burn chambers. This just needs to be set up correctly.

      ![image](https://user-images.githubusercontent.com/3229565/274441724-712f4ebf-7440-4d81-879e-19aa29788822.png)

    - This addresses problem (1), the "set up and forget" issue by adding temperatures and pressures to monitor. It also allows the opportunity for sabatoge.

    - This prevents somebody from doing a fusion burn inside a pipe.

    - This would need a station map pipe monitor similar to the new power map.

- **Breaking windows at high enough tile pressure differences.** To handle explosions and resulting space wind without leaning on the explosion system, and to encourage people to design burn chambers with more controlled burns instead of always putting their pedal to the metal.
