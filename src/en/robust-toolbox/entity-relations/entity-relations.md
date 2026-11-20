# Entity Relations

Most Robust Toolbox's underlying systems (for example networking) assume that all stored `EntityUid`s remain valid. However, when an entity is deleted, ensuring that there is no invalid reference anywhere may be repetitive or even complicated.

**Entity Relations** is a built-in tool that automatically finds and resets all invalid references to the entity when it is terminated.

This section explains how to properly use entity relations and how they work under the hood.
