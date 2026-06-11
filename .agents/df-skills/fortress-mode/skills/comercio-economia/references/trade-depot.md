# Trade depot

> Fonte: [Trade depot](https://dwarffortresswiki.org/index.php/Trade_depot) — Dwarf Fortress Wiki (GFDL/MIT)

A **trade depot** is a building that allows you to engage in trading with the caravans that arrive at your fortress. Trade depots can be created from almost any building material. Three materials must be used to build the trade depot, with the oldest\* material chosen serving as the main material to determine color and "material" as labeled; the color is visible immediately upon confirming the construction order.

(\* i.e. the first material created or imported on your map, by chronological order.)

There must be at least 10 spaces between the depot and the edge of the map. They can be built on top of constructed floors and walls, allowing you to make a trade depot which is elevated above the surrounding land. Should they be deconstructed, the depot itself generates an implied walkable floor.

The visiting merchant(s) always stands at the upper side of the center table of the depot, while the player's broker stands at the opposide lower side. Graphically, the left side of the depot will show the visitor merchants' trade goods, while the right side shows items the player is setting up to trade.

## Depot accessibility

There is no visual indicator of wagon accessibility. For a tile to be “Wagon accessible” it must be navigable between both the tile and the depot \*and\* the tile and the map edge. If you are trying to constrain wagons to a certain path, *only* the desired path should be accessible. *Warning:* If the map has an extremely large amount of trees (Heavily Forested) there may not be any way for the caravan to get to your depot, unless you chop down a path for the wagons.

Also note that traps will block wagon access (although not merchants with pack animals), so you cannot easily use them to defend your depot.

Boulders (the natural kind) and tracks also block wagons. Boulders can be removed by smoothing (-) or constructing and removing a wall. Bridges can serve as an alternative for tracks.

Wagons park next to the trade depot and need a parking space of 3×4 adjacent to the depot.

Forbidding the trade depot (by forbidding any material used to construct it) will make it inaccessible to traders. If inaccessible during the arrival of the caravan, it will cause the wagons to bypass your location.

## Depot building UI options

Press to build a depot. Depots occupy a 5x5 area. Click on the depot to gain access to the following options:

### Move Goods to/from Depot

This command becomes active when a caravan arrives on your map. This screen menu is similar to the stocks menu ( - Stocks). This is where you select what items you want to trade with the caravan. If you have particular items you want to sell to the caravan, you can earch for it. This is convenient if you want to export all your prepared meals or finished goods. Also shown is the culling on andate option. The move to depot screen will not show things that violate an export mandate. By pressing , it will change to Ignoring andates, and you can select banned items for export. For example, if your mayor has a mandate banning the export of iron, this screen will hide bins that contain iron items. By changing this option, all iron items will be shown.

Items stored in bins, bags or barrels will be shown under the category of their respective containers, not under the category of the items themselves. For instance, if all of your gems are stored in a wooden bin, no "gem" category will appear in the move goods menu; the gems will be found under "bins." It is not possible to move these items individually. To bring them to the trading depot, you must select the entire container.

Items stored in bins can be traded individually once they have been brought to the trading depot. Items stored in bags/barrels can only be traded as a whole. This is also true of the merchant's wares.

After selecting items and exiting the screen, jobs will be queued to move the items to the depot. All adult dwarves, regardless of labor settings, can move goods to the depot. Items that have not been moved will show \[PENDING\], while those that have been brought to the depot and are ready for trade and will be marked as \[TRADING\].

Items selected for trading will remain at the depot until the caravan leaves. Alternatively you can select the item again. Once no longer required at the depot, items will be available for use or hauling to stockpiles as normal. If you don't want all the items to be returned to their stockpiles, you can optionally orbid them by looking at the iems in the depot.

(Note that the "Move goods to depot" screen allows mouse controls, including controls like right-clicking on a list to scroll down, and double-clicking on a tab to select all items in that tab.)

### No trader needed at depot *or* Trader requested at depot

This requests a dwarf to come to the depot. To conduct trades with caravans, a trader must be present at the Trade Depot. Once requested, a job will be created for a dwarf to make their way to the depot and remain there until released with this setting, or the job is interrupted, such as by the dwarf deciding to drink, sleep, or eat. The Trade at Depot job is fairly low-priority, so labors may have to be disabled in order to get the broker to begin the job, or the broker can be temporarily added to a burrow which covers only the depot.

### Only broker may trade *or* Anyone may trade

This setting determines who will perform the trade. If **Only broker may trade** is active, then only the broker noble will respond to the trader request. This can become a problem when the broker is sleeping or otherwise occupied, but dwarves with low appraisal skill will receive poorer deals when trading. If **anyone may trade** is selected, and someone other than the broker becomes a better appraiser than the broker, the broker's appraisal skill is still used.

### Trade

This option becomes available once the caravan unloading their goods at the depot and your trader is at the depot; it begins trading. If more than one set of merchants is using the trade depot, you will be given the option of who you want to trade with.

## Adventure mode

In adventure mode, a trade depot can be found in the surface structure of procedurally generated fortresses. It is usually filled with trade goods and people like nobles, farmers, craftsdwarves, and a broker, though in ruined fortresses there might not be any people. The player can talk to the people in the depot and then select the "Trade and settle debt" option to trade with them. Usually food, copper/iron armor, cut gems, and clothing can be purchased in large quantities in these trade depots.

## Bugs

- Setting a meeting area over a depot, then removing it, will cause dwarves to act as though it were still a meeting area. This is irreversible.
- Merchants in a trade depot who are accosted by hostile creatures may then refuse to trade. If any merchant is unable to make it to the depot, all the other merchants will similarly refuse to trade.
- Dumping items belonging to the merchants will result in the depot thinking the merchants are gone, when they are actually hanging around.
- Forbidding a depot, or slating it for removal immediately after causing the caravan trader to be unwilling to do business with your dwarves (e.g. trading wood to the elves) will cause the caravan to leave all their items and embark on their journey, leaving you to claim the items for yourself. This is treated by the game as seizing the items and will incur diplomatic penalties on the player, unless done to a dwarven caravan (as you cannot have bad relations with your own civilization).
- The game behaves poorly when multiple trade depots are available. Merchants with wagons may path to one depot, while those with pack animals path to the other; then both groups will insist on waiting for the rest of their party to arrive. One of the wagons will scuttle upon arriving at a trade depot if there are multiple depots, causing the caravan to leave immediately. For this reason, it is recommended to build only one trade depot.
- If you slate a depot for removal while merchants are in the process of leaving, the wagons will never leave and eventually the animals and remaining traders will go mad.
