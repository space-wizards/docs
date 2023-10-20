# Roadmap For Atmospherics

## Background

Most atmos players currently agree that atmos is not very fun to play, for some of the following reasons:

1. There is little content to play after round-start setup. Part of the problem is that things like distro and TEG are "set up and forget".

2. Atmos can't actually rectify atmos problems in a reasonable amount of time. For example, if there actually is a plasma leak, scrubbers typically work too slowly resulting in the plasma inevitably being lit before it can be cleaned up.

3. Atmos techs don't play with the rest of the station, preferring to isolate themselves to produce a funny green gas that is only particularly useful for shuttle bombing. Mechanics like this violate the [fundamental design principles](en/general-development/feature-proposals/ss14-fundamental-design-principles.md). While these mechanics shouldn't be removed per-se, more focus should be given to mechanics that increase interactions with the station, like making sure the air is breathable and well-heated.

## Proposal

Make atmos more fun to play by adding more challenges and processes semi-inspired by real life.

**An atmos tech's primary job is to keep the station livable and breathable.** There are a lot of interesting real life challenges associated with making this happen, not in the least of which is that in space, every gas molecule wants desperately to escape into the cold of space. There is also the challenge of keeping the station appropriately temperature-regulated despite the cold outside and occasional plasma fires inside.

Where it does not conflict with fun (see below), **incorporate realistic processes and simulations**. As stated in the [fundamental design principles](en/general-development/feature-proposals/ss14-fundamental-design-principles.md), intuitive simulation makes for a better game. Having real-life analogs for gas behaviors helps make both atmos more discoverable and intuitive for new players and also caters to atmos nerds.

None of these realism additions require any sort of math to play. Only a basic understanding of the following principles should be enough to understand and play:

1. You should not be able to spin energy out of thin air.
2. When given a choice, gas flows from high pressure to low pressure.
3. When given a choice, temperature transfers from hot to cold.

### An Interlude on Realism

The chief objective of a game is to be fun to play, and not to be realistic. Where realism conflicts with fun, fun should be chosen every time.

**However,** games are most fun when players have a sense of agency (their actions matter in determining the final outcome of the game) and when their challenges are struggles are believable.

In order for players' challenges and struggles to be believable, the game universe must obey a consistent system of rules and physical limitations. It would not be fun if players have a way to *deux ex machina* out of every imaginable problem (e.g. Nukies? Why don't we use the magical remote control that makes all the nukies disappear? After all, we have *spess magic*.) We're in space, and it should be hard to get gases because they tend to escape into... you know... space. Not every station should have a magical gas miner.

But guess what? It turns out that realism provides both a set of interesting problems and a set of rules for how a universe should consistently behave. So by making things more realistic, we get both interesting mechanics and a set of consistent rules for free. Of course realism doesn't trump fun, and if it is fun to make something that is unrealistic (e.g. plasma gas), then we should always pick fun. **However, where realism does not conflict with being fun, then we should opt to be realistic because it provides a set of interesting problems and consistent rules.**

After all, why do we say that *PV=nRT*? Shouldn't we make up a different gas law because realism is bad?

## High-Priority Proposals

These proposals should be implemented first, because they have an outsized impact on atmos balance as a whole.

