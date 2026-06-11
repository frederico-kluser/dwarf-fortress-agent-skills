# Importing and exporting worlds

> Fonte: [Importing and exporting worlds](https://dwarffortresswiki.org/index.php/Importing_and_exporting_worlds) — Dwarf Fortress Wiki (GFDL/MIT)

Although *Dwarf Fortress* is a single-player game, it is still common to incorporate a social aspect into the game. For example, you may have found a great site that you want to share with others, you want to play a save or embark that someone else posted, you're reporting a crash during world generation, or maybe you simply want to back up your world or game. There are two primary methods for importing and exporting worlds in *Dwarf Fortress*: exchanging the seed, and exchanging the save.

## Seed

"Seed" refers to the 4 specific random strings used to seed the pseudo-random number generator. These values are not sufficient to duplicate a world without the rest of the world gen parameters, but "seed" is shorter to say, so is often used to mean the entire set of parameters. Provided the versions of *Dwarf Fortress* are similar enough and no modding has taken place on either end, using a person's worldgen parameters suffices to generate the same world/s as they did. Unfortunately, this method is incapable of also moving around any events that happened after world generation ended, including the fortresses or adventures that may have taken place.

If modding has taken place, the world (but still not any events past worldgen) can still be exchanged if both receiver and transmitter have exactly the same modification. Moving the world through this method may be slow for the receiver, especially for worlds with a long history.

### Export

The easiest way to export your worldgen parameters is to press at the "p: Export image/info" prompt right after worldgen has completed. If you didn't do that, then start the game in Legends mode, and press . Either way, your *Dwarf Fortress* root folder should now contain several new files including a text file with the phrase "world_gen_param" in its name. That's the one people want. Copy or email the file or the text inside it to the receiver, or simply store the file in a safe place to be able to regenerate the world later.

This process is more difficult during fortress or adventure play, because the world cannot be loaded in Legends mode. During fortress mode, load up your fortress and press . Go to "export local image". Export local images of however much of your fortress you want (select only one level of it to save time exporting); the exported image is not important. Your *Dwarf Fortress* root folder should now contain several new files including a text file with phrase "world_gen_param" in its name. That is the one people want. As before, copy or email the file or its contents to whatever purpose was intended.

During adventure play, the "export local image" function is not available. If this is the case, it is necessary to make a copy of the save. From the *Dwarf Fortress* root directory, navigate to "data/save". From there, locate the folder with the region name to export parameters of, and copy the entire folder. Then, paste the folder into the same "data/save" directory. Now, navigate to Dwarf Fortress and load the region with the name "Copy of ..." or "... copy" or the like, and retire or starve the adventurer. Then, load the same copy in Legends mode and press to export the same "world_gen_param" file.

After these processes, the extra files in the *Dwarf Fortress* root directory can be safely deleted. Additionally, after the adventure strategy, the copy of the region can also be deleted.

### Import

Open your *Dwarf Fortress* root directory, go to Data, then Init. Open the text file called "world_gen.txt". Copy/Paste the parameters given to the bottom of that file. Make sure to save and close the file.

Next, open *Dwarf Fortress*. Go to "Design New World with Advanced Parameters". Worlds that you have parameters for are listed by title on the right. Choose your newly acquired world from the list and hit enter. Note that this process may take a while.

## Save

The save folder contains all the information on your world, and all the things you have done to it since you started playing. Use this if you want to share your actual fortress or adventure rather than just the pristine unplayed world, or if the world has already been played in and the previous fortresses or adventures are important for the purpose. Moving save folders around is also a useful way to back up your games while keeping clutter to a minimum in the Continue Game menu.

Additionally, moving the world by save preserves all mods and graphics. Therefore, this may be the preferred method when the world is based on a modded game. Moving the world in this way is also significantly easier than by seed, but it may take up more disk space and will be harder to transfer.

### Location

Your saved game is located in your *Dwarf Fortress* folder inside the "data/save" folder. The save folder will contain one or more sub-folders, each one holding one of your worlds, and a "current" folder. The "current" folder is used to track the changes to the active world while *Dwarf Fortress* is running; it is not important unless *Dwarf Fortress* is open, and can safely be deleted otherwise.

### Export

Upload the entire save folder (preferably compressed) to your favorite file host, or, better yet, to the Dwarf Fortress File Depot.

### Import

Simply drop the other person's save folder in the "data/save", and the game can be played.
