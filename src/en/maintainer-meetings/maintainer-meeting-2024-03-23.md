# Maintainer Meeting (23 March 2024)

:::info
**Time:** 23 March 2024 18:00 UTC

**Attendees:**
- EmoGarbage
- Vasilis
- Julian
- PJB
- ShadowCommander
- TheQuietOne
- Notafet
- ElectroSR
:::

## The Great Map Culling - EmoGarbage

* we have a lot of maps. Emisse maintains all of them and is going to die and go patrick bateman on the repo
* most of our maps are pretty same-y
* it's hard to maintain decent quality across like 14 maps since reviewing them is time consuming

The Proposal:
* cut maps down to 2 lowpop / 2 midpop / 3-4 highpop
* get PJB and some map nerds to do a bigass review doc like before
* maybe get some volunteers to spend a day going through maps and really brushing up quality
* go over map standards again and tighten them up
* integrate random maints rooms since we have the tech 

Decision:
* **Normalize view that everybody can edit maps, at least for small changes -> remove need for somebody to "maintain" a map specifically.**
    * **Maybe need to fix map saving to avoid making huge diffs**
* **Needs better map issue reporting.**
    * **In game bug report form, category for "I want to report a map issue" -> "current map"**
        * Current map
        * Grid coordinates
* **Need better mapping guidelines**
    * Mappers don't know what departments need
    * Items, general layout, etc
* **The tools suck ass**
* **Better system for labelling mapping issues on GitHub: per-map projects**
* **Don't remove maps yet?**

## Map Editor - EmoGarbage

* convince PJB that this is on fire so we can bribe her into working on it
    * **Not Actionable**
* what are the features that we actually need this to do because we don't actually seem to have a git issue on it
    * **Made a project for it, fill it in after the meeting**
    * https://github.com/orgs/space-wizards/projects/13/views/1
* some kind of coordinated effort to expedite this maybe perhaps one in a million
    * **WYCI**

## Regular Maintainer Meetings and Schedule - EmoGarbage
* what if we stopped putting off meetings every single time they came around
* commit to doing doc reviews, merge sprees, and playtests
* make sure we actually have bimonthly meetings instead of just brushing them off
* maybe get someone to host if smug is dead in the water 
* **Just make the doc review a regular occurence, always something to talk about**
    * **Do design doc review for half an hour or something idk**
* **Consider moving maintainer meetings earlier?**
    * **Poll or ask later, but maybe 2hrs earlier might be nice**

## Design Docs

### [Automated Evac & Crew Transfers [Moony]](https://github.com/space-wizards/docs/pull/38)
- **verdict: closed**
- Stated goal is to avoid "we just evacuate the moment the round is mildly inconvenienced", but instead of solving this it turns "evacuate" into "new game+ that doesn't kick people back to lobby"
    - Would rather see this problem solved by making it easier for the station to stand its ground.
- Impractical to balance with SS13's design
    - People would be able to take items and progression between the stations, think double armory equipment.
- Document is light on details
    - What triggers a crew transfer?
    - Why is the doc title "automated evac"? What's automated about it?
    - What about antags?
- Using a shuttle as a transfer would definitely result in high shuttle bomb chance just from this


### [The Invisible War: Virology & Disease Rework [Goodwheatley, Unapproved]](https://github.com/space-wizards/docs/pull/46)

The first issue is that **virologist shouldn't be a job**. I'm not sure if the doc is trying to imply this, but just to be clear here. For starters there is not enough content here to justify a virologist job, in SS13 virologists have the ability to mutate COOL SPICY VIRUSES for good and evil. We have none of that here, so they'd be twiddling their thumbs 90% of the time. (And just so we're clear, virologist gameplay in SS13 is terrible so we don't really want that either.)

It feels like there's a bit of a hole in the core gameplay of the gamemode. It mentions a complex system of "strains" and the janitor's role in reducing germ transmission, but I kinda get the feeling that's not gonna pan out in practice. How long do we expect a virus outbreak to be something the crew has to deal with? This may just be a numbers balancing game, but my core thoughts revolve around the following topic: how does re-infection work, and what about getting infected when already sick?

