# Revolutionaries Rework

| Designers | Implemented | GitHub Links |
|---|---|---|
| SlamBamactionman | :x: No | TBD |

## Overview

Revolutionaries as a gamemode is a mechanically and thematically interesting concept; sedition against the station's established authority sounds fun and there is a lot of design space to work within to represent this in mechanics. Previous iterations of Revolutionaries (Revs) have however been seen as encouraging too much combat with too snowball-y rounds for either side, frustrating "metagameable" mechanics and design that both directly and indirectly encourages removing a sizeable number of players from the round. 

This rework intends to address many of the critiques of the original Revs gamemode while still keeping to the theme of exaggerated "Space Communism", allowing for the Revs faction to take over the station via stealth, subterfuge, blatant opposition or violence. 

### Breakdown
<sup>In this document, the default side players belong to will be referred to as either "crew" or "Command".</sup>

Revolutionaries are a team conversion antag: a small number of players begin as antagonists, but are able to convert crew to antags, with the antag faction's strength largely being dependent on the number of conversion. As a conversion antag, a round with Revolutionaries should attempt to follow the stages below. 

- Initial conversions
  - This is the stage where the antag begin conversion crew - this should be done stealthily, and failing to do so may result in a swift win for crew. To their benefit the antag is given some kind of initial advantage, providing a quick power bump to get things going.
- Expansion with risk
  - During this stage the antag faction grows, exhibiting signs and actions that may be more noticeable by crew. Staying stealthy becomes more difficult due to the number of antags growing, pushing the antags into more direct confrontration.
- Confrontation with crew
  - The antag faction has been exposed and crew are now working to counteract the antags. Depending on how well the two previous stages have gone the crew may be in either a good or poor position to fight back.
- Climax
  - An encounter between the antags and crew that largely decides the outcome of the round. 
- Resolution
  - After the climax the round finishes up, resolving the round for remaining players. Usually this is the last few minutes before the evacuation shuttle arrives.

Issues arise when one of these stages are too long, too short or entirely skipped over. A round doesn't necessarily have to be ruined just because a stage is misplaced, however if there are no sufficient back-up scenarios to fall back on the round may end up frustrating for some amount of the round's players (e.g. stalling, dragged out fighting, antag gets found too early without getting to affect the round, no resolution so players just evacuate).

This design document will try to ensure a round with a Rev antag follows this pattern.

### Revolutionaries gamemode, Goals

The goals that we want to reach with the Revolutionaries are the following:
- Revolutionaries should be applicable as its own round type and as a mid-round antag, equivalent to Nukies/LoneOp or Traitors/Mid-round Traitors. The difference should be in the number of antags and the resources available.
- Round removal should be discouraged where possible. It should not be the optimal choice to gib or leave a player to rot unless in specific circumstances.
- Revolutionaries should not be discovered through no fault of their own in the Initial Conversions phase (i.e. metagameable mechanics).
- A single non-Security crew member discovering an antag should not spell the end of the antag faction's progression in the round.
- Round end conditions should be clear and straight-forward, though a crew overcoming the antag shouldn't necessarily mean the end of the round.
- Crew shouldn't be able to hard counterplay the antag without engaging with the antag. 


## New Revolutionaries, Basic layout
<sup>Any values given here are suggestions, and should be adjusted based on playtesting.</sup>

The Revolutionary antag begins either as a 2-4 roundstart antag roll for the Revolutionary gamemode, or a single crewmember secretly becomes a Revolutionary antag during another gamemode midround.

Revolutionary antags that start out this way are considered Head Revolutionaries (HeadRevs). A Head Revolutionary has the duty to begin the conversion of other crew and have some extra tools at their disposal to strengthen the progression of the antag faction, but they are not strictly necessary for the revolution antags to succeed. The goal for Head Revolutionaries is to convert crew to grow the faction's strength, convert department Heads and survive until the evacuation shuttle without being deconverted. 

Head Revolutionaries share the same team and when they are given the role they obtain the names and jobs of the other Head Revolutionaries on the station. Revolutionaries can be identified by other revolutionaries via an icon next to their character, however Head Revs do not have a unique icon.

For crew, the goal is to deconvert revolutionary converts, protect Heads from being converted, and ensure Head Revs are discovered and/or do not make it onto the evacuation shuttle. 

### Win Conditions

Win conditions for a round with a Revolutionary antag are the following:

