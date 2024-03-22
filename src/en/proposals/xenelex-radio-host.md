# Radio Host Role

| Designers | Implemented | GitHub Links |
|---|---|---|
| xenelex | :information_source: Open PR | TBD |

## Overview

This document proposes transitioning the Musician role and to a Radio Host role and potentially merging it with the Reporter role.The change aims to enhance player interaction and media engagement within the game. By elevating the Musician role to a Radio Host, it will expandg responsibilities to include broadcasting music, talk shows, and news. Also, considers merging the Reporter role into the Radio Host, centralizing media functions and simplifying mapping requirements.

## Role Transition and Potential Merger
Radio Host Role:
Transition the Musician role to a Radio Host, expanding the role’s responsibilities to include broadcasting music, talk shows, and news.

Reporter Merger:
Potentially merge the Reporter role into the Radio Host, centralizing media functions and simplifying mapping requirements.

## Features
**PDA Cartridge Transcription**: A new PDA cartridge will be introduced, capable of transcribing the Radio Host’s spoken words in real-time, allowing players to read broadcasts if they cannot listen to them. Te design of it would be like teleprompter showing the spoken words and the person who said it, there sohuld also be a topic on the upper left of the message transcription that could be changed by the radio host using the Radio Console (more on that later), and the pda will only transcribe spoken words to a linked extended microphone that is connected to a server or the radio console.

**Headset Music Integration**: Headsets will now have the functionality to tune into the Radio Host’s channel and play music directly from their broadcasts, providing a more immersive experience. the headset can also now turn up or turn down the music playing from the radio station.

**Radio Host Room Camera**: A camera will be installed in the Radio Host’s room to have visual broadcasting. This will enable players to engage in debates and see live reactions from the Radio Host.

 **Unique Radio Host Identifiers**: By using a new custom Headset called the Radio Headset, radio hosts will have unique names or call signs in radio communications. For example, a Radio Host might use “SS14 News" as their identifier when delivering urgent updates in common comms.

 **Music Queue**: Allow the Radio Host to set up a playlist or queue of music that can be broadcasted through the station’s headsets.

### Unique Items and Objects
The **Radio Console** will serve as the central hub for the Radio Host. It will allow the Radio Host to:

**Change the Radio Station’s Name**: Customize the station’s branding to reflect the show’s theme or content.

**View and Edit Playlists**: Prequeue music and organize playlists for upcoming shows.

**Broadcast Controls**: Manage live broadcasts, including starting, stopping, and transitioning between segments.

**Scheduling System**: A scheduling system will be implemented to help the Radio Host plan and organize events, such as: Live Music, Talk Shows, Quiz Shows

**Extended Microphone**: This item will be one that will be only way to have the radio host words be transcribed onto the pda app.

**MIDI Rack**: the MIDI Rack is a specialized piece of equipment for the Radio Host, serving as the primary interface for playing and managing music.It features slots for instrument disks, which Radio Hosts can use to insert disks containing unique instrument sounds that will be incorporated into the songs they play. The MIDI Rack has 12 slots for instrument disks, allowing for a wide range of musical customization. At the start of each shift, the available instrument disks will be randomized, providing fresh options for Radio Hosts to create unique soundscapes. The Radio Host will get additional disk by ordering them from cargo or finding them in maints.

**Speakers**: A way to play music in the Radio Station room by connecting it to the MIDI Rack, this will broadcast to nearby players within the radio station, creating a communal listening experience.

**Antenna**: A large 2x2 antenna will be installed as part of the radio station’s equipment. The antenna serves as a critical component for broadcasting and can become an objective for thieves or a tool for sabotage. Thief Objective: The antenna can be targeted by thieves as a high-value objective by disassembling it into multiple pieces.

**Radio Headset**: The custom headset will not only serve as a tool for broadcasting but also as a symbol of the Radio Host’s identity.
Unique Feature: The headset will allow Radio Hosts to broadcast using their radio station name, it will connect to the antenna to use this function, this will also enable a syndicate function mentioned later in the design doc.

### Syndicate Unique Items
The Syndicate Radio Host items should be primarily Auxiliary or Support equipment. This classification will position them as pivotal components of an intelligence network, offering strategic advantages. Other syndicates can leverage this network for enhanced communication and coordination, thereby reinforcing teamwork.

**Electric Extended Microphone**

 A modified microphone that delivers an electric shock, causing Shock and stamina damage to the target.

Damage: Deals about 8 shock. Capable of causing stamina critical condition in approximately 6-8 hits. 

Cost: The price for this item is to be determined.

**Sonic Grenade**

Functionality: A throwable device that emits a powerful sonic blast, stunning anyone in its vicinity.

Effect Radius:

Direct Hit (0 tiles away): Stuns for 5 seconds.

1 Tile Away: Stuns for 3 seconds.

2 Tiles Away: Stuns for 1 second.

Cost: Priced between 6 to 8 telecrystals.

**Fake Radio Station Cartridge**

A deceptive device that appears identical to Radio Station Cartridge but contains embedded Syndicate code.

Functionality: When installed in a PDA, the fake cartridge scrambles the ID name when logged by a door, rendering the user anonymous and complicating identification efforts by security, using the fake cartridge can save Syndicate members telecrystals without the need for multiple, costly agent id cards.

Cost: priced between 2-4 Telecrystals.

**Comms Interceptor Module**

The Comms Interceptor Module is a sophisticated device designed for a Syndicate Radio Host it will come in a pair. One big module to install onto the antenna and the other a small one inserted into the Radio Headset

Interception: The module grants the ability to receive all comms messages from various departments when installed onto the antenna can be removed after a long doafter. The intercepted message will be sent to the receiving headset.

Stealth: Designed to be discreet, it does not alert others to the interception, maintaining the user’s cover.

Selective Filtering: The user can filter specific departments to monitor, avoiding information overload.

Downside: the inability to broadcast music and inactivty in the pda app will raise suspiscion to crew.


## Examples
**Music Show**

Title: “Galactic Grooves”

Concept: A weekly music show where the Radio Host plays a curated selection of tracks from across the galaxy.

Players can submit song requests via comms.

Interaction: Collaborate with Passengers for live performances, and allow listeners to vote for their favorite tracks.

**Talk Show**

Title: “Space Station Speak”

Concept: A talk show featuring interviews with prominent station characters, discussions on station policies, and call-ins via comms from players.

Interaction: Use the camera in the Radio Host room to stream video interviews, enhancing viewer engagement.

**Quiz Show**

Title: “Astro-Quiz Hour”

Concept: A game show where contestants answer trivia questions about the game universe. Prizes can be in-game items or currency.

Interaction: Integrate with the Reporter (IF not merged) role to provide real-time updates and questions based on current events in the game.

**Collaboration with Reporter** (IF not merged)

Title: “SS14 Live News”

Concept: A news segment where the Radio Host and Reporter collaborate to deliver breaking news and updates.

Interaction: The Reporter gathers news while the Radio Host broadcasts it, eliminating the need for the Reporter to use the media console. The PDA transcription feature allows players to follow along with text updates.
