# Quickstart guide

> Fonte: [Quickstart guide](https://dwarffortresswiki.org/index.php/Quickstart_guide) — Dwarf Fortress Wiki (GFDL/MIT)

*For installation instructions, see Installation.*

*This is a quickstart guide for dwarf fortress mode for those who have never played before and quickly want to jump in head-first.* *If you are looking to learn adventure mode instead, see the Adventure mode quick start guide.*

*Also see Tutorials for more detailed tutorials that people have submitted.*

So, you want to play **Dwarf Fortress**, but you have no idea what to do. That's understandable; in *Dwarf Fortress* you can really do anything you like. It is a huge, complex, and totally open-ended game. But in order to do anything, first you need a sustainable fortress. It turns out that this is not as hard as you might think.

As this article doesn't always contain the exact key sequences needed to do everything described, you will likely need to refer to the Fortress Mode Reference Guide and the rest of the wiki while reading this.

# Common UI Concepts

Contrary to what you might be used to, the *Dwarf Fortress* interface uses a combination of key presses, instead of clicking through menus with the mouse, so, for example, instead of clicking on the Build menu, then on the Workshop submenu, and finally on the specific workshop, you press --. All the keys you can use in a menu are shown in green somewhere on the screen. (If you see any displayed in red, those are added through DFHack.)

This is just the Quickstart Guide, so we skip lots of details on the UI. If you're looking for more UI help as you get deeper into your first fortress, you may also want to read this section in the Fortress Mode Guide.

## Options menu

Most basic game-related tasks (saving, keybindings, sound, etc.) are performed through the options menu, which can be reached with from the main screen.

To save and quit back to the main menu, select . Note that there is no "save and continue" option, but saves can be backed up and reloaded. (If you have DFHack, you can use the *quicksave* command.)

or ! These will essentially cause you to lose your save.

## Init Files

Some items related to gameplay (graphics / tiles used, features enabled, population cap, etc) are not available from in-game options screens, but instead are changed by editing certain text files located in the game's data/ folder. Most of these can be safely ignored for first-time players. However, you may wish to make a couple changes before you start:

- In init.txt, change screen size, or set up tilesets or alternate font instead of the default ASCII text interface. (Note that the rest of this guide uses the default font settings.)
- In d_init.txt, enable Autosave and/or change the save interval. Dwarf Fortress does crash occasionally, which can mean hours of lost work. Auto-save checkpoints your fort periodically (season, year, etc) so that in case of computer disaster things can be restored from somewhat recently.

# World Generation

First, generate a new world. *Dwarf Fortress* worlds are always procedurally randomly generated - there is no "default" or "standard" world. Luckily, the basic version of this process is simple, and with these suggested settings won't take too long. Wait until the game shows that the world has been generated, in this case at year 125, since stopping history too soon can limit material availability for embark and trade.

# Embark

Embarking is the process of choosing a site, outfitting your initial dwarves, and sending them on their way. Select from the main menu, then . The game will load and update the world, then show the **Choose Fortress Location** screen. There are three maps: Local, Region, and World.

- **World** shows the whole world.
- **Region** shows all of the region tiles in the part of the world indicated by the cursor on the world map.
- **Local** shows all of the local embark tiles in the region tile indicated by the cursor on the region map.

In the local map area is the highlighted embark area that you can move around with and resize with . This highlighted square will be your play area after you embark; you cannot directly act or see details outside of this area during your game. Use to move the region and world cursors around. Hold down while doing this to move more rapidly.

## Choosing a Good Site

Choosing a good embark site is crucial for beginners. Highly skilled players can run a fortress on an evil glacier, but for now, stick to friendly environments. Look for features in an embark site that will make your first fort easier to manage.

While finding a site is not as simple as world generation, the ind tool can help quite a bit. Use to change the criteria as shown to the right, then press to start the search.

If the search completes and the world map is covered with red flashing s, that means that it couldn't find any area matching your criteria. The criteria list shows which criteria it couldn't meet in red for the closet match — try changing or removing the red criteria and searching again. Or, you can put only some criteria into the tool (at the very least, No Heavy/Varied Aquifer) and add more to narrow the search. Note that "Calm" is classified as Neutral with Low Savagery (see the chart here for why) and that Neutral is Medium Evil on the finder criteria, while Good is Low Evil.)

Once the find tool has finished searching with matches found, press to look at the results. Any region in which it found a match will be indicated by a green flashing on the region and world maps. Since the find tool **only** indicates **regions** containing matches, you will need to check the local map manually (with ) until you find the most suitable site. Don't forget that there can be multiple biomes to check with , , etc.

Additionally, you can resize your embark area using . A 4x4 embark (the default) is usually reasonable, but you may want to change the size to avoid an undesirable biome or match your finder criteria.

If you are unable to find a site that you are willing to embark on, you could always create a new world. Otherwise, once you have the right area highlighted on the local map, press to move onto the next step.

