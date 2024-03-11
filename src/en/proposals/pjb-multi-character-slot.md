# Multiple Character Slots

| Designers | Implemented | GitHub Links |
|---|---|---|
| PJB3005 | :x: No | TBD |

## Background

Currently, a player can have one character slot selected. This controls their character's appearance, name, job preferences, and antag preferences. This is relatively restrictive, as people may want to have different settings per job. For example:

* Some people prefer having different characters per job or department, for roleplay reasons.
* The work on [loadouts](https://github.com/space-wizards/space-station-14/pull/25715) makes it so that loadouts are assigned per-job, which is kind of clunky.
* Allows people to set names for special roles such as clown or borg, without needing to have separate fields for that like some SS13 servers do.

## Proposal

It should be possible to have multiple character slots active at once. When selecting jobs, a job is picked for all your characters at once, after which the actual character slot is picked.

All the regular properties of a character slot apply. You can have separate names, appearances, and with the loadouts PR separate loadouts too.

As an example: if you have two character slots, one engineer, one medical doctor, the game will try to give you a job for either. The actual character slot then gets picked based on what job you got.

### UI

Most of the UI would remain mostly the same.

The character customization screen currently lists all your characters in a column on the left. With this change, it'd create two separate headings: one for "active" and one for "inactive". There would be buttons to activate/deactivate character slots.

The lobby currently shows your active character in the menu. With this change, that would instead show all your character slots lined up horizontally. This is also nice because if you do take advantage of multiple character slots this allows you to easily tell "I have engie, med and sec selected".

We will probably need a "duplicate" button to allow you to clone a character slot, if you want to make a character slot with the same appearance but a different job easily.

### Job/character selection

The game would run job selection first, with your apparent job preferences selected as the union of the preferences of all your characters. Then when a job has been picked for you, your character slot is picked based on what jobs are selected on your characters. If more than one character has the job selected, it'd just be picked randomely between them.

#### High Priority selection

Currently you can only have one "high" job preference. I'm not sure how this proposal would play in with that, as you'd obviously be able to have multiple characters each with their own high preference set. I can think of two solutions:

* Just allow this. This means people can have multiple "high" job preferences in practice. I'm not sure it's a big deal?
* Have the ability to select a character slot as "high" as well, and then ONLY that character slot gets high preferences, all the other character slots will have their "high" set to "medium".

### Alternative character types

This approach also opens up the way for "alternative" character slot types. Right now all character slots are "humanoid", which makes little sense for roles like borgs. Instead of selecting borg / AI as regular jobs, we may instead want to make a wholly new character slot type instead. May also make sense for antags like nukies.

To make this not confusing for existing players, we probably want to make the jobs and such still available through the regular selector, with a hint that's like "if you want to customize the borg name, make a new character slot!" or something.

### Character Slot count

Especially if we make dedicated character slot types for silicons/antags, we'll probably need to increase the max character slot count a bit.

### DB changes

Changes to the database would be minimal. Instead of having an "active character slot" index we'd just change each character slot to have a bool.