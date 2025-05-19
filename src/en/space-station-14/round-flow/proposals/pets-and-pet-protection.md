
# Pets and Pet Protection


| Designers      |Coders| Implemented | GitHub Links |
| -------------- |-| ----------- | ------------ |
| FairlySadPanda |FairlySadPanda| :x: No      | TBD          |

# NanoTrasen Believes In Your Emotional Support Needs

After several instances of our research station employees experiencing the unfortunate side-effects of severe emotional isolation, we at NanoTrasen Animal Research and Cloning (A.R.C.) are proud to announce our all-new mental health initiative for NT staff: cute, fluffy animals!

Research has shown that providing emotional support animals to crew-members in need of friendship (or a parent-child relationship) is 46.3% cheaper than the cost of providing actual psychiatric treatment or replacing failing crew-members with obedient robots.

To fulfil our aggressive quarterly targets and prevent needless destruction of company resources, A.R.C. now provides a range of pets to staff deemed at high-risk of common problems like depression (the HOP), psychotic rage (the CMO) or alcohol abuse (everyone else).

Be aware: NanoTrasen takes a dim view of your personal pets being mistreated, maimed, thrown into singularities, or traded for illegal contraband.

Oh, and take care of Pun-Pun. He's a good monkey.

# Overview

Pets have been a part of Space Station history since the early days of Space Station 13. Over the years, many different pets have been added (and removed from) the game. Sometimes, these pets have complex mechanics and involved gameplay. Sometimes, it's just Smile the Slime.

For a long while, Space Station 14 has had a "feature freeze" on new pets, for the following reasons:

1. Every new pet is a new set of YAML prototypes to maintain. If pets don't do anything immediately interesting, they end up having to be maintained for little tangible gameplay benefit.
2. Each new pet has to be mapped (or deliberately not mapped) onto each space station map.
3. Each new pet has to be assessed for balance, especially if that pet is made into a ghost role. This is often slow.
4. Once a pet is mapped onto the station, it contributes to the overall population of the station. This leads to stations feeling more crowded than they should be.
5. Pets are conceptually very easy to add, but become very challenging to remove as players get used to them. There's something about 32 pixels and a name that makes players fall in love with the lil' guys.

This design document outlines a proposal to lift the pet freeze by moving pets over to becoming loadout items, unlocked via playtime for various job roles. In addition, it outlines gameplay mechanics that encourage players to role-play owning and taking care of their pets. Afterwards, it outlines the principles behind pet ghost roles and when a pet should be unlocked for late-joiners and the recently deceased to play. Pet Carriers are discussed, and we then dwell for a short time on the Captain and Head Of Personnel's pets and their gameplay importance. Finally, it covers the unique trio of pet-crew ancestors (Pun Pun, Kweh Kweh and Wa Wa), their purpose in gameplay, and their unique circumstances as Junior Assistant Bartenders.

## Player Profiles

- **Cutesy Gamer** wants to play as a cute critter attached to someone they have a reason to have interactions with.
- **Thoughtful Role-player** wants their character to have more of a connection to the universe and more ways of expressing their (lack of) capacity for responsibility.
- **Green-text Enjoyer** wants to get that sweet, sweet green-text at the end of the round, and enjoys being challenged in creative ways to secure that green-text.

## What is a Station Pet?

Station pets are creatures such as Hamlet, Ian, Exception, Runtime, Smile, Renault, Shiva, Pun Pun and Walter.

Station pets do NOT include disposable animals like mothroaches, rats or (most) monkeys. It does also not include more exotic creatures like gorillas or Willow the Boxing Kangaroo. These should be designed as part of the (as yet missing) Zookeeper job role. In Willow's case, their rivalry with the station's boxers probably would require a design document of their own.

Station pets also do NOT include "summoned" pets. This include's the Chaplain's bat. Animals like these are better suited to a document covering crew magical abilities.

## How Should Station Pets Be Played?

The admins currently follow the following rules for determining how station pets interact with the crew:

```
Currently pets, such as Ian, Slime, and Renault, while not considered crew, still have certain protections from the rest of the crew. Crew cannot kill them without a reason, although they can justify killing a pet or otherwise harming it with much less justification. Additionally all members of the crew can have "attachments" to pets, as such harming a pet can count as escalation against crew members that care about that pet. Obviously, the Captain may care much more about Hamlet or Renault than a random janitor.
```

