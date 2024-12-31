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

I additionally propose that we treat "brigmedicloosing" as similar to "wardenloosing." The brigmedic _should_ always be in the brig, as their title says they should; they are not secmedics. Command should be encouraged to demote brigmedics who abandon their role by leaving the brig. The sole exception to this should be when the brigmedic is instead fufilling the role of a combat medic, in which case they should be in the backlines of sec providing first aid until the officers are well enough to be brought back to the frontlines or a paramedic can retrieve them to bring to medical. We should heavily discourage brigmedics from engaging in combat except as a last resort - they should be filling the same role as a Nuclear Agent does in NukeOps for their team in the combat phase.

Outside of the emergency scenario, the brigmedic's primary role would be patching up injured members of security or prisoners when they are within the brig. Some maps already have a dedicated brigmedic area to perform this duty in. As pointed out in PR discussions, prisoners do get hurt, secuirty officers can also get hurt in the process, and an injured officer bringing a prisoner and themselves to medbay creates risk of the officer critting before arrival. The brigmedic removes that risk.

The brigmedic should have an extra responsibilty that normal medics do not get: ensuring the medical wellbeing of prisoners in the event of abusive or negligent security. This creates a roleplay oppourtunity akin to the lawyer fighting for the legal rights of the crew. When a bad secuirty officer wants to harm a prisoner, the brigmedic can be there to advocate for the physical and psycological safety of the prisoner (or at least repair the damage quickly if the officer does it anyways).

> ### We're not readding the free hardsuit role.

The brigmedic's hardsuit should be stored with the security hardsuits. Through door access controls, the brigmedic would therefore only have access to their hardsuit duing the emergency scenario, when sec lets them get the hardsuit to provide medical aid in combat. The locker containing the hardsuit should have brigmedic access to prevent a cadet from accidentally taking the hardsuit dedicated for medical use.
