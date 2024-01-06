# Preprocessor Defines

Space Station 14 and Robust make decent use of [C# Preprocessor Directives](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/preprocessor-directives) for various things. For this document we're talking about `#if` and friends, to conditionally compile code differently based on specific settings.

This document aims to describe all preprocessor defines (what you can put in `#if`) declared by Robust.

## Most Common

* `DEBUG`: The game should be compiled with debug checks like `DebugTools.Assert()` enabled.
* `TOOLS`: The game should be compiled with development tools enabled.
* `RELEASE`: The game is being compiled on the [`Release` build configuration](./build-configurations.md). You generally should not need to check this, instead opt to check for `DEBUG` and `TOOLS` where applicable.

## The Gnarly Ones

You generally shouldn't need to look at these for content development, these are more engine stuff.

* `FULL_RELEASE`: Whether we are currently building for release that will be played by users. This is necessary to set up some code such as resources correctly in the final build.
* `DEVELOPMENT`: The opposite of `FULL_RELEASE`. Always true for local development, false for published releases.
* `WINDOWS`/`UNIX`/`LINUX`/`MACOS`: Whether we are compiling for specific platforms. In a lot of cases, `OperatingSystem.IsX()` checks at runtime are used instead, as conditional compilation can be convenient.
* `EXCEPTION_TOLERANCE`: Make the game more crash-resilient by inserting try-catch everywhere. The game is intentionally fragile on debug to encourage people to fix their bugs more.
* `CLIENT_SCRIPTING`: Whether to enable client-side C# Interactive. This is disabled for release builds due to security and size concerns.
* `USE_SYSTEM_SQLITE`: Whether to use the system's SQLite lib instead of the built-in `e_sqlite` lib. Used for FreeBSD.
