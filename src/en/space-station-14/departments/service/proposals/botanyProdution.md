# Botany Overproduction Fix Design

| Designers | Implemented | GitHub Links |
|---|---|---|
| Cerol | No | TBD |

## Overview

I have a big writeup on Botany and Hydroponics and expanding them is frequently met with discussions relating not to the game or changes, but the engine and side-effects of botanists making lots of produce. This is intended to be the conversation that ends that pattern by doing something about it, at least to the point where it's an acceptable headache instead of a persistent roadblock.

## Background
In the case where a player has optimized plants for output, they can drop a HUGE amount of entities in a round. If you have a perfectly min-maxed plant using only swabs and starting seeds, you can get 168 produce out of 28 harvests in 22 minutes from one tree. Filling the trays with seeds or clippings of that can hypothetically let you approach 4,000 produce in 30 minutes in a standard 16-tray Hydro room. Defensive for botanical nonsense as I am, even I can say that's too much. In the event you don't min-max quite that hard, numbers can still be pretty high. 2,000 produce in 30 minutes is entirely doable with cocoa or cherry trees alone.

Entity spam is eventually an issue, but bigger problems are hit by glowing plants. The lighting engine gets weird when there are hundreds or thousands of lights on screen at once, and reported issues vary from "screen goes permanently black" to "FoV disabled entirely" to "shadows dont look right until you walk away". I don't want to remove stuff because of engine limits, but I do know that some problems don't show up for everyone and are hard to reproduce live, and may vary in addition with settings and hardware performance levels.

I maintain that the best way to address the issue(s) is to give botanists more demands from the rest of the station to juggle, and more potential goals to pursue. I also acknowledge that doesn't mean players wouldn't choose to max production to a problematic degree anyways, and there should still be some sort of mechanical way to minimize the impact of that. It's time to fix the issue.

## Details

There are 2 plans to resolve the overproduction issue that I think are solid and worth implementing. I will also go over a bunch of ideas that are possible but I don't think are worth implementing, for discussion purposes and feedback.

We should do:
* SlowGrow: Slow down repeatable-harvest plants, reducing their lifetime yields.
* YieldCap: potentially problematic effect mutations enforce their own stat caps.

Other potential ideas I'd pass on:
* MutLock: Effect mutations block further plant changes
* BalanceDrop: Make Yield values lower across the board.
* PersistNot: Effect mutations become one-offs and can't be transferred between plants or seeds.
* GlowCode: A new system tracks the specific offenders everyone hates
* SpaceAnts: Produce rot after a certain amount of time on the floor.

## SlowGrow

