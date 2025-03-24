# Creating, Editing, and Deleting Station Records

<h1><b>THIS DOC IS IN AN INTERMEDIATE STATE! THE TEXT HAS BEEN UPDATED, BUT THE MOCKUPS ARE FROM AN OLD DRAFT! DON'T THINK TOO HARD ABOUT THE MOCKUPS RIGHT NOW BECAUSE I AM WAITING FOR MORE INPUT ON THE TEXT BEFORE I PUT IN THE EFFORT TO MODIFY THE MOCKUPS!!</b></h1>

| Designers  | Implemented | GitHub Links |
|------------|-------------|--------------|
| Centronias | :x: No      |              |

Station records track crew members "on paper". They're effectively the "truth" which ID cards represent, they're used to
look up information about criminal suspects, and in the future, they'll perhaps track medical information like blood
type. As it stands today, though, station records are created on round start and are immutable from then on (latejoins
notwithstanding), which leads to some pain points across the game. This proposal describes how Station Records could be
created, modified, and deleted diegetically within the game, but before we get to the proposals, I'd like to enumerate
the pain points to better motivate the changes, and I'd like to also explicitly deny some ideas to focus consideration.

### Pain Points

1. Visitors, adopted noncrew, etc. cannot be added to station
   records ([issue](https://github.com/space-wizards/space-station-14/issues/22503))
2. Destroyed records cannot be recreated
3. Known antagonists who are not in station records cannot be tracked by criminal records
4. Crew members who are known to have had their biometrics changed cannot have their records updated
5. Silicons determine crew membership based on HUD job icons rather than something more intentional

### What this Proposal _doesn't_ Suggest

1. Maintenance of station records will involve a ton of text entry
2. Station records can be modified to give silicons freedom to validhunt

## Record States

Today, the existence of a station record for an individual implies that that individual is a member of the crew, and it
gives no indication of their state of being. As part of enhancing station records, two new attributes will be added:

1. Crew Membership
    - Either `Crew` or `Non-Crew`
    - This value would be used to determine which records should be shown on the manifest (`Non-Crew` would not be
      included)
    - This value would be used by silicons to determine crew status
    - Recorded `Non-Crew` would enable roleplay for things like registering a captured Lone Operative as they're being
      processed in the brig.
2. Status
    - One of `Alive`, `Dead`, or `Missing`
    - This value would be used to determine which records should be shown on the manifest (Only `Alive`, or perhaps all
      are shown, but non-`Alive` are shown with their status)
    - This value would be used for other systems
        - e.g. Mail will not be sent to non-`Alive` crew

## Adding new Station Records

The ability to add new station records would go a long way to addressing the problems above, but it's critical that
the records reflect the actual situation on the station so as to prevent exploitation of other systems. All this means
is that records can only be added for individuals who definitely exist and who are not already represented by an
existing record. This limitation is enforced by requiring records to include DNA and fingerprints, and for those values
to be unique in the system. Mechanically, addition of station records would be performed on the existing Station Records
Computer with the following flow:

* Collect biometrics ([biometer](#collecting-and-entering-biometrics-for-new--edited-records))
* Use the new button in the Station Records computer:
  `Add Record` ([mockup](#station-records-with-add-and-edit-buttons))
* Clicking this button opens a new UI window which accepts the information required to create a new
  record ([mockup](#add-a-new-record))
* Submitting this window creates a new record with the given information
* At this point, the record would indicate non-crew, so the record could optionally be upgraded to crew here

Technically, this should be straightforward, as it'd just involve "reserving" a new station record key and creating the
associated station record entries just like on roundstart.

In terms of gameplay, this would give the Head of Personnel more things to do, though only rarely. It's not required by
the game, so some HoPs may choose to not do this at all.

## Editing & Deleting existing Station Records

Records are not deleted; instead they are marked with a non-`Alive` status. There should never be a case where a record
*needs* to be deleted. If a situation like this occurs, it should be prevented by some design effort.

Records are mostly immutable. The exceptions are fields useful for roleplay and not critical to gameplay (e.g. Name and
Gender); and Status and Crew Membership, which specifically exist to be modified. Note, again, that Crew Membership can
be modified from `Non-Crew` to `Crew`, but not the other way -- once somebody is crew, they are crew forever.

Mechanically, edits are easy enough to implement:

* New button in the UI of the Station Records Computer:
  `Edit Record` ([mockup](#station-records-with-add-and-edit-buttons))
* Clicking this button opens a new UI window which shows existing information in editable text boxes /
  dropdowns ([mockup](#add-a-new-record))
* Submitting this window applies any changes to the records.

Technically, this should be really straightforward. The records already exist, we're just changing the values. This is
already implemented for criminal records.

## Limiting Access to Station Record Editing

Station Records are quite sensitive information, so the average greytider shouldn't be able to edit them. A simple
solution to this could be something like the lock on the AI Upload Console: a machine-level toggle-lock which, when
unlocked, enables the use of any non-read capabilities of the computer.
([See explanatory text in mockup](#station-records-with-add-and-edit-buttons))

## Collecting and Entering Biometrics for New / Edited Records

Typing DNA and fingerprints manually sucks, and there's not a good way to get this information for new records. To solve
both problems at once, meet the "Handheld Biometer", a device similar to the Detective's forensic scanner. The Biometer
would be used to collect biometrics from humanoids and automatically enter that information into the Station Records
add UI. Specifically, the workflow would look like this:

* Person is at the HoP to get their record modified
* HoP picks up the Handheld Biometer, uses it on the person
* After a brief wait, the Biomete completes, storing the collected information internally
* The HoP opens the Station Records computer, open the `Add Record` window
* The HoP enters the name of the person manually (it's not a biometric which can be measured)
* The HoP, with the Biometer in hand, clicks a button, and the rest of the biometric information is miraculously entered
  automatically ([`Upload from Biometer` in mockup](#add-a-new-record))

The Biometer would include a UI for viewing the collected information, and that UI could include the ability to print
the information (both just like the Forensic Scanner). The Biometer would retain whatever information it's got until
another scan is performed, overwriting its internal contents.

This item, being unique and important for a part of the HoP's gameplay, should spawn in the HoP's locker and likely also
be a steal target like other unique command items.

## New Interactions and Possibilities

Beyond what's described above, there're a bunch of avenues for future enhancement:

- Add a ninja objective for mangling crew records, analogous to their objective for criminal records
- Add a thief objective for stealing the biometer
- Have the records stored in a server rather than nebulously just existing
- Some big refactor that makes it so that a lot of information isn't stored on IDs (at least diegetically), and instead
  IDs just reference crew records and systems (diegetically) get the record ID from the ID item and then have to look it
  up (eg. Visitor IDs aren't registered on the local station, so they'd show up as `?` rather than `V` in the ID HUD)

## UI Mockups

#### Station Records with add and edit buttons

![](station-records-mockup.png)

#### Add a new Record

![](add-record-mockup.png)
