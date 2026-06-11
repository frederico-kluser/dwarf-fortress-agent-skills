# Maximizing framerate

> Fonte: [Maximizing framerate](https://dwarffortresswiki.org/index.php/Maximizing_framerate) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A picture of *Dwarf Fortress* with frames per second displayed.

Framerate is used in *Dwarf Fortress* to measure the speed at which the game is running. It is measured in "frames per second", or FPS for short. To check your FPS in-game, go to settings - Game and turn Show frames-per-second to Yes. Then your FPS will be displayed on the bottom row of the screen. The first number is the current frame rate, while the number in parentheses is the current graphical frame refresh rate.

## Increasing your framerate

In general, the more stuff the game has to keep track of, the slower the game will run. So, reducing the amount of stuff that's active keeps your game running fast. The **vast** majority of processing time in Dwarf Fortress is taken up by units taking their turns, over 60% in larger forts, of which less than 10% is actually pathfinding related, so **the best way to prevent FPS loss is to reduce the amount of units spawned in general. The lists below separate ways to improve FPS into two categories: things that don't change the game in any fundamental way, and things that do.**

### Without Game Alterations

Fortress design is specific ways of building and planning; game settings changes are those that mostly don't actually change how the game plays out.

#### World Generation

- Larger worlds require more background processing to update. The larger the civilizations, the more events occur in the world and the more complex they are. Generating too-large civilized populations can result in a permanent, unavoidable FPS drop. However, with how rich the game is with content, even a small world will be fairly interesting, while leading to a much higher framerate, though you may want to adjust some of the advanced world generation settings.
- Longer histories require more memory and storage space for historical figures and events.
- Reducing the number of civilizations, sites, beasts, and setting world population cap can limit the resources spent updating the rest of the world.
- Caverns can be an FPS hog due to the large amount of creatures that spawn there if fiddled with. Sometimes even trading caravans will try to path out of your fort underground.
  - Adjusting the cavern layer number in advanced world generation parameters can reduce the number of cavern layers (default 3). However, this will restrict access to subterranean plants and creatures, and reduce the number of spawned forgotten beasts.
  - Similarly, one could adjust Layer Openness and Layer Passage Density in advanced world generation to make the caverns have fewer tiles to path through. In general, the pathfinding algorithm heuristically treats distances as a chess king moving in 3D ("Chebyshev distance"), which means that it can tend to go to the right X/Y then start floodfilling dumbly through the entire Z from there until it can find a way up, at which point the whole process repeats, so having fewer cavern tiles is better and open areas are to be avoided.[1]
  - Generating a world using a "REGION" template (instead of an "ISLAND" template which is used by "Create New World!") can significantly reduce the height of caverns and also place them closer together, resulting in fewer Z-levels. This generally also requires embarking in an area that isn't very close to an ocean or a mountain peak.
- Snow and ice melting can cause lag spikes.\[Verify\] You can generate a world without poles with a somewhat heightened temperature, or just embark somewhere which doesn't freeze over.

#### Fortress Design

- Larger embark sites dramatically increase the amount of terrain which DF needs to keep track of and path through.
  - Reducing the size of your embark site from the default 4×4 squares to 3×3 or even 2×2 will have an enormous impact on FPS.
  - Keep in mind that a 2×2 embark is only 25% of the size of a 4×4 embark. However, in 3D it is still a large enough area for many fortresses in normal play.

- Line-of-sight calculations, even after optimizations in v50.05, are the slowest part of the game by a wide margin. This is O(n^2) by nature, so the only way to truly reduce it is to reduce the amount of units. That said, there are still ways you can reduce the issues.
  - Keep your dwarves spread far apart--units who are more than 26 units away from a given unit in **any direction** are not considered for line-of-sight calculations.
  - Avoid having only one meeting area that has hundreds of dwarves in it.
  - Try to break line-of-sight in various places to keep your dwarves from asking "friend or foe?" too often.
  - Don't use doors to break line-of-sight, as doors can act as an FPS drain (in sufficient numbers). Use walls or bridges instead.

- Fewer items inside a fort means fewer items checked for temperature, which is the only major performance issue items cause.
  - The obvious solution is not to generate so many items in the first place. Don't build such large farm plots and don't go overboard with multiple workshops constantly queued or set on perpetual repeat.
  - Use a Dwarven atom smasher to remove items, or donate them to passing caravans to be taken away.
  - Quantum stockpiles can reportedly improve game speed.
  - The quantity of items in any particular stack doesn't affect framerate so much as the number of stacks in general, due to the resultant impact on hauling, stockpiles, pathfinding and other CPU-intensive tasks. The research done on the Undump Engine and Micha's experimental fort demonstrate very FPS efficient solutions, while avoiding traditional stockpiles and the use of barrels and bins.
  - That said, total quantity of items does matter. Quantity matters far more with objects that have quality or decorations than boulders, as they take up more memory. Temperature checks, wear increments, and other issues lag the game, although it takes far larger item quantities (10,000+) to be seriously notable.
- Changes to the map's connections can cause brief lag spikes as the game's connections map needs updating.
  - This is most notable with doors, drawbridges, or other objects linked to a repeater. An atom-smasher linked to a repeater, even disconnected from the rest of the fortress, can cause lag spikes every time it is raised or lowered. If you use an atom-smasher to eliminate garbage, make it operate only very infrequently through mechanics, or operate it manually by lever.
  - Wall off areas with changing water levels[1].
- Proper use of traffic designations will help.
- The amount of active plant gatherers can heavily impact framerate, especially if the "everyone does this" option is enabled in the labor menu, coupled with having a very high population. It is best to use the "only selected do this" and select just a fraction of citizens for this task, or to disable it completely with the "nobody does this" option if gathering plants is not a priority at the time.
  - Setting corridors to "high" traffic, and dead-end workshop rooms next to them to "low" traffic, means the pathfinder algorithm will search more quickly along the corridor, and waste less time searching in the rooms.
- While pathfinding is not a major FPS drain, reducing the area which the pathfinder algorithm has to search lets the game run a bit faster.
  - The obvious solution is to not dig out quite so much of the ground.
  - Some careful fort planning and design can cut down on pathfinding with shorter trips.
  - Spreading your fortress out horizontally tends to mean travelling three or four tiles further down the hallway per every second workshop you build. Making workshops stack vertically upon multiple stairwells or ramps up or down from the stockpiles lets you cram workshops around the stairs or ramps just one further tile per set of four workshops.
  - Giant stockpile areas are huge areas that cost pathfinding. Quantum stockpiling can prevent the need to excavate more space. That said, each item you produce takes up more memory and is considered in routine cycles like temperature. Avoid producing more goods than you can actually use just because you "want to keep dwarves busy". If you are starting to run out of space to hold your goods, rather than dig out more space to stash it all, just stop producing goods.
  - If fortress functions are spread far apart, consider multiple dining halls. A legendary dining hall isn't THAT hard to produce, and there are few reasons a magma forge operator has to cross 100 zs to the surface to get a drink before going back down.
  - Crowded hallways force "dodging" which results in more pathfinds. Find ways to spread traffic out to avoid collisions. Don't rely upon a 1-tile hallway for access to areas dwarves travel to frequently, and possibly set up multiple paths that are "shortcuts" for dwarves rather than always having to travel through the same hallways to the same central staircase every single time.
  - Dwarves have been found to prefer pathing across ramps to stairs or even horizontal travel if there is a change in z-level. Laying out your fortress with ramps rather than stairs can give an edge.
  - Closing off unused areas with raised bridges or walls can help.
  - Open "quarry pits" are pathfinding traps. Seal them off from your fort with walls when you are done with them.
  - Caverns are probably the worst offender for pathfinding in irrelevant areas. So keep any part you aren't occupying closed off.
  - Don't designate large areas to be smoothed at once.Bug 5986
  - Trapped dwarves, particularly trapped moody dwarves cause significant lag at times. **This is pretty much the only time pathfinding actually causes FPS issues.** There is a bug where a trapped dwarf with a strange mood will slow the game down tremendously. Bug:8698 Free them of bondage or life to get on with your own.
  - Locations without sufficient floor space invite frequent pathing. Make sure your locations are large enough for your population.
- Each animal needs to do line-of-sight checks, too.
  - Tame animals can be put into cages, in which case they are totally exempt from all such checks. Or you can butcher them, too.
- Multi-tile trees are a known source of lag.
  - Choosing an embark location that only grows trees on one or two squares can improve performance.
- Contaminants can accumulate on the ground and on dwarves and creatures. Especially for old forts, this can impact FPS. There is a bug (Bug:296) which makes contaminants continuously multiply and another (Bug:3270) which prevents blood from ever disappearing.
  - If the contaminants are outside, isolate the area and let rain slowly wash it away. Pets can be kept out with a pen/pasture or a pit. Similarly, setting the traffic designation to restricted and/or assigning Activity Zones strategically may keep dwarves away.
  - Add in some in-fortress means of cleaning dwarves and pets. Just soap and a well will allow dwarves to clean themselves. Make sure you have the cleaning labor enabled, too. Details of these and other suggestions can be found on the cleaning page.
- Encountering HFS will dramatically reduce FPS AFTER you seal the breach (Bug:1340). Either avoid doing so or use the work around posted in the bug report.
- Heavy construction, especially megaprojects, will cause increasingly severe input lag as the fortress grows. Forbid materials (especially stones, blocks, and bars) as much as possible to reduce the time the game needs to calculate the list of available materials to build constructions with.
- When a team comes back from a raid/mission, a huge lag can appear suddenly (down to 5 fps). You can disband the squad and situation should come back to normal.
- The same can happen when sending a squad out for a mission. If squad members are somehow locked inside, they will continuously try to find a path to the mission and the game can grind to a near halt.
- Engravings are an issue in ASCII, but not so much in graphics mode, due to the slow lookup for engraving graphics.
- Minimize the number of living plants. This will not endear you to the Elves.
- Avoid looking at complicated areas. Displaying a map tile takes a varying amount of work depending on what it is:
  - Unrevealed tiles take almost no time at all - it just needs to look up what "random glyph" to display there
  - Trees need to do a linear search through a column-specific list (one list per 48x48 tile embark region block) to determine what growths are present in the tile and look up within the plant itself to get the symbol/color. **This is the slowest part of the rendering step.**
  - Layer stone tiles need to take the biome number and layer number and look up the layer material, then look up the inorganic raw object to get the symbol/color
  - Lava stone tiles need to take the biome number and look up some region information to determine what lava-stone to use, then continue as above
  - Feature stone tiles (i.e. adamantine) need to look up the map feature located within the tile to figure out what it's made of, then continue as above
  - Vein stone tiles need to do a linear lookup within a list specific to the 16x16x1 map block to see which vein they match and determine the material, then continue as above
  - Grass tiles need to do a linear lookup within that same list to figure out what type of grass is present, then look up the plant raw object to get the symbol/color (and also account for animations)
  - Shrubs and saplings need to search a separate list (not sure if it's the global list or a column-specific one) to find the plant in question and determine its symbol/color
  - Constructed tiles need to do a binary search by X/Y/Z coordinates in a separate list to determine what material it uses, then look up that material for the symbol/color
  - On top of all of that, it does a *linear* search in yet another list to determine whether or not an engraving is present (and, if there is, what tile to display)
  - Other tile contents (units, buildings, items, vermin, etc.) get displayed
  - After all of that is done, it then does yet another linear search (though the same list as with vein stones and grass) to see if the tile has a spatter on it (e.g. mud, blood, vomit, or leaves) and adjust the symbol/color accordingly

#### Game Settings

- G_FPS is a setting in the init.txt file. It controls how often Dwarf Fortress redraws the screen. It also controls how often the game checks for keyboard or mouse input.
  - Reducing G_FPS **will not** speed up the rest of the game, as everything in it runs on a separate thread.

### With Game Alterations

All changes in this area have some effect on the game itself, use at your own discretion.

#### Game Settings

- Temperature calculations place a significant load on the processor.
  - Disabling them will speed things up, and can be undone at any time.
  - Without temperature calculations, obsidian farming becomes unusable; as the tiles never cool down, dwarves refuse to step on the obsidian floor, preventing access for hauling dwarves.Bug:6033 You can re-enable temperature occasionally to allow tile temperatures to normalize. Alternatively, you can work around this issue by altering obsidian in the raws to give it \[MAT_FIXED_TEMP:10000\] (as nether-cap does normally), preventing it from being hot.
  - Disabling temperature calculations will cause fire to become glitchy, including creatures who can create it (fire imps, dragons, forgotten beasts, etc). Dwarves set on fire with temperature disabled will burn perpetually until exposed to water, though they won't receive any damage. Tiles exposed to fire with temperature calculations disabled will become entirely impassable, which may lead to significant parts of your map being blocked away. If confronted by fire or fire-based creatures, it may be worth turning temperature back on until they're dealt with.
  - Multiple users have reported an FPS increase of 100% or better when disabling temperature calculations [2].
- Disabling weather is likely to speed things up as well, but then rain won't refill murky pools, clean contaminants, kill dwarves, etc.
- Each dwarf has a lot of processing involved with them, accounting for the actual majority of frame times.
  - Limit the number of dwarves by setting a population cap.
- Invaders also need to process. While you can simply kill them to get rid of the problem, their mere presence may slow the game down to the point it is unfeasible.
  - The number of invaders can be controlled in difficulty settings. Lower the invader cap to get smaller sieges with a more reasonable amount of enemies. If that is not enough, invaders can be disabled outright, though that will lock you out of fun content.
- The game also has to track what is happening in the caverns.
  - You can disable cavern layers in advanced world generation. Without caverns, you will have far fewer critters and threats pathfinding through winding passages. Unfortunately, you also lose underground plants and trees. Alternatively, you can reduce the number of cavern layers to just one.
  - If you don't mind losing large amounts of fun, you can also disable generation of the magma sea and bottom layer.

#### Mods and Utilities

- Accumulations of contaminants can decrease FPS, and they are somewhat buggy. (See Bug:296 and Bug:3270.)
  - Sometimes contaminants are widespread or difficult to reach, such that relying on the usual cleaning methods would be impractical or impossible, or the player may lack the patience to deal with it that way. Some opt to use the "clean" and "spotclean" commands in the DFhack utility to clear contaminants.

- Constantly-growing piles of cast-off clothes and checking for clothing wear and unhappy thoughts can impact FPS.
  - One could modify clothing to prevent wear. This can be done by adding an ARMORLEVEL:1 token. Aside from a possible FPS gain, this has other benefits as well. This fix is part of the Modest Mod as an optional "Eternal Fashion module". It might also be found in other mods which are based around Modest Mod. (Search the DFFD for "Modest".) Also, Masterwork Dwarf Fortress allows the creation of metal clothing.

## DFHack commands

A list of DFHack commands that can help with your framerate by fixing bugs and reducing items.

- autodump Useful for mass dumping or destroying items. Use help autodump for options.
- cleanowned Confiscates and dumps garbage owned by dwarves. Use help cleanowned for options. Can cause unhappy thoughts if no replacement clothing is available.
- clean and spotclean Removes contaminants from tiles/units/items or one tile. Bug:296Bug:1750Bug:3270 Use help clean for options.
- flows Counts map blocks with flowing liquids, which slow the game down.

- tweak fast-heat Further improves temperature update performance.

- timestream alters the game simulation speed so that it \*feels\* fast even at low FPS. Either the calendar, or the units themselves, or both, can be changed - so timestream -fps 100 -units while your actual FPS sits at a measly 20 will make the calendar tick and the units move five times faster. This is very useful to extend the playability of older forts where early micromanagement isn't as important and most of day-to-day functioning runs itself.

- fastdwarf Causes dwarves and other creatures to move and work faster or causes them to teleport. Run fastdwarf help for more information.

## GNU/Linux Specific

Placing the whole df_linux directory in tmpfs using Anything Sync Daemon might improve FPS depending on your system.

If you run any indexing, exclude DF directory.

Installing mimalloc or jemalloc and preloading it in your ./df script to run *Dwarf Fortress* may result in improved framerates:

    #!/bin/sh
    DF_DIR=$(dirname "$0")
    cd "${DF_DIR}"
    LD_PRELOAD="/path/to/libmimalloc.so.2.0" ./libs/Dwarf_Fortress "$@"

The path the malloc is installed to may vary, check */usr/lib/*, */usr/lib64/*, */usr/local/lib/*, */usr/local/lib64/*, and */usr/lib/x86_64-linux-gnu/*. The .so file's name may also vary.

### Setting process niceness

One thing that Unix-like systems feature is being able to control the priority of a process in relation to other processes running at the same time. This is its "niceness" value, with -20 being most favorable to the process. Some graphical task managers can set this value, but otherwise, you can use the "renice" command.

    sudo renice -n -20 -p $(pgrep Dwarf_Fortress)

or if you are using the Steam version of the game the command will look like:

    sudo renice -n  -20 -p $(pgrep dwarfort)

If the command was successful the output should be:

    (PID #) (process ID) old priority (whatever the old number was), new priority -20

## See also

- System requirements - hardware changes affecting framerate
