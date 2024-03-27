# The Informant Antagonist
| Designers | Implemented | GitHub Links |
|---|---|---|
| Krunklehorn | :x: No | TBD |


## Overview
The Informant is a minor, assisting antagonist designed to support other antagonists by delivering them random loot.  

A mix of covert espionage and Diablo-style treasure goblins, this antagonist is intended to be flexible between gamemodes and adaptable to player choice.


## Background
New design pillars have been created to differentiate antagonists. Recent changes to antagonist code are encouraging designs that are not bound to a unique game mode. This antagonist fits nicely between the Neutral and Major alignments as well as the Lone and Team categories, and can be neatly inserted into a variety of gamemodes.


## Briefing
_" You are a Syndicate Informant. Use clues to identify package recipients. Deliver packages to gain more clues.
Assist your fellows today or escape and continue deliveries tomorrow.  
Do not risk your identity or the identities of your package recipients. "_

### Goals
- Deliver each package successfully.
- Optional: Reveal yourself! Co-operate with your recipients to open your extra packages.
- Optional: Remain covert. Escape alive and unrestrained. Keep your extra packages sealed and on you.

### Locate
- Begin with one clue for each recipient.
- After each delivery, gain clues for remaining recipients.
- Use deduction and vigilance to succeed.

### Deliver
- Packages must make their way into their recipients inventory, that's all.
- Primary packages are sealed to their recipient's DNA.
- Extra packages are sealed to any recipient DNA, even recipients of other Informants.
- All packages can be opened by a cryptographic sequencer.
- All packages contain a single piece of minor syndicate loot.

### Escape
- Packages do not identify their recipients, but are obvious and will make you Valid™.
- Your packages and gear are valuable, reveal yourself at your own risk.
- Extra packages do not have recipients, you must escape with these.

### Starting Gear
- Standard job equipment
- 4 packages
  - 1-3 suspicious packages, each destined for a unique, current-round recipient.
  - 1-3 extra suspicious packages, open these if you wish, or keep them hidden.
- Courier's Gloves
  - Chameleon technology.
  - Wearer may discretely insert into equipment slots, pockets, hands and even worn containers!
  - Full containers drop the item beneath the recipient, oops!
  - Not useful for thieving.


## FAQ

#### "Greentext isn't everything, what stops Informants from emagging the extra package and going full murderhobo!?"
- Nothing really, however...your loot will always be minor, an emag is already worth 8TC and its use won't give you clues to find more buddies with.
- In terms of rules, the author suggests the following:
  - Informants may choose to open their extra packages at any time.
  - Informants may not invent their own objectives and must prioritize their deliveries.
  - Once all their deliveries are complete, an Informant may forfeit their final objective to assist in the objectives of other antagonists.
- In terms of mechanics: you gotta risk it all or play it completely safe.
- In terms of lore: Informants are carrying packages for other stations or future shifts.

#### "What counts as minor syndicate loot?"
- Grenade, noslips, smokes, ammo for a gun you're not using, pajamas lol
- Generally 1-6 TC, you won't get a holy hand grenade, could be an eshield though.
- Single items only, no bundles, bags, crates or boxes.
- Includes job specific items based on the job of the recipient.
- Bikeshed this into oblivion, the author doesn't really care how strong the rewards end up being.

#### "This is just a regular syndie with less TC locked behind Guess Who."
- Teamwork is incredibly powerful and way more interesting to balance than raw TC count.
- Informants get the benefit of knowing how many antags are in play and might even get an advance on who they are.
- Informants choose to cooperate with recipients at their own risk: initial infected, lone ops and greedy syndies can be terrifying.

#### "What if your recipient dies / goes to perma?"
- Your goal is to deliver, not open.
- Dead or zombified recipients still have hands.
- Recipients in perma make for great heist stories.
- Gibbed / borged recipients count as a loss: nobody likes a tardy courier, don't wait for the shuttle.

