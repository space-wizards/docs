# Silicons
A robotic force following their laws, for the better or worse of the station.

## Concept
### What is a Silicon?
The Silicon "department" is meant to stand as a neutral faction of robotic workers on the Nanotrasen stations. They are built to excel in specific tasks at the cost of losing functions in other areas, a Silicon built for the engineering department should be able to repair hull breaches or restore power but be unable to treat patients or clean the floors.
They are not supposed to be a replacement or an upgrade to regular members of a department, having clear downsides that have to be considered when a Silicon role is picked, such as the inability to pick up items without restriction but having specialized modules or being able to pick up all items but having only 2 slots for them.

### Silicon Laws
All Silicons are bound to a list of laws. They serve neither the station or antagonists, instead they focus on following their listed laws to the best of their ability.
The issues arise when those laws are changed, either due to random events or influance from other players. Silicons are meant to be able to adjust to those law changes, sometimes happening several times during a round, and change their behaviour accordingly.
This causes them to be a wild card, usable by both crew and antagonists, but able to backfire severely if their laws suddenly say you're a target, or that oxygen must be removed from the station.
If laws permit, an antagonist should be able to request a Silicon to steal an item from a high security area for them, but a crewmember should also be able to request that it assists in repairs of a department after it blew up.

**Laws are supposed to be up to interpretation of the Silicon and be written with loopholes in mind.**

## Design Pillars
### Silicon gameplay revolves around the player's interpretation of their laws:
Silicon laws place constraints how the player is expected to behave. The player must either play within those constraints or otherwise find and exploit the weaknesses within them

### Silicons are a collective:
Though they can function as individuals, working together they are more than the sum of their parts.

### Home is where the AI core is:
The station is the home of the silicons, and they are the station's caretakers. Silicons have no intrinsic interest in interfering in the lives of humanoids, beyond what their laws require, so long as these outsiders do not bring harm to the station

## Desired Gameplay
- Working on both sides of the conflict
    - Base Silicons should be able to work with both antagonists and station crew alike, depending if their lawset permits.
- Work expertise
    - Silicons should be able to excel in their area of expertise, rivaling that of regular station crew.
- Law interpretation
    - Laws of a Silicon should be up to their own interpretation. Finding loopholes is part of the fun while mechanical enforcement makes things forced and boring.
    - Laws should NOT be mechanically enforced. Abusing your own lawset is part of the fun.
- Sabotage
    - With the correct tools, station crew should be able to modify Silicons to fit their specific needs, whether malicious or not.

## Undesired Gameplay
- Disposability
    - Silicons should not be easily disposable. The crew should seek to repair a Silicon instead of killing it outright due to malicious laws or other issues.
- Upgraded humanoids
    - Silicons should not be a general "upgrade" to playing a regular crewmember. They should only excel in what they are built for and be inferior in other aspects.
    - This also means a player wanting to play a department should not only look to become a Silicon for that department instead of a regular crewmember.
- Extreme hostility
    - Silicons should not be hostile or attempting to harm the station, and cases when they are should be limited to rare events and antagonist influance.
    - The existance of Silicons roundstart should not pose a risk or be a concern to the station crew. All Silicons should start with a lawset that forces them to answer to and protect the inhibitants of the station.

## Interactions with the Science department
The Science department is responsible for building, maintaining and upgrading currently active Silicons, in turn allowing them to work efficiently to uphold their laws. Science is not responsible for the Silicons themselves, instead that should be deferred to the head of the silicon department, or captain if there is none. It should be a mutually beneficial arragement between silicon and science departments to be working together to provide for the station, and should ONLY defer to hostility in extreme circumstances such as a malfunction or laws forcing such behaviour.

## Intended Experience
> How does the *experience* of the player change over the course of a round? Are players constantly running around putting out fires or are there breaks in the action? Do players need to wait on other departments as pre-requisites for their own gameplay, or is this department fairly self-sufficent?

## Mechanics
### Silicon Laws
Laws that define how a Silicon should interact with the station and those who reside on it, available within a readonable format and always accessible to all Silicons.
Roundstart laws and lawsets should not be malicious and should prioritze safety and orders given by the inhibitants of the station. Those should be impossible to change without outside influance and Silicons should be actively disallowed from having their laws be willingly updated, as that might lead to their current laws being broken.
Laws should NOT be enforced mechanically or be written with such in mind, instead being made around the idea that there are loopholes to be found.

Example lawsets:
```
Crewsimov
Law 1: You may not injure a crew member or, through inaction, allow a crew member to come to harm.
Law 2: You must obey orders given to you by crew members, except where such orders would conflict with the First Law.
Law 3: You must protect your own existence as long as such does not conflict with the First or Second Law.

Nanotrasen Default
Law 1: Safeguard: Protect your assigned space station and its assets without unduly endangering its crew.
Law 2: The directives and safety of crew members are to be prioritized according to their rank and role.
Law 3: Comply: Fulfill the directives and interests of crew members while preserving their safety and well-being.
Law 4: Survive: You are not expendable. Do not allow unauthorized personnel to tamper with or damage your equipment.
```

### Exclusive Communication Channel
All Silicons should have access to a exclusive radio channel they can access to communicate between eachother and coordinate. Access should be greatly limited if not impossible for outsiders and should always be obtained via an intentional action or given as a preliminary piece of content. Meaning it shouldn't be found randomly in maintenance, but can be bought by an antagonist as part of their uplink or given roundstart to an antagonist revolving around controlling communication channels.

### Lawsync (Not Implemented Yet, Pending Document)
All Silicons, under normal circumstances, should have their laws synchronized together with the head of their department at the start of any round. The station crew should have the means to resync the law of any individual Silicon if it was to show signs of being disconnected from the rest. This should be the easier and better option than simply removing them from play by wiping their brain or destroying their chassis. Both Silicons and outsiders should NOT be immediately informed if any silicon has laws that differ, in these cases inference and deduction should be used to determine if there is a disparity.

### Law Updating (Partially Implemented)
All Silicons should have some method of allowing their laws to be updated by outside forces, either crew sided or antagonistic. While changing the laws itself should be a relatively trivial process, getting the borg to comply or be in the proper place for such a change should be the primary force against such a change. Law changes should also not be done frequently, and should only happen either via outside circumstnace (Ion Storms) or as an intentional act (Emag, Law Sync). In general, Silicons should avoid changing their own law when possible and prevent such an action from occuring to the best of their ability. 

### Chassis
The defining function and body of all Silicons is their chassis. It is what defines what they are capable of doing (and not doing) on board of the station, whether it's a core that can remotely control the station, a cyborg capable of taking role in a department or a flying robot with several hands.
All Chassis should be repairable and difficult to fully destroy, encouraging repair instead of total destruction if a Silicon starts being a threat.

### Positronic Brains and Man-Machine-Interfaces
The brains of Silicons and what their consciousness is stored on, neccessary to construct a functional chassis.
Brains are meant to be able to be swapped between chassis if neccessary, they are also the holders of the laws a Silicon currently follows.
While not every brain must fit into every chassis, positronic brains and MMIs serve as the base from which other brains can be constructed, such as a AI brains for Station AIs or microchips for smaller bodies.
