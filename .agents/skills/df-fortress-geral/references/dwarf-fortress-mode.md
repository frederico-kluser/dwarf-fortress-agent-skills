# Dwarf fortress mode

> Fonte: [Dwarf fortress mode](https://dwarffortresswiki.org/index.php/Dwarf_fortress_mode) — Dwarf Fortress Wiki (GFDL/MIT)

*This is a detailed reference guide. For a beginner tutorial, see Quickstart guide, see further tutorials.*

*Modding is not covered on this page.*

**Fortress mode** is the most popular of three modes in *Dwarf Fortress*, with the other two being Adventurer mode and Legends mode, often the mode implied when one talks about *Dwarf Fortress*. Fortress mode is a construction and management simulation of a colony of dwarves. In fortress mode, you pick an embark location, and then assign your seven initial dwarves some starting  skills, equipment, provisions, and perhaps, animals to bring along. After preparations are complete and your hardy explorers embark, they'll be faced with the fortress site you picked down to every little detail; from geologically appropriate stone types, to roaring waterfalls, to, for example, ornery  hippopotami. Rather than control individual dwarves, you design everything, and your dwarves will go about implementing your designs on their own.

## Goals

Fortress mode is considered a construction and management simulation game. This entails that few goals are imposed upon the player by the game.

The most apparent goal is survival, as your endeavors at the chosen site will, for the moment, end if the last dwarf dies. With this comes the need to keep your dwarves happy, as unhappy dwarves will cultivate some very unhealthy (yet surprisingly Fun) habits like murdering their colleagues.

Another goal of sorts, programmed into the game, is creating a fortress that attracts the king/queen of your civilization. Therefore players typically, but by no means necessarily, choose to expand into a thriving community with skilled workers, battle-ready warriors and nobles, creating ridiculous amounts of wealth like fine crafts, excellent armor, valuable furniture, decorated with precious gems, all the while protecting them from foes with deadly traps and a trained military. Avoiding imminent death also requires providing the dwarves with plenty of food and alcohol, by way of farms above and below ground, while clothing from leather or cloth will keep them happy.

Of course, every dwarf loves precious metals, but the only way to find them is to dig. Make sure you don't delve too greedily and too deep, for many creatures dwell in the caverns below...

## The world

To play *Dwarf Fortress* in fortress mode, you must generate a world that includes a dwarven civilization - see World generation for detailed instructions. After at least one world has been generated, you will be able to start the game. Only one game may be going on in a world at the same time.

### Geographic features / Inhabitants / History

The main features of a world are biomes on the surface and stone layers underground, some of which may contain aquifers. Other surface features that are significant, but which aren't biomes, strictly speaking, are rivers, volcanoes, and caves. There are also caverns and magma seas everywhere underground which your dwarves will most likely encounter, but you can't see these on the world map, or on the local map, for that matter, until you dig into them. There may also be other Fun things underground that you can't see. You will have to find these on your own, if they exist.

Every playable world will be inhabited by various creatures, civilizations, night creatures, and megabeasts (including titans and forgotten beasts) in addition to your dwarves. You may encounter all of these types of inhabitants at some point in the form of wildlife, invaders, or rampaging forces of nature.

Given that your world includes creatures and civilizations capable of independent action, it also has a history that is viewable in legends mode, historical events showing up in engravings and other artwork created by your dwarves. Historical dates are expressed in terms of the dwarven calendar.

You will also be making history as events occur in your fortress, and these events will be recorded for all time in the annals of your world, even if you'd rather that they not be. These events may later become the subject of various engravings and decorations created by your dwarves, or those in a later fortress.

## Embarking

*See also: Reclaim fortress mode*

Before starting to build a fortress, you must choose the embark location in the world, then assign skills and supplies to the seven dwarves on the expedition team you will embark with into that environment. This is the embarking process, and is a major subject on its own - see the Embark guide for all the details. Also see Starting build for more information on outfitting your expedition. After you embark, the real game begins.

## Gameplay user interface

Your main view of the in-game world is a top-down view of a multi-layered environment. You can move your view in the four main cardinal directions as well as up and down Z-levels (elevation) to see different layers. There is also a command menu that lets you issue commands that your dutiful dwarves will attempt to follow.

This section covers most of the screens and user interface elements used after embarking, at least in brief. It does not necessarily tell you how to accomplish every task you might need to, but instead just describes what you see on the screen and what various keystrokes do.

Later sections in this document and *many* other articles on this wiki help you tie all of this together by describing the sequence of actions needed to accomplish various things in the game; see Menu for a more detailed reference for the UI itself.

### Common UI concepts

### Pausing and resuming

[TABLE]

Entering all menus (except the quads menu) will automatically pause the game, but if you want to pause or unpause the game without entering a menu use . You will see appear in the upper left corner of the window when the game is paused. Certain announcements will also pause the game automatically and you will have to unpause it manually to proceed.

### Main screen

[TABLE]

The screen at the top level of the user interface hierarchy consists of the **main map**, a **command window**, and an **overview mini-map** area along with a few **status indicators** around the edge. While the main map is always visible at the top level of the UI, you can use the key to show and hide the command window and overview map areas, giving you more space to view the main map if desired.

### Options screen

[TABLE]

Assuming you are at the top level of the user interface looking at the map, you can hit to enter the options menu.

- – Exits the options menu. You can also just press .

- – Saves the game, unloads the fortress, and returns to the main menu screen. There is no "save and continue" option, but saves can be backed up and reloaded.

- – Screen for changing the Key bindings.

- – Exports selected levels of your map as .BMP files (for use on such things as the Dwarf Fortress Map Archive), world generation parameters, and some limited world information to the main *Dwarf Fortress* folder.

- – Volume control for the Music.

- – Like except it ends your control of the fort, giving limited control to the game. Most of the fortress remains as is, with citizens, livestock, and most items continuing to exist. Not always available, such as during sieges. After it saves and returns to the main menu you may start a new game in any mode including to unretire the fortress.

- (or ) – This permanently abandons the fortress, saves the map to the world's data files for later use, and returns to the main menu. Once you abandon a fort, all of your dwarves leave the site, all of your livestock dies, and all items including corpses will be scattered around the map before it is saved. This is how you "give up" on a fortress. You might later reclaim the fortress with a new group of dwarves or visit it with an adventurer in Adventurer mode.

Notably lacking is an "exit without save" option. Players who wish to quit and leave their previous save unchanged may manually kill the *Dwarf Fortress* process in the system task manager, or by using the \`die\` command in DFHack. **Do not** attempt this while saving, as your save folder will become corrupted. Alternatively, you can make a copy of your region folder in the *data/save* folder before saving, save the game normally, then delete and replace the region folder with the copy.

### Main map

[TABLE]

The main map window is what you will be looking at for the majority of the time. This is where all of the action happens.

While the play area itself is three-dimensional, the window is not; you can only view one Z-level at a time. You can change which Z-Level is currently displayed using and .

On the far right side of the screen is the **depth bar** showing you the approximate depth, below or above ground, of the current Z-level that the map is displaying. This indicator is relative to the surface, so it will change if you move the map around an area with a non-flat surface, even if you don't press or .

#### Map cursor

[TABLE]

After entering a command that involves the map cursor (), you can use as well as the numeric keypad keys to move the cursor around in all eight directions. If you hold while pressing one of these, the cursor will move 10 tiles instead of one, enabling you to move it more quickly.

### Overview map

The overview mini-map shows a compact version of the entire available map area. This can be useful especially if your embark zone is very large. After the fortress has settled into certain areas of the map, its utility decreases and it can be hidden with to provide more space for the main map.

A cursor that looks like on the overview map shows approximately what part of the map you are viewing in the main map window. Parts of the map inhabited by dwarves will be highlighted in blue.

### Status indicators

In the upper left corner of the screen, you may see some **report flags** indicating that new combat-related Reports have been generated. Some common flags are:

new combat report available

new hunting report available

new sparring report available

Press to view the new reports in the reports screen. Once you do so, the flags will be reset.

There is also an **idle counter**, usually in the upper right, indicating how many dwarves are milling around uselessly, in need of something productive to do.

An **FPS (Frames Per Second) counter** may also be present on the screen if it has been enabled. It is disabled by default. See Frames per second for more information on what this counter means, as well as how to enable/disable it.

### Command window

This is where key menus and most of the textual information about tiles and buildings is displayed. You can toggle it between single width, double width, and hidden using . The double-width option is particularly useful when lines of text are too long to fit. Once you become familiar with the UI you may want to hide it completely; it will reappear as needed when you activate a command.

The most important interfaces that use the command window are listed below. Many of these encompass a wide variety of functionality so they will not be fully described here. See the linked articles for more details on how they are used.

## Your dwarves

Your dwarves are one of the creature types who implement your designs in-between periods of drinking, eating, partying, drinking again, sleeping, and entertaining themselves. While you do not have full control of your dwarves, you have more control over them than any other creatures. Be aware that it is not necessarily always the case that a dwarf is friendly; insane dwarves, weredwarves or vampires are anything but.

For a comprehensive reference, Reddit user DarxusC has done research on the minimum requirements to keep dwarves alive for long periods of time here.

### Eating, drinking, and sleeping

Dwarves need food to eat, alcohol to drink (water is a poor substitute), and time to sleep. If only one of these is available, it better be alcohol; while water will keep dwarves alive, they will actually work more slowly and get unhappy thoughts (see below) if they don't get much alcohol to drink.

Dwarves will also get unhappy thoughts if forced to eat a single type of food or drink a single type of alcohol all the time, so variety is also important. Dwarves will also get unhappy thoughts if forced to sleep on the floor.

### Happiness

While going about their day, dwarves will get happy and unhappy thoughts, depending on what sorts of things happen to them. This will nudge their happiness levels up or down each time one such event occurs to them. If they become too unhappy, they may throw tantrums, or go completely berserk, killing and destroying things.

### Children and immigration

Periodically, new dwarves from the outside world will migrate to your fortress, drawn by tales of, and looking to share in, your wealth and success. Female dwarves will also get pregnant and have children, if they are married to a male dwarf.

### Jobs, labors and skills

Any adult dwarf can perform any labor even if they have no skill in that area. Unskilled dwarves will simply be slow and not very good at what they are trying to do, but, with practice, dwarves will acquire skill, and become faster and better at their jobs. Lack of practice for long periods leads to skill "rust".

### Nobles

Nobles are dwarves who have special positions within your fort. Some of these are appointed, such as your broker and bookkeeper, but others, such as the mayor, are essentially forced on you by conditions in the game. See the main article on Nobles for more information.

### Death

Assuming they somehow manage to avoid starving, dehydrating, freezing, drowning, burning, falling, being crushed, or otherwise suffering fatal wounds or infections, your dwarves will inevitably die of old age. Unfortunately, they are a bit picky about how they are buried or otherwise memorialized, and they will cause trouble if they are unsatisfied with their remembrance. Corpses lying around can also pose a hazard if there are necromancers in the area.

A Healthcare industry might help your wounded dwarves postpone death.

## Digging

All of the **digging** operations are considered Mining. Even if your goal is simply to dig out a passage and you don't care about extracting ore, your miners will be generating stone as a byproduct unless they are digging through soil. See Stone management for ways to deal with all the unwanted stone.

All digging operations are done using the esignations menu.

### Digging out tunnels and spaces

[TABLE]

This is what you use to dig out tunnels and larger spaces underground. See designating an area to be mined. Note that you can not mine constructions. Instead you must remove them with -. (See below.)

### Channeling

[TABLE]

A Channel is a hole dug in the floor which will mine out the z-level below too. Channeling an area will dig out the designated tile (if it hasn't been dug out already), the floor of that tile, and the tile below, possibly leaving a Ramp on the tile below. See Channel for more information.

### Stairways and ramps

[TABLE]

See Stair and Ramp. Note that digging a stairway will not automatically create a stairway on the z-level above and/or below, but it will make it possible to dig another stairway immediately above and/or below.

### Removing things

[TABLE]

These allow you to dig away upward ramps and stairs, and demolish constructed walls and floors. See Remove for full details.

### Water and magma

While digging around you may encounter Water or Magma, so be on the lookout for **damp stone** and **warm stone**. Digging into water or magma in the wrong place can completely flood your fort to the point where it is unrecoverable, so be careful where you dig.

## Stockpiles

**Stockpiles** are where dwarves will store items of various types. Dwarves with the corresponding "hauling" job on will seek out items that aren't already on a stockpile that accepts them and carry them to the appropriate stockpile. See the main Stockpile article for detailed information on setting up stockpiles.

## Rooms, furniture, and portals

To remove one of these, use the command, place the cursor on the item to remove, and hit . This will mark the item for removal and a hauling job will be queued. Eventually a dwarf will show up and haul the item off to a stockpile if one exists.

### Furniture

[TABLE]

Assuming that dwarves have already made a piece of Furniture, they can install it somewhere using one of these commands.

### Defining rooms

Certain types of furniture placed in an area can allow the area to be defined as a Room using . The command can also be used to undefine rooms, with or without removing the associated furniture.

### Doors and hatches

[TABLE]

These commands allow you to place already created Doors and Hatch covers assuming that you have an adjacent wall.

### Windows, grates, and bars

[TABLE]

These commands allow you to install Windows, Grates, and Bars over openings, assuming that you have already created them.

## Constructions

Constructions are features that are built in place rather than created in a workshop and installed or carved out of existing rock. Constructions are how you build above-ground structures or structures in any other place where there's no rock or soil to carve them out of.

Constructions are usually built out of, and thus require, Stone or Wood, but you can also use a variety of materials (such as metal) to build them. Possible constructions include Floors, Walls, Stairs, Ramps, and Fortifications.

### Walls, floors, and stairs

[TABLE]

Walls, Floors, and Stairs are removed with -. Bridges and roads are removed with .

### Bridges

[TABLE]

A Bridge is not only used to cross rivers or chasms, but can also be used as a large door when built as a drawbridge. Such use requires that a Lever be linked to it in order for dwarves to control its open or closed state.

### Roads

[TABLE]

Roads are most commonly used to give caravans a reliable path to your fortress from the map's edge, though they don't really require one. A paved road is much like a floor except that it requires fewer raw materials per tile to build. A dirt road requires no materials to build, but deteriorates over time.

## Trading

When you want to obtain things not available on your map, and you don't want to just kill people to get them, Trading is the way to go about it. See the main article for everything you ever wanted to know about legitimately and non-violently obtaining things from other creatures.

## Military and combat

*See also: Military interface*

The **military** is one of the most important aspects of a successful fortress. Even with many traps, drawbridges and other defenses, your military will still need to fend off goblin sieges, megabeasts, titans, and fiendish underground beasties. Using a combination of squad orders and scheduling, you can set up an elaborate offensive, defensive, or balanced military structure for your well-equipped soldiers to follow. Turning your dwarves from useless migrants into bloodthirsty killing machines never hurts (unless you're the enemy).

Setting up a military is a huge subject in and of itself, so check out the main article on it and the military interface guide.

## Hospitals and healthcare

Normally your dwarves do just fine assuming they get enough food and alcohol, but sometimes they get wounded. When this happens they can benefit from an efficient Healthcare system.

## Burrows

**Burrows** are optional user-defined areas in your fort where selected dwarves live and work. Dwarves will only use workshops, dig walls, use rooms, etc. in burrows they are assigned to, though dwarves not assigned to any burrow will still use workshops etc. even if they are located in a burrow assigned to some other dwarves.

Burrows are by no means required, but are useful when you want to restrict certain dwarves to certain areas of the map.

## Macros

**Macros** allow recording sequences of keystrokes and "playing" them back into the user interface as desired. Since the game often requires using a lot of repetitive keystrokes, this can sometimes make life much easier. See the main article for full information.

## Reference sheet

A quick reference guide on fortress mode in DF can be found here. **Credit to spongemandan on reddit.com**

It includes a reference sheet on the military, stone, agriculture and a summary reference sheet.
