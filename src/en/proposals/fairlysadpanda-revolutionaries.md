_Operative: you will be going deep undercover at the new Nanotransen research lab we have uncovered in the sector. Your objective is to seize control of the space station from those unsuspecting fools so we may use it and its crew for our own ends. To aid you in this, we are providing you with the tools needed to seize control of the loyalties of the unshielded crew. Install yourself as the leader of a mutiny and destroy the station’s chain of command. Be aware that Nanotransen has access to defensive mechanisms against your revolt, and you must not let their Security team act against you before you are ready. As such, stealth and intelligence will be needed to achieve your aims._

_Good luck, Operative. Long live the revolution._

# Revolutionaries 2.0

| Designers                      | Implemented | GitHub Links |
| ------------------------------ | ----------- | ------------ |
| Hannah 'FairlySadPanda' Dawson | :x: No      | TBD          |

# Overview

Revolutionaries is a classic Space Station 13 game mode, updated and revised for maximum chaotic fun. A cabal of Head Revolutionaries, specialist infiltrators from the Syndicate, have sneaked aboard the Space Station. Their job: deliver a functional space station into Syndie hands.

To do this, the Head Revolutionaries use their own guile like other traitors, but they also have access to tools that alter the loyalties of defenseless crew members. These tools provide a way of the Head Revolutionaries turning the staff against the station, creating a team of loyal operatives or a disposable human tide that can overwhelm the station.

Like all good political insurrections, the drama is in the betrayal and **paranoia is the point.**

## Background

The current Revolutionaries game mode ("Revs") as implemented is a problematic game mode that has lead to:

- Repeated revisions to anti-metagaming rules, via both SOP and Space Law
- A large number of complaints and discussions about improvements on Discord including, but not limited to:
  - Revs causing a murderhobo tide that Security has to fight with murderhobo violence
  - Boring stalemates and unclear round state, especially for the loyalist crew
  - The endless feels-bad forced round-removal of discovered Head Revs and Heads Of Staff, sometimes for over an hour
  - Paint-by-numbers round activities entirely focussed on flashes and MindShield implants.
- A lengthy discussion at the 30th December 2023 Maintainer Meeting surrounding Revs, specifically flagging its problematic impact on Salamander/MRP
- Drain on Admins, both due to players demanding ERT revents in response to a discovered revolution and rules enforcement

Revs is badly in need of a refactor to encourage a more dynamic round that encourages paranoia from Security and smart play from the Revolutionaries.

## The Rules

One or more Head Revolutionaries are spawned from the usual pool of players who have opted-in. These Head Revolutionaries have one specific goal: deliver the station, mostly-whole, into Syndicate hands.

- To deliver the station into Syndie hands, the Bridge must be taken over with the **CentComm Uplink Console** given all Head security IDs. This triggers a countdown until the uplink is severed and the Revs win. Doing so results in a major syndicate victory and the round ending.

- A draw is achieved if the station is somehow nuked, or if a Head Rev escapes to fight another day.

- A minor crew victory is achieved if a Head escapes to CentComm.

- A major crew victory if all Head Revs are neutralized, either by death, implant extraction or being imprisoned. If this occurs, all Rev members of staff de-convert and Centcomm (belatedly) detects the mind control rays being blasted at the station, sending an evacuation shuttle and allowing the round to end. (If the surviving chain of command wants a longer round, the shuttle can be recalled).

## Why this is fun for the bad guys

**As Head Rev:** You’re the underbelly of justice seeking to overthrow the mighty - the heroes of your own story. Target any department, any group of staff, and bend them to your will. Being a Head Rev means you get to pick your team and boss them around to cause specific, targeted acts of violence. There’s loads of role-play opportunities, and your directive to deliver a working station means you have to work around your horde’s desire for carnage.

**As a Rev**: Suddenly plucked from your normal life, you now need to continue your job keeping the station running and overthrow the horrible bosses who’ve been stepping on your neck for years. Work with a secret team, meaning RP opportunities with players you may normally never interact with. Turn your profession into a tool of destruction. Being a regular rev gives normal players a safe opportunity to learn to be an antagonist.

## Why this is fun for the good guys

**As Heads:** You are suddenly the mouse in a station filled with cats, but you have to keep the station running. Can you trust your team? Can you trust anyone? Do you have a weapon close at hand? All the fun kinds of stress. Most department heads suddenly need to become best friends with Sec.

**As Security:** You have multiple departments to defend, and a requirement to temporarily lock up anyone who looks at all shifty. An active competent security team is required to win a Revs round for the crew, and that means the HoS and friends are the stars of the drama.

