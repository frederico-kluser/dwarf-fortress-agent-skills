# Storage

> Fonte: [Storage](https://dwarffortresswiki.org/index.php/Storage) — Dwarf Fortress Wiki (GFDL/MIT)

Types of items used for **storage** include containers, cabinets, barrels, large pots, bags, bins, and bookcases. All storage objects are used to hold items, from personal possessions to gems, alcohol, seeds, quarry bush leaves, and even living creatures, but their use is context-sensitive, so you cannot for example use your barrels for storing coins.

Chests, coffers, and boxes are subsumed under *boxes* in the status stocks screen, and these can be built as "containers" from the uilding menu, urniture submenu to satisfy the "Needs: X Chests" requirement for nobles. Each other storage object type has its own entry.

To examine a storage object's contents, select the object location with the mouse. If the storage object isn't selected (say, if there are multiple items or units on the same tile) it should be selectable as a tab on the upper right of the window.

## Barrels, bins, bags, pots

Barrels are wooden or metal containers that are useful for storing items in a food stockpile and are used to store alcohol, plants, seed bags, meat, fish, dwarven syrup, quarry bush leaf bags, flour bags and dye bags, cooked food, fat and tallow, and all prepared organs. They are made at a Carpenter's workshop with 1 log or at a Forge with 3 bars of metal. Barrels can be disabled in a stockpile to prevent haulers from running off with everything else inside to pick up a stray seed.

Pots, an alternative for barrels, can be made of wood, stone, clay, glass, or metal. Pots can also be used to store alcohol and other related liquids, though clay pots (earthenware) must be glazed to hold liquids. Pots hold the same amount as barrels (60 total units of food, or 30 units of alcohol) and weigh 1/4th as much as a barrel of equivalent material. Except for a few barrel-specific requirements, pots are generally a superior replacement.

Bins are containers, again made from wood or metal, used for most non-food items. They are sent to all the other stockpiles (with the exclusion of the refuse, stone and graveyard piles) and will hold much larger stacks of items, making organizing those endless piles of +giant cave spider silk socks+ and trade goods much easier to manage. They are made at a Carpenter's workshop with 1 log or at a Forge with 3 bars of metal. Bars and blocks will stack into a bin, but not into any other container, so a stockpile with bar/block enabled will default to requesting bins.

Bags are used to store seeds, quarry bush leaves, mill products (flour, sugar, dye), gypsum plaster, quicklime and sand ("powders"). They are made from plant fiber (or silk) cloth, leather, or adamantine. Bags are used to gather and transport powders the same way buckets are used to carry water. Bags can be placed inside other containers, such as barrels. They are made at a Clothier's shop with 1 cloth or at a Leather works with 1 leather.

Empty barrels, pots, bins and bags can all be stored in a furniture stockpile.

## Cabinets and "chests"

These two containers are both furniture items only. A stone chest is called a **coffer**, and a glass chest is called a **box**, but they are used for the same purpose.

They must be built in rooms assigned to dwarves in order to fulfill the dwarves' room requirements. Cabinets are used to store clothing, and chests are used to store everything else. Also, locations like taverns, temples, libraries, and hospitals need containers for their supply storage.

Once built as furniture, their contents can be viewed by clicking on them with the mouse.

## Quick reference

\|}

¹ - Large Pots can be made from any hard material, including wood and metal

² - Used to carry water, can store Milk and Lye but will be emptied into Barrels

³ - Backpacks and quivers can only be made from Adamantine cloth, though ones made from other cloth can be purchased from caravans

⁴ - Rock and Wood versions of these items are made in Craftsdwarf's workshop rather than Carpenter's workshop or Mason's workshop as usual.

⁵ - A minecart can be placed where you need it and used for storage, but technically it's not built furniture

- Tools have capacity set in units 10 times smaller; liquids take container capacity 60 per 1 unit, i.e. capacity 180 = 3 units of water, 50000 = 833 units, etc.
- Large Pots are equivalent to Barrels except for a few specific uses (e.g. process plant to barrel).
- Bins are like Barrels but store different stuff.
- Buckets are used for temporary storage of Milk, Lye, and Water.
- Jugs are mini containers for honey and royal jelly and can be stored inside Bins, in this sense they are like Bags.
- Bags are mini containers for powders and can be stored inside Barrels/Large Pots if holding food items.
- Flasks/Waterskins/Vials are different names for the same containers depending on the material it's made from.
- Chests/Coffers/Boxes are different names for the same piece of furniture depending on the material it's made from.
- A terrarium can be designated as an Aquarium. A dwarf will use a bucket to fill it with water. If deconstructed it'll stay filled with Water\[10\] and can even be sold with the water inside. The water costs 1☼ each, so you get 10☼ for the water.
- A hive won't be destroyed if you don't have a stockpile for its products. You could use on the hive and dump the item to use it.

## Spilling

A container item that moves fast and collides with an obstacle spills its contents. If the obstacle permits (i.e. fortification), these continue to move in the same direction with some scattering, otherwise displaced 1 tile above and retain velocity. This was introduced for minecarts, but applies at least to other tools and cages. If the tile above also contains an obstacle and the spilled item is a container, the process repeats on the next tick, until it runs out of either nested containers or wall height (see the first link above).

## Bugs

- Hauling jobs block access to all the items in the destination containers until the hauling is complete. This often results in cancellation spam and work delays. One workaround is creating a "feeder stockpile" with containers disabled.
- Container size works in mysterious ways. Items only have "SIZE" determining the volume of their material and thus weight, but *no separate external volume*. For containers, CAPACITY is *not* added to it, i.e. they all are treated like soft bags: you can put 30 other bags inside a bag, and you can load a minecart with minecarts. At the same time, containers are assumed to *not* be soft bags - while weight of contents adds to the container's, the ambiguous SIZE is constant. Together, these facts make containers nest-able *indefinitely*, as long as CAPACITY\>SIZE (which normally is the case) and potentially act like bags of holding - have the same stated volume whether empty or holding an arbitrary total amount of items via nested containers. The only nesting that normally happens in Fortress mode is minecart \> barrel \> bag, but this still makes a minor exploit.
- Stacks made by a single job tend to ignore capacity. For one, dwarves picking up items may stuff a quantum stockpile worth of items into one container. The same applies to brewing and extracting.
- Conversely, a freshly produced stack, no matter how small, will be put into a new container and not added into the old ones. Which may be justified with *brewing*, but also happens to production of items/substances without quality modifiers.
