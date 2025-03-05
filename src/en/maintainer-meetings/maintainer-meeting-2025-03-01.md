# Maintainer Meeting (1 March 2025)

**Time:** 1 March 2025

```admonish info
**Attendees:**
- Myra
- Errant
- Julian
- Scar
- Simyon
- Orks
- Milon
- Slam
- Arshus
- Keron
- Geeky
- notafet
- Slartibartfest
- Boaz
- Chromiumboy
```

This meeting was recorded:

{% embed youtube id="LjHGgHPTGvg" loading="lazy" %}


## Reminder to please squash merge PRs!
We had several ones not squashed this time.

## AI docs part 2
We (still) have like 4 ai design docs can we like pick one?

Apparently according to some emoji reactions Scar, Chromiumboy, Errant and Aeshus have read em' all. Please tell us your findings.

Links to all prs and some hamsters for some reason: https://discord.com/channels/310555209753690112/1344749959035228200/1344806011273220239

TLDR by chromiumboy: https://hedgedoc.spacestation14.com/oldG2zWxTs-7j7PrPzJiCg?view#

- We consulted Keron, with their experience of wizard with how they worked on getting wizard up and organised it.
    - Through their insanity.
    - Had a basic idea from the SS13 design
    - People volunteered and they eventually got a good group of people to help.
- Geekys opinion
    - Wizard is a good example of people teaming up to work on a project.
    - We should encourage big features to be worked by multiple people to prevent a surgery situation.

Conclusion:
- While we did not pick a specific design doc (it would probably take too long for ~~this~~ any maint meeting) we should encourage a group to be made to take on design and development of the AI like wizard was.

### Sidenote: Silicon maintainer workgroup
- So on the subject of work groups, those are kinda in a wierd limbo
    - UHH i suppose this will be a lead maintainer thing. (oh yeah did we mention we are doing lead maints)
        - We do it i suppose, although work groups need to be looked at againa as well.

## Forums for maintainer use (Simyon)
- Currently we use threads and it sucks
    - Simyon hates threads
- A discussion can quickly get heated or it's just so many messages that it becomes hard to get a "grip" on if you are trying to join from an outside view

Stuff that should be discord threads:
- Maint reviews (cause maintainer bot and julian would cry otherwise, we should force him to learn Ruby)

Ok thats it... everything else is on the forums now. (New maints, triagers etc)
- Make an announcement in #maintainer-info after the meeting :3
- Remove ability to make threads in #staff-general-sorority?
    - screm at anyone who makes a Discord thread without good reason

## Maintainer leads
- Preliminary results is Myra, Julian, Simyon (nerds)
- Icon was suggested to be double hammers
    - Julian joke suggested a purple T-Online Magenta Icon. I now hate Julian.
- Tasks:
    - be very silly :3 :3
    - UHH
    - smell good (unlike other maintainers, trueee)
    - Organize the Maintainer Team’s Business(e.g. Maint meetings, stable releases)
    - Triaging critical issues.
    - Organize important development efforts(E.g. The way wizard was developed)
    - Drive changes to Maintainer Policy.
    - Make the final call where the Maintainer Team is unable to reach a decision.

## AFK Kick Ingame
- Good idea
- Previously removed cause code smelly (like the maintainer team)
- Shouldn't kick if in round / has body?
    - Defo kick if in lobby
- Maybe like 15 minutes? Or 30? Or like... 45?
    - 15 is fine
        - what if someone is grabbing food quickly, or warming soup?
            - You are warming soup for 15 mins?
                - Yes. I like to slow boil my soup. It tastes better that way.
                    - Whatever you can join midround even if the player limit is max if you were in round anyway
                        - Does that work for observers?
                            - I dont think they are considered valid? Check pls

