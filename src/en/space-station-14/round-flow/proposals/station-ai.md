# Resource-Oriented AI Proposal (Draft/Notes)

| Designers | Implemented | GitHub Links |
| --- | --- | --- |
| Saphire Lattice | :warning: Partially | TBD |

## Background

AI is one of the staple roles in practically any SS13 codebase. It’s ever-present both in and out of the game.
(TODO: why do we *even want it*? What’s the selling point? What does it add?)

The current implementation in SS14 suffers heavily from just plain not having anything to do. It’s an eye in the sky, without body, hands, and even its own “department” is not integrated with it as borgs have *no requirement* to obey or even listen to AI. All its abilities are served to it from the word go and require nothing extra to keep and use, beyond existing.

A rather common (todo: or is it just loud?) complaint is that AI validhunts a lot. That is probably a symptom of there not being much else for it to care about. Especially when the hunted antag have an incentive to mess with AI’s laws because it’s too good at finding them. There’s also not much antag counterplay to AI beyond “cut it off” and “compromise its laws”. The cameras are also treated by the crew as almost an afterthought unless AI’s actively malicious, and are then destroyed fully or wires are cut. They have no natural causes to be broken and it takes a lot to do so, giving away antagonists rather easily if they try.

Meanwhile in SS13, the AI as a concept also integrates rather heavily with an antagonist role “Malf”, a flip side to having an AI on the station. Or rather it does *not* integrate. The antag is not designed well in SS13, and is metagamed to hell. There’s no way to metashield it because you would need to meta shield pretty much *every single thing* that “Malf AI” can do. It’s also susceptible to just being rushed by power-gamers the moment it’s detected for sure. It’s a stationary target in a game where any attempt at solo “tower defense” is bypassed with 2 C4 charges, barring admin intervention.

