# Forking Tips

A general set of forking tips and agreed upon best practices from fork devs. If you are a fork dev that would like to add something here please open a PR.

It is strongly recommended that you have some experience with SS14 and RT before creating your own fork.

This document only describes the technical considerations of forking. Keep in mind that any good fork will require an administration team and policies.

## Creating Your Repo

You should not create your project's repository with the github fork button. This is because github only permits one fork of a repo per account and forks of your repo will be counted the same as forks of your upstream. Additionally, when you have a repository forked via the fork button, it makes it very easy to send changes to your upstream by mistake. 

Instead, do the following:
- Create a blank repository, either as an organisation or in your user. Do not initialize the repo with an initial commit; leave it blank.
- git clone the repository of the upstream you wish to fork from (if you already have a local copy, then you can use that instead)
- `git remote add YourFork github.com/YourOrg/YourRepo` to add your blank repo as a remote
- git checkout your desired remote branch. If you're basing off Wizard's den, it is strongly recommended that you base your fork on stable.
    - `git fetch upstream stable` (assuming the remote pointing to the repository you wish to fork from is called upstream)
    - `git checkout upstream/stable`
- `git push YourFork master` to push that to your fork as the master branch.

Congratulations, you have successfully started a fork!

To update your fork in the future do as flows:
- Create a new branch based on the most recent commit of your fork
- git fetch your desired upstream branch as above
- Then git pull it.

Continuing with the example of mainline stable, the commands used for the above would be:
- `git fetch upstream stable`
- `git pull upstream stable`
- Fix merge conflicts if needed, and PR your fresh upstream merge branch
- If you do not want an upstream feature, now is the time to revert the change using `git revert`

Note that any contributors to your fork will need to press the github fork button on your repository instead of your upstream's.

## Licensing Your Fork

```admonish warning
The information written in this document should not be interpreted as, nor used as, legal advice.

MAKE SURE YOU READ AND UNDERSTAND THE LICENSE OF ALL FILES IN YOUR FORK.
```

If you are not well-versed with open-source software licenses, we recommend that you license your fork under the same license as your upstream. This will cause you the least amount of legal issues (or more likely, general controversy). Wizard's Den uses the "MIT License" (which is sometimes referred to as the Expat license). A copy of this license is already included in the repository and requires no action on your part to use. The MIT license grants you the right to do almost anything with the code (including sublicensing it) as long as a copy of the copyright notice is retained.

A _majority_ of art assets are licensed solely under the [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), or [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/). For the latter, NC means 'non-commercial': therefore, any assets licensed under it may **not** be used in commercial projects; you will either have to remove the assets, or have them be relicensed by the owner to allow commercial use.

Be aware when porting content from other forks that they may have more restrictive licenses like the GNU Affero General Public License (AGPL) or Mozilla Public License (MPL). Be careful to follow the restrictions imposed by those licenses.

The AGPL and MPL licenses are "copyleft" licenses, meaning they require any modifications of your code to be released under the same license. The AGPL requires the resulting binary of your project to be licensed under the AGPL which means every user is entitled to a copy of the *entire* source tree. This prevents you from having hidden content. AGPL code can be licensed in two different ways: AGPL-3.0-only, or AGPL-3.0-or-later. The difference between them is that AGPL-3.0-or-later code will be licensed under any future version of the AGPL that the Free Software Foundation publishes. The MPL has no "v2 only" option, your license will always be the latest version published by Mozilla.

The MPL only requires that files under the MPL license be released to users which makes it suitable for projects that include hidden content. Note that the MPL has an optional term called "Exhibit B". Code which is licensed under the MPL and the Exhibit B clause cannot be combined with code licensed under the AGPL.

Remember that this document provides a very brief overview of the licenses discussed. You should read the license of any files/code you intend to include in it's entirety and consult a lawyer if you have any questions.

## Organization
### Put your code in dedicated server folders.
A highly recommended pattern is to put your server's code (alongside an optional but recommended LICENSE file containing your code's software license) in its own top level folder within the major sections of the codebase.

For example, all of the `Content.*` folders would have a `_ServerNameHere` folder inside, in which all of your server specific code would go. Avoid mixing your own code with upstream's in that regard to avoid potential merge conflicts down the line.

