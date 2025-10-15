# Virology

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| SeaWyrm | SeaWyrm | :x: | TBD |

<!-- In either case you will have to write an outline on how you plan to implement this feature in the **Technical Considerations** section to show that is technically sound and feasible. -->


## Overview

A take on how virology might be re-added to the game in a way that has depth and is interesting and enjoyable for everyone.


## Features to be added

### Diseases 

A few (one to three, maybe) diseases will happen every shift, but most of them will be mild and ignorable - a runny nose, a slight cough, and so on. Moderate diseases, requiring some virology intervention, will be possible but uncommon. Severe diseases will be their own game mode. 

A disease will spawn in at a location or on an object. Anyone who walks through the location or touches the object will have a chance to catch the disease.

A disease will be either bacterial, or virological. It will have:
- One or more symptoms from a weighted list, ranging in severity from "you get the sniffles" to "spontaneous combustion." These will include normal, sensible symptoms, but also (more rarely) silly space game symptoms.
- One or more methods of transmission. For instance, "surface contact," "airborne," "looking at someone."
- A mutation rate.
- A speed of progression.
- Incubation time and symptom onset time. Incubation time governs how long it takes for the victim to become infectious. Symptom onset time governs how long it takes for the victim to start displaying symptoms. Incubation time should be shorter, so that victims start spreading the disease before they know for sure that they have it. Speed of progression governs both of these, as well as the rate at which additional symptoms manifest. It should be possible to change the speed of progression via medical interventions.

Bacterial diseases will also have a separate resistance level against each antibiotic.

Viral diseases will also have a genetic code, similar to how different characters have different DNA patterns that the detective can find and match to their records.


### Damage and Immunity

Diseases will not and should not behave like an "invisible health bar."

Diseases will not harm the victim directly. All harm will be a secondary effect of the disease's symptoms. For instance, a fever will cause increasing amounts of heat damage. This means that a patient with a disease can be treated with normal medical interventions to control the symptoms, and if the symptoms are kept under control, will recover naturally.

All diseases will behave like reagents in the player's bloodstream, but with much slower metabolism governed by their speed of progression. Each time the progression ticks, the bacterial or viral load in the bloodstream will increase, which will also increase the severity of symptoms.

The victim's body will also produce 'antiserum,' which will diminish the amount of bacterial or viral load. These will accumulate slowly, but build up until they can overcome the disease. The numbers should center around a sweet spot where mild diseases will generally go away on their own, and severe diseases will grow quickly enough that they're likely to kill the patient before the patient generates enough antiserum to beat it back.

Antiserum will be keyed to a particular disease. If a person has one disease, and catches another, they'll produce two distinct flavors of antiserum at two different levels. If they get over a disease, the antiserum will linger in their bloodstream, making them much less likely to catch it again. Virologists can also extract antiserum from a person's bloodstream and isolate it to produce a treatment for other patients.

A new organ, 'Lymph Nodes,' will be responsible for metabolising antiserum.

### Diagnosis and Treatment

The first step in diagnosis is simply observing and talking to patients to start to build a profile of the disease. Swab samples can be taken from patients and from objects and surfaces that are suspected of harboring diseases; the Disease Diagnoser Delta Extreme will take a swab sample and reveal if there is a disease present in the sample, and if so, whether it is viral or bacterial, but at this stage, that's the only thing it will reveal. Virologists will have to determine how severe the disease is the hard way.

Bacterial diseases are straightforward: Chemistry will have three new reagents they can produce which serve as antibacterials. These will be roughly equivalent to each other - the main difference is that a bacterial infection can build up resistances to them, so for a particularly severe bacterial disease with a high mutation rate, it may be necessary to switch antibacterials. Antibacterials will attack the bacterial load in the patient's bloodstream just like antiserum.

In the case of bacterial diseases, virologists might still be responsible for helping to track down the source of the disease and eliminate it, possibly with some janitorial assistance for those hard-to-clean surfaces.

