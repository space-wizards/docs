# Species Languages

| Designers | Implemented | GitHub Links |
|---|---|---|
| TheNat'LaGuy | :x: No | TBD |

## Overview

This Proposal aims to add in-game languages based on what species you are currently playing, by giving the player the ability to speak in their species native languages that only other members of the same species can understand (With some cavaets depeding on what species you play and even your job)

## Design Pillars

### The galatic standard language

Every single member of the crew (and sentient beings, made sentient by an event or cognize), by default, speaks the Galactic Common Language, the equivelent of present day english. Any word you say by default while whispering, talking and speaking on the radio is automatically said in Galactic Common.

Nonsentient beings, like space carp, smile, hamlet and any ghost role or creature can understand Galactic Common, but can't speak it.

### Diffrent species, diferent languages

Besides humans and dwarfs, every species in the game can say a diferent language besides Galactic Common. The list is

| Species | Language Name |
|---|---|
| Reptilian | Draconic |
|---|---|
| Moth People | Moffic |
|---|---|
| Slime People | Gloomspeak | 
|---|---|
| Vox | Voxian |
|---|---|
| Diona | Sylvanic |
|---|---|
| Arachnid | Arachnis |
|---|---|
| Silicons (Cyborgs and AI) | Encoded Audio Language |

Some other species, like monkeys and kobolds, and even antagonists, like syndicate agents and nuclear operatives, can also speak different languages

| "Species" | Language Name |
| Syndicate Agents and Nuclear Operatives | Codespeak |
|---|---|
| Pirates | Piratespeak (Default language) |
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

Any other creature not covered here speaks what they already say ingame. Syndicats still meow, and space carp still 'raw'

### Special interactions

Understanding a language is only the halfway to speaking it. There are some specials interactions in that you can understand what is being said, but you cant speak it. These are:

1) Slime People can understand the Slime language (So understand what a slime is saying if they, for example, say hello), but cant speak it.
2) Arachnids can understand the Spider language, but cant speak it.
3) Although monkeys, gorilas and kobolds dont speak the same language, they can both understand each other languages clearly.

### Ways to learn different languages

The best, fastest and easiest way to learn all languages is spawning or arriving on the station as a Librarian. Their years of study have allowed them to understand and speak basically any language imaginable.

The other way to learn to speak and understand a different language is through Salvage. They can find discarded language manuals through debris and expeditions that upon used, it will consume the manual and the user will learn the language specific to the language manual it used(If its the draconic language manual, the user will learn to understand and speak draconic if they arent a Reptilian).

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
| Draconic | ,d |
|---|---|
| Moffic | ,m |
|---|---|
| Gloomspeak | ,g |
|---|---|
| Voxian | ,v |
|---|---|
| Sylvanic | ,s |
|---|---|
| Arachnis | ,a |
|---|---|
| Encoded Audio Language | ,u |
|---|---|
| Codespeak | ,t |
|---|---|
| Piratespeak | ,p |
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

### Examples of each languanges "gibberish"

| Language Name | "gibberish" |
|---|---|
| Draconic | "Ss rueh usuh shzuul lusr sk huro sz uk oru he elolso ar. Rsku suok sz zalo uh iksuah. Rasi si ilro sh sielo. Ek." |
|---|---|
| Moffic | "Sekygglitomånkönvii. Detdetdår møtmå. Ån. Gårköndagint. Viitehjaomköntyclaviinæbraånhönledetygglithankäytokmo sek." |
|---|---|
| Gloomspeak | "Qix quum. Qil qoovol qilzixqr quum. Zaoo qr*vol qil xrim qu-uuzix !qu-uu qil volqu-uu zix." |
|---|---|
| Voxian | tititihi SKREAHKEHK hikikikikiya EHKRAWK KRAKA yayichi chakah SKREAHKEHK titihi KRAAAA EEE KIIIKRI KA |
|---|---|
| Sylvanic | "Nasyu qip. Maaeobwex tisyudilamel tok. Eresnas aeqedointyuala haqipbalriifalbisvilbisinthaaearasbisalaqeuis. Pii." |
|---|---|
| Arachnis | "Clink-Click-Clink Hizee Click Hummme-Hunnee Hunne Cli. Clivk Hizee-Click Akkk-Hizee Akk. Vek Click Cli Hummne" |
|---|---|
| Encoded Audio Language | "Tzzzwurrboopbeepkssshbeephissbuzz keeyhsshisshsswurrboopdoo wahh. Buzzdoohisshssbeepboopbeepkeeyhss. Tzzzdeebeep." |
|---|---|
| Codespeak | "Nettles, hats, vodka and tonic, airlocks, zombies, engineering, Lawyer, petes, Captain, hungry, white russians, Darell Briner, peaceful, drunken blumpkin." |
|---|---|
| Piratespeak | "Timbers grog scallywag timbers scallywag scallywag matey me matey timbers rum shiver arr bucko bucko blimey shiver." |
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