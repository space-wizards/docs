# Malfunctions [Rane, Unapproved]

## Introduction
### Engineering as a reactive department
Engineering is a reactive department, similar to the medbay. A lot of rounds, this works just fine. Our construction system is quite good, there's a decent selection of tools, and so on. However, unlike the medical department, there is a lot less lower priority small issues for engineers to fix. There needs to be problems that can be ignored when the station is on fire, but are disruptive enough to provide reactive gameplay during downtime. We'll call these ***malfunctions***.

### What Malfunctions Are
Malfunctions are problems introduced by wear and tear on a machine. These cause the machine to behave in a different, usually undesirable way different from how the machine is designed. Malfunctions have a variety of proactive ways to prevent them, as well as interesting interactions to remove or bypass the malfunction once it has occured.

### What malfunctions are not
Malfunctions are not just a passive health bar ticking down until the game completely breaks. This is going to be what the barobrains immediately jump to, and there are several key differences here:
1. Malfunctions do not happen completely randomly (outside of random events, I guess.) Machines only accumulate wear towards malfunctions in specific circumstances.
2. Malfunctions change the machine's behavior. They do not totally break the machine.
3. Malfunctions introduce interesting interactions.

## Wear
Wear is another sort of 'damage' for machines that is not structural. In some surface level ways you could compare it to stamina 'damage.' It's not damage in the context we talk about 'damage' in the rest of the game, but an abstract representation of small things going wrong that may lead to a malfunction at some point.

### Receiving Wear
Wear is received during appropriate system events on the machine's entity. Examples include:
- The machine being used for its intended purpose (the smallest source).
- Power issues such as brownouts.
- Actual, physical damage to the machine entity.
- Conditions the machine may not be designed for.
- Abuse of the machine.

Notice how none of these include 'time has passed so add wear for no reason.'

When wear is received, 2 things happen:
1. Add wear to the machine's wear value.
2. Roll against the machine's wear to see if it receives a malfunction.

These both help greatly reduce the annoyance and ensure that the interesting gameplay caused by malfunctions is in an active area of the map.

### Healing wear
Ideally this shouldn't really have to cross engineer's minds, but some will want to be super proactive. Wirebrushes and oil can be used to remove some wear from a machine, and the janitor can get in on the action too if they're so inclined.

### Diagnosing wear
Unlike medicine, there's no roleplay to be had with an inanimate object. Doubly so because malfunctions are not existential threats to the machine in the way health problems are to beings. I don't see an issue with a health analyzer analogue for machines.

## Malfunctions
### Scope of malfunctions
Each machine has a **critical function** that should not malfunction. These are explicitly not breakdowns, so machines should continue performing their most basic tasks. Doors connect rooms, microwaves heat up food, dispensers dispense some sort of reagent, and so on. Details of how they do this or tertiary parts of the machine are what should malfunction.

### Oh no, we rolled a malfunction
For simplicity's sake, machines can have 1 malfunction at a time. The fact the machine is malfunctioning appears when the machine is examined by anybody. Feel free to debate whether the ideal implementation would need that, but it makes it very clear whatever is going wrong is an intended part of the video game.

The machine's behavior changes in a way that is mostly undesirable. For example, door sensors may keep having false positives and triggering their safety, causing an endless loop of opening and closing. For a lot of doors this would be a minor annoyance, but it can have some interesting consequences in many situations. The door has lost its ability to keep people in or out, but it keeps performing its critical function of connecting rooms.

### Fixing a Malfunction
Now, the fun part. Ideally, well designed malfunctions can be properly fixed, or worked around. The 'proper' fix is a construction graph, and resets the wear on the machine, but may consume time and materials. Malfunctions may also be bypassed by changing how you use the machine, or another, non-construction graph aspect of it. For example, the above malfunctioning door safety sensor would not be a problem if the safety wire was cut. This would be very quick to do and consume no materials, but now the door will crush people as its safety has been disabled.
