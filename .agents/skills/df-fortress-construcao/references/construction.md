# Construction

> Fonte: [Construction](https://dwarffortresswiki.org/index.php/Construction) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*"Construct" redirects here; for unnatural creatures, see Construct creature.*

A dwarf constructing a still.

**Constructions** are buildings such as floors, walls, and stairs. They can be made of boulders, logs, blocks, and bars of any solid material—including wood, stone, metal, glass, clay, and are accessible in the build menu by bn.

Unlike most objects accessed from the b build menu, constructions are treated as inert terrain features when completed, with a few limitations as described below. Some constructions can only be interacted with by looking at them or by pressing mx to designate their removal. Clicking on such will give no information after the construction is completed, but will allow removal, suspension, and an idea of the current status before the construction is complete.

## Required labors

In order to make a construction, a dwarf must have the "Wall/Floor Construction" labor enabled, found under the "Other Jobs" heading.

The mining labor is required for removing constructions, regardless of the material the construction is made from.

## Constructions and mines

Constructions are similar to mined out formations. However, unlike the walls and floors surrounding mined or channeled spaces, constructed features cannot be smoothed, or carved into minecart tracks unless blocks are used, though they can be engraved. In order to construct smooth stone walls and floors, blocks need to be used in place of raw stone; smooth constructions can be engraved as normal. Wood, metal, and glass constructions are not considered either rough or smooth, but in the case of wood, building with blocks will increase room value - metal bars have the same value as metal blocks and are thus interchangeable (though blocks may be preferred to simplify resource tracking), and glass can *only* be used in block form.

## Order of construction

Constructions, when equidistant to dwarf\[Verify\], are built in a Last-In-First-Out (LIFO) order. That means that whichever constructions are ordered first will be built last. Also, if there is a large group of constructions being built, and a new set of constructions is ordered, the constructions in progress will be ignored until the new constructions are finished.

If you place a single multi-tile order, as in the case of a long bridge or wide walkway over a gap or river, then that will be treated as a "single order". It will be built logically, from connected locations out, but it, as a single "order", will be addressed in sequence according to the rules of LIFO. Note that "logic" does *not* include building corners of a wall first, and so can result in un-reachable tiles. Use LIFO to avoid this - designate the main line of wall first (perhaps leaving a 1-tile additional space), *then* designate the corners; using LIFO, the corners will then be built before the main line, and you can fill in the last gaps after the hard-to-reach spots are finished.

The exception to this is if you click on the placed construction, and then click "Top Priority". This moves this construction to the front of the list - along with *all other* "Top Priority" constructions. These Top Priority constructions will then be treated as a priority list and finished in Last-In, First-Out order, followed by non-priority constructions in *their* LIFO order.

Respecting the LIFO order is also necessary to efficiently and correctly construct multi-z-level walls "Tower (project)").

## Destruction

Constructions which have not yet been completed are technically Buildings, which permits them to be toppled by building destroyers. Once they are completed, they become map tiles, which are effectively indestructible. Constructions are generally inert, resisting building destroyers, but will be destroyed if magma and water can interact in the square of the construction to form obsidian, or in a cave-in. Building and removing a construction can change the floor it is built upon to a default value, removing things like engravings and the "magma flow" floor above semi-molten rock.

## Impact on framerate

Constructions introduce slowdowns from two angles:

1.  It has to keep track of the original item (though there is a DFHack plugin which will delete the item and flag the construction as "recreate the item from scratch when you deconstruct it"), which means that general item lookups take slightly longer (it's done via binary search, so you'd only notice significant slowdowns each time the item count in your fortress doubles).
2.  It has to keep track of what the construction is made of, using a separate structure that needs to be looked up for each constructed tile that is visible on the screen. These also use binary searches, though with three values (X+Y+Z coordinates) instead of just one so they're a little bit slower. Typically, you only get noticeable slowdowns when you're building something on the scale of FlareChannel.
