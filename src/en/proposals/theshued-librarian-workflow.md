# Librarian Gameplay

| Designers | Implemented | GitHub Links |
|---|---|---|
| TheShuEd | :x: No | TBD |

``` WIP ```

## Overview

This proposal aims to improve the gameplay cycle of the "Librarian" role, by adding unique gameplay relevance to it in the round. 
Reviewing briefly: it is suggested that encrypted books be added, by studying which the librarian can improve the quality of life of departments or antagonists.

## Design Pillars

### Sociality is the key to success.

The librarian is a role about learning about books and interacting with people. 
On its own, the librarian is only concerned with processing information and distributing it.
To do his job, he **must** communicate and negotiate with other people. 

### Multidisciplinary
The librarian's activities should be able to interact with all departments in the game in two ways:
1) The departments have the opportunity to assist the librarian in his work
2) The librarian's work can improve the quality of life of the departments.

This also applies to antagonists. The librarian can be helped by the antagonists, and the librarian's work can help the antagonists.

### Non-deterministic

Given the concept of working with information, for the following principles to work, this "information" must be randomized each round.



## Implementation

### Encrypted books

The librarian's entire gameplay will revolve around encrypted books.

All books initially have encrypted titles and a random appearance, which does not allow you to immediately understand what kind of knowledge it is.
But under the encrypted appearance is one of the specific books that have the following parameters:
| Parameter | Type | Description |
|---|---|---|
| Discipline | List<Enum> | All books relate to specific well-defined disciplines. Books can be related disciplines. This affects which department can help you study this book.  (For more information, see the research section)
| Legality | Bool | Illegal books carry dangerous knowledge, and the security service needs to control what exactly is being studied in order to prevent the leakage of dangerous knowledge to ordinary personnel. |
| Difficulty | Int | Determines how difficult it is to study this book. It directly affects the number of hash codes required (Easy - 2, Medium -4, Hard - 8). The higher the difficulty, the more time it takes to study, the more difficult it is to hide the fact of studying, and the more valuable the reward should be. |
| Result book | EntProtoId | The final decrypted book, which the decrypted copy will turn into after studying. |

#### Crafting recipes books
This category consists of a recipe for items that have randomized crafting each round. The successful decoding of the book is a literary story with a description of the crafting sequence of the item.

This is an alternative way to explore powerful equipment that does not concern the scientists department.
The items in this category are thematically more related to "mystical" "alien" and "homemade" than to "high-tech"
The book can contain recipes for crafting 1 or mane item, or complex structures.

Also, this category should be a good source of references to existing fantasy or sci-fi books.
To begin with, the following items are proposal:

| Book | Description | Discipline | Legality |
|---|---|---|---|
| The legend of the Dagger of Withering | A special melee weapon that sprays Plant-B-Gone during attacks. It is extremely effective for fighting kudzu. | Biology | ✔️
| The story of wizards with silly magic wands and owls | A reference to Harry Potter, a self-loading ranged weapon that shoots rainbow projectiles with minor damage. | Mysticism | :x:
| The Stargate | Unlocks a complex crafting sequence that allows engineers to create gates for teleportation to planets (Current Gateways) | Engineering | ✔️

#### Books of skills
This category of books teaches the reader special new abilities (Mind actions from Keron). Successful decoding of the book allows anyone to read it to learn new skills.
The study is a fairly long doAfter, during which the player can actually read any decoded story.

There may be weak magic spells, various melee techniques, or theft without gloves techniques and much more.

To begin with, I suggest some of the following ideas. Each idea, of course, requires its own c# scripts, and is difficult to replenish.

| Book | Description | Discipline | Legality |
|---|---|---|---|
| The art of pickpocketing | Allows the player to steal items as if he were wearing thief gloves. | Social | :x:
| Advanced Botany Manual | Allows you to inspect hydroponic trays and get more information about plants and mutations | Biology | ✔️
| Necronomicon | Allows you to summon Cerberus | Mysticism | :x:
| 1001 ways to succeed in life | allows you to receive 10% more money when selling items in cargo | Social | ✔️

### Gameplay cycle

The whole gameplay of Librarian can be roughly divided into 3 parts, which form a cycle.
1) Searching for information
2) Analyzing and deciphering information
3) Dissemination of information

#### Searching

Every round, encrypted books appear at random points on the station (bookshelves, lockers, bedside tables). Their number is limited, they are not repeated, and not all of them may appear in the round.
These books have a random cover, and an unremarkable title and description. If you open them, you can only see gibberish text.

At this stage, the librarian is busy searching for these encrypted books. The search process may include:
1) Research of all available public places. 
2) Ask people to search in their departments 
3) Request access to departments to search for books
4) Salvage find ones on expeditions

People can also bring books to the librarian on their own. As you can understand, this stage is completely tied to socialization.





