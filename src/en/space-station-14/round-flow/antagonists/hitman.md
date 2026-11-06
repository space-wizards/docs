# Hitman
<!-- Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar. -->

| Designers | Implemented | GitHub Links |
|---|---|---|
| Storymatt | no | N/A|

<!--
`Designers` should be the names that you use on GitHub and/or Discord. This is optional but strongly recommended, since:

- This acknowledges credit where it is due
- People who are confused about the written intent can use this information to contact the authors

`Implemented` is the status of the feature.

Github links can include multiple PRs, if relevant.
-->

## Overview

a new subgamemode antag, and possible small midround antag. based around hyperfocusing on a single kill.

<!-- A very short, maybe three sentence summary of what this proposal is about. A high level "overview" or "what this adds". -->

## Background

A long while back, funky station questioned why there wasn't an antagonist based around kill objectives, only ones based around more general killing. so i endeavored to make one. this evolved into a antagonist based around a single kill objective, taking the planning such an objective set would need to its extreme.
this was made and merged into deltaV. I now hope to add this to wizden as i think it would be nice for it.
<!--
Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game.

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.
-->

## Features to be added
### primary additions
A new antagonist based around a single kill objective at a time named the Hitman
A midround variant that comes in a shuttle

### objectives
alongside the regular objectives of killing a crew member and get to centcomm, there would be a set of two new "modifier objectives".
modifer objectives are free objectives mechanically and provide limitations or required actions to the kill.
the current list of objectives is as such
- Make their death look like a accident
- Kill them in a public space
- Kill them dramatically
- Draw-out the kill
- Inform them about the assassination long before it happens
- Kill them cleanly (kill them without any blood spilling)
- Kill them in a funny way
- Kill them indirectly
- Kill them nicely
- Kill someone close to them and make sure they know
- Gain their trust

of course, all that matters is that they make the kill harder or add an extra step, not the exact objectives.

### the contract system
a system which would allow the hitman to get a new set of target and modifier objectives after completing the first one. for rp it could also give some spaceos in "good faith payment". this is to ensure a lucky or skilled hitman has something to do. it would be an ability of hitmen to do this for ease of coding.

### hitman card implant
An implant hitman would start with that would make a business card upon using. this would purely be for flavor and making the "inform them about the assassination long before it happens" objective easier to do.

### kits
hitman would have a case which works like an undisclosed thieving satchel. its kits would be as such
| Name   | Concept | possible Content |
|----------|:-------------|:-----------|
| Sharpshooter kit | sniper assassin fantasy | hristov bundle |
| Loud kit | something for if you want to go loud, cowboy fantasies? | armor vest, python, no slips |
| Assassin kit | quiet killer stuff, one silenced gun at least | cobra, throwing knife kit, radio jammer |
| Poisoner kit | poisoning fantasy | syringe, bottle of nocturine, pax, toxin, mute toxin, and a synthesis kit |
| Infiltration kit | stuff to get into places and sabtoage | emag, syndicate jaws of life |
| Disguise kit | disguising as anyone, its hitman you have to | agent id, chameleon clothing, bonic voice mask implanter, fake Mindshield implant |
| Escapist kit | escaping sec? I don't remember | dna scrambler, freedom implant, scram scrambler |
| Tracker kit | info gathering, tracking hard to find targets | all comms encryption key, universal pinpointer(menupinpointer if accepted), camera bug |
<!-- Give a description of what game mechanics you would like to add or change. This should be a general overview, with enough details on critical design points that someone can directly implement the feature from this design document. Exact numbers for game balance however are not necessary, as these can be adjusted later either during development or after it has been implemented, but mention *what* will have to be balanced and what needs to be considered when doing so. -->

