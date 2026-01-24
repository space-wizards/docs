# Maintainer Meeting (2 August 2025)

```admonish info

**Attendees:**
- Errant
- ArtisticRoomba
- Myra
- Fildrance
- Slam
- Tiniest Shark
- Slartibartfast
- ScarKy0
- Notafet
```

This meeting was recorded:

{% embed youtube id="8RmeZKz-i_w" loading="lazy" %}

## Go over freezes! (Beck)
- https://github.com/space-wizards/space-station-14/issues/8524
- Which ones are still in effect? (Also they are rarely followed!)

[The issue](https://github.com/space-wizards/space-station-14/issues/8524)

<br/>

- Lobby art: Moved to restrictions
- Guns: This freeze (which has now been moved to restictions) has been getting ignored. Multiple guns have made it past without pinging sloth.
- Clothing variants for mobs: Removed, animations for displacement maps are still an issue but its not an issue for the freeze to stay in effect.
- Clothing variants for mobs: Moved to restrictions, reword after meeting
    - [Relevant](https://github.com/space-wizards/space-station-14/issues/35943)
- New pet clothing: Same as above
- New pets: Has been ignored, FSP has a doc to unfreeze this. Slight rewording for now.
- Roundstart clothing / fluff clothing: Clothe dyeing
- Other silicon law changes or additions: Combined to "New Silicon laws or lawsets" 
- Emag Intaractions: MADE IT LOWERCASE, and changed the requirement from a design doc to maint approval.

## Maintainer Workgroups Reminder (ArtisticRoomba)
A reminder that the Maintainer Workgroups policy has passed its vote and has been merged to the docs repo. You can view the policy [here](https://docs.spacestation14.com/en/wizden-staff/maintainer/maintainer-workgroup-policy.html).

Maintainer Workgroups give Maintainers an opportunity to lead and direct a game area's design and development. These workgroups hold more power over the area and manage design documents, pull requests, and more. If you're interested in leading a game area's development, you should request to create a workgroup with another maintainer (or more!) on the internal forums.

### Reminder for Lead Maintainers
A request to create the Engineering/Atmospherics workgroup needs processing. You can view the request [here](https://forum.spacestation14.com/t/workgroup-creation-request-engineering-atmospherics/22677).
- We are aware we are just handling something else RN (Myra)

## Stable review

:::info
Write your name here if you read this list fully.
**I checked this PR list:**
- Slarti
- Southbridge
- Spanky
- ScarKy0
- Myra
- Tiniest Shark
:::

- [36839](https://github.com/space-wizards/space-station-14/pull/36839) Tweak Vendor Emag Inventory
  - `Slarti`: I kinda liked having emag inventory, and I think it doesn't need removal unless for powerful combat items like the acolyte armor (moving it to the uplink is good, see PR below). Especially the insulated gloves in the YouTool are now just a free roundstart item for the first tider hacking it. So I would propose reverting some of the changes except the overpowered ones.
  - `Beck`: yeah I agree! Its fun to have random things. Overpowered stuff isn't super fun but stuff like the insulated gloves are fun
  - `Scar`: Vendors are like the biggest emag bloat we have currently. I really feel the better option is to give this power more to the crew than just antags. Insuls, sure, are strong, but this doesn't make them any more free than just breaking into engi or getting one from the endless electrical toolboxes. If they prove to be an issue I'd say remove them from both emagged and hacked inventory instead of letting them just be a free pickup alongside the emag. This is the case the PR was meant to prevent (And you can just buy the susbox which comes with insulated gloves anyways).
- Slarti mentioned they will make a pr to move Insulated gloves and flyamita (anamita?) to hacked inventory.
    - Normal pr
- [36843](https://github.com/space-wizards/space-station-14/pull/36843) Add acolyte armor to chaplain uplink
- [38007](https://github.com/space-wizards/space-station-14/pull/38007) Marble tiles
- [38413](https://github.com/space-wizards/space-station-14/pull/38413) Adds Estoc DMR magazines to the syndicate ammo bundle
- [39043](https://github.com/space-wizards/space-station-14/pull/39043) Allow GenPop access perms on the AccessConfigurator
- [38152](https://github.com/space-wizards/space-station-14/pull/38152) Remove omnizine from unwarmed honk pockets, honk pockets make you honk
- [38247](https://github.com/space-wizards/space-station-14/pull/38247) nerf cheese prices, part 3: misc, last one
- [37731](https://github.com/space-wizards/space-station-14/pull/37731) Tighten DB shotgun spread, widened sawn off spread
- [38494](https://github.com/space-wizards/space-station-14/pull/38494) Golden plunger Trolley and Bucket Carp
- [38672](https://github.com/space-wizards/space-station-14/pull/38672) More atmos devices can be placed on layers easier.
- [36881](https://github.com/space-wizards/space-station-14/pull/36881) Crawling Part 1: The Knockdownening
- [39106](https://github.com/space-wizards/space-station-14/pull/39106) China lake rebalance
- [39158](https://github.com/space-wizards/space-station-14/pull/39158) Tweaks nukeop elimination announcement to be less wordy.
- [39142](https://github.com/space-wizards/space-station-14/pull/39142) Standardize and ngooden MIDI music via a good default soundfont
- [39153](https://github.com/space-wizards/space-station-14/pull/39153) Emissive engineering & chief engineer's hardsuit helmets
- [39177](https://github.com/space-wizards/space-station-14/pull/39177) Add name to AI eye
- [36316](https://github.com/space-wizards/space-station-14/pull/36316) Makes cold slowdown less punishing
- [37924](https://github.com/space-wizards/space-station-14/pull/37924) Change potassium-water explosion scaling
- [37915](https://github.com/space-wizards/space-station-14/pull/37915) Change smoke/foam/explosion chemistry reaction order & energy transfer
- [36969](https://github.com/space-wizards/space-station-14/pull/36969) Admin Tool: Observe entities in an extra viewport
- [39011](https://github.com/space-wizards/space-station-14/pull/39011) Added Kill Tome (Death Note).
  - `Slarti`: I don't think this item should be ever available to anyone, it will be mostly frustrating to players if you suddenly die without knowing why or any way to prevent it. Whoever has it can just write the whole crew manifest into it and the round is instantly over. So I don't really see the point even as an admeme only item. Also the code is pretty bad performance-wise and needs some work. I left a review for the stuff I found, Sloth had [some comments](https://discord.com/channels/310555209753690112/1193403928096821358/1398673830351736924) as well, saying it should be reverted. So unless someone fixes it up in time for the release I would revert it for now.
  - `Scar`: Saying it shouldn't be available to anyone is based on the fact that the admin wouldn't be making sure it isn't misused. The few times I spawned it in the server had a lot of fun chasing the "Kira" and alike. That is the case for any currently available admeme item, where it can be abused without admin supervision, that is why they are admeme only and will only be accessible with admin supervision. As for performance, making it cached means it will work 50% of the time with players joining and all, and since it isn't publically available I don't know whether it matters so much. But if it does, I guess I understand wanting to revert it.
    - BLOCKING: Vote to revert till code improvement: Revert (Until code improvement) / Keep
        - Scar said they had interest but not guaranteed.

- [39230](https://github.com/space-wizards/space-station-14/pull/39230) Make the cherry pit tiny
- [39233](https://github.com/space-wizards/space-station-14/pull/39233) Added utility belt function to scrap armor
  - `Slarti`: I'm not a fan of this one, this just feels like the usual storage space power creep. And armor clothing really shouldn't grant you extra storage slots.
  - `Beck`: I think its ok for this - the armor is not used often (I think - we need a stats system so we could tell for real!) and it makes sense because you use a belt
    - BLOCKING: Vote to revert: Revert / Keep
- [39111](https://github.com/space-wizards/space-station-14/pull/39111) Add scaling filter option (Nearest/Bilinear)
- [39250](https://github.com/space-wizards/space-station-14/pull/39250) Plushie sound 1984
- [39213](https://github.com/space-wizards/space-station-14/pull/39213) allow janibelt to hold golden plunger
- [39254](https://github.com/space-wizards/space-station-14/pull/39254) Added a network configurator to the Warden's locker.
- [39259](https://github.com/space-wizards/space-station-14/pull/39259) Quartermaster job and ID icon change
- [38811](https://github.com/space-wizards/space-station-14/pull/38811) Retry of Advanced Chem Tweaks
- [39222](https://github.com/space-wizards/space-station-14/pull/39222) New recipe: Cotton Cakes
- [39285](https://github.com/space-wizards/space-station-14/pull/39285) Change the description of barefoot drink.
- [37701](https://github.com/space-wizards/space-station-14/pull/37701) Adds Wizard's Den (Replaces Wizard Shuttle)
- [36289](https://github.com/space-wizards/space-station-14/pull/36289) EntityEffectConditions changed to be inclusive of min/max
  - `Slarti`: This PR changed all the thresholds to be inclusive without adjusting any recipes. Pretty sure that will also now include all overdose amounts for medicine, which will be annoying for those at exactly 10u. And it will create some different behaviour for reagents like nocturine that start having an effect at a certain reagent amount. So we should go through all reagents and make sure there are no larger changes in balance or behaviour.
      - Someone should go through to check everything


### Reminder to the person who handles stable merge
Ping the author on the revert PR

### Shitpost Corner

We need more funny admeme only items PLEASE -Scar
Dont you have an admeme repo for that?
Can we add [Brookies](https://serenetrail.com/wp-content/uploads/2024/04/Up-close-image-of-brookies.jpg) they are so tasty
