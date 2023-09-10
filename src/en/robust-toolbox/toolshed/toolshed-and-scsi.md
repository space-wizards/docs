# Toolshed and (S)CSI
Toolshed can be invoked freely from scsi with the `object? tsh(string toolshedCommand)`, `T tsh<T>(string toolshedCommand)`, and `TOut tsh<TIn, TOut>(TIn value, string toolshedCommand)` functions. You can additionally call any of the IInvocationContext functions like ReadVar, WriteVar, and co in the interactive context, as the context implements IInvocationContext.
```admonish warning
`csi` and `scsi` Toolshed variables are not shared with the development console, they are different contexts.
Toolshed in C# scripting can invoke all commands regardless of permissions, ala the server console.
You may need to manually initialize Toolshed on the client by calling `ToolshedManager.Initialize()` if using csi.
```

## Toolshed call semantics
Toolshed commands automatically have the providied initial value "piped in", meaning the first command provided must fit the initial value. If no initial value is provided, this type is `[none]`, which matches normal development console semantics. If a value is provided, Toolshed will expect the first command to fit the signature `TIn -> ???` where TIn is the type of or some downcast of the provided value.

## Toolshed expression type vs the real type
As you may have guessed, the return value of a toolshed command invocation is not necessarily the actual type of the value returned, often being an interface or other higher level type which is not itself constructable. **There are no guarantees for what the underlying type is and you shouldn't make assumptions about it.**