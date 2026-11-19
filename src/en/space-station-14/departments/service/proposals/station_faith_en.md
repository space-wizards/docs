# Station Faith and Chaplain Gameplay

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| aristophanivan | aristophanivan | :x: No | TBD |

## Overview

This proposal expands the Chaplain into a social role centered around building and maintaining a voluntary station congregation.

Each station receives one of several fictional religious traditions at the beginning of the round. The Chaplain and congregation develop that tradition through physical rituals, collective choices, personal vows, and recoverable religious objects.

The system is intended to produce player interaction and round-specific stories rather than act as a passive statistics tree or a way to identify antagonists.

## Background

Chaplain gameplay currently consists primarily of access to the chapel, Bible interactions, familiar summoning, and sending prayers to administrators.

These mechanics provide flavor, but do not form a sustained gameplay loop. The Chaplain has little reason to organize the crew, negotiate with departments, respond to changing station conditions, or make decisions that affect later religious activity.

Religion is also almost entirely expressed through player-written roleplay. This proposal does not seek to replace that roleplay or define what characters are allowed to believe. Instead, it provides physical tools and shared activities that players can use to create their own religious stories.

## Design Goals

The system should:

- Give Chaplains a social gameplay loop lasting throughout the round.
- Encourage voluntary interaction between Service and the rest of the station.
- Produce different congregations and stories each round.
- Create meaningful choices without establishing a mandatory optimal religion.
- Use physical objects, locations, participants, and resources wherever possible.
- Allow rituals to be interrupted, sabotaged, relocated, or rebuilt.
- Mechanically handle clear religious commitments without asking administrators to judge roleplay.
- Remain equally usable by crew and hidden antagonists.
- Leave room for additional traditions, rites, and doctrines after the initial implementation.

The system should not:

- Automatically assign a religion to every character.
- Mechanically judge whether ordinary violence or roleplay is morally justified.
- Turn Chaplains into antagonist detectors.
- Require administrators to answer prayers or enforce religious behavior.
- Give permanent station-wide combat bonuses.
- Make religious participation necessary for performing another department's job.
- Reproduce or mechanically rank real-world religions.
- Make one irreplaceable chapel object essential to continuing the round.

## Religious Traditions

Each eligible station receives one fictional tradition at round start.

A tradition supplies the congregation's initial theme, characteristic rituals, and the kinds of trade-offs offered by later doctrines. It does not establish the personal beliefs of the station's crew.

The initial implementation would use three traditions:

| Tradition | Theme | Typical Gameplay |
|---|---|---|
| Mercy | Care, shelter, sacrifice, and recovery | Treating others, protecting patients, sharing burdens, and communal meals |
| Zeal | Courage, ordeal, discipline, and consecration | Voluntary trials, risky temporary blessings, guarding others, and standing firm under pressure |
| Unity | Cooperation, fellowship, and shared responsibility | Processions, linked participants, communal resources, coordinated rituals, and group support |

These traditions should differ primarily in how players interact, not merely in which numerical bonus they provide.

All traditions are fictional and abstract. Players remain free to interpret their congregation's theology, aesthetics, deity, or lack of deity through roleplay.

## Joining a Congregation

Knowing that a station congregation exists does not make a character a member.

A character joins through a voluntary initiation rite involving the Chaplain, the initiate, and at least one witness. The initiate must explicitly consent before the rite completes.

Joining grants access to the congregation's rites, doctrines, and personal vows. A character may leave at an altar without publicly announcing their decision. Rejoining or converting should require another initiation rather than happen automatically.

This separates station gameplay from character background: a player may ignore the congregation, participate socially without joining, or formally join and accept its mechanical commitments.

## Piety and Congregational Development

The congregation accumulates a shared resource through successful rituals and religious service.

Piety should primarily reward:

- Bringing multiple unique players together.
- Performing rites relevant to current station events.
- Registering and distributing physical ritual items through an active rite.
- Completing processions or other exposed activities.
- Following mechanically verifiable commandments.

