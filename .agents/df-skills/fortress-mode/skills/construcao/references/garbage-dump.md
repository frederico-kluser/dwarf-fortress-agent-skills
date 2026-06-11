# Garbage dump

> Fonte: [Garbage dump](https://dwarffortresswiki.org/index.php/Garbage_dump) — Dwarf Fortress Wiki (GFDL/MIT)

**Garbage dumps** are activity zones in or from which dwarves will throw items marked for dumping.

Garbage dumps are *not* the same as refuse stockpiles.

- Refuse stockpiles can be designated to accept specific type(s) of refuse, such as animal corpses or bones, and then are automatically filled by haulers whenever the items appear on the map.
- Garbage dumps don't have categories. Dwarves will dump any items marked to be dumped, including objects of value!

Garbage dump zones are useful for many things beyond garbage disposal; they can create quantum stockpiles, transport materials to a job site, send items to the trade depot when no caravan is present, drop rocks on enemies below, and numerous other uses.

### Create garbage dump

To place a garbage dump, select zone (), then Garbage Dump, paint your desired shape, either on a flat area or next to a cliff or hole, and click Accept. After accepting the placement, the zone can renamed, repainted, suspended, or deleted.

If the dump zone is designated next to a cliff or hole, the items will be dropped off the edge; otherwise they will be dropped on a tile in the zone. Although each ground tile within that zone is considered a garbage dump tile, dwarves can drop multiple items on a single tile, usually the closest tile when they path to the zone.

Most items dropped in magma will be destroyed, and items dropped in a river may get washed downstream; in either case the items will be very hard to recover (*ergo, best not to do either of those in the first place*).

### Marking items to dump

To mark an individual item for dumping when it is:

- On the **ground**: Click the tile the item is on, then if there is more than one item there, click the tab of the item on the right edge of the sheet window, and click the dump button.
- In a **workshop**: Click one of the tiles the workshop, find the item in the list of items in that workshop (which may not be viewable if the UI is scaled to large), and click the dump button.
- **Held** by a dwarf: View the dwarf's sheet, select the Items tab, find the item in the list, click the button to view the item's sheet, and click the dump button.
- Inside a **container**: Display the container's item sheet, find the item in the list of items in that container, and click the dump button.
- In the **stocks** menu: Type or click the Stocks button, then either:
  - click the filter input at the top and enter text to match the item, and when you see the item, click the dump button.
  - select the item category, scroll to the item, and click the dump button.

To mark multiple items for dumping:

- As above in the Stocks menu, but click the dump button for a group of items.
- Use bulk designation -

**NOTE:** Bulk dumping designates *all* items on the tiles for dumping, even built furniture, the construction materials making up buildings, items inside containers, etc. In the case of built furniture and building components, this will have no immediate effect; however, upon deconstruction the item will immediately be dropped on a nearby square by the dwarf hauling the item to await disposal in the nearest dump.

### Moving items to dump

Garbage dumps only accept items that have been marked for dumping, require dwarves to have refuse hauling labor enabled, and are subject to refuse Standing orders.

Dwarves usually throw dumped items in the nearest available garbage dump, although this is not an ironclad rule. If a nearer zone becomes available after they have already started the job they will ignore it. They also have a preference for open space dumps. If a garbage dump is located next to open space, dwarves will always stand on a garbage dump square when dropping *into* that open space, even if it could potentially be done more efficiently. If a garbage dump is located next to multiple tiles of open space, they seem to prefer the one farthest to the northwest. If a tile to the north and a tile to the west are the only tiles available, they will throw to the west. Such garbage dumps can be a very efficient method of moving materials to the lower levels of your fortress. However care must be taken to prevent dwarves and livestock from being struck by falling objects, perhaps with traffic designations and pastures.

Dwarves will *not* dump items that are in a tile marked "Above Ground" unless you allow them to in Standing orders.

Items dumped into magma that are not magma safe will permanently disappear, which is useful for disposing of clutter and increasing FPS. Otherwise a single tile (either a dump zone, or the ground below the open space) will hold any number of dumped objects. Dumping items into magma can be dangerous due to the magma mist generated when objects fall into magma. It is advised to dump items into magma from a hole several z-levels up to avoid !!Dwarves!! running around the fortress.

**NOTE:** If you designate items for dumping, but forget to mark an active garbage dump, your dwarves will ignore the item until an active garbage dump is marked.

### Reclaim dumped items

Dumped items are automatically marked as forbidden, preventing dwarves from touching them. Therefore, these items can't be used, or even selected in workshop jobs, etc.

If for some reason Urist is yet again incapable of locating their favorite pair of cave troll leather socks, they should think to look among the black hole of matter that is the nearest garbage dump, as the socks could be snugly lodged between a few billion rocks.

You can reclaim Dumped/forbidden items in the same ways as in \#Marking items to dump section above, except clicking the forbid button.

### Dwarves won't dump no matter what I do

Dumping items requires the 'refuse hauling' labor. Items located in an "outside" tile will not be moved unless 'gather refuse from outside' is enabled in your Standing orders. Probably due to a bug, dwarves occasionally ignore items that are meant to be dumped; toggling forbid and dump status on, then off again seems to correct this problem.

### Strategy

Garbage dumps are great space savers because they can hold an infinite number of items on one tile; with some micromanagement they can even compress large, one-item-per-tile stockpiles into single-tile quantum stockpiles (although this requires additional work and is usually considered an exploit). The most common use for garbage dumps is for cleaning away loose stones left in your fortress by your miners: mark them for dumping, wait for the jobs to be completed, and then reclaim them (-) for use by your stonemasons; bonus points if you do this next to a stoneworking workshop and then re-designate the tile as a stone stockpile. If the dump is designated inside a workshop, the workshop will not become cluttered. However, if you put a garbage dump inside a magma workshop with the intent of dumping ores there, make sure the zone does not overlap any open pits of magma you may have carelessly left around, or as per intended behavior, items will be dumped into the magma.

## See also

- Garbage disposal
