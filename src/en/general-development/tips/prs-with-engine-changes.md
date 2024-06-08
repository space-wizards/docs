# PRs With Engine Changes

The engine still has many areas to improve, so it's unavoidable that some changes to content will require changes to the engine as well.

This is more complicated than just making a change to Space Station 14 as the engine is a submodule and a separate repository.

## Why Submodules

The engine does not work on its own. Without a game like SS14 to provide content, the engine will not do anything. To be able to test and work on your changes it is thus recommended that you directly work on the engine submodule inside your SS14 repository.

If you are unfamiliar with _Git submodules_, they are basically just Git repositories, tracked inside other Git repositories. For example, SS14 has a submodule pointing to Robust.

Because the submodule is still a fully fledged Git repositories, you can work out of it like any other repository: Make commits, branches, push, pull, and so on...

The parent repository tracks the currently checked out commit of the child submodule, and does not concern itself with anything else happening in the submodule.

## Guidelines for engine changes

Try to avoid any breaking changes that make future engine versions incompatible with old game versions.

This isn't a massive problem due to how we version engine builds, but it still causes a very awkward updating dance when we try to update the submodule in content.

Approaches like marking something `[Obsolete]` are far preferred to outright removing something when it isn't necessary anymore.

## Working with Submodules

First, you will need to create a fork of the [engine](https://github.com/space-wizards/RobustToolbox). You can then change your git remotes inside the submodule so that you can work against your fork:

````admonish note title="Git Bash Directions" collapsible=true
```bash
# Go to branch master
git switch master
# Rename "origin" (the default remote, keeping track of space-wizards) to "upstream".
git remote rename origin upstream
# Add your own fork as "origin" remote.
git remote add origin https://github.com/<your username>/RobustToolbox.git
# Master will still track upstream (so you can just run git pull on it)
# and any branches you push to origin will go to your fork.
```
````

Next, you will need to disable submodule auto-update.

By default, the build system automatically updates the submodule (so that people who _don't_ care to modify the engine don't have to manually run `git submodule update` constantly). This however gets in your way if you're trying to make changes to the engine, as it will constantly reset you to master!

To disable this perhaps feature, put an empty file called "`DISABLE_SUBMODULE_AUTOUPDATE`" in the `BuildChecker/` folder at the root of the SS14 project (not inside `RobustToolbox/`). Also make sure it doesn't have a `.txt` at the end or something.

## Making the PR

When making your PR, you will want to make a separate PR in the engine repository _and_ the main SS14 repository.

```admonish danger
Do not actually commit a change to the checked out submodule commit in your main content PR, you should just leave it as uncommitted while you develop it

Doing that is a constant cause of merge conflicts, and we will handle things when we merge.
```

### Build Failures

Your build may fail because SS14's CI system doesn't know that it needs to include your changes to make it work.

To have the build system use your engine changes when building your main PR, you will need to put "`Requires <PR>`" in the PR message.

For example, if your engine PR is `#1234`, then your main PR message would be:

```md
This is my PR that requires an engine change.

- Broke something
- Fixed something

Requires https://github.com/space-wizards/RobustToolbox/pull/1583
```

The supported formats can be found at https://github.com/space-wizards/submodule-dependency
