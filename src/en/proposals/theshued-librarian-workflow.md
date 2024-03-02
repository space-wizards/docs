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
| Discipline | Enum | All books belong to one of the strictly defined disciplines. This affects which department can help you study this book.  (For more information, see the research section)
| Legality | Bool | Illegal books carry dangerous knowledge, and the security service needs to control what exactly is being studied in order to prevent the leakage of dangerous knowledge to ordinary personnel. |
| Difficulty | Int | Determines how difficult it is to study this book. The higher the difficulty, the more time it takes to study, the more difficult it is to hide the fact of studying, and the more valuable the reward should be. |

#### Crafting recipes books
This category consists of a recipe for items that have randomized crafting each round. The successful decoding of the book is a literary story with a description of the crafting sequence of the item.

This is an alternative way to explore powerful equipment that does not concern the scientists department.
The items in this category are thematically more related to "mystical" "alien" and "homemade" than to "high-tech"
The book can contain recipes for crafting 1 item, as well as many items, or complex structures.

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

People can also bring books to the librarian on their own. As you can understand, this stage is completely tied to socialization.

#### Researching

The librarian has a new **"Book Decryptor"** structure, located in the library.
This decryptor has 2 slots for books, as well as an interface that allows you to enter hash codes, a "decrypt" button and all information about the copy being created.
To get started, the librarian must put the book he wants to decrypt into the decryptor, and then put the empty book in the second slot.
After clicking "Decrypt", after a 30-second delay, the decoder turns an empty book into a "[book name] research project"


The librarian's main tool is the "Analyser of history echoes"
With this object, you can scan various objects, and it will store information about the last scanned object in itself. The player can open the decryptor at any time and see what information is recorded in it.

Some items of historical value located in each department will present special information: Historical Hash code. 

The HH-Code is a valuable piece of information that consists of 2 parts: Dates, and sequences of characters.
This code is randomly generated at the beginning of each round for all special objects. And it can't be repeated on several objects.
``` 
Last scanning: 
Name: artifact container
Description: Used to safely contain and move artifacts.
HH-Code: 2984.12.14:HSGA-FEF3
```


The process of decrypting a book is conceptually the creation of a decrypted copy by a librarian. 
The original book always remains visually incomprehensible, so it makes sense for the librarian to label them with stickers.

(Mysticism - Chapel, Social - Service , Tech - RnD and Eng, Biology - Med and Botany, Alien )


