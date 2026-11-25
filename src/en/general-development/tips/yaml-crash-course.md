# YAML Crash Course

SS14 uses YAML for prototype definitions. Like JSON, YAML is a human readable data serialization format. The main difference between these two is that YAML supports more data types and is closer to natural, human language. Most importantly, YAML supports comments, whereas standard JSON does not.

### If you are already familiar with YAML, take note:
>SS14 implements a custom data-serialization system atop YAML, effectively imposing its own data model and type-handling semantics on the format. This provides engine-specific functionality but introduces additional complexity and fragility.
>You will understand more as you read, but there are additional notes at the bottom of this page that may help.


## Comments

To add a comment to a YAML document, simply add a `#` symbol before your text. This lets the YAML parser know that the subsequent text on that line is not data.

The `#` symbol can be added at the beginning of a line to create a `Full-line comment`, or in-line to create an `In-line comment`.

Example:
```yml
# Full-line comment. Hamlet is the cutest.
foo: bar # In-line comment. I love Hamlet.
```


## Data Types

For our purposes, YAML has 3 data types: strings, lists and dictionaries. 

### String

Defining a string is simple. Plain text without any prefix is recognized as a string.

```yml
hello
```

In a many cases, you'll want to use special characters that the YAML parser will recognize as a syntax indicator, such as `:`. 

To avoid the parser recognizing this as a key-value indicator, and allow it to be used literally, you can wrap it in double quotes.

```yml
"hello: hi"
```

Double quotes (`"`) allow escape sequences, such as `\n` (newline), while single quotes (`'`) do not.


### List

You can define a list by using the `-` prefix.

```yml
- A
- B
- C
```

That defines a list with 3 entries: `A`, `B` and `C`.

> **Ygg's Terrible tips:**
> You can also define a list in-line. This looks like:
> ```yml
>    [A, B, C]
> ```
> **Inline YAML is by convention discouraged**, especially for defining components list in entity. It's usually used to denote a simple single item list e.g.
> ```yaml
>    x: [ DoAct ]
> ```


### Dictionary

Finally, we have dictionaries. Dictionaries are used to represent data as a unique identifier, such as:

```yml
A: 123
C: Hamlet
```
The marvels of modern technology.

> **Ygg's Terrible tips:**
> Much like lists, dictionaries can also be defined inline. 
> ```yml
> { A: B, C: D}
> ```
> If you're going: "Wait a minute, inline YAML is just JSON." You're correct. YAML is superset of JSON, and you can actually just parse JSON files as YAML directly if you wanted.


## Nesting Things

Alternatively, instead of strings, you can use dictionaries and lists to represent values.

For example, when you have a list, you can put a dictionary in an entry by indenting it.
```yml
# Like this, first key on the same line.
- A: B
  X: "Y"
```

Likewise, you can put a list inside a dictionary, but in this case the list *has* to start on the next line:

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

Below are further examples:

```admonish warning
Don't expect these prototype examples to be something up-to-date for SS14. It's just here to show syntax.
```

```yml

# First, this entire thing is stored in a massive list. That's why there's a -.
# We're looking at one entry, a dictionary.
- type: entity # Simple key/value pairs.
  id: SMES
  name: SMES
  description: Stores power in its super-magnetic cells
  components:
  # AHA! A list in a key. Wow!
  # This list ALSO stores dictionaries.
  - type: Sprite
    sprite: Buildings/smes.rsi
    scale: 2, 2
    layers:
    - state: smes
    - state: smes-display
      shader: unshaded
    # Input lights.
    - shader: unshaded
      state: smes-oc0
    # Charge meter.
    - visible: false
      shader: unshaded
      state: smes-og1
    # Output lights.
    - shader: unshaded
      state: smes-op0
  - type: Icon
    sprite: Buildings/smes.rsi
    state: smes
```

## Additional Notes

SS14 does not use direct object deserialization, and `YamlDotNet` (the library we use to parse YAML) treats scalars as strings only. It does not try to parse strings as numbers when using the "YAML to LINQ" API. 

Parsing of numbers is handled by our own C# code on the spot, so if the code expects a boolean it'll treat `true` and `false` correctly, if it expects a string it'll just see it as the string.
