# Revolutionaries Rework

| Designers | Implemented | GitHub Links |
|---|---|---|
| SlamBamActionman<br>ScarKy0 | :x: No | TBD |

## Overview

Revolutionaries as a gamemode is a mechanically and thematically interesting concept; sedition against the station's established authority sounds fun and there is a lot of design space to work within to represent this in mechanics. Previous iterations of Revolutionaries (Revs) have however been seen as encouraging too much combat with too snowball-y rounds for either side, frustrating "metagameable" mechanics and design that both directly and indirectly encourages removing a sizeable number of players from the round. 

This rework intends to address many of the critiques of the original Revs gamemode while still keeping to the theme of exaggerated "Space Communism", allowing for the Revs faction to take over the station via stealth, subterfuge, blatant opposition or violence. 

This design document is inspired by ideas presented by the the following works and authors:<br>
https://github.com/space-wizards/docs/pull/251 - CaelleakNavinski<br>
https://github.com/space-wizards/docs/pull/146 - illdoodle<br>
ScarKy0

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

This design document will try to ensure that a round with a Rev antag follows this pattern.

### Revolutionaries Gamemode Goals

The goals that we want to reach with the Revolutionaries are the following:
- Revolutionaries should be applicable as its own round type and as a mid-round antag, equivalent to Nukies/LoneOp or Traitors/Mid-round Traitors. The difference should be in the number of antags and the resources available.
- Round removal should be discouraged where possible. It should not be the optimal choice to gib or leave a player to rot unless in specific circumstances.
- Revolutionaries should not be discovered through *no fault of their own* in the Initial Conversions phase (i.e. metagameable mechanics). 
- A single non-Security crew member discovering an antag should not spell the end of the antag faction's progression in the round.
- Round end conditions should be clear and straight-forward, though a crew overcoming the antag shouldn't necessarily mean the end of the round.
- Crew shouldn't be able to hard counterplay the antag without engaging with the antag. 


## New Revolutionaries, Basic layout
<sup>Any values given here are suggestions and are especially marked by being **bolded**. Any such value should be adjusted based on playtesting.</sup>

The Revolutionary antag begins either as a 2-4 roundstart antag roll for the Revolutionary gamemode, or a single crewmember secretly becomes a Revolutionary antag during another gamemode midround.

Revolutionary antags that start out this way are considered Head Revolutionaries (HeadRevs). A Head Revolutionary has the duty to begin the conversion of other crew and have some extra tools at their disposal to strengthen the progression of the antag faction, but they are not strictly necessary for the revolution antags to succeed. The goal for Head Revolutionaries is to convert crew to grow the faction's strength, convert department Heads and survive until the evacuation shuttle without being deconverted. 

Head Revolutionaries share the same team and when they are given the role they obtain the names and jobs of the other Head Revolutionaries on the station. Revolutionaries can be identified by other Revolutionaries via an icon next to their character; Head Revs have a unique icon that is only visible to other Head Revs, though to regular Revolutionaries they do not have a unique icon and appear as normal Revolutionaries.

For crew, the goal is to deconvert revolutionary converts, protect Heads from being converted, and ensure Head Revs are discovered and/or do not make it onto the evacuation shuttle. 

### Win Conditions

Win conditions for a round with a Revolutionary antag are the following:

- Revolutionary Major Victory: No *alive, unrestrained* Command *on the evac shuttle* are non-rev, >**50%** of Command are converted Revolutionaries.
- Revolutionary Minor Victory:  No *alive, unrestrained* Command *on the evac shuttle* are non-rev, <**50%** of Command are converted Revolutionaries.
- Rev-Crew Tie: Both Rev Minor & Crew Minor criteria are met, or neither Rev Minor & Crew Minor criteria are met.
- Crew Minor Victory: No *alive, unrestrained* headrevs are *on the evac shuttle* when Evac reaches CentComm.
- Crew Major Victory: *All* revolutionaries are *deconverted* or *dead* when Evac reaches CentComm.