#### Researching

The whole researching is based on the search for information presented in the form of abstract "History Hash Code", or briefly - HH-Code

The HH-Code is a valuable piece of information that consists of 2 parts: Dates, and sequences of characters.
This code is randomly generated at the beginning of each round for all special objects. Different instances of the same ProtoId contain same HH-Code. But these objects must be easily reproducible, and not unique, so as not to block the possibility of further study of the book.
``` 
HH-Code example: 2984.12.14:HSGA-FEF3
```

Considering that the station will have a huge number of items with these codes in literally all departments, this looks like an extremely difficult task. But, the book has a "discipline", which is a clue in which department to look for the necessary data.
There are the following disciplines in total:
| Discipline | HH-Code items location | Research themes |
|---|-----|--|
| Mysticism | items related to cults, priest, and libraries. Things like altars, books, priest's clothes, the Bible and the like. Alien artifacts, anomalyes.| Magic things |
| Biology | organs, syringes, liquids, plants, products of botanists, some med stuff, the corpses of xenomorphs and various xenofauna. | body management skills, biological improvements. |
| Technic | various tools of the engineering and science department. | unusual technologies |
| ? | ? |
| WIP |  There are many subjects in other departments that need to be classified. |

Each of the disciplines generates 20-30 unique codes at the beginning of the round, which are then distributed among random thematic types of objects. (tools, clothes, machines, people)


The librarian has a new **"Book Decryptor"** structure, located in the library.
This decryptor has 2 slots for books, as well as an interface that allows you to enter hash codes, a "decrypt" button and all information about the copy being created.
To get started, the librarian must put the book he wants to decrypt into the decryptor, and then put the empty book in the second slot.
After clicking "Decrypt", after a 30-second delay, the decoder turns an empty book into a "[source book name] research project", with 0% decrypting status

The process of decrypting a book is a value from 0 to 100%. The higher this value, the more decrypted information about the source book can be found out.

|%|Unlocked book data|
|--|----|
|0%| Discipline and list of hash dates |
|33%| Legality |
|66%| True name and description |
|100%| The ability to learn a skill is unlocked or an unlocked crafting sequence is fully available |

at 0%, the player immediately receives information about the discipline and part of the HHcode, in the form of dates. It looks like this:

```
-- "Ngaad-trec book" research project --
Decrypt status: [0%]
Discipline: Biology and Mysticism
Name: Unknown
Description: Unknown
Legality: Unknown
HH-Codes reference:
| 2984.12.14 | 1923.07.21 |
| 2981.11.04 | 3001.04.21 |
| 2983.12.23 | 2455.08.12 |
| 1644.04.12 | 1982.11.01 |
```

Next, the player needs to find certain items on the station that store these hash dates. The following tool will help him to do this.

"Analyser of history echoes"
With this object, you can scan various objects, and it will store information about the last scanned object in itself. The player can open the analyser at any time and see what information is recorded in it.

Some items of historical value located in each department will present special information: Historical Hash code. 


Last scanning: 
Name: artifact container
Description: Used to safely contain and move artifacts.

The librarian's goal is to find items with the desired hash date in order to learn the second part of the HH-Code in the form of a sequence of characters.

this means that the librarian will need to interact with the department and study its "background" by scanning various objects in search of suitable codes.
Among other things, it provides a logical reason why the librarian is in very different places of the station (which is an interesting position if the librarian is an antagonist)

When the player finds an item with the desired first part of the HH-Code, he must return to the decryptor and enter the second part of the Hcode in the field. Pressing "Decrypt" and waiting for 30 seconds can lead to the following two results:
1) The HH-Code was entered correctly. The required field turns green in the book research, and the percentage of book research increases.
2) The HH-Code was entered incorrectly. The player has made a mistake, or is trying to brutalize. No fines.

The player's goal is to enter all the required hhcodes, finding all the necessary items accordingly.

33% of the information about the legality of this book is revealed to the player. If the book is illegal and the player is an antagonist, he will want to explore this book even more, as it can be useful. But the Head of Staff should check how the librarian's work is going to prevent the final study of a dangerous book.

at 66%, the player learns the title and description of the book, which allows him to understand exactly what result he will get if he studies this book to the end.

100%, after the last correctly entered HH-Code by the player, completely decrypts the book. This turns the study into a separate ProtoEntity, with its own properties. This book can be read by getting information about current recipes, or studied by getting a new ability. It would be useful to be able to copy books on a special machine in order to distribute copies at the station.

#### Using

What to do with a fully studied book and the information in it is entirely the librarian's will. You can spread illegal knowledge around the station, you can give it to the command. If the crafting recipes are quite complex and require serious resources, give them to engineers for construction.

As a result of the librarian's work, access to special subjects and knowledge appears at the station, and it is the librarian who decides who and how to receive them.
