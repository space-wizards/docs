# K9 Unit Job

## Design Goal

The Goal of adding the K9 unit to add core gameplay loop variety to the security department. Currently, 3 of the roles are nearly identical (Cadet, Secoff, Det)
with only Det having a minor variation in loadout and some added utility for forensics. All three focus on patroling, detaining, and generally dealing with antagonists with Warden and HOS being the exceptions. A K9 unit would add great variety for sec players while also opening many roleplay opprotunities with a low MVP cost (as dogs and their behaviors already exist in code at least in part). The Main goal for the person playing the K9 is to give a security role where they are not expected to verbally interact with crew, which can be draining, irritating, demoralizing, etc. This gives security a way for players who need a break from the negative human interaction side of the department a way to continue playing there, while also giving new tools to combat the most destructive tools available to antags which currently have very few counters.

## K9 Officer Role

The K9 units are something most people are familiar with in real life, and their role will mirror that public perception. This includes sniffing for explosives (bombs, c4, etc)  No more than one (1) K9 officer slot should be made available on all stations, alternative this could be a good ghost role, fitting in with other animal ghost roles as a familiar. K9 Unit will spawn at the normal security officer spawn location and be equipped with a few canine specific items (detailed later). K9 Officers will be mechanically incentivized to accompany security officer, as they will cover gaps in each others abilities to keep the station safe, they would be as follows (and are detailed in their own section later on):

#### Pros / Abilities

* Speed: Faster base speed to chase down fleeing suspects / criminals.
* Scent: Ability to smell explosives or illicit chemicals on people within a range - useful for creating engaging difficulty for antags who risk being detected if they get too close.
* Bite: short fading slow on those bit to aide officers in pursuits in addition to damage.
* Signal: Whistle-like callout / bark to notify handler of contraband.

#### Cons

* Unable to talk or use radio(dog speech)
* Unable to detain or arrest (only bite)
* Slightly lower health / armor than humans


### Ability breakdown

#### Speed

The primary enabler of the K9 during normal operations is increased speed. Operating at somewhere between 110% and 130% normal character movement speed allows for easier pursuits than secoffs and for talented players to kite during melee or jink during firefights. This number is a rough first guess at an appropriate speed value, they should be able to catch any undrugged human but still struggle to keep up with those under the influence of hyerzine or similar super stimulants.

#### Scent

The main unique mechanic that K9 officers will have. This takes the form of a overlay 'cloud' or hue on characters who are carrying explosives. This can manifest in two ways, depending on maintainer feedback:

1) Denoted using an new security hud icon that is only visible to K9 units to match existing styles. This modifier will only be visible on characters in a short range of the K9 to prevent cross-screen snipes on players who are out of scent range and as a balancing mechanic.
2) The K9 unit must use a short 1 second 'sniff' action on a player and get a text message popup similar to that recieved when somebody is placing an entity into a players hands that tells the K9 if they picked up any foreign scent, including chemicals, reagents, or foods. "You smell explosives on this person!" / "you smell <chemical scent> on this person" / "you smell <food taste or scent>.
3) Scent mechanic is too powerful all together and is not implemented.

#### Bite

Unlike most bites from other creatures, this would inflict a small (0.25 - 0.5) second slow on targets, this would combo with their speed to give them more versatility in aiding security staff, further aiding their support toolkit.
Additionally, this bite would be stronger when wearing a k9 hardsuit (detailed in equipment section below) in exchange for lower speed and higher armor.

#### Signal

Functions identically to the security whistle, but with a barking sound effect, for alerting handler.


## Dog changes and New Items

To help make the K9 (and other K9 like animals) more versatile, some new Dog specific items and item slots will be created, outlined here

### Dog changes

Current dogs will be updated to be given support for all new appropriate items (Ian, Cerb, etc.), but doesnt need to be required for MVP.

* Dogs will now have an armor slot. The K9 unit default loadout will come with an K9 armored vest that provides similar bonuses to the standard armored vest that security gets.
* 