Although design proposals shouldn't touch on roleplaying or "the setting", station pets are sufficiently strange to require some design notes to support the above admin ruling.

Role-play interactions as station pets is **not strictly defined on LRP *or* MRP servers** - Ian might be as smart as Lassie or as dumb as an actual corgi. However, it is objectively funnier if a station pet (when piloted by a player) is able to play under the rule of "Pokemon logic". That is, they are about as smart as the crew, and the only thing holding them back from their rightful place as a Head of Staff is their unfortunate stature and lack of conversational ability. Station pet gameplay should be designed with this loose rule in mind.

The crew have no requirements to see station pets as anything other than dumb animals. However, due to their ownership (and the green-text mechanic) being known, it is not acceptable for a Chef to shove Hamlet in the microwave for no good reason, and should only do so under duress, at the risk of traumatizing the Captain.

All pets should be designed with the above in mind: pets that over-encourage griefing the crew, and pets that can only interact in ways likely to cause escalation, need to be transitioned to having more neutral or mildly-positive effects.

For the unique circumstances surrounding the Junior Assistant Bartender, see their section below.

# Pets As Loadouts

Pets are not mapped directly onto the station. Instead, each role may have at least one pet assigned to it via its loadout. Much like other loadout options, pets are unlocked via playtime.

When a role has a pet as a loadout option, that role will have a mapped pet spawn location on the station. If it does not, the pet will spawn as if the role spawned as a late-joiner (see "Joining Late with a Pet" below).

Most pets are optional. For example, a Head Of Security might not like any of the pet options they have unlocked, or might be roleplaying a character who hates animals.

Most pets are not required to exist inside the round. These are Optional pets.

Some pets are required to exist inside the round. These are Mandatory pets.

## Pet Spawn Priority

All pets spawn according to the rules below.

Almost all pets are considered a singular pet spawn. The only known exception at time of writing is Exception and Runtime, who are one "pet" for the purposes of spawn logic.

### Mandatory Pets

A Mandatory pet will always spawn, even if their associated role does not spawn at round-start. Mandatory pets include:


| Role              | Mandatory Pet Choices         |
| :---------------- | ----------------------------- |
| Captain           | Hamlet, Renault               |
| Head Of Personnel | Puppy Ian, Ian, Lisa, Old Ian |
| Bartender         | Pun Pun, Kweh Kweh, Wa Wa     |

Mandatory pets are spawned at round-start based on the following steps:

1. If at least one player from their associated role has spawned, a random player from that role is given priority. If no player with the role has spawned, skip to step 3.
2. If the player with priority has selected a pet, that pet is spawned and this workflow ends. Otherwise, randomly pick another player with the role who has not been given priority already, and this step is repeated. If no other player can be given priority, skip to step 3.
3. The spawn chance weights of each of the Mandatory pet choices for that role are used to randomly select a pet. This pet is spawned.

For example, if no bartender has spawned, Pun's weight might be 0.5, Kweh's weight 0.3 and Wa's rate 0.1. This would give Pun a 5/9 chance of being spawned, and Wa only a 1/9 chance.

Mandatory pets spawn in pre-mapped locations, inside their Pet Carrier.

### Optional Pets

Optional pets are spawned at round-start based on the same steps as for Mandatory pets, with a different step 3:

3. No pet is spawned.

Optional pets spawn in their owner's hands, inside their Pet Carrier.

#### Examples of Optional Pets By Job Role

This is a non-exhaustive list.


| Role                  | Optional Pet Choices        |
| :-------------------- | --------------------------- |
| Chef                  | Alexander                   |
| Research Director     | Smile                       |
| Chief Medical Officer | Exception & Runtime, Walter |
| Chief Engineer        | Tropico, Polly              |
| Quartermaster         | Morty, Morticia             |
| Librarian             | Paperwork                   |
| Janitor               | The Moproach                |
| Head Of Security      | Shiva, McGruff              |

**Note that the above includes some Heads gaining pets that are traditionally assigned to their subordinates**. This is intentional to reduce the number of pets on station. In general, outside Service, each department has a singular pet choice per-round.

## Joining Late With an Optional Pet