Viral diseases are more complicated. The virologists will need to piece together the virus's genetic sequence as best they can. The most effective way to do this will involve some legwork and detective skills: Tracking down contaminated individuals, objects, and surfaces, and taking lots and lots of swab samples. Each sample will have fragments of the virus's entire genome. These fragments will also be increasingly garbled based on how many steps they are removed from the original source. Virologists can also take blood samples, but these will have to have the person's own DNA factored out before they reveal anything about the virus. Blood samples have to be put in test tubes and centrifuged before they're useful.

Virologists don't need to figure out the whole genome of the virus before they can start to produce treatment, but the closer their sequence is to the correct sequence, the more effective it will be. If the treatment sequence is too far off, it will either be ineffective, or downright harmful. They can also produce vaccines based on shorter fragments of DNA. These won't help patients who are already infected, but will prompt uninfected patients to start producing antiserum. The effectiveness of the vaccine is based both on how well it matches the viral DNA, and how long a sequence it uses; a vaccine based on, say, "A" would match pretty much any virus, but would be basically useless.

Virology equipment will be able to produce test treatments, but only slowly. When a test treatment is determined to be effective, it can be sent to Chemistry for mass-production.

In addition to the DDDE, petri dishes will be available. A petri dish can be swabbed, and any bacteria present on the swab will be loaded into the petri dish. Once enough time has passed, the petri dish will reveal the presence, amount, and number of different types of bacteria that have grown in it. Reagents can also be added to a petri dish to observe their effects on the bacteria - this is one way to check if bacteria have developed resistence to a given antibiotic. Petri dishes should be supplied to Virology, and possibly also Chemistry. 

Petri dishes can break, spilling their bacterial load onto the ground. They will also contain agar, a food reagent that will transmit any bacteria growing in the dish to anyone who eats it. If there are no bacteria, it is harmless. Agar could also potentially be a component in food or drink recipes for chefs and bartenders.

Viruses will not interact with petri dishes.

### Mutation

Mutation rate is one of the things that can make a disease more dangerous.

Bacterial diseases can only mutate to build up resistance to specific antibacterial agents.

Viruses, however, can cause more problems.

First of all, as viruses mutate, they will drift from the original virus's genetic code, making treatment less effective. Second, as the code mutates, the disease's symptoms and stats will also change. At worst, this can introduce new, more harmful symptoms. For more serious diseases, virologists will have to act fast and continue gathering samples to stay ahead of mutations. Treatment based on the original genome will still tend to be most effective overall, since it will best match the widest range of possible mutations, but as a disease spreads, that initial genome will become less and less relevant.

This also affects antiserum! A rapidly-mutating virus might overwhelm the victim's immune system to the point where the antiserum they've accumulated becomes useless.


### Virology as a Role

Since an average round will require little to no action from virologists, a virologist will by default act as a regular doctor. Since medbay is where it will most likely first become evident that a disease is on the loose, this does mean that they'll be in position to know when they have to start mounting a response.

If there are no virologists on staff, a CMO might recruit from among the existing medical staff, or they might take on those duties themself.


### Prevention

Depending on the disease's mode of transmission, surgical masks, (which already exist,) latex gloves, (which already exist,) and even tissues or handkerchiefs (which could be added) can be used to help prevent them from spreading. Space Cleaner will reduce viral load on a given surface or object, though it won't necessarily eliminate it entirely. For more severe diseases, biosuits and gas masks might be necessary.

Anyone who leaves their used tissues on the ground is a bad person and should feel bad. Anyone who picks them up bare-handed is liable to contract whatever disease the person had.


### Quarantine

Quarantine is fun, except for when it really, really isn't: Dividing the station up into "safe" and "infected" areas could lead to all sorts of interesting situations, and should be encouraged by giving the virology department a healthy supply of inflatable doors and barriers, as well as warning signs and holos to put up. Locking a given player into a tiny room for half the round should be discouraged, and isolated wards for sick people should probably not be provided.