The round-end screen could look like the following:

```
Revolutionary Major Victory! [Green text]
X% of Crew were converted to the Revolution. [Yellow text]
X% of Command were converted to the Revolution.  [Green text]
0 Unconverted Command made it to CentComm. [Green text]
X Head Revolutionaries made it to CentComm. [Green text if >0]
```

```
Revolutionary Minor Victory! [Green text]
X% of Crew were converted to the Revolution. [Yellow text]
X% of Command were converted to the Revolution. [Red text]
0 Unconverted Command made it to CentComm. [Green text]
X Head Revolutionaries made it to CentComm. [Green text if >0]
```

```
Revolutionary-Crew Tie! [Green text]
X% of Crew were converted to the Revolution. [Yellow text]
X% of Command were converted to the Revolution. [Red text]
0 Unconverted Command made it to CentComm. [Red text]
0 Head Revolutionaries made it to CentComm. [Red text]
```

```
Crew Minor Victory! [Green text]
X% of Crew were converted to the Revolution. [Green text]
X% of Command were converted to the Revolution. [Green text]
X Loyal Command made it to CentComm. [Red text]
0 Head Revolutionaries made it to CentComm. [Red text]
```

```
Crew Major Victory! [Green text]
All Revolutionaries were killed or deconverted! [Red text]
```

## Conversion

Conversion is how the Revolutionary antag faction grows, and is a *requirement* to obtain Revolutionary Major Victory. To convert a crewmember they must be interacted with by a Revolutionary over time, and once a criteria is met they can be converted to the Revolution. Crew are also able to de-convert Revolutionaries. Conversion is not restricted to Headrevs, though they have access to certain tools that benefit them in this regard.

To represent the convertable state a crewmember is in and the faction they belong to, there is now a hidden nummerical stat called Loyalty Health Points (LHP). 

### Loyalty & Loyalty Damage

All sentient crew have Conversion Health Points, which can normally range between 100 to -100 LHP. All crew, unless specified, begin at a full 100 LHP.

- Revolutionaries are able to do specific actions that "deal damage" to a crewmember's LHP, gradually lowering it with varying effectiveness depending on how covert or obviously antagonistic the action is. 
- If a crewmember gets below <**10** LHP, they enter a Convertable state.
  - As long as the crewmember is not a Revolutionary, their LHP can not be reduced below 0. They will remain in the Convertable state until their LHP rises above **10** LHP again.
  - While a crewmember is in the Convertable state, they can be converted into a Revolutionary via specific actions available to Revolutionaries.
  - When converted to a Revolutionary, their LHP is set to **-25**.
  - A successful conversion is silent for surrounding players, however the player who is converted gets a pop-up and the appropriate music stinger.
- Crew are able to "heal" LHP via specific actions, deconverting Revolutionaries into normal crewmembers.
  - If a Revolutionary's LHP is no longer in the negatives (i.e. at >=0 LHP), they instantly revert into a normal crewmember with **25** LHP and lose their antag status. *This is true for Headrevs as well.*
  - Deconversion causes the person to fall to the floor for a second, as they remember their original allegiance.

Headrevs are unique in that they have a LHP range between **-500** and 100 LHP. Headrevs begin at **-500** LHP when they are given the antag status. As a benefit of being a Headrev, they are able to visually see the current LHP of any crewmember, similar to a health HUD display. 

The Captain is also unique in that they always have 100 LHP and can never go below this. This makes the Captain unconvertable to the Revolution, and they are the only Command on the station with this property. CentComm agents and other Admeme should be similarly unconvertable by default.

Unlike normal damage, LHP can only be dealt/healed to an individual who is conscious (i.e. awake, alive and not in crit). 

### Revolutionary Codewords & LHP Damage

Revolutionary codewords is the main way a Rev convert crew, and is the primary conversion method the gamemode is balanced around. When becoming a Revolutionary (Headrev or converted) you are provided with a number of codewords that when spoken deals LHP damage to anyone hearing it. These codewords are unique to each Headrev and are passed on to whatever Revolutionary they convert, and any further conversions down the chain get the same codewords passed on. 

