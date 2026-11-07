# 2026-09-26 Maintainer Meeting

:::info
## Maintainers In Attendance

* Ada 
* Aeshus
* Electro
* Errant
* Fildrance 
* Maybe
* Nem 
* Princess Chzblz 
* Samuka 
* Scar 
* Slam 
* Velken

:::

(Meeting recording goes here)

# Topics

## Release update policy (Fildrance)

We need to agree on policy changes!111

<https://github.com/space-wizards/docs/pull/676>

Errant: Regardless of where this goes, can we agree to do the next staging cutoff earlier, as proposed? Even if this would result in a temporary departure from the current release procedure

*Pushed to a follow-on meeting due to Jez attendance* 


## The game is running poorly? (Errant)

There seems to have been a lot of performance complaints lately. We should see if we can quantify anything, and even if we can't immediately find the reason, determine if we can narrow this down to just the master branch / Leviathan

*Seems to be a server side issue with deleting an ent leaving a dangling ref in a tree that leads to bad data causing clients to be dropped.* 

***ACTION*** *Coalesce information from this issue with a GH issue on engine (Electro will look at it!)*

Not a release blocker.


## Forks are not happy with the way breaking changes are provided (Fildrance)

Its important that forks are not ‘following forum and applying changes as they appear, they merge upstream into fork and then have to search through all changes. Usually they will search classes that are related to code that does not compile or have some bugs.

So forum is neat but its kinda invalid way to do things for downstream.

More details here <https://forum.spacestation14.com/t/better-communication-regarding-breaking-changes/28601/5>

Other problem is that breaking changes are not really bound to any release. It would be better to mark all PRs and issues with labels of release when it is published, i suppose? Maybe even mark nightly stuff? Its not obvious tbh. But it won’t help forks by A LOT here too, because they need a tool to find source of broken code, not search through tons of topics (even filtered by release version, it won’t help by a ton).

*Downstreams need to be well integrated with this process and discussion. Using a text file in a similar vein as* `*migrations.yml*` *may be the best option. We need to communicate planned breaking changes with broad impacts in advance of them occurring. A wiki may be a better option - go from file to wiki later.*

***ACTION*** *Gather a list of possible options for presentation to our DSR team and see what our ecosystem wants (Chzblz has already put this on the NextCloud, will be getting hivehum on it)* 

# Release Blockers

* <https://github.com/space-wizards/space-station-14/pull/46169> 
  * *Bricks storage implanters and other storages. Needs an integration test and a merge ASAP.*
  * ***ACTION*** *Review this (Done)*
* <https://github.com/space-wizards/space-station-14/pull/46072>
  * ***ACTION*** *Review this (Done)*
