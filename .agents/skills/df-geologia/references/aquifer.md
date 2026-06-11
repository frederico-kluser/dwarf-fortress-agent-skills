# Aquifer

> Fonte: [Aquifer](https://dwarffortresswiki.org/index.php/Aquifer) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

An **aquifer** is a subterranean layer of soil or stone that holds groundwater. Once exposed it will start leaking water, which can lead to a lot of Fun flooding if left unmanaged. Each embark tile within the embark rectangle might contain an aquifer.

## Leaking

Aquifer tiles produce water in any *neighboring* open tiles – **north, south, east, west,** and **below**. The amount of water an aquifer produces depends on what type it is. **Heavy aquifers** are faster to produce water and much harder to manage compared to **light aquifers**. Aquifers cannot be drained; the groundwater is limitless, with even a single isolated tile leaking water forever. However, smoothed, mined, carved staircase, or channeled aquifer tiles no longer produce water. Aquifers located in ocean biomes will produce salty water; aquifers in other biomes will produce freshwater.

## Identifying

If you are digging an up/down staircase in the downward direction and you hit an aquifer, the aquifer tile will be revealed as damp soil or stone and the dig designation cancelled for that tile. If you are mining horizontally, you will similarly be warned of "damp stone" before breaching the aquifer. If there is no water next to or above these tiles, these are aquifer tiles. If you are digging an up/down staircase in the *upward* direction, or a ramp, and you hit an aquifer from below, the aquifer tile will immediately start producing water in the stairwell.

## Types of aquifers

Embark screen: Area with a varied aquifer.

The type of aquifers contained within the embark location can be reviewed in the embark screen, and each tile in the embark rectangle (default 4×4) may contain an aquifer independently of the others. In addition to heavy or light aquifer, *Dwarf Fortress* can also display "Varied aquifer" if both types are present within the embark rectangle (also note that the biomes of neighboring tiles can "spill over" into a tile, resulting in different, unannounced aquifers in those parts).

### Light aquifers

Light aquifers are by far the most common (being ~19 out of every 20 aquifers), and produce water slowly enough that they can easily be penetrated with minimal effort by digging out one level at a time and walling it off reasonably quickly. Light aquifers can be useful for low-water applications such as slowly filling a cistern for wells, or feeding a waterfall.

An open tile will receive water from a light aquifer only if it is directly **north of, south of, east of, west of, or below** a tile of the aquifer (not in the tile **above** them, nor in any diagonally-adjacent tiles). The amount of water that the open tile receives is random, on average four per month, possibly reaching as low as two or as high as six. The same amount of water is received regardless of the number of adjacent aquifer tiles.

Since water will leak into tiles **below** an aquifer, you must dig out and wall off or smooth the same tiles in every single damp Z-level you wish to utilize, or else find all lower z-levels flooded from a seemingly unknown source; the rough aquifer walls above. It may seem as though the floor is leaking water, but it is actually the ceiling. There is no need to smooth or construct floors, as only rough wall tiles will leak water. However, if what you're trying to do is dig out a cistern, the most efficient way is to simply dig a large area out from directly under an aquifer layer, since every single tile will fill with water at a steady rate until it reaches 7/7. You'll know you're digging in the right level to make a cistern when every single tile you're trying to dig out is damp stone, but the layer below is dry.

If you wish to excavate a large area within a light aquifer without painstakingly and continually walling it off, dig regular drains to an open area in a non-aquifer layer where the water can evaporate more quickly than it arrives. Note, however, that the open area that the water drains to will need to be much larger than the area of the aquifer that has been dug out. Or drain the water off the edge of the map.

Unlike heavy aquifers, light aquifer tiles do not absorb (drain away) water.

Although digging through light aquifer walls is not very dangerous, your dwarves will continuously cancel designations with the "damp stone" warning with each new tile revealed. The player must therefore repeatedly re-designate light aquifer squares to get the dwarves to mine it, making it a tedious affair. There is no way to turn off this automatic cancellation without using external tools such as DFHack or playing the premium version, as of 53.12 there is a way to ignore warm/damp stone under the standing orders tab (Labor -\> Standing Orders -\> Other)

    Alternately, once all desired tiles are revealed from above and designated for mining, when the "damp stone" alert pauses the mining activity, simply unpause for each alert (note that the unrevealed parts of designations will still be cancelled).

### Heavy aquifers

Unlike light aquifers, heavy aquifers produce water almost immediately, effectively halting excavation at or 1 z-level below the aquifer level. This, in conjunction with the fact that they are often located in areas rich in loam and sand, makes it difficult to find great quantities of stone in areas with heavy aquifers, making them more challenging.

Rough heavy aquifer walls also act as an infinite *sink* for water, just like an open map edge. A single aquifer tile can absorb any amount of pressurized water each tick, limited only by the supply. One less obvious consequence is that if an opening is made through a multi-layer aquifer, only the lowest opened layer will ever fill with water.

Empirically, heavy aquifers gain approximately 1/7 water every 14 ticks, though production has been observed to vary from 2-28 ticks. This rate does not appear to change significantly based on the number of adjacent aquifer tiles.

## Where they are found

Aquifers appear based on the drainage of the terrain. Low elevations - particularly those near rivers and oceans - are more prone to having an aquifer present, while locations closer to mountains are much less likely, but still possible. Depending on the embark location's biomes, you may embark to an area containing no aquifers, or up to several aquifers throughout your map.

Layers which **can** contain aquifers:

- sandy clay loam
- silty clay loam
- loam
- sandy loam
- silt loam
- loamy sand
- silt
- sand "Sand (tan)")
- yellow sand
- white sand
- black sand
- red sand
- peat
- pelagic clay
- calcareous ooze
- siliceous ooze
- sandstone
- conglomerate
- puddingstone