## Stable review
- [35131](https://github.com/space-wizards/space-station-14/pull/35131) Vote kicks now ban the target's ip
- [35083](https://github.com/space-wizards/space-station-14/pull/35083) High Heel Boots do the Clicky Clacky
- [35122](https://github.com/space-wizards/space-station-14/pull/35122) Supermatter Grenade Rework
    - May have to lower the physics velocity to prevent people flying out into space
        - But everything reporting this is on the current stable, and none on vulture. So lets see how it goes first
- [34695](https://github.com/space-wizards/space-station-14/pull/34695) Engineering guidebook improvements
- [34945](https://github.com/space-wizards/space-station-14/pull/34945) Replaced Bulldog beanbag drum with lethals drum
- [35240](https://github.com/space-wizards/space-station-14/pull/35240) Centcomm 3: Beyond Thunderdome
- [35254](https://github.com/space-wizards/space-station-14/pull/35254) Magical contraband type
    - Do we want ninja controband?
        - Just call it illegal controband with no special grouping
            - Discuss this more on the FORUMS BABY
- [35248](https://github.com/space-wizards/space-station-14/pull/35248) Add CentComm Comms Console + Change admin announcement color
- [35239](https://github.com/space-wizards/space-station-14/pull/35239) [ChangeCVarCommand] Mapping Command
- [35168](https://github.com/space-wizards/space-station-14/pull/35168) Add radiation shielding to metal crates
    - This should work on all crates and not just steel ones (exept plastic)
- [35259](https://github.com/space-wizards/space-station-14/pull/35259) Crusher Dagger Knife Component
- [35282](https://github.com/space-wizards/space-station-14/pull/35282) add ShowJobIcons to AiHeldIntellicard
- [35296](https://github.com/space-wizards/space-station-14/pull/35296) ports two barsigns from frontier
- [35295](https://github.com/space-wizards/space-station-14/pull/35295) Space Lizard Plushie In-hands
- [33727](https://github.com/space-wizards/space-station-14/pull/33727) Fix to make all corpses butcher able and better disposable
    - Double check it does not effect crew species
- [35331](https://github.com/space-wizards/space-station-14/pull/35331) Require hwid
- [34446](https://github.com/space-wizards/space-station-14/pull/34446) Mjollnir and Singularity Hammer for Wizard
- [35333](https://github.com/space-wizards/space-station-14/pull/35333) Adds Colored Light Bulbs
- [35377](https://github.com/space-wizards/space-station-14/pull/35377) Wizard: Repulse Spell
- [35383](https://github.com/space-wizards/space-station-14/pull/35383) Give dogs speech noises
- [35403](https://github.com/space-wizards/space-station-14/pull/35403) Wizard: Smoke Spell
- [35421](https://github.com/space-wizards/space-station-14/pull/35421) Lattice tiles footsteps now sound like catwalks
- [35354](https://github.com/space-wizards/space-station-14/pull/35354) Swap price of EMAG and AD.
- [35031](https://github.com/space-wizards/space-station-14/pull/35031) Sentry turrets - Part 2: Basic prototype
- [35423](https://github.com/space-wizards/space-station-14/pull/35423) Remove disablers from emagged lathe
- [34105](https://github.com/space-wizards/space-station-14/pull/34105) Add microwave recipes to the guidebook
- [35226](https://github.com/space-wizards/space-station-14/pull/35226) Fix/Addition - Wizard Survivor Antag Status
- [35284](https://github.com/space-wizards/space-station-14/pull/35284) version watermark
- [35418](https://github.com/space-wizards/space-station-14/pull/35418) Make holoparasite's damage transfer ignore the host's armor
    - We can lower holoparasite price now!!!!!!!!!!!
- [35322](https://github.com/space-wizards/space-station-14/pull/35322) Put Neckwear above Backpacks
- [35345](https://github.com/space-wizards/space-station-14/pull/35345) [ADMIN] Admin IDs now have Agent ID properties
- [35346](https://github.com/space-wizards/space-station-14/pull/35346) Adds new speech bubble opacity sliders to the accessibility menu.
- [35508](https://github.com/space-wizards/space-station-14/pull/35508) Engineers can now choose to wear no head piece
- [35381](https://github.com/space-wizards/space-station-14/pull/35381) Lizard Plushie Slippers
- [35406](https://github.com/space-wizards/space-station-14/pull/35406) THE WIZARD
- [35043](https://github.com/space-wizards/space-station-14/pull/35043) Mime can no longer write on paper without breaking their vow
- [35530](https://github.com/space-wizards/space-station-14/pull/35530) Wizard ID
- [35537](https://github.com/space-wizards/space-station-14/pull/35537) Wizard robes allow you to wear gas tanks
- [35543](https://github.com/space-wizards/space-station-14/pull/35543) Admin Options tab
- [35544](https://github.com/space-wizards/space-station-14/pull/35544) Old Rollie Name Integration
- [35552](https://github.com/space-wizards/space-station-14/pull/35552) Wizard Stamp
- [33614](https://github.com/space-wizards/space-station-14/pull/33614) Add breakdown recipes for Insect and Ammonia blood
- [34763](https://github.com/space-wizards/space-station-14/pull/34763) Adding sorting to chem master
- [34315](https://github.com/space-wizards/space-station-14/pull/34315) Multiple categories for lathe recipes
- [34316](https://github.com/space-wizards/space-station-14/pull/34316) Add filters to uniform printer
- [35183](https://github.com/space-wizards/space-station-14/pull/35183) Fire resist now can be examined.
- [32255](https://github.com/space-wizards/space-station-14/pull/32255) add button to print logprobe logs
- [32996](https://github.com/space-wizards/space-station-14/pull/32996) Sap-Syrup balance
- [32136](https://github.com/space-wizards/space-station-14/pull/32136) Implanter draw rework
- [35512](https://github.com/space-wizards/space-station-14/pull/35512) Made forensic scanner classified as contraband.
- [35232](https://github.com/space-wizards/space-station-14/pull/35232) ConfirmableAction for DNA Scrambler implant
- [34795](https://github.com/space-wizards/space-station-14/pull/34795) Re-implement world gen (space debris) across all servers
    - Keep an eye out for perf
- [33448](https://github.com/space-wizards/space-station-14/pull/33448) Make OuterClothing hide PDA and belt sprites under it.
- [33614](https://github.com/space-wizards/space-station-14/pull/33614) Add breakdown recipes for Insect and Ammonia blood
- [34763](https://github.com/space-wizards/space-station-14/pull/34763) Adding sorting to chem master
- [34315](https://github.com/space-wizards/space-station-14/pull/34315) Multiple categories for lathe recipes
- [34316](https://github.com/space-wizards/space-station-14/pull/34316) Add filters to uniform printer
- [35183](https://github.com/space-wizards/space-station-14/pull/35183) Fire resist now can be examined.
- [32255](https://github.com/space-wizards/space-station-14/pull/32255) add button to print logprobe logs
- [32996](https://github.com/space-wizards/space-station-14/pull/32996) Sap-Syrup balance
- [32136](https://github.com/space-wizards/space-station-14/pull/32136) Implanter draw rework

## Required for stable
- [32209](https://github.com/space-wizards/space-station-14/pull/32209) Change Phalanximine to be more complex, increase Arithrazine damage
    - NOTE: The changelog entry is gonna be 2 weeks late LMAO x3 xd
    - also merge it
    - but change it to stable
    - also someone fix changelogs so we can do it on all branches without merge conflicts awawawawaw

## Considered
- [35583](https://github.com/space-wizards/space-station-14/pull/35583) Remove cellular resistance for slimes 
    - It was pointed out slimes have cellular resistance, which is a byproduct of when cellular was a more common and mob-dealt damage type (Slam)
        - I tested it and slimes already take the same damage on master because you set ignoreResistances to true so that PR isn't needed (Slart)
            - Yeah I checked it now as well, was just about to comment. Though I think the PR should be merged regardless; the intended purpose of cellular as a damage type meant to offset player-taken actions, removing cellular from slimes should still be desirable. Just for future-proofing's sake; there's no way in the game right now for slimes to take cellular damage where the resistance is applied. Might as well yeet it (Slam)
                - It sounds like we dont need to merge this into stable (Myra)

# Random stuff
:3 :3 :3

- We began talking about among us (SUS????)
- yip yap growl whine ~nik, 2025, colorized
- mrowr arf arf ~milon, probably
- seems like most ss14 staff are furries smh (lies and slander, false actually smh)
- among us 1984 wawa lmao
- Scar smells REALLY bad TRUE!!
- ArtisticRoomba is to be removed from triage cause they stinky
- Myra is eating soft tacos today
    - Good.
- CHAT! PLAY RAINWORLD!
- we should make ss14 integrate with chat gpt
- nik is stinky