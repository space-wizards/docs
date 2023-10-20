# Setting up a Development Environment

First you're gonna need some software:

* [Git](https://git-scm.com/) or one of the [many](https://www.sourcetreeapp.com/) [third-party](http://www.syntevo.com/smartgit/) [UIs](https://tortoisegit.org/) that make it easier to use. Make sure to let it install to your PATH like [this](https://cdn.discordapp.com/attachments/560845886263918612/861267188971470898/unknown.png).
* [Python 3.7 or higher](https://www.python.org/). Make sure to install it into your [PATH on Windows](https://cdn.discordapp.com/attachments/560845886263918612/1147634791148179457/image.png). You should get python from [python.org](https://www.python.org/). Versions installed from the windows store sometimes cause build issues.
* [.NET 7.0 SDK or greater](https://dotnet.microsoft.com/download). Visual Studio also installs this if you're on Windows.
  * ARM (M1) Mac users: You need to make sure to install x64 .NET, **not** ARM .NET. The engine does not currently run natively on Mac ARM so using x64 via Rosetta 2 emulation is recommended. 
* Preferably an IDE to make development not painful (all free options unless otherwise noted):
  * For **Windows**, [Visual Studio 2022 **Community**](https://www.visualstudio.com/). For a minimal install (Jesus it's large) you're gonna want the .NET desktop development workload, the C# compiler, C# support, NuGet package manager, MSBuild and .NET 7 SDK or something along those lines.
  * For **macOS**, [Visual Studio for Mac](https://docs.microsoft.com/en-us/visualstudio/mac/).
  * For **all platforms**, (NOT FREE) [Rider](https://www.jetbrains.com/rider/) is one of the best IDEs available, and many SS14 devs prefer it over Visual Studio. College/University students can get a free education license, even if they're not a computer science major.
  * For **all platforms**, [Visual Studio Code](https://code.visualstudio.com/) with the C# extension. Usually an inferior IDE experience than full blown IDEs like regular Visual Studio, but some experienced programmers enjoy the minimalism.
  * For **all platforms**, [VSCodium](https://vscodium.com/) with the C# extension. Open source and without the bloat and tracking of VSCode.

## 1. Cloning

**Even if you already know Git, scroll down to read the section about submodule setup. Seriously.**

If you're **familiar with Git**, just fork and clone the repository, set up remotes, and then follow the submodule guide below.

If you're **unfamiliar with Git**, or just don't know how to proceed, follow the [Git for the SS14 Developer](./git-for-the-ss14-developer.md) guide, which goes in depth on how to contribute to the game and how to set up your initial repository. It also touches on submodule setup, but that's included here as well because of its importance.

## 2. Submodule Setup

We have an automatic submodule updater so you don't have to worry about running `git submodule update --init --recursive` all the time. 

Run `RUN_THIS.py` inside the repo you downloaded with Python. Preferably from a terminal too. This should take a few seconds so if it instantly stops then check if you are running Python 3.7+ otherwise keep reading.

**If running `RUN_THIS.py` immediately opens and closes a window: do not worry.** This does not mean that it failed. The script closes automatically upon completion, so if you want to verify that it worked properly, check the submodule `/RobustToolbox/` and verify that all the files are there. If not try checking out the troubleshooting at the bottom of this page.

Note: If you have any issues when getting started with missing files it's recommended you run `git submodule update --init --recursive` by hand once in case something went wrong with python.

If you *do* want to modify the engine directly however, or you want to update the submodule manually (the auto updating can be a pain), make a file called `DISABLE_SUBMODULE_AUTOUPDATE` inside the `BuildChecker/` directory. 

And with that, your repo is now properly setup!

## 3. Setup an IDE

### Visual Studio

1. Download Visual Studio Community (if you don't own a paid version) from here https://visualstudio.microsoft.com/vs/community/
2. Run the installer and choose `.net desktop development`, then install
3. If the installer asks you for a development environment select `Visual C#`.
4. Open Visual Studio
5. Select `Open a project or solution`, then navigate to your cloned repository from above and open `SpaceStation14.sln`

### Jetbrains Rider
* TODO

### VSCodium
1. Download [VSCodium Here](https://vscodium.com/) or more directly [on Github Here](https://github.com/VSCodium/vscodium/releases) (On the latest release, click the assets dropdown then scroll to the ZIP or .exe for your OS).
2. Run the installer or extract the zip file to a location of your choice and run the .exe once extracted.
3. Once installed, navigate to the Extensions tab (part way down on the top left corner bar, looks like 4 tiles) and search for "C#". An extension by "Muhammad-Sammy" with over 70K downloads and a green / white logo is the one, install that. Extension ID `muhammad-sammy.csharp`.
4. Select File > Open Folder, then navigate to your cloned repository from above and open this full folder.
5. Now you can run and debug your game. Select the icon above "Extensions" from earlier for "Run and Debug" and from the dropdown next to the green play button you can select "Server/Client". This will run both the client and server, opening the game for you to debug. Relevant information will pop up in the debug along the bottom. Select the processes in the call stack on the left to change what you are debugging.

## 4. Starting SS14

Now you can get on to compiling the client and server! Use your flavor of IDE to open the solution file `SpaceStation14.sln` and press the build button.

To compile without an IDE, run `dotnet build` in the Space Station 14 repo directory. Then, call the following commands to run the client and server.
* `dotnet run --project Content.Server`
* `dotnet run --project Content.Client`

Both these commands use a debug configuration by default. To enable release optimizations, add `--configuration Release` to the dotnet invocation.
 
Note: If you're having problems with dotnet not finding libssl (e.g. when using libressl), try setting the `CLR_OPENSSL_VERSION_OVERRIDE` environment variable to the appropriate version. For instance, set it to `48` if your `/usr/lib` contains `libssl.so.48`.
If that doesn't work you can also try running `ln -s /usr/lib/libssl.so /usr/local/lib/libssl.so.1.0.0` instead.

## 5. Configuring Build Options

The SS14 client and server are independent projects, but both can launch with a single button somewhere in your IDE. This needs to be set up, however. Note: **It is recommended that you run `Content.Client` and `Content.Server` when developing from your IDE.** *Not* `Robust.Client` or `Robust.Server`. The reason is that running `Content.*` will make your IDE aware of dependencies correctly and ensure everything is rebuilt nicely. If you run `Robust.Client` directly you have to make sure the solution is fully built every time which is annoying and easy to forget. If you're unsure what Robust or Content are, check out [this page](../codebase-info/codebase-organization.md) on how the project is organized.

### Visual Studio 2022

In Visual Studio 2022, you can configure the build button to run both the server and client by right clicking the solution, then selecting `Configure StartUp Projects...`. Once the menu pops up, then select `Multiple startup projects:` and set the action for `Content.Client` and `Content.Server` to `Start`. Once you apply the changes, hitting the big `Start` button with a green arrow next to it should launch both client and server at the same time.

Note: If you're having problems with the program not getting built right, you may need to set always build before run. Go to Options `Projects and Solutions/Build and Run` and change `On Run, when projects are out of date` to `Always build`.

In VS you can also use the keys F7 to build the project and F5 to run it.

### Visual Studio Code

The C# extension provides a `"coreclr"` launch type which can be used to run the `Content.Server` and `Content.Client` executables in their respective `bin/` directories. A [compound launch configuration](https://code.visualstudio.com/Docs/editor/debugging#_compound-launch-configurations) can be used to run the server and client at the same time.

### Command Line

Build with `dotnet build` and run the client and server on different command lines with:

* `dotnet run --project Content.Server`
* `dotnet run --project Content.Client`

There's also definitely some way to run two commands at the same time, but you should probably google it.

### JetBrains Rider

In Rider you can create a "compound configuration" to run or debug both client and server at the same time. Quite convenient!

![](../../assets/images/setup-rider-configurations.png)

# Miscellaneous IDE setup

## JetBrains Rider
In Rider you can attach the resources directory to the solution so that you can more easily navigate to resource files like prototypes.

![](../../assets/images/setup-rider-attach-existing-folder.png)


# Troubleshooting

Make sure the first three items on top are downloaded.

## `RUN_THIS.py` not running
Check that python is installed from the website and not the Microsoft Store. If it's installed from the Microsoft Store, uninstall it then download and install from the python website.

If you are on Windows and get redirected to the Microsoft Store or encounter a message in your terminal claiming that Python is not installed. This issue may be caused by a stupid Microsoft shortcut. Which you can disable by searching for `Manage App Execution Aliases` and disabling the two python references

## System.DllNotFoundException: Unable to load DLL 'freetype6' or one of its dependencies: The specified module could not be found.

```PS C:\Users\Larme\Downloads\space-station-14> dotnet run --project Content.Client
Unhandled exception. Robust.Shared.IoC.Exceptions.ImplementationConstructorException: Robust.Client.Graphics.FontManager threw an exception inside its constructor.
 ---> System.DllNotFoundException: Unable to load DLL 'freetype6' or one of its dependencies: The specified module could not be found. (0x8007007E)
   at SharpFont.FT.FT_Init_FreeType(IntPtr& alibrary)
   at SharpFont.Library..ctor()
   at Robust.Client.Graphics.FontManager..ctor(IClyde clyde) in C:\Users\Larme\Downloads\space-station-14\RobustToolbox\Robust.Client\Graphics\FontManager.cs:line 33
   --- End of inner exception stack trace ---
   at Robust.Shared.IoC.DependencyCollection.BuildGraph() in C:\Users\Larme\Downloads\space-station-14\RobustToolbox\Robust.Shared\IoC\DependencyCollection.cs:line 348
   at Robust.Shared.IoC.IoCManager.BuildGraph() in C:\Users\Larme\Downloads\space-station-14\RobustToolbox\Robust.Shared\IoC\IoCManager.cs:line 271
   at Robust.Client.GameController.InitIoC(DisplayMode mode) in C:\Users\Larme\Downloads\space-station-14\RobustToolbox\Robust.Client\GameController\GameController.IoC.cs:line 16
   at Robust.Client.GameController.ParsedMain(CommandLineArgs args, Boolean contentStart, IMainArgs loaderArgs, GameControllerOptions options) in C:\Users\Larme\Downloads\space-station-14\RobustToolbox\Robust.Client\GameController\GameController.Standalone.cs:line 49
```

Uninstall .NET Core SDK x86. Install .NET Core SDK x64.


## The client and server aren't available in Visual Studio to configure in Multiple startup projects

This may be because you opened the project as a folder rather than a solution. Make sure you open it as a solution and click the space station 14 .sln file. 