Layers which **cannot** contain aquifers, despite their names suggesting otherwise:

- clay
- silty clay
- sandy clay
- clay loam
- siltstone
- mudstone
- claystone

## Working in aquifers

Some points to keep in mind:

- Water on the tile where a worker is standing will cause job cancellations if it gets too high. A construction job (e.g. wall building) will be suspended by 2/7 depth, but a mining job will only be stopped by 4/7 depth of water.
- Flowing water will cause parents to drop their infants, leading to job cancellations, and occasionally fun.
- Aquifers do not create water in diagonal tiles, but do create water in open tiles directly below them. Therefore, you will want to dig two z-levels below the lowest aquifer layer before continuing with your fortress.

### Probing an aquifer

You can discover what layer lies below an aquifer layer by digging up/down stairs into the aquifer. This will reveal the tile below the aquifer layer, and if this is non-aquifer (such as clay, ore, or bedrock) then you know the aquifer is only 1 Z-level deep at that location. This method can only be used to determine whether the aquifer is 1 layer deep, or multiple layers deep, but this is still enough information to help plan how to penetrate it. Using a pump-based method is highly recommended for multiple layer heavy aquifers.

## Dealing with heavy aquifers

### Going around

If your embark site is covered by multiple biomes, there is a chance the heavy aquifer is not present in every biome. In some maps this may be indicated by an outcropping of stone in a landscape otherwise composed of soil; in other maps the change in biome might be visible as a change in soil type, vegetation type or density. You might be able to dig down through a biome that doesn't have a heavy aquifer, to a Z-level below the heavy aquifer, and then (if you wish) tunnel beneath the heavy aquifer to the previously-inaccessible region.

Even if all the biomes of your site contain aquifers, they might not all be at the same Z-level, so you still might be able to dig down in one biome, reaching a Z-level beneath the aquifer in another biome.

Additionally, if your biome contains deep cliffs (such as a river gorge), it may be possible to build a staircase down the side of the gorge past the aquifer.

### The double slit method

This is one of the most commonly-used methods, due to its convenience and power. It was originally developed by QuantumMenace, and is also mentioned below under the pump method.

### The hatch trick

The hatch trick is a simple method for putting one or two dwarves through a single heavy aquifer layer. (This is not to be mistaken with only working for a single layer aquifer.) You can use the trick to essentially bypass the problematic final layer of a multi-layer aquifer, allowing access to the rock layers and caverns before you've put a sealed staircase through the aquifer.

First you must dig a pair of up/down stairs into the aquifer (i.e. as in twin slit), while draining one of the tiles with a screw pump, simply build a hatch on the tile (the hatch must be built on a downstairs or up/down stairs for the trick to work). Once the hatch is constructed, with the pump still operating, designate an up/down staircase under the hatch, a miner will dig the staircase out while standing 'on top' of the hatch, he can then pass through the hatch to continue digging, the hatch will let 1-2 water through with him before closing and preventing further water from following the miner. The miner is now safely under the aquifer and can dig down to the caverns or to the map edge and establish a drain, allowing you to use the much faster drainage from below method to finish penetrating the aquifer. This can save a lot of time for multiple-layer aquifers where the final layer is sand. It is also quicker and cleaner than cave-in for single layer aquifers if you plan to extend a staircase straight down to the caverns anyway (making the drain essentially free).

