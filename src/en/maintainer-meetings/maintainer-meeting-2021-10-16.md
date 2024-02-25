Maintainer Meeting Notes - Date: 16.10.2021
=
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

Attendees:  
PJB  
Paul  
ShadowCommander  
Vera  
Zoldorf  
DrSmokeleaf  
RemieRichards  
Mirrorcult (last 2)

## A plan for release | Mirror
do we feature freeze, keep going as a standalone thing and let forks take over?
- will /veegee/ steal PJB back? idk
- pjb doesnt like trees
- we will continue to develop the official game

18:07 -- My cookies are already gone. Oh no. WHATTAAMAGONNADO??? 🍪

## Game admins, we need em | Mirror
server population is picking up. we should probably look for more admins if we can.
- we really needs logs before we do this
- also other admin tools
    - logging
    - jobbans
    - notes
    - improve ahelps when we have logging & have them link to a private discord
    - Teleport Here and Jump to Player but not ass
    - click author name of a message to open a context menu, jump to them @PJB for the functionality for buttons in chat
- new admins are gonna ragequit because the lack of admintools
- all gameadmins are basically inactive, delete role


## Discord channel mosh pit
- we have info spread throughout #rules-info, #faq, #annoucements, #progress-reports
    - team agrees its fine, but move faq to website & link to it from #rules-info
- internal channels. its mostly not even for development, more like a meta-gang of friends, so the "contributor" might be a bit misleading
    - VIP: Assigned on discretion. Internal channels (secret-ss14, secret-offtopic, vidya-gamers)
    - Contributor: ""Automatic"" role after 1 PR. Access to #actual-development #progress-reports #role-assign #important-info
    - Move gamer role from role-assign to vidya-gamers
    - Have patreons & contributors have access to patreons?????????????
    - ~~maybe have a seperate discord for developing in the future~~


## Rotation bug funnies | Sloth
Spawning the station rotated to better spot obvious rotation bugs
- sure
- this is terrible for map diff renderer
    - you know the emoji disintegrating gif where it has the funny loading icon? that
      ![](https://i.imgur.com/s3it1jC.gif)
    - Deal with it


## Popup/Prompt standard | Shadow, Mirror
- which side confirm & cancel goes to
    - confirm right

Windows:

![](../assets/images/maintainer-meeting/2021-10-16-windows-confirm-prompt.png)

MacOS:
![](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/Art/dialog_simple_2x.png)

Ubuntu:

![](https://i.stack.imgur.com/tj9Fm.png)

KDE:

![](https://develop.kde.org/deploy/kdialog/yesnowarning.png)

- have a simplified way to create them
    - pjb hates em. "really does not like them" extreme hatred "input dialogs everywhere"
    - pjb made a spooky sound... she scares me
    - AaAAaaAAAaaaaaAAAAaAAA!
    - mom pick me up im scared
    - just saw a blue vera gradient in pjb's krita recent files, d'aw.

- solution: have "popups" that expand out of stuff like the examine window or:
  ![](https://i.imgur.com/iT2WuEo.png)


#### This is already in, woo
~~## Status effects framework & event handling | Vera~~
~~- We might wanna code a general framework for status effects. Discuss what we need.~~
~~- Certain status effects should probably be components so handling events with them isn't bad~~


## Runtime? Variant? Strains? Seed prototypes :chart_with_downwards_trend: | Vera
some systems depend on getting roundstart prototypes and modifying those (by creating variants). this should be standardized to not become a massive mess
- a
- conversation has gone off-rails :focus:
- codebase ain't prepared for YAML hot-reload...
- open git issue for this system
- sacrifice vera by rewriting seeds and then get ideas
- you know the emoji disintegrating gif where it has the funny loading icon? that


## Ancient Hardware vs. Compute Shaders | Paul, hopefully PJB
do we keep supporting ancient hardware or do we save ourselves the trouble and get nicer libs & nice new features
- veldrid
- benefits: pjb dies less daily, compute shaders
- downsides: pjb rewrites renderer, needs to be rewritten anyways
- pjb: might be possible to keep opengl and rewrite renderer to be onpar
- ancient hardware wins again


## Wallmounts, how do | Mirror
*refuses to elaborate*
*leaves*

very fast pjb transcription done by 3 people at once:
- visibility is dependent on the viewport (camera position, side of the wall)
- cant be global (e.g. cant be on the spritecomponent)
- collect list of spritecomponents & pass it to systems that want to look into it so they can switch the visibility (working on a copy of the data)



## Logging stuff | Mirror
- log by each entity system, then group systems together?
    - move entity system, logs are different
    - OOC is not in an entity system
    - manually assign groups instead (like ss13)
- how to store logs
    - throw it on postgres (jsonb goes brrrr) for the time being
    - if its a perf/(web) scaling problem we can change it later
- use loki to aggregate? @Silvertorch5
    - if we need perf we do it then, just postgres for now
- stay with grafana for all logs, or just server metrics? have our own prebuilt solution for logs? @Silvertorch5
    - grafana way too limited, we need our own solution for logs. keep for server metrics.
- ingame log viewer
    - yes, obviously
    - drag select an area when?
- API?
    - check pauls branch