Unfortunately, it would be difficult for any system where infections can be passed from player to player to not have some incentive for players to lock each other up.

For this design, it helps that diseases both have an incubation period where they can spread undetected, and multiple possible modes of transmission. Locking an infected person up still might seem like a good idea, but there are alternatives if the mode of transmission is identified, and it's less effective anyway since by the time symptoms show up, at least some of the damage is already done. The added uncertainty especially means that locking a particular person up is less undeniably a good idea, giving them more grounds to argue back or even justifiably resist.


### Bioengineering

MOSTLY TBD
My only note here at present is that any antag who wants to engineer a horrible disease should be required to incubate it within their own body. That's the price for unleashing a plague upon the crew: You're the initial infected.

This should naturally tend to reduce station-wiping diseases to the domain of DAGD antags, which is where it should be. And even the worst diseases shouldn't progress so rapidly that virology has no chance to catch them in time. Er, so to speak.

The same machine that creates treatments and vaccines can be used to do bioengineering, but that functionality is locked behind CMO's ID. CMO (or any antags who get their hands on CMO's ID) can use their ID to unlock it. The machine will keep a record of all bioengineering activity, including the IDs of the users, though this can be wiped by snipping the log wire or made to not record any new activity with an emag.

### Zombies and Romerol

The components of zombism could and should be picked apart and added separately as (severe) symptoms and transmission modes within this system, possibly weighted to have a greater chance of occuring together. Romerol then simply becomes a particular strain of disease suspended within blood. Zombie gameplay remains similar, in that the blood of zombies can be used by virology to help pin down the virus's genome and thereby develop a treatment. Initial Infected rounds, likewise, work basically the same way, with II players starting out with a certain amount of viral load in their bloodstream, a deficiency in antiserum production, and a particularly long time until onset of symptoms.


## Game Design Rationale

An important part of this is that virologists don't get to just sit in their department and swirl test tubes or whatever. They have to get out there and track down the disease's source, which will generally require interacting with crew members as well as poking about in various parts of the station. 

On the flip side, having a disease doesn't automatically mean running to virology - most diseases won't have enough impact to be worth doing anything about other than to carry tissues and maybe take off a layer of insulating clothing. Even somewhat more serious diseases might be manageable with regular medication, or topicals, or just gritting one's teeth/beak/whatever and tanking it. This means that having a disease is interactive for the victim; they're not just an object for virology to deal with. They have to make their own decisions about how and if to address their own symptoms, balancing the possibility that they've contracted something horrible that will lay waste to the entire crew with the probability that it'll go away on its own and be no big deal.

The different modes of transmission also lead to decision-making for infected crewmembers, since they have to figure out what they can and should do to prevent spreading their disease to others.

Since diseases cause problems through their secondary effects, in the form of symptoms, and since people will tend to get over any disease they can survive, there's flexibility and room for creativity in how players decide to handle a disease. Some diseases won't even be harmful or fatal - just inconvenient, or ugly. In which case, the whole crew might just end up going about their regular duties while trying to ignore their dripping pustules leaving puddles of yuk everywhere they go. This helps foster emergence as well as making diseases more interactive for non-viro crew. A good variety of symptoms, with potential interaction between them, can lead to emergence in its own right - any disease might present some novel and surprising conjunction of symptoms with unexpected consequences for the crew.


## Roundflow & Player interaction

Though every round should have a mild disease or two, these should usually be ignorable or at worst inconvenient, whereas a severe disease counts as a round-defining major 'antagonist' and should be its own game mode.

In a regular round, there should be a constant, low chance for a mild disease to spawn as an event. These will infect a particular object or location (tile) and afflict themselves upon anyone who touches or stands on their source, spreading from there as per their mode of transmission. The disease should infect one to a few people and cause mild inconvenience at best. The exact nature of the disease should be random, with at least some possibility that it will be severe enough for virology to take an interest - maybe one moderate disease appears every three to five rounds on average. Good janitorial coverage might reduce this.