### The ore method

On maps where the aquifer is not held in a layer of soil, but instead is held in a sedimentary layer such as sandstone, it may be possible to tunnel down through deposits of ore such as magnetite. For this to work you have to find a spot where there is coincidentally an ore deposit on each Z-level you need to dig through. This is only possible through tiresome trial and error, or through the use of a utility like DFHack's `reveal`. The trial and error method can be accomplished somewhat more easily by digging up/down stairs to reveal the layer underneath them without actually digging into the underlying layer. This method is more complicated with aquifers located in layers of conglomerate, as large clusters of puddingstone will support the aquifer and thus cannot be used to provide a path through it.

### The "Chicken Run" technique

When a newly revealed damp tile cancels a mining designation, and without any other mining designations, the miner will revert to "No Job" status and will take a few dozen ticks to resume mining. In that time, the miner will walk away and the site will be flooded, making the tile below unreachable. However, by digging downward staircases in the layer above the aquifer, those tiles can be revealed as damp, and thus will not trigger the mining cancellation. A sufficiently fast miner (Professional or so should do for soil layers, depending on agility) can then dig a stair in one of the tiles, and before that tile floods, channel out an adjacent tile, removing that tile and breaching the layer below; if that layer is also a heavy aquifer, it will act as an infinite drain for water from above. This then opens the possibility of digging space to work in the upper layer.

While not a direct staircase in the original method, establishing a drain with just a pick is also possible with a dabbling miner. One can channel an aquifer tile from up to four ramps dug at the corners of the tile to be channeled, such that the channel priority is higher than the ramp-digging priority. Using this, one can establish drains into the next level of a soil aquifer, as digging progress accumulates in revealed tiles.

If you fail to mine fast enough, or if flowing water pushes your miner down the channeled ramp, the dwarf will usually walk up the stairs to safety, but it is possible that the miner might ~~drown~~ have fun. In stone aquifers, a legendary miner can manage with one attempt at channeling, and at minimum, a proficient miner can manage with four, though in the second case they'll risk drowning and can take weeks to dig the next channel to expand the drain.

### Exploiting cave-ins

Conceptually this method involves removing the aquifer-bearing sand, soil or rock using channeling, and then dropping an island of dry sand, soil or clay into the resulting pond, a staircase can then be dug through the center of the resulting artificial island. This requires at least one natural dry layer, but is more flexible if two or more are available. An advantage of these methods is that they can be carried out by a single miner with no resources other than a pick.

This does not work with constructed walls since they deconstruct on cave-in.

**Note:** There is a bugBug:1206 that can occasionally prevent this method from working. Collapsed layers often turn into the layer type that was dug out at the level where they land (e.g. dry loam becomes dry sand). On occasion, a dry layer collapsed into an aquifer will also transform into actual aquifer tiles (e.g. dry loam becomes water-producing sand). It is unknown what triggers this behavior, but when it occurs it will be impossible to pierce the aquifer using cave-ins.

When unmined tiles collapse into a liquid, the displaced liquid teleports to sit *on top* of the collapsed tiles. Thus, when plugging an aquifer, it is usually advisable to incorporate aquifer drain space into the design to dispose of the displaced water.

#### Cave-in example

Side view

- Dig stairs down to the aquifer. Dig over the aquifer layer but under your "plug". You'll need a 5x5 landmass. (Slide 2)
- Channel out the area the plug will fall into. (Slide 3)
- Leave a single floor tile on top of the plug and dig out the outer layer of your plug. The plug should be a 3x3 landmass now. The single floor tile must keep the plug from falling. (Slide 3)
- Channel out the floor tile holding up the plug. (Slides 4 & 5)
- Construct floor tiles to reach the plug and dig through the middle to get under the aquifer. (Slide 6)

#### Concentric ring method for multiple layers

If you build many rings inside one another in your top drop layer, you can breach multi-level aquifers with as little as 2 natural layers of dry soil above it. Drop the rings from the outside to the inside using constructed arms to hold the center rings in place. Once a ring drops into the water below it, pump out the water in the center and dig down another layer. When that is complete, drop the next ring and continue the process until you are through. Since you start dropping rings from the outside it is necessary to know how many levels deep the aquifer is before you begin. Tutorial for more than one aquifer can be found here: User:Rhenaya/HowtoDualAquifer

#### "Chicken-Run" plug

