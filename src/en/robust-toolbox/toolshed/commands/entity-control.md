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