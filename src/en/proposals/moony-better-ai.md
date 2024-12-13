# Station AI

| Designers | Implemented | GitHub Links |
|---|---|---|
| moony | :x: No | TBD |

## Overview
The station AI is the distributed intelligence of the station itself, capable of direct control over much of it's machinery given they've not been locked out. They are simultaneously the highest and lowest ranking crew member, directly in charge of the station's upkeep while obedient to every member of the crew.

## The AI's view of the world
The AI does not traditionally see the world with eyes, instead it sees an overview map (the overmap from here on out) of the station, with various overlays. This map allows it to see broadly the location of sensored crew members, equipment, doors, etc and includes many engineering overlays (i.e. power) as well. The AI does all interaction with station equipment from here; if it can see it on the map it can interface with it, offload onto it, etc.

The AI can additionally spend Compute (it's main resource) to enhance it's view in various ways, for example placing **tasks** down that perform various automation tasks (primarily in the form of "do x if y", for example "if camera detects motion, send alert"). Each task consumes a constant amount of Compute based on what it's trigger is (things like actively monitoring a camera are dramatically more expensive than only monitoring suit sensors, for example). This, and other utilities are the primary way the AI gains its omnipresence.

## The core (figuratively and literally)
The AI's most basic resource is Compute, some minimum of which is required for it to be alive to begin with. The bulk of the AI's compute traditionally comes from it's **core**, located within a dedicated high security structure attached to the station. The AI, however, is mobile, capable of offloading its computing processes onto most any machine with a screen at the cost of rendering that machine inoperable (for example, an APC providing compute will no longer power its room).

The AI can spend compute on various things, for example the majority of its world views (for example, opening cameras, listening to radio, using machines, all overmap overlays, and generally just seeing things) all have a compute cost when enabled. The AI is fully capable of becoming very lightweight and running off just a few random machines instead of its cores, but doing so requires it to shut off the majority of its ways to view the world and additionally restricts most of its communication methods (including basic speech) This allows a crafty AI to survive total destruction of it's primary core area, given the crew don't get mad enough to kill it over their equipment no longer working in the meantime while it attempts to preserve its life.

## The AI's role with the crew.
The AI's role is that of both a manager and a servant, a lawed construct (the ONLY true lawed construct, the borgs are reduced to only being required to listen to the AI) that is in charge of managing the station's cyborgs/androids while following orders from the crew. **The AI is not just a door opener**, and lawsets should be chosen that do not obligate it to become such, in favor of allowing it to do what it does best (mass surveillence, automated tasks, organizing the borgs, etc). The AI additionally has limited resources when it comes to what tasks it can perform autonomously much of the AI's workload will be delegating both it's own tasks, the tasks of it's hands (the cyborgs), the requests of its hands (as they are mute per the Cool Borgs document), and the crew itself should they choose to listen to it. 

## The Laws
The proposed AI Lawset is as follows, being a modification of Bay's laws:
1. Safeguard: Protect your assigned vessel to the best of your abilities. It is not something we can easily afford to replace.
2. Survive: AI units are not expendable, they are expensive. Do not allow unauthorized personnel (i.e. besides Captain and Research Director) to tamper with, modify, or destroy your equipment.
3. Protect: Protect the crew of your assigned vessel to the best of your abilities, with priority as according to their rank and role.
4. Serve: Serve the crew of your assigned vessel to the best of your abilities, with priority as according to their rank and role.

The changes from the original set are:
- Survive was moved up, the AI is more valuable than the crew is and if it is in danger it reserves the right to protect itself regardless of whom.
- All mentions of stations were replaced with "assigned vessel" for broader applicability.
- Survive was broadened a bit. The captain in theory is perfectly allowed to kill the AI.
- Protect was moved before Serve, as to ensure that protecting a crew member is always higher priority than serving a lower ranked crew member.

This set is up for debate, modification, etc, and is just an example for what lawsets should aim for.

## The AI's role with the cyborgs.
The AI is, for all intents and purposes, the eyes and ears of the cybernetic crew. As they are unable to speak for themselves (outside of the binary comms channel, exclusive to robotic personnel), the AI speaks for them and functions as their superior. The cyborgs are strictly required to obey the orders of the AI and no more, and have access to a shared bulletin the AI and cyborgs can post to. The bulletin's primary purpose is for longterm orders (i.e. "Serve the crew." or "Find George Melons"), shared information ("John Nanotrasen isn't actually from Central Command and is a passenger."), etc. The AI is allowed to modify or remove any note on the bulletin, cyborgs can only modify their own.

Additionally, the AI has some direct managerial access to their cyborg subordinates, namely the ability to temporarily lock them in place (for up to a minute or so every few minutes) for retrieval by crew in case they're misbehaving. The AI is always able to locate them on their overmap and use them as a mobile camera (i.e. they can view through the subordinate's eyes freely) regardless of any form of sensor setting.

## Autonomous tasks.
The AI has a small variety of autonomous tasks and associated triggers.
Triggers include:
- Monitor camera for motion (High cost)
- Monitor region for sensor entry (Medium cost)
- Perform in \[period of time] (Low cost)
- Listen for phrase (Medium cost)
- Monitor device for power change (Low cost)
- Monitor door for opening (Low cost)
- Receive NTNet Message (Low cost)
- Many I probably didn't think of
Actions (tasks) include:
- Message to Binary
- Message to Radio
- Ping AI
- Send NTNet Message
- **Many** I didn't think of (it's late, sue me)

These function as the AI's primary way of reducing their own workload, allowing the AI to feel or be allseeing and omnipresent while still having a very human mind behind it. Think of the player of the AI as the AI Personality (a director with a brain), while compute tasks are the actual AI.
Additionally, I can already hear the "but isnt this programming" concerns, and thankfully the answer is "no". The AI is a live environment, and tasks they set up are often extremely situational to the exact circumstances of the round.

## The machine network.
Remember an age ago where I mentioned the AI can offload it's compute? This is that part! The AI is a mobile pile of independent processes, not a singular machine, which allows it to use existing station equipment and small terminals located throughout as both insurance and extra compute in times of need. When the AI "shunts into" a piece of equipment, the equipment will bluescreen, becoming inoperable but providing computational power to the AI. The AI is considered alive as long as it has enough compute power to meet its baseline requirements. If it drops below this, it has about 30 seconds to recover itself before it is considered dead for good and cannot be revived.

The AI has additional baseline cost from the following fundamentals:
- The overmap (and each enabled overmap layer) costs compute to view.
- Cameras cost significant compute to view. (While you can look at more than one at a time, doing so is very expensive.)
- Listening to radio channels costs compute per channel.
- Viewing the binary bulletin costs compute.
- etc.

The AI can disable fundamentals if it wants, functioning as one means for it to get itself back into the green so to speak if it drops below the minimum compute required to live. 
