# Maintainer Meeting (21 January 2023)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 21 January 2023 19:00 UTC

**Attendees:**
- moony
- AJCM
- Zoldorf
- Visne
- ElectroSR
- Remie
- Wrexbe
- DrSmugleaf
- Vera
- mirrorcult
- PJB

## Bumping map count to 15 | metalgearsloth
- Most of [c#10595](https://github.com/space-wizards/space-station-14/issues/10595) is done
- 15 is too many
- **Bump it up to 12**
- **1 more low pop map, 1 more high pop map**

## What to do about RSI licensing | metalgearsloth
- Do we use RGA outside of the folder
    - No, RGAs are for other resources
- Do we use something else entirely
- **Make the license field a list of licenses interpreted by a script**
- **Copyright is freeform interpreted by a human**
- **Don't use RGAs for RSIs**

## Do we explicitly block Windows 7 | PJB
- **Make the pop-up always show up, not only once**
- **Change the text and make closing the pop-up close the launcher too**
- **Localize the pop-up message to Russian if the OS is in Russian**

## Do we mandate guidebook entries for new large features | mirrorcult
- **Yes**

## How do we distribute replay recordings & clients, and should we hide some data | ElectroSR
- Should we hide data such as admin aghost positions?
    - No
- How do we distribute it
    - Tie replays to a version (game/engine), metadata and a link
    - Download the replay and its data should launch the sandboxed client with a specific version
    - Include the commit number in the replay file (any data can be appended to the replay file from content)
    - Content versioning scheme (commit number), download link (if it doesn't work you download it yourself)

## Can we do another stress test trace | mirrorcult
- Try and say that 10 times fast "stress test trace"
    - Stresst
- Run it from time to time (ping PJB)
- Ping tester for it
- Having links that connect you to a server would be useful

## PJB's renderer ASMR for Jez | PJB
- Problems with the renderer:
- We can't do what Byond can with planes, complex filtering
- We don't want planes (they are a bad idea)
- The alternative is a GOOD API (difficult)
- We can't have multiple post-shaders
- The hard part of a renderer is integrating it into the rest of the game engine (we are 2D)
- There are no existing rendering APIs we can just take
- We need a rendering API to:
    - Draw textures, polygons at locations
- The game's code:
    - Puts sprites at locations
    - People do funny things (shaders, render targets)
- Our API has some of this but is unperformant, not very flexible
- Going from "draw sprite" to "opengl arrays" is just a lot of glue-code, not complicated
- Clyde is divided internally, only one file takes the sprites and actually draws them with the rest of the API
- Using a different rendering API to replace Clyde because of the maintenance burden requires it doing everything that Clyde already does
- We can't build Clyde on top of another incomplete rendering API because it would be spaghetti
- When we tried to use Godot we had our own sprite component and tried to build it on top
    - Godot was too high level, too unperformant to integrate with nicely
    - Need something that's lower level
    - Godot 4 nonwithstanding
- Maybe something like Monogame but we would need a lot of glue code (replacing all of Clyde and refactoring anything that uses Clyde)
- PJB transferred from the Clyde mines and into the Monogame mines (we would need to fork it)
- Any other libraries unknown that don't need us to half-ass it
- Not worth the complexity
- PART 2: Even if you can find a good rendering API
- There are some good libraries (e.g. BGFX) that make you not need to write separate OpenGL/DirectX/Vulkan backends
- You would still have your own "Clyde" on top of it
- We still support very old hardware up to 10 years old, even if you raised this number WebGPU/etc require more modern APIs which would drop older hardware
- We don't want to expose the graphics library on Robust
- PROBLEM 2 (It's actually 3):
- We need to support Veldrid
- PROBLEM 3 (4):
- Older hardware
- this is still all just problem 2: "older hardware" she's just talking in a very roundabout funny manner
- Don't worry about it
- Maybe (maybe) use (maybe) WebGPU which uses the browser which reduces a lot of things you would need to create
- DirectX 10.1 hardware is what we target
- Visne left to go party, he is uncool
- Writing multiple backends: not good
- PJB is lost and confused, sad
- Just use Clyde :+1:
- Clyde2.0 When
- **If you want it easy drop OpenGL support**
    - Less ass to maintain
- There are no plug-in rendering APIs
- Maybe get WebGPU or Vulkan-based, code against that, OpenGL is a fuck


## Early Access Roadmap
- gamemodes/antags
    - dynamic | mirror
        - lings?
            - needs DNA
        - blob | Remie
        - revolutionaries
            - we want a generic antag overlay system
            - loyalty implant
            - faction system
- EL BODY SYSTEM | jez
    - some refactors were done by mirror, still some left
    - surgery died in the war of 1992
        - Mirror died in the war of 1993
    - limb damage.....
- Salvage proc gen | moony
    - she did it go port it https://github.com/Citadel-Station-13/space-station-14/tree/master/Content.Server/_Citadel/Worldgen
- body system but again
- body system
- __***ENGINE EDITOR***__ | PJB
    - could benefit from full state reload
- movement refactor
    - Client side movement?
        - a smidgen
            - as a treat
            - acruid pls com bak
- Add more shit to the guidebook
- combat rework (needs to be bikeshedded)
    - https://github.com/space-wizards/space-station-14/issues/3378
- ghostrole/antag bans
    - unify ghost roles prototype (mind refactor)
- experimental science
    - "Science is still a piece of shit" - Vera 28/05/2022
    - "I haven't played the game in 2 years" - Vera 07/01/2023
- State mandated Xonotic matches | PJB
    - Please I have severe withdrawal symptoms
    - Replaced by private SS14 playtests
    - Woman down
    - She added Miku to her server (real) now you can play as miku pls play with her
- The game runs like shit how do people play this
    - still does | PJB 28/05/2022
        - "how do people play this game" (high pitched scream) | PJB 28/05/2022
    - Slightly better | PJB 11/06/2022
    - It's better but still not as good as I'd like it to be | PJB 25/06/2022
    - I haven't played the game since | PJB 16/07/2022
    - "Please read the last line of that subsection" | PJB 30/07/2022
    - "Please unread the last line of the previous subsection" | PJB 07/01/2023
    - "I spent the last two weeks coding Rain World" | PJB 21/01/2023
- A trailer for Steam

Crashes / Critical bugs: (when are we moving these to GitHub)
- role timers not counting properly
  => till next time
