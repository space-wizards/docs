# Revolutionaries Rework (but way simpler)

| Designer | Implemented | GitHub Links |
|---|---|---|
| Mehnix | :x: No | TBD |

## Underview

Lots of people like having opinions of revolutionaries, considerably less actually seem to make things for them. This is probably because many suggestions, such as the prior "One rework to rule them all" https://github.com/space-wizards/docs/pull/309 require a lot of work to implement. Considerable reworks to the game have not exactly been wizden's speciality. That doesn't mean we can't steal ideas from it. The fundamental principles like avoiding round removing and avoiding single-failiure outings are good ideas so they won't all be reiterated here.

Regardless. Rather than looking for a theoretically perfect solution that requires a massive amount of time and that would probably never happen, a decent solution that requires orders of magnitude less effort might be a better target. AKA: What can we make with what we have?

This proposal tries to keep things simple, that is its core philosophy. Suggestions that attempt to soap it, balloon the scope or complexity, or so on won't be particularly useful. No fundamentally new ideas, just shuffling around old ones to a new shape. 

## Overview and Breakdown

Revs is the "Potential Man" of antags. When it works its is absolutely badass to ride the wave and be part of a massive group of people unified under a single banner of VIVA.
Problem with it is that requires a lot of things to go right. You probably need some of each of the following:
- **A Head Rev that *really* knows what they're doing:** Someone that has the power to move effortlessly between groups, keep the masses focused on a goal, to drag people to action, and a concrete plan. Captain material, that's basically what you are after all.
- **Favourable External Circumstances:** Cargo has cash and materials, there are a few decently competent crew to aid the head rev, a few power players around like a thief or a syndicate agent to fund the revolution, Security/Command doesn't happen to be in the wrong place at the wrong time to kill the revolution in its infancy.

Let's try and dissect each of these.

### The Head Revolutionary

Let's first look at another very swingy group antagonist, Initial Infected (II). Ultimately a single II in the right place can by themselves win the entire round. II benefits where revs does not that it only remains an antagonist centralised around a few people until the infection begins spreading. The II zombie is no different from the zombie the II infected, even if every II dies the infection can live on without them.

The Revolution meanwhile is an antagonist that relies very heavily on its Head Revolutionaries from start to finish (which, for some reason, is a role that only requires a single hour of playtime to unlock). If the heads cannot dictate the crowd and nobody sufficiently badass steps up it will fizzle and die into an endless loop of "preparation" until the shuttle gets called or people get bored and a half hearted "REVS GO LOUD" gets spurted over the radio. If security sees a person flashing they can decapitate that one person and deal a crippling blow to the entire revolution. Their significance is more akin to the Mothership core or nuclear operatives, unlike both of these they have no special tools but a magic flash and a (questionable) wall of bodies.

The key problems:
- **Communication** Revs have no reliable communications method, comms are all monitored by the captain and AI, they cannot talk about rev stuff over comms in a way that isn't going to sound really suspicious. Most head revs, knowing their own fragility will not even try. Therefore, all communication must be person to person. As everyone is spread out over an entire station this means the Head Rev is effectively having to run around trying to keep the mob organised, or hiring others to do that. This often leaves the recently converted clueless as to what they're supposed to do, as the Head Rev is being pulled in too many directions to stop and give orders to everyone. They're not likely to have luck asking anyone else, who probably won't know either. The revs should have a better way to communicate.
- **Fragility** The flash being the only method of conversion, your need to be everywhere, your death potentially spelling doom for the revolution. A lot rides on the head rev. Ways to lighten their load and better let the revolutionaries support their heads is a must.

### The External Circumstances

The "Theme" of revolutionaries often has them using the tools of the station to uproot their oppressors. This is good themeing, but suffers from most makeshift equipment being not great by design. Your alternatives for getting something better?
- Kill a secoff? Sorry you took too long they screamed out on the radio and now everyone knows.
- Raid Cargo? Sorry they didn't have any money.
- Materials? Sorry salvage all died.
- Get a bunch of people to change jobs to try to fix these? Sorry HoP says no.
- Raid the Armoury? Good luck

The Revolution is more than any other antagonist prey to the whims of external circumstances. Random circumstance is interesting from a crew perspective, you don't know whether your shift will be a chill one or ten trillion dragons, lone ops, and ninjas will make it a battle for survival. It is less interesting as an antagonist to find our you are being limited by circumstances you have little control over. Revs are rare after all.

Beyond this, whilst a makeshift revolution has its benefits, it is also limiting from a balance and gameplay perspective. It is difficult to inject any content into revs specifically because they have no vector to receive it. You're probably never going to have a makeshift cyborg converter, so as a revolutionary you have to hope a thief or syndicate agent is around to convert borgs to the revolution, who are very powerful allies.

