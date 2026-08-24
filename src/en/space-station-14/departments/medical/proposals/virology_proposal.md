# Virology

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| SeaWyrm | SeaWyrm | :x: | TBD |

<!-- In either case you will have to write an outline on how you plan to implement this feature in the **Technical Considerations** section to show that is technically sound and feasible. -->


## Overview

A take on how virology might be re-added to the game in a way that has depth and is interesting and enjoyable for everyone.

Basic principles:

* Diseases should be interesting to catch. They should drive gameplay and roleplay decisions.
* Most diseases should be minor, and possibly ignorable.
* Nevertheless, diseases should present in a way that doesn't immediately reveal how serious they are. Deciding if and when to go to medbay should be a non-trivial decision.
* Serious diseases are their own game mode, like Zombies. Otherwise, diseases should only become a major threat due to severe and prolonged neglect on the part of the players, and even then, only if they're unlucky.

* Diseases grow and spread based on station hygiene. If the station becomes utterly disease-ridden in a non-disease game mode, it should be entirely the players' fault.
* Diseases should not behave like "invisible health bars." They affect their victims entirely through symptoms.
* Diseases get worse over time, but characters' immune systems get better at fighting back until the disease is eliminated (or the symptoms kill the character.)

* Treatment starts with symptom management.
* Vaccine development requires legwork and decision-making: Virologists must track down infected people to get samples for their research. A round-start cure or a copy-pasted, routine solution is impossible.
* Diseases will mutate over time, becoming more dangerous and harder to cure.


## Features to be added

### Diseases 

Though every round should have a mild disease or two, these should usually be ignorable or at worst inconvenient, whereas a severe disease counts as a round-defining major 'antagonist' and should be its own game mode.

Janitors should be the station's first line of defense against contagion. Diseases show up at unsanitary locations or on unsanitary objects: Trash, spilled liquids, rotten corpses (but not fresh ones), spoiled food, grimy tiles, and so forth. Players should have some agency in their ability to avoid disease by wearing appropriate protection, (For instance: rubber gloves, surgical masks,) and by staying away from unhygeinic locations. If a player catches a disease, they should find out only when symptoms develop; symptoms are what make the disease interesting and interactive. There should be no direct "oh, I have a disease, better run to medbay" - instead, it will be a player's job to figure out when and if a medbay visit is appropriate. Initial symptoms shouldn't usually reveal how severe the disease is, either. A slight cough or sore throat might be the only symptoms they'll get, or they might be the harbingers of deadly plague. Usually, though, it should be the former. The balance should be such that a player who gets a disease shouldn't feel that running to medbay for every runny nose is the pragmatic option.

Diseases will not harm their victims directly. All damage will be a secondary effect of the disease's symptoms. For instance, a fever might cause the victim's body to heat up; it will not cause direct heat damage, though the heating effect might itself cause heat damage. This means that a patient with a disease can be treated with normal medical interventions to control the symptoms, and if the symptoms are kept under control, will recover naturally. This way, there is flexibility in how players can approach treatment, and also possibilities for emergent complexity: The disease that makes its victims heat up when the station is already overheating, the symptoms that compound with each other to create unique problems, and so on.

Viral diseases will require a vaccine to be developed. Bacterial diseases can be treated with antibacterials.

### Contagion

Contagion should come in multiple possible forms, so that determining how to prevent the spread of diseases by practical means is part of the detective work required. If a disease isn't airborne, then facial masks should be useless against it, for instance.

Diseases should be contagious before the arrival of symptoms in order to prevent incentivising game behavior that immediately shuts them down, such as anyone with a slight sniffle stuffing themselves into a biohazard suit so that they can't spread anything. They might still do that, but it's less of a binary spread/don't spread since they've already been spreading it for a bit.


### Symptoms

Symptoms should range from mundane to bizarre, harmless to gross to inconvenient to extremely dangerous, and from serious to silly. There should not be symptoms with solely beneficial effects. Either they're paired with significant downsides - yes, zombism makes you stronger, but it also makes you a zombie - or they shouldn't be beneficial at all unless by circumstance. (For instance, having a fever when the station is too cold.) Symptoms should, in general, feel like they're part of a disease, even if it's a silly one. They shouldn't generally be so extreme that they distract from regular gameplay - no disease that makes you spew particle or shader effects that flood everyone's screen, for instance, or that constantly spam loud and annoying sound effects, unless maybe it's a *very* severe disease in its very late stages - but they shouldn't be invisible, either, at least to the player that has them. Overall, simple is better than complex, and it's better to err on the side of subtlety, though subtlety should also be modulated by disease severity.

