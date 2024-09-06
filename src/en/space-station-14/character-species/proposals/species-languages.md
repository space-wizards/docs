# Species Languages

| Designers | Implemented | GitHub Links |
|---|---|---|
| TheNat'LaGuy | :x: No | TBD |

## Overview

This Proposal aims to add in-game languages based on what species you are currently playing, by giving the player the ability to speak in their species native languages that only other members of the same species can understand (With some cavaets depeding on what species you play and even your job)

## Design Pillars

### The galatic standard language

Every single member of the crew (and sentient beings, made sentient by an event or cognize), by default, speaks the Galactic Common Language. Galactic Common Language is an artifial language using a discovered pattern in every sapient vocal coords sound production to facilitate universal communication across different species in the galaxy, and it is an absolute requirement to know in order to work in any intergalatic organization or corporation, like say, Nanosten or the Syndicate. Any word you say by default while whispering, talking and speaking on the radio is automatically said in Galactic Common.

In-lore, it is a mishap of words and sentences. In-game, it can be any language, depending on the server's rules.

Nonsentient beings, like space carp, smile, hamlet and any ghost role or creature can understand Galactic Common, but can't speak it.

### Diffrent species, diferent languages

All species in the game can say a diferent language besides Galactic Common. The list is

| Species | Language Name |
|---|---|
| Humans | Neo-Solar |
|---|---|
| Dwarfs | Dwarfish |
|---|---|
| Reptilian | Draconic |
|---|---|
| Moth People | Moffic |
|---|---|
| Slime People | Gloomspeak | 
|---|---|
| Vox | Voxian |
|---|---|
| Diona | Rootsong |
|---|---|
| Arachnid | Arachnis |
|---|---|
| Silicons (Cyborgs and AI) | Encoded Audio Language |
|---|---|
| Monkeys and Gorilas | Monkey (Default language if not made sentient by cognize) |
|---|---|
| Kobolds | Kobold (Default language if not made sentient by cognize) |
|---|---|
| Spiders | Spider (Default language if not made sentient by cognize) |
|---|---|
| Slimes and Smile | Slime (Default language if not made sentient by cognize) |
|---|---|
| Rats, Rat King, Hamlet, Hamsters and Mothroaches | Chriter (Default language if not made sentient by cognize) |

Some other species, like monkeys and kobolds, and even antagonists, like syndicate agents and nuclear operatives, can also speak different languages

| "Species" | Language Name |
| Syndicate Agents, Nuclear Operatives and Syndicate PAIs | Codespeak |
|---|---|
| Pirates | Piratespeak (Default language) |
|---|---|
| Mutes and Mimes | Galactic Sign Language (Default language) |

Any other creature not covered here speaks what they already say ingame. Syndicats still meow, and space carp still 'raw'

### Special interactions

Understanding a language is only the halfway to speaking it. There are some specials interactions in that you can understand what is being said, but you cant speak it. These are:

1) Slime People can understand the Slime language (So understand what a slime is saying if they, for example, say hello), but cant speak it.
2) Arachnids can understand the Spider language, but cant speak it.
3) Although monkeys, gorilas and kobolds dont speak the same language, they can both understand each other languages clearly.
4) Although dwarfs are decendents of humans and are well incorporated into human society, their ways of speaking have diverged. Dwarfs can understand the Neo-Solar languange, but can't speak it.

### Ways to learn different languages

The best, fastest and easiest way to learn all languages is spawning or arriving on the station as a Librarian. Their years of study have allowed them to understand and speak basically any language imaginable.

Another way to learn a different language is through Salvage. They can find discarded language manuals through debris and expeditions that upon used, it will consume the manual and the user will learn the language specific to the language manual it used(If its the draconic language manual, the user will learn to understand and speak draconic if they arent a Reptilian). All languages have a manual and can be found through salvage this way, except Galactic Common.

The last way to learn a new language is through maintenance lockers. They have a very small chance to spawn a discarded language manual of every language except Galactic Common, Codespeak and Piratespeak, and it shoudn't be uncommon to not find a language manual through a whole shift.

