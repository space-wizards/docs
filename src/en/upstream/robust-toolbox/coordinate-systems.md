# Coordinate Systems

This document describes the measurement and coordinate systems inside the RobustToolbox engine. Any GamePacks should be using the same standards as RobustToolbox.

## 1 The World
The world is the 2D space inside a Map. The 2D world exists on the X/Y plane, and the camera appears to be above the surface looking down at it from the sky.

N/E/S/W cardinal directions can be used in the world, but be careful that you are not mixing them up with screen directions. "East" would be the +X axis, and "North" would be the +Y axis. Remember that the camera looking down at the world can rotate, so the "South" direction in the world is not always "Down" or "South" on the screen.

### 1.1 World Measurements
All measurements and units are in the metric system. The sizes of objects and distances are measured in meters. For visual reference, 1 Grid tile is 1m². Space Station 13 sprites are designed where 1 tile is 32px², so this project will also use the 32 texels per meter for sprites.

### 1.2 World Coordinate System
The game world is using 2D right-handed coordinates. This is all the Transform and Angle values you are working with in content. This is the math you learned in school, where the unit circle rotates counterclockwise as theta increases. The default camera is oriented so that it is looking down the -Z axis at the X/Y plane that all of the entities exist on. The local "Up" direction (forward face of the X/Y plane) of the world is +Z. All rotations rotate around the Z axis.

You can press the `F3` key to enable debug overlays, which print out all of the coordinate info.

### 1.3 Entity Local Coordinates
+Z should be local Up (away from gravity) so it can easily be ignored in 2D. The three basis vectors are +X (Forward), +Y (Left), +Z (Up).

You can use the `showpos` debug command to display the local direction widget on entities.

### 1.4 View Matrix
The default view matrix starts with no rotation, a scale of 0.5 (Zoom of 2), and centered on the client's attached entity. The View can be rotated around the Z axis, translated to a position in the world, and scaled to create a zoom effect. The view matrix is conceptually the inverse of the camera's world matrix (if the camera was an entity).

Using this default view matrix with 0 rotation, the +X axis of the world is to the right, and the +Y axis is upwards on the screen. The +Z axis is coming out of the screen.

If you want to manipulate the view matrix directly, you can open a VV window for your player, then on the client open the `EyeComponent`.

### 1.5 Projection Matrix
This is a basic orthographic projection like any other top down 2D game. Distance from the camera on the Z axis does not change the size of entities, all parallel lines stay parallel, and the field of view is a rectangular prism.

## 2 The Screen
The screen is the square box that the game is projected onto when rendered. This is what you look at, it's like a *window* that you can look at the World through. Some game effects and the UI are directly drawn onto the screen.

### 2.1 UI Coordinate System
The UI uses 2D left-handed coordinates, with the origin at the top left, +X going to the right, and +Y going down. Rotations go clockwise. This is exactly like any other UI library.

### 2.2 Clyde and OpenGL Coordinates
You do not need to worry about how Clyde works internally, or how Clyde works with OpenGL.