The document mentions features like "making a cure from a non-strain is less effective", but less effective *how*? Takes longer for the cure to work? Takes more reagent? Longer to produce in the first place? Will people cured by an imperfect disease match get less immunity system so they'll be easier to re-infect with a different strain?

A topic I'd like to see more elaboration on is re-infection of strains. I suppose a gameplay element would be that people can get re-infected via different strains, and if medbay and janitor are doing so badly you'd just have a long-drawn out cycle of some people get cured -> others re-infect with mutated strains -> those people get cured.

On the topic of antibiotic resistance: it is unclear to me how antibiotic resistance would propagate in practice. I'm imagining that while the antibiotics are taking effect, their virus becomes "stronger" against antibiotics. If it then has the chance to spread before being fully killed, that strain is then more difficult to kill. This however poses the question: does this matter if the entire station is already infected? If most people are already infected then this antibiotic resistance would not spread on its own much. I get the feeling that the factors at play in real populations do not work on the scale of SS13 without some "cheating" to make it so that antibiotic resistance can propagate even without direct virus spread. Perhaps just re-infection as I mentioned before might be sufficient here to make medbay hurt if their decision to cure stuff is "just put antibiotics over the counter carelessly".

On the topic of "getting infected when already sick", can you just camp with a shitty cough-only strand of the disease to be immune to a more lethal variant, or would a virus KEEP mutating so that wouldn't be practical?

The part about outbreak has this to say about strains:

> If this mutation is beneficial and spreads to new hosts, it now becomes a new strain of the initial virus.

This raises me the question of what "beneficial" means. Do we just mean "more fit at aggressively spreading to other people" that makes sense, but again I'm skeptical how much a virus' mutations can really make that big of a difference on the population scales of an SS14 round. Again, might need some fidgeting or a way for one strain to overtake another. 

We also raised the topic that there should be more interesting ways for players to play against diseases, such as cough medicine to suppress symptons while a real cure is being made.

Also we're not sure what role this proposal should play in a round with regards to lethality. A big problem in SS13 is that you kinda only have one way to deal with viruses and make cures, and it's one or two machines inside virology that people may not know how to operate OR be too incompetent to. This sucks because lethal viruses kinda have little counter play from individual players once they're infected, so we think maybe starting off with "viruses can't really be deadly, at most debilitating" might be a good idea.

On the topic of cure creation, cure creation seems very simplistically described and not in-depth enough. There are multiple methods (from immune person vs just from somebody who is sick). What are the tradeoffs between these approaches? How long (roughly) can I expect this to take? One minute? five minutes? Is there something virology can do to speed up the process? Just thoughts here.

On the topic of germ infection: since you mentioned ONI probably need to take the mechanic from ONI where you don't "just" get infected when you contact germs, in ONI your duplicants need to fill up a disease bar (IIRC) before they get infected. I feel like this would be a good idea too especially for airborne stuff, to make it so that medical staff don't just get unlucky with dice rolls.

Having written all of the above, I feel like the gameplay of "find the initial infected" might be a bit awkward. If I'm reading this right, getting the initial infected makes "the best cure" but that feels anticlimatic that it's then just over? No more gameplay, strains not relevant? Or am I misinterpreting this. Then again maybe that's fair and balanced with how annoying that might be to do.

Minor nitpicks:
* Separate vaccine gun is probably overkill. I'd just make it a syringe gun that can take any syringe (and is therefore a high-value item).
* The holobarrier projector thing should probably require the virus to be scanned first. Otherwise the optimal thing to do would be to go around keeping these things put up around the entire station all shift, which seems like terrible gameplay. Maybe make strain distance a modifier to stealth factor here. 
* Should probably rename "virus" to "disease". Y'know especially since antibiotics only work on bacteria, not on viruses.
* The disease detector patch thing is weird. Why can't a blood sample just be enough?

Maybe I forgot to note something down, first time I'm writing notes for a design doc from a maintainer meeting alright?

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