**As the crew:** Maybe you’ve always wanted to beat your boss senseless. Now you can! But for the strongly-loyal crew, running the station without getting turned is a game of risk-versus-reward. After all, Nanotransen isn’t going to just feed you into a wall of bullets and lasers, but the Head Revs totally might. Pity the medbay; if the round turns into a storming of the palace scenario, they are suddenly going to be very busy.

## Why this is fun for the admins

Revs is a mode where things ramp up in drama over the course of the round, but the regular operation of the station probably isn’t directly at risk. Both sides have specific win conditions (the elimination of the other), with the station being pulled between them. This means it’s different from the normal violence-and-gibbing approach that traitors and operatives cause. This also means no more having multiple layers of anti-metagame legislation to control round flow.

## Important Refactors and New Content

### Head Revolutionary abilities are tied to a Revolutionary Implant.

This implant does three things:

1. Gives the HR innate access to talk on the Syndicate radio.
2. Grants them a Influence conversion aura around themselves.
3. Grants them a conversion ability that allows them to covertly flip people to Rev.

Conversion works as follows:

1. The Revolutionary Implant grants the owner the ability to see the Influence level of those around them.
2. If the Head Revolutionary sees a crew member with a high enough Influence level, they can activate their implant's ability and click on the target.
3. If successful, the target is silently converted to a Revolutionary.
4. The ability enters a cooldown.

### Removal of MindShield implants being orderable from Cargo

MindShields are metagameable and make it extremely unfun to play as a Head Rev. They have no interesting interactions; they’re just a hand-wave for why some people are completely immune to a game mechanic, and whilst that’s utterly required for round flow (allowing Sec and the Heads to trust each other) it is a magic solve-everything button which leads to a total wall in design.

A small number of MindShields could be kept on-station to allow staff promotions within reason. _A kind admin might decide to send a crate if the station runs out and it'd be good for the round, but this is out of scope of this design document._

### Removal of Flashes being able to convert people

Flashes are metagameable, confusing for newbies, hard to balance, and enforce too much reliance on manufacture by Science by the Revs for effective round flow. They also have no narrative justification beyond it being an Ur-mode from the dawn of SS13. There are people playing SS14 that are younger than the only good _Men In Black_ movie.

### Addition of Influence as a tracked player stat, and associated gameplay features

Influence is a value that each player carries. MindShielded players are always value 0. Influence is raised by a few routes (exposure to Head Revs, propaganda and one or two restricted drugs like Mindbreaker Toxin).

Players gain Influence by:

- Standing near a Head Rev they can see.

- Being near Propaganda they can see.

- Being injected with Mindbreaker Toxin. This is a very big bump and is intended for kidnap scenarios.

Players lose influence by:

- Not being near any source of Influence. This is quite slow, and is reduced to nil if the player has been converted.

- Influence degrades reasonably quickly if placed in the Sec cells and exposed to calming jazz music.

### Influence ticks up when exposed to sources and slowly ticks down when not. There is a max Influence level.

Addition of NT and Revolutionary posters and propaganda, that both sides, and traitors, can put up and take down across the station.

These posters can be printed across the station by both sides and gives Security Cadets, Lawyers and bored Passengers something to do, even on non-Rev rounds, and a reason for Sec to patrol (imagine!). They’re an DOT effect with a max cap per item, and add or subtract Influence from those who see them.

Putting up pro-Revolution posters is added as a Traitor goal to make them have a reason to appear outside Revs.

Clowns get the ability to put up annoying "Visit Clown Planet" tourism posters.

Posters can be be destroyed by spraying them with paint or tearing them down.

### Addition of Loyalty Loudspeakers in Sec

These Loyalty Loudspeakers are audio emitters that reduce a player’s Influence level, even if they’re converted. If a player who is converted de-converts, their Influence immediately drops to zero. This is a new machine that requires quite a bit of power to run. A button is added to the Warden’s office to disable and enable all loudspeakers. The loudspeakers play calming, smooth jazz.

These Loudspeakers cannot be made on the station. One of the key jobs of Sec is to ensure Sec remains safe; if it's been bombed and the Loudspeakers are inoperable, the Revolution is succeeding.

### Head Revs can use an implant ability to silently convert characters with high enough Influence to being a Rev.

This replaces flashing outright, and makes conversion a stealthy game. Revs do not know who the Head Revs are unless the Head Rev outs themselves.

### Add the Interrogator, an electric chair that tests Influence levels

The Interrogator is a high-power-draw device that lives in Sec. This machine does three things:

1. Minorly fries the person placed inside it. `Your hair stands on end!` If you're a Diona, you are set on fire. `The lightning ignites your limbs!` It does no damage to Slimes. `You feel tingly`.
2. Reads their Influence level.
3. Causes the lights to flicker station-wide.