Codewords come in three levels; Low, Mid and High Conversion words, with **5** codewords given in each level.
  - Low Conversion words are meant to be easy to incorporate into normal speech. There should be so many possible low conversion words that can be rolled that it becomes effectively impossible to metagame. Examples: "love", "hello", "great", "hate".
  - Mid Conversion words deal a decent amount of LHP damage but can be noticed if one pays attention. These would be at the risk of metagaming due to being flavored towards revolutionary speech, so it would be on the rev player to incorporate them well into conversations. Examples: "disrupt", "rise up", "join".
  - High Conversion words are very clearly revolutionary and deal high LHP damage, *and is able to convert a crewmember in the Convertable state. They should be mostly useful when the revolution is in full swing, but risky for a non-convertable crewmember to overhear. Examples: "viva", "communism", "comrade".

Dealing damage with codeword has a **10** second cooldown, to avoid simply spamming the codewords. Damage is also split among the crew who hear it, making speech directed to a single individual more effective at targeted conversion, while multiple Revolutionaries can shout it out to crowds without the conversion happening to fast. Using multiple codewords in one sentence does not do anything; it simply uses the highest-tier codeword instead.

Codewords are proposed to deal the following damage:
  - Low: **10** LHP
  - Mid: **20** LHP
  - High: **30** LHP, and converts any crew in the Convertable state.

Codewords are able to deal damage even when communicated across different mediums, however the conversion strength is reduced to compensate for how easy it may be to do so:

- A Revolutionary speaking a codeword through a headset radio deals **0.2**x LHP damage. (Note that crew passively heal LHP, as described in the Deconversion section)
- The first time a Revolutionary uses the Announcement console to send a message with a codeword, it deals **1**x LHP damage, without being divided among the people hearing it. This is a one-time trigger.

### Deconversion

Deconversion is the main way for crew to fight back against the revolution. It should be fairly easy when targeted at isolated Revolutionaries but require more work when Revolutionaries are together. It should also not happen by accident; crew should consciously attempt it to be successful.

Deconversion puts you fully on the crew side. This does fully include the ability to sell out your fellow Revolutionaries by remembering their names. Headrevs therefore have a choice to act more stealthily disguise themselves and blend in with the Revolution, or assign another Revolutionary (possibly their first convert) to act as the revolution's leader to throw off potential deconvert sell-outs. 

Methods of deconversion include:
  - Harm baton, heals **10** LHP per hit
  - Being in cuffs heals **0.5** LHP / second
  - Wearing an electro pack heals **0.5** LHP / second

Loyal crew are also able to passively heal LHP at **0.1** LHP / second, though as this does not happen for Revolutionaries it can not be used for deconversion. This passive heal is disabled for **10** seconds upon taking LHP damage.

A deconverted Revolutionary can be reconverted again. If a Headrev is deconverted (>= 0 LHP) they lose their antag status, and being converted to the Revolution makes you a normal Revolutionary. 

### Death & LHP Damage

Authoritarian regimes killing of protesting civilians causing further unrest, or freedom fighters getting a shock when they first murder someone, are concepts that are closely tied to a revolution. They are also ideas that would be suitable mechanically to combat murder sprees from either side during a Revolution round. The following section is only relevant for crew and Revs; non-crew characters (pets, mobs) and other antags (traitors, Nukies) do not interact with the following mechanic.

If a Revolutionary *or crewmember* dies by the hand of another crewmember (being dealt the damage that put them in a critical state), they will deal **15** non-split LHP in a **8** tile line-of-sight radius around their body. While remaining dead they will also provide a passive **-0.1** LHP / second in a **4** tile line-of-sight radius. This works in the same way but in reverse if a Revolutionary performs the kill, healing LHP upon death when killed by a Revolutionary/Crewmember. The initial burst also has a **120** second cooldown, to avoid repeatedly reviving and killing the same person twice to trigger the effect. This means both sides are discouraged from indiscriminately killing, favoring limited killing and kidnapping. 

