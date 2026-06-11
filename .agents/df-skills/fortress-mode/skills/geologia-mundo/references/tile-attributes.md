# Tile attributes

> Fonte: [Tile attributes](https://dwarffortresswiki.org/index.php/Tile_attributes) — Dwarf Fortress Wiki (GFDL/MIT)

Every tile in *Dwarf Fortress* is described as or , or , and or . Unlike in versions prior to v50, these attributes can no longer be observed from the menu, when the cursor is located over any single tile.

These attributes do *not* change what tiles look like. DFHack's Rendermax plugin implements a lighting system into the game, but this is only an aesthetic change, and does not affect tile attributes.

There are eight different combinations, and only four of them occur naturally:

- \- Outdoors, or within outdoor-like conditions (such as being indoors, but with no roof above the tile, providing direct access to sunlight.)

- \- Impossible

- \- Impossible

- \- Impossible

- \- Constructed buildings on the surface, below-ground-level chambers with constructed floors or buildings only (possibly walls also) above them. Also tiles beneath branches of some trees.

- \- Impossible

- \- Possible in arena, does not occur in Adventure mode. It can occur in Fortress mode, e.g: after unretiring on stockpile tiles (biome becoming embark tile level biome).

- \- Underground tunnels, including most of your fortress

Being in the dark increases cave adaptation, and being outside causes it to decrease (along with stunning/nausea if the sun is out).

The entire fortress site starts out as . After that, a ray for and a ray for falls straight down from the highest z-level for every (x,y) position on the local map, changing each tile's modifiers until something that blocks that particular "ray" is encountered. Due to this behavior, any of the previous three tile combinations will never be encountered in the same (x,y) position on a lower z-level than a higher-numbered combination.

## Outside vs. Inside

This attribute is determined by whether there is a roof of some kind over a tile. Weather only affects tiles which are *Outside*. Almost any kind of geometry will block the *Outside* ray including natural and constructed walls, floors, stairs, and fortifications, and bridges, floor grates, floor bars, and hatches. A tile which is *Outside* will always be *Light Above Ground*, but an *Inside* tile may be either *Light Above Ground* or *Dark Subterranean*.

Tiles under a lever-opened bridge, hatch, grate or floor bars will keep counting as inside until any tile in that 1×1 column is built, constructed or dug on to force an update; remaining so after closing until another update.

## Light vs. Dark and Above Ground vs. Subterranean

These two attributes are determined in exactly the same way. Once an area is exposed to the outside world, it is *Above Ground* and *Light* (and thus channelling this tile will make the tile below it also *Above Ground* and *Light*). Even after being covered up again, it will remain this way. This allows growing outdoor crops inside safely.