Admins ghosts and normal ghosts know all languanges by default.

## Implementation

### Saying something in a language

The player will use the ',' keyword alongside a letter next to the keyword in the chat channel to say a specific language, just like using a department radio. So saying ",d I love the captain!" will say it in draconic (If you know it) in the local volume.

But thats not all. You can also use languages while whispering or on radio! You just need to first define on the chat channel where do you want to say('.' On local, ',' to whisper, and ":" + "the department you want to say" for radios) + what language do you want to use. So for example:

". ,v The captain is robust!" Will say this phrase in Voxian on the local volume.

", ,a Great, another one" Will say this phrase in Arachinis while whispering.

":e ,m Lamp brothers, can you all check on the tesla?" Will say this phrase on the Engineering radio channel in Moffic.

When you successfully speak something in a different languange that isn't Galactic Common, All words in the sentence will appear in italic and just like you type on your screen.

If no argument is presented on where to say the language on the text channel, it will default to the local volume.

Because of the similirities with department radio IDs, This system to identify what languange you are speaking is called Languange IDs.

### List of languages IDs

| Language Name | Language IDs |
|---|---|
| Galactic Common | ,c |
|---|---|
| Neo-Solar | ,n |
|---|---|
| Dwarfish | ,w |
|---|---|
| Draconic | ,d |
|---|---|
| Moffic | ,m |
|---|---|
| Gloomspeak | ,g |
|---|---|
| Voxian | ,v |
|---|---|
| Rootsong | ,r |
|---|---|
| Arachnis | ,a |
|---|---|
| Encoded Audio Language | ,u |
|---|---|
| Codespeak | ,t |
|---|---|
| Piratespeak | ,p |
|---|---|
| Galactic Sign Language | ,s |
|---|---|
| Monkey | ,o |
|---|---|
| Kobold | ,k |
|---|---|
| Spider | ,i |
|---|---|
| Slimes | ,e |
|---|---|
| Critter | ,c |

### Not understanding a language

When someone listens to a conversation from a languange they dont know, it will sound like absolute gibberish. Every word in the speech gets changed to a random sylable from a list in the languange it is speaking, with no pattern whatsoever, different from languange to languange. So saying "I want to file a complaint agaisnt security" can sound like "Ss rueh usuh shzuul lusr oru he elolso" to someone who doesnt draconic, to "shzuul lusr sk huro sielo. Ek sz zalo" and even "sz uk oru he elolso ar rueh".

When trying to speak a language you don't understand, Like a Slime person trying to speak Rootsong without being a Librarian or reading the discarted language manual for Rootsong, they will default to Galactic Common and a brief message will appear atop of their character saying "You don't know that language!"

### Galactic Sign Language

Galactic Sign Language is Special because it can only be "Spoken" by mimes and mute people, whatever species they might come from, whether they are a antagonist or not. Only other mimes, mute people, the librarian and crew that have read any found discarded languange manual for galactic sign languange can understand and "speak" galactic sign languange.

Galactic Sign Languange is completely silent by default, being only visible, even its "gibberish", by line of sight, it cant be heard over walls, and only appears in the text channel if it was send with line of sight. As a result of this, you can't send a message over the radio or whisper in galactic sign languange, and it may only be send in the local volume and seen if people have a direct line of sight.

Even if your mute, however, you can still understand your species languange and read discarded languange manuals. So if your a mute moth person and someone speaks moffic next to you, you will understand them, but you wont be able to reply back in moffic (or galactic common), or if your a mime and you find a discarted languange manual for kobold in maintenance and read it, you will be able to understand Kobold now, but you wont be able to speak it.

Mute librarians will still be able to understand all languanges, but they will only be able to speak in Galactic Sign Languange.

Since this languange is so unique, it needs to be developed separately from the main language system, so that it may not cause problems with the other languages, with potentially unique components and prototypes specific to galactic sign languange.

### Adding new languages

