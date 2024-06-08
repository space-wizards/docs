# YAML Crash Course

SS14 uses [YAML](https://yaml.org/spec/1.2.2/) for prototype definitions.

It's like JSON but actually supposed to be written by marginally-intelligent carbon-based lifeforms like you and me.

```admonish note
Space Station 14 only implements the core subset of YAML with some extensions to make it more amenable to the project.
```

## Comments

First of all, you can make a single line comment by putting a `#` somewhere, everything after that character on the same line is ignored.

````admonish example "Comment Example"
```yml
foo: bar # Look a comment.
```
````

## Data Types

For our purposes, YAML has like 3 data types: strings, lists and dictionaries. If you know enough about YAML to know that this isn't true, then scroll down to the bottom for an explanation.

### String

In YAML, strings do not need to have quotes around them by default. You just write like it was a normal text file.

````admonish example "String Example"
```yml
hello
```
Well done you're a YAML master you defined a string with the contents `hello`.

````

In a lot of cases you want to use special characters that YAML might get confused about, such as `:`. In that case you should wrap your string in quotes:

````admonish example "String Quotes Example"
```yml
"hello: hi"
```

The result is still one string, `hello: hi`.
````

There's also a difference between double (`"`) and single (`'`) quotes in YAML. Only double quotes allow escape sequences like newline (`\n`).

### Lists

Defining a list is done by putting a `-` at the start of a line in front of something else, such as a string.

````admonish example "List Example"
```yml
- A
- B
- C
```

That defines a list with 3 entries: `A`, `B` and `C`. Wow!
The values are just regular strings and you can pull whatever shenanigans you want: quotes or whatever.
````

While heavily discouraged, you can also define YAML inline by surrounding the items in square bracket (`[` & `]`).

````admonish example "Inline List Example"
 ```yml
    [A, B, C]
 ```

It's usually only used to denote a simple single item list e.g.
```yaml
   x: [ DoAct ]
```
````

### Dictionary

The last datatype in YAML is a dictionary, also known as a key/value mapping.

If you want to describe the relation that `A` means `B`, then you'd put a semicolon between them to create the mapping.

````admonish example "Dictionary Example"
```yml
A: B
C: D
```
````

The fact that regular text is a string also means that both the keys and values are strings. If desired, you can wrap them individually with quotes and they are functionally equivalent.

````admonish example "Quoted Dictionary List Example"
```yml
"A": "B"
"C": "D"
```
````

Much like lists, dictionaries also have a discouraged inline syntax, where you put curly braces (`{` & `}`) around the key/value pairs, with commas separating each pair.

````admonish example
```yml
{ A: B, C: D}
```
````

If you are thinking: "Wait a minute, inline YAML is just JSON?" then you are correct.

YAML is super-set of JSON, and you can actually just parse JSON files as YAML directly if you wanted.

## Nesting Things

YAML then uses its three building blocks to define more structure.

To nest a dictionary inside of a list, you put a `-` before the first pair in the dictionary, and then indent each pair after that so that all of the keys are left-aligned.

````admonish example "Dictionary Nesting Example"
```yml
# Like this, first key on the same line.
- A: B
  X: "Y"
```
````

Likewise, list can go inside dictionaries. In this case the list starts on the line after the key is defined.

````admonish example "List Nesting Example"
```yml
A:
- "X"
- "Y"
- "Z"

B:
- "U"
- "V"
- "W"
```
````

All of these together lets you create a complete prototype.

````admonish example "Complete Prototype Example"
```yml
# First, all prototype files are a massive list of all of the prototypes under it.
# This is one entry, which is itself a dictionary.
- type: entity # Key: "type", Value: "entity"
  parent: BaseHandheldInstrument
  id: HelicopterInstrument
  name: toy helicopter
  description: Ch-ka-ch-ka-ch-ka-ch-ka-ch-ka-ch-ka...
  components:
  # Nest the list inside of the "components" key.
  # These elements are then dictionaries.
  - type: Sprite
    sprite: Objects/Fun/Instruments/otherinstruments.rsi
    state: helicopter
  - type: Instrument
    program: 125
  - type: Item
    size: Small
    storedRotation: -90
```

Source: [`Resources/Prototypes/Entities/Objects/Fun/Instruments/instruments_misc.yml#L79-L92`](https://github.com/space-wizards/space-station-14/blob/63e0ee08cb50dbd937e11ab1e965b5f79aae134d/Resources/Prototypes/Entities/Objects/Fun/Instruments/instruments_misc.yml#L79-L92)
````

## SS14 Syntax Extensions

To make it easier to reference C# classes directly from YAML, there is a `!type` syntax sugar.

This will likely trip up any auto-formatter or alternative syntax linters.

````admonish example "!type Example"

```yml
- type: loadoutEffectGroup
  id: GreyTider
  effects:
  - !type:JobRequirementLoadoutEffect
    requirement:
      !type:RoleTimeRequirement
      role: JobPassenger
      time: 36000
```

Source: [`Resources/Prototypes/Loadouts/Jobs/Civilian/passenger.yml#L2-L9`](https://github.com/space-wizards/space-station-14/blob/63e0ee08cb50dbd937e11ab1e965b5f79aae134d/Resources/Prototypes/Loadouts/Jobs/Civilian/passenger.yml#L2-L9)
````
