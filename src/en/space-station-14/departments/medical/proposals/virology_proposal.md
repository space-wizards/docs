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

In any place where a large number of living creatures are stuck together in a small area, diseases are a fact of life; space stations should be no exception. Especially those space stations that tend to get trash and puddles of unknown slop all over the floor. Or random corpses rotting in a corner of maints.

For game purposes, however, most diseases should be minor, barring disease-focused game modes. 

A typical player experience should be that they start showing a mild symptom - say, a light cough - and then it goes away after a little while. Maybe they wear a face mask to help prevent it from spreading, or maybe they don't and a couple other people in the department catch it too. 

This is common enough to be no big deal.

Sometimes, the player will find out that the disease is a bit worse than they thought. New, worse symptoms will develop - a fever, for example. Nothing major, but maybe they decide to go to medbay, where the doctors will take action to protect them from the effects of their symptoms - something to stop them from overheating, for example. Medbay might keep the patient around for a bit, but most likely they can give them something to help and send them on their way. Alternatively, the player might decide they can handle it on their own. Maybe they think of a way to take care of their own symptoms, or maybe they just decide to grit their teeth/beak/whatever and suffer through. Either way, the symptoms will eventually subside.

This is less common, but still not unusual. Still common enough that if it happens, players don't feel they need to make a big deal out of it. Maybe it's a terrible death plague in its early stages, sure, but usually it isn't. Even from a meta point of view, "I have a fever" does not imply "Violet alert! This is a plague round! Quarantine the station! Arm the virologists with shotguns and kill anything that sneezes!"

If the players are too negligent, and allow a less-mild disease to spread too much, the disease might mutate into something that's actually a bit of an issue. Maybe serious enough for medbay to have to sit up and pay attention. Maybe virology comes into play, maybe not.

In extreme cases, where the crew are wading through sewage as they walk down the hall and coughing on each other for laughs, the disease could go completely out of countrol. The disease might spread, grow and mutate until a significant portion of the station is infected. The symptoms might go from inconvenient, to genuinely life-threatening. That, however, is in the hands of the players. If it gets to that point, it's because they collectively let it get to that point.

Or, of course, because it really is a disease-focused game mode.

Whether or not a player catches a disease in the first place shouldn't be solely due to the whims of RNG. Players who interact with unhygienic things and fail to use appropriate protective gear - or to at least wash their hands with soap afterward, as the case may be - should be more at risk, whereas players who take precautions against disease should see those precautions pay off.


### Contagion

Different diseases should have different methods of contagion.

Determining how a disease spreads, and therefore what will stop it from spreading, is part of the detective work required to combat it. Players who catch a disease might take a few obvious precautions, but there shouldn't be a single, simple go-to solution that will perfectly shut down a disease's spread every time.

Diseases should also be contagious for a period of time before a player starts noticing symptoms. Once they know they're sick, it should already be too late to keep it perfectly contained.

Methods of contagion should mostly be straightforward, but with a possibility of occasional sci-fi wackiness: Diseases that spread through eye contact, for instance, or that infect some of the words a person says, making other people who say those same words liable to catch it.


### Symptoms

Symptoms are the most important part of a disease. Without them, a disease is invisible, intangible, and may as well not exist. The only harm caused by a disease is through its symptoms.

Symptoms should range from mundane to bizarre, harmless to gross to inconvenient to extremely dangerous, and from serious to silly. 

There should not be symptoms with solely beneficial effects. Either they're paired with significant downsides - yes, zombism makes you stronger, but it also makes you a zombie - or they shouldn't be beneficial at all unless by circumstance. (For instance, having a fever when the station is too cold.) 

Symptoms should feel biological in nature. They should feel like they're part of a disease, not just wacky, random nonsense. That's not to say that symptoms shouldn't be wacky; just that they should be biologically wacky. They're being caused by tiny reproducing entities hijacking the machinery of the body they're inside, or by the body's own response to that hijacking. Even if they're really weird tiny reproducing entities.

Symptoms can cause visual and auditory effects, but they shouldn't be so garish or extreme that they distract other players from regular gameplay unless the mere fact of the disease itself is also that distracting; symptoms that display strobing lights, screen-covering shaders visible to other players, or that produce loud, shocking noises should only show up when the whole station is falling apart to the disease.