Symptoms should also be readable. If it's not immediately obvious what a symptom does to you and how you might deal with its effects, it should at least be straightforward to figure it out. There can and should, however, be symptoms that strongly resemble each other, so that it might seem like a player has one when they have the other; though even these should be possible to tell apart eventually or under the right kind of test.

Symptoms' annoyingness should also be considered part of a disease's severity. A typical mild infection should not, for instance, reduce someone's movement speed to a crawl, or make them repeatedly drop what they are holding. These symptoms should show up only in circumstances where a player has already had generous opportunity to identify and prevent them from occurring in some fashion or another, so that they are punishment for the player's failure, not an arbitrary this-person-in-particular-doesn't-get-to-have-fun-anymore. (Ideally, they should also not actually be so annoying or inconvenient that they ruin the player's fun.)

Though diseases should be generated randomly, and any combination of symptoms should be possible, they should ideally be weighted toward having symptoms that follow a common theme, or maybe a couple of themes. This helps them have coherent identities. Recognizing that certain symptoms are somewhat more likely to occur together, and preparing accordingly, also creates a way for medics to gain and use system mastery over time. The weighting should not be so strong as to prevent wacky nonsense combinations sometimes, and it certainly shouldn't be so strong that the exact same set of symptoms keep showing up together again and again and again. Diseases should be unpredictable more than they are predictable.


### Progression

Diseases should not be limited to just one symptom. As the disease progresses, more symptoms should be revealed. This is one way that diseases can worsen, and it ensures that just because a disease starts with a simple cough or sniffle doesn't mean it won't progress to something more serious. Obviously, diseases with more symptoms should be considered to have higher severity. That doesn't mean that disease progression necessarily *needs* to reveal progressively more dangerous symptoms, though. Mixing different symptoms keeps the disease unpredictable. Harmless but visually distinctive symptoms can add heightened drama by revealing that a character is without a doubt infected, or increase tension by heralding the imminent arrival of other symptoms. Inconvenient but non-dangerous ones can also compound with earlier symptoms to increase the amount of danger: A character who becomes unable to walk very quickly, for instance, might not be able to make it to medbay in time for their needed dose of whatever keeps their earlier symptoms in check, and a necessary chore turns into a dramatic struggle for survival. (Or possibly a farcical struggle for survival, which is also good as long as it's funny.)

Good symptoms, therefore, should have lots of potential to affect each other either directly or indirectly. Emergent symptom interactions can help make even well-known and understood symptoms combine to create a unique and memorable disease.

While progression shouldn't introduce symptoms strictly in increasing severity, the earliest symptom or two should be relatively mild. This is important for the sake of player agency: Players get a chance to react to having a disease before the disease takes full effect, rather than getting lightning bolt-blasted with serious symptoms out of the blue.

Symptoms should also be able to increase in severity themselves, either instead of or alongside the additions of new symptoms as the disease reaches new stages. A mild cough that turns into a hacking cough, for instance, or a light fever that becomes dangerous.

At least one symptom in the progression should reflect the severity of the disease; a disease that has five different symptoms that make the player's nose a bit drippy in each of five different colors and does nothing else is not a severe disease, despite having a lot of symptoms. On the other hand, a severe disease doesn't have to threaten the player's life. Dumping gallons and gallons of slippery snot on the ground everywhere you walk (no matter what color it is) should probably count as severe, even if there's no way to die from it. Enough crew members with that symptom, and any captain would be justified in calling evac immediately. Not to mention an emergency janitorial squad.


### Immunity

When a player catches a disease, their body immediately begins fighting back by producing antiserum. The disease's viral load will quickly ramp up and then taper off, while the antiserum will start off accumulating slowly, but build up until it can overwhelm the disease. How likely a disease is to kill the player before their own immune system can handle it is a big part of what differentiates serious diseases from mild ones: Mild ones will generally go away on their own, whereas serious ones will have both dangerous enough symptoms and fast enough growth that their victim is likely to lose the battle.

Antiserum is keyed to a particular disease. If a player catches more than one disease, they will begin producing a second type of antiserum against the second disease. This way, players aren't strongly incentivised to cultivate and catch mild diseases in order to build up their immune system against major ones. This also provides a simple and emergent way for players to develop immunity: The antiserum lingers in their bloodstream, making it harder for later infections to get a foothold.

