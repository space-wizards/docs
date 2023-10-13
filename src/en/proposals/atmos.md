# Roadmap For Atmospherics

## Background

Most atmos players currently agree that atmos is not very fun to play, for some of the following reasons:

1. Most things like distro and the TEG are "set up and forget", which means that after setting up things at round start atmos techs think that they have nothing important to do. (In reality they should be monitoring for breaches and fixing them but whatever...)

2. Because of low transfer rates and slow spacing, atmos can't actually rectify problems in a reasonable amount of time. For example, if there actually is a plasma leak, scrubbers typically work too slowly resulting in the plasma inevitably being lit before it can be cleaned up.

3. Atmos techs entertain themselves by hyper-optimizing setups that produce tritium and frezon, neither of which are particularly enjoyable or engaing for the station to play with (see shuttle tritium bombing, mass frezon leaks). As a result, atmos is kind of detached from the rest of the station, basically playing their own game.

## Proposal

Make atmos more fun to play by:

1. Making the core job requirements more interesting and challenging. **An atmos tech's primary job is to keep the station livable and breathable.** There are a lot of interesting real life engineering problems to making this happen, including the fact that this is a station in space where every gas molecule wants to desperately escape into the cold of space. However, because of a few crutches like gas miners, heaters and freezers that beat thermodynamic limits, and magical devices that separate gases (filters and scrubbers) pretty much remove all of the challenging aspects of what would be a pretty incredible engineering feat.

2. Rewarding players for transfer of knowledge by increasing realism (see below note on realism before you immediately take issue). Making things behave in ways that you could reasonably expect from real life both caters to atmos nerds as well as makes behaviors more intuitive and discoverable. If players who play atmos discover through the game that they like chemistry in real life (and maybe even pursue a career in chemistry), then we should consider it a job well done.

### An Interlude on Realism

Upon hearing the word "realism," many folks turn out to have been professional game designers all their life and say something along the lines of:

> "This is a game, the point isn't to be realistic; the point is to be fun."

I agree with this sentiment completely. The point of a game is to be fun, not to be realistic (that is what simulators are for).

**However,** games are fun when players have a sense of agency (their actions matter in determining the final outcome of the game) and when their challenges are struggles are believable.

In order for players' challenges and struggles to be believable, the game universe must obey a consistent system of rules and physical limitations. It would not be fun if players have a way to *deux ex machina* out of every imaginable problem (e.g. Nukies? Why don't we use the magical remote control that makes all the nukies disappear? After all, we have *spess magic*.) We're in space, and it should be hard to get gases because they tend to escape into... you know... space. Not every station should have a magical gas miner.

But guess what? It turns out that realism provides both a set of interesting problems and a set of rules for how a universe should consistently behave. So by making things more realistic, we get both interesting mechanics and a set of consistent rules for free. Of course realism doesn't trump fun, and if it is fun to make something that is unrealistic (e.g. plasma gas), then we should always pick fun. **However, where realism does not conflict with being fun, then we should opt to be realistic because it provides a set of interesting problems and consistent rules.**

After all, why do we say that *PV=nRT*? Shouldn't we make up a different gas law because realism is bad?

## Concrete Proposals

In no particular order, specific mechanical changes that I think will accomplish goals 1 and 2 are:

- **Phase out gas miners for all upstream maps.** It doesn't make sense that all stations have free and plentiful sources of gas, otherwise you might as well be on a planet. This is a game that is literally set in space. It would make sense to keep a few specialty miners, e.g. for plasma, if a station is set on a plasma mining planet. But in general, all other gases should be imported via gas canisters. Miners should still be kept available for any forks that choose to use them.

- **Make all atmos devices flow-based.** This means driving gas flow as a result of pressure differences created using pumps. The specific offenders are currently any "pumped" device that is not a dedicated pump, e.g. air vents, scrubbers, filters, and mixers.

- **Make station air flow-based.** Currently, air vents release air when the pressure is too low, and by default scrubbers only scrub waste gases. So if for some reason the station gets cold, there's no easy way to cycle the air out and heat it up. Of course, you could set all the scrubbers to siphon, heat your distro, and then set the air alarm to fill. But that would just be describing a bad way of doing what real life HVAC systems have always been doing: keep the air flowing.

- **Globally increase MaxTransferRate** for devices that are not flow-based, e.g. pumps.

- **Make heaters and freezers thermodynamically sound.** Keeping a station properly heated or cooled is actually a substantial real-life problem. Why deprive atmos techs an actual challenge that keeps gameplay interesting? Because of the existence of generators like the TEG, keeping things thermodynamically balanced is also a great way to prevent infinite power hacks.

- **Make heaters and freezers binary.** Just like your central heating and air conditioning circulate air through heat/cold coils, gases should flow across heaters and freezers in order to exchange temperature.

- **Reworking scrubbers and gas filters.** One of the most pressing challenges in the real world is "how do you separate different kinds of gas." Most current methods of gas extraction are based on chemistry (e.g. real life carbon dioxide scrubbers contain chemicals that react with CO2, pulling it out) or physical methods (e.g. fractional distillation, where you cool down air in different stages to get liquid nitrogen, oxygen, etc.) This creates a lot of opportunity for new game play mechanics and industrial processes. This would also give more opportunities to add gas-based reactions (i.e. more content).

- **Add gas condensation.** This would enable fractional distillation and permit conversion between gas and the equivalent reagent.

- **Add pump efficiency curves.** Pumps have to work harder when they create a larger pressure difference. As a result, pumping from 1 atm to 2 atm should be easier (read: faster) than pumping from 1 atm to 10 atm. You could create a multi-stage pump, and indeed, that is what people in real life do, at the trade-off of less throughput.

- **Add maximum temperature and pressure limits for most devices.** It does not make sense that you can contain the surface of the sun in your pipes. Adding limits would encourage designing processes and systems that work within reasonable constraints.

- **Breaking windows at high enough tile pressure differences.** To handle explosions and resulting space wind without leaning on the explosino system, and to encourage people to design burn chambers with more controlled burns instead of always putting their pedal to the metal.