In a Plague Round, there will be a severe disease that spawns within the first 10 minutes or so. Other minor diseases might also show up via events. Like mild diseases, the severe disease will have a particular object or tile that is its source, though it might slowly spread out from that source to help ensure that the crew doesn't totally miss it all shift. The only real difference between a severe disease and a mild one will be the numbers: Severe diseases can have higher mutation rates, a longer infection period before symptoms appear, faster progression once symptoms do appear, more serious symptoms, or most likely a combination of those.

Diseases start out small and weak, then escalate through spread and mutation. A quick and appropriate response on the part of the crew - not just virology, but the whole crew - can stop the disease in its tracks. On the other hand, the disease has the potential to lay waste to the entire crew and render the station downright uninhabitable if the crew can't stay ahead of them.


### Department Interactions

- Medbay will be the front line against any serious disease. Not just the virologists, but the doctors responsible for treating the symptoms; the chemists who will need to help produce and distribute treatments and vaccines; and the paramedics, who have to face the risks of going out into the infected parts of the station to recover downed crewmembers.

- Janitorial staff will also play a surprisingly strong role, since their efforts to keep the station clean will also help curb the spread of the disease. Also, if a disease causes projectile vomiting or something, their efforts will be doubly vital.

- Security might have to be responsible for keeping a panicking crew in order, or stopping people from breaking quarantine.

- Command, likewise, might need to take charge of organizing the crew to act together against the threat of disease.

- Engineering could help with creating quarantine zones. Atmos could help especially against airborne diseases with scrubbers and holofans. They might also be able to do things like cool down the station if the majority of the crew have terrible fevers.

- Possibly, some symptoms could be worth research points to Science? Which might lead to some interesting conflicts of interest. They should also get some relevant technologies to research - faster disease diagnosers, bluespace sample swabs, better bio-suits and the like.

- Cargo will have to keep the supply of sample swabs and latex gloves flowing in. They're also implicated as the department most likely to be responsible for spreading the disease all over the place. Salvage will be less directly involved, but might get to be the last few crew members left on their feet if they were away for the worst of the disease.

- Service has the least to do, but might have to navigate delivering food and drinks to quarantined parts of the station.


## Administrative & Server Rule Impact

There is some potential for griefing in the form of players deliberately trying to infect others. This is ameliorated in part by the fact that players potentially making bad decision about whether to get something looked at is deliberately part of the disease's challenge - a griefer and an irresponsible character don't look all that dissimilar in practice. Combined with the fact that disease sources are rare, unpredictable and invisible, I think the potential for serious griefing is low.

This might change if bioengineering new diseases is added - but see the note above on that subject.


# Technical Considerations

The Disease Diagnoser Delta Extreme and the machine(s) that develops treatments and vaccines will need new UI. For treatments and vaccines, this could be as simple as a single text input to type the genetic code into, although it should probably also keep some record of previously-used codes and allow for quickly copying them into the text input for easy modification. The DDDE needs to indicate both viral and bacterial load: It would be fun to show bacterial load in the form of circular blots drawn on a virtual petri dish, with the presence and size of the blots indicating the amount of bacteria. Viral detection should also have something along those lines, although it's less obvious what.

There will need to be an additional component for holding viral/bacterial load on objects as well as players. For objects, this is basically just a string for the genome, plus an integer amount. For players, the extra process of experiencing disease progression and generating antiserum needs to happen, but a lot of that can mirror or directly use the existing metabolism system.


# Addendum/Mediography

"Doomsday Book" by Connie Willis is a marvelous work of science fiction about a time traveller who is stranded in the dark ages, cut off from resources, and has to deal with a severe disease. I encourage anyone and everyone to read it for inspiration on how virology might work, and for a general example of what good storytelling about diseases can look like.
