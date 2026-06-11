# Quantum stockpile

> Fonte: [Quantum stockpile](https://dwarffortresswiki.org/index.php/Quantum_stockpile) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **quantum stockpile** (**QSP**) allows you to store an unlimited number of items in a single tile, which can make for more compact fortresses and efficient storage, hauling, and manufacturing flows. Quantum stockpiles are a developer tolerated[1] exploit.

## Simple quantum stockpiles

The simplest QSP is created by designating a garbage dump activity zone, dumping the items you want to store and then reclaiming them when you are ready to use them. If you place this garbage dump on top of an existing stockpile, the dumped items will automatically be considered part of the stockpile, allowing the use of stockpile links to distribute the items to workshops or other stockpiles.

A similar effect may be achieved for stones by building a wall two tiles in front of a catapult and digging a channel between the wall and catapult. By firing the catapult at the wall, the stone falls into the trench. The stone will pile up in the channel, putting it out of sight and out of mind. Not only does this train siege operators, but it clears the stone that your miners leave everywhere.

Another way to quantum stockpile is to not have appropriate stockpiles to move items back to after you move them to the trading depot. The depot can hold an infinite number of items, and those items will not be removed if there is nowhere else to place them. This is also useful for anything you want to trade anyway.

Despite using a minecart, the Hauling labor required is determined by the Stockpile settings.

## The Minecart Stop

This method allows the type of items to be stored in the quantum stockpile to be completely controlled and to be as broad or specific as required. Collection of items is automatic with no user input required, just like a normal stockpile, and the number of haulers collecting for the stockpile is controlled by the size and number of feeder stockpiles. Distribution is also automatic, with dwarves coming to collect items as needed from the quantum stockpile, just like from a normal stockpile.

This can be utilized as part of a minecart transport system, or standalone with no tracks or moving minecarts whatsoever. The steps below are to create a standalone quantum stockpile, but the same general principles apply if used in a minecart transport system.

### Setup

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   |   | f | f | f | f |   |   |   |   |   | f |   | f | e | e | d | e | r |   | s | t | o | c | k | p | i | l | e |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   |   | S |   |   |   |   |   |   |   | S |   | t | r | a | c | k |   | s | t | o | p | , |   | s | e | t |   | t | o |   | d | u | m | p |   | s | o | u | t | h |
|   |   |   | q |   |   |   |   |   |   |   | q |   | q | u | a | n | t | u | m |   | s | t | o | c | k | p | i | l | e |   |   |   |   |   |   |   |   |   |   |   |   |

1.  First, **pause the game**. If you don't, the dwarves will try to use the quantum stockpile for their own purposes while you're setting things up, like assigning barrels or bins or dropping an unintended item, and then the QSP won't work. You should also have a minecart ready in your inventory.
2.  Build a track stop b - n - K , being sure to set the dumping direction d. You may leave the friction as-is. This can be adjusted later should the need arise; see here for more information.
3.  Designate a 1x1 quantum stockpile p on the tile where the track stop will dump, then define preferences q to make the settings s store only what you want. Be sure to select zero barrels E, bins C, and wheelbarrows w. At this stage your dwarves may store a single item in this stockpile; this does not affect functionality.
4.  Designate a feeder stockpile p near the the track stop.note 1 It can be any size, but the larger it is, the more dwarves will simultaneously collect items.note 2 Define the preferences q of this stockpile to be the same as the quantum stockpilenote 3, including zero barrels and bins, and with the possible exception of the number of wheelbarrows. If the QSP is for heavy items (e.g. loose stones), you may want to use wheelbarrows in the feeder stockpile to speed up collection.
    1.  Even though the feeder stockpile can be anywhere in or out of the fort, it will be most efficient if it's positioned close to the track stop.
    2.  Keep it a reasonable size. In case something goes wrong, you won't want to have to deal with 200 unwanted boulders.
    3.  If you configure the feeder stockpile to accept more than one type of item within a category, such as Stone or Furniture, several quantum stockpiles can be set up to draw from the one stockpile. As an example, Metal Ores can be sorted out to iron-, copper- and silver-bearing ores in separate QSPs.
5.  Construct a new hauling route pressing h then r, being sure to place the cursor over the target track stop. Naming n the route now will save a hassle with troubleshooting later. Press v to assign a vehicle (told you that you'd need one), then press s to define a new route stop on top of your track stop. Press Enter to define the stop. Press x to remove the default conditions, press s to create a stockpile link, then position the cursor over the feeder stockpile and press p. Press Enter again to configure the route stop settings to match the quantum stockpile settings. **If using custom stockpile settings, make sure you don't turn off the additional options. If you do turn them off, things won't work.** Press ESC several times to back out of the Routes menu back to the Main menu.

It's a little fiddly to initially set up, and if you miss any step it won't work at all, but once in operation it's an extremely efficient storage system, and scales easily with the size of your fortress, number of haulers and number of items to store.

### Drawbacks

1.  This method cannot store any items in bins or barrels at all, including bolts.
2.  This method cannot store any type of drink (you will see your dwarves leave barrels and pots of alcohol all over the place), due to the fact that barrels assigned to stockpiles are marked to be put in specific stockpiles.
3.  Food stored using this method without barrels tends to attract vermin, especially swarms of flies, since it can't be placed in barrels.
4.  This method works well for furniture, cast-off clothing, metal and stone. A quantum minecart stop can be combined with some sort of garbage disposal mechanism to easily handle refuse and invaders' corpses.
5.  Note, however, that if your dwarves are under standing orders to ignore outdoor refuse (the default setting) they will also not load an outdoor refuse pile into the minecart.
6.  It has been observed that plant harvesting may be restricted by the number of empty valid stockpile spots. A larger receiving plant stockpile may be needed to get harvests done before the plants wither away.

## The Undump

This technique was developed before minecarts were implemented. While still a valid method, it has been superseded by the Minecart Stop QSP which achieves the same result, is easier to set up and has fewer drawbacks.

### Setup

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|   |   |   |   |   |   |   |   |   | H |   | H | a | t | c | h |   | c | o | v | e | r |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | = | = | = | = | = |   |   | ^ |   | p | r | e | s | s | u | r | e |   | p | l | a | t | e | , |   | c | i | t | i | z | e | n | s |   | t | r | i | g | g | e | r | , |   | l | i | n | k | e | d |   | t | o |   | h | a | t | c | h |
|   |   | ^ | s | H | s | = |   |   | = |   | W | a | l | l |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   |   | = | = | = | = | = |   |   | s |   | S | t | o | c | k | p | i | l | e |   | ( | s | a | m | e |   | t | y | p | e | ) |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

The idea is that haulers try to place some item on the right stockpile, step on the pressure plate and make the hatch cover retract. This makes them cancel the hauling job because they can't reach the right stockpile. They then drop the item on the left stockpile, on top of as big of a pile as you want.

More information on this method can be found on the inventor's user page.

### Drawbacks

This design has the following drawbacks:

1.  It's slow, because the one target stockpile generates only one job at a time. If you have more than one target stockpile they create lag because of pathing issues. You probably want to keep your normal stockpiles and use the undump to clean them up slowly. At which point you could consider just using the normal quantum stockpile dumping. Or you build more undumps.
2.  Job cancellation spam. You can turn that off.
3.  Oftentimes, dwarves drop the item on top of the pressure plate instead of on the stockpile. A feeder stockpile just outside the undump helps here.
4.  You obviously need some materials to build it.
5.  You need to create an open space tile where the hatch cover is (channeling only leaves a ramp), which means digging in the level below.
6.  You want to set the pressure plate to the lowest minimum weight (10000, which gets a zero cut off and displays as 1000). This can get tedious, so getting a macro is advised.
7.  If your stockpile management is exceptional already, the undump may not be of as much use to you.

However, there is a multitude of potential applications that get discussed in this thread.
