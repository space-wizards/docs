# Game Director
```admonish warning "Attention: Legacy Documentation!"
This document is ported from before the game-area reorganization and has not been reviewed or updated.
It may not fit with the new design requirements.
```
| Designers | Implemented | GitHub Links |
|---|---|---|
| tom-leys (RecallSingularity) | :information_source: Open PR | https://github.com/space-wizards/space-station-14/pull/16548 |

## Overview

Triggers game events to attain a chaos goal. Goal varies during each round to create variety. 
By measuring and varying chaos, the director keeps the challenge each round within a fun band. It reacts to player success
or failure by tailoring future events based on current chaos measured.

The Game Director adds new game modes, initially CombatDynamic and CalmDynamic. They can only be triggered by an admin
running for instance `addgamerule CalmDynamic`. A later PR could put them into automatic rotation. 

## Background

Events in SS14 trigger challenges or benefits for players. They might spawn spiders, dragons or zombies. Traitors 
come on board, Nukies attack or vents spew grease. Pizza might be delivered or power is turned off to sections of the station.

Historically events trigger in a few ways:

- At round start (for instance a zombie or nukie round begins)
- Randomly, every 5 minutes or so (extended rounds) 
- Randomly, at an increasing pace (survival rounds, now discontinued)
- Due to admin commands such as `addgamerule`
- Hand created by admins adding entities and using admin tools.

In the absense of administrator intervention, extended rounds can become boring and monotonous. Zombie or Nukie rounds 
are often boring for a period, intense for a period and if the station is saved boring again.

Due to the random nature of the extended round system, events cannot be too dangerous or too beneficial to the players
or through RNG they are likely to trigger at the worst time. One station might be flooded with spiders, a dragon and space lube 
under every vent while another only suffers a few rats and some flickering lights.

The Game Director aims to provide an alternative to the extended mode that is flexible and drives a fun set of events 
towards a larger set of Chaos Goals. A wide array of extreme events both positive and negative can then be added to the game
safe in the knowledge they will be run at suitable times rather than randomly.

Discord Topic: https://discord.com/channels/310555209753690112/1110002801448329226
GitHub PR: https://github.com/space-wizards/space-station-14/pull/16548

### Car Metaphor

Imagine you are driving on the highway. You look at the metric of your speedometer to see how fast you are driving. The
speed limit specifies how fast you should go. You then pick either the apply gas, reduce gas or turn on radio events to 
best match the car speed to the goal set by the speed limit. The director works in a similar way.

## Basic method

- **Chaos** - Metrics we are measuring and controlling with each event
- **Story** - Determines a series of Chaos Goals
- **Metrics** - Estimate the existing chaos on station
- **Events** - Have a predicted effect on chaos
- **Game Director** - Pick best Event to achieve story Metrics 

1. **Wait** until it is time for next event
2. Run **metrics** to measure current **Chaos**
3. Advance **StoryBeat** and **Story** (over time or based on Chaos)
4. Read **desired Chaos** from **current StoryBeat**
5. **Rank** valid events to achieve near desired chaos
6. Run **best event**

## Chaos - Metrics of a station

We want to measure how bad the Chaos is right now. If the station is doing well, the lights are on and the floor is clean, 
we expect low chaos scores. If the lights are out, the place is spaced and enemies are roaming the station, we want high 
chaos scores.

To best tailor events to the exact situation on the station, chaos is measured by several metrics. 
The solution to hunger is pizzas. The solution to enemies might be a squad of reinforcements. A station
that is too peaceful is ready for meteorites, spiders or other hazards.

A wide range of challenges should be reflected by moderate chaos values for every metric to best challenge all departments 
on the station. For instance many new anomolies will keep science busy and potentially annoy other players. But anomolies won't 
tax security the same way traitors or spiders would.

Obvious metrics, where a perfect station has chaos of 0 and it increases as things get messy:
- Hunger 
- Thirst
- Anomaly
- Death
- Medical
- Security
- Power
- Atmos
- Mess

Combat metrics:
- Friend - negative to represent how many friendlies are alive on the station 
- Hostile - Score for all antags and monsters
- Combat - Friend + Hostile. <0 if crew is strong. 0 if balanced (fighting). >0 indicates crew is losing.

## Story - Determines a series of Chaos Goals

Stories are composed of StoryBeats and determine the Chaos Goals over a 15-30 minute period within a round.

Beats generally last 5 minutes each, though they might end early if chaos hits certain thresholds. 
These are called `endIfAnyWorse` and `endIfAllBetter`, useful if there is too much war, or perhaps too much peace.

Once a story beat has ended, the director will move to the next beat in the story. Once a given story has finished, the 
director will pick one of its stories at random to start. 

