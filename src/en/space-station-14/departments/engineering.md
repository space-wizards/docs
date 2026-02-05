# Engineering
Assembling, maintaining, and powering a station soon to undergo rapid unscheduled disassembly.

## Concept
Engineering is the department responsible for assembling, maintaining, and powering the station and its equipment, keeping it functional and usable by the crew.
In addition, Engineering may embark on large construction projects, either transforming an area or deploying a new system.

It is extremely fun and rewarding for players to solve a mechanical issue or build something new for other players.
As such, Engineering and its mechanics should promote collaboration, cathartic solutions, and above all, the feeling that the player's actions are making a difference.

## Design Pillars

### Cogs in a Machine
Engineering mechanics should promote teamwork, where dividing multiple people up into performing individual tasks results in a speedy resolution to a large problem.

This gives the player the feeling of contributing towards a wider goal, or "keeping a machine alive."
This feels fantastic and provides engaging roleplay and interaction.
Players can divide themselves up among tasks, coordinate responses, allocate more people to matters more urgent, and so on.

As such, mechanics should be designed in a way that fulfills the following requirements:
1. **Large tasks can be parallelized.**
   - Multiple people should be able to work on a large task without one person conflicting with another person's work.
     - A good example: Setting up solars does not require people to wait on other people for tasks to be done—the work can be completed asynchronously and by any number of people.
     - A mixed, mostly good example: Engine construction. While the work is parallelizable, multiple people may have different ideas as to what engine design should be used. In addition, many engineers prefer to wait until the engine generator is in place and containment online before the PA is fully assembled.
       - While these concerns may not be able to be 100% alleviated, communication issues like engine design can be helped by giving the CE tools to help lead their team. For example, an engine projector that projects holograms of engine parts to be moved.
   - If a task requires that a certain phase of work being completed, that subtask should be parallelizable.
     - A good example: Hull breach repair. Atmospherics cannot restore air pressure without the hull being airtight, so that is a blocker. But multiple people can work on patching the hull, working from multiple directions inwards.
2. **Mechanics and tasks should be intuitive and easy to see how they fit into a larger picture.**
   - Players should be able to identify subsystems in a larger system and be able to understand what that system does and how it contributes to a larger system. Using an analogy, players should be able to identify a cog in a machine and see how that cog turning keeps the entire system moving.
     - A good example: SMESes in the context of the station power distribution network. They may be given a fancy name (Superconducting Magnetic Energy Storage); however, in the grand scheme of things, players can understand that it is just a big battery that supplies backup power to the station.
     - A bad example: SMESes and generators in the context of power ramping. Power is not delivered instantaneously in some devices, rather the output of the device slowly ramps up to match demand. As a result, power may not be supplied as quickly as consumers demand it, resulting in a deficit and brownout until the suppliers ramp up enough to satisfy demand. This is currently not communicated intuitively.
   - Mechanics or systems should intuitively communicate their role in a greater system, whether that be through their outer appearance, connection to real life, or through their UI or interactions.
     - Ex. It is **visually intuitive** that an air vent releases air into an atmosphere, or that an SMES stores power.
     - Ex. It is **interactively intuitive** through UI that a generator has greater fuel efficiency at power outputs lower than their maximum output.

### Toolset and Accelerated Work
The items in Engineering's restricted-level toolset should speed up their work, enabling productivity and response time higher than if a person wants to achieve a maintenance task on their own accord.

In a sense, everyone should be able to do work involving Engineering in a pinch, but performing work in a timely manner involves calling Engineering to help out.
This allows players to still perform their duties if Engineering is in a skeleton-crew state, but they are still encouraged to call on Engineering if available for large tasks.

### Proactive, Reactive, and Menial Tasks
#### Proactive Tasks
Proactive tasks are tasks that Engineering does on their own accord, whether that be fulfilling requests from departments or by constructing something in their pass-time.

The bulk of proactive tasks are projects.
These projects can be anything, from deploying and maintaining a station point defense grid, to renovating or installing a new section of a department.
These tasks should be able to be completed in a standard shift and benefit the station across the board, not just Engineering.

It's important that these tasks do not outshine repair work and station maintenance items. Repair work should be the most engaging and fun, in order to encourage players to perform repair work instead of huddling up in a department focusing on something that only benefits them. In a sense, proactive tasks should be something that is mostly done during engineering downtime.

#### Reactive Tasks
Reactive tasks are tasks that occur in response to some station event.
For example, science exploded their artifact chamber, meteors spaced an area of maints, or a hardbomb blew up medical.

These are the most important tasks that affect the round, as not completing them exacerbates the feeling of station damage.
If damage can be caused too easily, and the damage is not fixed fast enough, Engineering will feel underwater fairly early in the round, which is not a fun experience for players.

Since this gameplay is the most important, it should be the most engaging and fun to fix.
Reactive tasks should not be seen as a distraction from proactive tasks, as this can lead to Engineering ignoring issues that the crew cannot solve on their own accord, leading to a feeling of helplessness and evacuation.

#### Menial Tasks
Tasks given to Engineering should not be extremely menial or feel like a filler task meant to keep engineering barely idle.
These tasks are boring and do not contribute to fun gameplay.
Generally speaking, menial tasks should be converted over to feeling like reactive tasks, where station and player events cause these task items to appear.

