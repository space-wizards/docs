# Testing unpublished engines against launcher

In some rare cases, you may have to test your engine changes against the launcher. The problem you'll run into is that the launcher makes it *rather annoying* to use anything other than official published engine versions. Luckily I recently made this easier!

Download [SS14.Launcher](https://github.com/space-wizards/SS14.Launcher) from GitHub, compile it, yada yada. You'll notice you have a very funny button when you run it:

![](../assets/engine-development/launcher-dev-menu.png)

Tick both checkboxes, then set the text box to the `release/` directory of the Robust you're working out of. This will make the launcher use exclusively local engine builds you've made, regardless of what server you connect to.

You can then run the packaging scripts in `Tools/` (`package_client_build.py` or `package_webview.py`) to fill the `release/` folder with the engine zip files you need. Every time you change the engine you'd just re-run the script and the launcher would pick it up next time.

Then you can just connect your launcher to your local server through the wonders of ACZ, and you'll be off!