Repeatedly clicking a prayer verb or performing a rite alone should not be an efficient source of progress.

### Doctrines

A congregation develops through several required doctrine decisions. Each decision offers mutually exclusive interpretations of its current tradition.

Required doctrines define the congregation's overall direction. For example, Mercy might choose between emphasizing direct treatment and creating places of sanctuary.

The Chaplain proposes a doctrine, but it is ratified through a council rite involving members of the congregation. This prevents the progression system from becoming a single-player technology tree and gives other players a reason to discuss the choice.

### Aspects

Later, the congregation may adopt a limited number of optional aspects unique to its tradition.

Aspects provide specialization rather than straightforward upgrades. The congregation cannot adopt every available aspect, so different rounds should produce different combinations.

Adopting an aspect only makes its personal vow available. It does not force the aspect's restrictions or effects onto every congregant.

## Commandments, Ritual Taboos, and Personal Vows

Religious norms use three different levels of enforcement.

### Commandments

Commandments describe behavior the congregation wishes to encourage.

Completing a mechanically verifiable commandment may grant personal favor and a small amount of shared piety. Failing to perform a commandment is never punished.

Examples include:

- Treating another character's injuries.
- Bringing food to a communal meal.
- Remaining with a ritual group through an ordeal.
- Helping a linked partner out of danger.

Broader moral language may appear in flavor text, but only an explicit in-game action may produce a reward.

### Ritual Offerings

In this document, an offering is not an abstract gift to a deity. It is a physical item registered by an active ritual. Depending on the rite, this may be food, a candle, water, medicine, or another ordinary station item.

The ritual interface visibly marks the item and, when relevant, assigns it to a particular participant or ritual role. Ordinary items are never treated as offerings merely because they are placed near an altar.

An offering stops being tracked when the ritual ends or when the item is formally removed from the rite.

### Ritual Taboos

Automatic penalties apply only to actions that the server can attribute directly and unambiguously to a player. Each taboo and its exact violation condition must be shown before the player accepts the relevant rite or vow.

The initial implementation is limited to the following taboos:

- Consuming a ritual item that the active rite has explicitly assigned to another participant.
- Using the ritual interface to abandon an ordeal after explicitly accepting its final committed stage.
- Using the ritual interface to break a voluntary ritual bond while the linked participant is in a visibly displayed critical condition.
- Directly dealing damage to another character while benefiting from an explicitly nonviolent sanctuary.
- Directly damaging a body while it has an active and visibly displayed funeral or recovery preparation status.

Movement out of an area does not by itself count as abandoning a rite. Forced movement, incapacitation, disconnection, environmental damage, expired prompts, and actions attributed to another player never produce a violation.

The system does not evaluate motives or ordinary morality. It checks only the concrete actions listed above. A Security Officer shooting an armed suspect does not need to confess unless that officer voluntarily accepted a vow that explicitly prohibits the action.

### Personal Vows

The strongest benefits and restrictions are accepted individually.

When a congregation adopts an aspect, each member may review and accept its vow at an altar. The interface must disclose the benefit, drawback, and exact violation condition before confirmation.

Possible vows include:

- Improved treatment of others at the cost of personal combat effectiveness.
- Greater endurance at the cost of movement or recovery.
- Sharing damage with a consenting partner.
- Fasting in exchange for a situational benefit.
- Nonviolence in exchange for stronger healing.

A player may lay down a vow at an altar. This removes its effects immediately and prevents it from being retaken for a period of time. Leaving a vow is not itself sinful unless it also abandons an unfinished voluntary bond or rite.

## Favor, Sin, Confession, and Atonement

Members maintain private favor and sin representing their relationship with the congregation.

Following commandments builds favor. Breaking an explicit taboo adds sin. Accumulated sin weakens religious gifts and can eventually suppress them, but does not reveal anything publicly about the character.

