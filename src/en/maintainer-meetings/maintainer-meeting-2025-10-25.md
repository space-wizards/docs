# Maintainer Meeting (25 October 2025)

```admonish info

**Attendees:**
- Myra
- Simyon
- PJB
- Errant
- Scar
- Julian
- Ada
- Tiniest shark
- Slarti
- Princess cheeseballs
- Orks
- Slam
- Roomba

```

This meeting was recorded:

{% embed youtube id="4I8DrL52W2U" loading="lazy" %}

## ~~BLOCKER? - Bwoinkwindow pinning broken (Errant)~~
- ~~Admins can't pin users in the bwoink list. Apparently broken by stylenano changes~~
    - ~~Fix open [#41093](https://github.com/space-wizards/space-station-14/pull/41093) Seems fine, but it needs to be rebased because it wasn't branched off of staging~~
    - PR merged to staging, should be fine now.

meow

## Killing StyleNano for good (Janet)

- We have the sheetlets PR ([#29903](https://github.com/space-wizards/space-station-14/pull/29903)) in, which breaks up 99% of the styles used in the game into a more maintainable ofrm
- StyleNano is marked as deprecated and lost a lot of functionality
- When do we want to pull the plug for good and outright remove StyleNano.cs?
    - No harm in keeping it until we remove everything that uses it.
    - Kept for downstream compatibility.
- Proposal: 2 stable cycles from now (~4 weeks)
    - Just remove it when it's no longer fully used and then nuke it (see above, downstream compatibility)
- `Slam`: Any guide/instructions available on how sheetlets work? Thinking documentation-wise, as that was an issue with StyleNano.
    - [#269](https://github.com/space-wizards/docs/pull/269) prioritise this.
    - **This isn't really relevant to this topic in particular.**

- **No stated maintenance overhead, there is no reason to debate this any more than any other `[Obsolete]` tag, which we have plenty of.

## Remember to vote on the Wizard poll (Princess)
- Poll is here, it's the third poll ignore the second poll. (https://forum.spacestation14.com/t/remove-wizard-roundstart-antag/24764)
    - 3 hours from now (18:28 UTC), close and decide.
- Gonna try and get this into staging if we can.

nya~~~

## Super Synth Vote (Princess)
- Main discussion post. (https://forum.spacestation14.com/t/clarifying-the-supersynth-removal-and-my-perspective/24588)
- For clarification this is a vote as to whether or not we should have a midi-restricted super synth be admin only.
    - `Princess:` I think it should be unrestricted for reasons listed in the thread and my own. Super Synth doesn't need to be admin only if it's not capable of crashing clients anymore. Implementation is a seperate issue which can be voted on seperately. 
    - `Princess:` In addition to consider: Using a super synth over a DAW heavily restricts the instruments you can use when playing in a one-man-band.
        - `Princess:` These aren't niche instruments either, this stops you from using most instruments aside from pianos and percussion
        - `Princess:` Using bands to enhance your midis is very common, and I've seen a number of musicians who wouldn't have any use for a super synth just this week, since they had their hands occupied with a guitar/microphone in their band. The DAW is a much better instrument if you don't mind staying in one place or being slower dragging it around.
        - `Princess:` Super Synth is effectively a convenience option for a traveling musician, in that regard it should be rare and restricted but ultimately it will never be as good as a proper DAW band setup.
        - `Slam`: Been playing more instruments ingame to test this and I honestly prefer large instruments, even when patrolling around the station, since dragging frees up your hand whereas held instruments require the active hand. (I will not stoop to using handsfree harmonica.)
    - `Slarti`: I think introducing a admin and non-admin version of the super synth is just really messy and is the whole reason why there was so much confusion about this in the first place. We should have a requirement that admin and non-admin items should be clearly distinguishable. So if you want to add an instrument that can do what the super synth does but keep the midi limitations then add a new item for it, or resprite and rename the admin version a new admin-synth.
    - `Slarti`: Also it should not just be something you can order at cargo. The DAW already has the same purpose, but you have to put in a little effort to obtain it (and the flatpacker thing is clearly a bug). At least make it a little more interesting where you craft it by duct taping a bunch of instruments together for example. But a cargo order that directly obsoletes all other instruments seems boring from a gameplay perspective to me. And if the goal is to make it available to musicians than allow them to do so without having to convince cargo to gamble a ton of spesos until they find this one item.

- Admeme items should be clearly marked
- Introduce (soft) policy to disallow adding admin only items, possibly.
- Signpost that a PR being merged does not greenlight it for inclusion within the game / stable.
    - Upstream has a different direction, people can always PR downstream.
    - do that :tm:

## Silicon Workgroup (ScarKy0)
There is currently a document up for the creation of the Silicon workgroup. Not really a topic to speak about during the meeting however id appreciate if someone found some time to drop feedback.

The document can be found [here](https://github.com/space-wizards/docs/pull/537) and the forum post [here](https://forum.spacestation14.com/t/workgroup-creation-request-silicon/24848).

- Will be done after meeting.

## Stable review

```admonish info

Write your name here if you read this list fully.
**I checked this PR list:**
- Slam
- ScarKy0
- Errant
- Slarti
- Princess
- Myra
- aada
- Emo
- Tiniest Shark

```

- [32537](https://github.com/space-wizards/space-station-14/pull/32537) Slime organs metabolizing slime restores blood level + halves slime hunger satiation when consumed by a slime organ
    - `Errant`: That is one of the titles ever. Don't be affraid to edit the PR text before merging, if it needs a touch-up
- [41016](https://github.com/space-wizards/space-station-14/pull/41016) Allow matches to be placed into ash trays
- [40220](https://github.com/space-wizards/space-station-14/pull/40220) goats eat kudzu again

- [38076](https://github.com/space-wizards/space-station-14/pull/38076) Resprite Maint Hatch + New Syndicate Hatch
- [40580](https://github.com/space-wizards/space-station-14/pull/40580) Entity Effects ECS Refactor
- [40850](https://github.com/space-wizards/space-station-14/pull/40850) Changed Soviet soda vending machine name
- [38225](https://github.com/space-wizards/space-station-14/pull/38225) Adds a guidebook reference table for silicon lawsets
- [40196](https://github.com/space-wizards/space-station-14/pull/40196) Make SmartFridges airtight
- [39761](https://github.com/space-wizards/space-station-14/pull/39761) Rename "trash" reagent to "reprocessed material"
    - `Princess`: Trash as a reagent should really be removed in favor of letting voxes digest actual things like steel, plastic or silicon. 
    - Adding more effects will bloat the guidebook text even more
        - Compact it further to improve UI
- [40842](https://github.com/space-wizards/space-station-14/pull/40842) slime guidebook change
- [40880](https://github.com/space-wizards/space-station-14/pull/40880) Rollerbed & Bodybag tweaks
- [40908](https://github.com/space-wizards/space-station-14/pull/40908) New botany poster
- [39370](https://github.com/space-wizards/space-station-14/pull/39370) Improve lying trait grammar
- [40926](https://github.com/space-wizards/space-station-14/pull/40926) Ashtrays can contain ashes and matches
    - `Errant`: This is literally a subset of #41016, what happened here? 
- [34935](https://github.com/space-wizards/space-station-14/pull/34935) Grenade penguin htn
- [40867](https://github.com/space-wizards/space-station-14/pull/40867) Bring sky blue carpet in line with other carpets
- [39210](https://github.com/space-wizards/space-station-14/pull/39210) Fix custom MIDI instruments sounding incorrect; add two more microphone instrument options
    - `Princess`: We should let scurrets use the two new instruments as a natural ability.
        - `Simyon`: I agree, but this is a feature request. Make an issue :godo:
- [35636](https://github.com/space-wizards/space-station-14/pull/35636) Add "Reset to default" verb to TriggerOnVoice
- [39103](https://github.com/space-wizards/space-station-14/pull/39103) add the diona typing indicator to the FloraTree entity
- [40904](https://github.com/space-wizards/space-station-14/pull/40904) Remove two obsolete buttons from the Admin UI
- [40878](https://github.com/space-wizards/space-station-14/pull/40878) Added Vox Chitter and Clicking
- [39515](https://github.com/space-wizards/space-station-14/pull/39515) Add GenpopLeave and GenpopEnter to Security accesses
- [40818](https://github.com/space-wizards/space-station-14/pull/40818) Remove rag forensics cleaning
    - `Errant`: Okay so I missed this and the vote and it's a bit late now, but. Would it not be a better solution to add some sort of identifiable forensic leftover to it that acts similar to the soap residue? Seems like a better solution than just removing it as an option entirely
        - `Princess`: The issue is, this is an infinite use item that can be crafted with 1 cloth by anyone. It completely invalidates soap and even if you gave it a specific residue, there would be no way of knowing which rag was used since unlike soap it doesn't get used up.
            - Give soap an examinable solution to gauge usage easier.
- [39764](https://github.com/space-wizards/space-station-14/pull/39764) Slightly resprited the service borg
- [40955](https://github.com/space-wizards/space-station-14/pull/40955) Cargo orders that contain beverages now come in freezers
- [39104](https://github.com/space-wizards/space-station-14/pull/39104) All pens embed
  - `Slam`: Dubious of this. Last time we did this it resulted in borgs being pelted by pens and seeing them stuck in steel walls (???). Not saying "Revert", I just expect us to get tired of this pretty quickly again.
    - `Princess`: Needed to prevent metagaming the explosive pen. We also have the smite can which embeds now, even if it's much less common. 
    - `Scar`: Alternative option is to make explosive pens only embed when ticking. Alternative alternative option is to allow entities to unembed things even without hands.
  - `Slarti`: I'm not a fan of the "make everything embedd" trend, we repeatedly get PRs for this. It just looks jank visually and especially for pens it's easy to spam them. At least someone should rework the visuals first. (I can't seem to upload a gif here, see the discord thread to see what I mean)
    - `Princess`: Alternatively we could use triggers to make it so the explosive pen doesn't embed until it has been clicked? That might be less messy. We could just have all pens deal 1 damage but the explosive pen only embeds once it has been armed.
    - `Emo`: I'd rather just have the pen only embed when armed. Being able to stick someone with 20 pens that just linger on their body looks incredibly bad. The previous PR was rejected for the same reason so I'm not sure why it wasn't brought up again as a concern.
- [40054](https://github.com/space-wizards/space-station-14/pull/40054) Ninja headset
- [40970](https://github.com/space-wizards/space-station-14/pull/40970) Adding cotton seeds to cargo seeds crate
- [38542](https://github.com/space-wizards/space-station-14/pull/38542) Lets monkeys & kobolds shove/disarm!
- [40944](https://github.com/space-wizards/space-station-14/pull/40944) Silicon lawset book and Law boards can now point to the list of lawsets.
- [34127](https://github.com/space-wizards/space-station-14/pull/34127) New job lizard plushies + Job-specific trinkets loadout
  - `Slarti`: The ones for the trainee roles are unobtainable because you get locked out of the role before unlocking it, see [41095](https://github.com/space-wizards/space-station-14/issues/41095)
  - Do not loadout it. Confine it to job lockers as a rare spawn (e.g. Paramedic plushie spawns in Paramedic locker)
- [37681](https://github.com/space-wizards/space-station-14/pull/37681) Large thruster
- [40995](https://github.com/space-wizards/space-station-14/pull/40995) Added the cosmetic carp suit to the autodrobe inventory
    - `Emo`: Why do we bother freezing new roundstart clothing items if we're going to keep merging shit anyways. The autodrobe is already extremely overfilled with more than 60 items in it. It's a little bit ridiculous that fluff clothing is *THE* bloat item and yet we still don't actually handle it correctly.
        - This one is purely cosmetic, added to curb metagaming of the Hardsuit version of the carp suit. 
- [40998](https://github.com/space-wizards/space-station-14/pull/40998) Consistency fix for soap making
- [36244](https://github.com/space-wizards/space-station-14/pull/36244) Criminal console status expansion
- [36378](https://github.com/space-wizards/space-station-14/pull/36378) Feature/door remote radial
- [40542](https://github.com/space-wizards/space-station-14/pull/40542) Changed Vox Head Marking Point Limit To 4
- [40538](https://github.com/space-wizards/space-station-14/pull/40538) Add doafter to filling the hypopen
- [41027](https://github.com/space-wizards/space-station-14/pull/41027) Changed mindswaps cooldown from 5 minutes to 3 minutes
- [41018](https://github.com/space-wizards/space-station-14/pull/41018) Move ChemMaster buffer sort button out of transfer/discard button group
- [41031](https://github.com/space-wizards/space-station-14/pull/41031) added seclight to hos locker
- [41038](https://github.com/space-wizards/space-station-14/pull/41038) Changes Slippery Slope to not require a robe and hat for casting.
- [41013](https://github.com/space-wizards/space-station-14/pull/41013) Toilet cistern stashes spawn containing basic loot
  - `Slam`: These new prototypes could be further expanded to fix the "build new toilet -> plunger them for loot" "exploit" that exists right now.
  - `Emo`: The entity tables used for the toilet loot are just duped versions of the maint loot table. It really should just be reusing existing tables as it's basically just the maint locker fill but with different weights and extra maintenance for an extremely obscure feature.
  - `Slarti:` I agree with Emo, this should be using one of the existing loot tables.
  - Make issue on github for this. Not a blocker.
- [40318](https://github.com/space-wizards/space-station-14/pull/40318) Hand labeler UI improvements

##

Niko is a cat

:3

nik is a cat :3