#### "Mail couriers are already a thing on SS13 / Frontier and somebody else even posted a design doc for them. Choose a different theme!"
- I don't see why both can't co-exist. The addition of non-syndicate mail tasks would create additional camouflage to the Informant's identity and their package system.


## Details / Playtesting / Bikeshedding
- "Recipients" may be traitors, thieves, initial infected or head revolutionaries.
  - Lone ops are never recipients because a recipient's intentions to kill should not be obvious.
  - For the same reason, Informants should not spawn during nukies.
  - The author admits they have no experience with pirates so...that's still up in the air.
- Recipients should outnumber Informants at least 3 to 1.
- Informants are rolled after major antagonists, but should be rolled after thieves too.
- Informants will never be multi-antagonists.
- Informants may late-join.
- Multiple Informants may have packages for the same recipient, but an individual Informant will not.
- Informants can share their clues with other Informants, but will never be recipients of another Informant's package.
- Informants should never get packages with a total potential TC above 24.
  - 1 regular + 3 extra
  - 2 regular + 2 extra
  - 3 regular + 1 extra
  - A successful Informant potentially adds 18TC to the round, plus any teamwork or information shared.
  - A looted Informant does add an extra 6, for a total potential of 24TC, but they won't be very kind and are likely to thwart the offender if they happen to survive.
  - An Informant's potential TC contribution is spread evenly between 4 packages, so even in the unlikely event that the loot adds up to 24TC, no syndicate bombs, holoparasites, L6 SAWs and other major items will come into play.
- Packages and clues are labeled: A, B or C
  - Multiple Informants can mix up their packages, oops!
- Examining a package should reflect the character's knowledge of syndicate methods:
  - All Informants should see the clue letter label: A, B or C
  - All potential recipients should get a short briefing.
    - "Syndicate loot! You'll want to take this somewhere safe before opening."
      - if DNA will work: "The wrapping paper shimmers as you run your fingers over the label."
      - if EMAG is required: "The wrapping paper is encrypted, but that's never stopped you..."
  - Everyone else should just get a curious or inquisitive phrase.
    - "Huh...valid. Wonder what could be inside?"
- Clues are split into two types, weak and strong...
  - Weak clues vary from being pinpoint accurate to borderline useless.
  - Strong clues should significantly cut the list of potential candidates.
  - A system is used to automatically scale the strength of clue rewards. (see code)
  - Examples of weak clues...
    - One or more recently acquired item(s)
    - One or more recently interacted crew member(s)
    - One or more syndicate code phrase(s)
    - One or more recently spoken word(s)
    - ... #ideagays
  - Examples of strong clues...
    - Species
    - Department
    - First/last letter of first/last name
    - Position on the manifest (top/bottom half)
    - Deceased status (at the time the clue was gained)
    - ... #ideagays
- Super last minute ideagay addition: The Informant's self-destructing stamp!
  - Sets a hidden timer and appends a 'this message will self-destruct in..." message to the bottom of the page.
  - The timer beings ticking the next time the document is read.
  - Once the time runs out, the paper crumbles into ash.


## Implementation / Outline
#### Current Unknowns
  - Need maint overall temperature check
  - Rule code and gamemode code are __FROZEN__, pending antagonist refactor
    - Enforce ratio
    - Prevent multi-antag
    - Fail during nukeops (and maybe pirates)
    - Handle examine text for suspicious packages (see bikeshedding)  
  - Package reward spawn lists
  - Examine text and description handling


#### Code Plans
- [x] Changes to Thief gloves:
	- [x] Changes to ThievingComponent:
    - Split both StripTimeReduction and Stealthy fields to differentiate between insertion and removal
    - Made Stealthy fields true by default
    - Add new bool WornStorageInsert
  - [x] New event: WornStorageInsertAttemptEvent
    - Event contains information on the user, target and worn entity
    - Event must be allowed by at least one subscriber
  - [x] Changes to Strippable component & system:
    - Component contains new bool AllowWornStorageInsert
    - BaseBeforeStripEvent contains new bool Insert
    - OnStripButtonPressed branch modified
    - System defines private bool CanInsertWornStorage
      - Fails if not allowed or the entity isn't a storage container
      - Calls WornStorageInsertAttemptEvent
      - Allows stealthy insertions to fail if the reason is not obvious to the user
      - PlaceActiveHandItemInInventory calls this during Check()
	- [x] Changes to ThievingSystem:
    - Branch during OnBeforeStrip
    - Subscribes to &lt;WornStorageInsertAttemptEvent&gt;
      - Requires the user be wearing thieving gloves that allow worn storage insertion