Only the player can see their full record. A Chaplain sees a violation only when the player voluntarily presents it during confession.

Confession assigns an in-game penance appropriate to the violation, such as:

- Treating or feeding another character.
- Returning or replacing a ritual item recorded as taken or consumed.
- Helping purify a desecrated altar.
- Completing a communal rite.
- Assisting a previously abandoned ritual partner.

Completing the penance and returning to the Chaplain removes part of the character's sin. More serious atonement restores suppressed gifts but should not erase the character's history without effort.

Confession is content for players who knowingly accepted and broke religious commitments. It is not expected after normal combat or departmental work.

## Rituals

Rituals are physical, staged interactions rather than buttons that exchange a resource for a buff.

A ritual may involve:

- A celebrant and participants with distinct roles.
- Candles, food, water, blood, medical supplies, weapons, or a reliquary.
- Items placed at an altar or distributed between players.
- Timed actions or changes in formation.
- Carrying an object through the station.
- Explicit participant responses and consent.
- Safe points where a participant can withdraw.
- Failure caused by interruption, missing materials, environmental danger, or sabotage.

The initial content should provide a compact but varied set of rites. More rites can be added later without changing the core design.

### Common Rites

- **Initiation:** Voluntarily joins a character to the congregation.
- **Congregational Service:** The primary repeatable source of piety, requiring several unique participants.
- **Confession and Atonement:** Resolves explicit religious violations through player-facing penance.

### Mercy Rites

- **Anointing of Wounds:** Participants prepare and treat a patient together.
- **Vigil:** Stabilizes a dying character or prepares a body for later funeral interactions.

Mercy should provide useful recovery and protection, but should not replace Medical or guarantee resurrection.

### Zeal Rites

- **Consecration:** Temporarily dedicates an item to a declared purpose.
- **Ordeal:** A consenting participant accepts a controlled risk for a temporary benefit.

Zeal should offer risk and visible preparation rather than permanent raw combat upgrades.

### Unity Rites

- **Binding Circle:** Creates temporary, consensual links between participants.
- **Procession:** A group carries a reliquary through several exposed station locations.

Unity should become more effective through cooperation while remaining vulnerable to separation and disruption.

## Physical Counterplay and Sabotage

Rituals should interact with the existing sandbox.

Players may:

- Extinguish candles.
- Remove, steal, substitute, or contaminate items visibly registered to an active ritual.
- Take a reliquary.
- Damage an altar.
- Interrupt a procession.
- Pull participants out of position.
- Desecrate ritual space with appropriate substances.

Sabotage must remain recoverable. It cannot remove adopted doctrines, force conversion, expose antagonist roles, or permanently disable the congregation.

Altars and reliquaries must be replaceable. A destroyed chapel should create rebuilding and relocation gameplay rather than end the system for the round.

There should not be a generic "drain piety" sabotage button. Disruption should arise from physical actions players can observe and contest.

## Antagonists

Hidden antagonists interact with station faith under the same rules as everyone else.

A Traitor, Thief, Revolutionary, or infiltrating Nuclear Operative may join, perform rites, accept vows, and benefit from doctrines. Religious interfaces and mechanics never inspect or reveal antagonist status.

An antagonist who voluntarily accepts a restrictive vow may later break it and suffer its normal religious consequences. This reveals only that a vow was broken, and that information remains private unless the player confesses.

Taking a new ghost role represents a new character and does not carry over the previous character's faith.

## Brains, Cloning, and Silicons

Faith follows the character's continuing identity rather than their current body.

Cloning, resurrection, brain removal, polymorph, and similar transfers preserve the character's religious memory. Religious effects only function when supported by the current body.

A character placed into an MMI, cyborg, or station AI remembers their former religion but is no longer an active believer. They receive no gifts, vows, commandments, or ritual participation while bound to silicon laws.

If returned to an organic body, the character must voluntarily undergo initiation again. Their previous religious history is retained so siliconization cannot be used to erase violations.

