# Environments
Toolshed's primary method of controling which commands are available (which dictates everything from parsing to execution flow) is through `ToolshedEnvironment`. The default environment lives at `ToolshedManager.DefaultEnvironment`, and contains every command with the `[Toolshedcommand]` attribute applied.

## Best practices
- Cache your environments, `ToolshedEnvironment` is extremely expensive to create and should not be created more than once per system using them if possible.
- Avoid using the default environment for non-debug things, construct your own environment for your systems.
- Don't abuse reflection to obtain command types that're marked internal or private, **internal APIs are guaranteed to be unstable.**