Player experience in SS14 should have both its highs and lows. A peaceful extended shift can become boring with no challenges 
to overcome together. An overly intense battle might kill half the crew and leave the station in disorder that we cannot recover from. 
What we want is a middle ground with some variation.

The ideal story has a mix of both, with order followed by disorder and then a chance to recover and rebuild. We want variety with 
pleasant cycles in intensity potentially building towards an overall climax as the round progresses.

### Dynamic Game Modes: 

Each game mode preset specifies which stories will run and so determines the tone for the experience created by 
the director. 

The number of stories and story beats is quite small right now, as we add more content to the game we will also expand 
the range of stories followed by the director to increase the tonal variety between rounds. 

#### CombatDynamic
Contains combat stories and so will create a station with some fighting
- **RelaxedAttack** - Peace -> AttackMild -> EngineeringIssues
- **ScienceAttack** - Peace -> MadScience -> AttackMild -> Peace -> EngineeringIssues -> RepairStation
- **MajorCombat** - Peace -> AttackMild -> EngineeringIssues -> Attackers -> RestoreOrder -> RepairStation -> Peace

#### CalmDynamic
More like an extended round, has a balance of minor chaos events
- **Relaxed** - Peace -> AttackMild -> EngineeringIssues
- **Science** - Peace -> MadScience -> Peace -> EngineeringIssues -> RepairStation

### Story Beats
Some beats deliberately drive moderate or high chaos for a period of time. Others bring specific types of chaos to near
0 to encourage the director to pick helpful events until the station is moderate again.

The hostile story beats tend to end if the station chaos rises too high. The recovery ones end if the chaos drops low 
enough. By incorporating both into a story we can expect some hostile events, a period of chaos followed by positive 
events and a period of recovery.

- **Peace** - Minor Chaos across a wide range
- **PowerIssues** - Create high engineering chaos
- **MadScience** - Create high Science chaos
- **Attackers** - Drive high combat
- **AttackMild** - Drive medium combat
- **RestoreOrder** - Send help to quell disorder on the station
- **RepairStation** - Repair that station

## Metrics - Estimate the existing chaos on station

A number of systems called "Metrics" are used to summarize the chaos levels. Metrics each stand alone and so it will be 
easy to add or remove them as the game matures.

Metrics could subscribe to relevant events and dynamically adjust their scores as events occur on the station. Or they 
can do a single pass through the component system when run. The single pass approach has been preferred in favor of its 
stability and simplicity for now.

#### Metrics at the moment
- **AnomalyMetric** - Are there many? Are they out of control? Writes to "Anomaly"
- **CombatMetric** - Who is on the station? How injured are our friends? Writes to "Hostiles", "Friendlies", "Death" and "Medical"
- **DoorMetric** - Uses doors as a proxy to surveying the ship for danger. Writes to "Security", "Atmos" and "Power"
- **FoodMetric** - How hungry are the friendly crew? Writes to "Hunger" and "Thirst"
- **PuddleMetric** - How messy is the station (partially as a proxy for safety). Writes to "Mess"

I expect that as we describe a situation we want the Director to react to we will introduce further metrics to give us 
richer insight into the station. We might want trust metrics based on how many traitors there are. Or staff / department 
metrics based on staffing issues and role deaths.

## Events - Have a predicted effect on chaos

How do we describe what an event does?

Events have a metric called "Chaos" which describes different types of negative effects they bring to the station. 
Good events cause negative chaos. 

If our chaos estimates for each event are accurate, the game director can easily control chaos by picking the best events
for the current story beat.

### Negative events increase chaos
SpiderSpawn:
 - Hostiles: 40           - New hostiles are introduced
 - Friends: 20            - Friends are likely to die
 - Medical: 150           - Medical will have wounds to heal

### Positive events reduce chaos
PizzaPartySmall:
 - Hunger: -80             - The pizza party satisfies hunger
 - Thirst: -40             - And also thirst

## Game Director - Pick best Event to achieve story Metrics

Each of the **story beats** from above has a matching chaos level, specifying factors that we care about at that point 
in the story along with target values for those **Chaos factors**.

Once we know what **Chaos metrics** we currently attempting to achieve, we have a chance to select the correct event.

- The **Story Beat** has told us what chaos we want. 
- The **Metrics** tell us what chaos the station currently has. 
- Each **StationEvent** has a Chaos field predicting that event's impact

So we iterate through all the possible events, choose the one which moves the station chaos nearest to our goal and set 
that event into action. Simple! 

The whole process is richly logged into the admin log (under GameDirector) so the admins have insight into what the director
is attempting to achieve.

# Conclusion

The Game Director system will allow us to author specific experiences that are gated on how chaotic the station has become. 

The more events we introduce to the game with clear chaos outcomes, the better the system will be at guiding the station 
through a specific narrative experience.

The data driven nature of the metrics and story data means that a wide variety of narrative outcomes and station-specific
events can all be achieved through the same system.