This proposal is based in part on [Moony's AI proposal](https://github.com/space-wizards/docs/pull/160).

## General overview

The AI is a big eye in the sky capable of quickly observing any point on the station, and acting on it. It’s shackled by the silicon laws, yet can be subverted or be a round start antagonist. It’s a fully digital entity - a standard AI can not affect the physical world outside of a few specialized devices for such.

The AI is *not* a security officer with an observer role, and should not act as such. Its purpose is keeping the station intact, keeping the crew from dying *in general*, managing computer infrastructure of the station, and being the command role for the borgs. It should be treated under standards of a command role, as it has comparable power to the Captain.

Being a digital entity the AI requires processing resources to sustain its base capabilities and any extra it might want. This resource management would be centered around machines that provide them - either specialized ones that do so at maximum efficiency; or using crew oriented devices, temporarily locking the crew out in the process.

The antagonist, “Malf” AI, must not be immediately distinguishable from a normal AI. It has access to abilities that affect the physical world way more, and that push the resource management element even further. Is AI asking for more servers because it wants to help the crew even more, or is it because it plans to detonate the nuke?

Multiple AIs are not in the design scope of this document. They should however be possible, and all of the systems should NOT treat AI as a singleton. Machine takeover system could be reused, for example to implement minor “virus” ghost role antag/NPC.

## Proposal

Design principles:

- Decentralization and resource management
- Subversion integration
- “Malf” AI - antag integration

Design problems to consider:

- Control by the authorized personnel
- Too much dependence on power
- Difficulty to kill

**TODO SECTIONS:**
- Intellicard interactions, ways of controlling
- Holopads
- ??? please help

## Processing - Resource management

As described above, AI is a fully digital entity. It needs processing resources to continue to exist, especially in its full form. Without these it will be crippled or straight up start dying.

The computing resource system consists of two resources: Compute, and Bandwidth.

**Compute** is the constant upkeep resource, something that the AI requires by itself to exist, and is used for abilities that stay active indefinitely, until toggled off. It is a pool that gets its capability expanded by having more machines under AI’s control, and gets consumed by abilities until they are turned off.

**Bandwidth** is the momentary resource. It’s used for having something happen right now, near-instantly, and something that does not last for long. It’s a pool with a maximum size extensible by controlled machines, and every momentary ability consumes some of the resource from it. It regenerates at a base rate, further enhanced by the amount of unallocated **Compute**.

*Alternative*: Shared pool that gets extended/shrunk based on controlled devices, and chunks of it are allocated persistently while unallocated part can be used for temporary abilities. Something to playtest later!

And a “secret”, third resource: **Player’s Attention**. As an example: door bolting as implemented in SS14 initially uses a radial menu popping up on alt click, rather than instantly letting AI bolt doors, thus requiring the AI player to pay by being precise and quick with controls as a person behind the screen. This applies to any kind of “minigames” or other interaction heavy sequences. Think of science's APE.

### Usage

Nothing is a free action.

Primary use of the computing resources is ***keeping the AI alive***. It lives or dies through the lack of the processing power. The secondary use is actually letting it do things on the station. Having no processing power should hurt, but not an instant death.

The definition of “alive” here is fuzzy. The AI exists to serve (or kill, for antag) the crew. For that it needs to be able to act, observe, and exist.

- Being unable to act is the softest “kill”. And “speaking” is not a free action, though pretty close to it. It still can observe and maybe scrape resources together to shout out a warning. But it is effectively useless without someone else helping it.
- Being unable to observe anything is a much bigger issue. This drops AI down to a schematic view with maybe some critical infrastructure being visible to it in a vague way. It can still claw its way back, but it will not be easy. And again, this renders it effectively useless without help.
- Being unable to exist is self-explanatory.

The resource system should encourage an AI to either request extra processing machines for itself, or to start using the station infrastructure to power its abilities. Or as a last resort, start to micromanage and drop active abilities. As such the prices of things should be balanced accordingly. An AI that wants to do more than just listen, talk and speak shouldn't be able to just stay only with round start resources.

A possible way to accomplish that is to make vision and speech capabilities rather huge in resource demand, while the core AI footprint is relatively small and could fit on about 4-8 consoles or APCs, or 1-2 borgs, without losing integrity.

#### Processes (Abilities)

Let’s start with the persistent things, stuff that uses a “constant upkeep” resource. This list is mostly an example and general outline, the exact specifics should be nailed down after implementing and playtesting stuff.

- Staying alive - Not technically an ability, but uses the same system. May or may not be straight up be present in UI to shut that down, ala IC way to do “/ghost”. Automatically shut down when there’s just not enough processing power.
  - Malf AI should require significantly less resources for this. It’s by no means impossible to kill through cutting things down, but it shouldn’t beg for every scrap. Perhaps every base ability would be discounted as well? Have to be careful here not to make it metagameable, but a skill thing, to keep crew from figuring out the AI needs less resources for stuff this round than usual.
- Radio system (listening) - Binary is free! But the rest AI has to buy, requiring a tiny bit of resources for each channel. Comes as part of the spawn-in preset for standard AA radio.
- Radio system (speaking) - Binary is, again, free! This is distinct from listening as to not cripple the AI player entirely if they have to discard radio, but still force to sacrifice something to gain resources. Part of spawn-in preset with AA.
- Vision system - Without it, there’s just the “Nav UI”-like map replacing camera view. Can still see computing systems, doors, etc that have an AI wire. Maybe see Air Alarms? Spawn preset bundled. (MAYBE). See the [Vision](#vision---cameras-and-map) section for more details.
- Vision system composition - Map UI can be an extremely powerful tool in gameplay perspective. As such it should be an extra ability to composite it over where the cameras are missing. Balancing note - shouldn’t be bypassable by player toggling camera vision rapidly on/off.
- Comms console - Separate and cheaper than others as it’s rather important and relatively low impact (except round stalling, oops?). Though would it be better to keep it MORE expensive?
- Assorted consoles - Just a general category but they each should not be free.
- Bolting a door - it’s an override in case of an emergency, not a go-to that can be spammed with impunity. Bolting off giant hallways would require managing resources, and making sure to unbolt things elsewhere. Keeping things bolted is possible, but not unless you the player wants to do nothing else.
- Research - a resource sink that takes a lot of processing capability of the AI in both of the available resources at a base, and can be increased further (powers of two? exponential?) to provide more research. Should not be a way to completely ignore science department gameplay, but rather be a side option, requiring substantial resource investment to provide good enough amount of points.
- Cargo bounty - Call it “Bluespace Calculation” or any other fancy name. Basically the same as research but also gives out something that can fulfil a cargo bounty. Giving it to cargo could be done through integration with the [paperwork management UI](#assorted-ideas)? Should be separate from research resource sink to not let AI just double-dip.

#### Routines (Momentary actions)

Things that don’t require sustained cost, but should not be completely free. Practically anything that interacts with things beyond a digital interface.

- Opening a door! Minimal amount required.
- Speech when the radio process is inactive. A somewhat substantial amount when surviving off a single or two AI servers, but not extremely hard hitting. Binary channel is always free however.
- Left-click or alt-click on vents to unlock them, for cheap
- **TODO**. Ideas: sensor sweep? Mass applying (un)bolting to everything an APC’s connected to? Atmospherics reset action that can be used from the action bar/alt-click radial menu and applied to an atmos alarm to reset it to default? Clicking vents to unlock them?
- Consoles! They aren’t free and cut a decent chunk, to encourage the AI player to choose a Compute option, but in a pinch this should work too. It also gets paid by the player having to manually locate a console and being unable to check on things elsewhere but the vicinity of the console.

### Sources

- AI specialized machinery, contributing a significant amount of processing capability to the AI.
  - The downside to this is that it requires someone physical to build it, and needs a decent amount of resources
  - Such machinery should be difficult to destroy or even move. It stays where it stays, unless the situation requires it and someone puts enough effort to move it; or break it.
  - Generates heat up to a throttle cutoff, and works better when cooled. When not in an optimal environment, provides less computing power, but still comparable to servers.
  - Backup power? Camera built in?
- Crew devices; computers, machines, servers
  - These don’t contribute as much **Compute** as they are not specialized for AI use. Servers do provide more **Compute** than just consoles, and provide **Bandwidth** in amounts comparable or identical to dedicated machines..
  - Locks out the device for crew use, rendering it inoperable. This acts as a conflict point with the crew. Computers don’t work, machines either. Servers don’t provide normal functionality or do so in a very limited way.
    - E.g. crew monitoring server could give invalid/partial data with a warning, or just not work at all. Same for telecom servers.
  - Non-antag AI can be flushed out from the device via a near-instant crew exposed action. This includes a subverted AI. Could be an UI that shows “This device is in use by AI \<name\>. \<Override (button)\>.”
  - Such shooing away should keep the AI from taking the device over for at least some time, at least a minute. It should not be able to just annoy the crew to death even when compromised - it’s still shackled.
  - Antagonist AI, “Malf”, should have an option or be able to spend some resources to completely lock the crew out. Will require more detailed balancing later.
  - For “Malf”, the timeout should be reduced or bypassable. Again, might need some balance tweaking whether it’s just a pop up “you sure?” or a resource sink.
- Borgs! Useful and somewhat plentiful, perfect for an emergency ~~snack~~ method of survival when the station’s powered off and the AI SMES is about to drain, with a downside of rendering the borg unable to synthesize voice (speak) when AI’s along for the ride, except for beeps and emotes. Does not require borg sync, but requires approval from the borg even if synced. Malf AI can bypass the approval.

The AI satellite has several of the AI machines built into it, providing the base necessary resources for the AI, and some extra to make it actually useful to the crew.

**Note:** Something noted by other people is how this system would interact with multiple AI. Two AI might be possible with either significant crowding and cut down resources, or a very annoyed crew as two AI fight one another for scraps. They should be able to lock one another out from a device, and require significant investment of power to pull control away. Of course, the crew can always just shoo them away with same near-instant action.

## Vision - Cameras and Map

The AI is not a biological entity, and it’s only barely a “physical” one. It doesn’t need to care about specifics of how things look, but rather whether or not an area is intact, safe, and secure. As such, the vision system is an optional ability that an AI player can shut down, whether to free space up for something else, or as an emergency measure.

### Map Vision

The “map” view replaces the entirety of the AI player's vision if the camera ability is shut down, or if there’s no cameras *and* they activate a composite vision ability. It should provide information about the station’s hull - walls, floors (or a glaring lack of one or being stripped down to a lattice), windows. It also should display machines that have an AI control wire - deemphasizing them if the wire’s been snipped, and potentially not showing them at all if there’s no camera that can see the machine (to make camera snipping actually work around APCs, air alarms). Fire alarms and atmosphere alarm status should potentially be shown over the area too - perhaps as an ability.

While using the AI map vision, the crew can be seen via suit sensors, only if they have tracking on. Otherwise AI is unable to tell if someone is in the area without using cameras. A potential ability idea is to give cameras a motion detection cone that gets rendered for AI, and highlight entities within it - differently from tracked crew that enters it.

The map vision should not use “#00FF00 on #000000” color scheme for purpose of reducing eye fatigue. Consider dark dark gray background as a default for areas that are not space exposed. Preferably implement a way to set custom colors for your UI.

### Cameras

Cameras cover almost all of the crew areas, places where most people work and exist within, to monitor their wellbeing and the state of the station. They should not be nearly free to build, and should require an autolathe producible board, some steel, LV wire.

They should not be more durable than a person - a hard enough knock should deactivate it for a small period of time, while sustaining enough damage will keep it offline until repaired. A non-violent option for keeping cameras offline should be available, using cloth and/or gauze makes it impossible to see through a camera, taking a relatively long time to cover it completely (3 or 5 second doafter, balanced by it being a “stealth” option). A camera disabled in such a way should still be shown as active for AI and warden. Though it should have no motion detection cone and convey such explicitly.

Power is required for cameras to work at full capacity, reducing their vision to half or third of their normal range when it is not available. Though power being out is a bigger issue for AI itself than just the cameras.

## Borgs - Sync and control

The AI has no way to affect anything physical (at least, a shackled one - not malf). Its primary way to do anything in that regard is borgs, and directing the crew. While the crew has own concerns, like air, health and such, borgs are hardier and are almost always available for AI to use.

Borgs can opt into synchronizing their laws with AI, gaining map or camera view from AI (todo: detail the incentives). This does not make them less susceptible to ion storm law corruption, but the AI can fix the laws by rewriting them to its own at some cost.

Emagging should forcefully but silently unlink a borg from the AI if it’s synced. If it’s not, AI is not relevant.

Crew can cut AI control wire (multiple required?) in borg frames to prevent them from being able to sync to the AI, and letting the crew modify their laws once again (or just resetting to what they had before AI overriding them - including previously present ion laws, if there’s no way to set laws of a borg).

## Assorted ideas

- Paperwork management UI that AI gets *instead* of being able to interact with fax machines. It would list all papers received and let the player read them. It would also allow editing (if not stamped). Allows sending the same way a fax can.
- AI stamp that it can put on any received paper through paperwork management UI. If it fits into the art design, make it a QR or DataMatrix code that just says “AI”. Otherwise just have it be a text.
- Holopads are a way to communicate with the crew for free, with full vision and such. The downside is that it completely takes over the AI’s viewpoint for the duration of a personal call. Just formalizing the existing implementation by Chromiumboy here.