If the death of a *Revolutionary* is at the hand of a *crewmember*, the initial burst of LHP damage is able to convert. This is not true for the death of a crewmember by the hand of a crewmember (otherwise large-scale death in other gamemodes could risk spawning Revolutionaries without any headrev). 

Being converted/deconverted by a character dying displays a special conversion message, to indicate it was the reason for being converted/deconverted.

There is an interesting dichotomy that can form here where Revolutionaries have an easier time to "heal" revolutionary fervor by dealing LHP damage to each other via chanting codewords. On the other hand, Security has more access to stun weaponry and as such have an easier time subduing Revolutionary groups non-lethally. 

### Mindshields

Mindshield implants are a way to add extra safety for vital station personnel. They can not prevent or heal conversion on its own, but provides a buffer that requires the Revolutionaries to put in targeted effort to successfully convert someone with a mindshield. The mindshield is not a hard counter to Revolutionaries and while serving some use in preventing conversion they are not useful for deconversion.

Command and Security are the only roles that have mindshields roundstart.

- A mindshield gives its owner a "shield" with **100** LHP. The mindshield absorbs any LHP damage dealt to the owner and takes it instead.
- The shield slowly regains LHP on its own, at **0.2** LHP / second. This functionality does not work when converted to the Revolution. 
- Having a mindshield does not change Revolutionary status or antag faction; a Revolutionary can be mindshielded and still belong to the Revolution.
- A newly injected mindshield always has full LHP, regardless of Revolutionary status.
- Mindshields can be removed, much like any other implant. The exceptions for this is the Captain and ERT/CentComm, who have unremovable mindshields (however due to being unconvertable, this is mostly just flavor). 

New mindshields are able to be purchased from Cargo at a reasonable price. One possible suggestion would be 4 implanters for $8000.

## Revolutionary Items

To assist in the revolution, Revolutionaries have access to a multitude of items. Some are generally available regardless of roundtype, while some are specific to the Revolutionary antag. The choice and utilization of these items should provide players options and flavors for how the revolution plays out. It's important that the items do not encourage gameplay that go against the Revolutionary Gamemode Goals.

### Generally available items

**Headbands**
- Headband is a headwear item that can be created by using a sharp object on a bandana. (Crafting method may be changed if dyeing clothes is implemented).
- This is a fashion accessory accessible to all crew, however when worn by a Revolutionary their codewords deal 1.5x more LHP damage.

**Revolutionary posters**
- Crew can print rolled posters from autolathes using cloth. This feature is available regardless of roundtype.
- These posters are the same posters that spawn on stations roundstart. 
- Posters are randomized when printed, and can result in loyal, neutral or revolutionary posters. Examining a rolled poster gives its name and allegiance.
- Revolutionary posters have a **4** tile radius of influence when put up (requires line of sight).
  - When inside this radius, you take **0.25** LHP damage / second (to a max of **4** stacks).
  - When inside this radius, codewords deal **1.25**x more damage (does not stack with itself).
- Loyal posters also have a **4** tile radius of influence when put up (requires line of sight).
  - When inside this radius, you heal **0.25** LHP damage / second (to a max of **4** stacks).
  - When inside this radius, codewords deal **0.5**x damage (does not stack with itself).
- Posters can be taken down, and if recycled gives back some cloth.
- Destroying a poster that is rolled up on a wall heals **5** LHP if it's a Revolutionary poster, or deals **10** LHP if it's a Loyal poster.

### Dead Drop Duffelbag / The Revolutionaries Uplink 

The Dead Drop Duffelbag (DDD) is one of the few mechanics that make Headrevs unique and why they distinguish themselves as a great asset in the revolution. The DDD acts similar to an Uplink; a discrete and concealable way to retrieve unique items that can aid you in your antag activities. What makes the DDD unique is the selection of items, availability of items and how it is retrieved and activated. 