Symptoms should be readable: If it's not immediately obvious what a symptom does to you and how you might deal with its effects, it should at least be straightforward to figure it out. There can and should, however, be symptoms that strongly resemble each other, so that one might be mistaken for the other at first.

A disease's symptoms, like the other aspects of the disease, should be random, though they could be weighted so that particular symptoms tend to appear or not appear together. Diseases should have anywhere from one or two to a few different symptoms.


### Progression

Diseases get worse over time, and one way that happens is through new symptoms showing up: Just because a disease starts with a simple cough or sniffle doesn't mean it won't progress to something more serious. A mild disease might be limited to one or two symptoms, but more serious diseases will have more nasty surprises for their victims lying in wait.

Although the most dangerous symptoms should generally show up later in the disease's progression, the symptoms don't have to follow a strict ordering in severity. It's more interesting and dramatic if it's possible, for instance, that a distinctive but harmless symptom shows up second-to-last, just a short while before the final, most lethal one. Now the player (assuming they've seen others experience these symptoms before them) knows their time is running out. Or maybe it's the last symptom that's the harmless one, indicating that the disease has almost run its course and the player can breathe a sigh of relief.

The earliest symptom or two should still be relatively mild. This is important for the sake of player agency: Players get a chance to react to having a disease before the disease takes full effect, rather than getting lightning bolt-blasted with serious symptoms out of the blue.

At least one symptom in the progression should reflect the severity of the disease; a disease that has five different symptoms that make the player's nose a bit drippy in each of five different colors and does nothing else is not a severe disease, despite having a lot of symptoms. On the other hand, a severe disease doesn't have to threaten the player's life. Dumping gallons and gallons of slippery snot on the ground everywhere you walk (no matter what color it is) should probably count as severe, even if there's no way to die from it. Enough crew members with that symptom, and any captain would be justified in calling evac immediately. Not to mention an emergency janitorial squad.


### Immunity

Diseases should play out as a race between the disease itself and the character's immune system. Either the disease's symptoms overwhelm the character, or eventually their immune system overwhelms the disease itself. Assuming they survive, the character should have some lingering immunity to prevent them from immediately re-catching it.

Immunity to one disease shouldn't help against other diseases. There should be no incentive for players to catch a really mild disease so that they can build up immunity against a more serious one.


### Diagnosis and Treatment

In most cases, treating a disease is simply a matter of keeping the symptoms under control until the patient's own immune system fights it off.

As a serious disease worsens and spreads across the station, however, it'll eventually become clear to the medical department that something more proactive will need to be done.

Once the call has been made, the first step will be simply observing and talking to patients to start to build a profile of the disease. The medics will want to get a clear understanding of what the symptoms are and how the disease spreads, but also where it originated and who caught it first.

Virologists will also want to start taking swab samples (or something like that) from the disease's victims. Their goal is to get a wide array of samples, and not just from inside medbay: They should be going out into the station to sample other people who have caught the disease, as well as surfaces and objects that might be contaminated, and to interview people to help narrow down the disease's origin.

Alongside this, they will be analyzing their samples with the virology equipment. The analysis machine should take some time to finish running, to help encourage the virologists to go back out into the station to find more sample sources, but it should also be possible to analyze multiple samples at once, since the virologists will have a lot of them and will continue collecting more.

The analyzed samples will contain fragments of the disease's genetic code, possibly with inaccuracies, and possibly contaminated with DNA from the patient, or from other sources. The virologists must use these to figure out the virus's genome as best they can. No single sample will contain the whole genome, even in fragments, so the virologists will want to take a variety of samples from a variety of sources.

Samples from things or people who caught the disease earlier in the disease's history should have fewer inaccuracies than samples from later on. However, older samples should be more fragmentary and have more pieces missing. This creates a tension where virologists have to decide how much time to spend tracking the origin down, and when to do the best they can with the information they have. 

Since diseases don't show their symptoms until some time after their victim has caught them, it may not even be possible for the virologists to figure out exactly where the disease started. The player who caught it first might not themself know. Between that and the disease's mutations, it probably won't be possible for virologists to get an exact match; such a thing might not even exist. Their task is to get close enough fast enough to start producing a reasonably effective vaccine before it's too late for it to matter.

To produce a trial vaccine, virologists will have to input their best guess into the vaccine producer, and then give it a bit of time and/or resources. This should only produce a small amount of vaccine - enough for one patient, maybe. Enough to test its effectiveness, but not enough to easily vaccinate the whole station. Virologists might produce multiple trial vaccines before they create one they're happy with. Once they do, mass-producing it from the trial sample should be a different process, possibly conducted by the chemistry department, and expensive enough that it's worth trying to get it right the first time. Some of these things might still happen in parallel, with the virologists offering a poor vaccine quickly and then spending time developing better, more effective ones.

The computers used to develop vaccines should keep good records of what the virologists have and haven't tried, what the analysis results were from past samples, and ideally allow the virologists to add notes for when and where each sample was taken. Sample swabs should also accept paper labels.

Vaccines, of course, are not a cure. Those vaccinated will get a head-start on building up their immune system against the disease, but if they've already caught it, it won't do them much good.


### Mutation

Diseases will mutate over time.

This will impact both the way the disease behaves - it may acquire new symptoms or change its mode of contagion, for instance - and how well virology can attack it, since a mutated virus will have a slightly different genome. The more time the disease has for its separate strains to diverge from the origin, the harder it will be for virology to make a vaccine that's effective against all of those strains at once.


### Virology as a Role

Since an average round will require little to no action from virologists, the virology duties will fall under the responsibilities of existing medical staff rather than being their own role. Players especially interested in virology can still signal their interest by wearing clothes from the virology wardrobe, or by getting a different job title from HoP, or things of that nature.

It is the CMO's job to coordinate virology work and ensure that the available doctors are appropriately balanced between patient treatment and virology duties.


### Prevention

Players should be able to use protective equipment not just to avoid catching diseases, but also to stop themselves from spreading one. Aside from things like surgical masks and latex gloves, this could include, for instance, tissues or handkerchiefs for a minor disease that causes something like coughing or sneezing. Obviously, at the other end of the spectrum, there are biohazard suits.

Janitors can help prevent diseases by keeping the station clean in general, but should also be able to disinfect surfaces, potentially stopping a disease right at the source. Space Cleaner and bleach are the obvious tools for this; bleach should be more effective, but less available.

Janitors should not, however, be able to immediately tell whether or not a surface is disease-contaminated - much less how contaminated it is. They should have to work with the virology department on this. Virologists can test a sample swab to see if there is a disease present, and then pass that information back to the janitorial staff.

Any tool that can immediately reveal whether something is diseased without having to sample and analyze should be top-tier technology, if it exists at all.


### Quarantine

It'd be hard to have diseases and not have players attempting to quarantine each other. Locking someone up in a tiny room for a long time, however, isn't much fun - we already have genpop to avoid exactly that.

Dividing larger parts of the station up into "safe" and "infected" areas, however, has the potential to be much more interesting.

To discourage the former and encourage the latter, isolated wards for sick people should not be included in station maps. Instead, virologists should be equipped with things like inflatable doors and barriers, warning signs or holos, and other tools of that sort. Setting up larger quarantine zones might also be a task for security to get involved in.

For this design, it helps that diseases both have an incubation period where they can spread undetected, and multiple possible modes of transmission. Locking an infected person up by themself still might seem like a good idea, but there might be alternatives depending on the mode of transmission. Besides that, by the time symptoms show up, at least some of the damage is already done. This gives players some grounds to argue back or even justifiably resist if anyone tries to lock them away.


### Bioengineering

For anyone who wants to dip their rubber-gloved arms into the dirty, grimy world of engineering their own viruses, thinking of a virus's genetic code as a mere string of letters is no longer sufficient. The code has to have meaning. The process of bioengineering revolves around unlocking that meaning piece by piece, and using those pieces however possible.

The first step should be the same as that for vaccine creation: Collecting samples. Would-be bioengineers shouldn't be able to sit around in a closed-off room any more than any other practitioner of virology. 

Once those samples are sequenced, the bioengineer should get imperfect information about each fragment's function in the virus's genome. They might also have to factor out contaminating DNA, just like if they were hunting for a vaccine.

Where vaccine creation only requires piecing the fragments into as complete a genome as possible, however, engineering is about taking the fragments and creating something new with them. Since the bioengineer is limited to the fragments they're able to find, they almost certainly won't be able to create exactly the virus they're hoping for. Instead, they'll have to figure out what they can do with the fragments they have.

Once the bioengineer has come up with a genome they feel good about, they should be able to produce it in the vaccinator the same way a vaccine is produced. The only difference is the intent behind the genome entered into the system. This should not, however, be enough to create an actual disease: A vaccine isn't the same as a live virus. To make an actual disease, the bioengineer will have to take extra steps to extract the actual live, viral load from the vaccinator - possibly by disassembling it to get at an internal vial or beaker, making this step the one where someone up to no good is most likely to be caught - and then find a way to incubate it in a host body until it is strong enough to survive in the wild; there should be very little viral load produced this way. 1u, perhaps: The bioengineer gets one shot at incubating it without having to redo the whole process of generating a sample from the beginning.

The easiest host body to use will obviously be the bioengineer's own. This is good! Creating a death-plague is serious business, and should require sacrifice. Those who which to spread disease without themselves dying a glorious death should have a much harder time of it: For instance, a more cautious but slower approach would be to capture several live mice, though they will be harder to extract useful amounts of viral load from before they die. Monkey and kobold cubes, the obvious choice for getting ready-made victims, should have downsides in practice: For instance, maybe the monkeys and kobolds have no real immune systems to speak of, since they're not intended to last very long post-hydration, and will die even faster than mice. The bioengineer could also kidnap crew members, trading their own immediate safety for an increased risk of getting caught. 

There should be no easy, risk-free approach to this. It should not be possible to mass-produce live viral load the same way that vaccines can be mass-produced. The only ways to do it should be to either find victims, or suffer the effects of one's own creation.

Syndicate agents should get access to some kind of immuno-suppresant to help ensure their disease's host doesn't kill off the disease before it can establish itself.

In addition to just releasing the infected host into the station and letting contagion do all the work, the bioengineer should be able to extract the increased amount of viral load from the host's bloodstream so that they can find more creative delivery systems. Or so they can target a specific victim.


### Zombies and Romerol

Zombism is a disease, albeit one with some very strange and particular effects.

To integrate zombies into this system, the symptoms of that disease should be picked apart and treated the same as other symptoms, albeit rare ones. Romeral is then simply a particular strain of disease that combines the zombism symptoms all together. Ambuzol is any vaccine that attacks the genome of that disease.

This way, zombie gameplay remains very similar, in that virologists will need lots of zombie corpses to extract blood from in order to make a vaccine. The difference is that instead of mixing it with chemicals, they're sequencing it to puzzle out its genome.

For Initial Infected, they simply start out infected with a strain of zombism that won't show its symptoms too quickly but also won't be too weak to survive the II's own immune system; maybe II start out immunosuppressed to make this more straightforward. The version of the disease that II have should ideally be identical to what they pass along to their victims, though there might be some aspects, like the ability to succumb to the infection, that have to be handled as special cases.

Breaking the disease into symptoms also allows for variant zombies and zombie-adjacent diseases, both in zombie rounds and in general.


## Game Design Rationale

The ideal is for diseases to be interactive for everyone involved, to present interesting and meaningful decisions both mechanically and for roleplay, and to not arbitrarily limit someone's gameplay out of the blue: Getting infected is at least partially a consequence of a player's actions, and having a disease is often manageable with the right equipment or behavior.

Another important part of this is that virologists don't get to just sit in their department and swirl test tubes or whatever. They have to get out there and track down the disease's source, which will generally require interacting with crew members as well as poking about in various parts of the station. 

On the flip side, having a disease doesn't automatically mean running to virology - most diseases won't have enough impact to be worth doing anything about other than to carry tissues and maybe take off a layer of insulating clothing. Even somewhat more serious diseases might be manageable with regular medication, or topicals, or something along those lines. This means that having a disease is interactive for the victim; they're not just an object for virology to deal with. They have to make their own decisions about how and if to address their own symptoms, balancing the possibility that they've contracted something horrible that will lay waste to the entire crew with the probability that it'll go away on its own and be no big deal.

The different modes of transmission also lead to decision-making for infected crewmembers, since they have to figure out what they can and should do to prevent spreading their disease to others.

Since diseases cause problems through their secondary effects, in the form of symptoms, and since people will tend to get over any disease they can survive, there's flexibility and room for creativity in how players decide to handle a disease. Some diseases won't even be harmful or fatal - just inconvenient, or ugly. In which case, the whole crew might just end up going about their regular duties while trying to ignore their dripping pustules leaving puddles of yuk everywhere they go. This helps foster emergence as well as making diseases more interactive for non-viro crew. A good variety of symptoms, with potential interaction between them, can lead to emergence in its own right - any disease might present some novel and surprising conjunction of symptoms with unexpected consequences for the crew.

Bioengineering presents mechanical challenge while limiting a player from creating perfect unstoppable deathplagues: They have to figure out what they can do with the pieces they've got. It's also not consequence-free for the bioengineer, since they'll likely have to suffer their own disease. Even bioengineered diseases will be different and unique from each other depending on what the player gets and what they do with it. Preferably, the genome code should also work in a way that allows for surprising and unexpected outcomes for the bioengineer themself, if they've done some guesswork or interpreted something wrong.


## Roundflow & Player interaction

In a regular round, there should be a constant, low chance for a mild disease to spawn as an event. These will gravitate strongly towards the filthier parts of the station, or possibly even fizzle if there's no sufficiently filthy place for them. The disease should on average infect one to a few people across the duration of the round from both its original source and from contagion, and should on average cause mild inconvenience at worst. The exact nature of the disease should be random, with at least some possibility that it will be severe enough for virology to take an interest - maybe one moderate disease appears every three to five rounds on average, say. Good janitorial coverage can reduce this. Extremely filthy stations, on the other hand, might generate extra diseases in sufficiently disgusting areas.

In a disease-focused game mode round, a severe disease should spawn, obviously. The only real difference between a severe disease and a mild one should be the numbers: Severe diseases can have higher mutation rates, a longer infection period before symptoms appear, faster progression once symptoms do appear, more serious symptoms, or most likely a combination of those. Like mild diseases, these can be created randomly, so that no two diseases are the same.

Diseases start out small and weak, then escalate through spread and mutation. A quick and appropriate response on the part of the crew - not just virology, but the whole crew - can stop the disease in its tracks. On the other hand, a severe disease (or a sufficiently-neglected moderate one) has the potential to lay waste to the entire crew and render the station downright uninhabitable if the crew can't stay ahead of it.


### Department Interactions

- Medbay will be the main defense against any serious disease. Not just through virology, but also through the doctors responsible for treating the symptoms; the chemists who will need to help produce and distribute treatments and vaccines; and the paramedics, who have to face the risks of going out into the infected parts of the station to recover downed crewmembers.

- Janitorial staff will also play a strong role, since their efforts to keep the station clean will help curb the spread of the disease or prevent it from coming into existence in the first place. Not to mention, they'll be vital if a disease causes projectile vomiting or something.

- Security might have to be responsible for keeping a panicking crew in order, or stopping people from breaking quarantine. For a disease like zombism, they might have to more directly protect the uninfected crew from those infected.

- Command, likewise, might need to take charge of organizing the crew to act together against the threat of disease.

- Engineering could help with creating quarantine zones. Atmos could help against airborne diseases with scrubbers and holofans. They might also be able to do things like cool down the station if the majority of the crew have terrible fevers.

- Possibly, some symptoms could be worth research points to Science? Which might lead to some interesting conflicts of interest. They should also get some relevant technologies to research - faster disease diagnosers, bluespace sample swabs, better bio-suits and the like. There could be overlap between disease and infectious anomalies, even, requiring coordination between science and medbay if the scientists want to keep the anomaly (and the patient) alive.

- Cargo will have to keep the supply of sample swabs and latex gloves flowing in. They're also implicated as the department most likely to be responsible for spreading the disease all over the place. Salvage will be less directly involved, but might get to be the last few crew members left on their feet if they were away for the worst of the disease.

- Service has the least to do, but might have to navigate delivering food and drinks to quarantined parts of the station. They'll also have to consider the possibility that their food or drink becomes contaminated.


### Species Interactions

- Reptiles, arachnids and vulpkanin, as well as any other predatory species, should have a stronger immune response to diseases that come from eating raw flesh or (for reptiles in particular) drinking floor blood. Flood blood consumption is, after all, an important part of reptilian culture. Fresh kills should also not count as unsanitary - only after they've sat for a bit do diseases have a chance to develop.

- Diona should have a stronger immune response to diseases that come from the floor, and especially from infected puddles. This is to help counterbalance the fact that they can't protect themselves with shoes.

- Vox should have a stronger immune response across the board, but especially to diseases that come from trash. If they're able to eat trash, they shouldn't constantly be getting sick because of it.


## Administrative & Server Rule Impact

There is some potential for griefing in the form of players deliberately trying to infect others. This is ameliorated in part by the fact that the system already encompasses the possibility for players to make bad decisions - someone griefing isn't going to have an easy time doing something that's too far outside the scope of expected player behavior. Combined with the fact that disease sources are rare, unpredictable and invisible, and deliberate bioengineeering is difficult and slow, I think the potential for serious griefing is low.


# Technical Considerations

The Disease Diagnoser Delta Extreme and the machine(s) that develops treatments and vaccines will need new UI. For treatments and vaccines, this could be as simple as a single text input to type the genetic code into, although it should probably also keep some record of previously-used codes and allow for quickly copying them into the text input for easy modification. The DDDE needs to indicate viral load.

There will need to be an additional component for holding viral/bacterial load on objects as well as players. For objects, this is basically just a string for the genome, plus an integer amount. For players, the extra process of experiencing disease progression and generating antiserum needs to happen, but a lot of that can probably mirror or directly use the existing metabolism system.

There will also need to be a way for disease instances to mutate across game time without it being computationally overwhelming. Since mutations are just a random replacement of a nucleotide or so, or possibly a removal or addition of one, this shouldn't be too big a deal.

The hardest piece of this from a technical perspective is most likely bioengineering, since the genetic code will have to be matched up to functionality in a way that's randomizable each round, and the genomes themselves will have to be parseable. Genomes being parseable also means that they have to be parsed to determine their behavior, which, given the possibility of mutation, will have to be re-parsed many times. It would make sense to hold off on implementing bioengineering until after the basics are established.

### Here's one way it might work:

A virus's genome is a series of alternating tags and modifiers. A tag will declare the 'field' being modified - mutation rate, or symptoms, or so forth. The modifier will then decode to a numeric or keyed value, possibly negative, which is added to the virus's base values for its fields. This code is interpreted linearly from the beginning of the string to the end. This is straightforward to parse, and can still have some interesting interactions when taken apart into fragments and then pieced back together.

For added complexity, some fields could refer to specific positions in the genome for their values, or to the existing values for other fields. This has implications for mutation, since a single nucleotide replacement shouldn't usually be enough to radically change the whole disease's behavior, and since it might be possible to have horrible recursive loops that balloon out into something totally unparseable or game-breaking. The easiest solution to that last problem is: Don't let loops or recursion be possible, duh. Random mutations might nevertheless have to be checked for sanity, depending on what *is* possible.


# Addendum/Mediography

"Doomsday Book" by Connie Willis is a marvelous work of science fiction about a time traveller who is stranded in the dark ages, cut off from resources, and has to deal with a severe disease. I encourage anyone and everyone to read it for inspiration on how virology might work, and for a general example of what good storytelling about diseases can look like.

Of the many Star Trek episodes where the crews become infected, "Babel" from Deep Space Nine season one is a pretty good one and worth watching. One thing that's interesting and relevant is that for the disease in this episode, the first symptom that appears is the extreme, exotic one, but the second, deadlier symptom is just a fever - nothing fancy, but still potentially fatal. Its mode of transmission also mutates across the course of the episode.

The Red Dwarf series V episode "Quarantine" breaks this document's policy that viruses should not have beneficial symptoms, but it's also mandatory for Virology to get gingham dresses in their clothing vendors or something, and this episode is why.
