# Saved game folder

> Fonte: [Saved game folder](https://dwarffortresswiki.org/index.php/Saved_game_folder) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

"Saving world information" always seems to take the longest time...

The **saved game folder** is the location where the files containing the information for each world are stored by *Dwarf Fortress*. Knowledge of the saved game folder is crucial to moving, backing up, or sharing saves. See **Importing and exporting worlds** for sharing world generation parameters and seeds.

## Saving

**Warning**: Make sure there is sufficient free drive space before saving in *Dwarf Fortress*\!Bug:2587 Save folders can be large, ranging from just a few megabytes for small worlds with short histories, to several hundred megabytes for large worlds with many events, and even a gigabyte or two is possible in extreme cases. Also, in some cases, like world generation, *Dwarf Fortress* needs twice as much drive space for the save, since it first saves to the `current` folder, then copies that to the actual save folder. If it runs out of hard drive space while saving, *Dwarf Fortress* will act as if it saved correctly, but the save will be corrupted. Opening other saves to verify that they still work, then saving and exiting, will then corrupt that previously-working save as well.

At any time while playing *Dwarf Fortress*, you can manually save the game with Esc then selecting *Save and return to title menu* or *Save and continue playing*. If the game asks for a name for the timeline or folder, type the name you want, then press Enter when done. There is also an autosave feature, which will periodically (1, 2, or 4 times per year) save the game. To toggle **autosave** and control its behavior, see game settings.

The *Retire the fortress (for the time being)*, *Retire at this location (or rest a while)*, *Abandon the fortress to ruin*, *Give in to starvation*, *Succumb to the invasion*, etc, options also save the world, but end the game mode, and the world will now be available to start a new game mode in.

### Save and return to title menu

This option provides further options, which are also offered after retiring or abandoning:

- *Save to this timeline* - this is the normal save option for *Dwarf Fortress* which replaces the current *Active save* (any other saves will remain).
- *Save to new timeline* - this allows to save without replacing the current *Active save*, will ask what to name the timeline, and the saves in this timeline will be grouped separately from the previous saves with this save being the *Active save* of the new group.
- *Save to new folder (same timeline)* - this also allows to save without replacing the current save, but will also be grouped together with the previous *Active save*, and will also be classified as an *Active save*. This is not recommended since it can be very confusing to both the player and the game.

Since these options are also presented when retiring or abandoning a fortress, choosing to save to a new timeline or folder is useful if you want to both keep the fortress active and check Legends mode.

### Save and continue playing

This option also allows to save without replacing the current save, will ask what to name the save folder, will be classified as a *Manual save*, and will be grouped together with the existing *Active save*.

## Save folder format

|                                                   |
|---------------------------------------------------|
| save / current / region# / region#-year-month-day |

The location of the `save` folder depends on the portable mode setting, and contains one or more sub-folders, each one holding one of your worlds, and a `current` folder which is used to track the changes to the active world while *Dwarf Fortress* is running; it is not important unless *Dwarf Fortress* is open, and can safely be deleted otherwise.

By default, individual worlds are saved with the folder name `region#`, where \# is a number, starting with `region1` and then incrementing; however, world folders can be renamed without consequence **if the game is not running** (this will not change the actual name of the world). Autosave folders will be named starting with `autosave 1` and then incrementing.\[Verify\] (*Region* is also a term used for areas in worlds, thus is only used when referring to the folder name to avoid confusion.)

*Dwarf Fortress* shows the name of save folders when listing saves. There is no way to rename these folders in the game, but it is safe to change them using the standard methods of your operating system if the game is not running. However, **never** alter or delete the folder with the name of the game you're playing *while saving* from the game, or while that game is running!

### Contents

The saved game folder will usually have these contents:

- A series of files named `art_image-#.dat`. These store information about art and are necessary for proper functioning.
- A series of files named `feature-#-#.dat`. These store information about map features such as rivers, caverns, magma seas, and hidden fun stuff. These are only generated for parts of the world you have explored (e.g. by embarking in Fortress mode), but using the site finder will generate them for the entire world. Replacing these files will usually cause unwanted effects such as magma seas present on the surface or spires of adamantine spiraling up into the sky.
- A series of files named `region_snapshot-#.dat`. These are the historical maps not currently available in Legends mode.
- A series of files named `site-#.dat`. These store the detailed map data of previously abandoned or retired fortresses.
- A series of files named `unit-#.dat`. These contain the details of historical creatures which might potentially visit your fortress.
- A large file named `world.sav` or `world.dat`, depending on the mode currently active (or the lack thereof). This file stores the world data, and in fortress mode is named `world.sav` and includes the current fortress data. The custom raws generated for the forgotten beasts, titans, demons, night creatures, and evil effects are stored inside this file. Replacing this entire file will almost certainly crash the game.

Missing one or more of these important files may indicate a problem with the save; such save corruption is a source of crashes. While you are free to modify these files, their formats are undocumented and can be fragile, so it is recommended to instead use DFHack to change the data in memory and then let the game save those changes.

DFHack will sometimes add its own files to a save folder, but *Dwarf Fortress* ignores these, so there is no reason not to include them in backups or for sharing.

For basic backups and sharing, all you need to know is: Always copy the whole folder, not parts of it, and if the world was generated with mods, you may want to include the `data\installed_mods\` folder also, the location of which also depends on the portable mode setting.

## Manually backing up saves

Toady recommends that you make backups, and always save to a fresh file:

1.  Copy the relevant folder in `save`, `region#` or whatever you may have named it, to a safe location.
2.  When you want to restore a backup, copy that folder back into `save`.

Do **not** overwrite an old folder, as it might leave residual files which could corrupt the save - always delete the old folder first.

## Automatically back up save files

Windows systems: A batch file script can be run to handle copying the save folder from a cloud location like drobox into DF before the game starts, start the game and when it finishes copy the save folder back to the cloud location. If your interested in the script have a look at it https://onemancoder.wixsite.com/dwarffortress The script also creates date_time stamped backups of your local game folder to c:\temp\df as well as computer-name_date_time stamps of your cloud save games

(edit the info to make it more user friendly)

## Restoring saves

*See also: Save compatibility*

Restoring a save from backup can be confusing; the game saves back to the save you loaded, so if you load a seasonal autosave, the game will save to that folder (e.g. `autosave 1`) and not to the original folder (`region1`) where you might expect.\[Verify\] If you want to load an autosave, it is recommended that you copy and rename the folder to indicate that. For instance, using the examples above, copy `autosave 1` to `region1-fix` and continue play on that save. Remember to only modify folders while the game is **not** running.

This can cause some panic when you see your `region1` save is several years earlier than expected, and it might look like you lost all your (fortress/adventer party) work to some bug. However, the "missing" save is going to be in the folder you loaded previously. *Dwarf Fortress* shows the save type, in-game year, and folder name of each save on the load screen; the highest year will usually be the most recent save, unless you've previously loaded from earlier save.

## Mods

If a world is using a mod that's been updated, and is currently using an older version of that mod, the player will be prompted about this when a save is loading, causing a message like the following to appear:\

When this happens, you have the choice of simply updating the mod, updating *all* mods at once, continuing to use the older version of the mod in question without updating, selecting the previous task but not updating *any* possibly outdated mods or simply returning to the title screen.