- Revolutionary Major Victory: No *alive, unrestrained* Command *on the evac shuttle* are non-rev, >50% of Command are converted Revolutionaries.
- Revolutionary Minor Victory:  No *alive, unrestrained* Command *on the evac shuttle* are non-rev, <50% of Command are converted Revolutionaries.
- Rev-Crew Tie: Both Rev Minor & Crew Minor criteria are met, or neither Rev Minor & Crew Minor criteria are met.
- Crew Minor Victory: No *alive, unrestrained* headrevs are *on the evac shuttle* when Evac reaches CentComm.
- Crew Major Victory: *All* revolutionaries are *deconverted* or *dead* when Evac reaches CentComm.

The round-end screen could look like the following:

```
Revolutionary Major Victory!
X% of Crew were converted to the Revolution.
X% of Command were converted to the Revolution.
0 Loyal Command made it to CentComm.
X Head Revolutionaries made it to CentComm.
```

```
Crew Minor Victory!
X% of Crew were converted to the Revolution.
X% of Command were converted to the Revolution.
X Loyal Command made it to CentComm.
0 Head Revolutionaries made it to CentComm.
```

```
Crew Major Victory!
All Revolutionaries were killed or deconverted!
```

## Conversion

Conversion is how the Revolutionary antag faction grows, and is a *requirement* to obtain Revolutionary Major Victory. To convert a crewmember they must be interacted with by a Revolutionary over time, and once a critera is met they can be converted to the Revolution. Crew are also able to de-convert Revolutionaries. Conversion is not restricted to Headrevs, though they have access to certain tools that benefit them in this regard.

To represent the convertable state a crewmember is in and the faction they belong to, there is now a hidden nummerical stat called Conversion Health Points (CHP). 

### Conversion Health Points & Damage

All sentient crew have Conversion Health Points, which can normally range between 100 to -100 CHP. All crew, unless specified, begin at a full 100 CHP.

- Revolutionaries are able to do specific actions that "deal damage" to a crewmember's CHP, gradually lowering it with varying effectiveness depending on how covert or obviously antagonistic the action is. 
- If a crewmember gets below <10 CHP, they enter a Convertable state.
  - As long as the crewmember is not a Revolutionary, their CHP can not be reduced below 0. They will remain in the Convertable state until their CHP rises above 10 CHP again.
  - While a crewmember is in the Convertable state,  they can be converted into a Revolutionary via specific actions available to Revolutionaries.
  - When converted to a Revolutionary, their CHP is set to -25.
- Crew are able to "heal" CHP via specific actions, deconverting Revolutionaries into normal crewmembers.
  - If a Revolutionary's CHP is no longer in the negatives (i.e. at >=0 CHP), they instantly revert into a normal crewmember with 25 CHP and lose their antag status. *This is true for Headrevs as well.*

Headrevs are unique in that they have a CHP range between -500 and 100 CHP. Headrevs begin at -500 CHP when they are given the antag status. As a benefit of being a Headrev, they are able to visually see the current CHP of any crewmember, similar to a health HUD display. 

The Captain is also unique in that they always have 100 CHP and can never go below this. This makes the Captain unconvertable to the Revolution, and they are the only Command on the station with this property. CentComm agents and other Admeme should be similarly unconvertable by default.

Unlike normal damage, CHP can only be dealt/healed to an individual who is alive and not in crit. 

### Mindshields

Mindshield implants are a way to add extra safety for vital station personnel. They can not prevent or heal conversion on its own, but provides a buffer that requires the Revolutionaries to put in targeted effort to successfully convert someone with a mindshield. The mindshield is not a hard counter to Revolutionaries and while serving some use in preventing conversion they are not useful for deconversion.

Command and Security are the only roles that have mindshields roundstart.

- A mindshield gives its owner a "shield" with 100 CHP. The mindshield absorbs any CHP damage dealt to the owner and takes it instead.
- If the mindshield reaches 0 CHP, it breaks and is removed from its owner.
- The shield slowly regains CHP on its own, at 0.2 CHP / second.
- Having a mindshield does not change Revolutionary status or antag faction; a Revolutionary can be mindshielded and still belong to the Revolution.

Mindshields only protects the owner from CHP *damage*. Someone with a mindshield can still be healed.

### Revolutionary Codewords & CHP Damage

Revolutionary codewords is the main way a Rev convert crew, and is the primary conversion method the gamemode is balanced around. When becoming a Revolutionary (Headrev or converted) you are provided with a number of codewords that when spoken deals CHP damage to anyone hearing it. These codewords are unique to each Headrev and are passed on to whatever Revolutionary they convert, and any further conversions down the chain get the same codewords passed on. 

