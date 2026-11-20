# Partial Prototypes

Partial prototypes allow you to modify existing YML prototypes from a different file.

This is specially useful as a fork, as it lets you change upstream YML without causing merge conflicts later. Forks of forks can also use this system without problems.

Not all changes can easily be made, or are recommended to be made, into partial prototypes. Read below to distinguish which use cases it should and should not be used for.

To skip ahead to how to remove, modify, and add new components specifically, skip to [Special cases](#special-cases)

## Creating your first partial prototype

To start creating partial prototypes, open up `/Resources/PartialPrototypes/partialPrototypes.yml` in your text editor. It contains comments explaining how it works in detail, but in basic terms it is a list of directories where the game should look for partial prototypes on startup.

The order in which those directories are defined is what determines in what order the changes are applied, in case of a fork of a fork. For example, this will apply the changes in _ForkOne first, then the ones in _ForkTwo:
```yaml
- /Prototypes/_ForkOne/Partials
- /Prototypes/_ForkTwo/Partials
```

Both directories and specific files can be listed.

When using the above, if the following files exist:

`/Prototypes/original_file.yml`
```yaml
- type: entity
  id: MyEntity
  name: my entity
  components:
  - type: MyComponent
    list: !Clear
    - 1
```

`/Prototypes/_ForkOne/Partials/file.yml`
```yaml
- type: entity
  id: MyEntity
  components:
  - type: MyComponent
    list: !Clear
    - 2
```

`/Prototypes/_ForkTwo/Partials/file.yml`
```yaml
- type: entity
  id: MyEntity
  components:
  - type: MyComponent
    list: !Clear
    - 3
```

Then the list will only contain 3, as the original is applied first, then _ForkOne's, and then _ForkTwos.

## How partial prototypes work with each node type

There are 3 types of nodes in YML: Mappings, sequences, and values. Each one is treated differently by partial prototypes. There are two exceptions to this: the prototype `parent` field, and the entity prototype `components` field, explained further down.

### Mappings
Mappings are dictionaries, where different keys are assigned values. They are defined in the following format:
```yaml
dict:
  key1: "value"
  key2: "value"
```

By default, mappings are added to or replaced if the key already exists.

Mappings can also have key-value pairs removed entirely:
```yaml
dict1:
  key1: !Remove # Removes key1 from this dictionary, regardless of its assigned value
  key2: !Remove 1 # Removes key1 from this dictionary, but only if its value is 1

dict2:
  key1: !Remove # Removes key1 from this dictionary...
  key2: 2 # ... then adds key2 with a value of 2

dict3: !Clear # Clears this dictionary, removing all keys from this dictionary...
  key1: 1 # ... then adds key1 with a value of 1
```

### Sequences
Sequences are lists, each at a specified index. They are defined in the following formats:
```yaml
list:
- 1
- 2
- 3

shortFormList: [ 1, 2, 3 ]
```

By default, elements are appended to the end of the sequence.
```yaml
list: # Add three elements. These will appear at the end of the list in the order specified.
- 1
- 2
- 3
```

`!Index` can be used to specify the index to insert at:
```yaml
list:
- !Index:0 1 # Insert 1 at the start of the list
- !Index:-1 1 # Insert 1 before the last element of the list, AKA second-to-last
```

`!CombineIndex` can be used to combine an element at the specified index, optionally with negative indexes as with `!Index`.

This is used to modify some of the data for mappings that are inside a sequence, however, this should generally not be used as you have no guarantee that upstream's order won't change in the future. See [Cases where you should and shouldn't use partial prototypes](#cases-where-you-should-and-shouldnt-use-partial-prototypes) for an explanation.
```yaml
list:
- !CombineIndex:0 data: # Merges this data with the data at the first index of the origina list. Without !CombineIndex:0, this would be appended at the end of the list as normal.
  int: 1
  str: "a"
```

### Values
Values are a single value such as a string, integer, or boolean. They are defined in the following formats:
```yaml
stringValue: "string"
intValue: 1
boolean: true
nullValue: null
```

### Mixed sequences and values
In cases where one is a sequence and another is a value, both are treated as a sequence.

This means that they are combined, and the rules in [Sequences](#sequences) are followed.

This applies most often to prototype `parent`, where sometimes it is defined as a value, and sometimes a sequence for multiple parents.

If both are values:
```yaml
# Original YML file
- type: entity
  parent: MyEntityBase1
  id: MyEntityOne

# Partial YML, different file
- type: entity 
  parent: MyEntityBase2 # This will change the parent to be only MyEntityBase2
  id: MyEntityOne
```

If both are sequences:
```yaml
# Original YML
- type: entity
  parent: [ MyEntityBase1 ]
  id: MyEntityOne

 # Partial YML, different file
- type: entity
  parent: [ MyEntityBase2 ] # This will change the parent to be [ MyEntityBase1, MyEntityBase2 ]. Keep in mind that as normal, parent changes are applied in reverse, so if both parents change a value, then MyEntityBase1's will be used. 
  id: MyEntityOne
```

If one is a value and one is a sequence (does not matter which):
```yaml
# Original YML
- type: entity
  parent: MyEntityBase1
  id: MyEntityOne

# Partial YML, different file
- type: entity
  parent: [ MyEntityBase2 ] # This will change the parent to be [ MyEntityBase1, MyEntityBase2 ]. Keep in mind that as normal, parent changes are applied in reverse, so if both parents change a value, then MyEntityBase1's will be used. 
  id: MyEntityOne
```

If the original is a value, and the partial is a sequence tagged with `!Clear`:
```yaml
# Original YML
- type: entity
  parent: [ MyEntityBase1 ] # Sequence in this case
  id: MyEntityOne

# Partial YML, different file
- type: entity
  parent: !Clear [ MyEntityBase2 ] # This will set the parent to be only [ MyEntityBase1 ], by clearing first and then adding MyEntityBase2 afterwards. 
  id: MyEntityOne
```

If the original is a sequence, and the partial is a value tagged with `!Clear`:
```yaml
# Original YML
- type: entity
  parent: [ MyEntityBase1 ] # Sequence in this case
  id: MyEntityOne

# Partial YML, different file
- type: entity
  parent: !Clear MyEntityBase2 # This will set the parent to be only [ MyEntityBase1 ], by clearing first and then adding MyEntityBase2 afterwards. 
  id: MyEntityOne
```

This is because partial prototypes do not currently have a way to check a field's type.

For this reason, if you are modifying lists such as `parent` downstream in partials, it is recommended that you always make it a list for consistency, optionally using `!Clear` when needed. Otherwise, an upstream change could change your expected behaviour.

Sequences can be defined both as comma-separated elements between square brackets (most often used in `parent`), and new-line separated lists starting with dashes.

### Special cases
Partial prototypes have two special cases that behave differently than normal, entity `components`, and sequence-value pairs, most often found in prototype `parent`.

Entity components are treated as a dictionary internally, even though they are defined as a list in YML.

This lets you easily remove existing components:
```yaml
- type: entity
  id: MyEntityOne
  components:
  - !Remove type: MyComponent # Removes MyComponent, if it exists. If it doesn't, nothing happens.
```

Add components:
```yaml
- type: entity
  id: MyEntityOne
  components:
  - type: MyComponent # Adds MyComponent. This is added to the end, but ordering does not matter in components.
```

Modify components:
```yaml
- type: entity
  id: MyEntityOne
  components:
  - type: MyComponent
    int: 1 # Changes the value of Int to 1 in MyComponent, additionally adding the component if it does not exist.
```

For `parent`, see [Mixed sequences and values](#mixed-sequences-and-values)

## Partial prototype tags

All operations that aren't a simple replacement or addition have a tag associated with them:

- `!PartialOnly` is used on the prototype `type` field to make the prototype not be added as a regular prototype, if no original non-partial one exists. This can also be used outside explicitly-marked partial directories and files.
- `!Partial:0` will make the prototype a partial prototype, even if it is defined outside the directories or files that are marked as partials in your codebase.
- `!Clear` will clear a mapping or sequence, before optionally making additional changes to it.
- `!Remove` will remove an element by value from a dictionary or list.
- `!Index:0` inserts the element at a specific index on a list, instead of appending it to the end. This works the same as `IList.Insert` in C#, where normally it would be a `IList.Add` operation. Negative indexes will start from the end, where `Index:0` would be the end, the same as not specifying an index, and `Index:-1` would make the element become the second to last element in the list.
- `!CombineIndex:0` will combine the data at a list's index. See [Cases where you should and shouldn't use partial prototypes](#cases-where-you-should-and-shouldnt-use-partial-prototypes) for an explanation on when you shouldn't use it.
- `!PartialModified` is used internally by the engine to support easily adding, removing, and modifying components. You should never use this yourself.

## Cases where you should and shouldn't use partial prototypes

Partial prototypes are specially useful when changing names, descriptions, adding or removing a component, or changing most component data.

They should not be used in cases where you need to modify specific indexes on a list, such as in reagent effects. This can technically be done by using `!CombineIndex`, however that will break if the upstream prototype list's ordering is ever changed, leading to bugs.

Another difficult case is adding many elements to a list at different indexes. If you find yourself adding many elements to a list, all at different indexes, you may find it easier to use `!Clear` and then re-write the whole list. Keep in mind that any upstream changes to the list would then never be reflected in your fork, as it will be cleared completely before adding your elements. This can make you miss new important additions to that list in a future pull, such as pre-spawned items in a bag, or borg module tools.

If you are modifying a prototype's parent, it is recommended that you always `!Clear` first, even if you are only setting a single parent value. See [Mixed sequences and values](#mixed-sequences-and-values) for more detail.

## Prototype variants

Partial prototypes can be combined with prototype variants to modify many prototypes at once.
```yaml
- type: !PartialOnly listing
  id: !type:CreateVariants
  values:
  - VendorPlushieHuman
  - VendorPlushieMoth
  - VendorPlushieVulp
  conditions: !Clear
```

## Other tags

`!PartialOnly` can be added to the `type` definition to make it so that, if an original definition does not exist, the partial will not result in a new entity being created.

For example, this will make it so the game does not create MyEntity if no other original, non !PartialOnly prototype definition exists with the same type and id.:
```yaml
- type: !PartialOnly entity
  id: MyEntity
```

`IPrototypeManager.ValidateDirectory` has a `partialNoOriginalError` parameter that controls whether a partial existing without an original to modify is an error or not.

`!PartialOnly` ignores this parameter and will not error, even if it is set to true.

The value can be changed in Content.YAMLLinter, and defaults to false and does not error. This can be useful for automatically detecting stale partials if their original definition is deleted in a later pull, but defaults to false for cases where different fork content is pulled into the same repository, where inactive YML may be preferred to manually fixing every missing prototype.

# FAQ

## Can this add, modify, and remove components?
Yes, see [Special cases](#special-cases)

## How do I manually partial a file or directory in code, without using `/Resources/PartialPrototypes/partialPrototypes.yml`?
Call `IPrototypeManager.PartialFile` and `IPrototypeManager.PartialDirectory`. Both expect an index, which is normally the index at which the entry appears in the `partialPrototypes.yml` file, used to determine in what order to apply the changes from multiple forks. Smaller indexes are processed before larger ones. This does not retroactively partial already parsed prototypes.

## Do prototype variants work with this?
Yes, see [Prototype variants](#prototype-variants)

## Does this work with prototypes other than entity prototypes?
Yes. 

## Does this work with YAML hot reloading?
Yes. If you encounter any bugs with it though, report them in the [engine repository](https://github.com/space-wizards/RobustToolbox). You however cannot make the uploaded prototype be a partial, the uploaded prototype will replace the original definition, if one exists, or add a new one as normal if it doesn't.

## Does this work with forks of forks?
Yes. The order in `/Resources/PartialPrototypes/partialPrototypes.yml` specifies the order in which these files are processed. See [Creating your first partial prototype](#creating-your-first-partial-prototype) for more information.

## My game gets stuck loading after adding partial prototypes
Check that your partial prototypes do not result in an entity having the same parent defined twice, such as when `!Clear` is not used in `parent`. See [Mixed sequences and values](#mixed-sequences-and-values) for more detail.

## Can this remove prototypes?
No, partial prototypes are only intended to make changes to existing YML that you could make in the same file, in a separate file. Commenting out whole prototypes can't be done by this system (yet?). See abstract prototypes for a way to mark existing prototypes abstract, even in bulk. To remove **components**, see [Special cases](#special-cases).

# Other Resources
Other guides made by the community. If there's a contradiction between this doc and one linked below, check the engine comment in `IPrototypeManager.PartialDirectory` for up-to-date documentation, or ask either community for clarification.

Keep in mind that any codebase conventions present in these community docs may not be applicable to WizDen code, or your fork's code.
- [Starlight's partial prototypes doc](https://docs.starlight.network/s/d49865f5-b555-4803-b5d7-5c2fde54fbd9/doc/partial-prototypes-cT5r0wdfJ9)
