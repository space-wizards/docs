# Experimental Machinery & Machine Upgrading

Research disciplines, while widely positive in terms of their effect on science research as a whole, had an unforeseen downside. Due to requiring all research to be sorted into categories (disciplines), cross-disciplinary items end up semi-pointlessly sorted into categories, thus bloating disciplines and giving them unnecessary edges above other categories.

The two most obvious examples of this are **Power Cells** and **Machine Parts**. Despite being used in every single discipline (barring _Arsenal_), they are sorted into _Industrial_ and _Experimental_, respectively. The effects of this are quite apparent, seeing as these are some of the most widely researched disciplines in the game.

By locking these very common items and mechanics into disciplines, players are either:

- Obligated to research these technologies every round because they are so commonly used.
- Never familiarized with these mechanics since they are inundated with more pressing things to research.

Furthermore, machine upgrading itself has quite poor discoverability, with the majority of players never utilizing it outside of cost discounts for their lathes.

My proposal to solve this is to bring these specific parts into their own sub-department, called experimental machinery.
This is less of a rework of machine upgrading but moreso an expansion to better integrate it with the rest of science.

## The Machinery Database

The main utility system of the sub-department, the machinery database serves two main purposes:

- To instruct players on what machines they have available and what their upgrades are.
- To incentivize players to build new machines and to upgrade existing ones.

These exist pretty much in isolation from each other, so I'll refer to them henceforth as _Codex_ and _Contracts_, respectively.
The structure itself is just a large computer terminal (perhaps it will be a 2x1 structure for visual interest).

### The Codex
The Codex is simply a dictionary that allows science players to view information regarding machines. 
At the beginning, all entries in the Codex will be displayed as black silhouettes with a **???** for the name with a listing of what research technology unlocks it. 
As the respective machine boards are unlocked, the corresponding Codex entries will be revealed to the player.

Clicking on one of these entries will give the following information about the machine:
- The entity name and description
- What parts are needed to build it
- What each part upgrade does for the machine
- The total material cost to create the machine

The unlocking of a codex entry will play a "ping" sound and cause a visual change in the sprite until the entry is looked at, to aid in player discoverability.
The ultimate goal of this is to remove the obfuscation that comes with machine upgrading so that players are better able to understand it.

### Contracts
While The Codex servers to saturate the players with knowledge about the different machines and what they do, **contracts** exist to actually push players to utilize this knowledge.

Contracts have two main categories:
- **Build**: Build a machine or a set of machines that you have unlocked. 
  - Build X amount of a certain machine.
  - Build machines X, Y, Z.
- **Upgrade**: Upgrade a machine you've unlocked with higher level parts.

Completing contracts gives the department two main rewards, _research_, which can be used to unlock more technologies, and _machinery data_.
Machinery Data is essentially an experience system used to unlock high tiers of machine parts. 

Instead of using research to unlock technologies from the discipline, the machinery data can be spent to unlock recipes for each of the machine parts. Once all of the parts in a tier are unlocked, the next tier becomes available.

This addresses a common complaint about /tg/-style machine upgrading, wherein the only relevant parts are t1 stock parts, due to being widely found, and t4 bluespace parts, due to their power. By locking these parts behind actual tasks, it forces players to actually use middle tiers of parts.

## RPED
As a result of these changes, the RPED becomes more than just a simple convenience tool. The RPED now functions as the scanner through which these interactions are facilitated. "Using" the RPED in your hand will have it switch to a secondary "scanning mode" through which you can log the upgrades and constructions you make. **NOTE:** trying to log a round-start machine does not count as a construction.

Using the RPED on the Machinery Database will transfer all of the scans/logs to the database.

This all means that the RPED will be moved out of research as well. It can either be in some kind of science lathe or some kind of dedicated machinery lathe.
This is a really spur of the moment idea but it would be cool if the machinery database could print machine parts + interact with the codex.

## Technical Changes
The most pressing changes are just breaking upgradeable stuff into its own component so that things like APCs become upgradeable, since they aren't technically machines.

Additionally, the machine part to upgrade needs to either be defined in yaml or defined in a way that clientside entities can ALWAYS be used. This requires pondering on my part and I'm sure I'll figure it out at some point.