If an Optional pet has not been spawned for a role during the round, the first player to spawn with that role is given priority to spawn a pet. If that player has chosen a pet to spawn with, that pet always spawns in a Pet Carrier in one of the player's hands. If, for some reason, the player is unable to hold the Carrier, the Carrier spawns at their feet instead.

If the player had not chosen a pet, the next player to spawn with the pet's job role will be given priority. This will continue throughout the entire round if necessary.

# Crew Objectives To Keep Pets Alive

When a pet is spawned due to a player spawning with that job role, that player is given an objective in their mind to ensure that the pet escapes to CentComm alive.

This role should always match the equivalent "escape to CentComm alive" rules that antagonists use.

The objective to ensure the survival of their pet is removed if the player is made into an antagonist **other than a Thief**. A Zombie or Traitor has no interest in keeping their pet alive. Likewise, if a player is made into a Survivor, considerations about their pet's wellbeing ceases to be their chief concern, and the objective is removed.

If a Paradox Clone duplicates a player with a crew objective to protect that pet, that objective is inherited by the Clone.

For safety, a player may choose to load their pet into a Pet Carrier, buckle them to a bed or a seat, or any other method to prevent their pet from jumping out the escape shuttle mid-flight. As long as the pet is alive when arriving at CentComm, the player will green-text.

The exception to this is if the pet has fulfilled a steal objective for an antag, such as the Thief or Traitor. For these antagonists, they must directly be holding the pet in their hands, a Pet Carrier, or other storage on their person.

A player is NOT told if their pet has died. In the very rare circumstances where a pet has died and been cloned or duplicated, the clone DOES NOT count towards green-texting. Zombified pets do NOT count toward green-texting.

With one exception, all pets only have one "owner" and only one player will have an objective to keep that pet alive. For the exception, see the "Junior Assistant Bartender" section below.

# When Should A Pet Be A Ghost Role?

Pets should only be a ghost role if they match any of the following circumstances:

1. The pet has a unique gameplay gimmick that would be appealing to a ghost to play as.
2. The pet was historically a ghost role in Space Station 13 or a Space Station 14 downstream, and it would be sufficiently disappointing to players if the role was removed.
3. The pet is the Captain's.

Examples of pets that may be a ghost role under this design rule are:


| Pet                       | Why                                                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Hamlet                    | He can run under doors, be places they shouldn't, and eats everything on the station before being shoved into a microwave. |
| Renault                   | She's more durable than Hamlet but can't move around the station easily. A guard-fox for the bridge.                        |
| Polly                     | She can repeat anything she's heard and can fly.                                                                           |
| Pun Pun, Kweh Kweh, Wa Wa | They're a job role!                                                                                                        |
| Shiva, McGruff            | Supporting security in fighting crime.                                                                                     |
| The Moproach              | Helping the Janitor(s) clean spills.                                                                                       |
| Smile                     | Grandfathered.                                                                                                             |

# Pet Carriers

Pets always spawn inside a Pet Carrier.

Pet Carriers are a secure place to place pets out of sight. They also provide the perfect vector for stealing pets, as they do not allow outside observers to see inside.

It should always be reasonably possible for a player with an objective of keeping a pet alive to find a Pet Carrier for them. Pet Carriers should spawn as maintenance loot and be fabricatable via a lathe, possibly after a research tech unlock.

Pet Carriers protect the pet inside from harm, including loss of atmosphere, radiation, and other things that would be unfortunate to their health (such as shuttle bombings).

A Pet Carrier can be locked, preventing exit. This lock is trivial to remove from the outside, even by a station pet.

A pet inside a locked Carrier can break out of the carrier after attempts, unless the lock is reset.

If a pet is not being controlled by a player, it may randomly attempt to leave a out of a Pet Carrier it is inside unless that carrier is being held.

In general, a pet can rely on a Pet Carrier to protect themselves against anything other than a direct hit from an explosion or something Very Bad happening to Space Station 14.

# Hamlet And Friends

The Captain's pet is Mandatory. The Captain must choose from one of the following options at the start of the round.

* Renault
* Hamlet

Unlike other pet loadout choices, both of these options are available to the Captain as soon as the role is unlocked.

All Captain pets contain 5 TC that can be looted if the pet is butchered. All Captain pets are ghost roles.

Renault is a fox who guards the Bridge and the Captain's office.

Hamlet is a small bundle of furry chaos, a guaranteed ghost role with an insatiable appetite and an inability to be stopped by mere doors.

