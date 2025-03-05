# Contraband System
| Designers | Implemented | GitHub Links |
|---|---|---|
| Killerqu00 | :warning: Partially | https://github.com/space-wizards/space-station-14/pull/32250 https://github.com/space-wizards/space-station-14/pull/35206 and TBD |

## Overview
Contraband System is the system that defines what contraband is in-character. As of now (when I am writing this doc), it is a detailed examine showing 2 things: type of contraband (departmental-restricted, minor, major, syndicate) and whether or not the wearer ID allows the person to possess this contraband. 

## Background
Contraband system was initially added in [#28688](https://github.com/space-wizards/space-station-14/pull/28688). The main reason for this systems was to improve security work by strictly defining contraband. Shortly after, the Space Law was changed in [#30937](https://github.com/space-wizards/space-station-14/pull/30937), changing manual listing to a reference to the in-game system.
Afterwards, many small-scale PRs were made in order to adjust contraband markings. 
With the addition of magical contraband in [#35254](https://github.com/space-wizards/space-station-14/pull/35254), addition of job-specific contraband in [#33385](https://github.com/space-wizards/space-station-14/pull/33385) and changes to contraband examine in [#32250](https://github.com/space-wizards/space-station-14/pull/32250), several discussions took place about the desired behavior of the system.

## Technical info
Contraband System relies on ContrabandComponent in order to store all information about contraband status.
To simplify prototyping, abstract prototypes have been created for base contraband types, for example:
```yaml
- type: entity
  id: BaseSecurityBartenderContraband
  parent: BaseRestrictedContraband
  abstract: true
  components:
  - type: Contraband
    allowedDepartments: [ Security ]
    allowedJobs: [ Bartender ]

- type: entity
  id: BaseMajorContraband
  abstract: true
  components:
  - type: Contraband
    severity: Major
```
Severity here refers to the ContrabandSeverityPrototype, which can be defined like this:
```yaml
- type: contrabandSeverity
  id: Minor
  examineText: contraband-examine-text-Minor
```
In order to designate an object as contraband, assign one of the base contraband types as a parent. Here's an example with the security HUD: BaseSecurityContraband as a parent automatically adds the contraband designation.
```yaml
- type: entity
  parent: [ClothingEyesBase, ShowSecurityIcons, BaseSecurityContraband]
  id: ClothingEyesHudSecurity
  name: security hud
  description: A heads-up display that scans the humanoids in view and provides accurate data about their ID status and security records.
  components:
  - type: Sprite
    sprite: Clothing/Eyes/Hud/sec.rsi
  - type: Clothing
    sprite: Clothing/Eyes/Hud/sec.rsi
  - type: Tag
    tags:
    - HudSecurity
```
## Intended Experience
- Help security to solve conflicts like "I found it it maints, therefore it's legal" and "Not everything with syndicate mention in the name is illegal" using in-character means;
- Be an easy way to determine if using this item as security or command will be in breach of the rules;
- Help admins settle conflicts where items are being confiscated by security (lawfully or unlawfully).
## Experience To Avoid
- Starting OOC conflicts about legal status of an item;
- Uncovering stealth items;
- Blocking possibility of delegations and exceptions (like captain giving the sabre to HoS due to being a pacifist, or using syndicate contraband as a last resort against nukies).
## Needed features
- Hover detailed examine (to reduce the need for clicking);
- Detailed examine icons that relay information at a glance (not relying only on color for accessibility);
- Separation of "Grand Theft" status from ContrabandSeverity;
- Making a general "bad stuff" designation without sacrificing flavor text (right now, we have Syndicate and Magical).