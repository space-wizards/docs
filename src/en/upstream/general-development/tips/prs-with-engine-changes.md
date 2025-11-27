# PRs With Engine Changes

The engine still has many areas to improve, so it's unavoidable that some some changes to content will require changes to the engine as well.

## Working in the submodule

The engine does not work on its own. Without a game like SS14 to provide content, the engine will not do anything. To be able to test and work on your changes it is thus recommended that you directly work on the engine submodule inside your SS14 repo.

If you are unfamiliar with **Git submodules**: Git submodules are basically just Git repositories, tracked inside other Git repositories. For example, SS14 has a submodule pointing to Robust. 

Because the submodule is still a fully fledged Git repositories, you can work out of it like any other repo: Make commits, branches, push, pull, etc... The parent repository tracks the currently checked out commit of the child submodule, and does not concern itself with anything else happening in the submodule.

First, you will need to fork the [engine](https://github.com/space-wizards/RobustToolbox). You can then change your git remotes inside the submodule so that you can work against your fork:

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

Second of all, you will need to disable submodule autoupdate. By default, the build system automatically updates the submodule (so that people who *don't* care to modify the engine don't have to manually run `git submodule update` constantly). This however gets in your way if you're trying to make changes to the engine, as it will constantly reset you to master! To disable this perhaps feature, put an empty file called "`DISABLE_SUBMODULE_AUTOUPDATE`" in the `BuildChecker/` folder at the root of the SS14 project (not inside `RobustToolbox/`). Also make sure it doesn't have a `.txt` at the end or something.

## Making the PR

When making your PR, you will want to make a separate PR in the engine repo and the main repo.

**Do not actually commit a change to the checked out submodule commit in your main content PR, you should just leave it as uncommitted while you develop it.** It's a constant cause of merge conflicts, and we will handle things when we merge.

### My build fails!

To have the build system use your engine changes when building your main PR, you need to put "Requires <PR>" in the PR message.

For example, if your engine PR is #1234, then your main PR message would be:

```
This is my PR that requires an engine change.

  * Broke something
  * Fixed something

Requires https://github.com/space-wizards/RobustToolbox/pull/1583
```

The supported formats can be found at https://github.com/space-wizards/submodule-dependency


## Guidelines for engine changes

Try to avoid any breaking changes that make future engine versions incompatible with old game versions. This isn't a massive problem due to how we version engine builds, but it still causes a very awkward updating dance when we try to update the submodule in content. Approaches like marking something `[Obsolete]` are far preferred to outright removing something when it isn't necessary anymore.