## Game Design Rationale
to go over each design princple
### choas
the design of hitmans modifer objectives being freefrom and as sets of two is to try and ensure no perfect gameplan comes to light. the point of them is to encourage freeform planning through giving a limitation with several awnsers. this should lead to choatic situations since it should encourage the player to get up to some outright nonsense to complete their objectives
### seriously silly
the hitman by its nature will always be more on the serious side. but the round about ways the hitman must take to complete the objective or the outright loony contraptions for objectives like indirect or accidental should prove to be rather silly
### dynamic enviroument 
none of hitmans objectives require something you cant find on the station. they are freeform in part to stop requiring any one idea to complete. objectives like indirect or accident encourage using the environment for the kill.
### Intuitive and Inter-Connected Simulation
the contract system makes easy sense kill to get a new contract, the implant explains what it does easily, and the objectives are outright for the player to interpret. it should all be intuitive.
### Player Interaction
Several of the objectives are about interacting with the target in some way(gain their trust, inform them about the kill, kill someone close). Beyond this most of the objectives require a good amount of planning and thusly interacting with the area to case it for the plan or get needed materials.
### Player agency
the hitman themselves is limited in ways to kill them but almost all do not have a state in which they are outright impossible unless the hitman has already messed up.
for the target. two objectives(inform and kill someone close) give them warning of whats coming and thusly time to prepare. gain their trust gives time to interact with the hitman and the nature of high planning is that it gives them time to act and for someone to discover what is going to happen.

### just a spark
hitman needs to kill someone, they require interacting with people to become a problem
### escalation/ back and forth/Discoverability
as noted before, several objectives require something to be done before the kill, failing that they must prepare a good bit with their objectives. thusly there are events leading up to the main kill they perform. This gives escalation, dicovoribility, and back and forth.
### accessibility
the hitmans objectives clearly explain what it needs to do. they are a clear minor antag so the rules on what theyre allowed to do are also clear. the tracker kit is in place for hitman players who may have trouble finding their target.
### full time job
the hitman kills crew, i rather think most crew would not want someone doing this
### fun to lose as
this rather circles back to escalation, back and forth, and Discoverability. the main thing to note is the riduculous kill should be more enjoyable then the regular kill objective. for the hitman it should likely also end up pretty fun due to still getting to have the planning part alongside the funnyness in how such a plan would go haywire. besides that the desperate attempts to try and complete a kill after being found out should prove enjoyable for both.

<!--
Consider addressing:
- How does the feature align with our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosphy?
- What makes this feature enjoyable or rewarding for players?
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- How does it enhance player cooperation, competition, or emergent gameplay?
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?
-->

## Roundflow & Player interaction
the hitman despite being a roundstart antag, causes their main impact later on in the round. it should add more spice to the latter half of the round.

hitman players should generally go with every objective. this is not mechanically enforced as no objective can force the player to try and complete them. if they do not engage with the modifiers, specifically the kill happens far earlier on, in which case it becomes similar to a syndicate agent. well i dislike this outcome it is not a awful outcome and is okay.


<!--
Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
- Which department will interact with the feature? How does the feature fit into the [design document](../space-station-14/departments.md) for that department?
-->

## Administrative & Server Rule Impact (if applicable)
for griefing, it introuduces a new subgame which has a gun. but the limited ammo and fire rates of the weapons should stop main issues
for admins there is the chance targets will complain about hitman players not following objectives. but this will likely be after round mald and requires the hitman to actually be ignoring their objectives, thus these should be relatively rare and relatively easy to handle.


<!--
- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
- How are the rules enforced mechanically by way the feature will be implemented?
-->

# Technical Considerations
the new implant requires a new system, as does the contract system.
the card would have ui which is just a syndicate one turned to grey with a white crosshair instead of the red and snake symbol.
The contract menu would look like a basic ui with a button to get a new contract in the bottom right corner, and a list of drop down menus for each target and their modifers. a button to confirm its been completed at the bottom of each set and how much they completed for the playes who like such.

<!--
- Are there any anticipated performance impacts?
- Does the feature require new systems, UI elements, or refactors of existing ones?
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
-->
