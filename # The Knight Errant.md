# The Knight Errant

| Designers | Implemented | GitHub Links |
|2013HORSEMEATSCANDAL|Yea|https://github.com/space-wizards/space-station-14/pull/36069|


## Overview

A new addition to the pool of random shuttle events, the knight arrives in a slow, low-tech shuttle. 
They are free agents but are encouraged to do "knightly things" such as protecting the innocent
and slaying dragons. They are equipped with spaceproof plate armor (to fight dragons who like to go in space) and a claymore.

## Background

I thought it would be a fun addition, several members of the community including maintainers agreed with me. 
It also ties into the recent addition of the wizard.

## Features to be added

The current implementation is pretty basic, I'd like to add the code of chivalry, which is currently a book in their shuttle, as a set of borg-like laws that they must follow.
I'd also like to add more polish, like new sound effects and spawn stingers like the thieves and syndicate agents have, or new interactions with dragons and wizards, making them likelier to spawn when one of them is on a rampage. In the very long-term, I'd like to make this the introduction of a larger faction: the Space Kingdom of Glorgon, which is currently only referenced in the knight's description. They seek to take the sector over for their King, use medieval technology adapted for use in space and have a complicated relationship with the wizards.

## Game Design Rationale

I thought it would be a fun and simple addition to the game.

## Roundflow & Player interaction

This is a decently rare event spawn. I made them free agents who obey to a code that asks of them to obey their king, seek glory, protect the innocent and respect aliens. An admin may decide to send orders, posing as the knight's king. The knight's code encourages them to roleplay their character and think of what they would consider "harming the innocent". Is it the iron rule of security, or the scheming of the syndicate ? The respect aliens part is to avoid any alt-right crusader larping and speciesm. The last thing I will mention is that the knight's low tech environment can create a lot of interesting roleplay scenarios with the more technologically advanced crew.

## Administrative & Server Rule Impact (if applicable)

 In the current implementation, the knight's code of chivalry is more of a suggestion, which would make the knight about as easy to moderate as a closet skeleton. In the future, they'd be closer to a borg with ionned laws.

# Technical Considerations

The reason laws are more of a suggestion is because I'm not sure how to add laws to a non-borg, and make them immune to ion storms.