The key problems:
- **Resilience**: Rev's reliance on external circumstances results in a lack of resiliency, it is difficult for them to bounce back from a major loss or deal with secondary factors. They will rarely be the only dangerous force on the station. It would be very beneficial for them to have their own way to tip the scales.
- **Variety**: Everything on the station is a tool for the revolution, but the station has plenty of things it cannot do and the best things it can do are usually locked behind people that would want to kill you. A larger variety of specialised tools for the revolution would add more spice to the gamemode, these do not have to be revolutionary exclusive.

## The Theme

Quick mini-chapter before the meat. It's good to nail down a theme to build around. It gives a sense of what feels and doesn't feel right. Some examples:
- Initial Infected are Cultists/Terrorists/Viral Puppets sent to kill the station, they're just random nutjobs.
- Nuclear Operatives are Highly trained and well equipped kill-teams with a laser-focused objective.
- Xenoborgs are a splinter of a hyper-advanced machine-mind here to harvest the station of its power and sapient minds.

- Revolutionaries are...?
The most common theme seems to be they are the people's antagonist, unionists, proletariats, etc rising up against a tyrannical leadership using anything and everything they can find to bring down the man. Very much in the theme of the French and Communist revolutions.

This proposal *slightly* alters this theme to also include idea of an armed insurgency. A questionably trained militia formed in opposition of a leadership they despise. This functions just fine with the existing theme but is important to distinguish. One key element many historical and especially modern insurgents have is *External Help*.

This is something already thematically baked into Revs, albiet overlooked. The Syndicate are specifically sponsoring the Head Revolutionaries with their flashes. The revs do not need to fight their war in a (thematic) vacuum, plenty of groups hate Nanotrasen, and would love to fund ragtag group of rebels wanting to take them down.

So the theme of Revolutionaries per this document is: *A set of common men and women of the space station, seeking to convert the masses to their cause and overthrow the station's leadership with the aid of covert backers to whom they must appeal for the aid of.*

## Proposals

That was a lot of words. Let's do some actual proposing now to address these points.

### Communications
This one's conceptually simple enough. Revs should have some way to talk to each other covertly. Xenoborgs and Nuclear Operatives get it for free, Syndicate agents get it for 2TC at some codewords spamming in the Common channel. The captain gets all the crew channels round start for free, plus a spare.

Naturally, revs are none of these antagonists. It doesn't really hit the right theme to just have a magic comms channel that always works. The Revolution is fundamentally internal, so their comms should be too. 

The current concept draws heavily from modern communication methods like the Telegram App, obscure forums, or hidden messages in a newspaper. Effectively "Hiding in plain sight" using the establishments own communications systems against them with messages they can't see. But that the establishment can try to counteract through heavy handed suppression.

The "Undercommon" Radio Channel exists parallel to the Common channel, it consists of subliminal messages, static, and other nonsense background noise that those not tuned into the revolution will not notice. To the revolutionary, they can speak and pick it out as if it were second nature. As long as the Common Channel exists, revolutionaries can speak and hear Undercommon.

Undercommon is available immediately with no setup, all crewmembers who have a headset that can hear common can by extension hear undercommon if they are a revolutionary. If they aren't, they can't even see the channel in their headset. Here's the justifications for that:
- Adding required setup places more pressure on the Head Rev and another thing they need to think of right off the gate.
- Some level of two way communication must be possible, a head rev that asks their revs to perform a task but that cannot hear a reply cannot properly command. Imagine the frustration of being a command member when your crew don't respond to your requests, now imagine if they where not capable of responding...
- At bare minimum, if undercommon started as only head revs able to speak, there would need to be a consistent way to acquire Undercommon encryption keys that allowed two-way. For example, a way to craft it.
- Security being able to listen to the undercommon channel basically kills it stone dead. It's generally disapproved for security to spy on the Syndicate Channel because it immediately outs anyone using it. Same applies here but worse, this implementation just makes it impossible.

Undercommon by design allows for mass dissemination of information, with proper two way this takes a load of the head revolutionary's back. Tasks can be better offloaded, people checked up on, and information about the state of the station better known.

### Resilience and Variety
Slightly more complicated. As described in their sections, revs are vulnerable to the whims of the station. The proposed solution to this one is a way for them to acquire goods outside the station's normal ways, but still functioning within them, similar to how communications are linked to the station.

*The Black Market* is a cargo account that fundamentally works very similarly to the existing ones. It has access to a cargo market of things that revolutionaries can buy. Unlike the regular civilian market however, the black market has more limited options, but, it also has some contraband and revolutionary specific items they can buy. This shop is not intended to work like a Syndicate Agent's uplink or Changelings DNA store. It should not be the primary way of progression. Instead, The Black Market is intended to be supplementary.

