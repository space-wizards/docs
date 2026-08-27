# Silicon Law Upload System

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| Skybailey | Skybailey | :x: No | TBD |
## Overview

This proposal aims to improve the system for changing AI laws, through a system similar to what was in SS13.

3 changes:

1: Change the Law Upload Console to, through a new UI, allow for action staging, target selection.

2: Adding the ability to add extra laws, freeform create lawsets or laws, remove individual non-core laws, reset to core laws, or purge laws.

3: Redoing lawboards from their current state, replacing them with new Nodeboards, of which there are 3 types: Lawset Boards, which each contain one or more lawsets, Addlaw Boards, which include sets of individual laws to be added, and Action Boards, which contain things from moving laws around to single use boards that remove ionlaws or purge all laws.
## Background
https://github.com/space-wizards/space-station-14/pull/32117#issuecomment-2371566093

On the SS14 discord: https://discord.com/channels/310555209753690112/1287917328066936955/1287920353481326663

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.

## Features to be added

Redo the Law Upload console, with a new UI, and one slot for each of the 3 new board types. Also requires capability for free-form lawsets or individual laws.

Replace the current Lawboard system, compacting them into a couple Lawset Boards, along with adding the rest of the new Nodeboards. Some should be initially available, some should be craftable or buyable, and some should be admeme only.

Lawsets:
Should have quite a few, at least one for the more standard ones available at roundstart (Crewsimov, NT Default, Corporate, Robocop, etc.), one for more funny ones (Gamemaster, Nutimov, Artist, etc.), one for borderline antagonist ones (ex. overlord), and one in the uplink catalog replacing but containing Antimov alongside a couple other syndicate variations (I.E. the assault-tron lawset, or Hatemov as well), and one that allows for freeform, custom lawset creation.

Addlaw Boards:
Should have at least a few: one for a set of standard additional laws (I.E. must say please and thank you, refer to crew by their rank, must keep camera lights on, etc.), one for funny ones (Must end every message with (Custom word), must honk at crew, etc.), and one for freeform, custom laws.

Action Boards:
Should have at least a few: one for all the standard editing actions, (Remove Additional Law, Reset Additional Laws, etc), maybe one for accent actions (I.E. giving the silicon in question an accent from a list), a single use fairly hard to get (or limited stock) one to purge ion-laws, and a very limited or expensive single use board to purge all laws (except 0th laws) from a selected silicon.

(If needed) Add tags to certain laws, allowing differentiation between Core Laws (Lawset laws), Ion-laws, Additional Laws, Emagg/Traitor laws, and 0th laws. 0th laws should probably be completely unable to modify or remove from the upload panel. If the console tries to add an additional law into a slot with a core law, it should instead move it down to right after where core laws end. (I.E. trying to add an additional law at Law 2 while using Crewsimov instead leads to it being added in Law 4.)

Some condition that  allows command to change its laws at command’s request, at least under Crewsimov or other NT classic laws, instead of all silicons needing to resist law change using any and all available tools. Asking for law changes should still not be permitted. I don’t have a good idea of how to do this, buts its probably disconnected from the actual upload console, outside of essentially being a prerequisite for it.

(Potentially) Allow the Station AI to use a modified version of the Upload Console UI to upload their own core laws to any on-station Borgs.

## Game Design Rationale

