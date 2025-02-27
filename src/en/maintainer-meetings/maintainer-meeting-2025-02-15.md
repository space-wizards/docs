# Maintainer Meeting (15 February 2025)

**Time:** 15 February 2025

```admonish info
**Attendees:**
- Myra (Vasilis)
- Errant
- Simyon
- Julian
- Pancake
- ElectroSR
- Aeshus
- Milon
- Boaz
- Slartibartfast
```

This meeting was recorded:

{% embed youtube id="31mCKgzHDK4" loading="lazy" %}


## New maintainer welcome
Hi Milon
![](https://hedgedoc.spacestation14.com/uploads/4e5c13e3-d383-4959-8b0a-23b56122d1b5.png)

## Looking into crawling and antag balance (ScarKyo)
We dont have enough info to talk about this, moving it to the next meeting.

## AI, we still have like 3 open design docs (Errant)
- Did anyone read them?
    - No one read them next maitnainer meeting please for the love of god read them.
    - Also we have 4 now.

## PR Template (Errant)
Errant is not done putting everything in one nice doc so we can all agree on something so NEXT MEETING WOW THESE ARE GOING FAST

## [Should SpriteComponent be moved back to shared](https://discord.com/channels/310555209753690112/1339695192579637298/1339794508711202826) (Electro)
- There are useful stuff you could do by having the server be able to send clients the sprites to render
- Why was it taken out of shared?
    - Cause of networking and dirtying
    - Sending unnecessary data
    - (Check with PJB)
- There should be more discussion later on with people who know a bit more about sprite code.

## Vulture, and it's test server status (Aeshus)
Is good
:3

## April fools branch (Emisse)
Sure I suppose. After this stable releases.

## Game area Design doc
https://forum.spacestation14.com/t/game-area-design-documents/17317
Slam made it public
so uh yeah i suppose you can write about it now.

## Stable review
- [34591](https://github.com/space-wizards/space-station-14/pull/34591) Void's Applause
- [34785](https://github.com/space-wizards/space-station-14/pull/34785) Removed MoMMI from AI name list
- [34764](https://github.com/space-wizards/space-station-14/pull/34764) Tweak pill eat delays
- [34774](https://github.com/space-wizards/space-station-14/pull/34774) Update shutter sounds
- [34794](https://github.com/space-wizards/space-station-14/pull/34794) Rename shields
- [34841](https://github.com/space-wizards/space-station-14/pull/34841) Security Shield Naming Structure Inconsistency Change
- [32821](https://github.com/space-wizards/space-station-14/pull/32821) Replacing protein with razorium in flesh kudzu
- [34458](https://github.com/space-wizards/space-station-14/pull/34458) Separates frost oil into coldsauce and frost oil
- [33619](https://github.com/space-wizards/space-station-14/pull/33619) Randomized maints rooms
- [33239](https://github.com/space-wizards/space-station-14/pull/33239) Add Reagent gold and silver solification with frost oil
- [34819](https://github.com/space-wizards/space-station-14/pull/34819) Reworded the "SAY HEY LISTEN" silicon law
- [34531](https://github.com/space-wizards/space-station-14/pull/34531) Wizard Touch Spells (Smite, Cluwne's Curse, Slippery Slope)
- [34824](https://github.com/space-wizards/space-station-14/pull/34824) [Admin] Omni Accent Smite
- [32414](https://github.com/space-wizards/space-station-14/pull/32414) DSword Replacement - the Hypereutactic Blade
- [34687](https://github.com/space-wizards/space-station-14/pull/34687) Add binoculars
- [33607](https://github.com/space-wizards/space-station-14/pull/33607) Add clientside personal pointlight for observers
- [34843](https://github.com/space-wizards/space-station-14/pull/34843) Expand variety of strange pills
- [34277](https://github.com/space-wizards/space-station-14/pull/34277) Changed utensil sprites to appear smaller.
- [34619](https://github.com/space-wizards/space-station-14/pull/34619) Remove instant cryobed insertion
- [34675](https://github.com/space-wizards/space-station-14/pull/34675) Reduce NukeOps Reinforcement price from 35TC to 30TC
    - See how it goes and perhaps reduce the price by 5 more tc
- [33572](https://github.com/space-wizards/space-station-14/pull/33572) Elf Ears
    - 5 different types of elf ears that only differ by a few pixels is bloat, I would reduce it to maybe two variants (Slartibartfast)
        - It is fine for now but we should consider it in the future.
- [34890](https://github.com/space-wizards/space-station-14/pull/34890) Sec Balance Part 1: Buffs Disabler and Disabler SMG
- [34561](https://github.com/space-wizards/space-station-14/pull/34561) Added Genderqueer pin! (Properly this time.)
    - We should turn all the pins into a single chameleon pin so that the loadout and vending machine are less bloated (Slartibartfast)
        - I don't think they should be chaneleon. The bloat issue is mainly an issue in the loadout menu, and there the answer is to allow better item categorization. Collapsible groups in the loadout menu perhaps? (Slam)
            - This is being worked on now already by Milon
- [34904](https://github.com/space-wizards/space-station-14/pull/34904) Swapped butter w/ olive oil for making spaghetti
    - If the italian players come after us revert it
        - Simyon Italin friend says: I think they approve this. 
    - Real answer allow both
    - April fools idea: To make spaggeti you have to cut it in half.
- [34927](https://github.com/space-wizards/space-station-14/pull/34927) Buff the Combat Bakery Kit uplink item
- [33095](https://github.com/space-wizards/space-station-14/pull/33095) move lathe recipes into packs (easier for forks and maintaining)
    - Was a technical refactor but sneaked in some major balance changes by adding stun batons, disablers and disabler SMGs to the emagged lathes. These were previously excluded on purpose, since they are way too overpowered if you get them with an emag, especially now that it only costs 4TC. The batons have already been removed in 35014 again, but we should do the same with the disablers before release since we just buffed them to make sec stronger against antags. A disabler alone would be worth the 4TC for the emag. (Slartibartfast)
    - Baton was removed but not disablers
        - Remove the disablers
- [35014](https://github.com/space-wizards/space-station-14/pull/35014) Remove batong etc from emagged autolathe
- [34857](https://github.com/space-wizards/space-station-14/pull/34857) Paper door
- [34930](https://github.com/space-wizards/space-station-14/pull/34930) Drozd Colors for Kammerer
- [34932](https://github.com/space-wizards/space-station-14/pull/34932) Wizard shuttle preperation
- [34411](https://github.com/space-wizards/space-station-14/pull/34411) Wizard Item Recall Spell
    - The item itself should hopefully have a popup itself so that it does not appear like a bug/suddenly got deleted.
- [34977](https://github.com/space-wizards/space-station-14/pull/34977) add straight ally pin
    - We should turn all the pins into a single chameleon pin so that the loadout and vending machine are less bloated (Slartibartfast)
        - I don't think they should be chaneleon. The bloat issue is mainly an issue in the loadout menu, and there the answer is to allow better item categorization. Collapsible groups in the loadout menu perhaps? (Slam)
- [34450](https://github.com/space-wizards/space-station-14/pull/34450) allow paper labels on seeds
- [34974](https://github.com/space-wizards/space-station-14/pull/34974) Lecter + Magazine Resprite
- [34950](https://github.com/space-wizards/space-station-14/pull/34950) long bacon scarf
- [34996](https://github.com/space-wizards/space-station-14/pull/34996) Removes Cog station
- [34988](https://github.com/space-wizards/space-station-14/pull/34988) Relic station
- [31060](https://github.com/space-wizards/space-station-14/pull/31060) Allows pacifists to throw Items with DamageOnLand
- [34886](https://github.com/space-wizards/space-station-14/pull/34886) Wooden Grip for Antique Laser Pistol
- [35046](https://github.com/space-wizards/space-station-14/pull/35046) Display radio frequencies with a decimal place
    - Frequencies dont currently have a use so its mostly flavor rn, fixing it will require chat refactor.
- [34421](https://github.com/space-wizards/space-station-14/pull/34421) Grenade resprites part 1, stinger sound change, projectile grenade animation fix
- [35025](https://github.com/space-wizards/space-station-14/pull/35025) Sentry turrets - Part 1: Art assets
    - Emisse said it could use adjustments but can be merged for now
- [35059](https://github.com/space-wizards/space-station-14/pull/35059) Put screwdrivers in the vendomat
- [33306](https://github.com/space-wizards/space-station-14/pull/33306) buff python
- [34541](https://github.com/space-wizards/space-station-14/pull/34541) Increase the price of bulletproof armor.
- [32250](https://github.com/space-wizards/space-station-14/pull/32250) Move contraband text to a separate examine tab
    - Errant prefers that instead of a button this was an icon that changed with the legality of the item. This pr moves us closer to this.
- [31303](https://github.com/space-wizards/space-station-14/pull/31303) Add loadout names
    - Please for the love of god fill out the PR templete
    - What does this do?
        - Ok it adds a custom name for the AI on the character customization screen.
- [35063](https://github.com/space-wizards/space-station-14/pull/35063) give CE atmos gas mask
- [34209](https://github.com/space-wizards/space-station-14/pull/34209) Make Advanced Spray more tolerable to use
- [34991](https://github.com/space-wizards/space-station-14/pull/34991) Add new freezer atmos devices and fix freezer fixgridatmos marker
- [33110](https://github.com/space-wizards/space-station-14/pull/33110) RoomSpawner mask
- [34649](https://github.com/space-wizards/space-station-14/pull/34649) Wizard Staff of Animation
    - Critical station infra should not be able to be animated
        - Has a blacklist already
- [33554](https://github.com/space-wizards/space-station-14/pull/33554) Slime plushie now squishes
    - The slime squish sound was mentioned as problematic for players with misophonia before and can easily be spammed with a plushie. But I guess you can already do so with emotes
        - Misophonia options/related should be an accesibility option already. Valid consern.
        - Someone could make an alternate version. Bring it up in #accesibility
- [33807](https://github.com/space-wizards/space-station-14/pull/33807) Grilled Cheese Sandwich Entity and Recipe
- [34792](https://github.com/space-wizards/space-station-14/pull/34792) Make experimental welding tool less harmful to eyes
- [34657](https://github.com/space-wizards/space-station-14/pull/34657) Paramedic Void Suit update

### Stuff that is broken
- Nukie loadouts are completely broken and possibly yaml inheritance in general, caused by [RT5612](https://github.com/space-wizards/RobustToolbox/pull/5612)
    - Fixed
- The [chameleon clothing menu](https://github.com/space-wizards/space-station-14/issues/35077) 
    - Fix pr https://github.com/space-wizards/RobustToolbox/pull/5649
        - Eletro said they would review this tommorow
        - So yes delay it
- Possibly other UIs? Some have been fixed already
    - Addressed