Codewords come in three levels; Low, Mid and High Conversion words.
  - Low Conversion words are meant to be easy to incorporate into normal speech. There should be so many possible low conversion words that can be rolled that it becomes effectively impossible to metagame.
  - Mid Conversion words deal a decent amount of CHP damage but can be noticed if one pays attention. These would be at the risk of metagaming due to being flavored towards revolutionary speech, so it would be on the rev player to incorporate them well into conversations.
  - High Conversion words are very clearly revolutionary and deal high CHP damage, *and is able to convert a crewmember in the Convertable state. They should be mostly useful when the revolution is in full swing, but risky for a non-convertable crewmember to overhear.

Dealing damage with codeword has a 10 second cooldown, to avoid simply spamming the codewords. Damage is also split among the crew who hear it, making speech directed to a single individual more effective at targeted conversion, while multiple Revolutionaries can shout it out to crowds without the conversion happening to fast.

Codewords are proposed to deal the following damage:
  - Low: 10 CHP
  - Mid: 20 CHP
  - High: 30 CHP, and converts any crew in the Convertable state.

Codewords are able to deal damage even when communicated across different mediums, however the conversion strength is reduced to compensate for how easy it may be to do so:

- A Revolutionary speaking a codeword through a headset radio deals 0.15x CHP damage.
- Announcement messages with a codeword by a Revolutionary deals 0.5x CHP damage.

### Deconversion
- deconversion is the main way for crew to fight back against the revolution.
- deconversion should be fairly easy when targeted but shouldn't happen by accident. 
- deconversion returns a player to the crew side; doing this allows the player to sell out the revolutionaries they have interacted with
- a deconverted crewmate should be able to be converted again

- methods of deconversion:
  - harm baton heals 10 CHP
  - being in cuffs heals 0.5 CHP / second
  - wearing an electro pack heals 0.5 CHP / second

- if a headrev reaches 0 CHP, they are fully deconverted and lose their antag status


## Revolutionary Items

### Generally available items
Headbands:
- Headbands can be cut up using a sharp object to turn into a headband
- This is a fashion accessory accessible to all crew, however when worn by a revolutionary codewords they say deal 1.5x more damage.

Revolutionary posters:
- Crew can print rolled-up posters from autolathes using cloth
- These posters are randomized when printed, and can result in loyal, neutral or revolutionary posters
  - Examining a rolled-up poster gives its name
- Revolutionary posters have a radius of influence when put up.
  - When inside this radius, you take 0.25 CHP damage / second
  - When inside this radius, codewords deal 1.25x more damage
- Loyal posters also have a radius of influence when put up.
  - When inside this radius, you heal 0.25 CHP damage / second
  - When inside this radius, codewords deal 0.5x damage
- Posters can be taken down, and if recycled gives back some cloth

### Dead Drop Duffelbag / The Revolutionaries Uplink 
- can be spawned by rummaging through any disposals bin
- when used, opens the store
- can be carried around to access the store at any point & when worn deals passive conversion damage in an area around the wearer
- when placed back into a disposals bin it disappears.
- one dead drop item is available per headrev per tier
  - the next tier unlocks when a certain percentage of the station has been converted


### Dead Drop Items
tier 1:
tier 1 items should help the revolution grow in a stealthy or efficient way, in ways that don't involve combat
- the classic: a two-use flash that deals massive conversion damage and can convert
- headset override: when used on a headset adds the revolutionary channel
- revolutionary poster blueprint: allows producing rev posters directly, for cheaper cost
- expanded reading: unlocks more revolutionary codewords
- how to hug: after reading this book, hugging someone deals minor CHP damage.
- revolutionary stamp: any document stamped with this red stamp deals high CHP when read.

tier 2:
tier 2 items should allow the revolution to blossom; these should have conditional usecases, meaning a headrev selects the one that is most suitable for how the revolution has developed
- marximov: revolutionary-aligned AI lawboard
- cargommunism pad: QM's cargo pad but doesn't announce the purchase
- cyanide pills: a bottle of pills. when ingested, unlocks the ability to kill oneself with 200 poison, dealing 80 CHP damage in a radius around the user
- de-friedman-rillator: converts someone who is brought to life with this defibrillator

tier 3: 
tier 3 items is the revolution's capstone ability; if the revolution reaches this stage, the item should provide an option for the revs to go loud, or a way to comeback against a crew that is trying to fight back
- mind swap: allows you to change mind with a fellow revolutionary. a trusted scapegoat.
- revolutionary leader cap: amplifies conversion damage dealt by the wearer's codewords       
- megaphone: codeword damage spoken when holding a megaphone is not split; full damage is dealt to all who hear it                                                                                                                          
