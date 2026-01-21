# Metabolism

Covers the joys of eating and drinking, and - more importantly - doing things with solutions that affect each spessman's health and well-being.

## Design

## Engineering

### Components

#### MetabolizerComponent

This server-side organ component marks an organ as being a metabolizer - it causes an effect on the mob via consuming a certain amount of chemicals from a solution - usually the chemstream of the mob.

Like the BloodStreamComponent, it has a metabolism tick-rate.

A Metabolizer can be marked as deleting chemicals that otherwise don't do anything when metabolized - this is usually on the kidneys organ - and otherwise processes metabolizable chemicals (up to a certain amount) each tick based on its list of metabolism groups it supports. Examples of these groups include "medicine", "poison" and "food".

#### BloodstreamComponent

This is a server-side component that defines that a mob has a bloodstream. Despite being a Body component, this is actually for any mob that has blood, including decidedly non-humanoid mobs like space dragons. 

This component essentially covers three things:

1. The metabolism rate of the bloodstream - i.e. how many seconds between bloodstream ticks occur.
2. How bleeding works for the creature - how much they bleed, how much blood can they lose before taking bloodloss damage, how much blood they regain if they're not bleeding, and so on.
3. How the "bloodstream" and "chemstream" internal Solutions this Bloodstream works with work. This includes how much volume each stream has, what the names of the two solutions are, and what the name of the temporary solution that blood goes into before it pools into a puddle. 

The difference between "bloodstream" and "chemstream" is a common cause of confusion. The "bloodstream" exists as the blood of the mob - losing too much blood causes damage, blood is replenished over time. The "chemstream" is the actual flow of chemicals through the body; blood does not actually convey medicine to the heart to be processed.

#### MetabolismGroupEntry

This defines a particular metabolism group that the metabolizer handles - and it can handle them better or worse than usual too. 

### Systems

#### BloodstreamSystem

This is a server EntitySystem and covers how bloodstreams, chemstreams, bloodloss, bleeding, replenishing blood and regaining bloodloss damage all work. 

Bloodstreams operate on a low tickrate. Each tick, the amount of blood in the bloodstream is assessed. If there's some blood missing, a small amount is regenerated in (meaning that the Bloodstream stands in for a spleen organ). If there is not enoug blood in the bloodstream (for example because of the bleeding status effect), the mob the Bloodstream is on will be damaged. In addition, the mob suffers drunkenness effects and stuttering. 

When a mob's bleeding, this update loop also slows the bleeding and applies the removal of blood.

Bleeding itself is generally caused as an EntityEffect.

Blood that leaves the body due to bleeding pools into a temporary solution on the Bloodstream. This temporary solution only can contain a small amount of chemicals before overflowing - when it does, the solution is converted into a blood puddle, and a small amount of the contents of the Bloodstream's chemstream are also leaked into the puddle.

Bloodstreams, when the mob they are attached to gets damaged, may cause extra damage to the mob. Losing blood on damage is possible - e.g. a slashing attack from a sword - and bloodloss can cause immediate extra damage, and can sometimes "critical hit", causing extra blood to be lost. 

Bloodstreams also can cauterize wounds - it's how a tider can stop bleeding by touching a lightbulb.

The Bloodstream is responsible for dumping out the contents of the bloodstream and chemstream when a mob gets gibbed.

Otherwise, the Bloodstream behaviours are typical - adding and removing blood and chemicals from the bloodstream and chemstream, modifying the amount of bleeding, outright changing the blood reagent associated with a mob (for example, from normal blood to zombie blood), and setting up blood DNA.

Damage inflicted by this system is typed as bloodloss.

#### MetabolizerSystem

This is a server-side system that does one principle behaviour - attempt to metabolize chemicals from a Solution into an effect. Like similar systems this happens on a low tickrate, usually once every few seconds.

Metabolizing chemicals works by first stripping out unmetabolizable chemicals in the Solution (if the metabolizer can do that) and then iterating over every chemical in the Solution, up to the maximum the Metabolizer is able to metabolize in that tick. If the mob is alive, the chemical' effects are applied. These effects are ReagentEffectEntries that are defined on the reagent chemical itself.

Even if the mob is dead, some of the chemical will be removed. The amount removed is dependent on the reagent's ReagentEffectEntry metabolism rate and the metabolism rate modifier that chemical's metabolism group has on the Metabolizer (usually just a x1 multiplier).

## YAML