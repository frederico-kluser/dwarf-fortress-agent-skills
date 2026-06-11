# Wheelbarrow

> Fonte: [Wheelbarrow](https://dwarffortresswiki.org/index.php/Wheelbarrow) — Dwarf Fortress Wiki (GFDL/MIT)

A **wheelbarrow** is a tool used to increase the speed of hauling. Wheelbarrows can be made of metal or wood at a metalsmith's forge or carpenter's workshop, and can carry the equivalent of a single stockpile tile, be it a single stone, a bin or barrel (with its contents included), or a stray item. This is equivalent to one fifth of a minecart's capacity.

Wheelbarrows have a size of 3000 and a capacity of 100,000, meaning that you can fit 33 wheelbarrows in a wheelbarrow.

## Construction

Wheelbarrows are constructed of either wood or metal:

| Material | Worker | Workshop |
|----|----|----|
| Wood (1 log) | Carpenter | Carpenter's workshop |
| Metal (2 bars) | Metal crafter | Metalsmith's forge or Magma forge |

## Utility

Each stockpile may have up to 3 wheelbarrows assigned for hauling items to that stockpile. (DFHack allows assigning more than three wheelbarrows per stockpile with `tweak max-wheelbarrow`.) Stone stockpiles have 1 wheelbarrow automatically assigned upon designation, though any stockpile can have wheelbarrows assigned in the Set Building Tasks/Prefs () menu with the hotkey. Wheelbarrows will be stored in their assigned stockpile when not in use, potentially sharing a tile with a stockpiled item. A stockpile's wheelbarrows are only used to carry items *to* that stockpile; they will not be used to carry items away *from* it.

Dwarves carrying items in wheelbarrows ignore the weight of the contents, moving always at their top speed. This makes them particularly useful for hauling heavy items like stone, which slow haulers a lot. There's little benefit to carrying light items in a wheelbarrow, as dwarves won't load multiple items in it. They will, however, load a single bin *full of items* in a wheelbarrow.

Wheelbarrows carry less stuff than minecarts, but do not require a track to be preconstructed, and can go up and down stairs.

If wheelbarrows are assigned to a stockpile, dwarves will use them exclusively and cease hauling items to it with their bare hands, meaning that the number of assigned wheelbarrows is also the maximum number of active hauling jobs for said stockpile. This behaviour can save haulers for other more urgent jobs, but is sometimes inconvenient. Increasing the number of assigned wheelbarrows and adding linked stone stockpiles can allow you to pour more dwarfpower into hauling. If you set wheelbarrows at your stockpile to 0, all haulers may carry stones there, but will do it by hand, which is painfully slow work when long distances are involved.

## Forging and Melting

- Metal wheelbarrows cost **two** metal bars or **six** adamantine wafers to forge.
- When a metal wheelbarrow is melted down, it will return **1.8** metal bars for an efficiency of **90%**, or **1.8** wafers for an efficiency of **30%**.

## Bugs

- If a stockpile is assigned both a wheelbarrow and container, dwarves will only use the wheelbarrow to move the container to the stockpile, carrying the items to be stored in the container by hand. As a workaround, a "feeder" stockpile with wheelbarrows enabled can be designated to "give to" an adjacent "storage" stockpile with containers enabled.

- If all of a stockpile's tiles are occupied by wheelbarrows, it will stop requesting new items even though the tiles under the wheelbarrows have no stockpiled item. Consequently, stockpiles need to have more tiles than wheelbarrows to work correctly.

- Items can occasionally be left inside a wheelbarrow, causing the wheelbarrow to become unusable. This can cause a stockpile to stop collecting items if all of its wheelbarrows end up in this state You can work around this by marking the contents of the wheelbarrow for dumping.

- Dwarves carry wheelbarrows instead of pushing them when the wheelbarrows themselves are being hauled.

When they push an empty wheelbarrow, any dwarf walking by will jump in and demand a ride. To avoid this, the decision was made long ago that empty wheelbarrows must be carried to avoid elvish-type laziness.
