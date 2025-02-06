# Crawling

| Designers | Implemented | GitHub Links |
|---|---|---|
| plykiya | :x: No | TBD |

## Overview

Introduces the ability to intentionally lay down, and the crawling movement option while laying down. This introduces a less punishing option between standing up and being stunned/knocked down.

## Background

GitHub issue by @keronshb: https://github.com/space-wizards/space-station-14/issues/34894
Pre-doc Crawling PR by @Ratyyy: https://github.com/space-wizards/space-station-14/pull/30759

Crawling is a mechanic in Space Station 13 that has yet to be ported to Space Station 14's upstream fork. While the idea of crawling being implemented is a popular opinion, and has even been implemented on several forks, the upstream maintainers would like a clear and obvious visual indication that someone is crawling as opposed to being dead or being stunned on the ground. This was done in a few ways in Space Station 13, such as having the character's rotation while crawling looking different compared to being knocked down, or by darkening the character's sprite when stunned.

## Features to be added

The act of crawling is fairly self-explanatory, but for implementation features:

- Crawling should be slower than both walking and running.
- Crawling enables additional movement capabilities such as crawling under plastic flaps, but not under tables.
- Crawling should make you immune to slippables, such as space lube or soap.
- Crawling should cause bullets to pass by you unless you are directly targetted. **(TBD: Does this apply to melee wideswings?)**
- **(TBD: You shouldn't be able to crawl in zero gravity? or maybe you can, just at no dodging benefit?)**
- There should be a hotkey and a HUD action to go between standing or crawling, and vice versa. **(TBD: Actual hotkey/term on the UI. The SS13 hotkey uses EQUALS, and the indicator says STAND/REST. Sometimes you have to double-click the indicator to stand or lay down)**
- It should be an additional state in between standing up and being knocked down.
- Receiving enough stamina damage should force you to crawl while being stamcrit will fully knock you down. **(TBD: does being knocked down transition to crawling or standing?)**
- If you are forcefully put into the crawling state your character should automatically stand after a period of time.
- Shoving yourself empty-handed in harm mode should allow you to go from crawling to standing at the cost of stamina. This can be used to stand up faster if you were forced into a crawling state and want to get up faster.
- Crawling should look distinct from being knocked down by a stamcrit or shock.
  - My proposal is that crawling should only be possible if your character is facedown, since your arms have to be below you to move, as that's literally how crawling is carried out. This means that your character should be able to rotate both clockwise and counterclockwise when falling over as opposed to how it currently is where your sprite ALWAYS rotates counterclockwise. **(TBD: I don't think using the forward-facing/back-facing sprites for crawling is a good idea if we want to increase the amount of visual differences between knock downs and crawling. It doesn't look that bad for Morty, Slimes, Cleanbots, Goats, Honkbots, etc. so I think it'll be fine. In a perfect world we'd have new sprites or animations for crawling, but that's not going to happen.)**
  - Being hit by lethal damage flashes your character red. Being hit by stamina damage flashes your character blue. By this logic, being fully stamcritted can be another fully visual indicator without ruining immersiveness. The implementation for a visual stamcrit effect should look like **(TBD: should we darken the character, as if they were no longer active, like in SS13 Citadel? surround the player sprite on the left and right with zig zag lines and have them shake a little bit like pushing is done on RMC14?? needs to be decided)**

## Game Design Rationale

Allowing players to crawl gives them increased options for how to approach situations, such as crawling when in a combat zone to avoid stray fire, or by allowing them to maneuver slippery environments albeit at a downside. It equally enables everyone and gives a player additional options to approach situations they find themselves in.

## Roundflow & Player interaction

Crawling will be something that a player engages with every shift. It's a movement option as common as the act of walking or running, so it applies to every scenario that movement can occur in such as combat or RP. Everything related to crawling will be mechanically enforced onto the player by its implementation, such as the things that crawling enables and when the player is forced to crawl.

## Administrative & Server Rule Impact (if applicable)

People can abuse crawling to get through plastic flaps, so it could increase the amount of department break-ins, such as at Cargo or Science in some stations. I don't foresee any other administration issues that would occur besides that.