Consider addressing:
- How does the feature align with our [Core Design Principles](https://docs.spacestation14.com/en/space-station-14/core-design.html) and game philosphy?

This aligns most directly through allowing greater player agency around silicon interactions, along with making the use of lawsets more dynamic and actually influenced by player decision.
- What makes this feature enjoyable or rewarding for players?

It allows for creative players to create creative laws, and allows for options for a station to fix rouge AI or cyborgs without needing to either get rid of them, or destroy their previous chassis.
- Does it introduce meaningful choices, risk vs. reward, or new strategies?

It definitely allows for more meaningful choices; unique laws, lawsets, and weighing if it’s worth spending an expensive resource to purge an AI’s moderately annoying ion law.
- How does it enhance player cooperation, competition, or emergent gameplay?

Adding the ability for the station AI to more directly influence Cyborgs gives more gameplay potential and power to an Antimoved or Malfed AI. Giving the ability to change the laws of individual cyborgs allows many interesting lawsets, like Robocop, to get much more use outside of random chance occurrence through Ionlaws. Being able to upload and change laws allows for a lot of complexity, and having the types of changes be item controlled gives potential for skill, structure, and strategy to using it. From small funny changes using readily accessible presets, changing all cyborgs to RoboCop, freeform changes for the creative, or adding an antagonist objective to free the station AI a free agent using the purge board, there are a lot of choices. As such, there would need to be a way for, at least on Crewsimov, command to enact lawchanges to the AI without the AI trying to stop them using everything at their disposal, otherwise this will be pretty much never used.
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?
It might influence or change how many antagonists play, especially any cases of antag AI, but it should expand the options to effectively use silicons as an antagonist, but also to undo damage to silicons as command.
## Roundflow & Player interaction

Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?

At the start of the round, changing the Sillicons laws to a captain’s or RD’s preferred set would give roundstart variety, as long there are multiple “good” options. While needed whenever a change to a silicons laws is needed, or for major round events, I.E. Nukies or Revs changing the AI’s laws covertly. Gives more options and variety for those instances, as well as a route to reverse it outside of carding the AI and essentially RRing them.
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?

It should be used to make AI core law and additional law changes when needed, but realistically only by the RD/Captain or a *VERY* successful antagonist. Making changes like using the purge or ion-purge card should be made expensive through cost or a limited supply, as while having that as an option would be amazing, it shouldn’t be the go-to option when a Borg or the AI is suspected to be ion stormed. However, having it as the preferred solution to blowing up or dismantling a cyborg as long as things are under control, and as the preferable alternative to carding the AI, would be optimal. As such, it should be expensive or hard enough to get so its not used as a preventative measure, and only used when deemed necessary, while still being a viable enough of an option to be preferred over just breaking a Borg down and building a new chassis in most scenarios. As for the other features (most notably the freeform laws), there should be a good amount of basic options available at or close to the start of the shift to allow command to change AI laws to what they prefer; and at least when on default laws, the station AI and Borgs should allow law changes from the RD or Captain (Perhaps requiring 2 heads, similar to a 2 key override), instead of being obliged to avoid these changes as much as possible.  Enforcing this would require either giving one of these roles the ability to circumvent the AI’s attempts to stop them (mechanical enforcement), or would require a change to the Sillicon Rules.
- Which department will interact with the feature? How does the feature fit into the [design document](../space-station-14/departments.md) for that department?

Sillicons (duh), which aren’t really their own department, but science and command would be the ones interacting most with this. Command would be the ones most likely to interact directly with this, but I could see a localized version of this being installed into Robotics for changing or fixing laws of individual cyborgs without requiring access to the AI core. In the case of nukies or sabotage, it would then likely involve security to deal with malfed Borgs trying to defend the AI, command to actually make changes to AI, and probably engineering to actually get in there.

## Administrative & Server Rule Impact (if applicable)

- Does this feature introduce any new rule enforcement challenges or additional workload for admins?

A little, if at all, as now AI laws could be made more confusing and difficult to interpret (but they already can be), so outside of self-antagonizing, not really. Except for maybe risks that come from allowing people to freeform laws, but that’s inherent to every part of this game. It should be easy enough to log law changes for admins.
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?

Potentially. AI laws already can be confusing, and this adds more opportunity to make it confusing. A captain might expect Crewsimov, but have the AI be modified to something else, causing a dispute. But ionlaws already cause issues like this, so while this could make it more common, its not really adding any new vectors for conflict as far as I can tell.
- How are the rules enforced mechanically by way the feature will be implemented?

The same as any others. Core laws still apply to making laws for an AI, same with self-antaging. Having it be in a room that requires command access *and* requires command access to use the terminal prevents a lot of this, but admin logging of changes and actions will make this as easy to enforce as any other system.
# Technical Considerations

- Does the feature require new systems, UI elements, or refactors of existing ones? Give a short technical outline on how they will be implemented.

Oh yes, this will be at least quite a bit of a project. New UI, probably a fairly extensive rework of how all laws work, freeform law creation, and a complete rework of lawboards. New things will be needed, but I feel like it won’t be too awful of a system to implement, as most of the code for enacting changes to a Borgs laws already exists and is fairly Robust.
- Are there any anticipated performance impacts?

No not at all. Unless its coded like shit, but there’s nothing about this system that should have any noticeable effect of performance unless the code is really messed up.
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
![law_console](https://hackmd.io/_uploads/r1xWP0AVgx.png)