This allows Sec to ensure anyone they're releasing from prison has a low influence level.

It can be emagged to dramatically increase the power draw, EMPing the station for a period of time, and instantly frying any poor sod put inside it.

### Add the Centcomm Uplink Terminal as an indestructable core console on the Bridge.

This terminal is the core security uplink between the space station and the rest of the universe (in fiction). It can send announcements and notifies who is the current chain-of-command.

This console is indestructable, protected by military-grade force fields, immovable and powered by a nuclear engine that will outlast the star it's anchored to.

This is the end-game objective that Revs want to compromise.

### Denote the IDs that Heads Of Staff spawn with as Head Of Staff IDs

These are the mid-game objectives that Revs want to obtain. Because these are stealable objects, this gives Rev Thiefs a unique role.

### Killing the Heads is now not required for the Revs to win, instead requiring taking the Bridge and compromising the Centcomm Uplink Terminal and defending the Terminal for a period of time.

This removes one half of the round-removal problem and gives the Revs a clear final target that works a bit like the Nukie bomb.

To compromise the terminal, the Revs need access to a Head Of Staff ID. Any will do: using them on the terminal allows for the Uplink to be disabled after a timer.

Each ID used on the terminal reduces the amount of time the countdown will take by a certain amount.

The start of the countdown is broadcast as a station announcement:

`CENTRAL COMMAND UPLINK SEVERANCE PROCESS INITIALIZED BY [names on IDs here]. THIS STATION WILL BE REMOVED FROM NANOTRASEN SECURITY CONTROLS IN [amount of seconds]. IF THIS IS UNINTENTIONAL, PLEASE CANCEL THIS PROCESS BY VISITING THIS UPLINK TERMINAL AT CO-ORDINATES [co-ordinates here]`

When this countdown reaches one minute, similar to the Nuke Ops game mode, a short theme plays.

If the timer reaches zero, if it's a Rev round, this triggers victory. This totally shuts down station security, and all passes become All-Access. (This occurs even if the round is not Revs).

If this is a Rev round, the Head Revolutionary passes are renamed "Consul" and all Head and Sec passes are renamed "Enemies of the Revolution". But this is just for flavour, as we're into EOR gib-fests at this point.

_If this **isn't** a Revs round and this has happened, this would be an excellent time for CentComm to send an ERT._

### Head Revolutionaries can be de-converted by removing their Revolutionary Implant. Revolutionaries can be de-converted by spending a bit of time locked up in Sec listening to smooth jazz music.

This removes the other half of the round-removal problem.

# Role Outline: Head Revolutionary

## How It Should Feel

You’re the cunning insurgent plotting to overthrow the station. You get to pick your team and plot the stages of your revolution, and then overthrow all order and install yourselves as the leadership!

## Goals

### Build A Team

Convert a few loyal and smart associates for your revolution via exposing them to your mutinous ideas.

### Begin The Revolution

Your associates gather the tools needed to overthrow the station and expose more people to your influence, making your conversion job easier. You sit like a spider in the web and plot.

### Overthrow Centcomm

You steal the Head IDs, break into the bridge and switch off the station’s link to Centcomm, winning the round.

## Core Mechanics

### Revolution Implant

You have a Revolution Implant. This is a really powerful and special implant that hooks into Syndicate mind-control rays being blasted at the station. This implant does nothing outside the Rev round type.

This implant is what makes you a Head Rev. It can be removed via an Implanter, and if someone else is injected with it, they become a Head Rev. This probably will never happen (but would be a really robust way to evade Sec figuring out who the HRs are)

### Communications

Your implant gives you access to the Syndicate radio channel innately. This can be changed to a unique Revolution radio channel, but given Nukies, Traitors and Revs are exclusive to each other, it should be fine to just use the Syndie channel. Head Revs cannot talk to normal Revs on this channel: it's just for planning and collaboration between Head Revs.

### Influence

All non-head and non-security crew have an internal Influence count.

Players gain Influence by:

- Standing near a Head Rev they can see.

- Being near Propaganda they can see.

- Being injected with Mindbreaker Toxin.

Players lose influence by:

- Not being near any source of Influence. This is quite slow, and is reduced to nil if the player has been converted.

- Influence degrades reasonably quickly if placed in the Sec cells and exposed to calming jazz music.

### Conversion

By standing while conscious near people, you increase their Influence to your control. Once they reach a certain number, you can target them with your innate Convert ability. This mentally dominates a loyal crewmember and hands them their shiny Rev antag token. They are not told who converted them; it’s your choice as Head Rev to communicate this information.

Conversion works as follows:

