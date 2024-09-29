# Maintainer Meeting Notes - Date: 13 Nov 2021
=
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

<!-- Attendees: -->
DrSmugleaf  
Paul  
PJB  
Electro  
Remie  
ShadowCommander  
Vera  
Visne  
Silver  


# Metadata ECS Design | Vera
- Do we make a MetaDataSystem with GetName, SetName, GetDescription, etc methods, or do we make them part of EntityManager?
- MetaData stores the same things as IEntity used to, now. Lots of things will query this info, so it should be part of EntityManager.
- Put the data in MetadataComponent.
- Can't get name directly, localization.
    - GetName/SetName and SetDescription/SetDescription method in the system for localization.

# The VV meets ECS problem | DrSmugleaf, Vera
- How performant does this need to be (for BQL for example)
    - Slightly performant not super optimized
- How do we properly integrate VV-Setters with ECS
    - Put attributes on system methods then make the property read only
    - Show system methods on the component VV window
        - map with attributes, maybe synergy with friendattribute funnies here?
    - Put attributes on component fields that dont need any logic when changed
- How do we (and should we) allow method calls from VV
    - How does VV handle arguments for methods
- How do we make compiling or tests properly tell us if something will screw up in advance
    - Roslyn analyzer
- What to do when a resolve method has multiple entity uids
    - Pass all the ids manually, stop checking arguments when finding the first nullable component parameter with default value

Make it possible to raise events with VV
In the future merge VV with a generic inspector in the engine

# Admin Logs | DrSmugleaf
Vibechecking smugs work :yay:
- PJB are you happy:
  ![](https://i.imgur.com/SfyctsB.png)
  ![](https://i.imgur.com/xvBvZeW.png)

Make a log entry have multiple types
Filter by these types (be able to do and)
Grab the variable name with caller expression syntax from the method call

# Visualizers | Vera
Visualizers should have been components & entity systems from the start, writing visualizers is a pain in the ass my god

Visualizer data should be a component.
Have a way to make entity systems use visualizers ideally.
Components are heavy.
- Struct components?
- Flyweighting?

# Async/Await | mirrorcult
tldr: sometimes async stuff leads to less cbt and sometimes events lead to less cbt
- Which async stuff do we have atm? should it still be async.
    - Some leftover async doafters, port them over to new event doafter
    - Tool interact?
- Which event stuff do we have that should be async?
    - None
- What makes a certain usecase more suited towards async/events respectively.
    - Async never if it needs to be serialized.
        - Await wrapper for events?
        - Needs to be compact.
        - Not possible with serialization, would need to instantiate the task and you can't serialize the task.
    - Events when it needs to be serialized.

You can serialize the entire server state if you can serialize everything, good for testing.
EVERYTHING NEEDS TO BE SERIALIZABLE - Paul Paulson, 2021
We failed mirror

# Examining Tooltip | mirrorcult
Proposals:
- Hold shift to see name, click to see description
    - Hold shift for name + short description, click for long description
    - Short descriptions should make it obvious that a long description is available, i.e. having a "..." symbol/button etc. - Remie
- We gotta show characters equipment and stuff
    - Show it on examine
- Show armor values and stuff
    - How protective armor is
    - Good idea, show it
- How do we do it? it'd be a bit ugly to put all in the tooltip, so how about.. buttons in the tooltip that open up a more close examination?
    - Not bad
    - Popup somewhere on shift click
        - In the examine tooltip and hope it just looks good

We need a vibe check on how examining works in SS13

![](../assets/images/maintainer-meeting/2021-11-13-examine-1.png)
![](../assets/images/maintainer-meeting/2021-11-13-examine-2.png)

# Revert .NET 6 | PJB
- It wasn't a joke...
- ![](https://i.imgur.com/bMBsRbV.png)
- This is terrible for admin logging.
- If PJB fixes ef core issue with memory leaking it's fine.

# MEETING OVER
# MEETING OVER
# MEETING OVER
# MEETING OVER

# paul sounds like he's dying