### Namespace your components (and any other serializeable types)
All serializeable types are in the same global namespace. To prevent conflicts you should prefix them with a short identifier of your fork. For instance, if your server was called "Foo Bar" you might prefix all components with "FB". Keeping it short is advisable because you will be typing it a ton.

### Namespace your prototypes

In a similar vein to namespacing serializable types, prototypes also share a singular global namespace. Strongly consider giving all prototype names a prefix to avoid conflicts. For example one might give an entity the ID `FooMyEntity` instead of `MyEntity` if the shorthand of your server was "foo".

### Merge conflicts aren't that scary.
In short, when modifying existing code, conflict avoidance techniques are generally *bad* practice, as they often allow your code to continue compiling at the cost of it not actually working correctly anymore. In general if you get a merge conflict, it is not likely to be for no reason and you should review it manually instead of trying to incorporate avoidance techniques.

```admonish info
While this is mostly true, avoiding conflicts in, say, lists of elements, is generally a good idea (as they're going to conflict unnecessarily more often than not.)
This is usually as simple as just putting your entries at the start of the list, or in a separate part of the list separated by whitespace.
```

When modifying upstream code, it is recommended to leave a short comment explain *why* the change was made, so as to make upstream merges easier. An example of this would be `// FOOFORK: Changed Bar to 2 instead of 1 because everything breaks if it is 1.`

### Avoiding issues in shared enums.
A big example of this is the AdminLog enum containing all the kinds of admin logs. Pick a recognizable decimal (or hexadecimal) prefix, positive or negative, for your values, and stick to that. Ideally, pick one randomly, so you don't have issues merging other fork's changes if you want to cherry pick.

## CVars
### Namespace your CVars!
CVars can be as many tables deep as you want, for example `foo.respawn.time` is a valid CVar key and would map to the following:
```toml
[foo.respawn]
time = 360
```

This helps disambiguate where a CVar came from. Additionally, consider migrating any CVars you make significant changes to the behavior of (say, adding new UI layouts or changing the enum keys) to your prefix.

### Use your own `CVarDefs` instead of CCVars
The `CCVars` master class is something of an antipattern even upstream. You can declare new CVarDef classes anywhere you want, and put your CVars there instead of in CCVars.
For example:
```csharp
[CVarDefs]
public static class MySubsystemCVars
{
    /// <summary>
    ///     This is my CVar!
    /// </summary>
    public readonly static CVarDef<bool> MyCVar = CVarDef.Create("foofork.subtable.mycvar", false);
}
```

It may be advisable to have a CVarDefs per major subsystem, for example you'd put your world generation cvars in the same folder as the worldgen code itself. The name of the static class does not matter.

You **can** put a CVarDefs class in only the client or only the server, but be aware that this will result in the CVar being logged as missing if it winds up in a config file loaded by both sides.

### **DO** edit the defaults in code!
It's likely tempting to modify or introduce a config preset to modify CCVars defaults without editing the class itself. This kind of falls in line with [Merge conflicts aren't that scary.](#merge-conflicts-arent-that-scary), doing so leaves you open to upstream changing the default in a meaningful way (for example, changing what a number actually represents, like minutes to seconds or vice versa.) and getting stuck with a bug on production if it goes unnoticed.

The conflicts are trying to tell you something, if they happen.

### But don't make the defaults server-specific.
CCVars is not your server's config file, configure your server on your server in `server_config.toml`, not in the codebase. Change defaults if the default breaks the game, enables mechanics you want disabled, or breaks your design, not to set your discord link.

## Database Layout

EFCore is not really made to be used in the way that you will be using it as a fork developer, if you can avoid making DB changes you should. To avoid a number of bugs (most notably [this one](https://github.com/dotnet/efcore/issues/24834)) it is strongly recommended to not modify your upstream's tables. Instead, you should make a corresponding table for your fork's data that is in a one to one relationship with the original table.

Any migrations you add should be namespaced in the same way as prototypes and components. While the likelihood of a migration collision is basically nonexistent, it makes it clear which migrations were added by your fork.

Finally, make sure that you test your changes and migrations on both postgres and sqlite to avoid data loss. Remember to regularly take backups of your database.