"Lymph nodes" would be an appropriate organ to metabolize antiserum.


### Diagnosis and Treatment

The first step in diagnosis is simply observing and talking to patients to start to build a profile of the disease. Swab samples can be taken from patients and from objects and surfaces that are suspected of harboring diseases; the Disease Diagnoser Delta Extreme will take a swab sample and reveal if there is a disease present in the sample, and if so, whether it is viral or bacterial.

The first step in treatment is symptom management. Patients who are kept alive long enough will recover, so depending on the severity of the disease, this might be all that is required, if anything. Beyond symptom management, both types of diseases can be directly attacked in slightly different ways.

Bacterial diseases should be more common, and easier to treat. Doctors will have access to antibiotics that should be broadly effective against them. Strong enough bacterial infections might build up resistance to a particular antibiotic over time, requiring the doctors to use a different one. This makes chemistry a bit more interactive, since the chemists can usually just pick their favorite antibiotic to create, but might be called on to switch things up later.

There should probably not be more than, say, three different antibiotics, with enough difference between them that different circumstances might make one or another easier to produce, but without any particular one dominating the others. Chemists should not generally feel pressure to make more than one of them. Maints chemistry should strongly favor one, however; the downside of tider DIY antibiotics is that it's more likely to build bacterial resistance due to lack of variety.

In the case of bacterial diseases, some of the virology tools can still be helpful for tracking down the disease's source to eliminate it, possibly with some janitorial assistance for those hard-to-clean surfaces.

Viral diseases are more complicated, and are much easier to protect against than to directly treat after infection has already happened. The virologists will need to piece together the virus's genetic sequence as best they can. The most effective way to do this will involve some legwork and detective skills: Tracking down contaminated individuals, objects, and surfaces, and taking lots and lots of swab samples. Each sample will have fragments of the virus's entire genome. To reveal these fragments, the sample must be run through a new machine: The gene sequencer. This will take a little while - maybe 30 seconds to a minute, say - to sequence the DNA from the sample, though multiple samples can be queued up and run in parallel. The delay introduces downtime in the virology lab, incentivising virologists to go out into the station and gather more samples and information about the disease's spread. The ability to do it in parallel ensures that multiple samples taken together can still be useful. The gene sequencer, when finished sequencing, will present its results in the form of a set of chopped-up, unordered segments of varying length and completeness. Older samples will have shorter segments, fewer segments, and a higher likelihood of having unreadable or incorrect nucleotides. Contaminated sources might also have fragments that aren't part of the virus's genome.

The DDDE can take the data from the sequencer and manage it in a way that will help the virologist organize the information they have and offer some information about what the fragments actually do within the virus (see "Bioengineering" below.)

If the sample comes from a patient's blood, it will also have pieces of the patient's own DNA (the same code used by detectives) mixed in with the viral DNA. Virologists will have to sort out which fragments come from which source. Blood, incidentally, must be centrifuged and separated into components, one of which will contain the DNA sample.

One important part of this is that the virologists will have to take samples from a variety of sources, rather than a single patient over and over again. A single patient will only offer a single piece of the puzzle. They will also be incentivised to figure out the course of the disease's spread if they can, since the first infections will have the best data.

Virologists don't need to figure out the whole genome of the virus before they can start to produce treatment, but the closer their sequence is to the correct sequence, the more effective it will be. If the treatment sequence is too far off, it will either be ineffective, or downright harmful. They can also produce vaccines based on shorter fragments of DNA. The effectiveness of the vaccine is based both on how well it matches the viral DNA, and how long a sequence it uses; a vaccine based on, say, the single-nucleotide sequence "A" would match pretty much any virus, but would be basically useless. It's up to them to decide when their information is good enough.

Once the virologist has a promising sequence, they can take it to the vaccine generator, which will produce a small quantity of test vaccine. When a test treatment is determined to be effective, it can be sent to Chemistry for mass-production. Vaccines of course won't help patients who are already infected, but will prompt uninfected patients to start producing antiserum and thereby building up immunity.

The only real way to treat patients who are already infected with a virus, outside of disease management, is to produce antiserum, which can only be done in the blood of an infected living host (see "Bioengineering" below.)

