# Useful Tools

Collection of tools that are useful for maintainers.

~~~admonish info "Checking out someone else's PR"

```
[alias]
    pr = "!f() { git fetch -fu ${2:-upstream} refs/pull/$1/head:pr/$1 && git checkout pr/$1; }; f"
```

Put this somewhere into your `/.git/config` file.
Then use the console command `git pr 12345` to automatically pull that PR into a new branch named `pr/12345`.\
Alternatively use the [GitHub CLI](https://cli.github.com/), but you have to install that first.

To push changes to someone else's PR branch you can use the following command (example for adding me)
```
git remote add Slarti https://github.com/slarticodefast/space-station-14
git push Slarti <yourBranchName>:<theirBranchName>
```
For this to work the author has to select this checkmark when opening the PR, which is done by default:\
![](https://hedgedoc.spacestation14.com/uploads/6a9f9a32-e344-4c68-8f28-e18fa1d58e18.png)\
You can see on the right sidebar if they did:\
![](https://hedgedoc.spacestation14.com/uploads/cc6aaa68-11f3-4591-b73e-a45726670634.png)

If a PR only needs minor changes or a merge conflict fixed it is often easier and faster if you do this for the author, rather than wait for them to be addressed. Authors are often happy to see their PR is merged and it saves some maintainer time, so doing this is recommended.
~~~

~~~admonish info "GitHub Squash Reminder User Script"
Highly recommended is Myra's [GitHub Squash Reminder Userscript](https://github.com/VasilisThePikachu/GH-Squash-Reminder-Userscript/tree/master).\
It gives you a visual warning when you selected the wrong merge option by accident.\
![](https://hedgedoc.spacestation14.com/uploads/25eeda7c-c2c1-449d-9425-073c6756dd10.png)
~~~

~~~admonish info "GitHub Trollface Remover User Script"
GitHub has emojis, one of those is a trollface. [This userscript](https://cdn.replay.unstablefoundation.de/trollface-begone.user.js) removes trollfaces from GitHub with some optional functionality to replace the trollface with something else and it keeps track of how many were removed.
~~~