This method was developed for a single-pick challenge on a hostile biome. In the specific (but common) case of a 2-Z thick soil aquifer, with two dry layers above, it is possible to very quickly penetrate the aquifer using a cave-in without breaching the surface and compromising the fort's security. The method starts with a Chicken Run (see above), after which an area of the upper aquifer level is cleared out with drainage into the lower level. The lower dry level is then collapsed, which means that the sub-surface level only needs to be mined (to release the plug) rather than collapsed as part of the plug.

The procedure is described in detail in this and the following posts.

While not yet demonstrated, it should be possible to use successive cycles of chicken-running and clearing to pierce arbitrarily deep soil aquifers this way.

### The pump method

The pumping method uses one or more pumps to keep an area dry long enough to smooth or wall off the sides, stopping the flow of water. It requires no special environment or resources, other than wood and dwarves (and patience). Most commonly, a modestly-sized section of the aquifer layer is channeled out and several screw pumps are built facing it. Directly behind each of the screw pumps a few tiles are channeled out to receive and dispose of the pumped water. When the pumps are activated, they should pump water faster than the aquifer can produce it, allowing masons to smooth or build walls around your future staircase. You *will* get job cancellations during this process, as stray 2/7's of water interrupt the building process. Just unsuspend the construction when this happens, as long a dwarf manages to touch the wall before canceling, it will move incrementally toward completion and eventually finish. Depending on the availability of screw pumps and dwarves, you may need to wall off one corner or side at a time, then move the pumps and repeat. When drilling through more than one aquifer layer, be sure to leave yourself enough room to build additional layers of pumps and water disposal channels on lower levels.

Things to consider:

- The smaller your work area, the less water your dwarves will have to remove and the faster construction will finish. For a single-layer soil aquifer, you only need to mine five tiles (your stairway and walls directly North, South, East, and West of it); single-layer stone aquifers require only a single tile be channeled.
- Mechanical power may come in handy, but dwarf power works just fine and is much more portable.
- Channels can sometimes be used in place of walls, causing water produced by the aquifer on one level to immediately fall and be consumed by the aquifer on the level below.
- This method may take a while.

#### Specific pump methods in detail

QuantumMenace's double-slit method can pierce an aquifer of any depth using only wood and dwarven labor. Taken from this forum post.

