# Grab

Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar.

| Designers | Implemented | GitHub Links |
|---|---|---|
| FaDeOkno (dis: _kote) | :information_source: Open PR | https://github.com/space-wizards/space-station-14/pull/30011 |

## Overview

Add a combat system that allows to hardly grab, hold at one place, choke or throw away people. Grabbed person can escape with random chance.
While grab is on it's last stage, grabbed person can't breathe, and grabbing person can't use their hands.
Grabbing person can throw away the one who is grabbed if grab is on second or third stage.

## Background

This proposal is contextualized by the state of the game when you only can punch and disarm your opponent without weapon. Combat is based on equipment, and unarmed fights are really rare and simple. In my opinion, these fights with only LMB and RMB lack of dynamics and variety. With grab, fighters' moves can be much more unpredictable to the opponent, and unarmed fights will be not "who found the weapon first"-type every time.

## Grab itself

You can use Ctrl+LMB while in Combat Mode and pulling your target to grab it. Grab has three stages - Soft, Hard and Choke. Firstly your grab will be Soft, and can be easily broken. 
Next Ctrl+LMB click will change your grab stage to Hard, making it harder to escape and allowing you to throw your enemy. For this stage you need at least one hand to be used, even if you are reptilian, or any other mob that can pull objects without using hands.
The last stage is Choke. Grabbed person will not be able to breathe and speak while grab is on this stage. They can only try to escape as soon as it possible, or punch the grabber. Grabbing person have to use both hands to get to this stage, so they can not just be choking and attacking the target at the same time.
To avoid spamming, Grab and escaping it have a delay, so nobody can just spam-grab you and choke to death.

## Grab-Throwing

While on Hard or Choke grab stage, you can press Ctrl+Q to throw grabbed person at the direction you pointed. You can throw people on maximum 2.5 tiles distance. If they hit a wall, or anything else blocking movement - they will get Blunt and Stamina damage, as the hit entity. Second throw will cause staminacrit, if it was not restored.
