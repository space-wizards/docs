# Types
Toolshed's type system is, **for the most part** that of C#'s. Toolshed adds some additional type rules for the convenience of both users and developers.

## For users
### All values are a list of length 1 (`T -> IEnumerable<T>`)
Toolshed will automatically cast a lone value into a list containing only that value, if necessary. This lets you apply enumerable only commands to single values if necessary.

### Any collection of T is an `IEnumerable<T>`
This isn't technically toolshed specific, but it's useful to know that one can use a `List<T>`, `HashSet<T>`, `Dictionary<K,V>`, etc, as the input to any command taking an enumerable.

### `IEnumerable<T>` is boxed into `List<T>` on assignment.
When assigning an enumerable to a variable, Toolshed will automatically coerce it into a list to fully evaluate it and allow you to reuse it.
Within C#, using an `IEnumerable<T>` more than once is disallowed, hence this coersion. 

## For developers
### Co-variance and Contra-variance limitations.
Toolshed will refuse to do complex assignability checks for types with more than one co-variant or contra-variant argument, as to avoid combinatorial explosion from searching all possible types to use.

### `IAsType<T>` and implicit casting.
Toolshed will, for any type implementing `IAsType<T>`, consider T to be a valid implicit cast for that type.
For example, if `Foo : IAsType<Bar>`, Toolshed will use the IAsType implementation to obtain Bar from Foo if it'd allow it to successfully typecheck a command run.