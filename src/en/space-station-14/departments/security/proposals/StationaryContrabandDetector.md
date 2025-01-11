# Stationary Contraband Detector

| Designers | Implemented | GitHub Links |
|---|---|---|
| [Mixelz] Killerqu00 | ❌ No | TBD |

## Overview
The Stationary Contraband Detector is a one tile machine that will scan the inventory of any containers or people that pass over it. 
If the detector detects any contraband, it will alert those in its vicinity via a loud sound and lights like that of any alarm.
It will also alert security on their communication channel that the detector was triggered and who set it off, but *not* what item set it off; this effect is proposed to be achieved by having the machine automatically update the Records system whenever it is triggered.

It should additionally have a low percentage chance of having an incorrect result, proposed with a false positive result, so that it cannot be a guarenteed method of confirming contraband without a manual search by a physical Security Officer.

## Background

In the current state of the game, an end of round evac bombing is all but guaranteed and it its almost entirely impossible to stop unless you happen to have all potential agents already detained or very strong suspicion that a specific person will attempt to carry out the bombing.

There are also very few methods of security being able to accurately confirm that someone has contraband; they must either visibly see them carry the item in their hands or must have prior reasonable suspicion that the target has it due to a prior encounter that would only be possible through contraband.

A contraband detector, something that is a staple of real world security operations, would be a method to help alleviate these problems, add another layer of protection that traitors will need to bypass and would be a mechanical method of being able to detect if there is contraband in play while allowing sec to search a volume of people larger than themselves without grinding an area to a halt.

Additionally, it can be used as a method to more reliably indicate the presence of a Storage Implant (I.E. Someone consistently setting one off despite having an empty inventory.), which has been a point of contention as Meta Knowledge due to the limited avenues of knowing when one is in play.

## Attached PRs
These are PRs that will synergize with this one in such ways where the result will have a much higher quality with these PRs in mind, this PR should probably wait until these PRS are live before this one does:

### Locking Uplink when Evac arrives [#34359](https://github.com/space-wizards/space-station-14/pull/34359)
This would be a very appreciated PR to ensure its intent of evac protection is upheld, without this it would be trivial to bypass it for Evac bombing purposes.

## Design Intentions

The intents of this implementation on when, where and why it should be used are as follows:
1. As a starting point, it should trigger on any contraband that is not department specific. It should react the same to a Baseball Bat as it should a fully stocked C4 bundle. An item in a dragged container cannot be attributed to a specific owner/holder and thus would always set it off without an owner being attached to it.
2. It should be limited ONLY to high priority areas, there should not be a scanner on every hallway or maints shaft and its research restriction & difficulty to setup should be set accordingly. For this reason it should probably only be located on EVAC shuttles themselves baseline so that they cannot be stolen and moved round start.
3. It should not, by itself, be a reason to jail or detain someone. It should ONLY be used to raise a flag for a security officer to engage upon with roleplay, either via following up with a manual search or interrogating the suspect directly.
4. It should be able to be worked around IF it is planned for ahead of time. It should not be easily "cheeseable" through methods such as Q-Dropping the item past the detector, throwing the item past it or using a simple implant to ignore it. These would devalue more involved methods of a traitor getting past it and the point of the machine itself.

## Addressing Mentioned Concerns
> This would be a hard nerf to Storage Implants.

I think it would make storage implants easier to detect, but it is an opportunity for more adaptive gameplay to emerge instead of using the implant as risk free storage.
A very simple example could be holding major contraband in the implant while carrying minor contraband in a backpack to act as the scape goat.
A competent Security could then ask for a quick recheck, sending the traitor into a panic for how to resolve this situation with their contraband still in hand.
Effectively, we could roleplay as TSA agents and that itself sounds like it would lead to more fun situations than what we currently have available.
> This would remove evac bombs from being possible.

It would not since bypassing the detector is planned as part of its core intent.
It WOULD make it much more difficult to achieve for the DaGD objective type, but it is already a trivial objective to accomplish and would be a massive improvement to the Quality of the Evac portion of a round.
> Shitsec could abuse this and violate space law with a dubiously "legal" method.

It would be no different if those same officers decided to randomly search people without the machine and would still be breaking Space Law regardless. 
It would fall under being a new reason of probable cause and would be a massive boon for the players that are able to behave themselves.
Its planned implementation is already quite restrictive, and while the potential of abuse is there the same can be said for many other mechanics of the game and I do not think this falls outside those already established boundaries.
>  This would potentially nerf traitors too much and/or buff security too much.

Considering its intended restrictions, I do not see many scenarios beyond Evac Bombing that this would be a major change for.
It would be specifically alerting the behavior in regards to casually carrying contraband, which I feel is something that has not yet been dealt with in any direct capacity.
It would also encourage more RP scenarios as mentioned above, which may not inherently be a buff/nerf to either faction depending on how the "Meta" evolves from it.

## Follow Up PRs
Some potential follow up PRs to this device have been discussed, which will be noted below:

### EMAG Interaction
This will not be part of the initial implementation unless a maintainer would approve of it due to the EMAG restriction/freeze.
An example of a possible effect for consideration could be having the device always return a false positive result when Emagged, or giving completely random or arbitrary results instead.

### Refactored Implant Checking [#32136](https://github.com/space-wizards/space-station-14/pull/32136)
Considering one of the main pillars of this is to help with the Storage Implant problem, this PR will go very easily in hand with it.

### Create a handheld variant for individuals to hold in their hands.
This would allow it to be more flexible in its use, though it should probably come with even harsher restrictions such as being unlocked with late tier research or being part of the armory.
