# Invocation contexts
`IInvocationContext` is the context in which toolshed executes commands, it provides shell functions, variable read/write, permission checking, and error reporting.

## Best practices
- If your command temporarily sets a variable for executing a block, one should implement a wrapper context that provides the variable within it instead of setting the variable on the existing context. This avoids variable leaking.
- CheckInvokable should not be overriden without VERY good reason, as it is a security boundary.
- Do not discard errors, if you don't have a way to handle the error nicely it should likely be thrown as an exception to ensure it's seen by someone.