For bacteria, petri dishes will be available. A petri dish can be swabbed, and any bacteria present on the swab will be loaded into the petri dish. Once enough time has passed, the petri dish will reveal the presence, amount, and number of different types of bacteria that have grown in it. Reagents can also be added to a petri dish to observe their effects on the bacteria - this is one way to check if bacteria have developed resistence to a given antibiotic. Petri dishes should be supplied to Virology, and possibly also Chemistry.

Petri dishes can break, spilling their bacterial load onto the ground. They will also contain agar, a food reagent that will transmit any bacteria growing in the dish to anyone who eats it. If there are no bacteria, it is harmless. Agar could also potentially be a component in food or drink recipes for chefs and bartenders.

Viruses should not interact with petri dishes.


### Recordkeeping

The vaccinator machine should automatically log all created vaccines to the medical records computer's database - something a would-be bioengineer will have to keep in mind if they're trying to be underhanded. Virologists can then use the computer to associate vaccines with patients they've been used on, similar to how the criminal records computer can be used to set crewmembers to wanted and so forth.

Swabs and petri dishes should accept paper labels, also.


### Mutation

Mutation rate is one of the things that can make a disease more dangerous.

Bacterial diseases can only mutate to build up resistance to specific antibacterial agents. They have no actual genetic code.

Viruses, however, can cause more problems.

First of all, as viruses mutate, they will drift from the original virus's genetic code, making treatment less effective. Second, as the code mutates, the disease's symptoms and stats will also change. At worst, this can introduce new, more harmful symptoms. For more serious diseases, virologists will have to act fast and continue gathering samples to stay ahead of mutations. Treatment based on the original genome will still tend to be most effective overall, since it will best match the widest range of possible mutations, but as a disease spreads, that initial genome will become less and less relevant as the separate instances of the disease mutate away from each other. Mutations might also make the disease less impactful, of course.

This also affects antiserum! A rapidly-mutating virus's genome might drift from what the victim's immune system is trying to fight to the point where the antiserum they've accumulated becomes useless. Only the most severe diseases should mutate rapidly, as this makes them both more dangerous to catch, and significantly harder to vaccinate against.


### Virology as a Role

Since an average round will require little to no action from virologists, the virology duties will fall under the responsibilities of existing medical staff rather than being their own role. Players especially interested in virology can still signal their interest by wearing clothes from the virology wardrobe, or by getting a different job title from HoP, or things of that nature.

It is the CMO's job to coordinate virology work and ensure that the available doctors are appropriately balanced between patient treatment and virology duties.


### Prevention

As well as helping prevent oneself from catching a disease, players should be able to use protective equipment to stop themselves from spreading it, depending on its mode of transmission. Aside from things like surgical masks and latex gloves, this could include, for instance, tissues or handkerchiefs for a minor disease that causes something like coughing or sneezing. (Anyone who leaves their used tissues on the ground is a bad person and should feel bad. Anyone who picks them up bare-handed is liable to contract whatever disease the person had.)

For cleaning surfaces, Space Cleaner should be somewhat effective, and bleach much more so - but less available. Janitors should not be immediately able to see how germ- or virus-ridden a given surface is, or else the upgrade path will be fairly pointless, since they can just keep spraying Space Cleaner until it's totally disinfected, and they'll have much less incentive to work with the medical department to find and eliminate disease sources, since they can locate them just fine on their own.


### Quarantine

Quarantine is fun, except for when it really, really isn't: Dividing the station up into "safe" and "infected" areas could lead to all sorts of interesting situations, and should be encouraged by giving the virology department a healthy supply of inflatable doors and barriers, as well as warning signs and holos to put up. Locking a given player into a tiny room for half the round should be discouraged, and isolated wards for sick people should probably not be provided. If they decide something like that is seriously needed, the station might consider repurposing genpop or something, in which case all the benefits of genpop over individual cells are in play at least.

Unfortunately, it would be difficult for any system where infections can be passed from player to player to not have some incentive for players to lock each other up.

For this design, it helps that diseases both have an incubation period where they can spread undetected, and multiple possible modes of transmission. Locking an infected person up still might seem like a good idea, but there are alternatives if the mode of transmission is identified, and it's less effective anyway since by the time symptoms show up, at least some of the damage is already done. The added uncertainty especially means that locking a particular person up is less undeniably a good idea, giving them more grounds to argue back or even justifiably resist.


### Bioengineering