\`http://www.bay12forums.com/smf/index.php?topic=79224.0#msg2058307 Earlier\] in the same thread, Hans Lemurson laid out a very dwarfy method that can also pierce aquifers of any depth, using several pumps and machinery.

A convenient method without job cancellation using a pump stack was presented by kingubu in this forum post, see Pump-stack_method

Leonidas posted a detailed procedure, copiously illustrated, for tunneling through any aquifer with limited resources and relative safety.

### The freezing method

If you are playing in a freezing or very cold landscape, where it snows in winter and instantly freezes water on the map, you can dig out a 3x3 hole in the ground using channels, and make it deeper and deeper until you reach the aquifer level. Once you reach the damp rock, tunnel into it with up/down staircases, then channel out the downstairs, the exposed water will turn to ice, digging the up/downstairs before channeling allows the tiles to safely fill with 7/7 water before being frozen, this avoids the hazard of miners being encased in ice and avoids a bug(?) where frozen water which is less than 7/7 deep does not produce a floor above it. The central square of the 3x3 hole should be tunnelable ice, so you can get to the rock beneath.

If your fortress is in a zone that gets warm, build walls around the inside of the hole to stop the water coming in once the ice melts. In order to build a wall around a 1x1 staircase it will be necessary to have a 5x5 hole, since you need to leave an outer ring of ice to seal the aquifer.

If the aquifer is multiple layers deep you will need to start with a sufficiently large hole to account for both an ice wall to seal the aquifer and a constructed wall to seal the ice wall for each layer of the aquifer. A pump based method might be preferable.

As an alternative to building a second wall to seal the ice wall, you can establish a drain into the caverns, and build a constructed wall when the melt comes.

### The magma/obsidian method

If you have access to a supply of magma, you can create your own obsidian caissons. By channeling into the aquifer layer and then filling these channels with magma, or by digging staircases and pouring magma down the staircases, it is possible to create a wall of obsidian between your working area and the water-bearing rock or soil. However, changes to world generation with the last version have made this method more difficult than it once was, as it is now harder to find magma vents that extend above the aquifer level.

### The drainage method

Having made an initial hole in the aquifer, you may wish to punch another larger hole through, say for example to grow wild strawberries in the caverns. Or you may simply want an additional (natural stone!) staircase. Once you have access from below this is much easier than digging from above, and it has the additional benefit of producing a shaft of exactly the size you want.

Locate the caverns and dig a drainage shaft of up/down stairs or downward stairs up from the caverns to the aquifer (downward stairs function as grates and are far safer than channeling). Once the drainage shaft is complete punch the shaft up through the aquifer (using up/down stairs) until you hit dry dirt. Now mine out the walls around the shaft and build constructed walls to seal the aquifer. It's even faster if the walls are dug out using down stairs instead, constructed walls can be built on the stairs and water falls straight through, thus construction can always be started and is never suspended. Always build the walls from the highest layer down, so the dwarves aren't having water dumped on them from above.

This method can be used to create arbitrarily large (and shaped) holes. Large holes, which would be impractical to dig from above, are very easy using this technique. It's also extremely useful for digging straight shafts through "layercake" aquifers where aquifer tiles and non-aquifer tiles are intermixed.

Just be very aware that your framerate is bound to suffer, if you are not fast with plugging the aquifer walls.

### The modding method

By editing the raws and removing the \[AQUIFER\] tag from all of the appropriate entries in inorganic_stone_layer.txt, inorganic_stone_mineral.txt, and inorganic_stone_soil.txt it is possible to remove all aquifers from the world. This can be done before creating a new world or after, if you find a particularly neat location ruined only by the presence of an aquifer. In order to modify an existing world, you must delete the \[AQUIFER\] tag from the raws in the savegame's folder.

#### With DFHack

The DFHack command `light-aquifers-only` changes all heavy aquifers to light aquifers. If you prefer not having to deal with aquifers at all, the DFHack command `aquifer drain --all` removes the aquifer flag from all tiles in your current embark without requiring raw edits.

##### With DFHack's gui/aquifer command

DFHack's "gui/aquifer" command lets you interactively remove (or create) aquifers on specific tiles. This is useful if you want to keep a heavy aquifer on your map, but don't want to deal with the hassle of breaching it.

To create an aquiferless shaft, do this:

1.  Open gui/launcher by clicking on the DFHack logo and selecting gui/launcher
2.  Run gui/aquifer
3.  Draw a cube (*e.g. a 4x4*) containing the area to drain

Don't worry about hitting non-aquifer tiles: they shouldn't be affected by the tool at all.

#### Command-line (Linux)

Note that this prevents light aquifers as well as heavy ones!

    cd df_linux/data/vanilla/vanilla_materials/
    sed -i 's/\[AQUIFER\]/(AQUIFER)/g' inorganic_stone_*.txt

and generate your world. If you want to restore the tags later, you can do it with the command:

    sed -i 's/(AQUIFER)/[AQUIFER]/g' inorganic_stone_*.txt

#### Text editor (all operating systems)

You can manually perform the command-line method above.

There are three files, all found within `“THE FOLDER `*`Dwarf Fortress`*` IS INSTALLED IN”\data\vanilla\vanilla_materials\objects`:

- inorganic_stone_layer.txt
- inorganic_stone_mineral.txt
- inorganic_stone_soil.txt

Open these in a text editor, then use the “Find and Replace” function and replace all instances of `[AQUIFER]` with `(AQUIFER)`. Later on, if you would like to reverse the process, replace `(AQUIFER)` with `[AQUIFER]`.

## Benefits of aquifers

Aquifers can be useful for building a self-sufficient fortress, and are often indispensable for water-related megaprojects in maps without a river.

Aquifers outside ocean biomes also contain fresh water. Since aquifers are almost always located close to the surface, freshwater aquifers can easily be turned into a source of infinite, secure, non-freezing drinking water for your dwarves. While both of these roles can also be filled by cavern features, an aquifer allows you to get the same advantages without exposing yourself to potentially ~~dangerous~~ Fun cavern creatures.

### A benefit of heavy aquifers?

Although annoying, heavy aquifers can absorb an infinite amount of water, meaning they can function as a drain for anything above them. For instance, digging a pit in a lower Z-level of the aquifer, then connecting it to a breached aquifer a level above, through a channel dug a level above that, will create a permanently flowing, compact, secure water/power source completely contained within the fortress.

## Technical implementation of the aquifer type split

An aquifer will be heavy if the Drainage modulo 20 equals 7, all other aquifers are light.

## Bugs

- Aquifers south/west of the NW-SE diagonal in the local embark map are not displayed on the embark screen (but they're still present). Bug:11358

## External links

- QuantumMenace's two-slit method for breaching aquifers of any depth - Illustrated guide
- Hatch trick described with ascii art.

"This is what the in-game prompts were warning us about!"\
*Photographed by Michael Behrens*
