# Importing and exporting worlds

> Fonte: [Importing and exporting worlds](https://dwarffortresswiki.org/index.php/Importing_and_exporting_worlds) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Although *Dwarf Fortress* is a single-player game, it is still common to incorporate a social aspect into the game. For example, you may have found a great site that you want to share with others, you want to play a save or embark that someone else posted, you're reporting a crash during world generation, or maybe you simply want to back up your world or game. There are two primary methods for **importing and exporting** worlds in *Dwarf Fortress*: exchanging the seed, and exchanging the save.

## Seeds

"Seeds" refers to the 4 specific random strings used to seed the pseudo-random number generator. These values are not sufficient to duplicate a world without the rest of the world generation parameters. Unfortunately, the historical events during world generation don't currently always happen the same way, and this method is incapable of replicating any events that happened after world generation ended, including any fortresses or adventures. Mods and even parameters can greatly change how a world generates, causing the game to use more or fewer pseudo-random numbers for each step, meaning later steps get a different series of numbers.

### Export

When the game generates a world, it writes the seeds it used for that world in the `gamelog.txt` file in the main *Dwarf Fortress* folder. Unfortunately, the game doesn't currently provide a full output of the world generation parameters.

### Import

If the world was generated using advanced world generation and the parameters were saved, or can otherwise be remembered, then the seeds can be copied into `prefs/world_gen.txt`, using the proper tokens. They cannot currently be pasted into the game directly, but can be entered manually.

## Save

A save folder contains all the information on a world, including everything done in it since it was generated. Use this to share an active fortress or adventure, or if previous activity is important, rather than just the pristine unplayed world. In addition to being the more complete way of sharing a world than using seeds, moving a save folder around is also a way to back up your saves while reducing clutter in the Continue active game menu.

Additionally, mods are not included in saves, thus, when sharing a save of a modded game the installed_mods folder should also be included.

### Location

The easiest way to get to the save folder is to go into the "files" menu for the relevant save; this is opened with the Files button to the left of saves. If there's a "Delete" button instead, click on that world and the Files button is next to the saves within. A saved game is all the files in each folder in the `save` folder, the location of which depends on the portable mode setting. Saves that existed before the addition of the portable mode setting, or when changing the setting, may still be in the old location.

The `save` folder contains one or more sub-folders, each one a world, by default named `region`*`#`*, and a `current` folder. The `current` folder is used to track the changes to the active world while *Dwarf Fortress* is running; it is not important unless *Dwarf Fortress* is open, and can safely be deleted otherwise.

### Export

Upload the entire save folder (preferably compressed and maybe renamed to be less generic than `region`*`#`*), and the `installed_mods` folder if applicable, to the Dwarf Fortress File Depot, or some other file host.

### Import

Extract the archive to a temporary location, ensure the contained save folder has a unique name, renaming it if needed, and move it to the `save` folder, and the contents of the `installed_mods` folder, if included, to `data\installed_mods`, then start *Dwarf Fortress* and the save should be available.
