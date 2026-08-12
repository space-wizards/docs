# Accent Guidelines

If you are looking to add a new accent (e.g. Spanish, German, or something more silly like Pirate), please follow these guidelines.

## Accent Definitions

Accents in the game come in two types: Tonal Accents, and Dialects.

**Tonal Accents** aim to emulate the sound of someone speaking the words typed into the chatbox, without any changes to the contents of what is being said. An example would be a Southerner accent changing `something` to `somethin'`.

**Dialects** aim to emulate how someone from a certain area, genre or other source would speak in conversation. This includes accent changes, but also word substitutions and changes to sentence structures. An example would be a Cowboy accent changing `friend` to `partner`.

Accents are generally applied in two different ways: Programmatically, and Word Replacement. 

**Programmatically** applying an accent is done by following some sort of hard ruleset as defined in code. This is mostly achieved via Regex, and can produce results such as replacing all `-ing` word endings with `-in'` (e.g. `something` to `somethin'`). Programmatically is the preferred way to achieve Tonal Accents.

**Word Replacement** uses a pre-defined list of source words linked to replacement words. This can be used both for Tonal Accents and Dialects, depending on if the word being replaced is applying a tonal rule that is hard to do programmatically (e.g. Scottish's `shit` to `shite`) or if it's a word substitution (e.g. `friend` to `partner`). 

Note that accents do not have be strictly grammatical; emulating someone asking a question with a Spanish accent can be done by adding a `¿`-prefix (e.g. `¿What?`), and a Pirate accent can be enhanced by adding a "Yarr!" to the start of a sentence. Care should be taken to ensure that this does not reduce the legibility of the speech however.

## SS14 Accent Rules

SS14 aims to have accents that enable players to roleplay as being from different areas and cultures. These accents *must not* rely on offensive stereotypes, regardless of how they are achieved in the game.

**Trait accents** are selectable during character creation. These are *only* allowed to be Tonal Accents, i.e. no word typed in the chatbox should be distinctively different to what comes out of the character's mouth. 

**Conditional accents** are unavailable during character creation, but may be applied to characters through in-round means such as via clothing, reagents or ghost roles. These may be either Tonal Accents or Dialects and may be more humorous in nature, such as a Cowboy or Pirate accent. 
