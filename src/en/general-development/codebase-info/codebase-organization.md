# Codebase Organization

Space Station 14 and it's related projects are _big_. Like, very big.

It's pretty hard to stay organized with hundreds of contributors, so we have made some organizational guidelines to how they are all organized.

## Structure

Up-front, basic code structure is:

1. All game code will be organized in the project folders `Content.Client/Shared/Server` etc.
2. These project folders are further split into subsystems to limit their scope (such as `Clothing`/`Atmos`/`Botany`).
3. These subsystems are them split into their constituent parts through `Components`, `EntitySystems`, `Visualizers`, `UIs`, `Prototypes`, etc.

The basic resources structure is:

1. All resources/assets will be organized inside the `Resources` directory.
2. The resources directory is then split between all of the different kinds of assets (`Audio`/`Textures`/`Entities`etc).
3. The directories for all the different kinds of assets are then further split into their own respective subsystem (`Clothing`/`Atmos`/`Botany`)

If you are creating a new folder or file, you should keep in mind:

1. If there would only be one file in a folder, it doesn't need a folder.
2. Do not create a "misc" folder, as it makes organization completely arbitrary.

The rest of this guide goes over the history of how it got this way and the methodology behind it.

## History

In SS13 (SS14's predecessor), all game code was thrown into a `code/` directory with things being organized by abstract things. This made the codebase very messy and made it a pain to get anything done.

In SS14, we have decided to group things by their relevance to certain systems, such as Atmos/Botany/etc, as well as the classes that are required for it.

# Game Code

## Projects

First, Space Station 14 and RobustToolkit are split into two separate Git repositories.

In each of these Git repositories, they are further split into 3 "projects", which are:

1. `Server`  
   The server is meant to hold server-specific code that the client should never interact with, like atmospherics or botany. This assembly is only located on the game server.
2. `Shared`  
   Shared holds code that is shared between the Server and the Client. This assembly itself is not executable and relies on Server and Client to call methods from it. Shared is primarily for code-sharing and network prediction (which is when the client and server run code simultaneously to reduce latency).  
   Importantly, Shared code cannot rely on any code that isn't itself in shared.
3. `Client`
   Client, like the Server, contains the client-specific code like the UI. This assembly is only sent to the client/the person actually playing the game.

This was done mainly to help do "separation of concerns". The Server shouldn't have to worry about how the UI is rendered or how the game looks, and the Client shouldn't have to worry how the backend of the game works.

## Subsystems

The idea of the subsystems is that we should further abstract how each subsystem works. All subsystems probably need some way to interact with the ECS, so we give them a `Components` and `Systems` folder. This continues until everything's been properly split.

The whole `Server`/`Shared`/`Client` system already follows this in SS14, and RobustToolkit is currently on the way.

# Resources

Outside of the regular Projects is the Resources directory.

The way that this is organized is a slight inversion of the subsystems, as the constituent parts (or, types of assets) and the subsystems switch in order.

## Prototypes

In the `Prototypes` sub-tree under `Entities`, it is common code style to create a `base_[name].yml` type that holds all the parent prototypes. All of the other prototypes should go in a different file or folder.

This was chosen to make the directory structure mirror the prototype inheritance tree, making it obvious where to place new prototypes as well as being fairly unambiguous when choosing to create new folders.