For anyone who wants to dip their rubber-gloved arms into the dirty, grimy world of engineering their own viruses, thinking of a virus's genetic code as a mere string of letters is no longer sufficient. The code has to have meaning. The process of bioengineering revolves around unlocking that meaning piece by piece, and using those pieces however possible.

The first step should be the same as that for vaccine creation: Collecting samples. Would-be bioengineers shouldn't be able to sit around in a closed-off room any more than any other practitioner of virology. Once those samples are sequenced, the bioengineer should get imperfect information about each fragment's function in the virus's genome. Aside from the data being incomplete, fragments should also interact with each other to change each others' behavior, leading both to more emergence, more opportunity for interesting bioengineering results, and more difficulty in achieving a specific, desired result. Bioengineers will also have to factor out unrelated DNA from the sample's contributor, same as for regular vaccine development, or the information they get will be contaminated and innacurate.

Where vaccine creation only requires piecing the fragments into as complete a genome as possible, engineering is about taking the fragments and creating something new with them. Since they're limited to the fragments they're able to find, they probably won't be able to create exactly the virus they're hoping for. Instead, they'll have to figure out what they can do with the fragments they have.

To prevent gaming the system, the mappings between code fragments and effects should be random for each round. There might, however, be recognizable patterns or the like, allowing experienced virologists to figure things out more quickly. Ideally, there is room for skill mastery, but no room for bioengineering to devolve into copy-paste-this-genetic-code-to-make-superplague.

Once the bioengineer has come up with a genome they feel good about, they should be able to produce it in the vaccinator the same way a vaccine is produced. The only difference is the intent behind the genome entered into the system. This should not, however, be enough to create an actual disease: A vaccine isn't the same as a live virus. To make an actual disease, the bioengineer will have to extract the actual live, viral load from the vaccinator - possibly by disassembling it to get at an internal vial or beaker, making this step the one where someone up to no good is most likely to be caught - and then find a way to incubate it in a host body until it is strong enough to survive in the wild.

The easiest host body to use will obviously be the bioengineer's own. A would-be plaguebringer will probably have to suffer the effects of their own creation, making this process primarily the domain of those who would die a glorious death - though milder diseases should not be outside the purview of regular antagonists, or maybe even mischievous crew members if the disease is more or less harmless. A more cautious but slower approach would be to capture several live mice, for instance, though they will be harder to extract useful amounts of viral load from before they die.

It should not be possible to mass-produce live viral load the same way that vaccines can be mass-produced. The only way to do it should be to either find victims, or take the personal risk.

Viral load in the host body will be constantly attacked by the host's immune system, but just like antiserum, the viral load should be extractable from a centrifuged blood sample. The bioengineer can either use that directly, or release the host or hosts into the station at large once the disease is established in them and let the virus spread on the strength of its own contagion - depending of course on how that contagion itself has been engineered. An engineered disease with severe symptoms but little to no contagion might be an effective assassination tool. Or a needlessly complicated one.

Since antiserum is also extractable from blood, it should also be possible - in dire circumstances - to use this same process of deliberate infection and blood sample extraction to produce more antiserum that can be injected into disease victims to help them recover. Obviously, this should not be a better solution to the problem than developing a vaccine. Since the antiserum can only be produced in an infected person's body, and since the quantity of antiserum is dependent on how long the person has been infected, it's unlikely that it would be in most situations, though.


### Zombies and Romerol

The components of zombism could and should be picked apart and added separately as (rare, severe) symptoms and transmission modes within this system, possibly weighted to have a greater chance of occuring together. Romerol then simply becomes a particular strain of disease that causes all of the zombie symptoms together, suspended within blood. Zombie gameplay remains similar, in that the blood of zombies can be used by virology to help pin down the virus's genome and thereby develop a treatment. Initial Infected rounds, likewise, work basically the same way, with II players starting out with a certain amount of viral load in their bloodstream, a deficiency in antiserum production, and a particularly long time until onset of symptoms.


## Game Design Rationale

The ideal is for diseases to be interactive for everyone involved, to present interesting and meaningful decisions both mechanically and for roleplay, and to not arbitrarily limit someone's gameplay out of the blue: Getting infected is at least partially a consequence of a player's actions, and having a disease is often manageable with the right equipment or behavior.

An important part of this is that virologists don't get to just sit in their department and swirl test tubes or whatever. They have to get out there and track down the disease's source, which will generally require interacting with crew members as well as poking about in various parts of the station. 