Every time a repeatable harvest plant is harvested, another tick (15 seconds) is added to the time required for the next harvest(so after the 4th harvest, you're waiting another minute on top the plants normal wait time for the 5th). For the same min-maxed plant above, this reduces harvest count from 28 to 8, and total produce from 168 to 48. That's 30% of the original total, and puts the 30-minute spam number closer to 1,000.... which is still a lot, but a huge improvement.

For most normal plants, this cuts down on the number of total harvests by ~2. This isn't a big impact and shouldn't feel noticeably worse for standard chef supplying duty. This is also a very 'organic' change, in that it doesn't really impact baseline play and you won't feel it without close scrutiny. In a future state where specific stats and mutations can be moved without relying on chance and it is much easier to min-max a plant, this may be a fairly important change even if it's not one picked to do today.

* PRO: straightforward implementation, significantly improves the worse case scenarios, low-level botany play largely unaffected
* CON: still allows possibly-too-big numbers of produce production
* OPINION: This is my favorite idea on the list. It lets a botanist do stuff, and the quantities involved should still FEEL like you're making a ton of stuff even if those numbers are cut down from current state. It also limits bad actors ability to jump DUMP LIGHTS onto the engine, but it doesn't remove the possibility entirely. It's a solid plan, but it may not be enough to end the conversation on its own.

## YieldCap
We could allow mutation effects to set their own cap on stat values. In this case, no matter what you rolled Bioluminescent on, it would get its Yield/Production clamped to a specific value (EX: Yield at max 2 or 3, Production to min 5). This cuts back on using high-yield/fast-reharvest plants as the base for mutations since they no longer offer any benefit, and it does not matter which order mutations get rolled in.

This puts a solid cap on how quickly effects can be dropped in-game depending on the number of PlantHolders available. Using the example values (Yield 3, Production 5), that's 12 glowy fruits every 5 minutes per plant tray. In a normal Hydro room with the same min-maxed setup as above, it's a similar 1100 produce per 30 minutes. 

With SlowGrow and YieldCap, that minmaxed setup would be 9 harvests of 3 fruit, cutting the number almost in half again to 27. A full-room blitz to mass produce lights would get under 500 made in half an hour, 1/8th of the hypothetical starting number, which is about as low as that number is going to get. This is why my primary suggestion is to do these 2 plans.

* PRO: Simple and direct fix, only applies to mutations that cause significant issues, different mutations can set different limits and the harshest one can apply.
* CON: relevant EntityEffects now need to check if they're applied to a plant and do more work instead of being generic. tracking limits on multiple variables may get slightly messy, is immediately noticeable when a plants output changes quickly.
* OPINION: This is probably a good idea, and it covers the cases that SlowGrow doesn't.  Put together, the two plans should largely keep botany's output to acceptable levels.

## MutLock
Now that mutations are effects, its easier to expand out checks related to them. One option we can do is that once an effect mutation happens, it blocks all future mutations. This would mean that you can have produce with Bioluminescent or Slippery, but not both. This also means you can't mutate a room full of plants until one of them starts glowing, and THEN crank up the glowing plant to min-max output, you'll have to work with what you have.

This would involve using (and checking for) the Immutable flag on seeds, which is present but not used before. This also leaves open the case where you make a min-maxed yield plant, and then get lucky with a glowing mutation. You could still have players dropping a ton of glowing produce, but they'd have to go for yield first and then luck into getting glowly stuff without hurting their ideal numbers on future mutation rolls.

* PRO: Botanists that want to keep multiple effects now have to work harder to do so, can't make a glowy plant better than it was 
* CON: still permits engine-abusing setups with some preparation and luck, doesn't address raw entity count
* OPINION: This isn't a whole solution on it's own, but I don't think its a terrible idea either. At the moment, I think it would be OK to stop players from having a single plant with all available effects on it, but there may be a case where that isn't true (such as a particular mutation taking precedence over others). As is, the main thing to go for a "full collection on one plant" goal is chemicals, and those aren't affected by this idea. Maybe this is a lower priority and gets done later, if its really necessary.

## BalanceDrop

Open up seeds.yml, search for yield, and make all the numbers lower. For extra credit, numbers for Production could be increased. This means there would be fewer crops and more time between harvests. The odds of each mutation can also be set separately now, and problem ones made rarer if desired.

* PRO: Extremely simple, only requires YML changes.
* CON: Doesn't address mechanics of the issues, blatant nerf will be noticed immediately, stat mutations can still pump numbers up.
* OPINION: I'd prefer any 'balance pass' on seed numbers to be more holistic and look at everything involved with seed values and gameplay. I have opinions on all of that but that's a future discussion and needs a little more in-game evaluation to make sure I'm being reasonable.

## PersistNot

We could just make mutations not be 'genetic'. Instead of being carried on from plant to seed, they just apply their effect once and you can't have it be applied to 15 other plants from a single original lucky roll. If you want more than one plant to make glowing fruit, you'll have to roll Bioluminescent multiple times on multiple plants.

This means that mutations aren't presented as genetic, and that may break immersion somewhat for players when only SOME things get carried from parent-plant to child-plant. Instead, you'll be putting in an average of 30ish units of mutagen per plant to get a few glowy fruit out of them, and dealing with several other random mutations to that plant in the process. This gets away from the core game design pillars by removing reasons for people to ask Botanists for stuff and ways Botanists can engage with more systems than 'plant seed, give chef ingredients'.

* PRO: problematic mutations must be acquired separately multiple times, dramatically limiting how often they can show up.
* CON: is distinctly a meta-gamey answer, violates the premise that genetics are being manipulated if they can't be transferred, minimizes what little potential crossover interaction botany has now,
* OPINION: I do not like this idea, but I do want to present it as an extreme option. This takes a fair amount of fun out of the luck of getting an effect mutation, and breaks the feeling that Botany is a system that can interact with stuff and be explored when you hit a wall that says you can't in these circumstances. Players will quickly get bored of botany when mutations are exclusively one-off events that rely on luck and the resources to make the rolls for each individual plant. I would rather see an alternative system for botany be proposed over implementing this.

## GlowCode
If the only real issue is how many point lights botany makes, then just track that in a dedicated system. Have the mutation effect check with a new system that tracks some kind of GlowingProduceComponent, and reject creating new one if there are already more entities with that component than whatever the cap is. We'd also have to pick a cap, and I feel like putting it somewhere in the low triple-digits would be the right answer but I have no research to back that up right now.

* PRO: addresses worst issue very specifically
* CON: is a decent amount of extra code for one very specific issue, doesn't handle raw entity count spam
* OPINION: I would prefer to not have to do this, mostly because I fear it would set the precedent to do this for every effect at some point. I would rather the core issue of entity count be handled and let the light count be solved automatically with it.

## SpaceAnts
A solution from SS13 servers. Produce that sit around unused for too long rots into garbage or gets eaten by space ants. Lets say this gives produce 10 minutes to sit around before being deleted. In our hypothetical min-max setup, that still lets a botanist drop over 1,000 produce before the first one start to disappear. If they leave behind some garbage item, that doesn't fix the entity count issue at all. This also doesn't address the glowy fruit count issue. Finally, this isn't any sort of interactive component at all. Its a garbage collector that shows an animation on an item before deleting it. 

* PRO: Automatic resolution eventually, 
* CON: needs new systems that tracks produce, may not address core issues.
* OPINION: We don't need to copy this system from SS13. The highlight of this plan is being able to say the Archer quote at every botanist or chef that uses open space to hold things, and we can live without that.
