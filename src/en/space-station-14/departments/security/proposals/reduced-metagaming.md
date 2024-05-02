# Reducing Metagaming

| Designers | Implemented | GitHub Links |
|---|---|---|
| SlamBamActionman | :x: No | TBD |

## Overview

This proposal contains a list of design changes and features aiming to reduce the impact of metaknowledge in the game. 

## Background

Right now there are several instances in the game where admins are expected to enforce rules related to metagaming. Some of these are related to the current round (e.g. using knowledge gained as a ghost after being revived), but there are also rules disallowing knowledge about the game in general. This mostly includes knowledge about antagonist items, behaviors and round events. This kind of "*metaknowledge*" rules are primarily restricted to Security and Command, and there are examples of metaknowledge that is allowed under the rules; knowing where maints loot spawns, secret Chemistry recipes and recognizing modifications to station layouts. 

There are two ways to reduce the impact of metaknowledge: allow it in the rules, or make it unviable to act upon it. Often this is done in combination; uplinks are an example of this. It's pretty much impossible to find out if a locked PDA is an uplink due to the high number of permutations in the lock. While it's technically possible for Security to confiscate every roundstart PDA and replace them with ones from the P-Tech vendor, it's simply not feasible in practice. This becomes more of an issue when a specific person has been suspected of being Syndicate (which is why we have stringent rules about PDA confiscating still) but it shows there are ways to design around metaknowledge.

The negative impact enforcement of metaknowledge is the following:
- Players need to self-assess what counts as abusing metaknowledge, possibly over-correcting as there's no ingame feedback.
- Disagreements about whether someone is abusing metaknowledge (e.g. a SecOff testing a pair of gloves for chameleon) can easily occur between players in a round, and is highly contextual.
- Admins need to put in time and resources enforcing these rules, which is always desirable to reduce.
- Players have to pretend they don't know about certain mechanics.

