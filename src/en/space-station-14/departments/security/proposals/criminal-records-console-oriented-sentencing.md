# Formalized criminal records

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| Lukasz825700516 | Lukasz825700516 | :x: | TBD |

## Overview

Streamline criminal records computer usage by enforcement of filling small charge form, 
with new PDA app that can be used to prepare documents for later submission.

## Background

Currently the only trace the sentencing process in security leaves is information left
in the criminal records computer, which most of the time doesn't specify the exact crimes
given criminal committed. This leaves burden on security members to remember every crime 
that has been committed on the station for:

- cases of repeated offenders
- providing lawyer information to work with
- niche roleplay opportunities - court trials, arguing against criminal to get certain access at HOP, and more

In case such information doesn't properly get saved on paper/computer, for other players
to use it may increase tension between security officers, lawyers and crew due to 
lack of communication or incompetence.

## Features to be added

To ease all that new security related PDA app will be added, and be installed round 
start for warden and head of security, and its cartridge be as well available in warden's locker.
The purpose of the new app will be to simply provide easy to fill out form containing
all charges of given individual. The app will allow players to:

- select name of crew member
- select crimes the individual committed
- select criminal status
- add a note
- print filled out form with extra information when it was printed, what would be highest sentence
and if given charges validate permanent confinement or execution

Such document could be then presented to criminal and their lawyer, or other crew members.
If everyone was happy with it, it would be inserted into criminal records computer to 
automatically update records,
and if needed printed form computer to get more official looking document.

Alternatively such document could be just printed, slightly edited, and stamped by HOS to 
create search warrant for someone, so security is more compelled to perform them during green 
alerts in case of trespassing or other minor crimes.

All this new UI would be also available to any security officer from the criminal records computer,
in case warden is missing.

## Game Design Rationale

Although, all security is expected to know space law, I doubt there are any players
that during sentencing process dont have guidebook open to check if their charges
are valid or if sentence time makes sense.
Moving sentencing process into more streamlined *box checking* helps security with
following space law, by disallowing them on mechanical level to set multiple linked crimes.

## Roundflow & Player interaction

Ability to print copy of specific criminal records should not impact by much 
erasure of criminal records done by ninja, as:

- in case warden always print charges: submission of charges into criminal records 
computer would consume the paper (NT privacy reasons? so they wont just get thrown into the disposals)
- in case someone always prints updated criminal records: this can already be done,
if anyone is willing to keep track of this using pen and paper (on note taking app)
- when ninja strikes security, someone always just clears all bogus criminal records, 
and reenters those which they remember.

In cases where crew members just behave suspiciously or were seen trespassing,
security would just like normally set them to suspicious add some note why, and
maybe set crimes they committed. This could be then printed, document modified 
by adding header like "search warrant", presented to HOS, and then used to for 
performing search on green.

In case crew is behaving more antagonistically, their criminal records could be 
updated on the fly as their crimes are being communicated to the warden, so later
when antagonist gets arrested, they can be presented with all their charges in 
written form.

Lawyer in all this would have bigger chance to reason with security in case their
charges are invalid, as security would be compelled to show document containing 
names of actual crimes, and not just rely on inaccurate verbal communication -
instead of what crimes were committed, lawyers would ask how specific crime 
has been committed.

## Administrative & Server Rule Impact (if applicable)

This change only provides easier access to existing feature - setting specific
crimes, instead of only providing note in criminal records console.

# Technical Considerations

This feature could be split into parts:

1. space law crimes are data driven
2. new UI for criminal records computer, and PDA version
3. handling information changes on paper

To not increase maintenance burden, UI should be written in such way, that any 
changes to space law, would automatically be reflected in it. It would require 
changing the crimes listing (table in guidebook) to work like listing of all chemicals.

For the criminal records computer and new PDA app would probably share the same 
UI, but in case of the app, the printing code should be made so it is also shared by
the logprobe app, and possibly other apps that allow for document printing.

For handling any changes that were made to printed paper before it was inserted
into the computer, new system and component would be added, that purpose would be 
be updating the state of the attached component to the paper after it was edited.
Parsing the text on paper could be done by reliance on formatting tags and overall
text format. Text parsing could be an expensive operation, but it would be only 
performed when the paper got edited.

Having separate system that would handle modifications, instead of leaving it to 
criminal records computer system would allow the printed charges to get unique 
inspection text, and possibly inform players that they broke it during edition.
