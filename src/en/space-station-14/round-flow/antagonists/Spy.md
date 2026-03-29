# Antagonist - Spy

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| TheSecondLord | TheSecondLord + anyone else willing to help | :warning: Partially (Antag foundation, basic spylink and bounty board system) | TBD |

## Overview
This concept is inspired by the popular spy thief antagonist from ss13, which itself inspired elements of the current thief antagonist. However, they should differ greatly from thieves in terms of gameplay and round impact.

Spies are a semi-common *subgamemode solo antagonist*, infiltrating the station on behalf of a highly confidential but presumably malicious  (and presumably syndicate-affliated) agency. As a spy, your goal is to steal items and structures from a progressively cycling bounty list, using a hacked PDA to remotely beam them to your superiors. For each bounty completed, your contractors will send you a syndicate item as a reward, aiding in the completion of more crime.

## Background
There are currently concerns being risen about the underwhelming impact and player engagement resulting from traitor steal objectives (i.e. the item disappears into the traitors bag or stash, is usually not recovered and has little impact on the round), with potential reworks to traitor objectives on the table. This is an attempt to provide a very traitor-adjacent antag which approaches target stealing gameplay in a more engaging and directly impactful way, while also involving progressive traitor mechanics that help push them to disrupt the station throughout the round instead of just ticking off objectives right before evac docks.

## Features
**The Bounty Board**
Similar to an uplink, the bounty board is an interface that spies can access through a PDA, using a code that they are informed of in their character menu. The bounty board can be unlocked by inputting the code into a PDA's ringtone selector; unlike uplinks, this code will tune *any PDA* into the bounty board. Additionally, the code used to unlock the bounty board is determined per-round, and will be *the same code for all spies*.

Upon unlocking, the PDA will gain the ability to open the bounty board interface, lock the bounty board, and toggle object stealing. The bounty board itself contains a list of entries for objects which the spy's contractor desires, including a variety of devices, machines and weapons. These entries are divided into 4 categories: Easy, Medium, Hard and Grand Heist. Each entry lists a corresponding reward, which will be given to the spy who turns in that bounty. Each entry also contains a short flavour description from the spy's employers, as well as a very basic overview of where you can expect to see that target on a station as an aid to newer players. Completing a bounty will also mark it as "completed" on the board, locking off anyone else from turning it in. The board will fully reset every ~20 minutes, providing a new set of bounties. 

Whenever the bounty board is populated, it will check the jobs of spies currently in the round and discourage listing bounty targets that are very easily obtained by members of a certain department. For example, having a spy with a job in medical will discourage the bounty for a health analyzer to appear, as it is common departmental gear that is trivial for someone from that department to complete.

Targets that were submitted from a previous bounty will not repeat, while targets that were listed but were not submitted on time may appear again with a lowered chance. Grand Heist targets are an exception: there's always 1 listing for this difficulty, and it will not be replaced with a new grand heist objective on bounty board refresh, even after completion.

The items given as rewards are divided into 4 categories, corresponding to the 4 bounty difficulty tiers. Reward tiers are not necessarily categorised based on the exact TC value of the items they contain, and instead rank items by how useful they may be to a spy. 

**Spylink Stealing**
Stealing an item is done by interacting with it while in-range and holding an unlocked spylink. The interaction will fail with a popup if the item or structure is not a current bounty target, the bounty has already been fufilled, or if the user is not a spy. Otherwise, this will begin a medium length do-after, while playing a subtle ambient sound and creating a very obvious holographic visual effect over the target for the duration of the steal. If the do-after is completed uninterrupted, the target will disappear, and the bounty will be marked as completed and able to be turned in at the spy's leisure. Moving, getting hit, switching hands etc. will interrupt the do-after and cancel the visual and audio effects. Items with any kind of storage will dump their contents out when stolen.

Successfully stealing a target will cause it to be completely inaccessible for ~10 minutes while the spy's employers scan, study and take notes on the stolen technology. After this time is up, they will discard of the item or structure through...

**The Black Market**
The black market is a new category of cargo orders (labelled as "???" on the category list) which can be accessed with either a cargo or security request computer. This is a way to purchase from certainly not NT approved sources, and as such buying goods from the black market for personal use should be seen as a minor crime by security.

At round start, the black market is randomly populated with a few low-impact syndicate offers. Some possible deals include syndicate merch, bundles of mosins, syndicate bureaucracy crates including syndie stamps, cybersun pens and business cards, and bulk crates of nukie plushies, syndicate figurines and syndicate novelty lighterboxes. Roundstart black market deals should provide flavour and variety, and should not provide access to anything beyond very cheap low-tier gear. 

