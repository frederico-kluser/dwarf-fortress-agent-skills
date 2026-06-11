# Maximizing framerate

> Fonte: [Maximizing framerate](https://dwarffortresswiki.org/index.php/Maximizing_framerate) — Dwarf Fortress Wiki (GFDL/MIT)

Framerate is used in *Dwarf Fortress* to measure the speed at which the game is running. It is measured in "frames per second", or FPS for short. To check your FPS in-game, simply change \[FPS:NO\] to \[FPS:YES\] in init.txt, and your FPS will be displayed on the top row of the screen. The first number is the current frame rate, while the number in parentheses is the current graphical frame refresh rate.

## Increasing your framerate

In general, the more stuff the game has to keep track of, the slower the game will run. So, reducing the amount of stuff that's active keeps your game running fast. The lists below separate ways to improve FPS into two categories: things that don't change the game in any fundamental way, and things that do.

### Without Game Alterations

Fortress design is specific ways of building and planning, game setting changes are changes mostly in the init.txt and D_init.txt files that don't actually change how the game plays out.

#### World Generation

- Larger worlds require more background processing to update. The larger the civilizations, the more events occur in the world and the more complex they are. Generating too-large civilized populations can result in a permanent, unavoidable FPS drop. However, with how rich the game is with content, even a small world will be fairly interesting, while leading to a much higher framerate, though you may want to adjust some of the advanced world generation settings.
- Longer histories require more memory and storage space for historical figures and events.
- Reducing the number of civilizations, sites, beasts, and setting world population cap can limit the resources spent updating the rest of the world.
- Caverns can be an FPS hog due to pathfinding and how complex they can be. Creatures will repeatedly try to path into your fort from a cavern. Sometimes even trading caravans will try to path out of your fort underground.
  - Adjusting the cavern layer number in advanced world generation parameters can reduce the number of cavern layers (default 3). However, this will restrict access to subterranean plants and creatures, and reduce the number of spawned forgotten beasts.
  - Similarly, one could adjust Layer Openness and Layer Passage Density in advanced world generation to make the caverns have fewer tiles to path through. In general, the pathfinding algorithm will make a beeline to the right X and Y coordinates and then start floodfilling dumbly through the entire Z from there until it can find a way up, at which point the whole process repeats, so having fewer cavern tiles is better and open areas are to be avoided.
  - Generating a world using a "REGION" template (instead of an "ISLAND" template which is used by "Create New World!") can significantly reduce the height of caverns and also place them closer together, resulting in fewer Z-levels. This generally also requires embarking in an area that isn't very close to an ocean or a mountain peak.
- Snow and ice melting can cause lag spikes. You can generate a world without poles with a somewhat heightened temperature, or just embark somewhere which doesn't freeze over.

#### Fortress Design

- Setting doors to be tightly closed causes pets to repath every time they try to enter them. **If you value your FPS, keep all of your doors pet-passable!**
- Larger embark sites dramatically increase the amount of terrain which DF needs to keep track of and path through.
  - Reducing the size of your embark site from the default 4×4 squares to 3×3 or even 2×2 will have an enormous impact on FPS.
  - Keep in mind that a 2×2 embark is only 25% of the size of a 4×4 embark. However, in 3D it is still a large enough area for many fortresses in normal play.

- Fewer items inside a fort means fewer items to be stockpiled, checked for wear, and so on and so forth.
  - The obvious solution is not to generate so many items in the first place. Don't build such large farm plots and don't go overboard with multiple workshops constantly queued or set on perpetual repeat.
  - Checking for clothing wear and unhappy thoughts could still have some impact on FPS. (Research is needed.) Armor counts for missing clothing thoughts, so dwarves can wear armor instead of clothes or going naked. If nothing else, dumping excess/worn out clothing may help FPS on an old fortress.
  - Use a Dwarven atom smasher to remove items, or donate them to passing caravans to be taken away.
  - Quantum stockpiles can reportedly improve game speed.
  - The quantity of items in any particular stack doesn't affect framerate so much as the number of stacks in general, due to the resultant impact on hauling, stockpiles, pathfinding and other CPU-intensive tasks. The research done on the Undump Engine and Micha's experimental fort demonstrate very FPS efficient solutions, while avoiding traditional stockpiles and the use of barrels and bins.
  - That said, total quantity of items does matter. Quantity matters far more with objects that have quality or decorations than boulders, as they take up more memory. Even in quantum stockpiles, temperature checks, wear increments, and other issues lag the game, although it takes far larger item quantities (10,000+) to be seriously notable.
- Flowing water slows the game down.
  - Don't build mist generators, pump stacks, or other major water-moving projects. If you do build them, build a way to switch them off.
  - Don't embark on a river or ocean. Rivers aren't too bad in their natural state, because the game only needs to calculate at where the water enters and where the water leaves, more-or-less skipping the water in between. Then you start damming them and pumping water out, and it gets worse.
  - Aquifers don't impose load until you start digging around in them.
  - Dwarven water reactors also slow down the game, often significantly.
  - Wall off areas with changing water levels1. This prevents the game from needing to update pathfinding information whenever the water level changes and is safer anyway.
- Changes to the map's connections can cause brief lag spikes as the game's connections map needs updating.
  - This is most notable with doors, drawbridges, or other objects linked to a repeater. An atom-smasher linked to a repeater, even disconnected from the rest of the fortress, can cause lag spikes every time it is raised or lowered. If you use an atom-smasher to eliminate garbage, make it operate only very infrequently through mechanics, or operate it manually by lever.
- Proper use of traffic designations will help.
  - Setting corridors to "high" traffic, and dead-end workshop rooms next to them to "low" traffic, means the pathfinder algorithm will search more quickly along the corridor, and waste less time searching in the rooms.
- Reducing the area which the pathfinder algorithm has to search lets the game run faster.
  - The obvious solution is to not dig out quite so much of the ground.
  - Some careful fort planning and design can cut down on pathfinding with shorter trips.
  - Spreading your fortress out horizontally tends to mean travelling three or four tiles further down the hallway per every second workshop you build. Making workshops stack vertically upon multiple stairwells or ramps up or down from the stockpiles lets you cram workshops around the stairs or ramps just one further tile per set of four workshops.
  - Giant stockpile areas are huge areas that cost pathfinding. Quantum stockpiling can prevent the need to excavate more space. That said, each item you produce takes up more memory and is considered in routine cycles like temperature. Avoid producing more goods than you can actually use just because you "want to keep dwarves busy". If you are starting to run out of space to hold your goods, rather than dig out more space to stash it all, just stop producing goods.
  - If fortress functions are spread far apart, consider multiple dining halls. A legendary dining hall isn't THAT hard to produce, and there are few reasons a magma forge operator has to cross 100 zs to the surface to get a drink before going back down.
  - Crowded hallways force "dodging" which results in more pathfinds. Find ways to spread traffic out to avoid collisions. Don't rely upon a 1-tile hallway for access to areas dwarves travel to frequently, and possibly set up multiple paths that are "shortcuts" for dwarves rather than always having to travel through the same hallways to the same central staircase every single time.
  - Dwarves have been found to prefer pathing across ramps to stairs or even horizontal travel if there is a change in z-level. Laying out your fortress with ramps rather than stairs can give an edge.
  - Closing off unused areas with raised bridges and locked doors can help.
  - Open "quarry pits" are pathfinding traps. Seal them off from your fort with walls when you are done with them.
  - Caverns are probably the worst offender for pathfinding in irrelevant areas. So keep any part you aren't occupying closed off.
  - Don't designate large areas to be smoothed at once.
  - Trapped dwarves, particularly trapped moody dwarves cause significant lag at times. There is a bug where a trapped dwarf with a strange mood will slow the game down tremendously. Free them of bondage or life to get on with your own.
  - Locations without sufficient floor space invite frequent pathing. Make sure your locations are large enough for your population.
- Each animal needs to pathfind, too.
  - Tame animals can be put into cages, keeping them from having anywhere to go. Or you can butcher them.
  - Avoid pet-impassable doors; animals will stand at the door and continuously path through it.
- Multi-tile trees are a potential source of lag.
  - Choosing an embark location that only grows trees on one or two squares can improve performance.
- Contaminants can accumulate on the ground and on dwarves and creatures. Especially for old forts, this can impact FPS. There is a bug () which makes contaminants continuously multiply and another () which prevents blood from ever disappearing.
  - If the contaminants are outside, isolate the area and let rain slowly wash it away. Pets can be kept out with a pen/pasture or a pit. Similarly, setting the traffic designation to restricted and/or assigning Activity Zones strategically may keep dwarves away.
  - Add in some in-fortress means of cleaning dwarves and pets. Just soap and a well will allow dwarves to clean themselves. Make sure you have the cleaning labor enabled, too. Details of these and other suggestions can be found on the cleaning page.
- Encountering HFS will dramatically reduce FPS AFTER you seal the breach (). Either avoid doing so or use the work around posted in the bug report.
- Heavy construction, especially megaprojects, will cause increasingly severe input lag as the fortress grows. Forbid materials (especially stones, blocks, and bars) as much as possible to reduce the time the game needs to calculate the list of available materials to build constructions with.
- Training your military can cause lag, mostly due to sparring. Try to avoid training more than one or two squads at a time.
- When a team comes back from a raid/mission, a huge lag can appear suddenly (down to 5 fps). You can disband the squad and situation should come back to normal.
- The same can happen when sending a squad out for a mission. If squad members are somehow locked inside, they will continuously try to find a path to the mission and the game can grind to a near halt.
- Use as few engravings as possible.
- Minimize the number of living plants. This will not endear you to the Elves.
- Avoid looking at complicated areas. Displaying a map tile takes a varying amount of work depending on what it is:
  - Unrevealed tiles take almost no time at all - it just needs to look up what "random glyph" to display there
  - Layer stone tiles need to take the biome number and layer number and look up the layer material, then look up the inorganic raw object to get the symbol/color
  - Lava stone tiles need to take the biome number and look up some region information to determine what lava-stone to use, then continue as above
  - Feature stone tiles (i.e. adamantine) need to look up the map feature located within the tile to figure out what it's made of, then continue as above
  - Vein stone tiles need to do a linear lookup within a list specific to the 16x16x1 map block to see which vein they match and determine the material, then continue as above
  - Grass tiles need to do a linear lookup within that same list to figure out what type of grass is present, then look up the plant raw object to get the symbol/color (and also account for animations)
  - Shrubs and saplings need to search a separate list (not sure if it's the global list or a column-specific one) to find the plant in question and determine its symbol/color
  - Trees need to do a linear search through a column-specific list (one list per 48x48 tile embark region block) to determine what growths are present in the tile and look up within the plant itself to get the symbol/color
  - Constructed tiles need to do a binary search by X/Y/Z coordinates in a separate list to determine what material it uses, then look up that material for the symbol/color
  - On top of all of that, it does a *linear* search in yet another list to determine whether or not an engraving is present (and, if there is, what tile to display)
  - Other tile contents (units, buildings, items, vermin, etc.) get displayed
  - After all of that is done, it then does yet another linear search (though the same list as with vein stones and grass) to see if the tile has a spatter on it (e.g. mud, blood, vomit, or leaves) and adjust the symbol/color accordingly

#### Game Settings

- G_FPS is a setting in the init.txt file. It controls how often Dwarf Fortress redraws the screen. It also controls how often the game checks for keyboard or mouse input.
  - Reducing G_FPS can speed up the rest of the game. The default choice of 50 works well, but many people reduce it down to 20 with no ill effect.
  - Reducing G_FPS too far can make the game unresponsive and glitchy. Some people can cope with 5; most cannot.
- PRINT_MODE is another init setting. It controls the method Dwarf Fortress uses to draw the screen.
  - More advanced methods allow DF to make more use of OpenGL features and therefore your graphics card. STANDARD and VBO are good starting points.
  - More advanced methods may still have bugs. 2D is more likely to be reliable.
- Using creature graphics may reduce FPS. (Using a custom ASCII tileset should have no effect)
- PRIORITY represents how much importance the game is given when it makes a request of the CPU. From init.txt:
  - "Change this to make the dwarfort.exe process have a different priority. From highest to lowest, the options are REALTIME, HIGH, ABOVE_NORMAL, NORMAL, BELOW_NORMAL and IDLE."
  - While it's best to run DF with no other programs in the background if FPS is an issue, giving the priority a bump or two can help speed things up regardless. You should not set this to REALTIME.
- TEXTURE_PARAM controls how the graphics are displayed, specifically how the color value of each pixel is smoothed. It is LINEAR by default. Turning this to NEAREST gives the CPU slightly less to do, though the improvement in performance is so far unquantified.
  - From init.txt: "Change this to NEAREST if you want the texture values to use the nearest pixel without averaging. Change this to LINEAR if you want the texture values to be averaged over the adjacent pixels."

### With Game Alterations

All changes in this area have some effect on the game itself, use at your own discretion.

#### Game Settings

- Temperature calculations place a significant load on the processor.
  - Disabling them, using the settings in d_init.txt, will speed things up.
  - Without temperature calculations, obsidian farming becomes unusable; as the tiles never cool down, dwarves refuse to step on the obsidian floor, preventing access for hauling dwarves. You can re-enable temperature occasionally to allow tile temperatures to normalize. Alternatively, you can work around this issue by altering obsidian in the raws to give it \[MAT_FIXED_TEMP:10000\] (as nether-cap does normally), preventing it from being hot.
  - Disabling temperature calculations will cause fire to become glitchy, including creatures who can create it (fire imps, dragons, forgotten beasts, etc). Dwarves set on fire with temperature disabled will burn perpetually until exposed to water, though they won't receive any damage. Tiles exposed to fire with temperature calculations disabled will become entirely impassable, which may lead to significant parts of your map being blocked away. If confronted by fire or fire-based creatures, it may be worth turning temperature back on until they're dealt with.
  - Multiple users have reported an FPS increase of 100% or better when disabling temperature calculations 2.
- Disabling weather is likely to speed things up as well, but then rain won't refill murky pools, clean contaminants, kill dwarves, etc.
- Each dwarf has a lot of processing involved with them.
  - Limit the number of dwarves by setting a population cap.
- Invaders also need to pathfind. While you can simply kill them to get rid of the problem, their mere presence may slow the game down to the point it is unfeasible.
  - The number of invaders can be controlled with d_init.txt. Lower the invader cap to get smaller sieges with a more reasonable amount of enemies. If that is not enough, invaders can be disabled outright, though that will lock you out of fun content.
- The game also has to track what is happening in the caverns.
  - You can disable cavern layers in advanced world generation. Without caverns, you will have far fewer critters and threats pathfinding through winding passages. Unfortunately, you also lose underground plants and trees. Alternatively, you can reduce the number of cavern layers to just one.
  - If you don't mind losing large amounts of fun, you can also disable generation of the magma sea and bottom layer.

#### Mods and Utilities

- Accumulations of contaminants can decrease FPS, and they are somewhat buggy. (See and .)
  - Sometimes contaminants are widespread or difficult to reach, such that relying on the usual cleaning methods would be impractical or impossible, or the player may lack the patience to deal with it that way. Some opt to use the "clean" and "spotclean" commands in the DFhack utility to clear contaminants.

- Constantly-growing piles of cast-off clothes and checking for clothing wear and unhappy thoughts can impact FPS.
  - One could modify clothing to prevent wear. This can be done by adding an ARMORLEVEL:1 token. Aside from a possible FPS gain, this has other benefits as well. This fix is part of the Modest Mod as an optional "Eternal Fashion module". It might also be found in other mods which are based around Modest Mod. (Search the DFFD for "Modest".) Also, Masterwork Dwarf Fortress allows the creation of metal clothing.

- Some mods have been created specifically to improve performance. They often reduce and standardize materials (like leather and bone) and may reduce the types of clothing available to control item count (especially for invaders).
  - Accelerated Dwarf Fortress for v0.34.11
  - Modest Accelerated Mash for v0.40.x
  - Modest Mod for v0.42.x has the Accelerated module

## DFHack commands

A list of DFHack commands that can help with your framerate by fixing bugs and reducing items.

- Useful for mass dumping or destroying items. Use for options.

- Confiscates and dumps garbage owned by dwarves. Use for options. Can cause unhappy thoughts if no replacement clothing is available.

- and Removes contaminants from tiles/units/items or one tile. Use for options.

- Counts map blocks with flowing liquids, which slow the game down.

- Further improves temperature update performance.

- alters the game simulation speed so that it \*feels\* fast even at low FPS. Either the calendar, or the units themselves, or both, can be changed - so while your actual FPS sits at a measly 20 will make the calendar tick and the units move five times faster. This is very useful to extend the playability of older forts where early micromanagement isn't as important and most of day-to-day functioning runs itself.

- Causes dwarves and other creatures to move and work faster or causes them to teleport. Run for more information.

## Mac OS X Specific

Spotlight indexes files on your mac. Since DF constantly changes files, spotlight will keep indexing them using 60-70% of your CPU. Exclude DF in system preferences: spotlight's privacy settings (by dragging the save folder into the list or pressing the button) and you can get a factor of two in FPS. This can easily provide benefits of over 30 FPS, even on multicore computers that do not need to worry about CPU. This is due to the fact that DF is not multi-threaded in any significant way.

Note that excluding the save folder from Spotlight means you can't use Spotlight or Finder to search through the raw files. If you need to for some reason, you can use "find" from the command line for this.

## GNU/Linux Specific

Placing the whole df_linux directory in tmpfs using Anything Sync Daemon might improve FPS depending on your system.

If you run any indexing, exclude DF directory.

Installing mimalloc or jemalloc and preloading it in your ./df script to run *Dwarf Fortress* may result in improved framerates:

`#!/bin/sh`\
`DF_DIR=$(dirname "$0")`\
`cd "${DF_DIR}"`\
`LD_PRELOAD="/path/to/libmimalloc.so.2.0" ./libs/Dwarf_Fortress "$@"`

The path the malloc is installed to may vary, check */usr/lib/*, */usr/lib64/*, */usr/local/lib/*, */usr/local/lib64/*, and */usr/lib/x86_64-linux-gnu/*. The .so file's name may also vary.

## Mac OS X or GNU/Linux Specific

### Setting process niceness

One thing that Unix-like systems feature is being able to control the priority of a process in relation to other processes running at the same time. This is its "niceness" value, with -20 being most favorable to the process. Some graphical task managers can set this value, but otherwise, you can use the "renice" command as so:

`sudo renice -n -20 -p $(pgrep Dwarf_Fortress)`

This command should work in most distributions of GNU/Linux. For macOS (whose Dwarf Fortress binary uses Windows' naming convention for some reason), use:

`sudo renice -n -20 -p $(pgrep dwarfort.exe)`

## See also

- System requirements - hardware changes affecting framerate
