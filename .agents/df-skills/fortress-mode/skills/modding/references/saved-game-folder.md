# Saved game folder

> Fonte: [Saved game folder](https://dwarffortresswiki.org/index.php/Saved_game_folder) — Dwarf Fortress Wiki (GFDL/MIT)

The **saved game** files are the files that store a player's progress in *Dwarf Fortress*. The game can be saved manually or automatically.

The **saved game folder** is the location where the files and information corresponding to each world (also referred to by, at least, the game, given the default characterisation of the file names as "regions") are stored and accessed by *Dwarf Fortress*. Knowledge on the technicalities of the saved game folder is crucial if one wishes to change their computer, make a backup, or wants to share a save with someone else.

Any mods that are subscribed to on Steam, and enabled for a world prior to generating it will be implemented into the save.

**See also:** Importing and exporting worlds.

## Saving

At any time while you are playing *Dwarf Fortress*, you can manually save the game with then selecting *Save and return to title menu* or *Save and continue playing*.

There is also an autosave feature, which will periodically (1, 2, or 4 times per year) save the game. To toggle **autosave** and control its behavior, see: game settings.

When loading a save the game displays the name of the fortress and its translation, what type of save it is (Active, Manual, or Autosave), the date in game, and the folder name.

The *Retire the fortress (for the time being)* and *Abandon the fortress to ruin* options also save the game, but the world will now be available to start a new game in, either with a new fortress, by unretiring a previous player fortress, or reclaiming a ruin.

If the game asks for a name for the timeline or folder, type the name, then press when done to save.

### Save and return to title menu

This option provides further options, which are also offered after retiring or abandoning:

- *Save to this timeline* - this is the normal save option for *Dwarf Fortress* which replaces the current *Active save* (any other saves will remain).
- *Save to new timeline* - this allows to save without replacing the current *Active save*, will ask what to name the timeline, and the saves in this timeline will be grouped separately from the previous saves with this save being the *Active save* of the new group.
- *Save to new folder (same timeline)* - this also allows to save without replacing the current save, but will also be grouped together with the previous *Active save*, and will also be classified as an *Active save*. This is not recommended since it can be very confusing to both the player and the game.

Since these options are also presented when retiring or abandoning a fortress, choosing to save to a new timeline or folder is useful if you want to both keep the fortress active and check Legends mode.

### Save and continue playing

This option also allows to save without replacing the current save, will ask what to name the save folder, will be classified as a *Manual save*, and will be grouped together with the existing *Active save*.

## Save folder format

[TABLE]

Your saved games are located in your ```\save\` folder. The save folder will contain one or more sub-folders, each one holding one of your worlds, and a "current" folder. The "current" folder is used to track the changes to the active world while *Dwarf Fortress* is running; it is not important unless *Dwarf Fortress* is open, and can safely be deleted otherwise.

By default, individual worlds are saved in the format: *region#*, where \# is a number, starting with region1 and then incrementing; however, world directories can be renamed without consequence **if the game is not running** (this will not change the actual name of the world). If using auto-backup, then backup folders will be named *region#-year-month-day*, for example region1-00202-01-01. (In versions prior to v0.43, the format was *region#-season-year* (for example region1-Spring-202) instead.)

This can become confusing if you frequently savescum^(‡). There is no way to change the name of these folders inside the game, but it is safe to change them using the standard methods of your operating system if the game is not running. However, **never** alter or delete the folder with the name of the game you're playing *while saving* from the game, or while that game is running!

### Contents

The saved game folder will usually have these contents:

- A series of files named *art_image-#.dat*. As their name would suggest, these files store information about art and are necessary for proper functioning. Don't replace!
- A series of files named *feature-#-#.dat*. These files store information about map features such as rivers, caverns, magma seas, and hidden fun stuff. These files are only generated for parts of the world you have explored (e.g. by embarking in Fortress mode), but using the Site Finder will tend to generate them for the entire world. Replacing these files will usually cause unwanted effects such as magma seas present on the surface or spires of adamantine spiraling up into the sky.
- A series of files named *region_snapshot-#.dat*. These are the historical maps available in Legends mode.
- A series of files named *site-#.dat*. These files store the detailed map data of previously abandoned or retired fortresses.
- A series of files named *unit-#.dat*. These contain the details of historical creatures which might potentially visit your fortress. Prior to version 0.44.10, modifying or deleting these files would lead to the dreaded "Nemesis Unit Load Failed" crash, but now the game will attempt to gracefully recover from such corruption by regenerating the unit from other available information.
- Depending on the mode currently active (or the lack thereof), a large file named *world.sav* or *world.dat*. In fortress mode, this file is named *world.sav* and includes the current fortress data, as well as the world data. In a save without a currently active game, this is the main save folder. The custom raws generated for the forgotten beasts, titans, demons, night creatures, and evil effects are stored inside this file. Replacing this entire file will almost certainly crash the game; however, replacing certain portions of the raws included may still keep the save folder working.

Missing one or more of the aforementioned important files may indicate a problem with the save; this is a very common source of crashes.

For basic backups, though, all you need to keep to is: Always copy the whole folder, not parts of it.

## Manually backing up saves

Toady recommends that you make backups, and always save to a fresh file:

1.  Copy the relevant region folder in "data/save" to a safe location.
2.  When you want to reuse it, copy that region back to "data/save".

Do **not** overwrite an old folder, as it might leave residual files.

## Restoring saves

*See also: Save compatibility*

Restoring a savegame from backup can be very confusing: The game saves back to the directory you loaded, so if you load a seasonal save, the game will save to that folder (e.g. \[region1-01056-01-01\]) and not to the original folder (\[region1\]) where you might expect it.

This can cause some high blood pressure and panic when you see your 'Region X' save is several years older than expected, and it might look like you lost all your (fortress/adv party) work to some bug. The "missing" save is, however, going to be in the directory you loaded previously. *Dwarf Fortress* lists the in-game year of each save on the right of the load screen; the highest year will generally be the most recent save (unless you've savescummed from earlier saves).

*Dwarf Fortress* autosaves to the original folder and then copies the save to a backup folder, so you should generally be able to recover from a crash by simply loading the 'main' save folder--it should be as recent as the latest "backup" save. If you want to load a backup savegame, it's recommended that you copy/rename the save to indicate that. For instance, using the examples above, copy \[region1-01056-01-01\] to \[region1-fix\] and continue play on that save (creating new backup saves of the form \[region1-fix-01056-04-01\]). Remember to only modify saves while the game is not running, per the instructions for savescumming above.

**Warning**: Save folders can be large, ranging from 20 MB for small saves to several hundred megabytes for large saves. If you run out of hard drive space while saving, *Dwarf Fortress* will *pretend* to save correctly, but the save will be unloadable. Opening other saves to verify that they still work, then saving and exiting, will corrupt your previously-working saves as well. If you don't want the game to save, just kill the application. Make sure you have sufficient free disk space before launching *Dwarf Fortress*!

## Mods

If a world is using a mod that's been updated, and is currently using an older version of that mod, the player will be prompted about this when a save is loading. Causing a message like the following to appear:\

When this happens, you have the choice of simply updating the mod, updating *all* mods at once, continuing to use the older version of the mod in question without updating, selecting the previous task but not updating *any* possibly outdated mods or simply returning to the title screen.

## Hints

On Linux or macOS, you can replace the *raw* directory with a symbolic link to *../../../raw* if you want to save a few megabytes on every backup. \[\| Forum thread\].

\]\]
