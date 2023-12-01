# 2021-10-02 Maintainer Meeting
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

Attendees:  
PJB  
Vera  
Paul  
Smüg  
Silver  
Shadowcommander  
Mirrorcult

First topic: when are we playing spelunky arena mode

## Vera: Standard for missing components in new resolve standard
right now they just fail silently and return
- log errors in the resolve, make it optional to disable

## Sloth: Refactoring collision masks to something like source
because everyone stuffs them up
- sounds good go for it

## Vera: mobs probably need a base mob prototype
yes
pj notes current species impl is bad
3 different prototypes per species -> should be one honestly
pj notes "eausugeuguegebgeyehmeh"
SS13 does 2 too the problem is that all the data is duplicated in the mob entity prototype SS14, SS13's is fine.

## Vera: can we stop naming things base.yml
- may the odds be ever in her favor
- base_xyz.yml format

## Vera: future of async interactions
- do_after() etc
- actions/callbacks instead?
- events can be serialized unlike async, but using events is more painful
- T E C H D E B T -> makes issue 2&>1 /dev/null

## Mirrorcult: wiki.js docs & bi-directional git support
- git support for wiki.js docs so non-maintainers can contribute easier
- talk about more docs in general, how do we get em? enforce it? when do we enforce it?
    - enforce for large prs. make required
    -
- vera still salty about ECS document being grieffed smh :pensive: at below
- silver grieffed ECS omegalul
- paul discovers autoscrolling based on where you type in hackmd

## Sloth: PVS performance because people lifted up the carpet and saw the termites
- serialization slow
- acruid missing
- remove player specific states -> ???? -> pvs fixed
- custom path for player specific states?
    - have two events, one for common state and one for player-specific states
- pjb.speech_speed=120%

## Playtest review
- bugs, perf. etc
- the gang gets ratiod by vera
- vera is in (s)pain
- tickets
    - persistent
- mom and dad are fighting

## Literally everyone: We need logging
- how do we persist:
    - positions -> entitycoordinates, but not the literal type
    - entities -> euid, name, prototypeid
- db stuff needs doing and paul is too dumb
- silver will check out grafana/loki pains

## SS14.Admin experience
- what stats to display
- have one place to view logs
- access to admin panel?

## Progress Report
- opendream & shuttles in next pr
- look over contents
- deadline: soon:tm:
    - yes pls soon I want tg walls and byondchat
- [PR link](https://github.com/space-wizards/website-content/pull/19)

## Sloth: The big shuttle bonanza
#### How to thrust
- Should thrust be related to the position of the thruster, especially for angular velocity i.e. should it be perpendicular?
    - Should thrusters be smoothed to make w i d e t h r u s t
- How should thrusters be obtainable
- What should the driving UI look like, radar like raft / baro? Controls? Access locked?
- Should it be possible to rotation-lock to make driving something like an escape pod easier
- Shuttle collisions, minimum velocity / mass / effects (I think last time we talked about it was a couple tiles destruction max)
- Speedcap?
- Which sprite set are we using (eris?) Should we support additional stuff like wings
- how should ship guns work
#### How to dock
- Do we actually want grid merging vs just attaching it via a joint. Gonna have the eventbus flooded with the grid change (parenting events)
- Somewhat related: Floyd mentioned having a salvage shuttle that tows stuff in rather than using something like a tractor beam
#### Balance questions
- How many thrusters to move an average size
- S H U T T L E BOMBING

#### GitHub Projects, Discussions
- Discuss how bad they are.
- GitHub Discussions is where ideaguys go to die.
    - Vera: YEET
    - salvage, then yeet
- Why tf did Paul create https://github.com/orgs/space-wizards/projects/6hh
    - i propose raising the debt ceiling. all in favor say aye

## Meeting review
what could be done better in terms of moderating?
- make sure pjb eats dinner before meeting X3
- play jackbox after next meeting
- play xonotic *during* meeting
