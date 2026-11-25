# Resource-Oriented AI

| Designers | Implemented | GitHub Links |
|---|---|---|
| ScarKy0, Aeshus, Saphire | :warning: Partially? | TBD |

## Overview

> [!NOTE]
> This proposal is based in part on [Moony's AI proposal]().
> Based on doc by [Aeshus](https://github.com/Aeshus/docs/blob/ebcf19a686b3b6a7240fbc9e916b530bfeeccacd/src/en/space-station-14/round-flow/proposals/station-ai.md)

The AI is the same "big brother" that can quickly observe any place on the station (that has cameras), which can communicate with crew and interact with technology.

It is a digital entity stored within the AI core, meaning that it can be easily moved using things like [Intellicards](), killed by breaking the core (with difficulty due to the [AI Turrets]()) and only really interacts with crew through [technology]() and the [radio/holopads]().

In order to balance their frankly obscene amounts of power, this PR introduces the notion of ["Processing Power"]() in order to sustain or extend its capabilities. The idea is that by capping the amount of Processing Power an AI player has, we force them to make choices on their playstyle. Lasting actions, like bolting or electrifying doors, etc. would require a an upkeep of Processing Power in order to maintain their state, while temperory actions would place temperory "debt" of processing power (opening and closing doors, sending announcements, etc). If the usage would exceed the available Processing Power, AI would lose the ability to use more "actions" until more resources become available.

The AI gains Processing Power in three primary ways: The AI core, 2: expanding server infrastructure, 3: degreading crew-oriented technology. 
- [AI Core]() means the AI has a constant but low output of processing power as long as the core is connected to a power grid. This is not a big amount and should simply be enough for the AI to survive if this was the only means of generating processing power.
- [Server infrastructure]() means Processing Servers, which would be mapped alongside the AI in the AI Core. They are the main means the AI has to have processing power roundstart and should not grant more than the basic capabilities until expanded. Regular servers(Telecomms, Camera, etc) will also grant a small bonus of resource to the AI.
- [Degrading crew-oriented technology]() means that it can disable things like consoles, APCs and servers(Telecomms, Camera, etc). This is the main way AI would be able to gain more processing power by itself. A piece of machinery used by the AI to gain processing power would have degraded or fully disabled capabilities. If machinery that already grants a small processing power bonus was to be disabled by the AI the amount will increase.

For the antagonist ["Malf" AI](), this PR mainly curbs their ability to quickly bolt & electrify the whole station without recourse, while still giving them a path to quickly do similar but more targetted attacks. All of their paths to gaining resources are not explicitly suspicious in any way, and the crew can quickly subvert their expansion by cutting off the antagonist AI's processing power sources, requiring them to reduce their attacks. Please note this doc does not aim to explain the roundflow of Malf AI outside of small connections.

## Background

AI is a staple role for any Space Station implementation. Many different implementations use it for different niches, but this proposal is meant to outline a version that is much closer to an actual role than a glorified observer.

The current implementation in SS14 suffers from two major sins: the AI can do *too* much, and the AI isn't really connected to the crew.

For the abundance of stuff it can do, just look at two common complaints: 
- Antagonist AI ("Malf" or Antimov) is too quickly able to disable the whole space station with no recourse or way of fighting back except changing their laws at the console. They have nothing stopping them from bolting, electrifying, and then cutting power to the whole station. 
- The crew-oriented Validhunting AI is too quickly able to antag hunt around the station, bolting off escape routes and electrifying doors. While I do personally like this playstyle a bit, this PR mainly requires them to focus on things instead of just wandering constantly.

For the lack of crew connection, just look at how:
- There's no real departmental connection to AI. There is basically no reason for the average crew member to ever go to the AI core or ever interact except for command. This pr introduces reasons for crew to see the AI, such as upgrading it.

## Intended Outcome

This implementation is meant to make AI into a more interesting and versetile role to play. Currently the AI is considered "all powerful" but can also be very boring.

If the AI is granted more options, but is limited by the amount it can take at any time, it leads to an interesting gameplay where you might need different things active at different points in time. You can no longer answer to the call from a security officer to help chase down the clown as you might lack the processing power to bolt a door in their face, or you might not even have access to the radio as you try to redirect power to the containment field emitters so the singularity doesn't loose.

## Processing Power

The AI is designed around the central conflict of managing it's processing power.

Is used for essentially every interaction the AI does, and as such, the AI must make sure to use their resources for the right reasons to ensure that it has enough to continue to function.

The AI would start with a default amount of processing at the start of the shift that it can use for basic functionality (such as connecting to camera routers, to telecomms servers). This default is provided by the starting server infrastructure and by the AI core's default gain.

Processing power is not a resource that regenerates, rather a maximum capacity. If the AI had 100 max processing power and using cameras would cost 30, the AI would have 70 resource left for other actions. In the case the AI would go above this capacity the action will be denied, and if the capacity will be lowered (by let's say, a syndicate breaking the servers) below the current usage, the AI will be forced to lower the usage before resuming action.

### Sources

#### Server Infrastructure

Most of the AI's starting compute comes from the their server infrastructure, which can be expanded by the crew and cyborgs. They will require power to function properly.

This should give at least enough power for the AI to listen on all radio frequencies and all camera routers.

For a non-antagonist AI, the benifits are:
- It gives them a simple source of processing power.
- Incentivizes crew into actually setting up, maintaining, and securing their critical infrastructure.

For an antagonistic AI, the benifits are:
- It makes crew question the need for this critical infrastructure. If the crew really needs to stop the AI, they can cut telcomms and cameras off. 
- It gives another location that the AI desperately needs to defend from crew incursions.
- It heavily incentivizes the AI to not just cut telecomms power, as they are hurting themselves more than the crew by doing that.

For mappers, AI servers should be mapped along the AI in the core, the telecomms rooms should stay where they are, though camera routers should be placed within their respective departments as to make that an easier and less centralized way for crew to dispose of AI's resources.

#### Degredation of Crew-Oriented Technology

The final source (and greatest potential) is the degredation of crew-oriented technology. This could be things like consoles, machines, etc.

When the AI is degrading it, the crew is unable to use it.

The purpose of this is to provide a viable way for the AI to quickly gain a burst of resource while also making it come at the cost of annoying crew and raising suspicion.

For the non-antagonist AI:
- It provides them additional compte for consoles that the crew just aren't using, such as the power console in the bridge.
- During Nukie shifts, the AI can justifiably use it to force its resource up and defend themselves and the crew.

For the antagonistic AI:
- It lets them quickly gain resource and cause disruption to the station. 
- The crew can simply cut the AI control wire to renable functionality.

### Sinks

There are going to be two types of sinks here: constant and temperory. For things like Cameras and Radio, it makes sense to have them be constant sinks as they are constantly being used by the AI. For things like opening doors or using a console, however, that is a time based cost.

This mainly means the AI cannot suddenly bolt every single door on the station with no drawbacks. If you imagine bolting a door costs 5 processing power for 10 seconds and the AI has 20 resource available, it cannot bolt more than 4 doors within those 10 seconds.

## AI "Modules"

AI Modules do not function in the same way as cyborg modules do. Instead they are toggleable features inside of a special AI menu.

The main point here is to allow the AI how to distribute it's resources. Does the AI want to be unable to use the radio but be able to listen to motion alarms? Toggle off "Radio" and enable "Motion Alarm". Though toggling modules should invoke a cooldown as to make it some commitment instead of micromanaging a menu based on the situation.

#### Radio

The most basic and essential ability for the AI, should use low amounts of processing power. It simply means the AI is able to speak and listen to channels other than binary.

Radio gives some needed justifications:
- A "silent" AI may just not be using their resource for radio.
- A basically essential sink that will always lower the AI's total processing power.
- Incentivizes the malf to stop eavesdropping on crew as they need to spend more resources to defend themselves.

In order to access specific radio frequencies (except binary), the AI will need to use processing power.

An antagonistic AI could use a module to impersonate the voice of a crew member (like a voice mask) in order to confuse radio communications.

#### Cameras

Cameras are probably the most important thing to an AI player, and as such, will be one of their main draws for their resources.

It will need to spend a continous amount of power to connect to specific camera consoles in order to view the cameras attached to it.

There will also be a "general" camera router that will connect to any camera placed on the station that isn't associated with another camera router already.

This forces the AI to choose which camera networks it would like to view, incentivizing them to do things like disabling it's own cameras inside of its core to save resources.

For a non-antagonist AI:
- Incentivizes them to either watch everything and not have much they can do or view little and do a lot.
- Still incentivizes crew to set up cameras and for crew to use the camera router.

For an antagonist AI:
- Incentivizes them to minimize what they're viewing in order to save resources for messing with crew.

#### Doors

Doors are currently the main way that an AI would interact with a station.

Opening doors would be a temperory resource cost as it just opens the door. It's meant to be cheap as it's the most basic thing a non-antagonist AI would be doing.

Bolting doors would be constant resource as it's activly blocking out a crew member. This is done as to stop an antagonist AI from just bolting the whole station and a metagaming AI from just bolting all the doors to its core.

Electrifying doors would be a higher constant resource as it's activly harming crew. Laws should already restrict most use of it, and as it's a higher cost, it stops the antagonist AI from just electrifying every door like they would currently.

For non-antagonist AI:
- They don't have infinite ability to bolt doors to stop antagonists.

For antagonist AI:
- They now have to selectivly bolt/electrify doors.

#### Consoles

AI will have several modules related to intrinsic access to their consoles. While not really a high resource cost, this will make it require more thought than just to jump from announcement to crew monitor to station records.

The most basic consoles that could be included in this are:
1. Crew Monitor
2. Communications console
3. Criminal Console
4. Research Console
5. Mass Scanner

#### AI Alerts

Probably one of the most important modules. AI Alerts would notify the AI of events happening across the station and can be reviewed in their little "Alerts" menu.

This is meant to allow the AI to view more places at once than just whatever they are floating over with their eye, while not being openly available to the point where they will know everything.

For example, the AI might decide that, during a nukeops round, they will enable the module that saves alerts of AIV wires being cut, notifying them of the location and time of the event, as well as allowing them to jump to said location to try to investigate the surrounding areas.

This adds another layer of allowing the AI to respond to things on the station, which while quite powerful is obviously not free and would require some thought put into it.

While this list can be expanded, the most basic types of logs could include:
1. AIA and AIV wires being cut.
2. Tripping motion sensors.
3. States of air alarms.
4. High-value door interactions. For example doors to bridge being opened and closed as well as who did it. This would require the AI to first mark the door it wishes to observe.
5. Usages of consoles, such as research consoles, announcements and cargo purchases.
6. General station events.

#### Power Redirection

An important ability of the AI as well as the main way it can assist the crew. While this module is enabled the AI gets access to a "Power Redirection" action. It would be unfair if the AI only took from the crew and wasn't able to grant anything back. Ideally it could be a common occurance where during a catastrophe (or if engineering fails to do their job) the AI could redirect the power towards critical areas of the station (Medbay, the containment field, bridge) to allow it to function.

At the cost of a hefty amount of processing power, the AI is able to power a machine, APC or similiar, assuming it is connected to the same power network. This is obviously not the most efficient way to power something, but is enough to help in a stressful situation. (Let's say, to power the bridge during a singuloose so the evac shuttle can be called).

For a regular AI this can serve as a good way to assist the crew in cases of power outages (assuming the AI has enough resource from other powered machines), while a Malf AI might allow a subverted cyborg to recharge during a tough moment so it can continue it's operations.

#### Overclocking

Another ability the AI can use to assist crew. This module allows the AI to "overclock" machines at a constant use of processing power, allowing them to operate beyond their normal capabilities.

For lathes this may mean things like faster printing, while for computers lowered or removed cooldown on their usage. Ideally overclocked machines will become a thing the crew frequently asks the AI for so it is more than simply a door opener for them, granting a sense of mutual help.

As stated above, a regular AI can use this ability to assist the crew. This then encourages the crew to built more Processing Servers for the AI so both sides can benefit.
While a Malf AI might use this to trick the crew into building more servers for itself, or even overlock a cyborg to grant it some additional buffs.

#### More Modules, More Fun

Obviously these aren't the only modules the AI would have access to. In reality there could be more and then some exclusive to Malf AI itself. This is more so meant to grant the idea of how they function and affect the AI.

## Intellicards and Additional AIs

#### Intellicards

By default, stations should have only one AI. But in cases their AI is destroyed, or threatened to be at risk, it can be downloaded onto an intellicard and stored before being placed in a new core.

The AI can be downloaded by interacting with the core using an intellicard, which starts a doAfter as well as notifies the AI it is being downloaded. Intellicards can be researched by the science department, but by default the Research Direction spawns with one in their locker, allowing to card a misbehaving AI and Wipe it, as you would do with a positronic brain. A Malf AI could be able to deny being slotted instead.

As stated above, the intellicard has to serve some basic functions:
1. Store AIs. While the intellicard is not literally meant to be an AI storage, the AI can be kept on it in case of emergencies, core transfers or similiar. The AI in this state should function identially to a pAI.
2. Wipe AIs. It is obvious the AI will not always behave, whether due to a malfunction or ion stormed laws. The AI cannot be directly wiped from the core itself (unless it is destroyed) and as such the intellicard is to serve as a less destructive way of doing so.
3. Create AIs. It is not as easy to get a new AI as wipe the old one and click a button on the intellicard. An active positronic brain can be inserted into an empty intellicard to create a new AI inside of it. This process cannot be reverted, meaning once a new AI is inside of the card it must be wiped or put inside of a core. This option is meant to make crew think twice before replacing an AI they simply dislike as it introduces a cost to creating more.

#### Additional AIs

In an ideal scenario there will be only one AI on the station. Having several will severely limit their active resource gain as only one AI can disable machines to increase their processing power at a time. This eliminates scenarios where many more AIs can be created for the sake of it, now needing consideration whether a second AI is needed.

This solution limits the ability to have several AIs who can keep an eye on EVERYTHING on the station, if the AI can be a problem while it assists security, imagine what happens when there is several.
Additionally, this can introduce a gameplay element where a secondary AI is created with the goal of stealing processing power from the first.

Now when it comes to creating AI Cores. The construction itself is locked behind research, together with the intellicard. A core frame is first built using the build menu and with resources it leads to an empty AI core, into which a positronic brain (or a filled intellicard) can be inserted.

## Laws

AI, same as other silicons, is bound by a lawset. This is meant to stop the AI from being too destructive upon the station and it's assets. The laws of the AI can be modified by using the AI Upload Console.

Uploading laws ot the AI is a simple form of inserting a lawboard into the console, confirming the lawset, selecting the AI and uploading it. This process will wipe the lawboard and make it into essentially scrap as to introduce some sort of cost to constantly swapping laws (if the AI somehow allowed you to, anyways).

Lawboards can be printed at science and are a prerequisite to being able to unlock the AI Core. They can simply be printed inside of the circuit imprinter for a slightly increased cost.

#### Ion Laws

As any other silicon, the AI can be the subject of Ion Storm, modifying it's laws with random effects. This builds some tension between the AI and crew as an ion stormed AI can become a small problem to deal with, while being under the defense of turrets. The crew is not meant to fully trust the AI as that can lead to many situations where it is simply be abused by security, however what would really break this trust is the [Malf AI](), which is a topic for a seperate doc.