## Roundflow and Department Interaction

The tradition is selected at round start, but the system remains dormant until players engage with it.

A typical progression is:

1. The Chaplain discovers the station's tradition and explains it to interested crew.
2. Players join or assist with early rites.
3. The congregation earns enough piety to discuss its first doctrine.
4. The Chaplain proposes a choice and the congregation ratifies it.
5. New rites and vows influence how participants respond to later station events.
6. Damage to the chapel, deaths, shortages, sabotage, and emergencies create new religious needs.

The Chaplain organizes the loop, but relies on other players:

- Medical provides patients and supplies without losing ownership of medical gameplay.
- Cargo can replace destroyed ritual objects and source unusual ritual materials.
- Service supplies food, performance, and public space.
- Engineering can rebuild or relocate a damaged chapel.
- Security may protect public rites or investigate sabotage.
- Antagonists can participate sincerely, exploit trust, or disrupt ceremonies.

The system should continue to generate interaction even when the congregation does not reach its final doctrine.

## Game Design Rationale

### Player Interaction and Agency

Joining, accepting vows, sharing burdens, and participating in dangerous rites are voluntary. Congregational progress requires several players and creates reasons to negotiate with other departments.

The Chaplain proposes decisions, but cannot complete the entire progression alone.

### Unpredictability and Chaos

The randomly selected tradition changes the available interactions each round. Physical materials, station emergencies, sabotage, and participant behavior determine whether rituals succeed.

The mechanic creates potential chaos without guaranteeing disruption.

### Dynamic Environment

Religious gameplay is grounded in replaceable physical objects. Chapels may be destroyed, rebuilt, moved, or improvised elsewhere.

No unique round-start object is required to keep the system functional.

### Intuitive and Inter-Connected Simulation

Rituals use understandable actions: lighting candles, carrying a reliquary, sharing food, treating a patient, maintaining a formation, or protecting a partner.

Requirements, risks, and vow conditions are displayed in-game. Players should not need an external guide to avoid violations.

### Darkly Comedic Tone

The system supports sincere ceremonies and absurd station stories without treating religion itself as a joke. A solemn procession may be interrupted by decompression, contaminated ritual food, a stolen relic, or an argument over doctrine.

## Administrative and Server Rule Impact

The proposal should not require new roleplay rules.

- Participation and vows are mechanically consensual.
- Only explicit religious actions produce automatic violations.
- Ordinary morality and justified violence are not judged by the system.
- Sin and confession are private.
- Antagonist status is never exposed.
- Sabotage uses existing standards for theft, assault, poisoning, and disruption.
- Prayers do not require an administrator response.

This design aims to reduce disputes by showing players the exact conditions of a commitment before they accept it.

## Scope and Future Expansion

The first implementation should establish:

- The three traditions.
- Voluntary congregation membership.
- Piety and congregational doctrine choices.
- Personal vows.
- A small representative set of common and tradition-specific rituals.
- Recoverable altars and ritual objects.
- Private favor, sin, confession, and atonement.

Additional rites, doctrines, aspects, ritual objects, and tradition variants can be added after the core loop has been playtested.

Guaranteed resurrection, permanent global combat modifiers, real-world religions, competing player-created religions, and antagonist-exclusive dark faiths are outside the initial scope.

# Technical Considerations

The feature requires shared station religion state, a player-facing altar interface, data-defined traditions, rites, and doctrines, and tracking of voluntary membership and vows.

Religious identity should follow the character's mind through cloning and body transfers. Effects are applied only to the current compatible body. Ghost-role takeover creates a new identity, while siliconization converts active membership into remembered former belief.

Ritual execution must be server-authoritative and support interruption, participant consent, recoverable objects, and explicit safe withdrawal points.

The initial implementation should avoid polling large entity sets. Proximity and participation should be tracked only while a ritual or relevant temporary effect is active.
