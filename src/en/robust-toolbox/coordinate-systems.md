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

### 1.6 Coding conventions

`Vector2` are row vectors with an implict $1$ in the third component. These vectors are transformed by `Matrix3x2`, which are row-major matrices with an implicit third column of $\left(0, 0, 1\right)$. Vectors are pre-multiplied with matrices, i.e. $vM$.

Refrain from giving your `Matrix3x2` variables names such as `matrix`, `invMatrix` or `matty`, as this makes your code unnecessarily difficult for others to read. Instead, what transformation the matrix is applying. The suggested way to describe this transformation is to use a naming pattern in the form of "original space - TO - result space"; for example, a matrix named `entityToWorld` converts a vector in entity space into world space. Aside from clarity, this naming convention has several advantages:

- When inverting a matrix, swap the order of the space names - the inverse of `entityToWorld` is `worldToEntity` and is the matrix which transforms a vector in world space into entity space.
- When multiplying matrices and choosing a name for the result, the space names can be concatonated; for example `var entityToWorld = entityToGrid * gridToWorld` - in general, the space names in the "middle" of the multiplication will match. This allows you to easily see if your transformation makes sense -- `entityToGrid * gridToWorld` sounds good, but `gridToEntity * gridToWorld` would be a very suspicious transformation and might indicate a bug. 
 
## 2 The Screen
The screen is the square box that the game is projected onto when rendered. This is what you look at, it's like a *window* that you can look at the World through. Some game effects and the UI are directly drawn onto the screen.

### 2.1 UI Coordinate System
The UI uses 2D left-handed coordinates, with the origin at the top left, +X going to the right, and +Y going down. Rotations go clockwise. This is exactly like any other UI library.

### 2.2 Clyde and OpenGL Coordinates
Unless you are writing shaders, you do not need to worry about how Clyde works internally, or how Clyde works with OpenGL.

With respect to the above coding conventions, when writing a shader, we need to make considerations for the fact that OpenGL post-multiplies vectors with matrices (i.e. $Mv$). The recommended naming convention is "result space FROM original space"; for example, the matrix `worldFromEntity` converts a vector from entity space into world space. 
