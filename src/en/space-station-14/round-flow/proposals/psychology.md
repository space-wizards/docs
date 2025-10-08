# The psychology system


| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| BeatusCrow | BeatusCrow | :white_check_mark:| [PR #40779](https://github.com/space-wizards/space-station-14/pull/40779) |


## Overview

A system of psychology consisting of subsystems of triggers and psychoanalysis. This will give diversity to the representatives of this profession, as well as increase the importance of the service department, since some triggers (clown/mime clothes, priest altar, etc.) have a positive effect at the emotional component.

## Background

Recently, I had the opportunity to play about 20 shifts for the chief physician, during which I noticed that the psychologist is a rather unclaimed role due to the lack of clients. Few people want to act out mental disorders on LRP and MRP projects. In addition, the clown and the mime often played only at the beginning of the shift, and then left the game, because they received little attention from those who wanted to do their work in the department throughout the shift.

In addition, the cleaner is also an unclaimed role on many projects, as nothing prevents you from moving around the station in the presence of mountains of garbage or graffiti.

## Features to be added

The psychology system currently consists of 3 trigger systems and a psychological analysis system.

The first trigger system is visual, which applies various effects depending on what you see. The field of view is 5 tiles (objects behind obstacles like walls are not visible, of course). Visually, you can be affected both by items on other players (for example, a clown's mask) and by any other object... All trigger objects in their prototypes can have both positive and negative effects. Additionally, they can affect all races or only some of them. Along with race restrictions, there's also a whitelist for roles, so that, for example, a roboticist wouldn't be afraid of borgs while others might be scared of them.

By the way, it's worth mentioning that triggers are selected randomly in volume and order for each player at the start of the round, but there's also the possibility to make some of them permanent. For example, clown and mime equipment has a positive effect on representatives of all races.

The second system is the chemical content of the organism. Each solution provides an instantaneous positive effect (calculated per ounce of substance) and a long-term negative effect to express a kind of dependency... So, eating a chocolate bar will give you 5 units of emotional state (for each ounce of substance) and you'll lose 10 units over the next 15 seconds. There are also restrictions here, for example, ethanol doesn't affect dwarves.

Finally, the third system is health. When taking damage that amounts to 5% of the allowable amount (from the maximum to enter a critical state), you will start losing emotional state points.

Let's move on to the psychological analysis system... The psychologist has many special cards "with images" that can contain either 1 trigger or an infinite number. All triggers are divided into groups (departments, common features), which makes it possible to first identify the approximate group that your trigger belongs to, and then use refinement to find the specific one.

In this simple way, a medical specialist can create recommendations for your work environment (maybe you should put more flowers in your department).

When the emotional state level drops below neutral (sadness, depression, deep depression), black-and-white shaders with different coefficients and slowing effects are applied. When reaching the depression state, the character may commit self-anti-resurrection with a probability of 0.15. This process occurs if you have an item that deals damage in some inventory slot or in your backpack... If there are none, then any item from the ground can be picked up for this act. If there are none of those either, static objects can be used: microwave, crematorium, etc.

## Game Design Rationale

In my opinion, such a system will make it necessary for various departments and roles to interact frequently. This is how people can contact the cargo department to purchase plush toys or flowers to increase their emotional state. They can also visit a bar or other public space more often to watch the performances of a clown and a mime, which raise the mood with their funny appearance. The same cleaner will now become a necessary part of any station, because if there are candy wrappers or puddles, your mood worsens. It is worth saying that the system will not oblige you to run to a psychologist every minute... According to my observations, on most maps, there are on average about 30 objects in rooms of different departments, which, at the boundaries of a good emotional state (from 600.0f to 750.0f) and the average value of the influence of triggers (0.125), gives 20 minutes of a calm existence with a transition only to a sad emotional state (assuming that every second decreases by 0.125, although I have often seen an increase).

## Roundflow & Player interaction

This innovation works from the beginning of the shift and, as I described earlier, does not force players to worry too much about their emotional state, which does not change the overall pace of the round. In my opinion, players can safely consult a psychologist at any time, but in order to encourage them to take this action, I added one event that randomly changes the emotional state of the character with a probability of 0.3. In addition, I would like to add a brainworm-type antagonist in the future, which would have to identify a person's negative triggers through analysis and then cause hallucinations in the form of them, thus bringing him to a critical state in order to leave the host for procreation (which is not a RDM process, but a calm RP wagering). Nevertheless, I assume that some players, having identified their triggers with the help of a psychologist, will put them in a small room in large numbers, which will give a significant change in their emotional state. And at the moment, I have not provided any systems to limit this situation.  Of course, for the most part, these mechanics are for the medical department, and in general, they fit in well here, not changing much, but only expanding the current capabilities of the psychologist.

# Technical Considerations

- Does the feature require new systems, UI elements, or refactors of existing ones? Give a short technical outline on how they will be implemented.
- Are there any anticipated performance impacts?
- For required UI elements, give a short description or a mockup of how they should look like (for example a radial menu, actions & alerts, navmaps, or other window types)
