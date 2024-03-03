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
| Discipline | List<Enum> | All books relate to specific well-defined disciplines. Books can be related disciplines. This affects which department can help you study this book. |
| Legality | Bool | Illegal books carry dangerous knowledge, and the security service needs to control what exactly is being studied in order to prevent the leakage of dangerous knowledge to ordinary personnel. |
| Result recipe | ProtoId | Books consists of a recipe for items that have randomized crafting each round. The successful decoding of the book is a literary story with a description of the crafting sequence of the item. |

This is an alternative way to explore powerful equipment that does not concern the scientists department.
The items unlocked by books are thematically more related to "mystical" "alien" and "homemade" than to "high-tech"
The book can contain recipes for crafting 1 or many item, or complex structures.

Also, this category should be a good source of references to existing fantasy or sci-fi books.
To begin with, the following items are proposal:

| Book | Description | Discipline | Legality |
|---|---|---|---|
| The legend of the Dagger of Withering | A special melee weapon that sprays Plant-B-Gone during attacks. It is extremely effective for fighting kudzu. | Biology | ✔️
| The story of wizards with silly magic wands and owls | A reference to Harry Potter, a self-loading ranged weapon that shoots rainbow projectiles with minor damage. | Mysticism | :x:
| The Stargate | Unlocks a complex crafting sequence that allows engineers to create gates for teleportation to planets (Current Gateways) | Engineering | ✔️

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

At the beginning of the round, 2 tables are taken: Keywords, and gibberish. additionally, keywords are grouped by discipline, for better theming. Each keyword is assigned a specific gibberish word. Example:
| Keyword | Discipline | Gibberish |
|---|---|---|
| Legacy | Social | Grauugha |
| Bluespace | Technic | Pupilo |
| Clown | Social | Filurgha |
| Tesla | Technic | Hiiski |
| Revenant | Mysticism | Jubaijin |

Each book with secret information is made up of N keywords. Keywords are replaced with gibberish, and when you look at the book, you can only see this gibberish text.

The librarian's task is to find which gibberish words which keywords mean.
The following 2 ways can help him in this:
1) Special reference books-dictionaries. These are special books that explain the meaning of a series of 3-6 random keywords. These books are grouped by discipline, for example, "History of Biology, Volume 1". Such books can be: bought in cargo, found on an expedition, accidentally found in maints.
2) Communication with the players. All players at the beginning of the round receive "knowledge" about some keywords. It depends on the discipline: For example, an engineer will know 10 words from the discipline "Technic" at the beginning of the round, and a scientist 5 words from "Technic" and 5 words from "Mysticism". These players, having encountered gibberish in the text in conversation or when reading, will automatically understand what this word means.

As a result, a librarian needs to either communicate with people with requests to read books and share crumbs of information, or dig through dozens of reference books in search of the right meanings of incomprehensible words.
When the librarian finds the meaning of the desired word, he can start work on translating the book.

The librarian has a new **"Book Decryptor"** structure, located in the library. It looks like an old dusty computer with a analog keyboard.

This decryptor has 1 slots for books, and an interface with the following elements:
1) 


<><><><> WIP WIP WIP <><><><>

as well as an interface that allows you to enter hash codes, a "decrypt" button and all information about the copy being created.
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