1. The Revolutionary Implant grants the owner the ability to see the Influence level of those around them.
2. If the Head Revolutionary sees a crew member with a high enough Influence level, they can activate their implant's ability and click on the target.
3. If successful, the target is silently converted to a Revolutionary.
4. The ability enters a cooldown.

### Centcomm Uplink Terminal

You win by compromising this terminal.

To trigger this:

1. Get at least one of the Heads ID cards. This must be their special ID cards, not HOP-manufactured ones.

2. Input the cards and click the button to start the unlinking of the uplink.

3. Wait some number of seconds for the uplink to be disabled. This alerts the entire station over comms that the Revs are doing this: I hope you have fortifed the bridge!

# Role Outline: Revolutionary

## How It Should Feel

Plucked from your normal life by sudden desires for mutiny, you need to spread the good word across the station and assist your friends in overthrowing Centcomm. But don't be too suspicious: Security have ways of making you talk!

## Goals

### Spread The Revolution

Use Propaganda posters and literature to spread the Influence of the Revolution and get into the harder-to-reach areas of the ship.

### Free Yourself From Tyranny

Ambush and arrest your department head; steal their ID for the greater good, and requisition their tools for the Revolution.

### Don’t Get Gibbed By Sec

Avoid being rumbled by Sec; they have guns and equipment that makes rumbling and smashing your mutiny possible.

Core Mechanics

### Propaganda

The printers, posters and books of the station can be influenced by Revolutionaries, who can also make them via crafting and using the station’s printers. Sec, the HoP and the Captain are trained to identify revolutionary literature (it’s not obvious to the rest of the station), but it’s also possible for traitors and nukies to make them to throw Sec off their own activities.

Propaganda slowly ticks up an exposed character’s Influence meter and allows Head Revs to quickly convert a compromised department if not dealt with.

### Drugs

Mindbreaker Toxin can be manufactured and administered as a bulk Influence dose.

# Role Outline: The Security Team

## How It Should Feel

The crew might be plotting against you. Is the missing Chief Engineer due to incompetence, a traitor, or a mutiny? Dispatch officers to identify suspicious individuals - people who are in places they shouldn’t be, and confused people acting out-of-character. Find the spiders at the centre of the web and crush them. Or, robust your way to victory by reclaiming the Bridge from the mutineers.

## Goals

### Investigate Insurrection

Why are your posters being torn down? Where’s the HoP’s ID? Why does that Clown seem to show up everywhere?

### Crush The Mutiny

Once you’re confident it’s a Rev round - the HoS being missing or his ID being stolen is a bit of a clue - you need to find out who it is who’s been doing all the converting and stop them. That’s easier said than done - even de-converted revolutionaries might not know who the ringleaders are, but arresting and interviewing them after deconversion is a good place to start.

### Reclaim The Bridge

No matter what, if things go wrong there’s always violence to fall back on. Grab your hardsuits and laser rifles and reclaim the bridge from those traitorous dogs.

## Core Mechanics

### Propaganda

Sec officers, the HoP and the Captain can identify revolutionary propaganda easily. and disposing of it as simple as throwing it into a disposals chute or out an airlock.

Sec and Sec-friendly professions like the Lawyer are also encouraged to put up their own friendly posters around the station, encouraging loyalty in the crew. These posters counter-act Influence generation and decrease unconverted crew Influence levels.

Putting up loyalty posters is something to spend time on if the shift is quiet, and can be delegated to adjacent roles like the Lawyer. Likewise, if someone’s tearing down those posters, there’s a problem.

### Loudspeakers

Several security loudspeakers are built into the Security offices. These loudspeakers have quite the power draw, but when enabled (by the Warden or HoS) they emit calming jazz music that is proven by Nanotrasen behavioural scientists to counteract mutinous intent. Being inside Sec whilst the loudspeakers are on rapidly purges Influence and can de-convert Revolutionaries.

It is also possible to allow for mobile loudspeakers that’d behave a bit like the A.P.E to be moved around the station, although they’d affect station power quite a bit, and people might complain about the constant jazz music.

### Identifying The Revolution

You can identify the revolution in one of two ways:

- Extracting the Head Rev implant from a Head Rev
- The Revs attack the Bridge

And even an uplink disconnection attempt might be a very complex psi-op by a Traitor!

There are no other mechanical ways to fully identify a mutiny. **Paranoia is the point.**

### Reclaiming The Bridge

If the Revs decide to launch their mutiny, it’s time for the Warden to hand out guns to Security, and recruited loyalist crew, to take back the bridge before the uplink is disconnected. In this way the round functions a little like Nukies, except with a (probably) less well-armed opponent who is defending one specific point.
