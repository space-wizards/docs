# Entity commands
{{#title Entity commands}}

## Sources
{{#template 
    ../../../templates/toolshed-command-head.md
    name=entities
    typesig=[none] -> IEnumerable<EntityUid>
}}
Returns a list of all entities in the simulation.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=ent &lt;entity&gt;
    typesig=[none] -> EntityUid
}}
Returns the given entity.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=spawn:at &lt;entity prototype&gt;
    typesig=IEnumerable?<EntityCoordinates> -> IEnumerable?<EntityUid>
}}
Spawns a new entity at the given coordinates.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=spawn:on &lt;entity prototype&gt;
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<EntityUid>
}}
Spawns a new entity on the other given entity.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=spawn:attached &lt;entity prototype&gt;
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<EntityUid>
}}
Spawns a new entity attached to the other given entity.

## Filters
{{#template 
    ../../../templates/toolshed-command-head.md
    name=with &lt;component type&gt;
    typesig=IEnumerable<EntityUid> -> IEnumerable<EntityUid>
}}
Filters the input for entities with some given component.
This command can be inverted with `not`.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=prototyped &lt;prototype&gt;
    typesig=IEnumerable<EntityUid> -> IEnumerable<EntityUid>
}}
Filters the input for entities built from a given prototype.
This command can be inverted with `not`.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=paused
    typesig=IEnumerable<EntityUid> -> IEnumerable<EntityUid>
}}
Filters the input for entities that are currently paused.
This command can be inverted with `not`.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=nearby &lt;range&gt;
    typesig=IEnumerable?<EntityUid> -> IEnumerable<EntityUid>
}}
Filters for entities nearby the inputs, returning all entities within range of it.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=named &lt;name&gt;
    typesig=IEnumerable<EntityUid> -> IEnumerable<EntityUid>
}}
Filters the input for entities with a name matching the regex `$regex^`.

## Transforms
{{#template 
    ../../../templates/toolshed-command-head.md
    name=comp:has &lt;component type&gt;
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<bool>
}}
Returns true if the input entity has the given component, otherwise false.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=pos
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<EntityCoordinates>
}}
Returns the coordinates of the input entities, relative to their parent.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=mappos
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<EntityCoordinates>
}}
Returns the coordinates of the input entities, relative to the map.

## Mutators
{{#template 
    ../../../templates/toolshed-command-head.md
    name=delete
    typesig=IEnumerable<EntityUid> -> [none]
}}
Deletes the inputs from the simulation. Gone. Poof.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=replace &lt;entity prototype&gt;
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<EntityUid>
}}
Replaces the given entities with another of some prototype, preserving only it's position and rotation.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=tp:coords &lt;entity coordinates&gt;
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<EntityUid>
}}
Teleports the input to the given coordinates.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=tp:to &lt;entity&gt;
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<EntityUid>
}}
Teleports the input to the given entity.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=tp:into &lt;entity&gt;
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<EntityUid>
}}
Teleports the input into the given entity.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=comp:add &lt;component type&gt;
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<EntityUid>
}}
Adds the given component to the entity.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=comp:ensure &lt;component type&gt;
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<EntityUid>
}}
Ensures the input has the given component.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=comp:rm &lt;component type&gt;
    typesig=IEnumerable?<EntityUid> -> IEnumerable?<EntityUid>
}}
Removes the given component from the entity.