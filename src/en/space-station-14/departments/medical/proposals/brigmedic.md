# Fixing Brigmedic

| Designers                                                                                                   | Implemented | GitHub Links |
| ----------------------------------------------------------------------------------------------------------- | ----------- | ------------ |
| [minus1over12](https://github.com/minus1over12) ([WarPigeon](https://forum.spacestation14.com/u/warpigeon)) | :x: No      | TBD          |

## History of the role

_[Apr 3, 2023](https://github.com/space-wizards/space-station-14/pull/15115)_: a PR is proposed adding in a brigmedic hardsuit. Three points were given to justify adding the hardsuit:

> 1. This will improve the experience of playing on the brig medic, because now you don't have to be the main link of the epidemic.
> 2. This will diversify the gameplay of the security service, and people who prefer medicine rather than beating clowns will be motivated to become a guardian angel of the brig. In a word, popularizes the role of the brig medic.
> 3. It turns out that we are improving the antagonists, improving, and the security service continues to stagnate, the most significant improvement of this department was at the moment of adding wardens hardsuit, after that there was a lull.

The proposed PR was closed after discussion determined that the hardsuit should only be added if it is for a new role dedicated to the task.

_[Apr 11, 2023](https://github.com/space-wizards/space-station-14/pull/15319):_ a new PR is proposed, expanding to create a new role for use with the hardsuit. The new role is merged the same day.

_Apr 11, 2023 - Apr 16, 2023:_ Brigmedic was mapped onto Bagel, Origin, and Box.

_[Apr 15, 2023](https://github.com/space-wizards/space-station-14/pull/15426):_ Brigmedic recieves a nerf, removing their hypospray (hyposprays are currently exclusive to the CMO, Nukie Agent, and CentComm roles).

_[Apr 26, 2023](https://github.com/space-wizards/space-station-14/pull/15496):_ An update for brigmedic is merged in, adding in further entities made exclusively for the brigmedic.

_[May 4, 2023](https://github.com/space-wizards/space-station-14/pull/16069):_ Brigmedic is removed from the game, citing complaints from Discord as the reason.

_[May 4, 2023](https://github.com/space-wizards/space-station-14/pull/16082):_ Brigmedic removal is partially reverted to keep the uniform around.

_[May 6, 2023](https://github.com/space-wizards/space-station-14/pull/16196):_ A PR to revert the brigmedic removal is proposed, citing the majority reactions against the removal. The request is rejected, giving the following reason:

> […] we're not readding the free hardsuit role. The game already has one of those (Paramedic) and it already causes issues. This is the same role except with security access to boot with none of the responsibilities of a medic, and it's primary use seemed to be security with a hardsuit, not an actual medic.

> In other words: Gimmie a well reasoned, thought out design doc for this role, what it should do, what it should not do and how it makes sure those things don't happen, and how it should influence the round, and I'll let you readd it.

This proposal aims to accomplish the goals as requested:

- What brigmedics should do
- What brigmedics should not do
- How does the game make sure those things don't happen
- How brigmedics should influence the round.

Some thoughts on how to go about fixing the issues are also provided in the PR's thread, which will will be incorporated into this proposal.

_[Jun 4, 2023](https://github.com/space-wizards/space-station-14/pull/17037):_ The removal is partially reverted again, bringing back the starting gear loadout for admin use.

## Fixing the problems

> ### This is the same role except with security access to boot with none of the responsibilities of a medic, and it's primary use seemed to be security with a hardsuit, not an actual medic.

We should start off by changing the mindset of brigmedic to focus more on medic instead of brig; it should be brig**medic**, not **brig**medic. Brigmedic should be removed from the security department, and be considered a member of the medical department instead. The brigmedic would still have access to the brig and security channels, similar to the civillian department's lawyer, but just like the lawyer is not a true part of security (i.e., they should not have lethals or cuffs outside of emergencies).

I additionally propose that we treat "brigmedicloosing" as similar to "wardenloosing." The brigmedic _should_ always be in the brig, as their title says they should; they are not secmedics. Command should be encouraged to demote brigmedics who abandon their role by leaving the brig. The brigmedic's primary role would be patching up injured members of security or prisoners when they are within the brig. Some maps already have a dedicated brigmedic area to perform this duty in. As pointed out in PR discussions, prisoners do get hurt, security officers can also get hurt in the process, and an injured officer bringing a prisoner and themselves to medbay creates risk of the officer critting before arrival. The brigmedic removes that risk.

The sole exception to this should be when the brigmedic is instead fufilling the role of a combat medic, in which case they should be in the backlines of sec providing first aid until the officers are well enough to be brought back to the frontlines or a paramedic can retrieve them to bring to medical. We should heavily discourage brigmedics from engaging in combat except as a last resort - they should be filling the same role as a Nuclear Agent does in NukeOps for their team in the combat phase.

The brigmedic should have an extra responsibilty that normal medics do not get: ensuring the medical wellbeing of prisoners in the event of abusive or negligent security. This creates a roleplay oppourtunity akin to the lawyer fighting for the legal rights of the crew. When a bad security officer wants to harm a prisoner, the brigmedic can be there to advocate for the physical and psycological safety of the prisoner (or at least repair the damage quickly if the officer does it anyways).

> ### We're not readding the free hardsuit role.

The brigmedic's hardsuit should be stored with the security hardsuits. Through door access controls, the brigmedic would therefore only have access to their hardsuit duing the emergency scenario, when sec lets them get the hardsuit to provide medical aid in combat. The locker containing the hardsuit should have brigmedic access to prevent a cadet from accidentally taking the hardsuit dedicated for medical use.

## Implementation

### Gear

The brigmedic, while heavily focused on working with the security department, is a member of the medical department. As such, they will not be permitted to carry security gear. Any gear they do need that should not be generally available will be marked as restricted to medical or security and medical.

#### Roundstart gear:

- Brigmedic PDA with Brigmedic ID card
  - The PDA should be functionally equivalent to a medical doctor's PDA.
  - The ID should have the following accesses:
    - Brig
    - Brigmedic
    - Maintenance
    - ~~Medical~~ (needs further discussion)
    - ~~External~~ (present in original implementation, needs discussion)
- Brigmedic jumpsuit or jumpskirt
- Brigmedic coat (optional)
- Brigmedic backpack, duffelbag, or satchel
  - Exact contents TBD
  - Should be enough to not need to commit theft from medbay, but still require coordination with them.
  - Absolutely no security only restricted gear.
- Medical HUD
- Brigmedic beret (optional)
- Brigmedic headset
  - The headset will have both security and medical access. The medical access is primarily useful for coordinating with chemistry and the rest of medical on distribution of supplies within the department.
- Brigmedic mask
- Implanted mindshield
  - This also implies that the brigmedic should be antag immune.
- Medical belt
  - It is only capable of holding medical gear, not security gear.

#### Emergency gear:

The brigmedic has a hardsuit for emergency use. It is stored with the security hardsuits, which the brigmedic would not have general access to due to them being in a security access controlled area. In the event of an emergency, an officer can let them in to retrieve the hardsuit. From an environmental hazard perspective, the brigmedic hardsuit should be equivalent to a standard security hardsuit. From a combat perspective, the hardsuit should only be good enough to stop a few lucky bullets; it must not be robust enough to make having it an advantage in frontline combat.

### Brig Infirmary

The brig's infirmary is the workplace of the brigmedic. It should be equipped with at minimum a medvend (or a brigmedic equivalent), a medical bed, medkits relevant to combat damage, a brigmedic locker, and a morgue. It should be noted that medvends require medical access to operate. The brigmedic is expected to always be available at the infirmary, or at least somewhere within the brig where they can easily get to the infirmary as needed.

### Role Requirements

The original implementation had two requirements:

- 5 hours medical
- 2 hours security

The new implementation would substitute the security time with at least 2 hours of warden time, to make sure the player understands the concept of staying in the brig with an already well established role.

## Roleplay Responsibilities

### General case

At the surface, the brigmedic is similar to a doctor you would find at medbay. They treat the wounded from the brig, whether that be prisoners after a fight in perma, a sec officer wounded from apprehending a syndicate agent, or the lawyer needing a quick bandage from a papercut.

In addition to responding to injuries, they also have a role in advocating for the physical (and potentially psychological) wellbeing of prisoners. They should make sure that the warden or other members of security allow for prisoners to be treated if they have injuries, that the dietary needs of prisoners are being met, and that prisoners are given help in recovering when a security officer ends up beating up a prisoner for some reason.

The brigmedic manages the medical supplies allocated to security, and needs to ensure that security has the stock it needs while not draining the rest of medical of critical resources. The CMO is tasked with ensuring resource distribution is optimal between the medical subdepartments.

### Red Alert combat medic case

In the event of a severe threat to the station that requires combat, the brigmedic becomes the combat medic for the security department. Their job is to remain behind security, patching up the wounded so they can return to combat sooner. The brigmedic may be given access to an exclusive hardsuit by the security department if there is a credible risk of pressure loss (such as a space dragon or china lake being in play).