The Black Market basically acts as the way revs can tip the scales. If materials are in shortage, they can buy some from the black market. If they have a good base set up, they might want to buy a contraband ammo fabricator to resupply whatever weapons they've managed to scrounge up. This would also be where the thematic change to revs comes in. The Black Market is meant to be the primary vector by which the revolution receives supplies from their nebulous backers. 

The revolution does not use spesos to purchase its goods, instead, it earns favour from their backers through conversion. This amount earned can vary depending on the converted. Converted Security officers or Command members can offer more earned favour, encouraging them not to be round removed due to the loss of bonus rewards.

The Black Market would be accessible by any revolutionary via a Black Market Telepad, which would include its own request console. Although to prevent complete anarchy it would likely be a good idea for Head Revolutionaries to have a digi-board and sole permission to approve orders. Although if this digiboard wasn't connected to the telepad it would instead send to the ATS. Ideally all purchased goods would come in covertly disguised containers and not marked as "THE BLACK MARKET". The intention of this also means if security smashes the telepad you still have backups to buy things as long as one Head Rev isn't dead.

The Black Market also acts as the gameplay vector for adding fun tools to revs. Such as those from prior proposals. It may also be possible to make it so certain items unlock depending on the number of conversions, similar to how Salvage Jobs unlocks new items in the market depending on jobs complete.

This store implementation is intended as providing Resilience and Variety to the Revolution.

### Fragility
Communications and the Store are both very useful tools for reducing the fragility of the Head Revolutionary. It's no longer as neccessary for them to run around as much and they have more tools at their disposals. However some more can be done.

Here are two smaller, interconnected proposals:
- *Alternative Conversion Methods:* Flashes are innately associated with rev conversion, some alternatives, or more simply, additions would be useful. Here's a few suggestions:
    - Injectable devices that convert a person, like an anti-mindshield. Covert, but you can only get more by buying them from The Black Market.
    - Consumable Books, craftable and one use, forceably stuffed into a peron's face to convert them. Very cheap, bit slower than a flash.
    - Advanced book, like the last one but usable infinitely, bought through the Black Market.
    - Defib that converts you the instant you're revived (stolen from the last proposal)
    Basically, if you have enough alternatives, using flashes is now a choice rather than a neccessity, and therefore so is the risk.
- *Head Revolutionary Starter Kits:* This is mostly like the thief kits. They give head revs a set of starter tools to get things rolling. The kits would either be a conversion vector, or equipment. Head Revs can choose two. They could choose two conversion vectors or two equipments if they wanted to. All Head Revs would get a digi-board at minimum so they always have access to the black market.
    - The Classic, A 5-use flash and covert sunglasses that show job icons and mindshields, a viper and spare mag.
    - The Fixer, A box of 6 micro-syringes that convert on injection and some medical equipment.
    - The Proselytizer, Advanced Revolutionary Tome, a stun stick/taser.
    - The Merchant, A Black Market Telepad, bonus favour, and basic tools.
    - The Everyman, A Chameleon Clothing kit, fake mindshield, jaws of life.
    - The Voice, A Master Encryption Key, Voice Mask, Camera Bug, (if relevent, Box of Undercommon Encryption Keys).

Head Revolutionaries can communicate before choosing to best optimise their loadouts and choose how they're going to play. One might decide to bunker down and create a base of operations, choosing the Proselytizer and Merchant, Someone prefering a more manegerial playstyle may wish to take the Fixer and Everyman, disguising themselves as a paramedic to covertly inject key targets.

Some additional starting equipment helps get revolutionaries off the ground.

### More Variety
The prior entries represent the baseline for improvements to Revolutionaries that are relatively simple to implement. If these were implemented and proved successful, there would be opportunity for more advanced game mechanics to build upon.

One aspect that this proposal does not directly address is the arbitrary "preparing" that often happens during revolutions, where a revolutionary, not knowing what to do, basically just continues doing their job as normal with the potential of stockpiling whatever they think is useful in the hope someone else gives them direction.

Whilst comms provide better guidance, it's unlikely to remove this behaviour. Therefore a more advanced mechanic could be introduced stealing from the idea of Salvage Jobs and Bounties. These being *Revolutionary Duties*.

This would effectively be performing jobs for the revolution's backers in exchange for favours. Ranging from "Acquire thing" to "Kill person". The intention being for head revs to delegate these jobs to their underlings to provide them things they can do to help the revolution. The vaguely clueless intern in medical who's on their third ever shift probably doesn't know what to do during a revolution but if they were given the task to inject a security officer with a covert implant that made them blow up, they could probably figure that out and give the revolution some bonus favour.

This would require considerably more work as it is in effect a form of "Progression Traitor" where a series of objectives are picked out and completed for rewards.

## Conclusion
This is a basic set of additions to revolutionaries. Currently a basic form of Undercommon and The Black Market have already been created. This helps to justify I made them they way I did.