Historically, both Renault and Hamlet are mapped onto Space Station 14 maps. This has been specifically changed to encourage more design focus to be placed on both pets, in particular Renault, and to actively help to reduce the pet count.

# Ian And Friends

Ian is the most iconic pet in Space Station 14 and is Mandatory.

The Head Of Personnel must choose one of the following Ians:

* Puppy Ian
* Ian
* Lisa
* Old Ian

Puppy Ian is the first Ian a HOP unlocks. Veteran HOPs ergo have access to a more veteran Ian.

# Junior Assistant Bartenders

NanoTrasen space stations are always a strange place, but one of the most obviously strange things about them is their bars, which always seem to have some critter trained to serve drinks. Some of these critters are experiments, others are unusual aliens just taking the best job they can to stay alive. In all cases, the Bartenders of Space Station 14 are glad for the company, the extra hand in making drinks, and someone to talk to when the shift gets quiet.

Junior Assistant Bartenders are a Mandatory pet. They are also the only station pet that also counts as crew, both to silicons and other crew-members.

Junior Assistant Bartenders always spawn with the following equipment:

* A top hat
* An appropriately-sized barkeeping outfit
* An ID card

Unlike other station pets, **all** Bartenders are given a crew objective to keep the Junior Assistant Bartender alive.

The role of Junior Assistant Bartender is a role a player can select preference for, and select off of the late-join list. Observers may also raffle to join the game as the Junior Assistant Bartender as usual for ghost role pets.

The most senior Bartender on staff can pick from the following options:

* Pun Pun - voted 'most likely to become Captain' by a census of the station's alcoholics, this monkey may well be the most veteran member of staff working in NanoTrasen's research division. They are also individually responsible for ten percent of NanoTrasen's consumption of tequila. Ook!
* Kweh Kweh - a grey kobold with a love of warm liquor and fireside schnapps. A recent arrival at NanoTrasen, it has a fierce one-way rivalry with the other Junior Assistant Bartenders, and looks up to the station's Lizard population. Kweh!
* Wa Wa - a scurret with fur as white as snow and huge eyes as black as midnight. After a successful temping job on Space Station 14, this scurret left their tribe on Planet Wawa to become the first scurret employee of NanoTrasen. Wawa!

### A Note On Ancestor Pets More Generally

Pets, outside the Junior Assistant Bartender, are assumed to be creatures that lack hands. They _may_ be capable of dragging things, or even wearing a small container for moving items around. However, ancestor species always have one "hand", reflecting their diminished size. Ancestor species are a significant power-creep over normal animals, and *should be avoided* as station pets without being backed by a very strong idea. We would welcome a future design document for ancestor species more widely.

# Technical Plan

This plan is a series of simple YAML changes, some refactor of loadout code, some mapping alterations and the creation of a "crew objectives" system that supports crew members being able to greentext via doing tasks during their shift. As noted above, the only task we care about for this document is keeping their pet(s) alive.

## Step 0: Review and refactor loadout spawn logic

1. Review current loadout spawn logic to make sure it is fit for purpose and that the new spawn logic for pets does not further decay the code.
2. If decay is unavoidable, work on paying off technical debt until step 1 can be started.

## Step 1: Junior Assistant Bartender

1. Add Kweh's prototype.
2. Add the scurrets species prototypes and resources.
3. Add Wa's prototype.
4. Randomly choose between Pun, Kweh and Wa each round.
5. Add being able to round-start as the Junior Assistant Bartender.
6. Add crew objective to bartenders to protect the Junior Assistant Bartender.
7. Review current Junior Assistant Bartender balance and resolve any lingering concerns/ideaguying.

## Step 2: Mandatory and Optional Pets

1. Add support for selecting a pet roundstart, similar to selecting other loadout options.
2. Agree with maintainers and project management what responsible playtime requirements should be used.
3. Enhance pet carriers with specified functionality.
4. Migrate mandatory pets to new spawning system (excluding the Junior Assistant Bartender, who was migrated in step 1)
5. Migrate non-mandatory pets to new spawning system.
6. Review mandatory and non-mandatory pet balance and review the code freeze on new pets.

## Step 3: Document and Review

1. Document implemented design for historical record.
2. Conduct review meeting and retrospective about learnings and opportunities for future code refactors exposed by this work.