For example, presume that we make a task where engineering has to replace fuses on a substation frequently. The fuses blow out randomly and cannot be blown out via regular player interaction.
If these fuses aren't replaced, the substation will be disabled. This has the following effects:
- If this task is not completed for some reason, a large portion of the population's round is now negatively impacted, and this impaction is outside their control, which reduces agency.
- This menial work distracts away from potentially interesting work that Engineering could be doing, such as construction, renovation, or other interesting mechanics. In addition, this menial work could be so boring that Engineers may frequently forget to perform the work in exchange for doing work that actually interests them.

Instead, your mechanic should be designed around upsets driven by in-round events that can happen either by chance or by antagonistic activity.
Players should be able to tell when these upsets occur if their effects on the round are large. These upsets should do damage to the station proportional to the time or amount of resources it takes to perform the upset. These mechanics should also tie into other mechanics as much as possible to make it feel like it's part of a greater system.

Take the substation fuse mechanic for example. The mechanic can have the following elements:
- The fuse does not burn out on its own, rather it is just like any other fuse that burns out if too much power is flowing through the substation over a period of time.
- Random events or crew-generated interactions can induce high power draws, causing fuses to blow. For example, maybe science triggers an artifact that overloads some machines on the LV net and blows the substation fuse. Maybe Cargo tried to hook up their third industrial ore processor without upgrading the line, and now the breaker popped.
- The substation fuse doesn't have to be a fuse - it can easily be replaced with something devious and cursed like a sheet of steel, glass, plastic, or soda can. The type of item inserted can cause a number of different effects, but it'll probably result in the substation either sparking like hell and melting or exploding.

### Difficulty Population Scaling
The difficulty of tasks should scale with the population of the Engineering department, or the number of people that is expected to be doing that task.

The intention of this design pillar is to prevent situations where a skeleton crew (likely) cannot achieve the tasks necessary for the station's beginning-of-round survival.
For example, stations designed to host a skeleton crew (or stations that may see a skeleton crew engineering department) should have engines that can be operated by a skeleton crew.

It's important to note that it's okay to have tasks out-scale the player in the end-stages of a round where chaos and disrepair are supposed to be happening. However, this should not be happening at the beginning of the round, or as a first introduction to a system.

For example:
- Setting up the AME is a task that can be achieved in a reasonable timeframe by one person.
- Setting up the Singularity or Tesla engine can be achieved solo, but this takes a bit of time as setup is a complex series of steps, compared to other engines. Multiple people should be able to set up the engine in a reasonable timeframe. This makes the Singularity/Tesla less attractive for lower-population stations, and an alternative generator should be afforded, or the setup of these generators be partially or fully completed.
- Setting up the TEG can sometimes be a difficult task for one or multiple people, especially people being introduced to many mechanics like Atmospherics and its limiting factors like window shattering. Mechanics like these should be communicated visually or intuitively as mentioned before.

### Station Infrastructure and Sabotage
Large and/or critical station infrastructure mechanics should be designed in a way that makes sabotage difficult to perform unless significant resources and/or time are dedicated to performing it.
For other station infrastructure, the level of disruption should match the time, effort, or resources put into the sabotage. For example:
- Disrupting the power in a single room shouldn't be too hard—anyone can cut the wire or disrupt the APC if they have access to it.
- Disrupting the power in an area serviced by a substation should be harder. The substation can be access locked, be in a space where you can be caught, and disconnecting the substation could set off a series of low power alarms.
- Disrupting the power on a station-wide level should be challenging unless done at the source or the circuit is open.

Very frequently, the actions of one singular person doom the entire round, whether by intentional malice or simple accident.
This is unfun for all players, as people may lose out on their antagonist or job roll, and nobody wants to sit through the ~25 minutes that it takes to restart the round.
This is a large pain point that can be solved through mechanical design.

## Progression
### Roundstart
Engineering starts the station off in a state of calm before the storm. Their first task is to suit up and prep all the systems available to them and ensure they are operational.
The only major station system available to all engineering personnel is power.

Power is the most important system to set up, as a station without power effectively pauses gameplay for the entire station. In time-sensitive events like nuclear operatives declaring war, this can easily result in a loss outside the crew's control.
A lack of power also exacerbates issues like atmospheric upsets, as many devices that stop spacing and maintain an atmosphere stop functioning during a power outage.

Considering that Power is the most important system to set up, it should be the most intuitive system to set up.
The time that Engineering gets to set up power should allow someone to mentor and teach people how to set up power.

Further guidelines as to what power (and other systems should be like roundstart) should be explained in their respective design documents.

### Mid-Round
As the round progresses, Engineering can engage in various tasks that are either created on their own accord or pop up due to random events (proactive or reactive tasks).
Maybe a small group of engineers dedicates themselves to working on a point-defense array, and maybe another group responds to a spacing incident triggered by a passenger.

In any case, this is where Engineering starts to pick up the pace, responding to issues more pressing than the simple emagged door.

### Late-Round
As the round progresses, Engineering may find that their workload is starting to overwhelm them, with chaos ramping up and destruction widespread. Maybe syndicate traitors have knocked out important substations, or the engine is being forced into an unstable position. 

At this rate, players will start to notice that Engineering simply cannot keep up, and evacuation will be called.
Just like what is outlined in the Atmospherics design document, it is important that this feeling of being underwater or overwhelmed with work does not come too early.
Otherwise, players may feel like their efforts are not making a difference.

