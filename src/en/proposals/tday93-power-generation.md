# A Core Pattern for Power Generation

| Designers | Implemented | GitHub Links |
|---|---|---|
| tday93 | :x: No | TBD |

## Background

Power generation is currently in an odd state. In order to power the station suffciently at round start, engineers need to do one of the following:

1. Collect a number of draggable generators, move them in to place and power them.
2. Rush to cargo before the power goes out to order AME fuel.
3. Rush the power source that can sustain the full round - A Singularity, a Tesla, or the TEG.

In most rounds engineers will choose option number three. If they are relatively new, and take longer than the current
short time window they have on the power the station started, the station is plunged into darkness and they are harassed
on the radio. If they are very experienced, but want to take the time to teach new players to set up the power source,
the station is plunged in to darkness and they are harassed on the radio. The only situation in which engineering is not
harassed on the radio is an experienced engineer quickly setting up the power source in silence.

This is not fun for the experienced engineer, the technical assistant trying to learn, or the other players stuck in
darkness.

This proposal will outline a generic pattern for power generation design which will seek to alleviate these issues, and
simultaneously present engineer players with a wider variety of options for mid-round and end-round play.

## Overview

The proposed pattern for power generation is as follows:

1. Round start power stored in station batteries that without intervention rapidly deplete - on the order of minutes.
2. A stop-gap solution that can be set up and activated within those minutes, which will power the station for the next ten to
   fifteen minutes, but which cannot power the station for the full round.
3. A main power source which can be set up within those ten to fifteen minutes, and which can power the station for the
   rest of the round.


<img src="https://i.imgur.com/YFdOtGC.png"/>


Each phase of power generation scales in both complexity and power output. Stop-gap generation options are simple,
immediate, and weak. Main power generation is complex, takes longer to set up, and supplies a large amount of power.

Additionally, every one of the existing power generation options available today can be made to fit this pattern with
only minor adjustments.

## Round Start Power

Round start power options are characterized by:

1. Actively supplying power to the station at round start.
2. Supplying only enough power to last until Stop-Gap power can be activated.

Currently this means SMESs, and there is little reason to change this phase of power generation at this time.

In the future this could be more exotic power options with extremely limited fuel and diffcult to obtain fuel, or any
number of other possibilities.

## Stop-Gap Power

The core characteristics of stop-gap power generation options are that they are:

1. Clear and easy to set up.
2. Immediately available to set up on round start.
3. Not enough to keep the station powered through the full round.

As it stands the only power generation option which comes close to handling this phase are the portable generators.
However, as it stands maps would need to be tweaked to make it clear that use of the generators for this purpose is
intended, by for instance including an array of them ready to be anchored and fueled within engineering it self.

This is also a role which could be handled by the Antimatter Engine. Spawning a mostly-depleted jar of AME fuel, and
removing the option for cargo to buy additional AME fuel would allow the AME to fulfill this role as-is.

Finally, while solar power is not a good fit for primary power generation in this phase - its perpetual nature removing
and time pressure - it does stand as a useful option to extend the length of the stop-gap power phase - and can be
utilizied if engineering needs more time to set up main power.

## Main Power

Main power generation options as proposed are characterized by the following:

1. They are complex to set up.
2. They take a good deal more time to set up than is available with Round Start power.
3. They can power the station indefinitely, or at least longer than a typical round.

With tweaks to the existing maps, the TEG, the Telsa, and the Singularity could all act as Main Power generation
options. As it stands their setup has been drastically simplified, as they are currently serving as the next phase of
power after round start power runs out - with no clear stop-gap options existing.

With the additon of clear stop-gap options, the setup process for each of these could be made more complex. Each map
could start with the components necessary for one or more of these main power options in storage - and require engineers
to set them up almost from scratch.

The additional time before blackout supplied by the stop-gap power options would allow this complex setup process to be
completed without the station losing power.

Furthermore, the addition of future main power generation options would no longer represent a direct burden on mappers.
Without the need for immediate, rapid setup, ordering these options from cargo becomes a viable option. Maps would only
need space to build these options - not have them mostly set up already.


## Beyond Main Power

The core pattern of power generation outlined at the beginning of this proposal is enough on its own to bring engineering
and power genration to a more consistent and engaging place. This section will outline some ideas for moving beyond that
core, but should be treated as less important than the rest of this proposal.

As it stands engineering is incentivized to produce enough power for the station to sustain itself, and there is little
incentive to go beyond that.

Having methods to turn excess power into other resources or commodities would change this. Some of these options could
even be locked to specific methods of main power generation - adding to the considerations when choosing a main power
generation method. The following are a few examples of what could be possible:

* Allow the AME to be deconstructed and rebuilt along with some of the radiation collectors to capture AME fuel - which
    could be sold by cargo for a significant amount.
* Special rods could be installed beside the Tesla which would sink the power from those arcs, but which would allow
    revival of rotted corpses.
* Science could research a machine which allows for the direct production of base resources - but which has insane power
    requirements.
* An experimental convection oven which must be directly attached to the TEG, sapping some of its power but allowing the
    creation of powerful baked goods.

While secondary to the core proposal, I do believe that looking for incentives to generate more than just enough power
will be valuable to gameplay long term.