* Disabler/Stun Baton changes (Maybe not a blocker, move to topics?)
  * These changes are experimental, so we should probably get a finalized version before stable.
    * Stun baton straps?
    * Energy shotgun still stuns
    * Are disabler changes fine?
    * How does the bola fit into this?
  * `Slam`:  Ye this needs to be discussed. My thoughts are the following:
    * Overall this is a nerf to Security, but I am less concerned about that and more about how it feels to interact with Security + stuns. In this regard, I think it is an improvement. The disabler and stun batons work well to deal with shitters and non-lethal threats; disabler slowdown makes chases easier, stun baton strap heavily reduces the sense of “risk of lethality” Sec has to deal with. Stuns are essentially unusable against lethal threats (especially nukies, which now take ages to stun not counting hyperzine) but can be used if you are two or more SecOffs due to friendly fire being less of a concern. 
    * Disablers are now (after the nerf and then subsequent buff) considered weak by the playerbase, but they do see use. We had a period where SecOffs went into using lethals more heavily but I think that’s passed. It works very well as a chase tool or to keep distance, i.e. situations where you are going to be at range and the movement of the other party is predictable. It’s now useless in melee range, which is good, because previously it worked very well in melee as well. After using it myself, the main annoyance is low ammo capacity per stun (faster charge could work).
    * I think the negative reaction to the stun baton strap thing was mostly a kneejerk reaction. SecOffs losing their baton to an unreactable slip can be very lethal and I think the “predict hold shift to walk” being a core part of Sec arrest gameplay is just [*fart noise*]. Slips are still good in that they buy you time to get away, and if they got a disabler out instead you can always yoink that, which is a lot less lethal for the SecOff *and* makes it easier for you to escape.
    * ((a meme image was embedded here)) Bola slowdown kinda strong ngl, especially now that SecOffs use them more. 
    * *We may make it automatic but we will come back to revisit this later*
  * ***ACTION*** *We are keeping these changes for now, review nukie balance, e-shotty balance, bola balance* 

    (Done #46207)\n 
  * `Jezi`: This should probably be covered at the end in topics.
* `Slam`: Prototype uploads are still broken. There is half a fix implemented, but it doesn’t solve all of it. The issue is that prototypes are validated upon being uploaded but before they are registered, so any reference to a custom entity prototype causes a validation failure. 
  * `Velken`: Somehow even protouploaded FTL are failing validation when you try to reference them.
  * `Slam`: Probably same issue; they aren’t taken into consideration for the validation…
  * ***ACTION*** *Create a CVar to disable validation on uploads enabled by default, then change it to disabled by default later. (Slam will get this)* 

# I read through the PR list:

* ScarKy0
* Meow
* Princess
* Velken
* Nem
* ada

# PR List

(excluding bugfixes, small and medium refactors and mapping changes, text only changes or similar)


* [45402](https://github.com/space-wizards/space-station-14/pull/45402) Add Postboards for displaying papers publicly - Reforked PR #44792


* [45421](https://github.com/space-wizards/space-station-14/pull/45421) Botany Random Chem Table Weight Tweaks


* [45541](https://github.com/space-wizards/space-station-14/pull/45541) Changes potassium iodide to digestion, adds 20u pill to emergency boxes
  * `Slam`: The way pills and digestion works right now is lowkey kind of frustrating (I love giving someone a 20u Dexalin pill and it does *nothing!*). We are amassing patchwork debt like this PR. What are our plans for this?
  * `Nem`: I do not like this. There’s no reason to do this other than filling a hole in a box. KI pills are already reasonably available via radiation lockers, which makes much more sense.
  * * `ada`: Agreed it feels unnecessary.


* [44507](https://github.com/space-wizards/space-station-14/pull/44507) Atmospheric pipe layers YAML simplification


* [45445](https://github.com/space-wizards/space-station-14/pull/45445) Radial Sorting: add explicit order field


* [45231](https://github.com/space-wizards/space-station-14/pull/45231) Injecting entity table conditions into context


* [41949](https://github.com/space-wizards/space-station-14/pull/41949) Fix projectile grenades (stingers, shrapnel, incendiary) going through walls, and projectile distance


* [45583](https://github.com/space-wizards/space-station-14/pull/45583) EntTable EmptyContainerCondition


* [45612](https://github.com/space-wizards/space-station-14/pull/45612) Make counter tables block crawling underneath
  * `Slam`: Should be propagated to the mappers so they are aware.
  * `Slam`: There is a small concern that the counters aren’t very distinct compared to tables. I know a few maps that use reinforced tables because they look like they could be proper counters. Kazne should be poked about keeping this in mind for the respritening. 


* [45622](https://github.com/space-wizards/space-station-14/pull/45622) Allow the baseball burger to be caught like other balls


* [45377](https://github.com/space-wizards/space-station-14/pull/45377) Resprited MMI and recolored brain cakes


* [45674](https://github.com/space-wizards/space-station-14/pull/45674) changeling store update


* [45667](https://github.com/space-wizards/space-station-14/pull/45667) Hushpup Spread Tweak


* [45711](https://github.com/space-wizards/space-station-14/pull/45711) Readds random rotation and offset to dev map


* [45701](https://github.com/space-wizards/space-station-14/pull/45701) Add chameleonOutfit and startingGear prototypes for prisoners


* [45729](https://github.com/space-wizards/space-station-14/pull/45729) Make living tissue contain the changeling's DNA


* [45705](https://github.com/space-wizards/space-station-14/pull/45705) Make metal foam preserve tile air


* [45749](https://github.com/space-wizards/space-station-14/pull/45749) Buff changeling devour and windup damage (resubmit of #45743)


* [45692](https://github.com/space-wizards/space-station-14/pull/45692) [HOTFIX] Prevent Off-Station Objective Targets


* [45738](https://github.com/space-wizards/space-station-14/pull/45738) [HOTIFX] Changelog actualisation for stable release


* [44346](https://github.com/space-wizards/space-station-14/pull/44346) Device Network refactor part 1: API improvements


* [45608](https://github.com/space-wizards/space-station-14/pull/45608) Feature/refactor xenoarch trigger to be entity table ed


* [45681](https://github.com/space-wizards/space-station-14/pull/45681) Midround Changelings


* [45748](https://github.com/space-wizards/space-station-14/pull/45748) Buff the China Lake to be stronger and more lethal (resubmit of #45685)
  * `Slam`: I don’t think Nukies have realized how strong it is yet. Keep an eye on it.
    * `Velken`: 9/10 Nukies still traumatized with old clake and immediate shout “NO!” to it.


* [45754](https://github.com/space-wizards/space-station-14/pull/45754) Add grenade (round) descriptions, proper noun China Lake


* [45808](https://github.com/space-wizards/space-station-14/pull/45808) Change the bug report URL from Github to the Bug Reports forum


* [45400](https://github.com/space-wizards/space-station-14/pull/45400) Electrify critical machines


* [45810](https://github.com/space-wizards/space-station-14/pull/45810) Allow feedback pop-ups to show always when opening the feedback window


* [45807](https://github.com/space-wizards/space-station-14/pull/45807) Add a Report Bugs button to the escape menu


* [45769](https://github.com/space-wizards/space-station-14/pull/45769) Allow for multiple mutation and chem tables


* [45752](https://github.com/space-wizards/space-station-14/pull/45752) Botany Refactor Bugfixes and Value adjustments


* [45724](https://github.com/space-wizards/space-station-14/pull/45724) Fake Armblade Sting


* [39434](https://github.com/space-wizards/space-station-14/pull/39434) Image Overlay for welding masks
  * `Slam`: We need to have a pass on flashes, since this has *drastically* reduced the welding mask usage. 


* [45511](https://github.com/space-wizards/space-station-14/pull/45511) Properly split "Service" and "Civilian" into separate departments


* [45837](https://github.com/space-wizards/space-station-14/pull/45837) Add heart attack smite for admins


* [45823](https://github.com/space-wizards/space-station-14/pull/45823) Crew-sided stuns rebalance


* [45634](https://github.com/space-wizards/space-station-14/pull/45634) Make self-vaulting not interruptible by damage, prevent crawling past holobarriers
  * Errant: We should consider making unarmed shoves prevent vaulting. That way you can still stop someone from coming through, but it requires YOU to take a risk if there is combat, and works just fine if there is not. It also makes thematic sense - you shove them off. (Also, turns out editing Outline on mobile is wretched, someone please indent this)


* [45850](https://github.com/space-wizards/space-station-14/pull/45850) Added a recipe to teargas


* [45775](https://github.com/space-wizards/space-station-14/pull/45775) Added night vision status effect AND a night vision drug


* [45469](https://github.com/space-wizards/space-station-14/pull/45469) Zombie event tweaks for new ambu changes


* [45853](https://github.com/space-wizards/space-station-14/pull/45853) Hivarol no longer requires licoxide, needs histamine instead


* [45835](https://github.com/space-wizards/space-station-14/pull/45835) Vulpkanin Welding Gas Mask Sprite


* [45859](https://github.com/space-wizards/space-station-14/pull/45859) Martinis - Stirred, not shaken


* [45763](https://github.com/space-wizards/space-station-14/pull/45763) Added the ability for cargo to order a crate of mosins


* [45350](https://github.com/space-wizards/space-station-14/pull/45350) Cleanup of UseDelay


* [45869](https://github.com/space-wizards/space-station-14/pull/45869) Make bolas able to be removed as long as any hand is free, reduce Sec locker bola count


* [44138](https://github.com/space-wizards/space-station-14/pull/44138) Energy Bow Nerf
  * `Slam`: I feel like I haven’t seen enough use of these. Would like to monitor this more and get others’ opinions.
    * `Velken`: Saw some players use as a “Stay Away” tool rather than an “You are going to die now”


* [45867](https://github.com/space-wizards/space-station-14/pull/45867) [Map] Nukie planet - roof test


* [45886](https://github.com/space-wizards/space-station-14/pull/45886) Tweak disabler/disabler SMG values up


* [45887](https://github.com/space-wizards/space-station-14/pull/45887) Make stun batons not drop when slipping/stunned
  * `Slam`: See dedicated topic


* [45647](https://github.com/space-wizards/space-station-14/pull/45647) Changelings as Foreign Invaders


* [45904](https://github.com/space-wizards/space-station-14/pull/45904) change ultravasculine plasma required to catalyst


* [45901](https://github.com/space-wizards/space-station-14/pull/45901) Nutriment Metabolism Adjustments


* [45948](https://github.com/space-wizards/space-station-14/pull/45948) Oppo and Aloxadone tweaks


* [45740](https://github.com/space-wizards/space-station-14/pull/45740) changed ultravasc in poison pen to stellbinin


* [45962](https://github.com/space-wizards/space-station-14/pull/45962) Simplify ultravasculine recipe ratio for better readability


* [45967](https://github.com/space-wizards/space-station-14/pull/45967) Changeling Carepackage


* [44936](https://github.com/space-wizards/space-station-14/pull/44936) Telepad can link to multiple consoles
  * `Slam`: This is the big Cargo rebalance PR.
  * `Slam`: Personally I think this one has worked fine as non-Cargo, but I would like to hear your thoughts.


* [44887](https://github.com/space-wizards/space-station-14/pull/44887) Galaxythistles are flowers
  * `Nem`: Has issues with the flower tag, although this is more with the tag itself


* [45998](https://github.com/space-wizards/space-station-14/pull/45998) Adjust Structural Damage of Weapons


* [45510](https://github.com/space-wizards/space-station-14/pull/45510) Shield Adjustments based on feedback.
  * `Slam`: I have heard that energy shields are kind of buns now? We might need to do a pass on those.


* [45987](https://github.com/space-wizards/space-station-14/pull/45987) Digiboard can be linked to the telepad.


* [46041](https://github.com/space-wizards/space-station-14/pull/46041) Buff disablers into stunning again, minor beanbag nerf


* [46029](https://github.com/space-wizards/space-station-14/pull/46029) Action Requirements


* [45348](https://github.com/space-wizards/space-station-14/pull/45348) Move truncheon & telescopic shield to T2 research, make truncheon 2x3


* [45834](https://github.com/space-wizards/space-station-14/pull/45834) Move GameTicker to Shared
  * `Velken`: We still gotta keep an eye if nothing ancient is silently breaking in the background.


* [45550](https://github.com/space-wizards/space-station-14/pull/45550) Move admin smites to prototypes


* [46052](https://github.com/space-wizards/space-station-14/pull/46052) Examinable Changeling Doafters


* [42891](https://github.com/space-wizards/space-station-14/pull/42891) Added accuracy values for pistols, SMGs and rifles, including spread increase per shot and spread recovery time


* [45931](https://github.com/space-wizards/space-station-14/pull/45931) You can now water plants directly


* [46083](https://github.com/space-wizards/space-station-14/pull/46083) Fix space racism


* [45868](https://github.com/space-wizards/space-station-14/pull/45868) Clean up obsolete chat styles


* [45820](https://github.com/space-wizards/space-station-14/pull/45820) Standardize UI separators


* [45843](https://github.com/space-wizards/space-station-14/pull/45843) Energy Gates make a swoosh sound when you walk through them


* [45955](https://github.com/space-wizards/space-station-14/pull/45955) Predict SpawnAfterInteractSystem


* [45759](https://github.com/space-wizards/space-station-14/pull/45759) SHARK
  * `Slam`: The sharkminnows are lowkey kind of tanky, which can be frustrating when dealing with a rift that you need to take down. I feel like the PR should have motivated the minnow’s stats rather than just “nice variety”. Will probably see someone PR a tweak in the future. 
    * `Velken`: I can see it being moved to spawn only on 100% rifts.


* [45742](https://github.com/space-wizards/space-station-14/pull/45742) Brute pen tweaks


* [45397](https://github.com/space-wizards/space-station-14/pull/45397) mime crayon in PDA instead of pen


* [46051](https://github.com/space-wizards/space-station-14/pull/46051) Changeling Sting Carepackage


* [46106](https://github.com/space-wizards/space-station-14/pull/46106) Add support for dialogue variation for SpeakOnActionSystem


* [46116](https://github.com/space-wizards/space-station-14/pull/46116) Move RuleGridSystem to Shared


* [43651](https://github.com/space-wizards/space-station-14/pull/43651) Add industrial smelters (admin only)


* [45219](https://github.com/space-wizards/space-station-14/pull/45219) Standardized EVA Storage access (Part 1)
  * `Velken`: Right now, these just became copies of HoP’s door. I personally would like that they have some texture or something to differentiate them.


* [41180](https://github.com/space-wizards/space-station-14/pull/41180) Ninja headset / lighter are now highly illegal contraband
* <https://github.com/space-wizards/space-station-14/pull/45699> Split ERT/CBURN/DeathSquad off into their own department


* [44802](https://github.com/space-wizards/space-station-14/pull/44802) Adjustments to emergency locker fills


* [45098](https://github.com/space-wizards/space-station-14/pull/45098) Add Salt and Pepper Containers and Sources


* [44989](https://github.com/space-wizards/space-station-14/pull/44989) Added Wheelchairs to Medical Techfab


* [46075](https://github.com/space-wizards/space-station-14/pull/46075) Fix station job slot configs to work with minimum job slots


* [45029](https://github.com/space-wizards/space-station-14/pull/45029) increase scram implant radius to useful range


* [46156](https://github.com/space-wizards/space-station-14/pull/46156) Giant Spider Variants + Venom modification V2
  * `Slam`: Merged right before cutoff so keep an eye on this. 


* [45851](https://github.com/space-wizards/space-station-14/pull/45851) Changeling Fleshtomb
  * `Velken`: Technically an Experimental, just hadn’t time to live on master for long before cutoff, do still want to keep it for stable?
  * `Scar`: The idea is experimental the PR is not, id need a lot of time with it to figure out how to move forward with it, which i cant really get on lizard only I feel.


* [44709](https://github.com/space-wizards/space-station-14/pull/44709) Add "new player label" over the head of players joining the game for the first time


* [46163](https://github.com/space-wizards/space-station-14/pull/46163) Updates to sandals (i.e, tourist shoes / wizard shoes)
  * `Slam`: I feel like the PR author misunderstood the tourist sandal joke? That being socks in sandals. Shame to lose that. :/ 
    * `Velken`: We need sandals with socks joke back, maybe a crafting with any sandals + cloth.
  * `Nem`: Unvalidated art changes


* [46056](https://github.com/space-wizards/space-station-14/pull/46056) Extinguisher/Fireaxe/Shotgun Construction Graphs


\

# Question Time!

## Mapping Editor When

No ETA. But Please :)

## How is Data Collection going for Tests

Data collection is still down since grafana is still broken.

Testing has been going well and we’re getting a lot of useful data.

## Shipbreaker

Slam is trying to bribe scar to review it

## Cool Species Proposals?

We haven’t looked at them in a while since we’re looking at moving away from Github for Design Docs.

## When will ATS hijack be rebalanced?

Low priority for princess due to blocking PRs and low motivation.


Releases since the last non-squashed PR: 


*Niko is a cat*
