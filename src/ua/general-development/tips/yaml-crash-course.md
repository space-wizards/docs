# YAML Crash Course

Because apparently there aren't any good ones.

SS14 uses YAML for prototype definitions. It's like JSON but actually supposed to be written by marginally-intelligent carbon-based lifeforms like you and me.

## Comments

Alright first of all, you can make a single line comment by putting a `#` somewhere, everything after that is flat ignored. Example:

```yml
foo: bar # Look a comment.
```

## Data Types

For our purposes, YAML has like 3 data types: strings, lists and dictionaries. If you know enough about YAML to know that this isn't true, then scroll down to the bottom for an explanation.

### String

Defining a string is easy, you just put it there.

```yml
hello
```

Well done you're a YAML master you defined a string with the contents `hello`.

In a lot of cases you want to use special characters that YAML might pick up such as `:`. In that case you should wrap your string in quotes:

```yml
"hello: hi"
```

Still one string.

Double quotes (`"`) allow escape sequences such as our friend `\n` (newline), single quotes (`'`) do not.

### List

Defining a list is done by just putting a `-` in front of something else like a string:

```yml
- A
- B
- C
```

That defines a list with 3 entries: `A`, `B` and `C`. Wow!
The values are just regular strings and you can pull whatever shenanigans you want: quotes or whatever.

> **Ygg's Terrible tips:**
> You can also define YAML inline. Instead of above you can also write:
> ```yml
>    [A, B, C]
> ```
> **Inline YAML is by convention discouraged**, especially for defining components list in entity. It's usually used to denote a simple single item list e.g.
> ```yaml
>    x: [ DoAct ]
> ```


### Dictionary

And finally we have dictionaries, which is just a key/value mapping. So you can do `A` is equal to `B` and `C` equal to `D`.
Just use colons (`:`) to define one like so:

```yml
A: B
C: D
```

Woosh.
The values here (both key and value!) are ALSO regular strings, so you can do this too:

```yml
"A": "B"
"C": "D"
```

The marvels of modern technology.

> **Ygg's Terrible tips:**
> Much like lists, dictionaries can also be defined inline. 
> ```yml
> { A: B, C: D}
> ```
> If you're going: "Wait a minute, inline YAML is just JSON." You're correct. YAML is superset of JSON, and you can actually just parse JSON files as YAML directly if you wanted.

## Nesting Things

Hey it turns out that instead of strings, you can use dictionaries and lists in place of things too.

It gets *kinda* complicated here but if you just do what's sane formatting wise you're fine.

When you have a list, you can put a dictionary in an entry by indenting it. So you can do the following:

```yml
# Like this, first key on the same line.
- A: B
  X: "Y"
```

Really it just makes sense.

Likewise you can put a list inside a dictionary, but in this case the list *has* to start on the next line:

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

Easy.

And yay you can mix and match:

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

## Notes

YAML actually has a lot more data types. YAML is also a mess. There's like 10+ ways to define strings. The entire spec is 100+ pages long and overengineered.

> **Ygg's Terrible tips:**
> Speaking of data types:
> ```yml
>     behaviors:
>     - !type: HeartBehavior {}
> ```
> What does the `!type` map to? 
> A class in SpaceStation14 and/or RobustToolbox. 
> In C#. 
> This of course trips up any YAML validator that tries to find the YAML tag schema for it. Be careful when auto-formatting `.yml` Resources.

SS14 does not use direct object deserialization, and `YamlDotNet` (the library we use to parse YAML) is nice enough to treat scalars as strings only. It does not try to parse strings as numbers or whatever when using the "YAML to LINQ" API (What I like to call "the sane one that isn't completely useless for practical use"). Parsing of numbers is handled by our own C# code on the spot, so if the code expects a boolean it'll treat `true` and `false` correctly, if it expects a string it'll just see it as the string.