On the flip side, having a disease doesn't automatically mean running to virology - most diseases won't have enough impact to be worth doing anything about other than to carry tissues and maybe take off a layer of insulating clothing. Even somewhat more serious diseases might be manageable with regular medication, or topicals, or just gritting one's teeth/beak/whatever and tanking it. This means that having a disease is interactive for the victim; they're not just an object for virology to deal with. They have to make their own decisions about how and if to address their own symptoms, balancing the possibility that they've contracted something horrible that will lay waste to the entire crew with the probability that it'll go away on its own and be no big deal.

The different modes of transmission also lead to decision-making for infected crewmembers, since they have to figure out what they can and should do to prevent spreading their disease to others.

Since diseases cause problems through their secondary effects, in the form of symptoms, and since people will tend to get over any disease they can survive, there's flexibility and room for creativity in how players decide to handle a disease. Some diseases won't even be harmful or fatal - just inconvenient, or ugly. In which case, the whole crew might just end up going about their regular duties while trying to ignore their dripping pustules leaving puddles of yuk everywhere they go. This helps foster emergence as well as making diseases more interactive for non-viro crew. A good variety of symptoms, with potential interaction between them, can lead to emergence in its own right - any disease might present some novel and surprising conjunction of symptoms with unexpected consequences for the crew.

Bioengineering presents mechanical challenge while limiting a player from creating perfect unstoppable deathplagues: They have to figure out what they can do with the pieces they've got. It's also not consequence-free for the bioengineer, since they'll likely have to suffer their own disease. Even bioengineered diseases will be different and unique from each other depending on what the player gets and what they do with it. Preferably, the genome code should also work in a way that allows for surprising and unexpected outcomes for the bioengineer themself, if they've done some guesswork or interpreted something wrong.


## Roundflow & Player interaction

In a regular round, there should be a constant, low chance for a mild disease to spawn as an event. These will gravitate strongly towards the filthier parts of the station, or possibly even fizzle if there's no sufficiently filthy place for them. The disease should on average infect one to a few people across the duration of the round from both its original source and from contagion, and should on average cause mild inconvenience at worst. The exact nature of the disease should be random, with at least some possibility that it will be severe enough for virology to take an interest - maybe one moderate disease appears every three to five rounds on average, say. Good janitorial coverage can reduce this. Extremely filthy stations, on the other hand, might generate extra diseases in sufficiently disgusting areas.

In a disease-focused game mode round, a severe disease should spawn, obviously. The only real difference between a severe disease and a mild one should be the numbers: Severe diseases can have higher mutation rates, a longer infection period before symptoms appear, faster progression once symptoms do appear, more serious symptoms, or most likely a combination of those. Like mild diseases, these can be created randomly, so that no two diseases are the same.

Diseases start out small and weak, then escalate through spread and mutation. A quick and appropriate response on the part of the crew - not just virology, but the whole crew - can stop the disease in its tracks. On the other hand, a severe disease (or a sufficiently-neglected moderate one) has the potential to lay waste to the entire crew and render the station downright uninhabitable if the crew can't stay ahead of them.


### Department Interactions

- Medbay will be the main defense against any serious disease. Not just through virology, but also through the doctors responsible for treating the symptoms; the chemists who will need to help produce and distribute treatments and vaccines; and the paramedics, who have to face the risks of going out into the infected parts of the station to recover downed crewmembers.

- Janitorial staff will also play a strong role, since their efforts to keep the station clean will help curb the spread of the disease or prevent it from coming into existence in the first place. (Also, if a disease causes projectile vomiting or something, their efforts will be doubly vital.)

- Security might have to be responsible for keeping a panicking crew in order, or stopping people from breaking quarantine. For a disease like zombism, they might have to more directly protect the uninfected crew from those infected.

- Command, likewise, might need to take charge of organizing the crew to act together against the threat of disease.

- Engineering could help with creating quarantine zones. Atmos could help especially against airborne diseases with scrubbers and holofans. They might also be able to do things like cool down the station if the majority of the crew have terrible fevers.

- Possibly, some symptoms could be worth research points to Science? Which might lead to some interesting conflicts of interest. They should also get some relevant technologies to research - faster disease diagnosers, bluespace sample swabs, better bio-suits and the like. There could be overlap between disease and infectious anomalies, even, requiring coordination between science and medbay if the scientists want to keep the anomaly (and the patient) alive.

