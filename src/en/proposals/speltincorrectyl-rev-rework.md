# Revolution Gamemode Rework

| Designers | Implemented | GitHub Links |
|---|---|---|
| SpeltIncorrectyl | :x: No | TBD |
## Terminology
Loyalists - Sec, command and other mindshielded crew
Telecrate - A crate teleported onto the station by Centcom to help the loyalists.
Telecrate Drop - The process by which telecrates are announced and then spawned.
## Background
I enjoyed the revs gamemode to an extent, but there were always some issues.
* **The success or failure of the revolution depended very heavily on how early/late the revolution was discovered.** An incompetent headrev could flash someone with sunglasses and give away the revolution very early, giving the loyalists a swift victory.
* **Too reliant on cargo.** Loyalists needed cargo to get mindshields and materials for the secfab. Revs needed cargo to get guns. Whoever controlled cargo won the game. Cargo was also susceptible to unfun sabotage, like revs wasting the budget so the loyalists can't buy mindshields.
* **Rounds commonly stagnate.** Security turtling in sec, or heads of staff hiding, or revs just doing nothing.

I plan to fix this by adding telecrate drops, which are crates valuable to both the loyalists and the revs, yet are not necessary to win, and are spawned in at regular intervals. This spawns conflict, and stops stagnant rounds. It also lets a winning revolution track hiding heads of staff.
## Win Condition
A revolutionary major victory is killing all heads of staff.
A revolutionary minor victory is ensuring no heads of staff are evacuated to centcom.
A loyalist major victory is killing all headrevs.
A loyalist minor victory is evacuating at least one head of staff to centcom.

Upon a major victory being reached by either side the shuttle will be called.
## Announcement
**25 minutes** into the revolution,the loyalists are notified of the existence of the revolution by an announcement on the sec and command radio. Previously, upon learning of the revolution the loyalists would now attempt to control cargo. However, the rework changes this.

The shuttle can't be called for at least **30 minutes** after the announcement. This is important, since the loyalists can win by evacuating a head of staff, and would otherwise just call the shuttle immediately. If any side achieves major victory than this restriction is lifted and the shuttle is called.

If the revs are struggling to find and kill the heads of staff, they can call the shuttle themselves and then just kill all non revs onboard.
## Telecrate Drops
The loyalists now must secure a telecrate drop to get mindshields. Telecrate drops happen at regular intervals after the announcement. They follow this process:
* The spawn location is decided. It must be a room within the station.
* Security is notified of the spawn location by an announcement on security radio **5 minutes** before the telecrates arrive. This is so security can secure the area before the crates arrive.
* An central command announcement will be made, visible to all crew, detailing the location of the telecrate drop **2 minutes** before the telecrates arrive. It warns the crew not to go near the area, and says that security is authorised to use lethal force. This is so the revs can try to attack the area and take the telecrates for themselves.

A telecrate drop contains the following contents:

| Crate Name | Contents | Use for Loyalists | Use for Revs |
| ---- | ---- | ---- | ---- |
| Mindshield Crate | A substantial quantity of mindshields (15). | Used to mindshield crew. | Can be sold for a lot of money, to buy guns. |
| Amoury Resupply Crate | Ammo (.20 rifle, .35 auto, buckshot) | Used to replace ammo lost defending the teledrop. | Used to arm the revolution. |
| Emergency Triage Crate | Defibrillators<br>Advanced Meds (medicated suture and regenerative mesh) | Used to revive any revs so they can then be mindshielded. Doesn't make medbay obsolete, as the supplies are limited and no chemicals are included. | Extra medicine for healing comrades. |
| Head of Staff Tracking Crate | Two pinpointers which point to the location of two random living heads of staff. | Can find kidnapped heads of staff. | Can track heads of staff in hiding. |
A telecrate drop is very valuable to both the loyalists and the revolution. The loyalists have an advantage in that they start off better armed and know where the teledrop is happening before the revs do. The revs need to buy guns (a lot easier now that the loyalists have no reason to control cargo) and convert the crew to gather enough firepower to take the teledrop. The revs can also kill a secoff and get security radio to be alerted of the teledrop earlier.

Neither side needs the teledrop to win. 
The loyalists are greatly aided by mindshields, since they can hurt the revolution by deconverting revs, and can find the headrevs that way. However, they can just protect head of staff until the shuttle arrives, and then evacuate a head of staff.
The revolutionaries are aided by ammo and trackers and money (selling mindshields), but can overthrow the loyalists without these things.

## Conclusion
To wrap up, I'll explain how my changes would fix the problems with the gamemode.
* **Revs being found early** - If the revolution was exposed, the loyalists could control cargo and start mindshielding far sooner than what the revolution could deal win. However, cargo control is no longer necessary, and the loyalists knowing about the revolution doesn't enable them to get mindshields earlier - they still have to wait for the telecrate drops.
* **Too reliant on cargo** - The loyalists no longer need cargo to get mindshields, freeing it up for the revs to arm themselves. The loyalists could try to control cargo to stop the revs getting guns, but this would draw their attention away from the telecrates.
* **Round Stagnation** - The telecrates provide a source of conflict to stop rounds getting stagnant. The revs can't block loyalists from getting mindshields by wasting the cargo budget - instead they have to fight them for the telecrates. The revs can get trackers to track hiding heads of staff.
