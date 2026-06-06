# Central Command Intern

| Designers | Coders | Implemented | GitHub Links |
|------------|------------|-------------|--------------|
| n1-nbt | n1-nbt? | :x: No | TBD |

lmk if you want to be added ^

## Overview

The CC Intern is a new roundstart role that spawns at Centcomm, and responds to faxes from the station. This would be mostly an RP role similar to reporter, but there are possibilities to have a bigger gameplay impact, such as by calling reinforcements.

## Background

[This thread](https://forum.spacestation14.com/t/cc-intern-role/27769) pushed me to make this proposal, and has some discussion on the idea. It provided the main rationale for adding CC Intern: contacting Centcomm is inconsistent. The CC Intern is intended to fix that, and make Centcomm somewhat more significant to the station without stepping on anyone's toes *(glances at the NTR)*.
It is a Nanotrasen station, after all. A higher up in Nanotrasen should at least be able to make the intentional choice to ignore the station's command trying to contact them.

## Features to be added

New role: Centcomm Intern
- Spawns at CC
- Spawns with Centcomm Standards (links to CC Intern page of guidebook)
- Unable to be targeted by antags

New CC Intern stamp, distinct from an admin's CC stamp.

New long-range camera monitor mapped to the CC control room.
- Cross-grid camera monitor to view station cameras.
- Alternatively, an AI-eye-type view.

New CC Intern Headset.
- Centcomm channel access.
- Possibly the ability to listen, but not talk on station channels.

The PDA should have a "CC network status" indicator. This indicator is automatically on if there is a CC Intern. Admins can also turn it on manually if they want to respond to faxes.
- Or some other easy way to check if there is a CC Intern before writing and sending a fax.

The nuke code paper in CC should be removed (or moved to an area the intern can't access).

The CC Communications Computer should be able to remotely change the alert level of the station.

The ID computer in the CC control room should be removed.

Above is what I consider to be the minimum list of features. I have suggestions for other potential [anti-griefing features](#Griefing-Prevention) as well as a major gameplay feature below.

### Centcomm Budget & Reinforcements

Centcomm gets its own budget, which can be transferred to/from station funds similar to current department funds.
The CC intern can use the funds to trigger various events.

These events can range from basic CC-approved packages, like the pizza party event, to calling in station reinforcements.

The intern can only call in reinforcements that fit the station's current state. This could use the GameDirector chaos values, as well as other basic checks.

For example, the presence of a zombie would allow the intern to buy CBURN reinforcements. Low security, or high levels of chaos from death may allow the intern to buy security ERT, and potentially set alert level gamma.
- In order to prevent an intern from trying to buy CBURN to check if zombies exist, the CC fund account could be fined for trying to call reinforcements without meeting the requirement.

CC reinforcements could also have body cams that the intern can view (similar to the xorg mothership).

The intern may also have the ability to recall the reinforcements (aka round remove them, as they are not intended to be crew), for a small refund on the purchase (depending on how many survived, and maybe how much equipment they used)

Reinforcements do come with balancing considerations of course, and the roles would probably have to be weaker versions of the current admeme versions. Guidebook entries would also need to be made for the reinforcements.

The CC budget should be disabled if the "CC network status" indicator is down.
- Imagine someone sending all station funds to CC, there is nobody at CC to return it to the station. It would be funny the first time it happened

CC funds could possibly also be used to purchase normally unrecoverable items (such as command gear).

## Game Design Rationale

I think being able to contact Centcomm is a pretty cool feature. There is also an amazing potential for unique situations and interesting roleplay when there is an IC method of contacting admins. Admemes are fun, even just a basic ERT spawn.
But there is no guarantee that a message to CC will even be seen.
The CC Intern isn't an admin, but at the very least, can reply "no" to a fax. Even a negative reply encourages people to try, because they know that their messages are at least being read by someone. 
If the CC budget gets added, the intern will also have a way to create interesting special events without needing to be an admin.

## Roundflow & Player interaction

Being off-station, the CC Intern does not have direct influence on the station. As such, it is very roleplay focused. Command (or anyone with a fax machine) can contact CC for advice or to get support for circumstances they are not equipped to deal with.

If given the ability to buy reinforcements, the CC Intern makes the station more dynamic in response to threats, creating more of a back-and-forth between station and antag.

## Administrative & Server Rule Impact

Any new role is going to cause more complexity, confusion, and problems for admins. CC roles especially are fairly contentious, because there is potential for them to be confused with being an admin.
For example, if the station gets a Central Command Announcement that "This is the purge: all crimes, including murder are now legal." Or something else obviously bad, there is a chance that people will see it as coming from CC, and therefore assume it to be law.
- This is mitigated by giving the intern a separate intern stamp and having the job shown as 'intern' when making announcements, but is still a concern, especially when the role is new.

Some roles are going to have authority, and therefore have more potential to cause issues for admins. Over time, people will get used to CC Interns, at which point I don't think it would be any different from a Captain abusing authority.
Role requirements also help with abuse somewhat, as well as clear guidebook documentation (CC Interns should spawn with a guidebook for this reason). 

### Role Requirements

People have suggested making CC Intern a whitelisted role, but I personally don't like whitelisting roles. Reading whitelist requests makes more work for admins, and doesn't add a whole lot compared to just having a time requirement. I think CC Intern should probably have a HoP and/or Captain time requirement, as well as a general command time requirement.
If admins think it is necessary, I think a better system than whitelisting would be making it require previous CC Intern experience if there is no online admin. That way an admin would actually have to be present for someone's first time(s) playing CC Intern to ensure they aren't terrible. This option would help a lot when CC Interns are first introduced by ensuring an admin is there to handle any issues with the new role.
With a new role, I think it is smart to start with stricter prerequisites, and loosen them if necessary as people get more comfortable with it.

### Griefing Prevention

EORG (or CC griefing) is allowed on wizden LRP.
I personally am not a fan of EORG, but even with EORG, I don't think a CC Intern should be able to grief CC (at least until the round officially ends).
I think this is a relatively minor issue: A griefing centcomm intern is a single, fairly playtime-restricted role, and is the only one at centcomm before the shuttle arrives. It is obvious if an intern griefs, and doesn't seem likely if there is a 0-tolerance policy and long prerequisites.
Additionally, unlike griefing the station or otherwise loosing, CC griefing doesn't have any effect until after the round.
That being said, if admins are worried about a player messing with centcomm before end of round:
- Intern should have minimal access:
	- Command access to get into the control room.
		- The ERT room should be changed from command to CC access.
		- The CC Communications Computer should be changed from CC to command access.
	- Janitor access, so going in dispo doesn't trap the intern.
	- Service, bar, and kitchen access. This both allows the intern to get food and drink for themselves, and potentially become the coveted CC bartender at end of round.
	- Alternatively, CC access can be split into several access groups.
- Currently mapped captain and centcomm official IDs allow access escalation, and should be removed (or somewhere the intern can't reach).
- The intern should be unable to construct/deconstruct.
	- This creates more development complexity, and prevents some fun interactions, such as decorating the evac dock, so should be avoided if possible.
	- The intern should preferably be given construct/deconstruct ability at end of round. The intern's access may also be upgraded to CC all access if it is reasonable to implement such a system.

## Technical Considerations

The base features are relatively self-explanatory.

Long-range camera monitor requires cross-grid camera functionality (also needed for wizard orb).

If the CC budget is added, the request computer UI can be reused, just with a new orders list.

None of the added systems would have any significant performance impact.

### Bonus Wishlist Features

The CC Intern should have a method to talk to the Station AI.

## Small Justification Rant
The CC Intern shares a lot of similarities to the Station AI. It is an entirely unique role that cannot interact with the station via normal means. I occasionally read complaints about AI not having enough to do, but I personally quite enjoy playing AI. I don't think we should be scared to create unusual and roleplay-focused roles. If you don't like playing as a role, simply don't play it. CC Intern is not critical to the station operations; the round will progress fine if nobody wants to play it.
Sometimes you just want to chill, or you are on a trackpad and don't want to play a role where you might need to actually control your mouse quickly, but you still want to do stuff.