## Skills and Equipment

Now the **Prepare for the Journey** screen should appear. You will be given the choice to either:

-

- .

Selecting will start you out with a default set of equipment that is reasonably safe, allowing you to skip having to set up your skills and equipment. If you'd like to get going now, just select that option.

# A Minimal Fortress

At this point, you have embarked, and your dwarves have arrived at their destination. You will see your dwarves clustered around their wagonful of supplies, somewhere near the center of your map. **Immediately hit to pause the game** unless it is already paused.

## Surveying the Area

**Do not unpause the game just yet.** Take a look around. Use the command and the arrow keys (remember that +arrow keys will move faster). Look up and down a few z-levels with and ( and on many keyboards). The mousewheel will zoom the map in and out. Place the cursor on various tiles to familiarize yourself with what the symbols mean. If you get lost, you can press (or on some systems) to return to the wagon. (You can define more hotkeys later, to jump quickly to other sites of interest.) Notice the terrain features, the vegetation, and any minerals visible. If you chose a site with flowing water, where is it? What about pools of water? The more carefully you examine your site before breaking ground, the better off you will be.

Remember that this is more of a simulation than a game. It is not "play balanced", and you can very easily find yourself in impossible situations. That is all part of the fun, because even when you lose, you create an interesting story. Your wagon serves as the initial meeting area for your dwarves. Since you should have started in a non-freezing, calm (low savagery), non-evil biome, you shouldn't face any immediate danger, but if for some reason the area around your wagon proves to be unsafe, immediately designate another meeting zone using (see Temporary Meeting Area below).

## Controlling Your Dwarves

The first thing to keep in mind is that, for the most part, you can't directly control your dwarves the way you control characters in a typical fantasy RPG. Instead, you **designate** things that need to be done and then dwarves with the appropriate labor assignments will decide what to do.

Some tasks receive a higher priority. For example, if a dwarf needs to eat, then he will go eat, and only get around to digging a tunnel once he is done eating. It is also possible to designate things that no dwarf is able to do. For example, if you designate an area to mine, but no dwarf has mining as one of his allowed labors, or no dwarf has a pick, then the mining will never get done, and the game will not always advise you of why.

So, what you are doing throughout the game is essentially giving your dwarves a detailed group-wide to-do list, but it's up to them to figure out which one of them will execute any given task if the task is even possible. Often many of the details of how a task is performed (such as exactly which rock will be used to make crafts) are left up to them (though you *can* specify the details of tasks, such as the material or design, in the etails menus in workshops).

### *Stout Labor*

**Labors** are how you control what types of tasks a dwarf will do. For example, if the Fishing labor is enabled for a dwarf, that dwarf is allowed to engage in fishing. When dwarves are idle, it could be because you haven't given them anything to do, or it could be because none of the idle dwarves have been told that they're allowed to do the types of tasks you've designated. For example, if you designate an area to mine, but none of the dwarves have the mining labor enabled, they will all just sit around ignoring your mining designation, thinking that it isn't their job. Dwarves will automatically have some labors enabled if they start out with skill in those labors, and some labors (such as hauling and cleaning) are enabled for all dwarves by default. This is why you didn't need to enable any labors on dwarves to get them to haul and mine, but later you may need a labor that no dwarf is currently capable of. Look over your dwarves' assigned labors: Press (View Units) then place the cursor on a dwarf. Now, press - for "preferences: labors". You will see a list of labor categories that you can navigate using and . You can enter each category with (except for mining, which is a single labor), toggle each labor off and on with , and get back out with . After exiting the View Units menu, you can use (the units screen) to help you locate dwarves. Hit , select a dwarf, hit for "zoom to creature" and you'll automatically be placed in view mode on that dwarf. (Then use - to get to the labor configuration menu if necessary.)

Even if no dwarves have the corresponding skills, ensure the following labors are set as specified:

| Category | Labor | Dwarves Assigned |
|----|----|----|
| Woodworking | Wood Cutting | 1 or more |
| Stoneworking | Stone Detailing | 1 or more |
| Hunting/Related | Hunting | 0 (disabled for all) |
| Farming/Related | Wood Burning | 1 or more |
| Farming/Related | Plant Gathering | 1 or more |
| Fishing/Related | Fishing | 0 (disabled for all) |
| Metalsmithing | Furnace Operating | 1 or more |
| Metalsmithing | Armoring | 1 or more |
| Metalsmithing | Weaponsmithing | 1 or more |
| Metalsmithing | Blacksmithing | 1 or more |
| Metalsmithing | Metalcrafting | 1 or more |
| Jewelry | Gem Cutting | 1 or more |

It's important to disable fishing and hunting until you have your initial fort completed — dwarves with these labors enabled will constantly be outside attempting to perform them. When you're first starting out you don't want dwarves wandering around alone where they can get killed (in addition, they won't be doing anything useful, like hauling). Note that *any* unskilled dwarf can perform any labor given the necessary equipment and materials. Dwarves with no skill will simply be slow and produce a smaller quantity of lower-quality goods in a given time period, but they will gain skill points as they do so.