The DDD is a duffelbag provided by an unknown sponsor of the Revolution, bluespaced into the station via the station's disposals system to provide items critical to your success:
- The DDD can be retrieved by a Headrev by "Rummaging" through an anchored disposals bin. This is a verb only available to Headrevs, selected by rightclicking any intact anchored disposals bin.
- Interacting with a DDD opens up a Revolutionary-specific store UI.
- Each DDD is tied to the Headrev that spawned it, and items acquired through the DDD are tracked on that Headrev.
- Putting the DDD back into a disposals bin, regardless of who does it, immediately despawns the DDD.
- A Headrev can not rummage for a new DDD if they already have one active on the map. 

The items in the DDD are available in three different tiers. A Headrev is able to select **1** item per tier with the Tier 1 items available from the start, with the Tier 2 and Tier 3 items locked until certain criteria are met. This criteria is the percentage of crew on the station that are converted. The DDD shows this percentage in its UI.

- Tier 1: Always available.
- Tier 2: **20**% conversion.
- Tier 3: **45**% conversion.

These percentages *could* be made lower for a solo mid-round Revolutionary, or they could be granted extra items on the same tier, if this would result in better balance.

### Dead Drop Items

This list is not exhaustive and more items could be added in the future, and some items listed may end up not working in actual gameplay and will have to be removed. Because of this they might be a bit wacky, playtesting is paramount.

#### Tier 1
Tier 1 items should be designed to help the revolution grow in a stealthy way or give them a temporary bump in effectiveness, in ways that don't involve combat.
- The Original: A **2**-use flash that deals massive conversion damage and can convert.
- Revolutionary Poster Blueprint: Allows producing rev posters directly, for a cheaper cost.
- Expanded Reading: Unlocks **4** revolutionary codewords in each category.
- How 2 Hug: After reading this book, hugging someone deals **10** LHP damage at a **10** second cooldown.
- Revolutionary Stamp: Any document stamped with this stamp deals **40** LHP when read and can convert. The stamp is not visible on the overworld sprite.

#### Tier 2:
Tier 2 items should allow the revolution to blossom; these should have conditional usecases, meaning a headrev selects the one that is most suitable for how the revolution has developed.
- Marximov: A Revolutionary-aligned AI lawboard. Must still be installed in the AI law upload.
- Cargommunism Pad: QM's Cargo Pad, but doesn't announce or log the purchases. 
- Cyanide Implanter: A reusable implanter. When used, unlocks the ability to kill oneself with 200 poison, dealing **80** CHP damage in a **5** tile radius around the user. Can not convert convertable crew.
- De-Friedman-rillator: An Revolution-marked defibrillator. Someone brought to life with this defibrillator is automatically converted.
- Headset Override: An item that, when used on a headset, adds the revolutionary comms channel. If you are not a Revolutionary, any message is on this channel is heard as static. 

#### Tier 3: 
Tier 3 items is the revolution's capstone ability; if the revolution reaches this stage the item should provide an option for the revs to go loud, or a way to comeback against a crew that is trying to fight back
- Megaphone: Reduces the codeword cooldown to **5** seconds when held. Can also play midi files.
- Mind swap: Allows you to change minds with a fellow revolutionary; a trusted scapegoat.
- Revolutionary Leader Cap: Codeword damage spoken when wearing the cap is not split; full damage is dealt to all who hear it. Only Headrevs benefit from this effect.
- Distress Beacon: Spawns a Revolutionary-aligned shuttle with **3** Revolutionary ghost roles and some supplies to combat Command.

## Possible Expansions

- Revolutions could be flavored after certain corporations with appropriate codewords (Syndicate converting the station or DonkCo. doing a corporate takeover).
- More items could be implemented for more Revolutionary playstyles.
- Certain events could trigger based on conversion thresholds; e.g. ERT if station reaches 80% conversion.
- Revs could be given objectives that, if successful, deals special map-wide LHP damage that is difficult to heal back up.
