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
The current concept of a hub is essentially just a list of servers. Under this new system these would effectively be the same, except now each server hub will be associated with one or more "games". These will be referred to explicitly as "Server Hubs" to distinguish them from "Game Hubs".

Each Server Hub will have a whitelist of game(s) that can be advertised on it. For example, the official WizDen Server Hub could support both SS14 and RobustPong servers. When a server attempts to advertise on a Server Hub, it must declare the game that it is running and it must be one of the Server Hub's whitelisted games to advertise successfully. Server Hub operators are responsible for moderating the servers that are permitted to advertise on their hub, and ensuring that information such as the advertised game is accurate. 

When a player adds an additional Server Hub in the launcher, the additional servers will be associated with the correct games using the game identifier being advertised by the server. More on this later in the launcher section. A potential quality-of-life enhancement would be to allow players to toggle individual games on a per-Hub basis (e.g. if I were running my own alternative Server Hub for OpenDream servers dubbed "IkeHub", which advertises both SS13 and Eternia servers, a player may wish to disable polling the hub for Eternia servers if they only play SS13).

### Game Hubs
A higher-level hub dubbed "Game Hub" will fill a similar role to server hubs, but instead of providing a list of servers they will provide a list of *games* and their associated metadata that the launcher needs in order to play them and/or browse their Server Hub. **Note:** The launcher is only intended to support a singular "Game Hub", and the concept exists to provide examples of how Robust Toolbox can be utilized separately from Space Wizards Federation infrastructure, such as games developed independently of SS14 or communities who wish to "hard fork" their own infrastructure.

The list of games available on a Game Hub is under the purview of the hub's operators. The official Robust Toolbox Game Hub (RobustHub) will be managed by the Space Wizards Federation. The system now looks something like this ([direct link](https://i.imgur.com/lyRfy8t.png)):

<img src="https://i.imgur.com/lyRfy8t.png" />

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

<img src="https://i.imgur.com/DSXdzyP.png" />

I don't expect it to look exactly the same; for example, we may have a separate page for singleplayer games. But players will be able to download, play, or browse the server list for any RobustHub game from Robust Launcher.

#### Adding Alternate Server Hubs
As previously mentioned, the launcher will support allowing players to add additional Server Hubs. This should be as straightforward as adding a URL to a list in the launcher settings, with the launcher handling it from there. The launcher will check to make sure a game's RobustHub metadata permits alternate hubs before polling an alternate Server Hub for that particular game. When a player goes to a particular game's server list, the launcher will poll the Server Hub only for servers with that game's identifier. On the game's server list, each server entry will include a field displaying the Server Hub it was pulled from, and the list should support optionally filtering by Server Hub.

Adding alternate Server Hubs should warn the player about potential moderation issues compared to using official Server Hubs. We may wish to somehow present each hub's rules to the player when the hub is being added in the launcher.

#### Optional: Steam Release
I'm of the opinion that Robust Toolbox should have its own dedicated Steam page which ships Robust Launcher directly, to reduce confusion when people want to play other RT projects like OpenDream via Steam. I'm not saying we should do this *immediately*, but I think it's worth serious consideration if any not-SS14-adjacent projects are created in Robust Toolbox.

We should also check Steam's policy for this sort of thing, as the SS14 launcher at this point would just be Robust Launcher in Game-specific Mode for SS14 (see below).

### Game-specific Mode
Obviously we can't just switch out the SS14 launcher on Steam for Robust Launcher, which is where Game-specific Mode (better name pending) comes in. Somewhere in the launcher build pipeline we will need the option to pass in a RobustHub game identifier which tells the launcher to launch in Game-specific Mode for that game.

When operating in this mode, the RobustHub page is not accessible by default, instead the launcher opens directly into the page for the specified game. This would look practically identical to the current SS14 Launcher experience.

However, buried deep in the launcher settings would be a setting for "Other Games Browser" or similar, which gives the whole explanation that the launcher is able to play other games made in the same game engine. Enabling this setting would still keep the game in Game-specific Mode and open straight into SS14 by default, but now the "RobustHub" page (which would normally be the default page outside of Game Mode) will be unlocked as an additional tab that they can easily navigate to. The purpose of this is so users whom are aware of this functionality don't need to have a duplicate Robust Launcher installation on their PC.

Let's expand upon the hub diagram to incorporate launcher examples ([direct link](https://i.imgur.com/Kz5KM6Y.png)):

<img src="https://i.imgur.com/Kz5KM6Y.png" />

#### Optional: Don't Hide Other Games
PJB seems amenable to the idea of _not_ hiding the Other Games list by default when operating in Game-specific Mode.

### Example UX
Here's the process of joining an OpenDream server depending on whether you're using Robust Launcher or the redesigned SS14 Launcher (which is just Robust Launcher in Game-specific Mode for SS14). This assumes we do decide to hide other games by default in Game-specific Mode.

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

### Optional: RobustHub Game Jam

Once RobustHub is fully implemented, we should advertise and then run a game jam (1-2 weeks) to develop new games (singleplayer or multiplayer) for RobustHub, unrelated to SS14. In addition to adding some variety to the games list, this will give us a chance to dogfood the system and also identify pain points in creating new Robust Toolbox projects.

Depending on the level of interest, we could potentially offer prizes for the best submissions like a fancy Discord role and/or a $20 Steam gift card.
