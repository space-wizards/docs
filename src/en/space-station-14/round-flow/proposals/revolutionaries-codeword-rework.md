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

--- uuuuuuuh below is draft ---
## Basic layout
headrevs exist, several can spawn if it is the revolutionaries gamemode, and one spawns if it's a midround. headrevs can see each other. whenever a value is given it's a *suggestion* and will need to be tweaked based on playtests and feedback.

## Conversion Damage
- crew have conversation HP (CHP), in the range of 100 to -100 CHP. Crew begin at 100 CHP.
- revolutionaries can do covert and loud actions to deal conversion damage.
- if the CHP becomes 0, the crewmember gets into a convertable state.
  - in this state, revs can perform certain actions to convert the crewmember to being a revolutionary. this sets their CHP to -25. 
- if the CHP goes above 0 after being in the negatives, it gets set to 25 CHP. 
- headrevs have a range of CHP between -500 and 100, and starts at -500.
- the Captain is unique in that they always have 100 CHP and cannot go below this
- headrevs can see a healthbar of an individual's CHP
- CHP can only be dealt/healed when alive, non-crit

- having a mindshield gives the character a shield with 100 CHP
  - the mindshield takes CHP damage before the character
  - the shield slowly regains CHP, 0.2 CHP / second
  - if the mindshield reaches 0 CHP, it breaks
  - this does not change revolutionary status; a revolutionary can be mindshielded, but they are still a revolutionary.
  - someone who is mindshielded can still have their CHP healed

## Deconversion
- deconversion is the main way for crew to fight back against the revolution.
- deconversion should be fairly easy when targeted but shouldn't happen by accident. 
- deconversion returns a player to the crew side; doing this allows the player to sell out the revolutionaries they have interacted with
- a deconverted crewmate should be able to be converted again

- methods of deconversion:
  - harm baton heals 10 CHP
  - being in cuffs heals 0.5 CHP / second
  - wearing an electro pack heals 0.5 CHP / second

- if a headrev reaches 0 CHP, they are fully deconverted and lose their antag status

## Revolutionary Codewords
- revolutionary codewords is the main way a rev can convert crew
- hearing a revolutionary codeword spoken by a revolutionary will deal conversion damage
- codewords come in three levels; low, mid and high conversion.
  - low conversion words are easy to incorporate into normal speech. these should be so many, so wide that they are effectively impossible to metagame.
  - mid conversion words deal a decent amount of damage but can be noticed if one pays attention. these would be at the risk of metagaming, so it would be on the rev player to incorporate them well.
  - high conversion words are very clearly revolutionary and deal high conversion damage. mostly useful when speaking to crew with high conversion damage to seal the deal, but risky if someone with low conversion damage hears it.
- these codewords are unique to each headrev
  - when a crewmate is converted, they are given the codewords as well
- damage dealt is split among the crew who hear it
- dealing codeword conversion damage has a 10 second cooldown
- codewords deal the following damage:
  - low: 10 CHP
  - mid: 20 CHP
  - high: 30 CHP, converts any crew in a convertable state

## Dead Drop Duffelbag / The Revolutionaries Uplink 
- can be spawned by rummaging through any disposals bin
- when used, opens the store
- can be carried around to access the store at any point & when worn deals passive conversion damage in an area around the wearer
- when placed back into a disposals bin it disappears.
- one dead drop item is available per headrev per tier
  - the next tier unlocks when a certain percentage of the station has been converted

## Win Conditions
Win conditions are the following:
[draft]
rev major victory: no *alive, unrestrained* command *on the evac shuttle* are non-rev, >50% of command are revolutionary
rev minor victory:  no *alive, unrestrained* command *on the evac shuttle* are non-rev, <50% of command are revolutionary
rev-crew tie: both rev minor & crew minor criteria are met, or neither rev minor & crew minor criteria are met
crew minor victory: no *alive, unrestrained* headrevs are *on the evac shuttle* when evac reaches centcom
crew major victory: *all* revolutionaries are *deconverted* or *dead* when evac reaches centcom

### Generally available items
Headbands:
- Headbands can be cut up using a sharp object to turn into a headband
- This is a fashion accessory accessible to all crew, however when worn by a revolutionary codewords they say deal 1.5x more damage.

Revolutionary posters:
- Crew can print posters from autolathes
- These posters are randomized, and can result in loyal, neutral or revolutionary posters
- Revolutionary posters have a radius of influence.
  - When inside this radius, you take 0.25 CHP damage / second
  - When inside this radius, codewords deal 1.25x more damage
- Loyal posters also have a radius of influence.
  - When inside this radius, you heal 0.25 CHP damage / second
  - When inside this radius, codewords deal 0.5x damage

### Dead Drop Items
tier 1:
- the classic: a two-use flash that deals massive conversion damage and can convert
- headset override: when used on a headset adds the revolutionary channel
- revolutionary poster blueprint: allows producing posters directly, for cheaper cost
- expanded reading: unlocks more revolutionary codewords

tier 2:
- marximov: revolutionary-aligned AI lawboard
- cargommunism pad: QM's cargo pad but doesn't announce the purchase
- cyanide pills: a bottle of pills. when ingested, unlocks the ability to kill oneself with 200 poison, dealing conversion damage around you
- de-friedman-rillator: converts someone who is brought to life with this defibrillator

tier 3: 
- mind swap: allows you to change mind with a fellow revolutionary. a trusted scapegoat.
- revolutionary leader cap: amplifies conversion damage dealt by the wearer's codewords       
- megaphone: codeword damage spoken when holding a megaphone is not split; full damage is dealt to all who hear it                                                                                                                          
