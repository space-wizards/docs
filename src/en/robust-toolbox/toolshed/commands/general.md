# General

## Sources
{{#template 
    ../../../templates/toolshed-command-head.md
    name=iota
    typesig=T -> IEnumerable<T> where T: INumber<T>
}}
Returns <code>1..N</code>

{{#template 
    ../../../templates/toolshed-command-head.md
    name=to &lt;dest&gt;
    typesig=T -> IEnumerable<T> where T: INumber<T>
}}
Returns <code>N..M</code>

## Filters
{{#template 
    ../../../templates/toolshed-command-head.md
    name=where &lt;block (T -> bool)&gt;
    typesig=IEnumerable<T> -> IEnumerable<T>
}}
Filters the input by the provided code block.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=unique
    typesig=IEnumerable<T> -> IEnumerable<T>
}}
Filters the input by uniqueness, eliminating duplicate values.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=take &lt;amount&gt;
    typesig=IEnumerable<T> -> IEnumerable<T>
}}
Removes N values from the input, discarding the rest.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=select &lt;quantity&gt;
    typesig=IEnumerable<T> -> IEnumerable<T>
}}
Removes a quantity (amount or percentage) of values from the input randomly, discarding the rest.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=sort
    typesig=IEnumerable<T> -> IEnumerable<T>
}}
Sorts the input from least to greatest.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=sortby &lt;block (T -> TOrd)&gt;
    typesig=IEnumerable<T> -> IEnumerable<T>
}}
Sorts the input from least to greatest using the given ordering value.

```
    entities sortby { allcomps count }
```

{{#template 
    ../../../templates/toolshed-command-head.md
    name=sortmapby &lt;block (T -> TOrd)&gt;
    typesig=IEnumerable<T> -> IEnumerable<T>
}}
Sorts the input from least to greatest using the given ordering value, returning the ordering values.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=sortdown
    typesig=IEnumerable<T> -> IEnumerable<T>
}}
Sorts the input from greatest to least.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=sortdownby &lt;block (T -> TOrd)&gt;
    typesig=IEnumerable<T> -> IEnumerable<T>
}}
Sorts the input from greatest to least using the given ordering value.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=sortmapdownby &lt;block (T -> TOrd)&gt;
    typesig=IEnumerable<T> -> IEnumerable<T>
}}
Sorts the input from greatest to least using the given ordering value, returning the ordering values.

## Transforms
{{#template 
    ../../../templates/toolshed-command-head.md
    name=isempty
    typesig=IEnumerable<T> -> bool
}}
Returns true if the input is empty, otherwise false.
This command can be inverted with `not`.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=isnull
    typesig=object? -> bool
}}
Returns true if the input is null, otherwise false.
This command can be inverted with `not`.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=count
    typesig=IEnumerable<T> -> int
}}
Counts the number of values in the input.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=iterate &lt;block (T -> T)&gt; &lt;times&gt;
    typesig=IEnumerable<T> -> IEnumerable<T>
}}
Repeats the given code block N times over it's own output, effectively `f(f(...N f(x)))`

{{#template 
    ../../../templates/toolshed-command-head.md
    name=first
    typesig=IEnumerable<T> -> T
}}
Returns the first value in the input, or errors if there isn't one.


## Mutators
{{#template 
    ../../../templates/toolshed-command-head.md
    name=rep &lt;amount&gt;
    typesig=T -> IEnumerable<T>
}}
Repeats the input value N times.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=bin
    typesig=IEnumerable<T> -> IDictionary<T, int>
}}
Counts the number of times each unique instance of T occurs in the input, returning a dictionary of unique instance : count.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=map &lt;block (TIn -> TOut)&gt;
    typesig=IEnumerable<TIn> -> IEnumerable<TOut>
}}
Applies the given code block to each element of the input.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=reduce &lt;block (T -> T)&gt;
    typesig=IEnumerable<TIn> -> T
}}
Reduces the input, effectively `f(x1, f(x2, ...f(xn-1, xn)))`