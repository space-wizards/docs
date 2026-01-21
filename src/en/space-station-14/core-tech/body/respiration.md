# Respiration

## Design

## Engineering

### Components

#### LungsComponent

A server-side organ component that covers managing the solution of Air that the organ will contain, and tags an organ as being lungs.

#### RespiratorComponent

This does the actual "lungs" activity for a given mob. As a reminder, LungsComponent is a component that controls the solution of Air that a set of lungs currently contains. This is a server-side component that actually breathes. Like BloodstreamComponent, this is actually a mob component - most mobs respire.

The Respirator works by tracking the "Saturation" of the Respirator - this reflects how ogygenated/nitrated/etc the Respitaror mob is as a whole. Insufficient Saturation causes suffocation, which if not resolved quickly causes damage. When suffocating ceases, the Respirator will slowly heal the damage inflicted. 

Respirator also controls what emote plays when someone gasps for air, and if someone is currently breathing in or out.

### Systems

#### LungSystem 

Lungs covers a small selection of lung-related behaviours, including some atmos behaviours that control how internals work.

Due to the way that the overarching systems have been coded, LungSystem's job outside of some token internals orchestration is directly driven from RespiratorSystem (see below).

#### RespiratorSystem

This is a server-side system with a low tickrate that covers how mobs respire - i.e. breathe in and out.

Similar to other Body systems this runs off a metabolism tick rate. This tickrate determines the opportunities for a mob to breathe in and out - each attempt is either one or the other, and it switches each time.

When breathing in, some atmosphere is transferred from the air to the lungs, or from the lungs to the air when exhaling. Air that enters the lungs is then converted into the Solution the lungs store. The Respirator is directly tied into using Lungs to actually store the Air it breathes in - it can use multiple pairs of lungs, and the conversion of atmosphere to Solution is done by the Lungs on behalf of the Respirator.

Failing to breathe in causes a loss of Saturation. When the Respitator's Saturation drops below a critical level, the Respirator start suffocating, dumping airloss damage into the mob.

Likewise, regaining Saturation stops suffocation and begins to restore damage.

Suffocating is not immediate - it takes two failures to breathe before suffocation causes damage. 

Damage inflicted by this system is typed as airloss.

## YAML