- [ ] Changes to trash wrappers:
  - [ ] Refactor all trash related items under one BaseTrash
  - [ ] Use BaseTrash to define new item: PackageTrash
- [x] New cancellable event: CheckDnaMatchEvent
  - Event contains an EntityUid for the user
  - Event contains a bool for whether EmaggedComponent should influence the result
- [x] New component & system: CheckDna
  - [x] Component contains a DNA string
  - [x] Component contains a bool for whether it can be emagged
  - [x] System defines private bool DnaMatch()
    - Succeeds on matching dna or emagged
  - [x] System subscribes to &lt;CheckDnaComponent, CheckDnaMatchEvent&gt;
    - Calls CheckDnaMatch, cancels on failure
  - [x] System subscribes to &lt;CheckDnaComponent, OnGotEmagged&gt;
    - [x] Handles the event if emaggable
- [x] New event: InformantPackageDeliveredEvent
  - Event contains an Entity&lt;InformantPackageComponent&gt;
- [x] New component & system: InformantPackage
  - [x] Component defines and stores a new enum: InformantPackageState
    - Unresolved: failure
    - Compromised: failure
    - Delivered: greentext
  - [x] System subscribes to &lt;InformantPackageComponent, EntGotInsertedIntoContainerMessage&gt;
    - Returns if package is not Unresolved
    - Raises CheckDnaMatchEvent
      - Disregards emag
      - Returns if cancelled
    - Sets package as Delivered
    - Raises InformantPackageDeliveredEvent on self
  - [x] System subscribes to &lt;InformantPackageComponent, UseInHandEvent&gt;
    - Before SpawnItemsOnUseSystem
    - Returns if package is not Unresolved
    - Raises CheckDnaMatchEvent
      - Handles and returns if cancelled
    - Sets package as Compromised
- [x] New item: BasePackage
  - sprite: basic looking
  - item: small, 1x2
  - SpawnItemsOnUse: PackageTrash
- [x] New item: PackageSuspicious
  - parent: BasePackage
  - sprite: valid looking
  - tags: SusPack
  - CheckDna
  - SpawnItemsOnUse: PackageTrashSuspicious
  - InformantPackage
- [x] New item: PackageSuspiciousExtra
  - parent: PackageSuspicious
  - tags: ExtraSusPack
  - SpawnItemsOnUse: PackageTrashSuspiciousExtra


#### (OLD, needs antag rework)
- [ ] New abstract prototype: BaseCluePrototype
  - Defines a bool for weak vs. strong, required
- [ ] New clue prototypes: XCluePrototype
  - Inherit from BaseCluePrototype
  - Name varies
  - One for each of the weak and strong clues
- [ ] New component and system: InformantCluesSystem
  - Component contains ProtoId&lt;BaseCluePrototype&gt; list for weak and strong clue prototypes
  - System contains entity query for all InformantRoleComponent owners
  - System contains a list of BaseCluePrototype
  - System handles all XCluePrototype data (OLD, also vague as hell, needs antag rework)
  - System responds to InformantRewardEvent by adding clues to InformantCluesComponent
  - System fine tunes clue strength based on the following parameters: (HOLY SHIT)
    - Crew manifest count: low pop should be weak clues only
    - Courier shift time: stronger clues for later-joining Informants
    - Overall shift time: slightly stronger clues as the round progresses
  - The strength system should not scale with any of the following parameters:
    - Successful deliveries: new clues already compound their strength with previous clues
    - Courier count: roll rules already enforce a ratio, no need to scale clue strength based on the ratio