# Maintainer Meeting (10 May 2025)

:::info
**Attendees:**
- Myra
- Errant
- Simyon
- PJB
- Orks
- Slamn
- Janet (Welcome)
- Roomba
- Shadowcommander
- Slart
- Eletro
- Fildrance
:::

This meeting was recorded:

{% embed youtube id="f1K4AddPzD8" loading="lazy" %}


## Stable review process (Myra)
- Did you guys like how we only did what we had comments on?
- I will be doing it again this meeting since more people can be effected by it
- If you guys like it i will write it on the docs, along with general "how 2 run a maint meeting 101" stuff.
- Slart mentioned wanting to keep the old process (going through all the prs on the meeting, instead of letting reviews happen in advance)
    - Maybe we should do a vote with all maints?
    - If we do keep the old process, it needs to be streamlined or tool-assisted somehow (x-factor button) to make it easier for the meeting host
- Pro and cons of the old and new system
    - Review in advance (Proposed system, system applying for this meeting again)
        - Pros: 
            - We get to spend less time reviewing prs, meeting goes faster
            - We have a lot more time to add an objection. Instead of like 5 seconds of myra hoping someone speaks up, we instead have 2 whole days + time before stable review during the meeting (I like this since if you dont have anything to add on a topic you can have something to do).
            - Also prevents the embarrassing "Anyone has any objection" without anyone saying anything when we have 0 objections.
            - Allows maintainers who cant make it to the meeting put in their thoughts to be discussed.
        - Cons:
            - Relies on maintainers actually taking their time to read the pr list. Maintainer that forgot may be unable to get a discussion on a pr they were concerned about
            - Does not bring up everyone "up to speed"
            - (Slart) I expect the participation turnout to be lower on other platforms than on discord
                - See the forum posts, where discussions end up completely dead
                - While in theory it is only a single extra click it still seems to have an effect since communication on discord is quick and easy
                - I mostly would like to see the PRs getting the discussion they deserve instead of quickly waving them through without because not enough people took a look
    - Review at the meeting (Current)
        - Honestly, essentially the opposite of the above. All (attending) maints get brought up to speed and can make an objection right there and then. We can make sure no one misses a pr.

