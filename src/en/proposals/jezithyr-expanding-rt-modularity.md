# Expanding Robust Toolbox Modularity
| Designers | Implemented | GitHub Links |
|---|---|---|
| Jezithyr | :x: No | TBD |
## Overview

A proposal for creating a more modular robust toolbox to enable greater flexibility for both Spacestation 14 forks and Non-Spacestation 14 projects.

#### This proposal is a high-level conceptual overview. The examples of Robust modules are just examples! The plan is to start with just RobustEngineCore (current RobustToolbox) and slowly split out/add new modules.

This proposal also builds on Ike's Gamehub concept #133

## Engine Modules

### What is an Engine module
An engine module is self contained assembly that may have dependencies or dependants. An engine module is effectively a self contained "Piece" of the Robust Toolbox game engine for a particular area. Eg: Physics, UI, Rendering, etc.
Engine modules are served by a Central CDN in the same way the Engine currently is. 

### Core Engine Modules
Core engine modules are engine modules that are *NOT sandboxed*. These modules deal with low level systems and as such their maintenance is managed by the CDN owner or a trusted community.

### Community Modules
Community engine modules *ARE Sandboxed* modules that are created/maintained by the community. These are still provided by the robust CDN however the community is responsible for their upkeep. 
Community modules are effectively a way for the community to contribute features to the engine that only make sense in specific use cases and would not be approved as a core module.

### Modular Architecture
Instead of a monolythic engine assembly being served to each server, smaller individual assemblies are served. This allows developers to tailor Robust Toolbox to their particular usecase, 
or server hosts to run different versions of engine modules to mitigate breaking changes while still receiving updates for the other modules (this may not always be possible). Additionally, 
community modules allow for community servers to make limited "engine modifications" that are easily reusable by other servers. 
https://i.imgur.com/nW7uYru.png

## Module Infrastructure:
### Developer Specific CDN
Modules are served in a very similar way to the current method of serving engine binaries. When a server registeres with a gamehub, it will provide access to that gamehub's allowed CDNS.
Instead of manifest files including just the engine version, they will instead contain a list of engine modules and their appropriate version/hashes, and which CDN to fetch the file from.
Clients/Servers can only pull modules from CDNs that are approved by the GameHub. Additionally multiple different CDNs may be used. https://i.imgur.com/lbEWGQ4.png

# TODO