- **Phase out gas miners for all upstream maps.** It doesn't make sense that all stations have free and plentiful sources of gas, otherwise you might as well be on a planet. This is a game that is literally set in space. It would make sense to keep a few specialty miners, e.g. for plasma, if a station is set on a plasma mining planet. But in general, all other gases should be imported via gas canisters. Miners should still be kept available for any forks that choose to use them.

    - This solves problems (1) and (3). Maintaining a livable atmos would involve work during the round beyond setting up distro to pipe gas from miners. It would help increase interactions with other departments, such as cargo and salvage as atmos needs to order gas.

    - Ensuring a appropriate round-start supply of gas would make the game playable without a functional cargo department.

    - This would discourage fighting fires or atmos problems by wholesale spacing a section. There is currently very little downside to spacing a section to get rid of problems because of an unlimited gas supply.

    - There is [overwhelming consensus on mappers for this](https://discord.com/channels/310555209753690112/770682801607278632/1162179968915210280).

  - As an interim or for very low pop-count maps, keep miners but make them mine gas at low temperature that has to be heated up before use. This preserves a bit of an incentive for atmos players to not space a section at the first sign of trouble.

- **Globally increase MaxTransferRate** for devices that are not flow-based, e.g. pumps.

  - This solves problem (2). Among other things, it would make scrubbers and other devices actually useful for combating atmospheric problems. Currently players prefer to just space everything. Increasing this would provide a feasible alternative.

## Medium Priority

- **Make all atmos devices flow-based.** This means driving gas flow as a result of pressure differences created using pumps. The specific offenders are currently any "pumped" device that is not a dedicated pump, e.g. air vents, scrubbers, filters, and mixers.

    - This addresses an issue about atmos intuition and accessibility. Players should not have to understand the internal workings of the pipe net system (e.g. a pipe is one big node, gases move between them). In real life, a fan or pump creates a pressure difference, and pressure differences drive gas flow. If you blow on one end of a straw, you can expect it to come out of the other end, not get stuck in a pipe net.

    - This also addresses (2). Instead of having a fixed upper bound on volume transfer, transfer rates would always depend on the pressure difference that you create.

- **Add maximum temperature and pressure limits for most devices.** It does not make sense that you can contain the surface of the sun in your pipes. Adding limits would encourage designing processes and systems that work within reasonable constraints.

    - Some "sub-optimal" setups are really unintuitive and wouldn't work in real life due to temperature and pressure limits.

    - There are some concerns about being able to run burn chambers and the TEG. The screenshot below demonstrates a TEG that is capable of powering an entire large-sized station (256.8 kW current output, the peak output is quite a bit higher) with a maximum pressure excursion of 1600 kPa. It shows that pipes that burst at reasonable pressures are entirely consistent with having burn chambers. You just need to set them up correctly.

      ![image](https://user-images.githubusercontent.com/3229565/274441724-712f4ebf-7440-4d81-879e-19aa29788822.png)

    - This addresses problem (1), the "set up and forget" issue by adding temperatures and pressures to monitor. It also allows the opportunity for sabatoge.


- **Make heaters and freezers thermodynamically sound.** Keeping a station properly heated or cooled is actually a substantial real-life problem. Why deprive atmos techs an actual challenge that keeps gameplay interesting? Because of the existence of generators like the TEG, keeping things thermodynamically balanced is also a great way to prevent infinite power hacks.

## Low Priority

- **Make station air flow-based.** Currently, air vents release air when the pressure is too low, and by default scrubbers only scrub waste gases. So if for some reason the station gets cold, there's no easy way to cycle the air out and heat it up. Of course, you could set all the scrubbers to siphon, heat your distro, and then set the air alarm to fill. But that would just be describing a bad way of doing what real life HVAC systems have always been doing: keep the air flowing.

    - This addresses problem (2) by making it possible to better regulate station temperature.

- **Make heaters and freezers binary.** Just like your central heating and air conditioning circulate air through heat/cold coils, gases should flow across heaters and freezers in order to exchange temperature.

- **Adding process-based alternatives to scrubbers and filters.** For example, with gas reaction-based scrubbing processes, scrubbers with limited uses, or physical processes.

    - This addresses problems (1) and (3) by adding more content that is directly related to the well-being of the station.

    - One of the most pressing challenges in the real world is "how do you separate different kinds of gas." Most current methods of gas extraction are based on chemistry (e.g. real life carbon dioxide scrubbers contain chemicals that react with CO2, pulling it out) or physical methods (e.g. fractional distillation, where you cool down air in different stages to get liquid nitrogen, oxygen, etc.) This creates a lot of opportunity for new game play mechanics and industrial processes. This would also give more opportunities to add gas-based reactions (i.e. more content).

    - This does not advocate for removal of scrubbers and filters, but rather makes it a mapper option, e.g. whether to use scrubbers at round-start or make atmos set up a system depending on the desired level of role-play.

    - When set up correctly, these should have much higher processing rates than scrubbers. This should give an incentive to set these up, e.g. on longer rounds, while still keeping scrubbers as an option.

    - This adds "optimization, tinkering, and creation of intricate builds."

- **Add gas condensation.** This would enable fractional distillation and permit conversion between gas and the equivalent reagent.

- **Add pump efficiency curves.** Pumps have to work harder when they create a larger pressure difference. As a result, pumping from 1 atm to 2 atm should be easier (read: faster) than pumping from 1 atm to 10 atm. You could create a multi-stage pump, and indeed, that is what people in real life do, at the trade-off of less throughput.

- **Breaking windows at high enough tile pressure differences.** To handle explosions and resulting space wind without leaning on the explosino system, and to encourage people to design burn chambers with more controlled burns instead of always putting their pedal to the metal.

- **Various QoL improvements** such as the RPD.