The main purpose of the black market, however, is that listings for items previously stolen by spies will show up here. When the 10-minute study time is completed on a handed-in target, a listing for that target will be added to the black market, which can be bought back by cargo or security for a marked-up price. This both allows the crew to retrieve stolen items for a cost and allows security to survey the criminal activity of spies, albeit with a significant delay. The price of the buyback is predetermined and based on the difficulty tier of the stolen item; the station should expect to be paying a premium to buy back a stolen department head steal target item.

**Freebies**
A minor feature of the bounty board is that it has a tab for free flavour items, similar to the uplink "pointless" tab. These can only be redeemed once per spylink, and include such luxuries as: a pair of sunglasses, a fancy blue suit and balaclava to impersonate a certain mercenary, and the same distinguished attire but in red.

**Objectives**
Spies are given some basic objectives. These will always be the following:
- Complete at least x bounties.
This is intended as a basic nudge towards what you should be doing as a spy. Unless you have an unfortunate round, you should be able to complete this objective easily over the course of a round.

- Complete at least x *difficult* bounties.
Similar to above, but only counts "hard" and "grand heist" bounties. Encourages spies to push for the harder bounties if they want completion. Should only require 2 or 3.

- Assassinate a random department head.
Functionally identical to the syndie equivalent. Gives the spy something to use their hard-earned gear on besides stealing.

- 1 roleplay objective.
This will be an untracked objective similar to wizard's "show off". This may be something like: cut power to x department, interfere with x department's communications, hinder x department's work, commit identity theft, spy on x crewmember and so on.

## Game Design Rationale
Spies are, first and foremost, designed to compliment both syndies and thieves. As a subgamemode, they are not intended to be the driving force of a round, but they should still be impactful and dangerous. They are a slowly growing threat that, if not kept under control, will gradually become more and more detrimental to the station's operations until an evac is necessary. Unlike syndies or thieves, which are both given their budget/tools at roundstart, spies start with nothing but have the unique potential to become more lethal as they engage with the antag's intended gameplay loop.

Spies should be kept *simple*, sticking to these main few mechanics to form a gameplay loop that is approachable to less experienced antag players. Variety can be added through more bounty targets, rewards and roleplay objectives.

For the antag player, they reward skill, speed and evasiveness with more gear, and the randomness of the given rewards encourages resourcefulness while making a "meta" impossible. They create many risk-reward scenarios that the player must navigate, pushing players to act swiftly and boldly to secure particularly desirable rewards. Generally speaking, spies should be *stealthy*, but should *not* play passively.

Syndies are limited by a tight budget and a reliance on their uplink, while thieves are limited by pacifism and restriction of choice to predetermined kits. Spies have their own limiting mechanics to keep them from becoming too powerful:

- *Evidence of crimes*: No matter how stealthy a spy is, their successful steals will always eventually appear on the black market. This makes it impossible for the crew to never catch onto a spy's crimes, even if they haven't yet pinned it down to a single person. This creates emergent security gameplay, since a detective can scan forensics on recovered stolen items, check door logs in places where stolen items may have came from, and eventually build a case to uncover the culprit. This also prevents rounds where the crew feels like nothing is happening at all, since they are given solid proof of unlawful activity occurring.

- *Competition*: The biggest threat to a spy is most likely another spy. Spies are designed in a way such that they are encouraged to compete against each other. It is likely that spies will encounter each other going for the same steal target, leading to natural conflict to complete the bounty for themselves. Spies would not be prevented from working together, and collaborating may sometimes be worthwhile, but spy gameplay and tasks should be designed in a way such that teamwork sacrifices efficiency in terms of task completion.

The tight timers on bounty completions, better rewards for harder targets, and the constant threat of being beaten by another spy encourages spies to be bold in their antagonistic actions, leading to them having more impact on the round overall. The presence of the black market may also end up assisting other antagonists, particularly for cargo members who can use it as an opportunity to get their hands on otherwise high-security items without having to steal them for themselves.

Additionally, departmental tech being stolen creates problems which will form rifts between departments: in a round, the chef may have their microwave stolen, leading to them asking for it back ASAP from cargo. Meanwhile, cargo may be prioritising spending their limited funds to pay the extortionate price to get the captain's antique laser back, which was also stolen. Cargo may put pressure on security to catch the culprit, the head of personnel may increase funding allocation to cargo to buy these items back, and the whole time security may blame the captain for getting their prized laser stolen in the first place. All of this creates friction between departments, which drives the story of a round.

Spies being able to access the bounty board from any PDA ensures that they can't be completely locked out of completing their objectives as a result of making a mistake. If security catches a spy, they may take their PDA, but the spy should be able to get a replacement from HoP. Having spylink access is a requirement for 2 of their objectives, so it is important that they can't lose it permanently in the same way that a traitor may lose their uplink. This makes them more forgiving than thieves or traitors, since even if you have everything taken from you, you can still start over from the beginning and bounce back.