To find out where these problems lie, [I created a thread on the Discord](https://discord.com/channels/310555209753690112/1227226189358174209) to gather feedback from the playerbase where they have percieved metaknowledge abuse. This feedback is used as a basis for the changes and will be cited throughout the proposal.

The proposal will contain both mechanical design changes as well as rule changes. The rule changes are necessary as the goal of the PR is to reduce admin workload, and where it's not possible to eliminate them the goal will be to make them more clear and reduce grayzones. 

### Security & Resources

Other than explicit rules and Space Law, the main thing holding Security back is **time**, **materials**, **personnel** and **information**. Performing a search takes time, which holds up a SecOff that then becomes unable to respond or assist in other duties. Needing to utilize guns, stun batons and flashes means a SecOff must return to Sec to refill, and if materials are scarce this wait can be even longer. Similarly, health is a resource which will cause time and personnel loss from the SecOff needing to be treated.

Information helps mitigate these losses; knowing who to search, what materials to prepare and where to go. The more Security has of each resource the more effective it will be, and overabundance of one resource can make up for the lack of another. Some of these resources put strain on other departments however; materials may be necessary to craft or refill vital Security equipment, but those materials come from Cargo's work. Any rule change that relaxes the requirements on Security should instead impose a drain on its resources. For example, guessing uplink codes is usually too much of a timesink and takes up an officer's attention despite it being allowed by the rules, so it's rarely done.

## The Implant Problem

```admonish quote
Implant checking someone "just in case" after being arrested for some unrelated crime.
```

Implants are very useful to Syndicates since they allow direct access to certain functionality and are hidden by default. Security is unable to detect an implant unless it has been used, though it may be suspected through circumstantial evidence. The DNA Scrambler is a great example of this; if it's not witnessed being used, Security will first have to a) find the user, b) detect they are not on the manifest, c) make a determination whether a DNA implanter was used and/or find the used implanter. 

There is a big weakness to implants however. SecOffs can use an implanter to extract implants, and the mechanical limitation to this is relatively minor. Acquiring an implanter can be easily done via Medical, and while the doafter to use one is pretty long it's nothing compared to the brig times a suspected antag may have. This means they can be very easily taken away from the antag by any SecOff who wishes to do the procedure.

Strangely, implant searches are much more restrictive on MRP. To check, Security must have witnessed an implant being used, or any other explanation must be *extremely* unlikely. This requirement is held up to an almost absurd amount; you can't check for a Storage or Uplink implant if someone suddenly has a weapon in perma, because someone could have broken in, given them the gun and then left after repairing the hole. This means subtle implants or one-time use implants like the Storage Implant and DNA Scrambler are much more valuable on MRP since a suspicion is nowhere near enough to be allowed to implant check. 

### Proposed Solution

Security should not have any rule limitations on checking implants, but instead Security should be mechanically discouraged from performing random implant checks. I propose the following:
- Rule change: Security has knowledge of implants; that they exist, and what types the Syndicate have access to.
- Rule change: Security has no limitations on performing implant checks.
- Checks can only be performed with the `Implant Extractor`, a device that can be printed in the Medfab.
- To extract, the Implant Extractor must be set to the specific type of implant to be extracted. A doafter is then performed.
   - If successful, the chosen implant gets extracted into the Implant Extractor similar to how an Implanter is done now.
   - If unsuccessful, no implant is extracted. The user that tried to use the Implant Extractor takes 45 Cellular damage, ignoring resistances, as the device backfires.
 
The main point is the damage taken by the Implant Extractor. Performing an implant check without sufficient suspicion and being wrong becomes a very high price to pay, encouraging Security to be sure of their search. Even a single failed search essentially requires the user to be sent to the medbay, and two puts them out of commission for a long time.

Note: The particulars of this suggestion may change as Newmed/Surgery gets implemented. The important part is that implant searching someone without being correct should punish Security by temporarily taking away a resource, in this case in the form of personnel.

## The PDA / Uplink Problem

```admonish quote
Confiscating PDAs of anyone you suspect of being a traitor without proof.
```

Uplinks are in a kind of weird situation where it's one of the most powerful tools for a Traitor and in-universe a very well-hidden feature, but at the same time it's also one of the easiest metaknowledge items in the game. As soon as a player has been found using a traitor-exclusive item Security players have to pretend that the PDA isn't a high target to confiscate. The reason for this is because you generally want antags to be able to use all their TC during a round to make it interesting. As such, the PDA may only be confiscated for two reasons:
- Security finds an open uplink in the PDA.
- Security has previously found an open uplink in another PDA, and can thus pre-emptively confiscate any PDA they have reasonable suspicion of having an uplink.

Right now the rules are the main way of preventing overzealous Security confiscating PDAs. Traitors do have a gameplay option as well: The Uplink Implant. This implant does have the benefit of making PDA confiscating a non-issue, but the tradeoff is 2 less TC and an implanter that must be disposed of, and with the stringent rules on PDA confiscating it's unlikely to get any benefit from it. There's no reason to keep the uplink open after the implant is used, so you only get value if another uplink has been found. Additionally it suffers from the vulnerability of implant checks.

### Proposed Solution

The PDA is very easily the single point of failure with this problem, but it's also unique in its ringtone lock. Confiscating a PDA does come with some cost to Security in that they need to secure a replacement; worth it for a confirmed Syndie, but not viable for all arrests. If we were to remove the limitations on Security randomly confiscating PDAs there would need to be an equally effective method of eluding detection. It would also need to incur a cost for Security to confiscate. I propose the following:

- Rule change: Security has knowledge PDAs can contain Uplinks, and may confiscate them if they have a reason to believe it could contain one.
- Uplink Implanter cost is reduced to 1 TC, and changes proposed in "The Implant Problem" are also included.
- The Uplink Patch is a new device that can be bought from the Uplink for 1 TC.
  - The Uplink Patch can be attached to any object and turns it into an Uplink.
  - The Uplink can be locked and unlocked by saying one of the agent codewords while wearing/holding/carrying the object.
  - TC must be inserted into the object to purchase anything.

The Uplink Patch would turn any object into a possible Uplink, making the permutations for what to confiscate anything in the Syndie's inventory. Even if a SecOff would be overzealous and try to take everything, the uplink could be an implant as well. With the changes in the Implant Problem, this would require Security to have strong suspicion of where the uplink would be to actually catch it.

## The Thief Gloves Problem

Thief gloves come in two varieties, each with their own problem. 

1. Normal Thief Gloves are indistuingishable from black gloves. The only way to know they have been used is if someone finds out an item on their person has been stolen, and even then Security are not allowed to know they must search for black gloves unless an uplink has been previously found. They also stand out for crew who don't normally wear black gloves, making overzealous SecOffs search and possibly even confiscate them.

2. Chameleon Thief Gloves mean to remedy this. However, as they leave holographic fibers on everything they touch it becomes very obvious whenever they have been used. It leads to a rather opaque and unintuitive game of trying to not wear the thief gloves except in the most critical of moments, making finding a spare pair of gloves in someone's bag highly suspicious. They're also trivial to check since it's just to put them on and check whether they allow Chameleon properties.

### Proposed Solution

- Thieving Gloves and Chameleon Thieving Gloves are merged into a single item: The Thief Glovebox.
  - When purchased/obtained, the user is given a box. Opening this box activates a UI similar to a Chameleon UI.
  - Once a glove design is chosen, the user is given a pair of thieving gloves with that design.
  - The gloves give off matching fibers. They are not Chameleon.
- Non-engineering insulated gloves/budget insulated gloves now come in 3 different colors with corresponding colored fibers. They are still called "Insulated Gloves"/"Budget Insulated Gloves". 
- Rule change: Security has knowledge of Thieving Gloves and may confiscate the gloves of anyone who has stolen or attempted to steal contraband.
- Rule change: An additional rule is added: Security may *not* test Thieving Gloves by putting them on and trying to steal an item off someone.

This means that a thief is safe from having their gloves lost before committing a crime. Detectives can no longer use holofibers to confirm a Thief antag, but must instead rely on the fibers of the gloves around the crime scene. The addition of additional insuls colors means selecting yellow insulated gloves is no longer a safe option to blend in with all the other yellow gloves.

## The Thief Sets Problem

### Proposed Solution

## The Disguised Items Problem

### Proposed Solution

## Other Problems that have PRs in the works

- Roundtype problem
- Map loot problem
