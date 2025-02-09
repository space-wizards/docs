# Game Area Design Document & Template

The goal of a game area design document is to provide a cohesive direction for developers that want to add or modify content in the game. New PRs should aim to align themselves with the design as laid out in the document, and Maintainers are expected to adhere to them when reviewing and discussing PRs.

These documents are meant to be "directional" documents rather than "implementation" documents; focus should be on defining the goals and boundaries of a game area, not the specific game mechanics the player interacts with. The documents should include high-level descriptions of gameplay and the intended *feeling* players should have when interacting with the game area. 

A design document may be more or less precise depending on how large or small the game area it is covering. A general combat document may be more high-level compared to a gun weapons document, and similarly a departmental document may be more high-level than one covering just a specific role in that department. 

Below is the recommended template to use.  
<br>
## Template
<br>

# Document Name

## Concept
> 1-2 paragraphs acting as an abstract, condensing the information of the document into an easily readable format and setting expectations for what the other sections will contain. It should provide a brief overview of the game area, but avoid to include any information that isn't mentioned elsewhere in the document.  

## Intended Experience
> A collection of simple high-level ideas that embody this game area. These are usually expressed with singluar words or short punchy phrases, but may also include a short one sentence explanation. The goal is to convey the *feeling* a player should have when playing/interacting with the game area, such that other documents and PRs can align with that intended experience. 

## Responsibilities
> A collection of points regarding what the game area is responsible for in terms of gameplay, mechanics and/or station duties. This section should highlight what unique things the game area brings to the game and simulatione. If the game area is a resource provider to the station, this is highlighted here.

## Desired Gameplay
> A list of high-level concepts, explaining the *kind* of gameplay and mechanics we want to see in the game area's design. Each list entry should be a short sentence summarizing the design pillar with a more detailed (1-2 paragraph) description underneath. 

> While the "Intended Experience" section focuses on how it *feels*, this section's entries should focus on what the player *does*. They should still be high-level, in that you are not providing instructions on specific gameplay mechanics; they are there to act as guides when creating new mechanics or interactions, serving as the measuring posts to make sure that what you are trying to do will fit in the boundaries of the game area.

## Undesired Gameplay
> Similar to "Desired Gamplay", but instead listing easy pitfalls and directions we *don't* want the game area to move in. This sets boundaries and helps achieve cohesion when designing new aspects of an area.
