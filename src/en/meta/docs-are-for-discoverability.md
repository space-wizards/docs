# Docs are for Discoverability

This document is here to elucidate an **extremely important point** when it comes to writing docs that everyone looking to contribute new pages should internalize.

***Docs are for discoverability!***

What this means is that docs for systems should *not* include things like:
- Specific method APIs that are bound to change
- Enumerating and explaining every field a random prototype has
- Explaining code details that are 100x better communicated through code comments and xmldocs

When someone is looking for 'documentation' on a subject, there's really two different things they could be looking for. They could have only a general idea of what they want to do and are looking for the *how*--looking for *what tools and systems are available* to begin with, and how they fit together as a cohesive whole. This is the service that a markdown documentation site like this is intended to provide.

Or, they can be searching for the *what*--the specifics of the APIs they're working with, what methods they can call, what to pass into those methods, overrides for abstract methods, etc. This is best served by *your IDE*, because C# is a statically typed language and this information is very easily available to anyone programming. Search in files is also *very* powerful, when your IDE can't help (such as searching for available YAML datafields).

``````admonish example
Good:
```
If you are trying to accomplish X, the best way is through GlubbySystem...
...
First make a GlubbyPrototype in YAML, then in your own system call methods on GlubbySystem
to create and register a glubber...
```

Bad:
```
Here are the fields available on GlubbyPrototype:
glubPotency: this field is an integer
glubDecay: this field is a timespan
glubberDelay: this field is a timespan
glubTargets: this field is a dictionary of string to entityuid of glub target
```
``````

There is no guarantee that all of the docs pages here will actually adhere to this concept! A lot of them are very, very old. If you feel like rewriting them, [go for it!](./guide-to-editing-docs.md)