If any new sapient species gets added into the game, the creator of the species needs to create a new language for their species, and a species cannot have more than one species language at a time.

If it is an non-sapient species, a new language is unadvised, and may be discussed with the maintaners if need be, but if it is an antagonist non-sapient species, a new language is allowed, but only one species language.

### Examples of each languanges "gibberish"

| Language Name | "gibberish" |
|---|---|
| Galactic Common | "Sao chua guang zhan alion pukai hong shanislun e sheng tha. Arnotpoha. Orle lao. Re shan qiang shuaithe are le es" |
|---|---|
| Neo-Solar | "Arm, instable amarillo kàn bù dào, rehabilitation shìjiè davniy equitación, and dobro pozhalovat làzhú assurément community" |
|---|---|
| Dwarfish | "Kadrin rinriak karaz ekrund sked grint. Karugrombthi gnol druegskaggrund kalan. Jifful grong haraz dum chuf bak grob frongol rikkaz." |
|---|---|
| Draconic | "Ss rueh usuh shzuul fliskth lusr sk huro sh uk oru he elolso ar. Rsku suok fs zalo uh iksuah. Rasi sh flinsss si ilro sh sielo. Ek." |
|---|---|
| Moffic | "Sekygglitomånkönvii. Detdetdår møtmå. Ån. Gårköndagint. Viitehjaomköntyclaviinæbraånhönledetygglithankäytokmo sek." |
|---|---|
| Gloomspeak | "Qib quum. Qil qoovol qilzixqr quum. Zaoo qbvol qil brim qu-uuzib! Qu-uu qil volqu-uu zix." |
|---|---|
| Voxian | tititihi SKREAHKEHK hikikikikiya EHKRAWK KRAKA yayichi chakah SKREAHKEHK titihi KRAAAA EEE KIIIKRI KA |
|---|---|
| Rootsong | "Nasyu qip. Maaeobwex tisyudilamel tok. Eresnas aeqedointyuala haqipbalriifalbisvilbisinthaaearasbisalaqeuis. Pii." |
|---|---|
| Arachnis | "Clink-Click-Clink Hizee Click Hummme-Hunnee Hunne Cli. Clivk Hizee-Click Akkk-Hizee Akk. Vek Click Cli Hummne Click" |
|---|---|
| Encoded Audio Language | "Tzzzwurrboopbeepkssshbeephissbuzz keeyhsshisshsswurrboopdoo wahh. Buzzdoohisshssbeepboopbeepkeeyhss. Tzzzdeebeep." |
|---|---|
| Codespeak | "Nettles, hats, vodka and tonic, airlocks, zombies, engineering, Lawyer, petes, Captain, hungry, white russians, Darell Briner, peaceful, drunken blumpkin." |
|---|---|
| Piratespeak | "Timbers grog scallywag timbers scallywag scallywag matey me matey timbers rum shiver arr bucko bucko blimey shiver." |
|---|---|
| Galactic Sign Language | "***Hand Up*** ***Hand Down*** ***Thumbs Up*** ***Hand to the left*** ***Hand to the Right*** ***Clapping*** ***Thumbs Down*** ***Hand to the mouth*** ***Punch down*** ***Finger Walking*** ***Holding three fingers*** ***Hand Palm*** ***Point finger up*** ***Closed hand***" |
|---|---|
| Monkey | "Eek eek oop aak chee aak oop oop aak oop oop aak chee. Chee chee chee. Chee oop aak aak oop aak oop eek eek eek." |
|---|---|
| Kobold | "Yip eep greeek gaaaa mip gaa shilk aak aya gaaaa mip yip yip yip aya eep yip greeek" |
|---|---|
| Spider | "Hissss Hisss Shieek Hiss Shieek Heeek Heeek Keee Hisss Hisss Shieeek" |
|---|---|
| Slimes | "Bloop bleep blooop blap blopepe blenk blam blem bloop blooop blopepe blenk blep bap blap" |
|---|---|
| Critter | The sounds these creatures already make |