Spies sharing a PDA code creates an interesting dilemma where, despite usually being against each other, all spies have something in common that they can use to their advantage. The spy code is highly desirable for security, because even though they can't use the spylink themselves, they can use it to track what the next possible targets will be and potentially prepare sting operations at the locations of these targets to catch spies. Due to this, a confident spy could possibly send security an anonymous tip informing them of the code in an attempt to sabotage another spy.

To compensate for this, spies should be, in most ways, weaker than traitors. While they may be able to acquire gear over time that exceeds the value of a traitor's uplink, this gear is picked randomly from a separate spy pool (which may include omissions such as having some of the high-end explosive options removed, and may also have additions that are not usually seen in the uplink), and the highest achievable tier of reward can only be claimed once by one spy as a reward for an exceptionally high value item. Combined, these factors should prevent spies from powercreeping beyond traitors, and instead put a focus on resourcefulness, planning and most importantly *strategy* instead of large quantities of strong traitor tools, while still providing many options and variance between spy rounds.

An important part of determining the targets to be used in the bounty target pool is featuring items and machines that will make the spy put in work. Higher difficulty items should require more *time, planning* and *equipment* to obtain; for some easy difficulty targets, you may be able to find spares by chance in maints, fabricate new ones with a circuit imprinter, or even ask for them. However, medium difficulty targets should almost always require you to trespass into an area or steal something from someone, hard difficulty objectives should usually involve either stealing a department head's prized possession or trespassing into a secure area such as security or the bridge, and the most difficult grand heist tier will require you to steal from the captain, warden or head of security. It is vital that a spy cannot just roll science, make a flatpacker, and achieve every objective through crafting machinery. Likewise, targets that can be ordered from cargo should be discouraged, although this comes with more leeway as this requires either justification (roleplay!) or a previously acquired method of silencing the order announcement and, if not in cargo, retrieving the order.

A simple example of this is that, while you may think the head of personnel's uniform printer would make a good bounty target, it's value as a secured item is undermined by the circuit imprinter's ability to make more from roundstart.

Another important part of picking targets is ensuring that they will not cause *unmitigable issues for the station*. Bounty targets should either be not important for the station to function (e.g. a department head's special item or door remote: it is one-of-a-kind and provides a strong utility, but won't really cause serious gameplay issues if missing for a while) or, if it is, should almost always be replaceable (e.g. cargo's order computer, which not having would softlock the station...if it wasn't for the fact that the QM gets a spare board in their locker). Lastly, a target should *not* be something that is not intended to move (e.g. items that cannot be unwrenched like the crematorium, and structures that behave illogically when unwrenched due to being intended as static wall fixtures).

Following these rules, some valid targets in rough difficulty order include: holopads, microwaves, vending machines, RCDs, substations, departmental request computers, disablers/stun batons, door remotes, the deckard, special department head items, ID computers, communications computers, the security techfab and the warden's energy shotgun.

## Administrative and Server Rule Impact
Spies should follow the same rules as other minor solo antagonists. In short: no mass station destruction, no deliberate round removal of players who are not your kill target *including other spies* (although violence without escalation to achieve a goal is allowed, given the victim is recoverable), and no over-escalation beyond the scope of your objectives. Bounty targets and completion rewards should prioritise reflecting these guidelines, and should not tempt spies with gear that is overly capable of mass sabotage, destruction or murder.

Subtext surrounding the antag should strongly hint that other spies are present and you should be distrustful of others, to hopefully dissuade situations where unaware spies become frustrated/create ahelps relating to being backstabbed or otherwise bested by another spy.

A space law rule may need to be added that states that crewmembers not in custody are entitled to a PDA, to prevent or at least heavily discourage situations where security forbids a known spy from being given a new PDA as a deliberate move to shut them down forever.

On servers with no metashield where security is aware of the existence of spylinks, security may interrogate a suspected spy in custody in an attempt to make them to give up the code, potentially in exchange for a lighter sentence. However, threatening to or attempting to prolong a spy's sentence until they give up the code would already be in violation of brigging procedures relating to prolonging prisoner sentences without an urgent reason.

Cargo techs rushing to purchase the minor syndie orders off of the roundstart black market may arise as an issue, but should be dealt with in the same manner as a cargo tech wasting budget trying to order guns for cargo.

# Technical Considerations
Many features here should function similarly to existing features: the method of unlocking a spylink is almost identical to that of an uplink, the bounty board itself should be very similar to the cargo bounty console UI, the black market would simply be a new tab added to cargo orders with an accompanying system to only pick a limited number of starting entries from a pool, and claiming bounties should grant items to players in the same way that an uplink purchase does. The process of interacting with an entity to eventually steal it would need to be entirely unique, likely rendering a similar overlay as the holopad hologram filter over the entity.