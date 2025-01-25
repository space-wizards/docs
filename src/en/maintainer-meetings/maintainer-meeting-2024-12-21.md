# Maintainer Meeting (21 December 2024)

**Time:** 21 December 2024

```admonish info
**Attendees:**
- Vasilis (Myra)
- EletroSR
- Julian
- Faint
- Errant
- Ed
- notafet
- ShadowCommander
```


Notice: This meeting was recorded:
Notice 2: Myra is stupid and forgot to unmute her mic in OBS. Also the voice is double. Sorry!

{% embed youtube id="qnYBHDHw5mU" loading="lazy" %}

# No topics?
![image](https://i.imgflip.com/64sz4u.png?a481512)

## Stable review
Here the usual list of new features. Mapping changes, bugfixes, refactors and code cleanup are not included.
- [33450](https://github.com/space-wizards/space-station-14/pull/33450) Make unknown shuttle events trigger an announcement
- [33752](https://github.com/space-wizards/space-station-14/pull/33752) Christmas Nuke Song
- [33684](https://github.com/space-wizards/space-station-14/pull/33684) Organize the Sandbox Panel window
- [33763](https://github.com/space-wizards/space-station-14/pull/33763) Give silicons proper lobby/character editor previews
- [33762](https://github.com/space-wizards/space-station-14/pull/33762) Singularity equipment can now be activated with E interact
- [33781](https://github.com/space-wizards/space-station-14/pull/33781) Signal timer duration limit
- [33612](https://github.com/space-wizards/space-station-14/pull/33612) Popup when being pulled shows who is pulling you
- [33348](https://github.com/space-wizards/space-station-14/pull/33348) Adds an introductory message to the user-facing ahelp chat window
- [33788](https://github.com/space-wizards/space-station-14/pull/33788) You can now pet the AI core
- [33505](https://github.com/space-wizards/space-station-14/pull/33505) Bar related tweaks
- [33810](https://github.com/space-wizards/space-station-14/pull/33810) Made anchor visuals generic
- [33496](https://github.com/space-wizards/space-station-14/pull/33496) Names camera routers
- [32104](https://github.com/space-wizards/space-station-14/pull/32104) Rework the HoS's Energy Shotgun (Varying energy consumption depending on fire-mode + re-adds a toned down self recharge.)
    - Suggestion is to increase the recharge delay.
- [33521](https://github.com/space-wizards/space-station-14/pull/33521) Warden headdresses In-hand Sprites
- [33464](https://github.com/space-wizards/space-station-14/pull/33464) Safari hat In-hand Sprites
- [33628](https://github.com/space-wizards/space-station-14/pull/33628) Increase war ops evac time
- [33848](https://github.com/space-wizards/space-station-14/pull/33848) Add meat tag to Five Alarm Burger
- [33830](https://github.com/space-wizards/space-station-14/pull/33830) Monospace Support for Rich Text
- [33841](https://github.com/space-wizards/space-station-14/pull/33841) Other colour of the binary channel
    - These really should be user customizable
- [33678](https://github.com/space-wizards/space-station-14/pull/33678) Rename Dungeon Master Laws to not run into copyright problems
- [33665](https://github.com/space-wizards/space-station-14/pull/33665) Zombies can see Initial Infected
- [33416](https://github.com/space-wizards/space-station-14/pull/33416) Wizard Mind Swap Spell
- [32620](https://github.com/space-wizards/space-station-14/pull/32620) add SpawnTableOnUse
- [32198](https://github.com/space-wizards/space-station-14/pull/32198) Add generator scrap (Plasma / uranium scrap)
- [32583](https://github.com/space-wizards/space-station-14/pull/32583) Add an in-hand sprite for the lizard plushie
- [33424](https://github.com/space-wizards/space-station-14/pull/33424) Makes admins not count towards the playercount cap
    - Should this also remove admins from the playercount reported to the hub? At least as a ccvar?
- [32802](https://github.com/space-wizards/space-station-14/pull/32802) Add the Zombie, a new cocktail
- [32755](https://github.com/space-wizards/space-station-14/pull/32755) Add Holy damage
- [33253](https://github.com/space-wizards/space-station-14/pull/33253) Add Explosion Resistance to SecBelts
- [33328](https://github.com/space-wizards/space-station-14/pull/33328) Chem master UI
- [31872](https://github.com/space-wizards/space-station-14/pull/31872) Spaceshroom grilling
- [32769](https://github.com/space-wizards/space-station-14/pull/32769) Figures can now be activated remotely
- [33889](https://github.com/space-wizards/space-station-14/pull/33889) Christmas anomaly
- [32294](https://github.com/space-wizards/space-station-14/pull/32294) Atmospheric network monitor
- [32032](https://github.com/space-wizards/space-station-14/pull/32032) Gate map
- [33867](https://github.com/space-wizards/space-station-14/pull/33867) Zombies keep their anomalies on zombification
- [33427](https://github.com/space-wizards/space-station-14/pull/33427) Anomaly Scanner In-hand Sprites
    - Should we have policy to add in hand sprites?
- [32711](https://github.com/space-wizards/space-station-14/pull/32711) Holopads
    - Issues noticed:
        - If someone does an emergency broadcast and end it, you can end the broadcast for one and that one wont display the broadcast. Is this a bug of a feature?
        - All holopads break when you unwrench one?
            - Real or cap?
        - The line busy message needs to be better
        - The holopads seem to be client authorative, this should be refactored if true
        - If you are in the range of multiple holopads multiple messages will be printed in chat, issue needs replicatiation.
- [32825](https://github.com/space-wizards/space-station-14/pull/32825) Fix AME power generation
- [33757](https://github.com/space-wizards/space-station-14/pull/33757) Adds Advanced SMES, an SMES with higher capacity for mapping
- [32694](https://github.com/space-wizards/space-station-14/pull/32694) Make safes craftable
- [33879](https://github.com/space-wizards/space-station-14/pull/33879) Only disable panicbunker for admins with AdminFlags.Admin
- [33104](https://github.com/space-wizards/space-station-14/pull/33104) Replace Cellular Slime mob damage with Caustic
- [33647](https://github.com/space-wizards/space-station-14/pull/33647) Mercenary gear contraband tweaks
- [33494](https://github.com/space-wizards/space-station-14/pull/33494) Sprite Movement working with AI movement
- [33776](https://github.com/space-wizards/space-station-14/pull/33776) New Drazil plushie (inverse lizard plushie)
- [33922](https://github.com/space-wizards/space-station-14/pull/33922) [Christmas] Y'all want a Smite Cranberry?
- [33854](https://github.com/space-wizards/space-station-14/pull/33854) Show battery level for selected devices in Power Monitoring Console
- [33697](https://github.com/space-wizards/space-station-14/pull/33697) New mid pop station: Loop
- [33842](https://github.com/space-wizards/space-station-14/pull/33842) Food Container Size Increase
- [33635](https://github.com/space-wizards/space-station-14/pull/33635) Fix hugging buckled mobs instead of unbuckling

## Other
- "Do not map" suffix should be an entity catagory (and checked)