# Loadout Character Select

| Designers | Implemented | GitHub Links |
|---|---|---|
| Saphire Lattice | :x: No | TBD |

## Overview

Change the character selection screen into having a flow to it, and putting loadouts front and center, rather than a side thought within a giant list. Proposed new look is to split it into three columns: jobs, loadouts and character(s). This changes emphasis away from the character player has selected, but rather what role they want to play as.

TODO: add the supplementary sketch here, for now leaving this here https://discord.com/channels/310555209753690112/1008709214006427689/1300145640327741450

## Background

Current character selection UI is alright, and the focus on characters is rather nice. But it focuses on characters to the exclusion of everything else and does not give proper emphasis to the roles. Loadouts are shoved off to the side and meld into a pile of buttons that most people likely filter out unless they know and purposefully give the button a poke.

Roles, or jobs, are also not clearly emphasised. The antag enrollment does not clearly differentiate between subversive roles that blend within the station population, and roles that spawn in away from the station and have their own look and loadout.

## Jobs Column

The leftmost/first column (note: what about RTL?) is dedicated to jobs, as well as antagonists that spawn separately. All jobs are listed as menu items vertically. The general design is to split the column itself into categories based on priority of the job, and antag enrollment. So the categories would be "Antagonist, High Priority, Medium Priority, Disabled". The sorting *within categories* should be done automatically based on job's importance, department or just alphabetic name. A good addition would be user controlled sorting - recently played, playtime.

The left part of the job menu item has a "< ||| >" vertical control that changes the position of the job when the arrows up/down are clicked, and the "|||" control should be a hint for drag-and-drop capability. The *entire* menu item can be drag and dropped within the menu.

Every job should note the amount of loadouts and/or characters within it, perhaps last played time. The rightmost part of the job's menu item should have a checkbox that deactivates that job from being picked at all, until user toggles it back on. The checkbox only reflects the state of the loadouts in aggregate and should have three states - all loadouts are inactive, all are active, and some of them are active. Clicking on the checkbox should toggle it between all inactive and all active. Partial loadout activation should be treated as inactive for this.

Clicking on a menu item should show all loadouts linked to the role. If a loadout with a character is already selected, then the first loadout with the same the character should be opened automatically.

If a character is selected, a hint should be given noted as to which roles they have a loadout in, perhaps a faint highlights along the leftmost border of the menu item.

TODO: Should categories be always shown to guide the player into knowing they can have these distinctions, or should they be hidden?
TODO: I was considering an "< ||| >" vertical control that could let user shift a job around in the list, and drag and drop. But should that bump a job between categories only, or should players be able to arrange jobs in an arbitrary order?
TODO: Should there be drag and drop interactions with character list? E.g. should dropping a job onto a character create a new loadout?
TODO: Quick controls for toggling every job on/off?

## Loadouts Column

The middle/center column, which describes a link between a job and a character. It should cleanly display the character's name and icon, as well as any *subversive* antag roles opted in for the character. If an alt job titles/subroles system is implemented, these should be also displayed distinctly and prominently.

TODO: Are subversive antag roles selected per-character or per-loadout? Which would be better, less confusing?
TODO: Related to above, should loadouts be able to override some things about the characters? If so, how should this be communicated in the UI?

## Character Column

It's the char gen UI. The topmost part should show a clear image of the character with the selected loadout.

This column should not have a fixed size and will fill in the rest of the screen so that the first two columns are not stretched out to the extreme.

Title bar should have a dropdown button than changes this column into alternative view, see [Character Dropdown](#Character-Dropdown)

The rest of this UI is undecided, likely reusing the current character creation UI.

It should be possible to drag and drop from any "inert" element of this UI, or if that's technically difficult, the character preview icon, into the job list, to quickly create a new loadout.

## Character Dropdown

This is the alternative view of the chargen UI. It should show characters in a way similar to the current character list. Where relevant, the preview icon of the characters should reflect their first loadout within the selected role. Hovering over any of the characters should highlight the roles and loadouts they are linked to, or gray out any that they aren't linked to.
