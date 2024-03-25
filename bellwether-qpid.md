# QPID Power Reactor

| Designers  | Implemented | GitHub Links |
| ---------- | ----------- | ------------ |
| Bellwether | :x:         | TBD          |
## Overview
The Quantum Probability Induction Drive (QPID for short) is power system similar to the Singularity or Tesla Engines, but without the possibility of a single failure point resulting in total station destruction. Instead the QPID is a risk/reward system, where tolerating a certain degree of instability results in generating a larger amount of power, but also greatly increases the chance that a mid-round event occurs. 
## Background
When the Singularity looses, the round is probably over. 
When the Tesla looses, the round is _definitely_ over. 

While there are some attempts to control potential looses in the game, such as the particle decelerator, these are rarely available and consequently don't often save the station from a reactor gone wrong.  In addition, apart from a few basic maintenance tasks, the Singularity and Tesla are not very interactive for Engineering, since all they have to do with those systems is either refuel the radiation collectors or repair/replace lightning rods occasionally. 

The QPID offers a different gameplay mode for engineers, one that requires more interaction (and potentially weird or fun behaviors) to maintain a certain desired degree of controlled instability. This will give Engineers something to actually do instead of wait for problems with the power system to cause the station to explode.
## Setting up the QPID
The QPID begins as a small, flatpacked box stored in Engineering (or, potentially, ordered via secure crate from Cargo). Setup is easy - you take it out to the Singulo/Tesla array, place it in the middle, deploy it with a multitool, and leave. Once deployed, the QPID becomes a large box, similar to an artifact crate but visually distinct. The QPID is activated with a particle accelerator, and from that point is considered to be "On." 

The QPID has a Superposition trait. Once deployed, direct observation of the QPID causes its Superposition to degrade (for quality of life purposes, Superposition degrades far slower before the QPID is activated, so it's not a horrible rush to get it set up). Once the QPID is On, however, it cannot be observed without rapid Superposition decay, so shutters and other forms of visual blocking are necessary. The upside is that the QPID is not a direct physical threat, and so does not require the usual containment setup that Singularity or Telsa does. If Superposition decays entirely, the QPID fails, turns Off, and cannot be reactivated. In an emergency, the QPID has a very simple failsafe shutoff mode: walk up to the QPID and open it. When the QPID is opened, its Superposition drops immediately to zero, and the interior of the QPID spawns either a living Space Cat or a dead normal cat (50% chance of each). 

## Operating the QPID 
The QPID generates a baseline amount of power, which increases with instability - the less stable the QPID, the more power can be drawn from it. However, with increased instability of the QPID comes a greater chance that midround events will occur, much like how the frequency of events scales over time in Survival mode. At extreme instability, the QPID is effectively adding late-stage Survival mode to whatever other game mode the station is operating in. Suggested terms for QPID energy states might be Stable, Metastable, Unstable, and potentially Critically Unstable and even Runaway, if more granularity in system states is desired. _The QPID cannot enter a failure state of its own accord; it will continue to operate unless stopped._

Since the QPID generates less baseline power than either the Singularity or the Tesla, some degree of instability is likely desired. A canny CE with a dedicated team can even tune the QPID's stability to match increases and dropoffs in the station's power consumption needs. 

Stability is affected by choices and decision points; in game terms, this includes any roll of dice, antagonist greentexting (or degreentexting, if, for example, someone killed is revived), whether a station pet allows a player to pet them or not, etc. Any discrete, trackable event or in-game state is fair game for this system, though it's likely the final version will only care about a particular selection in order to limit complexity and performance issues. 

Engineers can monitor the QPID with a specialized Quantum Probability Assessment Device, or Q-PAD, which when paired with a QPID will track its stability and identify the current "focus" of the QPID: mechanically, this is similar to alien artifacts in Science that want a particular input to activate a node. Events of the type listed as the focus (for example, dice) will _decrease_ instability; all others will _increase_ instability. However, once stability reaches perfect equilibrium (i.e., instability reaches zero), the QPID will change its focus. 

_All tracked decision points on the station grid affect the QPID. It is functionally impossible to maintain perfect equilibrium long-term._

The Q-PAD is also a new potential antagonist theft objective, and while it cannot directly influence the QPID, it could allow an antagonist to steer the QPID in an undesirable direction for the station. 

## Development Considerations 
I (Bellwether) am an extreme novice when it comes to coding; all my game design experience is in analog (i.e., Tabletop/Traditional) gaming. Collaboration on the code end from a more experienced developer or developers will be necessary for this project to get off the ground at all. 

In terms of resources, this proposal will require a few new sprites (the QPID in various states, the Q-PAD, etc), as well as an interface for the Q-PAD. It's also reliant on the power systems rework for the Singularity and the Tesla being completed, since the QPID would probably suffer from the same problems those engines have in terms of power spikes and flickering. 
