# Librarian Gameplay

| Designers | Implemented | GitHub Links |
|---|---|---|
| TheShuEd | :x: No | TBD |

> WIP

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

| Book | Description | Discipline keywords | Legality |
|---|---|---|---|
| The legend of the Dagger of Withering | A special melee weapon that sprays Plant-B-Gone during attacks. It is extremely effective for fighting kudzu. | 3 Biology + 2 Military + 1 Mysticism| ✔️
| The story of wizards with silly magic wands and owls | A reference to Harry Potter, a self-loading ranged weapon that shoots rainbow projectiles with minor damage. | 7 Mysticism + 3 Military | :x:
| The Stargate | Unlocks a complex crafting sequence that allows engineers to create gates for teleportation to planets (Current Gateways) | 18 Engineering + 2 Musticism | ✔️

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

Disciplines are categories of knowledge. Different categories of knowledge allow you to study different crafts, and also differ in the complexity of obtaining this knowledge.
| Discipline | Methods of obtaining | Application topics |
|--|-----|---|
| Mysticism | Librarian, Priest, Reporter. Folklore reference books that can be found at the pietyvend, bought in cargo or found on expeditions. | crafting mystical and occult items. |
| Techinc | all kinds of engineers, all scientists. Reference books about ancient technologies that can rarely be found in the lockers of scientists and engineers. Buy in cargo or find it on expeditions. | crafting of technological homemade devices. |
| Biology | The cook, the botanist, all the doctors. | Biology reference books that can be found in the medical department, bought in cargo or found on expeditions. | living beings, implants, biomechanics. |
| Military | The entire security service. Reference books on military technologies that CANNOT be bought, only found in the armory or on expeditions, or bought in traitor uplink. | weapons, and other dangerous things. |
| Social | All roles. It can be found randomly everywhere. | Funny things |

Each book with secret information is made up of N keywords. Keywords are replaced with gibberish, and when you look at the book, you can only see this gibberish text.
The book can consist of keywords from different categories. For example: the pie thrower is studied for 1 Military and 7 Social keywords.

The librarian's task is to find which gibberish words which keywords mean.
The following 2 ways can help him in this:
1) Special reference books-dictionaries. These are special books that explain the meaning of a series of 3-6 random keywords. These books are grouped by discipline, for example, "History of Biology, Volume 1". 
2) Communication with the players. All players at the beginning of the round receive "knowledge" about some keywords. It depends on the discipline: For example, an engineer will know 10 words from the discipline "Technic" at the beginning of the round, and a scientist 5 words from "Technic" and 5 words from "Mysticism". These players, having encountered gibberish in the text in conversation or when reading, will automatically understand what this word means.

As a result, a librarian needs to either communicate with people with requests to read books and share crumbs of information, or dig through dozens of reference books in search of the right meanings of incomprehensible words.
When the librarian finds the meaning of the desired word, he can start work on translating the book.

The librarian has a new **"Book Decryptor"** structure, located in the library. It looks like an old dusty computer with a analog keyboard.

This decryptor has 2 slots for books, and an interface with the following elements:
1) The text of the first book
2) The text of the second book
3) A field for entering gibberish
4) A field for entering keywords
5) Button "Encrypt"
6) The percentage of decryption of the book and known information

To get started, the librarian must put the book he wants to decrypt into the decryptor, and then put the empty book in the second slot.
After clicking "Decrypt", after a 30-second delay, the decoder turns an empty book into a "[source book name] research project", with 0% decrypting status

The process of decrypting a book is a value from 0 to 100%. The higher this value, the more decrypted information about the source book can be found out.

|percentage of decryption|Unlocked book data|
|--|----|
|0%| Discipline |
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
```

The librarian enters a pair of "Gibberish / keyword", click "Decrypt" and after a 30-second delay, the following may happen:
1) The pair was decoded correctly. If this pair is used in the current encrypted book, then the decryption of this word is recorded in its examined copy. This increases the decryption scale, and can open up new data about the book according to the table above.
2) The pair is incorrect, or is not used in the current workbook. Nothing happens

Thus, the librarian needs to find all N keywords, and correctly enter them into the decryptor, which will lead to a complete decryption of the book and the ability to use random crafting written in it.

#### Using

What to do with a fully studied book and the information in it is entirely the librarian's will. You can spread illegal knowledge around the station, you can give it to the command. If the crafting recipes are quite complex and require serious resources, give them to engineers for construction.

As a result of the librarian's work, access to special subjects and knowledge appears at the station, and it is the librarian who decides who and how to receive them.
