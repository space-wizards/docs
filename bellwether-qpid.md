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
### QPID Infrastructure Requirements
Specialized equipment, both extant and non-extant in the game at present, denoted in _italics_. Non-extant equipment is additionally ***bolded***. 

+ Needs to be on an HV wire 
+ A _Particle Accelerator_
	+ The PA needs to be equipped with a ***Phase Shift Lens*** array placed in front of the PA; this is a machine construction that results in a 1x3 "bar" in front of the PA. The PSL aligns particles passing through it to a desired quantum waveform. 
+ A ***PSL Control Computer***. This is a normal computer loaded with a PSL Control Computer Board. It must be paired with a constructed PSL using a multitool or similar networking device. This is used to alter the quantum waveform of particles produced by the PA. 
+ A ***Quantum Resonance Monitoring Computer***. This monitors sources of quantum resonance on board the station, including the QPID itself, presented a map similar to the Power Monitoring Computer with a list on the side and a small window displaying a waveform, either of the the station's overall quantum resonance or a selected source's alone. Most instances of quantum resonance are single events are sudden bursts, positive or negative, in the overall quantum resonance of the station, which is dominated by the QPID's steady output of a sinusoidal wave. These bursts may be small and transient, but they still affect the stability of the QPID. The information provided by this computer is critical to properly aligning the PSL, but it also serves to locate and to some degree identify other sources of quantum resonance on board the station that are affecting the QPID. This includes, but is not exclusive to, anomaly pulses, games of chance, etc (see below, "Other Sources of Quantum Resonance"). The QRMC does not need to be linked to any devices to function and so can be constructed anywhere that is convenient, and can even be constructed in the absence of a QPID (though it has very little function without one). 
## Operating the QPID 
The QPID generates a baseline amount of power, which increases with instability - the less stable the QPID, the more power can be drawn from it. However, with increased instability of the QPID comes a greater chance that midround events will occur, much like how the frequency of events scales in Survival mode. At extreme instability, the QPID is effectively adding late-stage Survival mode to whatever other game mode the station is operating in. Suggested terms for QPID energy states might be Stable, Metastable, Unstable, and potentially Critically Unstable and even Runaway, if more granularity in system states is desired. _The QPID cannot enter a failure state of its own accord; it will continue to operate unless stopped._

Since the QPID generates less baseline power than either the Singularity or the Tesla, some degree of instability is likely desired. A canny CE with a dedicated team can even tune the QPID's stability to match increases and dropoffs in the station's power consumption needs. 
### Superposition
The QPID has a Superposition trait. This is effectively the QPID's health; once deployed, direct observation of the QPID causes its Superposition to degrade (for quality of life purposes, Superposition degrades far slower before the QPID is activated, so it's not a horrible rush to get it set up). Once the QPID is activated by a PA, however, it cannot be observed without rapid Superposition decay, so shutters and other forms of visual blocking are necessary. The upside is that the QPID is not a direct physical threat, and so does not require the usual containment setup that Singularity or Telsa does. If Superposition decays entirely, the QPID fails, turn off, and cannot be reactivated. The station will need to secure a new one if they want to continued to run on a QPID.

In an emergency, if the QPID's instability has become impossible to manage for whatever reason, the QPID has a very simple failsafe shutoff mode: walk up to the QPID and open it. When the QPID is opened, its Superposition drops immediately to zero, and the interior of the QPID spawns either a living Space Cat or a dead normal cat (50% chance of each). 
### Controlling the QPID
The QPID's instability is measured as divergence from a balanced median; the higher that instability, the more power the QPID generates, and the more random events occur. This instability will naturally fluctuate over time, tending to grow, resulting in larger waves in the sinusoidal display visible on the QRMC. The PSL can be used, in conjunction with the PA, to generate a matching waveform, which can be projected either in- or out-of-phase with the QPID's; this will amplify or interfere with the QPID's waveform, thereby increasing or decreasing instability, respectively. 

Since the PSL is controlled by a separate computer, this encourages teamwork in management of the QPID. It is possible for a single engineer to maintain the system, but it'll always be easier with a helping hand. 

The Chief Engineer now has a Quantum Probability Assessment Device, or Q-PAD, which when paired with a QPID will track its quantum resonance and stability, as well as identifying the current "focus" of the QPID: this is the only device that can do so. Events of the type listed as the focus (for example, dice rolling) will _decrease_ instability; all others will _increase_ instability. However, every time the QPID changes stability states (from Metastable to Unstable, for example), the QPID will change its focus. 

The Q-PAD is also a new potential antagonist theft objective, and while it cannot directly influence the QPID, it could allow an antagonist to steer the QPID in an undesirable direction for the station. 
### Other Sources of Quantum Resonance
The PA isn't the only thing affecting the QPID. Stability is affected by choices and decision points across local space; in game terms, this includes any roll of dice, antagonist greentexting (or degreentexting, if, for example, someone killed is revived), whether a station pet allows a player to pet them or not, anomaly pulses, etc. Any discrete, trackable event or in-game state is fair game for this system, though it's likely the final version will only care about a particular selection in order to limit complexity and performance issues. 

_All tracked decision points/events on the station grid affect the QPID. It is functionally impossible to maintain perfect equilibrium long-term._
## Development Considerations 
I (Bellwether) am an extreme novice when it comes to coding; all my game design experience is in analog (i.e., Tabletop/Traditional) gaming. Collaboration on the code end from a more experienced developer or developers will be necessary for this project to get off the ground at all. 

In terms of resources, this proposal will require a few new sprites (the QPID in various states, the Q-PAD, etc), as well as several new interfaces. It's also reliant on the power systems rework for the Singularity and the Tesla being completed, since the QPID would probably suffer from the same problems those engines have in terms of power spikes and flickering. 
