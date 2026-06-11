# Wheelbarrow

> Fonte: [Wheelbarrow](https://dwarffortresswiki.org/index.php/Wheelbarrow) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **wheelbarrow** is a tool used to increase the speed of hauling heavy items. Wheelbarrows can be made of metal or wood at a metalsmith's forge or carpenter's workshop, and can carry a single item (or a single stack of items, e.g. prepared meals). The capacity of a wheelbarrow is equivalent to one fifth of a minecart's capacity.

## Construction

Wheelbarrows are constructed of either wood or metal:

|  |  |  |
|----|----|----|
| Material | Worker | Workshop |
| Wood (1 log) | Carpenter | Carpenter's workshop |
| Metal (2 bars) | Blacksmithing | Metalsmith's forge or Magma forge |

- Although classified as "Furniture" for stockpiles, metal wheelbarrows (only) are manufactured under the "other objects" category.

## Utility

Dwarven wheelbarrows are sturdy and practical.

Stone stockpiles have 1 wheelbarrow automatically assigned upon designation, though any stockpile can have wheelbarrows assigned in the stockpile settings menu in the "Storage and tools" submenu (). Wheelbarrows will be stored in their assigned stockpile when not in use; when used to haul an item to that stockpile, the item and the wheelbarrow will both be dropped onto the same tile. A stockpile's wheelbarrows are only used to carry items *to* that stockpile; they will not be used to carry items away *from* it, nor carry other assigned wheelbarrows back to that stockpile (unless it is a "wheelbarrow" stockpile). Wheelbarrows assigned to a stockpile do have the stockpile number appended, eg. "feather wood wheelbarrow \".

Dwarves carrying items in wheelbarrows will ignore both the weight of the wheelbarrow's contents and the weight of the wheelbarrow itself, moving always at their top speed. This makes them particularly useful for hauling heavy items like stone, which slow haulers a lot.

Dwarves will haul any items weighing exactly 75Γ or more\* via wheelbarrow if their destination stockpile has wheelbarrows enabled and available. All stone boulders (with the exception of raw adamantine) weigh significantly more than 75Γ - these, and most large stone furniture, are the most common heavy items most players will find themselves needing to haul during normal gameplay\*. Any items weighing less than 75Γ will not be hauled via wheelbarrow, even if there are empty wheelbarrows available. Once again, the weight of wheelbarrows is ignored for this condition, meaning that a dwarf will not haul a 50Γ object with a 50Γ wheelbarrow, despite if the combined weight would be greater than the 75Γ threshold.

*(\* As examples, items that are too light to trigger wheelbarrows include all logs, (wooden) barrels of booze (but* not *all barrels of food items!), most individual stone blocks and metal bars (not platinum, gold or gold alloys), among others. Many categories, especially furniture, depend on the exact item size and material density.)*

Wheelbarrows carry less stuff than minecarts, but do not require a track to be preconstructed, and can go up and down stairs.

Initially bringing a wheelbarrow to its assigned stockpile uses furniture hauling and the wheelbarrow will be carried to the stockpile (not pushed), so here the weight\* of the wheelbarrow actually matters.

*(\* Wheelbarrows have a size of 30,000, making them 50% larger than a barrel, and twice the size of a bin. Any item's weight is {size x density of material} / 1,000,000 - but without worrying about the actual math, it's enough to understand that it's directly proportional to the density of the material. This means that denser material is 50% more noticeable vs. barrels, and twice as noticeable vs. bins, etc. So, choosing a* slightly *lighter wood will not be very noticeable when carrying a wheelbarrow, but choosing nickel (density 8,800) vs. any common wood (density ~390-990) will make a* much *bigger difference. Remember this only matters when hauling a wheelbarrow to an assigned stockpile, not when pushing the wheelbarrow with a heavy item in it (when all weight is ignored).)*

## Forging and Melting

- Metal wheelbarrows cost **two** metal bars or **six** adamantine wafers to forge.
- When a metal wheelbarrow is melted down, it will return **1.8** metal bars for an efficiency of **90%**, or **1.8** wafers for an efficiency of **30%**.

## Bugs

- If all of a stockpile's tiles are occupied by wheelbarrows, it will stop requesting new items even though the tiles under the wheelbarrows have no stockpiled item. Consequently, stockpiles need to have more tiles than wheelbarrows to work correctly.Bug:8861

- Items can occasionally be left inside a wheelbarrow, causing the wheelbarrow to become unusable. This can cause a stockpile to stop collecting stone if all of its wheelbarrows end up in this stateBug:6074 You can work around this by marking the contents of the wheelbarrow for dumping (allthough for artifacts, which cannot be dumped, you will at least temporarily need to use df with dfhack enabled, as such stuck artifacts are automatically moved from such wheelbarrows on load, or otherwise the artifact will forever be stuck in the wheelbarrow). Also the most likely (and possible only) cause for an item getting stuck in a wheelbarrow is, when the jobs gets interrupted, cancelled (or aborted), while an item is currently in the wheelbarrow, ie. due to the stockpile, the wheelbarrow is hauling the item to, has become inaccessible or the stockpile was deleted (while the wheelbarrow already has an item loaded).

- Dwarves carry wheelbarrows instead of pushing them when the wheelbarrows themselves are being hauled.Bug:6008

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
When they push an empty wheelbarrow, any dwarf walking by will jump in and demand a ride. To avoid this, the decision was made long ago that empty wheelbarrows must be carried to avoid elvish-type laziness.

\

    [ITEM_TOOL:ITEM_TOOL_WHEELBARROW]
    [NAME:wheelbarrow:wheelbarrows]
    [VALUE:50]
    [METAL_MAT]
    [WOOD_MAT]
    [TOOL_USE:HEAVY_OBJECT_HAULING]
    [FURNITURE]
    [TILE:153]
    [SIZE:30000]
    [MATERIAL_SIZE:6]
    [CONTAINER_CAPACITY:100000]