## Strike The Earth!

Decide where you will build your main entrance. Generally, you will want to get all your dwarves and supplies inside a protected area as quickly as possible. The best strategy is to put the entrance near your wagon to speed up the process of hauling all of your supplies inside.

The esignations menu allows you to select areas to dig. There are multiple methods of digging:

- **Mining** removes solid, floor-to-ceiling terrain (natural 'walls') on the z-level selected, leaving behind a rock or soil surface (also referred to as a natural floor). This does **not** do anything in areas without natural walls (for example, the surface or previously-mined areas).
- **Channeling** removes *natural* (rock/soil) floors (either created naturally or by mining) and creates a ramp (▲) on the z-level below. Note that you will see a down arrow (▼) on the current z-level, indicating a ramp on the level below. (For best results, ensure that the area below is unrevealed, i.e. black).

To designate an area for digging:

1.  Hit to bring up the Designations Menu.
2.  Hit to mine or to channel (see above)
3.  Place the cursor on one corner of the rectangular area you want to designate and press .
4.  Move the cursor to the other corner of the rectangle and press . A rectangle will be highlighted and a miner will start to dig out this area once you exit the menu (with ) and unpause the game with .

This is basically how all of the designation commands work. Everything has to be designated one rectangle at a time, but rectangles can be many tiles wide. After you press to designate, make sure it's set to "Standard" in the settings at the bottom, rather than "Marker only." You can set this with . If it's set to "Marker only", the designation will not be carried out.

If your wagon is near a cliff or hill (generally speaking, any difference in levels, usually shown by the existence of natural ramps), you can just designate a tunnel to mine (-) into the cliff to create an entryway. If the wagon is surrounded by flat terrain, channel out a 3x3 rectangle on the surface with - to create a sort of pit with ramps on the edges, then go down one z-level with and tunnel into one wall of the pit (with -) to create your entry.

Dig a hallway one tile wide and *at least* 10 long, ideally more like 20 ( moves 10 tiles when digging, so this can be easily accomplished by pressing +an arrow key twice). This will be your entryway.

Your entryway defines the boundary between your safe and protected inner fort, and the big, bad, outside world. You want this to be your only entrance, so that you only have to worry about defending this one opening. A somewhat-outdated video guide to starting a fortress can be found here. (Note that this applies to v0.34.11, not v, so some parts may be inaccurate in the current version.)

### *Additional miners*

Mining will go faster if you have more than one dwarf doing it. By default, only one dwarf has the Mining labor enabled, but this can be changed fairly easily:

- Choose a dwarf that isn't doing anything especially useful (the fish cleaner is a good choice for a beginning fortress, but you can always change your mind if you end up with a useless peasant later on)
- Press , navigate to the dwarf, and press -
- Enable the "Mining" option (see Stout Labor above)
- Exit with

The next time you designate an area for mining, both of your miners should start working (assuming they're not busy doing something else).

**Notes:**

- Each miner requires a pick. A standard embark comes with 2 picks. If you want more than two miners, you'll need to forge more picks (forging is covered later in this guide). Two miners should be adequate for most fortresses, but more miners can add reliability (for when a miner decides to sleep) and speed. For now, you'll almost never need more than two miners, but you'll want more once your fortress expands.
- If you're digging a one-tile-wide hallway, only one miner can work from an end.
- Mining, Wood Cutting, & Hunting labors are mutually exclusive - a dwarf can only have up to one of these professions active at a time. For this reason, it's not recommended to make your only woodcutter a miner, since they won't be able to cut wood anymore.

## Delving Secure Lodgings

Near the middle of the entry tunnel, build a 5x5 room, and link it to the entrance tunnel with a 3-tile-wide passageway. Expand the main entry tunnel to *three* tiles wide from the entrance of the new room to the outside entry. At the end of the entry tunnel, dig a small room, which will later become your main stairwell. Two tiles past that, dig a larger room, which will later become your general stockpile, and connect it to the stairwell with a narrow passageway.

### *Room dimensions*

Apart from wagon access (3 tiles wide), the trade depot (5x5), and other workshops (3x3), there are no fixed dimensions you need to worry about. The lower limiting factor is the traffic your tunnels receive (dwarves may have to start climbing over each other), and the space your rooms need (stockpiles, tables/chairs, livestock). The practical maximum size is limited by how long it takes your miners to dig the rooms out, especially if they're digging in stone instead of soil (digging through soil is much faster). Most sites have at least one level soil layer below ground level, which is where you're digging right now, but as you dig deeper you'll hit stone (if you haven't already), and digging will become slower. In most fortresses, even the main hallways never need to be wider than 3 tiles, and needing more than 3 tiles of stairs per floor is very rare. A 3x3 per floor staircase (9 stairs!) is absolute overkill for anything but 20-year-old 300-resident capitals. For most tunnels in your fortress, 2 tiles wide will be sufficient, and many will be fine at just 1 tile wide. 11x11 is a convenient size for stockpile rooms, as the +arrow keys move the cursor 11 tiles. However, something smaller is perfectly fine for rarer stockpiles, offices, and small dining rooms. Commoners’ bedrooms need not be larger than the amount of furniture you want inside.

