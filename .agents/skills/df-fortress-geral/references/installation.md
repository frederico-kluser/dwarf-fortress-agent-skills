# Installation

> Fonte: [Installation](https://dwarffortresswiki.org/index.php/Installation) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*Dwarf Fortress* is available as Premium and Classic versions. The installation process depends on the game version.

The *Premium version* is published on the Steam and itch.io platforms. Once bought, the game will automatically add to your game library and will handle like any other game on the platform.

The *Classic version* is freely available directly from the developers, Bay 12 Games. Simply download the latest version, extract its contents, and play.

Note that plans for a native MacOS build have been cancelled for the time being, but some people have gotten both the Steam and Classic version working through Wine. See below.

# Classic Download

**Download:** Linux · Windows · all versions · starter packs

*Dwarf Fortress Classic* is freely available directly from the developers, Bay 12 Games. Simply find the version that matches your operating system and click the link. You may be prompted to save an archive file, or your browser may save it to its configured downloads folder, do so and follow the installation instructions bellow.

The download linked at the top of the main page is a 64-bit version for Windows. "All versions" links to a page with additional choices depending on version, possibly including "small" builds for Windows (which lack sound files).

## DFHack and other third-party packages

The most prominent add-on to install for *Dwarf Fortress* is DFHack, which introduces a wide variety of interface improvements, bugfixes, and productivity tools. If you have installed *Dwarf Fortress* via Steam, you can also install DFHack from Steam. Players of other *Dwarf Fortress* distributions can download and install DFHack from DFHack's GitHub releases page.

If you have an older version of DF, you might be interested in the Lazy Newb Pack, which bundles a number of utilities and graphic sets (including DFHack). With recent (*50.01+*) versions of *Dwarf Fortress*, a Lazy Newb Pack is no longer needed.

There are also a wide variety of player-made mods available at the Dwarf Fortress Steam Workshop and the Bay 12 forums. If you don't have a Steam account, workshop mods can also be downloaded from Steam using the steamcmd commandline utility.

# Classic Installation

*Also see: System requirements*

## Windows

There is no installer for the game. Simply right-click the zip archive you downloaded and choose `Extract All...`, then choose a destination folder, and click `Extract` (or maybe `Unzip` or `Next` on older versions of Windows). By default Windows uses the name of the archive as the folder name, in the folder the archive is in, so something like `C:\Users\yourusername\Downloads\df_50_12_win`. You should change that to something like `C:\Users\yourusername\Desktop\Dwarf Fortress` or `C:\games\Dwarf Fortress`. After the files have been extracted, double-click the `Dwarf Fortress.exe` file within the folder you chose to start the game.

- Make sure to actually *extract* the archive; do not just double-click the archive and run the game from the window that appears. If you do this, then it may appear to work, but your save game data will get discarded - the cause of many "my saved games keep getting deleted" complaints.
- The game needs to be able to write to its own folder, choose a game folder your user has write access to without requiring administrator rights for example: your `Downloads` folder, `Desktop`, or `C:\games\..`; do **not** install it in `C:\Program Files\..` unless you know how to set up the correct permissions.

Troubleshooting:

- If you have an error stating that MSVCP140.dll or MSVCP140_ATOMIC_WAIT.dll is missing, it can be obtained by downloading the Visual C++ Redistributable for Visual Studio 2022.
- If Windows is set to scale the display, you may need to disable that for DF. Right-click the *Dwarf Fortress.exe* icon, select **Properties**, select the **Compatibility** tab, and then activate the **Disable display scaling on high DPI settings** (or **Override high DPI scaling behavior, scaling performed by: Application**) check box.[1]

Creating shortcuts:

- Right-click the `Dwarf Fortress.exe` file and choose any of `Pin to Start`, `Pin to taskbar`, or `Send To > Desktop (create shortcut)`. (The availability of these options may vary depending on the version of Windows.)

## Linux

*Dwarf Fortress* for Linux is expected to be run from a terminal (command-line) interface, and so the instructions here will assume you know how to log in and get to a command prompt. By default, however, *Dwarf Fortress* is a graphical desktop program (an X client), so you should be in a terminal emulator (inside an X session) before starting the game. *Dwarf Fortress* will create a new window outside of the terminal window by default, so don't worry about the size of the terminal.

**Downloading**: Either download it from the Dwarf Fortress Homepage with a web browser, or with the following terminal command, replacing "XX_YY" with the numbers in the desired *Dwarf Fortress* file version, found on the site:

    wget http://www.bay12games.com/dwarves/df_XX_YY_linux.tar.bz2

**Unpacking**: *Dwarf Fortress* is shipped as a (bzip2) compressed tar archive. Current builds will extract directly into the current directory, so create a new subdirectory in a suitable location (perhaps `~/games/df_linux`), `cd` to it, and then run

    tar -xjf /path/to/df_XX_YY_linux.tar.bz2

where /path/to/df_XX_YY_linux.tar.bz2 is the path and filename of the actual file you downloaded.

**Dependencies:** *Dwarf Fortress* requires at least the SDL2 and SDL2_image libraries. If you downloaded Classic or Itch builds of DF, these libraries are not included. To install these libraries, run the appropriate command for your distro:

- on Debian-based systems (e.g. Ubuntu/Linux Mint/Pop!\_OS):

    sudo apt install libsdl2-image-2.0-0

- on Fedora/CentOS, use one of the following depending on your package manager:

    sudo dnf install SDL SDL_image
    # or:
    sudo yum install SDL SDL_image

- on OpenSUSE:

    sudo zypper in libGLU1 libSDL_image-1_2-0

note: these lists may not be exhaustive.

**Running**: First, change to the new directory

    cd df_linux

then run the program.

    ./dwarfort

If you have DFHack installed, instead run

    ./dfhack

which will set up the console as a DFHack command terminal. The DFHack launcher also solves some issues with loading libraries that you may otherwise run into.

**Troubleshooting**:

Now you need to ensure that the required dependencies are installed. If you try to run the game and get errors about missing SDL_image libraries (etc.) then you need to install them. Use your distribution's package manager for this - details will be extremely distribution-specific. You don't need the development versions of the packages with the headers (although that won't hurt) - you just need the runtime versions, with the actual shared libraries.

If sound is not working for you, load the game through the DFHack launcher (`./dfhack`) or change the startup command to:

    LD_LIBRARY_PATH=. ./dwarfort

If you see any errors related to glibc when starting DF (for example, "version \`GLIBC_2.34' not found"), your version of Linux is too old and will need to be upgraded (e.g. Ubuntu 20.04 LTS is insufficient, but 22.04 LTS should work). Alternatively, you can try running the Windows version in Wine.

## MacOS

Although there is no native build, you can run Dwarf Fortress Premium version on a Mac through either Whisky or Wine. Whisky only works on Apple Silicon Macs, but is the preferred option if you are on Apple Silicon.

### via Whisky on Apple Silicon Macs

- Download the zip file for the lastest release of Whisky.
- Unzip the app and, optionally, move it to your /Applications/ folder.
- Open the Whisky app and verify in the Setup settings that Rosetta and "WhiskyWine" are installed and checked. (Versions of Whisky prior to v2.3.0 will have "GPTK" instead of "WhiskyWine".\[source\])
- Create your first bottle. Win10 will work fine.
- Click Bottle Configuration, then Open Wine Configuration. In the pane “Libraries”, add a new override:

    msvcp140_atomic_wait

- Download Steam for Windows installer on your Mac
- In Whisky click “Open C: Drive”, navigate to your Steam installation file, double-click the file and follow the instructions.
- You should be able to run Steam and log in. Install Dwarf Fortress and strike the earth!

You can install DF Hack through Steam too. If this fails (as it does for some) you can install it manually. Download the latest release from their GitHub. Unpack the zip and copy all files inside the DF Hack folder into your Dwarf Fortress folder. The DF folder can be found here: Library \> Containers \> Whisky \> Bottles \> (individual string of letters and numbers representing your bottle) \> drive_c \> Program Files (x86) \> Steam \> steamapps \> common \> Dwarf Fortress

For the Classic version follow the steps to create a Win10 bottle. Download the latest classic version from theDwarf Fortress website. Unpack the .zip file. Click “Open C: Drive” in Whisky and navigate to the unzipped classic version. Click Dwarf Fortress.exe to run the game.

### via Wine for older MacOS distributions

Wine needs Homebrew to be installed, which is a Mac OS packet manager. If you don't have any experience with this, it might seem a bit overwhelming at first, but you should be fine just following the step-by-step guide below. If you need help with Homebrew, you find plenty of tutorials on the web. You will also need to run Terminal, which is a build in App you can find and start through a search via Spotlight.

If you have Homebrew installed, you can open Terminal and paste the following for installing Wine through brew.

    brew install --cask --no-quarantine wine-stable

Be sure to consult the winehq website for the most up to date instructions. If you don't have brew installed, follow the instructions on brew's website before running the above command.

For the Classic version, download the Windows version available on the Dwarf Fortress website (see Classic Download for a direct download link). A .zip file named df_50_13_win.zip or similar should automatically download and extract itself in your Downloads folder. Open the folder, right click Dwarf Fortress.exe, click Open With and then click Wine Stable. If (default) appears next to this, you don't need to do this next time and you can just double click Dwarf Fortress.exe to run it.

For the Steam version, first the caveat that you shouldn't buy it with the expectation of it working on MacOS. It is *not* officially supported on MacOS and so if you don't have a Windows or Linux machine as a backup, then you risk not being able to play what you paid for in the future, even if it happens to work for some people today.

That aside, download the Windows version of Steam from Steam's website by clicking on the little Windows icon. Right click SteamSetup and Open With Wine Stable. It might take a minute, but it should pop up the installer. The default options Steam gives should be okay. Once you're able to log in to Steam, download Dwarf Fortress from Steam like you would on Windows. You should be able to run Dwarf Fortress afterwards.

Opening the Wine version of Steam again after closing it is a bit more tricky. Open Finder and press shift command G or click Go \> Go to folder. Paste `~/.wine/drive_c/Program Files (x86)/Steam` into the prompt and press enter. You can then click steam.exe to run Steam again, or click steamapps \> common \> Dwarf Fortress to backup your saves and run Steam Dwarf Fortress directly by opening it with Wine.

Creating shortcuts:

- Right-click the `Dwarf Fortress.exe` file and choose `Make alias`. It should make a file in the same folder called Dwarf Fortress.exe alias. You can rename it and move it wherever you want. You can also make aliases for the Steam and Dwarf Fortress folders, so you don't have to find the hidden Windows files through Finder again.

# Documentation

Fortunately, the documentation on this wiki is very detailed and extensive. You may want to start out with:

- Tutorials
- Fortress Mode Quickstart Guide
- Adventure Mode Quickstart Guide

Then move on to:

- Fortress Mode reference
- Adventure Mode reference
- Searching the wiki

DFHack has its own documentation site:

- DFHack docs

**Getting Started**

About - Installation - Tutorials - FAQ

Fortress Mode Quickstart Guide - Adventure Mode Quickstart Guide

Fortress Mode Reference - Adventurer Mode Reference (Quick Reference)

How do I get more help?
