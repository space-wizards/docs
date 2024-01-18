# RobustHub™

| Designers | Implemented | GitHub Links |
|---|---|---|
| ike709 | :x: No | WYCI |

## Overview

Redesigning the launcher UI/UX and server hub concept to better facilitate creating and playing games developed in Robust Toolbox that *aren't* Space Station 14.

#### This proposal is a high-level conceptual overview. Please do not bikeshed specific details such as every potential field for RobustHub metadata. Once this is conceptually approved, the bikeshedding can commence in subsequent design documents fleshing out each aspect of the design.

Even the nomenclature used (e.g. "Game Hub") is subject to change but preferably won't be bikeshedded prior to overall proposal approval.

## Games & Game Hubs

### Defining "Game"
In this context a "game" is referring to a single *project* such as Space Station 14, OpenDream, or RobustSand. Forks of SS14 are considered separate codebases, but still part of the SS14 "game". 

### Server Hubs
The current concept of a hub is essentially just a list of servers. Under this new system these would effectively be the same, except now each server hub will be associated with a single game. These will be referred to explicitly as "Server Hubs" to distinguish them from "Game Hubs".

When a player adds an additional Server Hub, they will be adding it to a specific game. More on this later in the launcher section.

### Game Hubs
A higher-level hub dubbed "Game Hubs" will fill a similar role to server hubs, but instead of providing a list of servers they will provide a list of *games* and their associated metadata that the launcher needs in order to play them and/or browse their Server Hub.

The list of games available on a Game Hub is under the purview of the hub's operators. The official Robust Toolbox Game Hub (RobustHub) will be managed by the Space Wizards Federation. The system now looks something like this ([direct link](https://i.imgur.com/lyRfy8t.png)):

![[Pasted image 20240117195400.png]]

### RobustHub Repository
A new Space Wizards repo will be created called RobustHub (or similar). This repository will provide the "official" Game Hub that will easily be accessible with any official build of the launcher.

Each game will have a directory in the repository with a variety of metadata and branding files (e.g. the game's default logo). I expect this will be fleshed out and bikeshedded more thoroughly in a separate design document, but metadata would consist of information such as:
- Game name (obviously)
- Creator/Developer information
- Official Discord/GitHub/Website/etc.
- URL to pull News from (like the existing News tab in the SS14 launcher currently)
- If the game is singleplayer, multiplayer, or both. 
	- Multiplayer games will include the default/official Server Hub URL for the game
	- Multiplayer games can decide whether or not to allow adding alternate unofficial hubs in the launcher (obviously SS14 would allow them, but Johnny GameDeveloper might want full control of the servers for his game)
	- Exclusively-singleplayer games will point to the content bundle download URL 
		- (Side note: the existing SS14 launcher still can't launch singleplayer games you've already downloaded like RobustSand)

Adding a game to RobustHub should be as straightforward as creating a pull request and meeting whatever criteria is deemed sufficient by the RT project managers to be considered a separate game.

The process of who will be permitted to update a game's hub entry and how will be fleshed out in a future design document dedicated to RobustHub pending this proposal's approval.

## Launcher Changes
 
 I couldn't find a way to articulate these launcher changes that doesn't make it sound a little crazy at first, so I advise reading all of this section before judging it.

### Robust Launcher
The SS14 launcher as it exists currently will no longer be maintained as a project. Instead the launcher will be stripped of all SS14 branding in favor of Robust Toolbox branding. The "Servers" tab will be nuked in favor of an interface similar to the BYOND pager, except with RobustHub games instead ([direct link](https://i.imgur.com/DSXdzyP.png)):

![[Pasted image 20240117200532.png]]

I don't expect it to look exactly the same; for example, we may have a separate page for singleplayer games. But players will be able to download, play, or browse the server list for any RobustHub game from Robust Launcher.

#### Adding Alternate Server Hubs
On the page for a specific game, there will be a button to configure the Server Hubs for that game (assuming the game allows alternate hubs in the RobustHub metadata).

#### What About Other Game Hubs?
Whether or not other Game Hubs should be addable to Robust Launcher is at the discretion of RT project managers. If they opt not to allow this functionality, other Game Hubs will ship their own launcher forks pointed at their hub instead of RobustHub.

#### Optional: Steam Release
I'm of the opinion that Robust Toolbox should have its own dedicated Steam page which ships Robust Launcher directly, to reduce confusion when people want to play other RT projects like OpenDream via Steam. I'm not saying we should do this *immediately*, but I think it's worth serious consideration if any not-SS14-adjacent projects are created in Robust Toolbox.

We should also check Steam's policy for this sort of thing, as the SS14 launcher at this point would just be Robust Launcher in Game-specific Mode for SS14 (see below).

### Game-specific Mode
Obviously we can't just switch out the SS14 launcher on Steam for Robust Launcher, which is where Game-specific Mode (better name pending) comes in. Somewhere in the launcher build pipeline we will need the option to pass in a RobustHub game identifier which tells the launcher to launch in Game-specific Mode for that game.

When operating in this mode, the RobustHub page is not accessible by default, instead the launcher opens directly into the page for the specified game. This would look practically identical to the current SS14 Launcher experience.

However, buried deep in the launcher settings would be a setting for "Other Games Browser" or similar, which gives the whole explanation that the launcher is able to play other games made in the same game engine. Enabling this setting would still keep the game in Game-specific Mode and open straight into SS14 by default, but now the "RobustHub" page (which would normally be the default page outside of Game Mode) will be unlocked as an additional tab that they can easily navigate to. The purpose of this is so users whom are aware of this functionality don't need to have a duplicate Robust Launcher installation on their PC.

### Example UX
Here's the process of joining an OpenDream server depending on whether you're using Robust Launcher or the redesigned SS14 Launcher (which is just Robust Launcher in Game-specific Mode for SS14).

#### Robust Launcher
1. Start Robust Launcher
2. Find and select OpenDream from the list of games
3. Pick a server and join it

#### SS14 Launcher
1. Start SS14 Launcher
2. Go to somewhere deep in the launcher settings
3. Enable the "Other Games Browser" setting (only needs to be done once)
4. Exit the settings menu
5. SS14's main page now has a "RobustHub" or "Other Games" tab in the corner that players can select
6. Find and select OpenDream from the list of games
7. Pick a server and join it

Quality-of-life enhancements like being able to pin/favorite certain games is subject to further design and bikeshedding.