### *Mining safety*

While mining, take care to avoid digging into water. Dwarves are usually poor swimmers, and are unlikely to escape from an underground flood. However, it is safe to mine *next to* underground water, as long as you leave at least one "wall" tile between them (see the picture to the right). You can also mine one z-level under a body of water (for example, mining under a river), but you will have to designate each tile individually because DF automatically cancels digging of newly-revealed "damp" tiles (tiles are considered damp when they are adjacent to a water tile, regardless of whether the water tile is on the same z-level or not).

Also note that **water can flow diagonally**: \ \[#00f\]≈\[#\]▓.▓ \[#00f\]≈\[#\]▓.▓ ▓▓.▓ ▓..▓

\[#0f0\]ok\[#\] \[#f00\]flood\[#\] \

### *Stockpiles*

**Stockpiles** are very important. These areas are where your dwarves will drop things for storage when they aren't needed elsewhere. To create a **general purpose stockpile** for your first storage area:

1.  Hit to open the Stockpiles menu.

2.  Use to change the custom stockpile settings to nable everything but **Corpses**, **Refuse**, **Stone**, **Gems**, and **Wood**. Use directional keys, nable, isable to do this.

3.  out of that screen back to the stockpiles menu.

4.  Hit to select Custom Stockpile, if it isn't already selected.

5.  Designate the whole 11x11 storage room as a custom stockpile. This works just like designating an area to dig: place the cursor on one corner of the room, hit , move to the opposite corner, and hit again.

6.  Press to get out of the Stockpiles menu.

Once you exit the stockpiles menu and unpause, you should see dwarves running off to haul everything from your wagon into the new stockpile area. Later, if you like, you can change what sort of things the stockpile accepts by hitting (Set Building Tasks/Prefs), placing the cursor on the stockpile, then pressing to get to the stockpile settings.

It is particularly important to **keep wood, stone, refuse, and corpses out of your general purpose stockpile**, so you may want to double check to make sure all of these things are disabled in the stockpile settings. Failure to keep these things out of this stockpile will rapidly fill it up, causing workshops to become cluttered when dwarves can't store things in the stockpile. **Note:** When assigning stockpiles, you should make sure they're in a vacant area (i.e. the tiles should not have any items already stored on them). Dwarves will not haul items to occupied tiles, so make sure the area is vacant (and already mined out) before assigning a stockpile.

### *Stairways*

Designate a downward stairway in the room you dug out for the stairwell (*not* the 5x5 room that you dug out earlier) with . Notice that after your miner digs the stairway, it doesn't automatically create another stairway on the z-level below. If you hit to move the view down a z-level you'll see that there's no stairway below, but there is a revealed tile of rock/soil. Because of the down stairway that was dug, this tile is now accessible to miners. You can then designate an up/down stairway on it with and the miner dwarf will dig it out. Below that you can then dig out another up/down stairway and so on. For now just dig down one level; we will deepen the stairwell later.

## Temporary Meeting Area

On the second z-level below ground (the one below the stockpile level, which you just reached with the staircase), dig a short, 3-tile wide passageway (this only needs to be 1-2 tiles long). Past that, dig out a room between 5x5 and 7x7, leaving room to enlarge it in at least one direction in the future. Using the key, create an activity zone in the room you just created, filling the entire room (be careful not to make this too small lest your overcrowded animals start fighting). This works much like creating a stockpile except that you draw the rectangle before defining what the area is for. Draw the rectangle, filling the entire room, and set it to be a eeting area. Your idle dwarves will hang around in this area, hopefully keeping them inside the fort and out of trouble.

NOTE: Again, make sure your activity zone is already mined out before attempting to designate the meeting area.

## Refuse

Outside your fort entrance, use followed by to create a stockile for efuse *at least* 5x5 in size. This should be outside in the open or you will have problems with Miasma. If you do not disable vermin (Item Types -\> remains), you will probably have to expand it later as it will fill up with vermin remains rather quickly. If you are seeing refuse appear in your general-purpose stockpile instead of the refuse pile, use on the general stockpile and check its ettings to make sure refuse has been disabled.

## Food

Food is necessary for your dwarves' survival - to keep functioning, they require constant supplies of food and drink - the stock screen can be used to monitor how much food and drink is available. Luckily, your dwarves will eat almost everything raw, including plants.

### *Farming*

For a reliable, long-term food and alcohol supply, you'll need to set up a farm. Dig out a medium-sized room in a soil layer (including sand, clay, loam, silt, peat, and ooze) accessible from inside your existing fortress. 5x5 is a good size to start with, but you'll want to leave room to expand in at least one direction. You must pick an *underground* area with mud or soil\*. Placing this near the stockpiles is more efficient, since farmers won't need to travel as far.

_(\* Hopefully you have chosen a site with a soil layer, which will make farming much easier, but if not you will need to irrigate to create the required mud on stone floors.)

Use - to build a 3x3 farm plot in the room you just created. Notice that some types of buildings (as well as most constructions) are not designated corner-to-corner like digging designations, stockpiles, or activity zones. Instead, you define the length and width of the building using and position it with the directional keys. Use to make the plot 3x3 and position it in the room, ideally near the wall to leave space for more plots later on.

Remember that you must enable the labour for at least one dwarf, or the farm plot won't get built and farming will not take place. (If you selected "Play Now" earlier then you will start with a dwarf with farming enabled.)

out of the build menu and wait for the farmer dwarf to create the plot. Once the plot is built, use to set the plot to grow plump helmets during all seasons. You can use and to select plump helmets (pressing once should do the trick). Select with . **You will need to press , , , and select Plump Helmets for each season** — otherwise you'll end up with an idle field for 3/4ths of the year.

Later, if you are curious what is planted in each plot this season and how much, select the View Items in Buildings command and move to the farm plot.

Note that a default embark starts with *five* plump helmet seeds — for now, only half of your field will end up being planted. Eventually, as your dwarves consume plump helmets, more seeds will become available and will be automatically planted by an unoccupied farmer.

*For more troubleshooting tips, see How do I build a farm*

### *Emergency food sources*

Occasionally, even with a working plump helmet farm, you may experience food shortages. For now, you should have plenty of food on hand left over from embarking. However, if you ever run low on food, there are a few ways to obtain more:

#### *Plant gathering*

If you have shrubs () growing above ground, you can harvest plants from them. Note that this requires a dwarf with the labor enabled (under ), and time (this can take a while for an inexperienced dwarf, and it doesn't always yield edible plants). To start, esignate some lants to be gathered on the surface (similar to selecting an area for mining, except it only selects plants in the given rectangle). Once processed, some will leave behind harvested plants (often edible berries).

#### *Butchering*

If you suddenly run low on food, butchering an animal is another option. Build a butcher shop (, , ) and mark one of your animals for slaughtering (press , move the cursor to the animal, then press , ). A dwarf with the butchering labor enabled will haul the animal off to the butcher's shop, work for a while, and produce neat stacks of meat products.

## Building material

Initially, wood is probably a good choice for building material, as it's lightweight and can be easily obtained. You will need plenty of building materials as your fortress grows, but wood will suffice for now. If you are unable to locate enough wood (or if you run out of trees, which is unlikely at this point), extend your staircase down to a stone level (-) and mine out a small area (at least 5x5) to obtain stone.

Even if you don't have trees, you can obtain 3 logs from your embark wagon. Press , place the cursor on your wagon, and hit to deconstruct it. This will flag the wagon for disassembly. Eventually a carpenter will come along and turn the useless wagon into 3 units of wood. (Removing other buildings is done the same way.)

### *Woodcutting*

Assuming your site has trees above ground, now is a good time to start obtaining wood. Create a stockile for ood outside your entrance (preferably near to it). As it will only be temporary, don't make it too big (maybe 5x3, or 15 tiles total). Later, you will move this closer to your carpenter's workshop (once you build one), so don't worry about placement too much. Also near the entry, designate a couple of trees to be chopped down with -. One tree will produce many logs, so only designate three to five at this point. If you designate too many trees, your woodcutters will spend all of their time chopping them down and hauling the resulting logs, instead of doing other work. As soon as one tree is cut down and its wood stored in a stockpile, you can proceed to the next step (your woodcutter will continue cutting down any remaining designated trees).

## Drinks

Drinks can be more problematic than food, since they require more preparation (except for water, that is). In warmer weather, you can specify a "water source" activity zone (-) around a lake or river on the surface to keep your dwarves from dying of thirst, but dwarves deprived of alcohol slow down and become unhappy. In addition, drinking outside can be dangerous — dwarves running outside constantly risk running into wild animals, or worse. Creating a still to brew alcohol is the simplest solution to these problems.

You need a brewer to brew drinks. Unfortunately, your brewer is also your woodcutter (with a default embark), who is busy cutting down trees. You will want to make a different dwarf your brewer instead, since both your brewer and woodcutter will be busy (and one dwarf can't do both jobs at the same time).

1.  Find your woodcutter in the nits list, select it, and press (this selects the dwarf without you having to search your entire map). Use the - menu to disable brewing (located under "Farming/related" — you can navigate this menu with the and buttons).
2.  Pick another dwarf that isn't doing anything useful. Right now, this can probably be your fish cleaner, but you can change this as soon as some migrants arrive (by following these steps again).
3.  Use the --- menu again to enable brewing on the new dwarf.

Assuming you have building materials available (which you will if your woodcutter has been doing their job), you can now create a still:

1.  Dig out a 3x3 area connected to the farm plot.
2.  Use -- to build a still. Position it in the 3x3 area you just created and press .
3.  Use to select a building material for the still (this is probably one of the logs you just cut down by default).
4.  Use to exit the menu, and unpause the game.

After a short delay, your new brewer should run off, drag a log over to the workshop site, and build the workshop. (This is also how building other workshops works, but you won't need to do that yet).

To brew drinks, use to select the still and press dd task-rew drink. **This will not work yet**, since you don't have any empty barrels or rock pots, but you should start brewing in the first six months (see Calendar and Status).

## Pasture

If you have any grazing animals with you, such as the draft animals used to pull your wagon, they will die if they are kept away from grass for too long. Use to create a Pe/Pasture zone over a grassy area outside and assign your grazing animals to it using (while still selecting the zone). This area needs to be about 10x10 or so to ensure they have enough grass and don't trample it all. The amount of grass required varies greatly, depending on the type(s) of animals being pastured. If you intend to keep grazing animals permanently, you may need vastly larger pastures later. As an alternative, you might wish to slaughter your largest animals for food and materials.

## Designing your first fortress

While this guide recommends a vertical fortress design around a central stairwell, with each z-level being used for a particular purpose, it is not really that important to use this design for your first fortress. Therefore, feel free to put any of the areas described in the rest of this guide on your main level or wherever you want as long as dwarves can get to them without going outside the fort. In other words, you can think of the "levels" described in the guide more as areas that can really all be on the same level if you have space. Later you can ponder over what makes things most efficient, but for now just do whatever you find easiest. Note that you may need to dig down a bit to get to stone if you have more than one z-level of sand/clay/soil below the surface.

## Workshops

Most labors of your dwarves need a place where they can process raw materials — workshops. Almost all of them occupy a 3x3 square, and most of them require just 1 unit of any building material (wood, stone, metal). Dig your stairwell down one level (with ), if you haven't already. It's fine if this layer is soil — in fact, soil is better, since it's easier to dig through (if you only have one soil layer, you can put these workshops somewhere on your first level). Dig space for your workshops off of the stairwell. It will hold your mechanic's, mason's, carpenter's, and jeweler's workshops. Something to consider is stockpile proximity: the farther away the material is the dwarves use, the more time they waste with walking. So for now, dig out some more space for stockpiles close to where your new workshops will be (wood for your carpenter, stone for your mason and mechanic, and gems for your jeweler). It doesn't matter if you put everything in one large room or dig out small rooms for each workshop and stockpile. Note however that some tiles of workshops are impassable: they appear as dark green 'X' when you choose a location (the specific wiki pages of the workshops also show you this). So before you build small 3x3 rooms for each workshop, make sure your dwarves will be able to reach them. Once you've dug out your rooms, set your miners to work by adding a z-level or two to the staircase (you can designate multiple z-levels at once using and , just like moving up and down). Hopefully you'll obtain some stone by doing this, which will be useful eventually. While your miners are busy, use to build the workshops, using whatever building material you have. If you are still digging in soil and don't have stone yet, just use wood; the material really doesn't matter in this case. Be sure that your craftsdwarves still have labors corresponding to each workshop enabled (see Stout Labor above) so they will begin construction. (Dwarves already busy mining or hauling may not immediately stop to construct workshops; if you like, you may temporarily disable other labors in order to jumpstart workshop construction.) If the construction of any building gets "suspended" just use to unsuspend it. (This can happen if another dwarf or object is blocking the way. See Garbage Dumping below if you find you need to remove an object.)

Remove the temporary wood stockpile you created outside (using and selecting the entire stockpile) and dwarves will move the wood to the new wood storage area.

Go to your mason's shop with and use to queue up one able and one throne/hair. You will find out why you need these in a second, but now is a good time to start building them. If you still don't have any stone at this point just use wood at the carpenter's workshop.

At this point, it is a good idea to build a few wheelbarrows to make hauling large objects (particularly stone) more efficient. Queue up 2 or 3 at the carpenter's workshop. (Wheelbarrows are located near the bottom of the list, on a separate page. They are not visible initially, so you'll need to scroll with or — scrolling up with is more efficient, as it wraps to the bottom of the list.) While the wheelbarrows are being built, select your stone stockpile with and use to increase "Max Wheelbarrow" to 3 (the maximum). Your dwarves will automatically move wheelbarrows to the stockpile once they are built.

### *"Where did I build that \_\_\_\_?"*

As you build workshops, furnaces, Trade Depot, other buildings, rooms and even zones, you may start to lose track of where they all are -- or where they're supposed to be built, but some dwarf is too busy eating/drinking/hauling. There are a couple of commands available from the main UI that will help you locate what you built.

- You can View ooms/Buildings to see a Building List, and also Zoom o the building/item, or uery the building tasks.

- For incomplete buildings/constructions, you can also open the ob list and then Go to uilding to find the intended location.

## Brewing

You'll need barrels to store drinks for your dwarves. The stockpile you set up earlier will use as many barrels as possible to store items in, which means they can't be used to store drinks. To change this, press to access the stockpile menu and use to increase the number of "reserved" barrels (i.e. barrels kept out of stockpiles - 5 barrels is good for now). Queue up two or three barrels in your carpenter's workshop with -. (If you run out of wood at any point, cut down another tree or two outside). If a lack of wood cancelled a job, you will need to queue the job again. Go back to your still and order some drinks to be -rewed. Each drink requires one barrel and one edible plant, such as a plump helmet. Even if none of yours have been harvested yet, you should have some left over from embark. Also, brewing plump helmets creates *two* seeds from one plant, which makes plump helmets an excellent choice for a beginning fortress. Five barrels should be plenty for now (each plant makes 5 "units", or servings, of booze, and dwarves don't need to drink too often, so 30 units should last you a whole year. When the stocks get low, you'll probably want to start queueing up more drinks to be made (you should have more empty barrels by then)).

## "Garbage" Dumping

**Note that garbage is not the same thing as refuse.** Refuse is rotting stuff. Garbage is anything you designate to be hauled to a garbage dump, even important things that aren't really garbage. Think of your garbage dump zone as a way to specify that objects you select will be brought to a specific area.

Use to create a 1x1 activity zone somewhere near your mason's and mechanic's workshops and set it to be a garbage ump. Unlike stockpile areas where you are limited to storing one object per tile, any number of items may be piled in a garbage area. That means you will only need one tile to hold as much "garbage" as you like. Although many of the room sizes in this guide are suggestions, think of the 1x1 garbage dump size as mandatory. At some point you will probably want to retrieve an important item from your garbage dump, and the more tiles your dump contains, the harder it will be to find anything in it. Press - to get to the mass dump/forbid screen and select the ump option. With "dump" selected, designate a rectangle over the loose stones cluttering up your living area (if there are any – this often isn't a problem yet if you've built your fort in a soil layer). This will designate this stone to be transported to a garbage dump zone. Be sure not to designate the stone in your stockpiles by mistake, since that will only cause your dwarves to perform unnecessary hauling. Once the stone from your living area has been moved there, it will be set as forbidden. Before it can be used you will need to unforbid it using the same - screen, hitting to claim it. Note that dwarves hauling stone (or any large, heavy objects) move slowly, and can take a lot of time to reach their destination. This can be a major waste of time if you designate 50 boulders to be dumped at once. Unless the stone is in the way of something, you don't *need* to dump it every time you dig out a new area. Stones lying on the ground don't slow dwarves down at all. If there is a particular dwarf you don't want hauling "garbage", you can disable the "Refuse Hauling" labor (under the "Hauling" category). Miners are good candidates, since they are far more useful when digging than when moving the stone they just dug out.

Congratulations! Knowing how to use garbage dump zones puts you head and shoulders above many new players - it takes some people weeks to figure this out.

## Trading

Not all embark sites have all the resources you need for a successful fortress, but every site has *something* you can sell. A talented dwarf can process any useless resource into something valuable, and trading is a good way to sell those goods.

*Note that producing goods creates wealth and getting too much wealth too fast can have unwanted consequences.*

### Trade Depot

Build a trade depot using - in the 5x5 room you created near your entrance. This is where caravans will park their stuff and where trading will take place when one arrives. (as stated earlier, the wagons are 3x3 so the entrance tunnel needs to be at least 3x3 for the wagons to go by). You will need one architect, which will be enabled on your mason if you selected at embark. You also need at least 3 logs or boulders to build the depot.

### Producing for export

While there are some goods that are more valuable, and some that are less valuable, it's a good idea to simply produce/export what you have too much of and to import what you have too little of. Generally though, Gems and Finished goods are decent exports for a new player.

### Trading

Once a caravan has arrived, you can mark the goods you want to sell through the Trade Depot, and your dwarves will begin moving them to the depot. Be careful not to sell wooden items to Elves; **this includes containers:** even a wooden bin full of metal crafts will make them upset. Also note that the traders will want to make a profit off of you. While they're happy with about 200%, the more profit they make on your site, the more goods they will bring next time, so it can be a good idea to give them even better deals.

*A more detailed overview of the entire process is here.*

### What to buy

In your first fortress, your priority should be importing some food and alcohol. In addition, you might want more livestock, seeds (comes with a free bag), and - depending on what resources you are missing - additional picks, barrels, wood, bags, as well as rope and a bucket (for a well). While you're at it, check if you need an anvil. Maybe you forgot to bring one, or a kea stole it. Always having a small supply of *all 3 kinds* of cloth, some gems, leather, a bit of sand (free bag!) are handy to have, as those are hard to come by on short notice. If you're short on weapons-grade metal for your military, import not only actual metal bars and ores, buy *all* metal goods you can afford and melt them down in a smelter to increase your yield.

### Troubleshooting

Once the depot is built, use from the main menu to make sure your depot is accessible. (This command is only available once the depot is built – before building, the command will be disabled, and while the depot is under construction everything will flash red until the depot is built). Once completed, checking epot access will flash some of the following symbols:

-
  This tile is not accessible by wagon. This could be because something is blocking it (a tree, a natural boulder, etc.).

-
  This tile is accessible by wagon. (These tiles will radiate outward from the depot, not from the map edges.)

This is good, but does not guarantee wagons will be able to reach the depot. Make sure you see the words in the menu.

- The depot is accessible via wagon.

- The depot is **not** accessible by wagon. See below.

If you see the message in the menu (or the ) symbol over the depot, try these solutions:

- Is the path to the depot (in your fortress) less than 3 tiles wide? If so, expand the entranceway and try again.
- Are there trees blocking a path to the depot outside? Try clearing a path by cutting down a few (you probably won't need to cut *all* the trees in a 3-tile wide path); usually cutting some at the end of a path of 's clears a path.
- Are there boulders () blocking the path outside? To remove them easily, you need an engraver. If you selected "play now", you should have one already. Select -mooth Stone and designate the boulder(s) for smoothing. They should flash this symbol:
- Is the path to the depot only accessible via stairs or did you build traps in the way? Wagons cannot pass traps or stairs, even if they're 3x3 wide.

It's possible that there are multiple obstacles blocking the depot, so keep checking epot access until the message appears.

*Note that even if your depot is inaccessible to wagons, traders still will come without wagons. They will carry much less goods and you can sell them much less, because their carrying capacity is greatly reduced.*

## Migrants

At some point soon, you'll most likely be getting migrants (if you haven't already). You'll usually get between 5 and 15 migrants in the first 2 waves, which occur sometime during your second and third seasons. See this page for advice when you receive migrants.

## Bedrooms

Up to this point, your dwarves have probably been sleeping on dirt or rock in your fortress. While this is fine for a short time, your dwarves will gradually become less happy if they are forced to sleep without a bed. Under normal circumstances beds can only be made from wood, so be sure to designate some more trees to be cut down if you're short on logs.

Designing living quarters is largely a matter of personal preference and aesthetic sense. While a few useful designs are discussed here, there are many other options. In general, try to keep the bedrooms close to the stairs, and make your access hallways at least two tiles wide to reduce congestion.

### Location

Because noise generated from certain jobs (especially mining and woodcutting) can bother sleeping dwarves, doing these jobs within 8 tiles of a sleeping dwarf should be avoided (see noise for more information). There are two ways of accomplishing this:

- Placing bedrooms at the end of a hallway at least 8 tiles long will avoid most noise (as long as you are careful to avoid noisy jobs directly above or below the bedrooms).
- Extending your fortress down several z-levels will also work (9 levels from the surface is a safe choice), although extending a 3x3 staircase takes more work than extending a single hallway.

Both options work equally well, as long as you are careful to avoid disturbing sleeping dwarves. Ultimately it depends on how you want your fortress to look.

### Layout

Due to the limited resources of a new fortress, setting up a communal sleeping area in a dormitory is often the best short-term solution. However, you can also set up individual bedrooms for dwarves.

**Benefits of individual bedrooms:**

- Dwarves are happier with their own bedroom and furniture.
- Individual rooms can increase your fort's perceived wealth.

**Benefits of dormitories:**

- Dormitories are easier to set up and expand (only one room is necessary, and each dwarf only requires one bed).
- Sleeping dwarves are much less likely to be attacked when other dwarves are around them.
- Multiple dwarves can sleep in a dormitory. In contrast, only one dwarf can ever sleep in a bedroom (dwarves cannot sleep in another dwarf's bedroom, even when unoccupied).
- Far fewer beds are needed – in a fort of 50 dwarves, for example, around five dwarves will be sleeping at a time (on average). A dormitory, therefore, rarely requires above ten beds, while individual bedrooms would require 50 beds to be built.
- Even when all of the beds are occupied, dwarves will still sleep in the general area of the dormitory. This is more convenient than having dwarves sleeping all over your fort.

For now, setting up a dormitory is easiest (although you can change this later, if you feel the need to).

### Building

Queue up as many beds as you need in a carpenter's workshop (no more than 3 or 4 should be necessary for a dormitory). Beds are queued with -- at a carpenter's workshop and built with -. (As long as your furniture/general-purpose stockpile isn't full yet, dwarves will store beds in them as they are finished, so there may be a delay before they're available to be built.)

---
⚠️ Conteúdo truncado (72526 bytes = ~18131 tokens). Para o artigo completo, visite [Quickstart guide](https://dwarffortresswiki.org/index.php/Quickstart_guide).