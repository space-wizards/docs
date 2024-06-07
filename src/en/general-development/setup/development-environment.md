# Development Environment

A local development environment is required to be able to build and develop on top of Space Station 14.

This guide provides step-by-step instructions to configure your development environment, allowing you to contribute to the SS14 codebase and the RobustToolbox Engine.

```admonish warning
Please do not skip around this guide, even if you're an experienced programmer. Skipping steps may lead to unforseen bugs and issues.
```

## Prerequisites

Before you can really set anything up, ensure that you have the following software installed on your system:

1. [**Git**](https://git-scm.com)  
   This is SS14's version control system.
   Refer to [Git for the SS14 Developer](./git-for-the-ss14-developer.md) on how to set it up and its basics.
   If you are looking for a Git GUI, you can use the one built-in to your IDE or the [many others](https://git-scm.com/downloads/guis).
2. [**Python 3.7 or higher**](https://www.python.org/)  
   This is used for many development scripts.
   **Only download this from the Python website and not the Microsoft Store.**
   Make sure `py launcher` option is enabled.
3. [.**NET 8.0 SDK**](https://dotnet.microsoft.com/download/dotnet/8.0)  
   This is used for building and developing C#, which is the programming language SS14 is built in. If you have installed Visual Studio, you probably already have this installed.

```admonish note
Make sure that all the software you downloaded is added to your `PATH`, otherwise you will not be able to run it.
- [Git](../../assets/images/setup/git-path.png)
- [Pyhon](../../assets/images/setup/python-path.png)
```

```admonish tip
If you are using an M-Series/Arm Mac, make sure you install `x64 .NET`, **not** `Arm64 .NET`.

RobustToolbox does not currently support Arm64, so using Rosetta 2 emulation is recommended.
```

```admonish note title="NixOS Directions" collapsible=true
If you're running on Nix/NixOS and have [flakes set up](https://nixos.wiki/wiki/flakes), you can just run `nix develop` and all of the project dependencies will be managed for you.

If you want to use Jetbrains Rider with it, run `NIXPKGS_ALLOW_UNFREE=1 nix shell nixpkgs#jetbrains.rider --impure` which creates a new shell. Then, run `nohup rider >/dev/null 2>&1 &`, and you now have your whole development environment set up (except the submodules, haha).

```

## 1. Cloning the Repository

To develop [Space Station 14](https://github.com/space-wizards/space-station-14), you first need a local copy of all the code on your machine to develop on.

- If you're familiar with Git, follow the standard procedures for forking, cloning, setting up remotes.
- For those new to Git, refer to the [Git for the SS14 Developer](./git-for-the-ss14-developer.md) for a comprehensive guide on setting up Git and the basics.

## 2. Setting up Submodules

Space Station 14 uses Git Submodules to manage its dependancy on the RobustToolbox engine. Without the submodule, you cannot build Space Station 14.

Here are the steps to set them up (using our automated submodule handler):

1. After you first clone the repository, run `RUN_THIS.py` (idealy run in a terminal like `python3 RUN_THIS.py`) found at the root of the repository using Python. If you have any issues, refer to the [troubleshooting section](#troubleshooting).

2. Verify it has succeeded by checking for `/RobustToolbox` directory with in files in it.

```admonish tip
If you actually want to modify the engine code or otherwise want to manually update submodules, create a file called `DISABLE_SUBMODULE_AUTOUPDATE` inside the `/BuildChecker/` directory.
```

## 3. Setting Up an IDE

An Integrated Development Environment (IDE) is highly recommended for Space Station 14 development.

Here are the most popular options:

- For **Windows**
  - [Visual Studio 2022 Community](https://visualstudio.microsoft.com/) is a widely used choice. During installation, ensure you select the ".NET desktop development workload" and related C# development components.
- For **all platforms** (**Paid**)
  - [Jetbrains Rider](https://www.jetbrains.com/rider/) is the most used outside of Windows. College/University students can obtain [free educational licenses](ttps://www.jetbrains.com/community/education/#students).
- For **all platforms** (**Free**)
  - [VSCode](https://code.visualstudio.com/) or [VSCodium](https://vscodium.com/) can be used alongisde thier respective C# extensions. However, they will provide a less comprehensive development experience compared to full-fledged IDEs and you won't get as much help.

### 3.A. Installing the IDE

To actually use an IDE, you must install it. If you already have an IDE of your choice installed, feel free to skip straight to [Configuring Build Options](#3b-configuring-build-options).

#### Visual Studio

```admonish info title="Visual Studio Directions" collapsible=true

Follow the [official guide](https://learn.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2022).

```

#### Jetbrains Rider

```admonish info title="Jetbrains Rider Directions" collapsible=true

Follow the [official guide](https://www.jetbrains.com/help/rider/Installation_guide.html).

```

#### VSCode

```admonish info title="VSCode Directions" collapsible=true

Follow the [official guide](https://code.visualstudio.com/docs/csharp/get-started).

```

#### VSCodium

```admonish info title="VSCodium Directions" collapsible=true

1. Download [VSCodium](https://vscodium.com/#install).
2. Run the installer.
3. Once installed, download the C# extension by Muhammad-Sammy, with the extension ID `muhammad-sammy.csharp` and 70k downloads.

```

### 3.B. Configuring Build Options

What you think of as Space Station 14 is actually 2 (well, the only two we care about here) are `Content.Client` and `Content.Server`. In order for the client to be tested, you must also be running a local server.

Thus, make sure that when your IDE is running SS14 or is trying to debug it, it is running both at the same time.

#### Visual Studio

```admonish info title="Visual Studio Directions" collapsible=true
1. Right click `Solution`
2. Select `Configure StartUp Projects...`
3. Select `Multiple StartUp Projects`
4. Set the action for `Content.Client` and `Content.Server` to `Start`.
5. Press `Apply`.

Now, if you click the `Start` button, both the client and the server should both launch at the same time.

If you are having problems with the program not getting build correctly, you may need to set it to always build before run.

1. Go to `Options`
2. Go to `Projects`
3. Go to `Solutions/Build and Run`
4. Change `On Run when projects are out of date` to `Always build`.
```

#### Jetbrains Rider

```admonish info title="Jetbrains Rider Directions" collapsible=true

In Rider you can create a “compound configuration” to run or debug both client and server at the same time.

![](../../assets/images/setup-rider-configurations.png)

```

#### VSCode(ium)

```admonish info title="VSCode(ium) Directions" collapsible=true

The C# extension provides a `"coreclr"` launch type which can be used to run the `Content.Server` and `Content.Client` assemblies.

Alternatively, a [compound launch configuration](https://code.visualstudio.com/Docs/editor/debugging#_compound-launch-configurations) can be used to run the server and client at the same time.

```

### 3.C. Configuring IDE Directories

C# IDEs like Visual Studio and Rider do not automatically show the `/Resources/` folder in the project.

This folder contains all the non-C# files such as sprites, audio, and most importantly, YAML prototypes. If you are not able to view or edit the `/Resources/` folder, you will be unable to develop for Space Station 14.

#### Visual Studio

```admonish info title="Visual Studio Directions" collapsible=true

In Visual Studio, you can switch the Solution Explorer from “solution” view (only showing the C# projects) to “folder” view (showing all the files in the project).

1. Press the button to switch views as follows, then select the folder view:

![](../../assets/images/setup/vs-solution-explorer-switch-view-1.png)
![](../../assets/images/setup/vs-solution-explorer-switch-view-2.png)

2. After this, the Solution Explorer should look something like this, and you should be able to easily access the Resources folder:

![](../../assets/images/setup/vs-solution-explorer-switch-view-3.png)

```

#### Jetbrains Rider

```admonish info title="Jetbrains Rider Directions" collapsible=true

In Rider, you can "attach" the resources directory to the solution.

1. Right click the solution in the explorer
2. Click doing "Add" -> "Existing Folder...".
3. Select the "Resources" directory in the file picker.

![](../../assets/images/setup/rider-attach-folder-1.png)
![](../../assets/images/setup/rider-attach-folder-2.png)

After this, your solution view should look something like this, and you should be able to easily access the `/Resources` folder:

![](../../assets/images/setup/rider-attach-folder-3.png)

```

## 4. Starting SS14

With all of that setup, you can now get on with compiling and running the client and the server!

If you have an IDE and have set it up following this guide, you should just be able to click run and it should work!

If you are compiling without an IDE, you must:

1. Build the project through `dotnet build` in the root of the repository.
2. To start the server, run `dotnet run --project Content.Server`.
3. To start the client, run `dotnet run --project Content.client`.

```admonish tip
Both these commands use a debug configuration by default.

To enable release optimizations, add `--configuration Release` to the dotnet invocation.

```


# Troubleshooting

### `RUN_THIS.py` Isn't Running

Make sure that the version of Python that you are using is installed from the website and not the Microsoft store. If you installed it from the Microsoft store, uninstall it and install Python from the website.

If you are on Windows and get redirected to the Microsoft Store or encounter a message in your terminal claiming that Python is not installed, then you need to disable an aweful Microsoft shortcut. You can disable it by searching for `Manage App Execution Aliases` and disabling the two Python references.

### Missing Submodule Files

If you ever start missing files from the submodules, it's recommended to run `git submodule update --init --recursive` in a terminal in case something went wrong in the Python.

### `py` Not Found

If Python was correctly installed from the website and the `python` command works but still get this error, then check if `C:/WINDOWS/py.exe` works.

If it does work, add `C:/WINDOWS` to your path.

### Unable to load DLL "`freetype6`"

If you get the following error, then you need to uninstall `.NET Core SDK x86` and instead install `.NET Core SDK x64`.

```

Unhandled exception. Robust.Shared.IoC.Exceptions.ImplementationConstructorException: Robust.Client.Graphics.FontManager threw an exception inside its constructor.
 ---> System.DllNotFoundException: Unable to load DLL 'freetype6' or one of its dependencies: The specified module could not be found. (0x8007007E)
   at SharpFont.FT.FT_Init_FreeType(IntPtr& alibrary)
   at SharpFont.Library..ctor()
   ... Truncated ...

```

### `libssl` Not Found

If you’re having problems with dotnet not finding `libssl` (e.g. when using `libressl`), try setting the `CLR_OPENSSL_VERSION_OVERRIDE` environment variable to the appropriate version.

For instance, set it to 48 if your `/usr/lib` contains `libssl.so.48`. If that doesn’t work you can also try running `ln -s /usr/lib/libssl.so /usr/local/lib/libssl.so.1.0.0` instead.

### Client/Server Aren't Available in Visual Studio

This may be because you opened the project as a folder rather than a solution.

Make sure you open it as a solution and click the `SpaceStation14.sln` file.

### System Cannot Find File `RUN_THIS.py`

The system cannot find the specified file error usually means that OneDrive is conflicting with the git repository.
Clone the git repo outside of OneDrive or disable syncing for the cloned folder.
