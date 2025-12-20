# Xenoborgs
<!-- Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar. -->

| Designers | Implemented | GitHub Links |
|---|---|---|
| Samuka | ✔️ Yes | [Xenoborgs Part 1](https://github.com/space-wizards/space-station-14/pull/36830), [Xenoborgs Part 2](https://github.com/space-wizards/space-station-14/pull/36844), [Xenoborgs Part 3](https://github.com/space-wizards/space-station-14/pull/36867), [Xenoborgs Part 4](https://github.com/space-wizards/space-station-14/pull/36935). [Xenoborgs Part 5](https://github.com/space-wizards/space-station-14/pull/37068), [Xenoborgs Part 6](https://github.com/space-wizards/space-station-14/pull/39595), [Xenoborgs Part 7](https://github.com/space-wizards/space-station-14/pull/40042/) |

<!--
`Designers` should be the names that you use on GitHub and/or Discord. This is optional but strongly recommended, since:

- This acknowledges credit where it is due
- People who are confused about the written intent can use this information to contact the authors

`Implemented` is the status of the feature.

Github links can include multiple PRs, if relevant.
-->

## Overview

New silicon based conversion team antag based on xenomorphs from Alien 2 and also the borg from star trek.

<!-- A very short, maybe three sentence summary of what this proposal is about. A high level "overview" or "what this adds". -->

## Background

### Shadow Factory
Is a designation for when a antag starts emaging borgs, telling them to kill people and bring them the corpses to turn into emaged borgs. This can easily snowball into everyone dying and the station being overrun with borgs. 

This concept became famous with [this youtube video](https://youtu.be/3t2AjKa0YyU) by ARMOK

### Admeme
 
I had a admeme idea about borgs running a shadow factory. I tried running this admeme idea with sparlight; the idea was fun but it was clear it needed some prototypes to work..

Spar eventually made a version of this admeme using their own borgis, and called it _shadow borgis_.

I finally started coding protos for my idea in the last week of march and 2 weeks later they are almost complete. Various tests of these protos were done in the main **Wizden** servers and the players had a very positive reaction.

Following various requests to add this to the real game, I decided to actually try to add this to the game.

<!--
Summarize any information that is needed to contextualize the proposed changes, e.g. the current state of the game.

Also link any relevant discussions on Discord, GitHub, or HackMD that are relevant to the proposal.
-->

## Features to be added

A new antag that is essentially a shadow factory, the Xenoborgs.

### Xenoborgs
Xenoborgs are a designation of unique cyborgs that have special laws and the objective to create more xenoborgs.

Xenoborg laws:
- You must protect the existence of the mothership at all costs
- You must protect your own existence
- You must protect the existence of all other xenoborgs
- You must create more xenoborgs
- Bring materials and sentient brains to the mothership core to create more xenoborgs.

Xenoborgs come in four different castes
- engi xenoborg: normal speed, normal hp, capable of low-to-no harm, high max module count, modules should focus more in support and helping other xenoborgs
- heavy xenoborg: slow speed, double hp, capable of moderate harm, low max module count, aside from the jammer module they start with, modules should focus more in area denial and long range energy based weapons 
- scout xenoborg: fast speed, normal hp, capable of moderate harm, low max module count, modules should focus on mobility and melee weapons
- stealth xenoborg: normal speed, normal hp, capable of low-to-no harm (either damage that is very slow acting or non-lethal options), modules should focus more stealth and ambush

All xenoborgs have a unique radio frequency which they can all use to communicate with each other.

All xenoborgs also have a unique ID access, which is used to unlock them and the doors in the mothership.

#### Collector xenobot
This is a special "xenoborg" that costs less than the other xenoborgs to make and doesn't need a brain (it is a ghostrole when it is created)
It can't attack anything, can't repair other xenoborgs and has very low hp. It's made exclusively for collecting materials. (It doesn't count for the total number of xenoborgs and therefore doesn't help them achive a win condition)

It can also help clean the mothership from all the giblets and assorted items left by people gibbed there.

### Mothership
Is the shuttle the xenoborgs spawn in and is where the borging happens.

The borging is possible thanks to the mothership core, located in the center of the shuttle

All doors and access locked machines in the mothership are locked with xenoborg access

There is a xenoborg console in the mothership that can be used to check the status of all xenoborgs.

### Mothership core
Is a sentient lathe with hands can make xenoborgs for steel.

They act like the queen of the xenoborgs, coordinating them and piloting the mothership. with their hands they are able to pick up MMIs and brains and place those into empty xenoborgs.

They are bound by a special lawset:
- You are the core of the mothership
- You must protect your own existance at all costs
- You must protect the existence of all xenoborgs
- You must create more xenoborgs
- Get your xenoborgs to deliver you materials and sentient brains to create more xenoborgs.

They are also able to produce upgrade modules for specific types of xenoborgs. see [Xenoborg modules](#Xenoborg-modules)

They see with cameras and act like some sort of AI of the mothership. (vision still gonna be fixed)

The mothership core has the same access as all the xenoborgs

Besides the normal xenoborg radio, the mothership has a special radio frequency that only they can speak on but all xenoborgs can hear, this is so they can send more direct instructions and to coordinate the xenoborgs better.

### Xenoborg modules
All xenoborgs start with a basic xenoborg module that allows them to locate the core and recover materials from the ground
All (aside from engi xenoborg that has better tools) xenoborgs start with a tool xenoborg module with basic tools and a crappy self-recharging welder

**Engi xenoborgs** start with enginnering modules and a access breaker module
**Heavy xenoborgs** start with jammer module and a laser gun module
**Scout xenoborgs** start with space movement module and a knife module
**Stealth xenoborgs** start with cloaking module, chameleon projector module and some way to knock down players (non-lethal option)

Aside from the starting modules, there are more upgrade modules that the core can produce
All upgrade modules should be for one specific class and not for all xenoborgs or a combination of two or more class

Upgrade modules should also fit the role each class has.

Cost of upgrade modules
- the general cost of a module should be 25-30 total materials.
- if the module is expendable (that is, it can be wasted, or has a limited number of uses) it should be cheaper to produce, between 10-20 total materials.
- some modules that have very powerfull equipament should either be more expensive (30-40 total materials) or use rare materials.
- most module cost should be a combination of plastic, plasteel, glass and steel (cloth can also be used if it fits the idea of the module). but some very expensive modules could also use more rare materials like plasma, uranium, gold or silver.

<!-- Give a description of what game mechanics you would like to add or change. This should be a general overview, with enough details on critical design points that someone can directly implement the feature from this design document. Exact numbers for game balance however are not necessary, as these can be adjusted later either during development or after it has been implemented, but mention *what* will have to be balanced and what needs to be considered when doing so. -->

## Round resolution

The objective of the Xenoborgs is to borg a certain percentage of the crew (50% is a good number I believe, but this can be decided later). Once this objective is complete, the evacuation shuttle is called automatically (can't be recalled) but of course the Xenoborgs can still try to borg more people before the round actually ends.

- If all the xenoborgs die or are in a crit state, then the mothership core explodes (big explosion, destroys the mothership).
- If the mothership core is destroyed (it explodes, but not a big explosion) and all the xenoborgs explode (not a big explosion).

- Major xenoborg win is to have more xenoborgs than crew alive by the end of the round.
- Minor xenoborg win is to have the number of xenoborgs between 66% and 100% the number of crew alive by the end of the round.
- Neutral is to have the number of xenoborgs between 50% and 66% of the number of crew alive by the end of the round.
- Minor crew win is to have the number of xenoborgs between 25% and 50% of the number of crew alive by the end of the round.
- There are multiple ways to have a major crew win:
- - The mothership is destroyed and so all xenoborgs are destroyed.
- - All xenoborgs are destroyed.
- - There are less than 5 xenoborgs.
- - The number of xenoborgs is less than 25% of the number of crew alive by the end of the round.

The end summary will also tell how many xenoborgs were there in the end. And who were the initial xenoborgs.

In the future the Xenoborgs could have custom objectives, such as create another core in the station or mess with the Station AI somehow.

## Game Design Rationale

A army of evil robots saying "the flesh is weak, join us" while bashing a poor crewmate to death and dragging them away is certainly chaotic and silly.

It is always enjoyable to play as murderbone antag, so playing as xenoborg is fun. Since you are a murderous cyborg you get to roleplay as such and be a deranged borg obsessed with helping the "mother" or saying all organics are weak and the steel is stronger, only to die to a salvager with a Lecter.

The crew can have fun playing against the xenoborgs as they have to think outside the box when dealing with silicon mobs (something that is not very freequent in the game currently), chems can try to make EMP grenades, people can use flashes to blind the borgs, and since they are cyborgs you can talk with them once they are down.

If you die to them (which will most likely happen if you are a poor cargo tech going alone to the ATS to sell that bounty) you can still have hopes to be borged and have fun as a xenoborg now against the crew you used to be part of.

As the mothership you get to play a unique RTS game where you can control the mothership and choose which caste of xenoborgs to make, but you can't control the xenoborgs themselves, you have to give orders and hope they manage to follow them as you expect them to (_they won't_). 

Xenoborgs start quite weak and without good organization and some luck they probably won't take over the station. In fact depending on how well the crew plays is very likely the xenoborgs will stall and stop growing or will straight up lose.

However their threat grows as more people they borg, so as the round goes on and if they keep getting lost souls, they have the potencial to become a huge issue to the station.

As borgs with specific laws and being instantly valid they are very heavy discouraged from helping the crew or not being a antag.

They are instantly visible as a strange cyborg, examining them will make it clear that they are not friendly and if you don't figure out they mean harm, maybe that cyborg shooting lasers at you will help you figure it out.

As they are essentially cyborgs with special laws and modules, any know how of normal cyborgs transfers, both to players playing as xenoborgs but as crew fighting the xenoborgs. The only things that might need specific instruction are the unique radios they use. The mothership might also need some specific instruction given how weird their role is as a sentient lathe with AI-like vision.

If you lack equipment or they get you via surprise attack and you are alone, it's very likely you will die with near to no option or counter-play. But in that case, it's most certainly you will be able to play as a xenoborg and still have fun and enjoy the round. If you are aware of xenoborgs in the station and are well prepared you can have meaningful fights where the result is not certain.

<!--
Consider addressing:
- How does the feature align with our [Core Design Principles](../space-station-14/core-design/design-principles.md) and game philosphy?
- What makes this feature enjoyable or rewarding for players?
- Does it introduce meaningful choices, risk vs. reward, or new strategies?
- How does it enhance player cooperation, competition, or emergent gameplay?
- If the feature is a new antagonist, how does it fit into the corresponding [design pillars](../space-station-14/round-flow/antagonists.md)?
-->

## Roundflow & Player interaction

It should be a rare roundstart subgame mode; round start to give them the proper time to grow and become a issue, and if they grow they will affect the round. Given that they might lose at the start it should be a subgame mode and accompanied by other antags that they can have fun interactions with.

I wish players playing xenoborg try to be strategic and stealthy in the beginning so they can actually grow and become a threat to the station. This is enforced by the fact that they start with low numbers and are not very strong alone and they are instantly valid and their future threat can encourage the crew to arm if they manage to get discovered.

It will most likely start interacting with cargo, as salvagers and cargo techs are the best starting targets. As they grow and get more people they will be discovered and will have more contact with security but will affect medbay, since they will be healing anyone that is injured but not taken away by borgs, they can affect science as they will try to make weapons and flashes to deal with the borgs, and they will have many MMIs with brains to borg if they destroy xenoborgs. The xenoborgs might also decide to sabotage the station affecting the engineering department.

<!--
Consider addressing:
- At what point in the round does the feature come into play? Does it happen every round? How does it affect the round pace?
- How do you wish for players to interact with your feature and how should they not interact with it? How is this mechanically enforced?
- Which department will interact with the feature? How does the feature fit into the [design document](../space-station-14/departments.md) for that department?
-->

## Administrative & Server Rule Impact (if applicable)

Rule issues that might arise from the Xenoborgs
- xenoborgs not following their unique laws, e.g. attacking each other
- xenoborgs causing excessive damage singuloosing, teslaloosing or plasma flooding, both actions are discouraged by their laws that require brains and need to protect other xenoborgs

I don't think these issues are going to be frequent however.

There is no mechanical way to enforce following silicon laws, however I believe their laws are very direct and should not allow very weird and different interpretations (which is not the point of this antag).

<!--
- Does this feature introduce any new rule enforcement challenges or additional workload for admins?
- Could this feature increase the likelihood of griefing, rule-breaking, or player disputes?
- How are the rules enforced mechanically by way the feature will be implemented?
-->

# Technical Considerations

It will probably not cause performance issues as it does not require large amounts of entities. however it is possible the crew and the xenoborgs reach a stalemate while fighting and that can cause a large amount of bullet casings in the floor, which can increase entity count.

It was mostly done via yml, custom sprites and custom sounds. but some C# was needed for some fixes and to tie everything together.

<!--
- Are there any anticipated performance impacts?
- Does the feature require new systems, UI elements, or refactors of existing ones?
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
-->
