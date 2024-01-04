# Automated Evac & Crew Transfers [moony, unapproved]
A common problem within SS13 at the moment is the "evacuate the minute there's a problem" mentality. This comes from two places:
 1. Evacuating is often easier than actually fixing the problem.
 2. Fixing the problem is tedious (and sometimes impossible, say power's out and there's no engine at all.)

This document is primarily focused on point #1, but point #2 needs to be addressed for this to have any weight.

# Crew Transfers
SS14 is capable of loading multiple stations simultaneously, and only takes a few seconds to load even the largest maps. It is possible to leverage this: Transferring the crew from the old map to a new one to extend playtime.
From some testing (running crew transfers manually in-game) this has a tendancy to tack another hour onto the round's total length without much ire from players (as they retained control over evacuation for the duration of the round.)
## Problems with this approach
- Extending the round length reduces play opportunities, as people have to wait longer to play again after death.
    - This could potentially be solved by allowing a respawn after the next crew transfer (with an enforced 30 min wait period). Could easily explain this away as offsite cloning.
- This conceptually only works for mid-high pop.
    - Likely needs a minimum player count for transfers to occur.
- To avoid grief and round-ending incidents, the crew transfer shuttle needs to be decently large. During testing, Atlas (a *station*) was used for this purpose, which is nigh impossible to implement autopilot for.
    - One could shrimply implement autopilot anyways (Extremely technically complex)
    - Have people engage in self-transfer to the vessel via smaller, cargo-shuttle sized vessels (likely would only work on MRP and higher.)
