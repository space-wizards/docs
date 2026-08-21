# Versioning & Compatibility

This page describes how RobustToolbox is versioned and what backwards-compatibility guarantees we make.

## Version numbers

Robust follows a [SemVer](https://semver.org/)-ish system. Version numbers are normally in the form `major.minor.patch`, where the following generally holds:

* Major version changes mean some form of breaking change for games using RT.
* Minor version changes mean new features that are not directly a breaking change.
* Patch version changes are bug fixes or other minor stuff.

We also sometimes publish experimental versions of the engine marked with suffix strings like `1.2.3-pvstest`. These versions are intended for the use of testing things on specific live servers and are not held to any particular stability guarantees. As such, you should not be using these unless you're in talks with engine maintainers. Also yes the way we use these probably isn't semver compatible.

## Compatibility guarantees

### Major versions

There are no general guarantees between major versions. We will do our best to document any breaking changes, provide instructions for updating, and not create any more pain than necessary.

### Minor versions

Minor versions should not change existing behavior in any way beyond likely-compatible bug fixes.

We do not guarantee the following:

* ABI-level stability: recompiling games may be required.
    * This notably means we may do things like move types between projects, add parameters to overloads, modify behavior of source generators, etc.
* Game network compatibility: client and server must be on the same minor version.

### Patch versions

Patch versions should only contain bugfixes or other minor changes with no observable impact. They are generally network- and ABI-compatible between other patch versions on the same minor.

The launcher may roll client engine versions forward to a later patch version when necessary, for example to ensure compatibility with newer .NET versions.

