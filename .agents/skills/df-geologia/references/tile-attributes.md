# Tile attributes

> Fonte: [Tile attributes](https://dwarffortresswiki.org/index.php/Tile_attributes) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

Underground and above ground. Simple as that.

Every tile in *Dwarf Fortress* is described as Outside or Inside, Light or Dark, and Above Ground or Subterranean. In this version, these attributes *cannot* be viewed directly, but they can still be inferred via other means.

These attributes do *not* change what tiles look like. DFHack's Rendermax plugin implements a lighting system into the game, but this is only an aesthetic change, and does not affect tile attributes.

There are eight different combinations, and only four of them occur naturally:

- Outside Light Above Ground - Outdoors, or within outdoor-like conditions (such as being indoors but with no roof above the tile, providing direct access to sunlight.)
- Outside Light Subterranean - Impossible
- Outside Dark Above Ground - Impossible
- Outside Dark Subterranean - Impossible
- Inside Light Above Ground - Constructed buildings on the surface, below-ground-level chambers with constructed floors or buildings only (possibly walls also\[Verify\]) above them. Also tiles beneath branches of some trees.
- Inside Light Subterranean - Impossible
- Inside Dark Above Ground - Possible in arena, does not occur in Adventure mode, but can occur in Fortress mode, e.g: after unretiring on stockpile tiles (biome becoming embark tile level biome).
- Inside Dark Subterranean - Underground tunnels, including most of your fortress

Being in the Dark increases cave adaptation, and being Outside causes it to be triggered.

The entire fortress site starts out as Inside Dark Subterranean. After that, a ray for Outside and a ray for Light Above Ground falls straight down from the highest z-level for every (X,Y) position on the local map, changing each tile's modifiers until something that blocks that particular "ray" is encountered. Due to this behavior, any of the previous three tile combinations will never be encountered in the same (X,Y) position on a lower z-level than a higher-numbered combination.

## Outside vs. Inside

This attribute is determined by whether there is a roof of some kind over a tile. Weather only affects tiles which are *Outside*. Almost any kind of geometry will block the *Outside* ray including natural and constructed walls, floors, stairs, and fortifications, and bridges, floor grates, floor bars, and hatches. A tile which is *Outside* will always be *Light Above Ground*, but an *Inside* tile may be either *Light Above Ground* or *Dark Subterranean*.

Tiles under a lever-opened bridge, hatch, grate or floor bars will keep counting as inside until any tile in that 1×1 column is built, constructed or dug on to force an update; remaining so after closing until another update.

## Light vs. Dark and Above Ground vs. Subterranean

These two attributes are determined in exactly the same way. Once an area is exposed to the outside world, it is *Above Ground* and *Light* (and thus channelling this tile will make the tile below it also *Above Ground* and *Light*). Even after being covered up again, it will remain this way. This allows growing outdoor crops inside safely.