## Command naming convention (ElectroSR)
Should we change toolshed commands to use snake_case instead of whateverthisconventioniscalled
Relevant [docs](https://github.com/space-wizards/docs/pull/210) and [engine](https://github.com/space-wizards/RobustToolbox/pull/5829) PRs

- PJB is a little unsure of the breaking change, (the admins may kill us)
    - Can we maybe do aliases to not break it too much?
        - This should come down to a vote, alias should be included though

## General Power Rebalance 2 Electric Boogaloo (ArtisticRoomba)
- "Who sent me a :3" - Myra
<img src="https://hedgedoc.spacestation14.com/uploads/4a65c149-c7e0-4db7-8734-93f2896b16ab.png" alt="drawing" width="340"/>

- I'd like to move all radiation collectors internal to the station, following discussion on it. It's just better from a game design perspective.
- Singularity collectors need to be buffed, or singularity radiation needs to be buffed, in order for the collectors to power the station properly.
- This has a lot of caveats, ex. radiation being too powerful and leaking into supposedly safe areas, accidentally buffing broken-RTG setups, etc.
- I'm going to buff the collector rads-to-power conversion and potentially nerf RTG rads output. Let me know if anyone disagrees with this change.
<br>
- The AME needs to be rebalanced again, the logarithmic curve is too great and it leads to core spamming for larger stations.
- We can simply dampen the logarithm. It's pretty extreme right now.
- A community member (nikovnik) has suggested a new linear equation (https://www.desmos.com/calculator/wyq44riaaq) which would promote the AME as a "target capacity emergency generator" rather than a flexible grid-match emergency generator. I'd much rather have this (though grid matching will still be encouraged, see the PR when I make it)

## Machine Variable Power Consumption (ArtisticRoomba)
- Most machines on the station consume a static 200-1000W or more when not preforming any work, and this doesn't change when they are actually preforming work.
- This makes engineering work sort of bland and dull (grid is always boringly constant), and it makes it hard to balance power around (powering 350 kW for 10 minutes on batteries alone takes a lot of power).
- After posting issue [#36277](https://github.com/space-wizards/space-station-14/issues/36277), contributors are starting to make PRs to give machines variable power consumption via their state. This is being done directly by setting the APC Receiver component's load to a power value. The amount of power the machine uses in idle and on load can be set on the main component of the machine in YAML.
- It is probably not a good idea to hardcode variable powernet behavior into every unique system
- Would it be more desirable to instead have a generic system that handles idle/active loading, and possible transient loading based on curve types?
    - This solution/logic is similar in vein to the ActivatableUIComponent which handles simple UI interactions and reduces code boilerplate in systems for kid named 
- We have no real idea how much power different categories of stuff ACTUALLY uses, would be neat if this could somehow be seen ingame?

- Request changes on existing PRs that are adding different power states to machines.
    - Making the new system shouldn't 

## Make the meetings not be 2 hours (Errant)
- Suggested ideas (Myra)
    - Breaks
    - Splitting the meeting
        - FSP also mentioned this one, more bellow.
    - Set max time for a topic (with the option to extend, if it needs it)
    - Myra's proposed stable review system (Which we hopefully talked about above)
    - Max amount of topics per meeting
        - Kinda depends
    - Anything else?
- I missed last meeting, why did it take that long? I thought you skipped most PRs?
    - We kept getting derailed

- FSP suggested:
    - Split meetings into two different ones: staging review and maint topics
    - Maybe see if we can shuffle the times around with this, so people like Sloth can be more engaged?
    - Prioritize topics by order of importance. Stuff that needs deciding on should go at the top.

## Post-Meeting Xeno Station (Slam)
- Simyon will be hosting a private server running Xeno Station *after* the meeting, maintainers & admins are free to come check it out. 

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- Slarti
- Roomba
- Scar
- Errant
- Myra
- Slam
:::

- [32734](https://github.com/space-wizards/space-station-14/pull/32734) Change some posters to be rules-compliant
- [34186](https://github.com/space-wizards/space-station-14/pull/34186) Cyborg Rebalance
  - Instead of rebalancing modules all the time we should finally port how ss13 is doing borg items. (Slarti)
      - (Ideaguys tinfoil hat activate) If we make robust hand whitelisting real, we can easily make borg modules not suck. I've wanted to poke at it for a while. (Roomba)
  - We should either start telling contributors to fill out the description stuff or do it ourselves at merge time. But either way, it should be possible to design-review a PR without having to look through the code. No, I do not have all the tool module icons memorised, or remember what had what before this change (Errant)
      - We should probably be more strict in enforcing the PR guidelines/template. It would be much better if we forced contribs to properly document their changes, why they made them, and if they're breaking, instead of us taking the time to do it ourselves, or attempt to extrapolate them through diffs. It's a waste of time. (Roomba)
- [36890](https://github.com/space-wizards/space-station-14/pull/36890) Reptilians Can Eat Orange Creamsicles
  - Not specifically about the PR, but it mentions "Otherwise inedible foods, such as cakes, are made edible when fruit flavoured (for instance, Reptilians can eat orange cake, but not normal cake, or carrot cake)." If this is the current dietary logic, it does not really make sense. You would think a reptilian should be blacklisted by pastries, instead (Errant)
- [33305](https://github.com/space-wizards/space-station-14/pull/33305) Add Bloodstream to Goliaths
- [31450](https://github.com/space-wizards/space-station-14/pull/31450) Nerf mining hardsuit's effectiveness against bullets and bombs.
- [36363](https://github.com/space-wizards/space-station-14/pull/36363) Controls page guidebook rework 2025 Q1
- [36841](https://github.com/space-wizards/space-station-14/pull/36841) Lower interdyne herbals TC cost
    - ~~This may need to be re-evaluated as omnizine is finally getting health pool based healing (which reduced its effectiveness if your damage wasn't across multiple damage types) (Roomba)~~
    - The new omnizine changes still won't really make them viable, they just take SOOOO long to heal anything (Scar)
        - Agree. (Roomba)
- [32293](https://github.com/space-wizards/space-station-14/pull/32293) Inaprovaline metabolizes slower for better use as a stabilizing medicine
- [36910](https://github.com/space-wizards/space-station-14/pull/36910) Releasing an under-pressure lockout is now a verb
- [36921](https://github.com/space-wizards/space-station-14/pull/36921) Make 10u of "Atomic Bomb" drink instead of 11u
- [31247](https://github.com/space-wizards/space-station-14/pull/31247) PKA Modkits + Rebalance
- [33883](https://github.com/space-wizards/space-station-14/pull/33883) Land mine armament
- [36405](https://github.com/space-wizards/space-station-14/pull/36405) Add Cotton Burgers
- [32676](https://github.com/space-wizards/space-station-14/pull/32676) Sheet-meister 2000 Cloth recipe
- [36952](https://github.com/space-wizards/space-station-14/pull/36952) Changed soundGunshot for Pulse Pistol and Pulse Carbine from laser_cannon to laser3
- [36376](https://github.com/space-wizards/space-station-14/pull/36376) The Atmos A Airlock
- [36412](https://github.com/space-wizards/space-station-14/pull/36412) Only sec glasses can show contraband: second attempt
- [36918](https://github.com/space-wizards/space-station-14/pull/36918) Delivery random multipliers
- [36945](https://github.com/space-wizards/space-station-14/pull/36945) Truncate lathe announcement lists
  - I think this one should be reduced to a single "N new recipes unlocked" message, otherwise it is just too much chat spam. (Slarti)
  - Also the announcement should come from the research server, not from the lathe. Otherwise you get message duplication if you have multiple lathes for some reason. (Slarti)
      - We should opena github issue for the two reasons above.
- [36958](https://github.com/space-wizards/space-station-14/pull/36958) Descriptions for .30 Rifle
- [36957](https://github.com/space-wizards/space-station-14/pull/36957) CMO Hardsuit: Zombification Resistance tweak
- [34471](https://github.com/space-wizards/space-station-14/pull/34471) Adds Parcel Wrap
  - Could use consistent sprites with the other mail deliveries (Slarti)
- [34235](https://github.com/space-wizards/space-station-14/pull/34235) Ammo Mag + Speedloader Inhand Sprites
- [36929](https://github.com/space-wizards/space-station-14/pull/36929) New Science Biosuit Locker Sprite
- [36968](https://github.com/space-wizards/space-station-14/pull/36968) Priority Deliveries
  - Seeing the exact time feels a bit "gamey", and wouldn't this be more "intense" if it was like: 0-30 "It has almost expired!" 31-60 "Less than a minute left to deliver!" etc (Errant)
- [36707](https://github.com/space-wizards/space-station-14/pull/36707) Paramedic suits adjustments
- [36386](https://github.com/space-wizards/space-station-14/pull/36386) Battery (SMES/substation) interface
  - Would probably be nice with a guidebook entry in the future, now that the interaction is more complex (Slam)
      - Someone is getting to it.
- [36851](https://github.com/space-wizards/space-station-14/pull/36851) Use RMC mob collision values
  - What are our plans for mob collision? I think they are still disabled. Do we need further tweaking before activating them again, or do we keep them off? (Slarti)
  - New RMC values should be tested on Vulture (they've been given a break from mob collision, so it's time to get back at it) (Roomba)
  - I have tested the new values already, players agree these are way better to play with, but that mob collision still sucks (honestly probably just a getting-used-to-it thing) (Scar)
  - It sounds like it's comfortable to test on stable, does anyone else agree with enabling it on stable for a release cycle and seeing how it goes? (Roomba)
- [36635](https://github.com/space-wizards/space-station-14/pull/36635) Feature/auto sync node scanner
- [34848](https://github.com/space-wizards/space-station-14/pull/34848) Add a mapping changelog to upstream
  - Do we have guidelines for this? (Errant)
      - https://github.com/space-wizards/docs/pull/454 Yes (Myra)
      - Tangent: pull request template should be updated to include the `MAPS:` log. It should also probably be updated to assert that the pull request guidelines need to be followed...
- [36980](https://github.com/space-wizards/space-station-14/pull/36980) Fragile Deliveries
  - It does not break if it's in your backpack when you fall! That seems a very easy bypass (Errant)
- [34195](https://github.com/space-wizards/space-station-14/pull/34195) Temporarily Making Cargo Buy and Sell Pallets Indestructible
  - Do we know if anyone is actually working on the "can-repair" fix for this? Should we solicit a volunteer internally or among contributors? "Fix this later" has been a very long later (Errant)
  - In the interim the ability to repair them should be real instead of having it be neigh invulnerable, though in the long term discussion needs to happen on how antagonists interact with and damage the ATS, and how it's repaired. (Roomba)
- [36986](https://github.com/space-wizards/space-station-14/pull/36986) nuke shelves' whitelists
- [36702](https://github.com/space-wizards/space-station-14/pull/36702) Mime suit resprite
- [37013](https://github.com/space-wizards/space-station-14/pull/37013) make scrubber widenet in panic mode
- [37000](https://github.com/space-wizards/space-station-14/pull/37000) Shoulder-length hairstyles resprite
- [36844](https://github.com/space-wizards/space-station-14/pull/36844) Xenoborgs part 2
- [37003](https://github.com/space-wizards/space-station-14/pull/37003) Theatre access to Service Request Computer
  - If we ever move away from the new Acquisition Slips system, this will probably become a problem... (Errant)
- [33500](https://github.com/space-wizards/space-station-14/pull/33500) BatteryWeaponPowerCell tweaks
- [33517](https://github.com/space-wizards/space-station-14/pull/33517) Buffing slugs and replacing beanbags from the Bulldog bundle
- [37025](https://github.com/space-wizards/space-station-14/pull/37025) Rebalance magnet debris, update worldgen
  - I beg you, please someone fix the heisentest caused by this. We got like half the tests failing at the moment. (Slarti)
- [32650](https://github.com/space-wizards/space-station-14/pull/32650) Display obvious plant mutations in examine text
- [34039](https://github.com/space-wizards/space-station-14/pull/34039) SSD sleep take 2
  - `EMO:` Might need reverting; reports of zombies and other mobs falling asleep when they're not supposed to.
      - Lets try to hotfix it instead of reverting, but if its very bad we should revert it before it hits stable.
  - The preview icons in the spawn menu are falling asleep, too :godo:
  - And the SSD examination text is mispredicting
  - Revenants are eating good, but this does cause all urists on Dev to also fall asleep, might need some additional checks or something (Scar)
  - Yeah, it should only affect actual SSD players, meaning they had a mind before that disconnected. A spawned Urist should not count as SSD. (Slarti)
      - This should only affect players/mobs that had player control, not CPU mobs
- [37023](https://github.com/space-wizards/space-station-14/pull/37023) More Mail Sprites
- [37012](https://github.com/space-wizards/space-station-14/pull/37012) re-buffs proto kinetic accelerator
- [36995](https://github.com/space-wizards/space-station-14/pull/36995) Chem master more unit transfer buttons
- [35397](https://github.com/space-wizards/space-station-14/pull/35397) Add borders to the asteroid sand
- [36009](https://github.com/space-wizards/space-station-14/pull/36009) Push horn
- [31257](https://github.com/space-wizards/space-station-14/pull/31257) Added Space Carp Tooth Arrows and Sharkminnow Spears, buffs sharkminnow teeth.
- [37041](https://github.com/space-wizards/space-station-14/pull/37041) Add inhand sprites for mini jetpack
- [37030](https://github.com/space-wizards/space-station-14/pull/37030) Show other speso colours, add larger denominations (Frontier#1496)
- [37048](https://github.com/space-wizards/space-station-14/pull/37048) Add toolbox sound effects
- [37049](https://github.com/space-wizards/space-station-14/pull/37049) Mail visual update
- [37047](https://github.com/space-wizards/space-station-14/pull/37047) Un-copypaste wallmount substation prototype to give them a UI
- [35301](https://github.com/space-wizards/space-station-14/pull/35301) Centcomm carapace, moved armour from vests.yml to armor.yml
- [37079](https://github.com/space-wizards/space-station-14/pull/37079) Make universal access config better
- [35681](https://github.com/space-wizards/space-station-14/pull/35681) Vox now can eat trash other other inedible things
  - Do we have to worry about any potential specism issues with this? (Slarti)
  - Worth noting the contributor is a prominent Vox player! (Slam)
- [37061](https://github.com/space-wizards/space-station-14/pull/37061) Atmos air (6500 kPa) marker
- [37027](https://github.com/space-wizards/space-station-14/pull/37027) Updates the Pirate Captain Hardsuit Helmet light sprites.
- [36923](https://github.com/space-wizards/space-station-14/pull/36923) Add noir glasses
  - We all know that this is a vulpkanin trojan horse (Errant)
- [36336](https://github.com/space-wizards/space-station-14/pull/36336) Overhauled stamina slowdown behavior
  - Anyone know how this played on Vulture? (Errant)
- [37084](https://github.com/space-wizards/space-station-14/pull/37084) Wizard Helmet in the Magic Vend
- [37057](https://github.com/space-wizards/space-station-14/pull/37057) Species are now picked at random in the developer environment!
- [36847](https://github.com/space-wizards/space-station-14/pull/36847) Mob Movement Major Refactor
  - Still has a bunch of bugs that should be looked at soon, but nothing compeletely game breaking (Slarti)
- [33470](https://github.com/space-wizards/space-station-14/pull/33470) New Weapon: Knuckle Dusters
  - The (apparently as yet nonfunctional) stun version can be used as a melee weapon even without being worn but I guess since it's not yet mapped/accessible anywhere that's not that big a deal? (Errant)
      - It should be looked at though but not a blocker
- [37146](https://github.com/space-wizards/space-station-14/pull/37146) make node scanner don't show interface if scanned entity not a artefact
- [35149](https://github.com/space-wizards/space-station-14/pull/35149) Sentry turrets - Part 5: Reuseable UI components
- [37060](https://github.com/space-wizards/space-station-14/pull/37060) Revert "Resprited the Chief Engineer's mantle/manica"
- [36369](https://github.com/space-wizards/space-station-14/pull/36369) Replace uplink thieving gloves with chameleon thieving gloves
- [37160](https://github.com/space-wizards/space-station-14/pull/37160) Salvage Threat: Gibtonite
- [37149](https://github.com/space-wizards/space-station-14/pull/37149) Revert "add material composition to some salv treasure"
- [37188](https://github.com/space-wizards/space-station-14/pull/37188) Allow Pacifists to Use Bola
- [37140](https://github.com/space-wizards/space-station-14/pull/37140) Add collapse button to lobby right panel
- [29349](https://github.com/space-wizards/space-station-14/pull/29349) Port fancy speech bubbles
  - Some species (Vox!) still need sprites to support this, but a bigger issue is that the animation only playes while you have NOTHING typed - the first letter you hit, the fancy animation is replaced with the old '...' animation? (Errant)
  - That's how it's supposed to work though, no...? (Roomba)
- [37082](https://github.com/space-wizards/space-station-14/pull/37082) Darken reptilian eye sockets to reduce the effect of mixels
- [36944](https://github.com/space-wizards/space-station-14/pull/36944) Make departmental orders consoles print slips
  - How was this received on Vulture? There was concern on the PR about it being a very annoying stepback toward the previous system. (Errant)
  - Suggestion: a self-serve "Acquisition Form Scanner" could be added to the cargo front desk. Whether it's active or not, and whether it requires the form to be stamped by the relevant head, could either be decided by server cvar, somehow set by crew, or determined by the game (for example, low pop or no cargo on the crew manifest would activate it?) (Errant)
- [37092](https://github.com/space-wizards/space-station-14/pull/37092) Four-way pipe junction, swapping junction construction fix
- [37065](https://github.com/space-wizards/space-station-14/pull/37065) Raises max chest markings for all species (except Reptilian) to 2
- [30683](https://github.com/space-wizards/space-station-14/pull/30683) Make container draw disableble for mob-affecting Hyposprays
  - So what does this actually do? Nothing on upstream, right? (Errant)
      - But a good reason for "Encouraging filling out the pr description"
- [37260](https://github.com/space-wizards/space-station-14/pull/37260) Add 3 new Exomorph posters
- [37281](https://github.com/space-wizards/space-station-14/pull/37281) Tweaks to the push horn so its less of a shitter tool

- [36564](https://github.com/space-wizards/space-station-14/pull/36564) Changed the storage sizes of different swords.
- [37077](https://github.com/space-wizards/space-station-14/pull/37077) Skeletons leave glove fiber evidence
- [37213](https://github.com/space-wizards/space-station-14/pull/37213) More filters for station records
- [37107](https://github.com/space-wizards/space-station-14/pull/37107) Ichor double-metabolize fix + Very minor cleanup
  - This is the thing that heals dragon when they devour mobs, right? While this is a bugfix, it might have an impact on dragon's combat viability? I'm not really knowledgeable about that, but has this angle been considered, in case anything needs to be adjusted to compensate? (Errant)
  - I'm not too up-to-date on space dragon balance however I don't really like bugfixes shadownerfing stuff. If it wasn't an issue when the bug was real then ichor should probably just be buffed back to its pre-bug implementation.
- [37237](https://github.com/space-wizards/space-station-14/pull/37237) Genpop closet cargo orders
- [37234](https://github.com/space-wizards/space-station-14/pull/37234) Cargo request and bounty console deny sound cooldown

## Shitposting Corner
Why....
You know why :3 arf

woof

Niko is a cat.

Finals week or my final week? Stay tuned.
I did well on my finals, I believe in you!
<3
<3

meow :3 :3 :3 mrrp~ meow

I cant get you guys to not add this on the meeting huh...

latrina eschibidia