- Cargo will have to keep the supply of sample swabs and latex gloves flowing in. They're also implicated as the department most likely to be responsible for spreading the disease all over the place. Salvage will be less directly involved, but might get to be the last few crew members left on their feet if they were away for the worst of the disease.

- Service has the least to do, but might have to navigate delivering food and drinks to quarantined parts of the station.


### Species Interactions

- Reptiles, arachnids and vulpkanin, as well as any other predatory species, should have a stronger immune response to diseases that come from eating raw flesh or (for reptiles in particular) drinking floor blood. Flood blood consumption is, after all, an important part of reptilian culture. Fresh kills should also not count as unsanitary - only after they've sat for a bit do bacteria have a chance to develop.

- Diona should have a stronger immune response to diseases that come from the floor, and especially from infected puddles. This is to help counterbalance the fact that they can't protect themselves with shoes.

- Vox should have a stronger immune response across the board, but especially to diseases that come from trash.


## Administrative & Server Rule Impact

There is some potential for griefing in the form of players deliberately trying to infect others. This is ameliorated in part by the fact that players potentially making bad decisions about whether to get something looked at is deliberately part of the disease's challenge - a griefer and an irresponsible character don't look all that dissimilar in practice. Combined with the fact that disease sources are rare, unpredictable and invisible, and deliberate bioengineeering is difficult and slow, I think the potential for serious griefing is low.


# Technical Considerations

The Disease Diagnoser Delta Extreme and the machine(s) that develops treatments and vaccines will need new UI. For treatments and vaccines, this could be as simple as a single text input to type the genetic code into, although it should probably also keep some record of previously-used codes and allow for quickly copying them into the text input for easy modification. The DDDE needs to indicate both viral and bacterial load: It would be fun to show bacterial load in the form of circular blots drawn on a virtual petri dish, with the presence and size of the blots indicating the amount of bacteria. Viral detection should also have something along those lines, although it's less obvious what.

There will need to be an additional component for holding viral/bacterial load on objects as well as players. For objects, this is basically just a string for the genome, plus an integer amount. For players, the extra process of experiencing disease progression and generating antiserum needs to happen, but a lot of that can probably mirror or directly use the existing metabolism system.

There will also need to be a way for disease instances to mutate across game time without it being computationally overwhelming. Since mutations are just a random replacement of a nucleotide or so, or possibly a removal or addition of one, this shouldn't be too big a deal.

The hardest piece of this from a technical perspective is most likely bioengineering, since the genetic code will have to be matched up to functionality in a way that's randomizable each round, and the genomes themselves will have to be parseable. Genomes being parseable also means that they have to be parsed to determine their behavior, and mutations require that to happen whenver the disease's behavior is used, since it might have changed since the last time. It would make sense to hold off on implementing that until after the basics are established.

### Here's one way it might work:

A virus's genome is a series of alternating tags and modifiers. A tag will declare the 'field' being modified - mutation rate, or symptoms, or so forth. The modifier will then decode to a numeric or keyed value, possibly negative, which is added to the virus's base values for its fields. This code is interpreted linearly from the beginning of the string to the end. This is straightforward to parse, and can still have some interesting interactions when taken apart into fragments and then pieced back together.

For added complexity, some fields could refer to specific positions in the genome for their values, or to the existing values for other fields. This has implications for mutation, since a single nucleotide replacement shouldn't usually be enough to radically change the whole disease's behavior, and since it might be possible to have horrible recursive loops that balloon out into something totally unparseable or game-breaking. The easiest solution to that last problem is: No, that shouldn't be possible. Random mutations might nevertheless have to be checked for sanity, depending on what *is* possible.


# Addendum/Mediography

"Doomsday Book" by Connie Willis is a marvelous work of science fiction about a time traveller who is stranded in the dark ages, cut off from resources, and has to deal with a severe disease. I encourage anyone and everyone to read it for inspiration on how virology might work, and for a general example of what good storytelling about diseases can look like.

Of the many Star Trek episodes where the crews become infected, "Babel" from Deep Space Nine season one is a pretty good one and worth watching. One thing that's interesting and relevant is that for the disease in this episode, the first symptom that appears is the extreme, exotic one, but the second, deadlier symptom is just a fever - nothing fancy, but still potentially fatal. Its mode of transmission also mutates across the course of the episode.
