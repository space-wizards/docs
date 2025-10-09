# The psychology system


| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| BeatusCrow | BeatusCrow | :warning:| |


# Overview
A system of triggers and hallucinations (shaders and sound effects) that depends on the humanoid's immediate environment and the products they consume. This system will increase the demand for service department roles and improve interaction between departments to keep the station in good condition.

# Background
Recently, I had the opportunity to play about 20 shifts as the Chief Physician, during which I noticed that the Psychologist is a rather underutilized role due to a lack of clients. Few people want to roleplay mental disorders on LRP and MRP projects. In addition, the clown and the mime often only played at the beginning of the shift and then left the game because they received little attention from other players who were busy with their own work.

Furthermore, the Janitor is also an unpopular role on many projects, as there is no gameplay penalty for moving around the station despite piles of garbage or graffiti.

# Features to be added
After considering constructive criticism on the original idea [PR #40779](https://github.com/space-wizards/space-station-14/pull/40779 ), I concluded that the system should work as follows:

* Puddles, wrappers, cans, and other garbage will cause negative emotions for every humanoid.
* Frequently consuming the same dishes will also have a negative effect.
* I think it would be a good solution to allow players to choose their favorite food and drink in the lobby before the round starts. These preferred dishes/drinks will not only avoid reducing the humanoid's mental state but will also have a positive impact.
* Sustaining severe damage for a long time will also negatively affect the mind, but being in good health will restore it.
* I would also like to include some racial traits regarding the psyche, such as arachnids' love for interior items made of webs and moths' corresponding aversion to them.
* I would also add certain items that can strongly influence one's mental state. This could be useful for cult-related gameplay.

I propose replacing the previous, unsuccessful penalties with the following for losing one's mind:

* Applying a weak WB effect in a "sad" state.
* Applying a stronger effect in a "depressive" state.
* A glitch effect when entering a "lost mind" state.
* Adding auditory hallucinations and involuntary character actions (such as using emotes or picking up/throwing random nearby objects).

# Game Design Rationale
In my view, these innovations will not disrupt the round for players and will allow them to choose things they like (yes, it's only about food and drinks for now, but the system is more focused on negative effects that must be eliminated during the game by janitors, cooks, or security). It is the elimination of these triggers that should unite departments. The crew will monitor the station's condition to prevent a decrease in sanity. If it does happen, they can contact a psychologist who will prescribe them medicine.

# Roundflow & Player Interaction
Given that most stations are in good condition at the start of a shift (no rusty walls, debris, puddles, or other visual eyesores), players will only need to maintain their workplaces, which is not difficult. Therefore, the overall pace of the round should not change.

* The burden on Chefs will likely increase to ensure a more diverse menu (which, in turn, will affect orders for Botanists).

* Janitors should become more in-demand, and players will call on them more often to keep their departments clean.

* Psychologists may get more clients if, for example, medicine that blocks shaders (a cure for hallucinations) is added.

# Technical Considerations
This update will require:

* Adding new shaders.
* Slightly modifying the food consumption system to track eaten dishes.
* Modifying the existing system for tracking visible objects.
* Adding a system for auditory and textual hallucinations (changing the penalty system for losing one's mind).
