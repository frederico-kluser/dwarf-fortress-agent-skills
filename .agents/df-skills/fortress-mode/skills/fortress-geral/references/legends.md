# Legends

> Fonte: [Legends](https://dwarffortresswiki.org/index.php/Legends) — Dwarf Fortress Wiki (GFDL/MIT)

**Legends** mode is one of the three main methods of interacting with an already-generated world. In Legends mode, players can view maps, histories of each civilization and any figure who has lived or died in the generated world. Any noticeable achievement made by the player in Fortress or Adventurer mode is recorded and is viewable in Legends mode. You may explore Legends mode after you generate a new world.

Many players choose to generate a world where the option 'Reveal All Historical Events' is set to YES (the default) - however, if you set the option to NO, then the vast majority of the world history will be hidden in Legends mode until uncovered by brave adventurers. Even when set to YES, some things may not be revealed; all *events* will be revealed, but some historical figures, sites, regions, and civilizations and other entities may *not* be, possibly because they are not known to any civilization.

Ways for an adventurer to uncover events and other things include:

- talking to people in civilized sites and asking them various questions
- viewing items with images, like coins, armor, engravings, statues, etc
- finding artifacts and books and other written works
- possibly reading written works or by listening to stories and songs

You don't *have* to have had an adventurer or fortress game active in order to use Legends mode - some players simply enjoy it for the option of looking at the interactive historical map, or to read about the last time their favorite kingdom went to war, or for the ability to export lists of all the sites and governments active in the world. In fact, Legends Mode cannot be entered if there is an active adventurer or fortress in the world. However, a copy of such a world can be made, loaded in the game and the current mode retired or abandoned, then opened in Legends mode.

## Accessing Legends Mode

When you choose "Start Playing" in a world that doesn't have a current active game, the options include Legends mode. By accessing Legends mode, you are deciding to reveal all the knowledge of the world that would otherwise be discoverable only in pieces, through Fortress or Adventurer Mode.

Note: If you are already playing a fortress on the save you want to use, you can save to a new timeline after choosing to retire or abandon, both leaving the active fortress and allowing access to Legends mode in the new timeline.

### Available Information

- **Number of Events Undiscovered** - A self-explanatory number, indicating how many "legends" are still lost in the mists of time–if you chose to reveal all history during world generation, the number displayed should be 0. Otherwise, better get out there and adventure some more.

- **Historical Figures** - The number to the right indicates how many historical figures exist in the world's history. Historical figures include entries on megabeasts, forgotten beasts, demons, gods, dwarves, humans, goblins, kobolds, and other named creatures.

- **Sites** - The number to the right indicates how many sites have existed throughout the world's history. Sites include things like towns, towers "tower"), fortresses, forest retreats, and caves.

- **Regions** - A list of the various regions of the world, along with the various historical events that occurred within those regions.

- **Civilizations and Entities** - The number to the right indicates how many civilizations, local governments, and religions have existed throughout the world's history. The histories of these various groups can be viewed as well, detailing events like when a site was founded, when a person was kidnapped, or when a road was completed.

- **Structures** - Structures are buildings found throughout the world. Fortresses, towers, shops, taverns, temples and more can all be found in this list. Temples are the central location of religions, and can be 'profaned' by historical figures, though it is not explained what this involves.

- **Historical Map** - The historical map is a very cool feature of Legends mode - from here, you can view the territorial disputes between different civilizations and entities, including those that were destroyed before your starting year. If you are new to *Dwarf Fortress*, reading the map may be a little difficult, but play around with these buttons and you might get a better grasp of what you are seeing.

Press while looking at the map to change between the political and geographical view of the world. The geographic map is colored (blue seas, gray mountains, green forests etc.) while the political map's background is tan (think parchment) with colored fields corresponding to the territories of different civilizations. Multiple civilizations can lay claim to the same area, causing the colored territory markers to overlap. You can also see how territories change over time, by moving 10 or 100 years forward and back through time. Pressing while looking at the political map will show local government territories instead of civilizations, but that's generally a pretty messy scene.

- **The Age of...** - During world generation, the calendrical ages are named for the greatest powers extant in the world, which commonly advance during world generation (e.g. Age of Legends, Age of Heroes, Age of Humans) due to the death of megabeasts, and sometimes even regress due to the creation of night creatures and the birth of new megabeasts. When you choose to look at the history of an Age, you will be given a list of all historical events in chronological order. Here, you can read the battle reports from various wars, or the duels that took place between long-dead champions, or the burninations rampages of megabeasts amongst the peasants. See here for a list of ages and their conditions.

## Exporting World information

Legends mode has built-in tools to export lists of events, maps at various scales, and data such as locations of sites. This is particularly useful as input data for the utilities described below; there are even tools to make this export process easier (see next section). (*however, as of 50.04, exporting is suspended pending further updates, potentially because... well, time constraints.*)

### XML dump

Once you've generated a world, you can dump much of the historical data into an XML file for external analysis. The XML dump currently doesn't include every detail of world history, but it contains many of the important ones. Be warned that a large world with, say, 1000 years (or even 10,000) of history can produce an XML dump up to a full gigabyte in size, which may prove unwieldy. Press while in Legends mode to produce an XML dump (it will be placed in the root *Dwarf Fortress* directory and named the same as your game's save folder) See XML dump for information on the XML file's format.

### Export Map/Gen Information

Another option is to export the map/gen information by pressing in Legends mode. This produces three .txt files and one bitmap image that are placed in the root directory of *Dwarf Fortress*. The exported data files are named by the save file name, and the current world date:

1.  (save name)-world_gen_param.txt - contains the world generation settings.
2.  (save name)-(year)-(month)-(day)-world_history.txt-(year)-(month)-(day)-world_history.txt") - Includes some information about the deities, and rulers of the Human, Dwarven, Elven, and Goblin civilizations.
3.  (save name)-(year)-(month)-(day)-world_sites_and_pops.txt-(year)-(month)-(day)-world_sites_and_pops.txt") - Lists the sites' population, owner, parent civilization and warlord. This one will also list all the animal populations above and below ground including demons.
4.  (save name)-(year)-(month)-(day)-world_map.bmp - This is the full world map as it is shown on the embark screen, and, unlike the detailed maps below, will depend on the tileset and colour scheme you have installed.

### Export Detailed Maps

Pressing in Legends mode reveals a list of the different kinds of map you can export. The images are exported to the game's root directory when you highlight the one you want and press .

[TABLE]

## Utilities & Tools

There are many utilities that work with the data exported from Legends mode, or make exporting that info easier.

### Export tools

When using DFHack, you can use the built-in `exportlegends maps` to export all detailed maps, saving a lot of time on large worlds compared to exporting them individually and waiting for each to finish. Likewise, `exportlegends all` will export all including all detailed maps, as well as their worldgen info and legends XML. See Further docs.dfhack.org Documentation.

Export processing script can automate processing of Legends information, and is included in the Windows Lazy Newb Pack. If GIMP is installed, the script will use Dwarf Map Maker (see below); optipng can be used to compress the images from bitmaps to .png files. This tool previously also removed non-printing ASCII characters from the XML dump, that could crash Legends Viewer (usually caused by DFHack's workflow), and creates a compressed folder for each region suitable for Legends Viewer (or simply compresses the XML, if some parts have not been exported).

### Legends viewing tools and visualisers

The most famous is likely Legends Viewer, an alternative interface that recreates legends mode from exported data with many more features such as graphs, filtering, sorting, and hyperlinks. There are alternative tools with similar functionality, including World Viewer.

The Dwarf Map Maker is available as a GIMP script (free software) or a photoshop actionscript. Both use the detailed maps to produce a pretty fantasy map that looks somewhat like a satellite image. The GIMP script is called as part of PeridexisErrant's legends processing script, if the dependencies are present.
