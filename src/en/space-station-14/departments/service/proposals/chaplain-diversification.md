# Chaplain Diversification
AKA. The Quran update

| Designers | Implemented | GitHub Links |
|---|---|---|
| Terraspark4941 | ⚠️ Partially | [#27400](https://github.com/space-wizards/space-station-14/pull/27400) [Sprite] |

## Overview

Adds a backbone for intergrating new varients of the bible via radial menus (like in TG station) and a new item; jacketed religious books. 

Every instance of the bible in-game should be replaced by these jacketed books (with potential exception for loadouts) to allow for chaplains to "unwrap" their book of choice.

To implement this, a new religious book, the Clear Quran, will be implemented with a different AoE healing mechanic to boot.

## Okay, but why?

In TG/station13, chaplains are much more developed than they are in SS14, with sects, different books/philosophies and **the null rod**; this feature request aims to amend atleast one of those features to SS14.

It's pretty clear that this community aims to make SS14 as accessible as possible; locking chaplains to preach just christianity (by default) is both anti-accessible and biased, as a whole.

With the (somewhat) recent addition of radial menus AND our superior engine, we can finally port different religious books AND slap new mechanics on top of it, too!

### No, but why AoE healing?

As muslims, we are generally refrained from applying our book to the foreheads of others for "spiritual healing"; this undermines the respect given to our book and the bodies of other people.
The Clear Quran does state that such healing can still be administered via *recitation*, which is where the AoE aspect aries from. 

Instead of whacking someone with the Quran, chaplains will instead recite from the Quran, applying a weaker healing to all nearby humanoids who can hear them (think within audible distance and not deaf [WYCI]).

## Implementation

As previously stated, every instance of the bible to-date will be replaced by the jacketed religious book; the first time a chaplain interacts with this book, they can pick whether they want to select a recitaional skin (with an AoE of healing *on use*) or a non-recitational skin (see: current bibles).

After selecting their mechanic of choice via the first radial menu, they can choose skins as they prefer (I'd still prefer the Quran be locked to recitational skins only, but not so with bibles and non-recitational skins!), also via nested radial menu.

A new sprite for the Clear Quran has already been developed and should be present at [Resources/Textures/Objects/Specific/Chapel/quran.rsi](https://github.com/space-wizards/space-station-14/tree/master/Resources/Textures/Objects/Specific/Chapel/quran.rsi), implemented by the linked PR [#27400](https://github.com/space-wizards/space-station-14/pull/27400).
