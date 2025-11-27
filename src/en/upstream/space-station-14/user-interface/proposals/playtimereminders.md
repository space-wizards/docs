# Playtime Reminders

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| Bhijn & Myr | Bhijn & Myr | :information_source: Open PR | https://github.com/space-wizards/space-station-14/pull/36483 |

## Overview

This is a proposal to add a message to the lobby screen that reminds the player exactly how much time they've spent on the game in a given day. In some countries, playtime reminders in video games are mandated by law (though these are often met with malicious compliance from game developers, if complying at all). These laws are often backed up by various studies proving their effectiveness in defusing video game addiction, and deterring addiction from forming.

## Background

This is primarily spurred by internal staff discussions, where we've broached the topic of addiction. [Those with access to the forum's staff categories can read our internal post here](https://forum.spacestation14.com/t/19282/7).

Currently, addiction to the game is viewed as socially acceptable across the SS13 and SS14 (here-on referred to as SS1X) community. When players bring up that they've been spending 60+ hours a week on the game (an amount of time that, with a full time job, leaves very little time for basic life necessities. Some players even break into the 100+ hour/week threshold, which, even if unemployed, leaves no time for life), the response from their peers is a mix of thinking they're joking or exaggerating, and sometimes goading them into playing even more. Their peers simply don't see an issue with that excessive playtime. But these players are often serious; viewing their replay history reveals that they are indeed spending that much time on the game.

These players often exhibit all the stereotypical symptoms associated with addiction. When there's something that they don't like, like another player doing something odd, or a change to the game is made that they perceive as an inconvenience, they have a strong knee-jerk reaction to it (usually a distinctly negative one). When something can potentially take away their ability to play the game, they perceive it as a personal threat (this is most prevalent in ahelps, where particularly invested players are usually irrationally hostile towards admins). And when they're unable to play the game, they can grow quite desperate (whether it's being round-removed, banned, gated by the playercount limit, or blocked by technical issues).

These symptoms are a heavy contributor to community-wide toxicity. Not just on Wizden, but SS1X as a whole. For these players, SS1X is effectively their life, and the impact on their mental health is quite obvious to those who know the signs of addiction. Yet no one really speaks up about it, and peer acceptance leads to these players neglecting their real lives to a problematic degree. As the addiction grows, their mental health gets worse, leading to an increase of toxicity for them. We know full well that publishing this proposal and accompanying PR will make us a target for this toxicity, but we don't care, as it'll only prove our point.

The community's normalization of addiction doesn't just affect the addicted players themselves, but also the volunteers behind servers. Admins and developers alike are frequent targets of toxicity from these players, as admins and devs are often irritants for them. These players also tend to strain inter-server relations, as being banned leads to them filtering towards other servers and declaring their ban unjust, which can turn that server into an echo chamber of toxicity towards the server they were banned from (with the most common indicator of such being bans from that server being viewed as honorable or a rite of passage; Wizden is a common target of this in SS14, as was Goonstation in SS13 prior to Ssethtide). This toxicity is a major contributor to staff members of various servers burning out across the SS1X community.

Due to the nature of SS1X's innate design, there's simply no good way to eradicate addiction to it. The round-based format of multiplayer games is known across the games industry to be one of the most addictive there is. On paper, rounds offer a natural stopping point for playsessions, but in reality, this very frequently leads to players overcommitting playtime with the thought of "well, just one more round wouldn't hurt" (at which point they're committed, and are deterred from stopping due to a mix of FOMO, and punishments often being present for leaving mid-round. In SS1X, you're socially locked in for the whole round due to the expectation of you doing your job). This tendency to cause overcommittal is a volatile catalyst for habit-forming, one of the biggest risk factors in something becoming a psychological need (especially among groups particularly vulnerable to that, notably minors and neurodivergent individuals. Coincidentally, the latter's the largest demographic of SS1X).

In centralized multiplayer games, playtime limits can curb addiction to a given game by directly discouraging prolonged playsessions. A famous example of this is World of Warcraft, where you get a boost to experience when logging in after being offline for a while, and various pieces of content can only be done once a day or week. However, this simply doesn't work in a game like SS1X, as every server is its own isolated environment and codebase. Neither a hardset playtime limit nor a softer enforcement will work here, as players will opt to simply hop to a different server, where they're free of those limits (or more likely, where those limits don't exist to begin with).

While existing cases of addiction can't really be stopped directly, there's ways to help stifle the formation of addiction, as well as encouraging healthier life habits in those spending a lot of time playing the game. One such example of this is a [recent small PR increasing the amount of time the server spends in the lobby](https://github.com/space-wizards/space-station-14/pull/36476), allowing players to, among other things, have a reasonable amount of time for a bathroom break between rounds.

A far more impactful method is the subject of this proposal document: directly reminding the player how much time they've spent playing the game. Yes, this is something regularly ridiculed by gamers unaccustomed to them (see: the reactions of gamers to the playtime reminders common in the EU and South Korea), but the truth is that this works. One of the bigger factors in addictions forming is a genuine lack of self-awareness around the subject of that addiction (Y'know, the stereotypical "No, it's not an addiction, I can stop at any time" spiel). By directly informing a given player of just how much time they've been playing, they're able to make a much better-informed decision on whether to continue playing. Instead of "eh, just one more round, it isn't *that* late", a player can see that they've spent 6 hours ingame that day, potentially swaying them to take a break.

## Features to be added

A fairly simple addition to the lobby screen.

If a player has spent more than an hour actively playing ingame on a given day, a notice should appear underneath the left top panel in the lobby, stating exactly how many hours have been spent within that day, alongside a reminder to take a breaks. This is likely to kick in after two consecutive rounds on Wizard's Den, as rounds are usually just under an hour long.

This mockup illustrates an example of how that'd look.

![UI mockup of the playtime reminder](media/playtime-reminder-mockup.png)

When implemented, this reminder should be simple, and to-the-point. No fluff necessary, just a pure statement of how many hours have been spent.

The left top panel is an excellent spot for this reminder, as it's right underneath the button to play another round. This makes it unlikely that a player would miss it.

## Game Design Rationale

See background section.

## Roundflow & Player interaction

N/A

## Administrative & Server Rule Impact (if applicable)

As detailed in the background section, this is very likely to have a positive impact on administration, as this encourages players to live a healthier life. Addiction to the game is a major underlying contributor to the toxicity faced by staff. By taking steps like this to help alleviate addiction, staff should hopefully see a gradual decrease in toxicity.

It may potentially be productive to implement similar reminders for admins to take breaks as well, 

# Technical Considerations

There's many valid ways to implement this. The most straight-forward one is a client-side approach, as this allows the tracking to properly function across servers that port the implementation. The client-side approach is also fairly trivial to keep self-contained and simplistic, keeping potential maintenance overhead low.

The alternative route is to implement this from the server's side itself. However, this makes it far more complicated to account for the player's timezone, and is generally more demanding from an engineering standpoint. To do it properly from the server, there would need to be a way to get an exact timeframe worth of playtime from a specific player. This currently isn't doable with the server's current schema, to our knowledge.
