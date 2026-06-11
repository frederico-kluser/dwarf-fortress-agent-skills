# Utilities

> Fonte: [Utilities](https://dwarffortresswiki.org/index.php/Utilities) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A collection of third-party **Utilities** that are useful for *Dwarf Fortress* players and modders alike, of which this page serves as a list. *Dwarf Fortress* is a difficult game to play, and any help that can be had in the task is welcome help.

If you would like to add an article on a *specific* game utility to the wiki, please do so under the Utility namespace. Not included on this page: tileset repositories and graphics set repositories, due to having been given their own, separate pages. Mods have also been listed under their own Modification namespace.

To avoid namespace clutter, websites *are* considered utilities and have been included.

A subsection of the Bay12 forums is devoted to such third-party programs, and contains development threads for most of them.

## Game manipulation tools

### DFHack

DFHack is an advanced *Dwarf Fortress* memory access library and a set of tools and scripts using this library, providing direct object-oriented access to Dwarf Fortress's internals as if it were compiled into the game itself. Runs on Windows, macOS, and Linux (natively if supported by DF, or through Wine). The standard configuration enables a variety of included bugfixes and interface upgrades, and provides many useful tools such as "clean all". See main page for a summary of features, common use, and more.

- Links: Bay12 Forum Thread, Documentation, Releases, GitHub Repository, Steam page

### Dwarf Therapist

Dwarf Therapist gives you an advanced GUI to manage and check dwarf job allocations, military assignments, statistics (such as attributes, personality traits and happiness), sort dwarves by various criteria (e.g. profession, migration wave, happiness, number of assigned jobs etc.) and generally manage the Dwarven Resources of your fortress in a very convenient way. Available for Windows, Mac and GNU + Linux.

- Links: Bay12 Forum Thread, Releases, GitHub Repository, Manual (outdated)

## Legends tools

### LegendsViewer-Next

A web-browser-based multi-platform tool to browse the information in an exported legends file. It creates wiki style backlinks, searchable lists, interactive maps and family trees for historical figures. LegendsViewer-Next is a replacement for the classic Legends Viewer fully compatible with v50+ premium and classic. Builds for Windows, Linux and macOS are provided.

- Links: Bay12 Forum Thread, Github Repository

### Legends Browser

Another web-browser-based multi-platform legends information viewer (including using legends_plus.xml generated via DFHack) fully compatible with v50+ premium and classic.

- links: bay12forums

### DF Storyteller

Dwarf Fortress Storyteller (DF Storyteller, DF ST) is an application that parses *Dwarf Fortress* legends files, stores them internally and makes them queryable using API's. (Cross platform: Windows, Linux, macOS) This utility can be used to easily create new visualizers to view the legends data.

- links: Website, Gitlab project, list of visualizers can be found here. An example of a visualizer is The Bard created in DF ST.

## 3D Visualizers

### Stonesense

Stonesense is a third party visualizer, implemented as a DFHack plugin, that lets you view your fortress in a classic isometric perspective. It runs alongside *Dwarf Fortress*, and can follow the main game's view, updating in real-time. It is included in DFHack, and can be opened by typing `stonesense` or `ssense` into the console window.

- Links: Utility:Stonesense

### Vox Uristi

A tool that exports fortresses to a 3D voxel format (.vox). Once exported, rendering software such as MagicaVoxel (for Windows and Mac) or alternatively Goxel (for Linux) can make detailed 3D renders of it. It requires DFHack, and is mostly tested with the Steam version, though previous versions should work too.

- Links: Website, Bay12 Forum Thread

## Perfect World DF

A tool for creating custom world maps allowing highly customized world generation. Creates a world_gen.txt entry or file.

- Links: forum thread

## Music and Sounds

### SoundSense

SoundSense parses game logs and plays reacts to game events with sound effects, incidental music and dwarfy comments. Due to it being written in Java, Soundsense is portable to all platforms.

Note that older Soundsense users may have different default seasonal soundtracks, which were removed and replaced in early 2011. These are available here.

- Links: Website, Bay12 Forum Thread, Google Code Repository

### SoundCenSe

A C# port of SoundSense, it uses the existing sound pack files and XMLs present in SoundSense, but with some added enhancements. More information regarding what specific type of enhancements and how to install SoundCenSe can be gathered at the official forum thread. If problems emerge while trying to get SoundSense to work with the latest versions of Java, this port may prove to be a useful alternative.

- Links: Bay12 Forum Thread, Releases, GitHub Repository

### SoundSense-RS

A SoundSense alternative in Rust with a minimalistic GUI. Sound volumes can be adjusted realtime, based on channel. Events can be ignored with a custom list based on log patterns.

- Links: Bay12 Forum Thread, Releases, GitHub Repository

## Modding tools

### DF RAW Language server

Modding support for DF RAW files in IDE/Code/Text editors. Checks syntax of files, detects errors and syntax highlighting.

Current extensions:

- VS Code
- (more are coming)

-

  DF RAW Language server Logo

-

  DF RAW Language server in VSCode

-

  DF RAW Language server in VSCode

The Language server is a shared component that can be used to easily add support for more IDE's.

### Notepad++ Highlighting

language highlighting modes for the text editor Notepad++ link

## Modding tools pre v50

### Rubble

A useful plugin-based modding tool that generates raws and supports easy installation of reactions, tilesets, macros, modding fixes and DFHack scripts. It is a fork of the now abandoned Blast. Binaries are available for Linux 32-bits, OS X 32-bits and Windows 64-bits, as well as the source (written in Go with building instructions). As of 4.0, a GUI is available for Windows.

### PyDwarf

For players, PyDwarf is an easy way to manage and configure preferred mods in a way that avoids almost entirely the problems of outdated mods or incompatible groups of mods. For modders, PyDwarf's mod manager exposes a powerful Python API for interacting with raws and other data files.

### Raw Explorer

A tree-based raw files browser, editor and manager.

### Dwarf_RAW

A GUI for editing raw files, updated 2019.

### Dwarf Fortress real-life material helper

A Python script that generates raws based on custom real-life material values.

### Roses' Random Creature Script

A Python script that generates random creature raws.

### DF Diagnosipack

A collection of modding tools, with a focus on diagnosing problems and getting statistics on what is found within the raws. It includes:

- DF Duplisearch - checks your raws folder for duplicated objects, and counts the number of objects of each type (creature, entity, reaction, etc.).
- DF Creatureclasser - tells you what creature classes are in your raws, and what they are used for.
- DF CVunpack - unpacks creature variations, so you can see how the raws for e.g. wolf men really look (spoiler: they have 7 fingers).
- DF Creaturescale - calculates creature weights, and the proportions of each body part and tissue.
- DF Biomeviewer - shows what creature/plants can be found in which biomes.
- DF Rawminer - extracts procedurally generated raws (of Forgotten Beasts etc.) from save files.

## Remote playing tools

\

### Dfterm3

Dfterm3 is a remote *Dwarf Fortress*-playing software for multiple users through a web interface. DFterm3 enables play through a web interface, and games can also be viewed on mobile - or even played if a bluetooth keyboard is attached. The web interface should work with Chrome or Firefox browsers, but there are known problems using Internet Explorer. DFTerm3 functions via a DFHack plugin, and is thus dependent on each version of DFHack.

It is a successor to dfterm2, which functions similarly using telnet instead of a web browser. This utility only works with version 0.34.11 or earlier.

### Webfort

Playable in Mac browser.

A newer alternative to dfterm3 that functions similarly, but players must wait in a queue before assuming control for a given period of time. It also functions via a DFHack plugin. Binaries are available for Windows, as well as the source (written in C++). *(Note: main repo unmaintained. New repo last updated 5/22/2015.)*

### DorfServer

Like Twitch, without Twitch.

A remote SSH-based *Dwarf Fortress* host software. (repo)

### DFEverywhere

A utility that connects a locally-run *Dwarf Fortress* instance to a proprietary remote website, allowing remote browser-based play. *(Note: Main website no longer available. Client source here.)*

### Dwarf Fortress Remote

iOS app (paid) that allows one to play *Dwarf Fortress* remotely with native UI. A server can be set up at home, or on DigitalOcean, AWS or other hosting service.

### DFPlex

DFPlex is a plugin for DFHack which introduces simultaneous, real-time online co-op to fortress mode: each player has their own independent view, cursor, menus, etc. so nobody has to wrestle for control. It's a fork of webfort, so players join just by connecting from their web browser.

### Box64

Box64 allows *Dwarf Fortress* to be run locally on Android devices. A more detailed tutorial is available here.

## Language tools

\

### DFLang

A language creating tool.

### Toadese Language Utility

A language editing and translating tool.

### DFlangOpt

A little tool meant to prevent redundancy when importing or updating language files.

### Python language extraction and injection script

This simple script will extract words from language files and put them a word per line, for easy automatic translation or treatment. It can also read that list and put the translated words back in their place.

## Announcement tools

\

### DFMon

An announcement monitoring/filtering program, useful to hide some types of job cancellation spam or other more advanced filtering. Note that you can set the game to announce no job cancellations *without* any utilities or mods from the orders menu, with x.

### DF Announcement Filter

An alternative to DFMon written in Java (and thus portable to Linux and OS X).

### Announcement Window+

Announcement Window+ is a Python application that interfaces with *Dwarf Fortress* to print announcements and combat reports to a separate window. It was written to fix some annoying bugs that are present in DF Announcement Filter, which is no longer being updated.

One less game-pausing hotkey.

## Filesharing websites

\

### Dwarf Fortress File Depot

The Dwarf Fortress File Upload Service - an excellent place to store mods, community games, tilesets and other files. Courtesy of Janus; for files related to *Dwarf Fortress* only.

### Dwarf Fortress Map Archive

The Dwarf Fortress Map Archive is a large collection of user-submitted maps and videos and a nice flash viewer for perusing them. Maps are uploaded, stored, and downloaded in a special compressed format created by the DF Map Compressor; videos are stored in a compressed version of Toady One's own video-recording format.

Read more about the DF Map Archive on Markavian's User page.

## Launchers

Historically, starter packs were used to easily configure settings, keep the game up to date, and integrate third-party mods and bugfixes. With the release of v50 on Steam, much of this can be done in-game and through the Steam workshop, making starter packs no longer necessary.

### PyLNP

A cross-platform port of the Lazy Newb Pack, written in Python and providing some support for v50. See PyLNP: The modern cross platform launcher for more information.

- Links: Bay12 Forum Thread, Releases (for pack maintainers), GitHub Repository, Documentation

## Other/miscellaneous

\

### DF Map Compressor

Main program window.

The DF Map Compressor encodes multiple bitmaps exported from *Dwarf Fortress* into a single, very compressed, .fdf-map file. The fdf-map file can then be shared with your friends by uploading to the DF Map Archive.

### Exita

Exita is a Python program that takes your DF world map exports and dump them into several different text outputs.

### DwarfFamily

A tool that lets you import your legends XML file and converts all dwarf entries to a .GED file, which you can use in Family Tree programs like MyHeritage to display a family tree for the dwarves.

### Kobold name generator

A Python script that generates random names in the way of kobold utterances

### Dwarf Fortress News - Android App

Watches the *Dwarf Fortress* devblog. Receives Push Notifications on new updates.

### DF2HTML

Converts DF screenshots into formatted HTML.

\

## Calculators

### DFTools

A set of web-based utilities for mods, including calculators for temperature, time, and weapon damage.

### Dwarf Fortress Food and Booze Calculator

Web-based calculator for planning farm tiles, brewers, stills, and barrels needed to sustain a fortress by food type and population. Computes yields for all crops, brewing rates, and multi-year production scales.
