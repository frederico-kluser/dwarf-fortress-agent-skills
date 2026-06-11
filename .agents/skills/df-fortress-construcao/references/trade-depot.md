# Trade depot

> Fonte: [Trade depot](https://dwarffortresswiki.org/index.php/Trade_depot) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **b - T**
- **Job Requirement**
- **Broker noble (optional)**
- **Construction**
- **Materials:** Jobs
- **3 Building materials (non- economic ):** Depending on material: Metalsmithing Masonry Carpentry
- **Purpose**
- **Trade goods with merchants .**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

A **trade depot** is a building that allows you to engage in trading with the caravans that arrive at your fortress. Trade depots can be created from almost any building material. Three materials must be used to build the trade depot, with the oldest\* material chosen serving as the main material to determine color and "material" as labeled; the color is visible immediately upon confirming the construction order.

(\* i.e. the first material created or imported on your map, by chronological order.[1])

There must be at least 10 spaces between the depot and the edge of the map. They can be built on top of constructed floors and walls, allowing you to make a trade depot which is elevated above the surrounding land. Should they be deconstructed, the depot itself generates an implied walkable floor.

The visiting merchant(s) always stands at the upper side of the center table of the depot, while the player's broker stands at the opposide lower side. Graphically, the left side of the depot will show the visitor merchants' trade goods, while the right side shows items the player is setting up to trade. If multiple merchants are at a single depot, the player will have the choice of who to trade with.

## Depot accessibility

There is no visual indicator of wagon accessibility. For a tile to be “Wagon accessible” it must be navigable between both the tile and the depot *and* the tile and the map edge. If you are trying to constrain wagons to a certain path, *only* the desired path should be accessible. *Warning:* If the map has an extremely large amount of trees (Heavily Forested) there may not be any way for the caravan to get to your depot, unless you chop down a path for the wagons.

Also note that traps, boulders (the natural kind), and tracks, will block wagon access (although not merchants with pack animals), so you cannot easily use them to defend your depot. (Boulders can be removed by smoothing (v-m) or constructing and removing a wall, bridges can serve as an alternative for tracks.)

Wagons park next to the trade depot, and need a 'parking space' of 3×4 adjacent to the depot.

Forbidding the trade depot (by forbidding any material used to construct it) will make it inaccessible to traders. If inaccessible during the arrival of the caravan, it will cause the wagons to bypass your location.

## Depot building UI options

Press bT to build a depot, which occupies a 5x5 area. Click on the depot to gain access to the following options:

### Move goods to/from depot

This command becomes active when a caravan arrives on your map (and stays active until for all caravans the announcement that they are packing there things is made). This screen menu is similar to the stocks menu (k - Stocks). This is where you select what items you want to trade with the caravan: ticking an item will generate a task for your dwarves to pick it from whatever stockpile it is stored in and move it over to the Trade Depot, and once there it will be available for trading; unticking items will make them no longer available for trade, and generate a task for your dwarves to move them back to the proper stockpile. If you have particular items you want to sell to the caravan, you can search for them. This is convenient if you want to export all your prepared meals or finished goods. Also shown is the culling on mandate option. The move to depot screen will not show things that violate an export mandate. By pressing , it will change to Ignoring mandates, and you can select banned items for export. For example, if your mayor has a mandate banning the export of iron, this screen will hide bins that contain iron items. By changing this option, all iron items will be shown.

Items stored in bins, bags or barrels will be shown under the category of their respective containers, not under the category of the items themselves. For instance, if all of your gems are stored in a wooden bin, no "gem" category will appear in the move goods menu; the gems will be found under "bins." It is not possible to move these items individually. To bring them to the trading depot, you must select the entire container.

Also for some stock categories, ie. seeds and "leaves and fruit", there is no category in the interface to move these goods to the trade depot. Meaning the only way to bring such items to the depot is if they are within a container (ie. bag or barrel), allthough traders might bring these items without any containers (only non-tree seeds will be brought by traders within a bag).

Items stored in bins can be traded individually once they have been brought to the trading depot. Items stored in bags/barrels can only be traded as a whole. This is also true of the merchant's wares.

After selecting items and exiting the screen, jobs will be queued to move the items to the depot. By default this hauling job (trade good hauling) is done via the "Haulers" work detail, but a custom work detail for only trade good hauling can be created. Standard work detail/labor rules apply for whether a dwarf is allowed to do trade good hauling with the standard work details (and settings) this means that basically all non-specialized dwarves will do trade good hauling. Note that trade good hauling takes precedence over most other tasks (and dwarves might even drop items they are currently hauling to do some trade good hauling). Furthermore children can be drafted to do trade good hauling as chore (and is activated by default). Items that have not been moved will show , while those that have been brought to the depot and are ready for trade will be marked as .

Items selected for trading will remain at the depot until the caravan leaves. Alternatively you can select the item again. Once no longer required at the depot, items will be available for use or hauling to stockpiles as normal. If you don't want all the items to be returned to their stockpiles, you can optionally forbid  them at the very bottom of the depot menu.

Bins (which contain items and where the bin is no longer marked for trading), which are in the trade depot and are not currently assigned to a stockpile (eg. because the bin was either purchased or has been deselected in the move goods menu) will be assigned to any stockpile, which allows bins with the contains items to be stored there, regardless of any stockpile links and whether the stockpile can take from anywhere or not, if any such stockpile exists and has still space the bin will be assigned to any such stockpile. Only bins, which are in the trade depot and are either forbidden or cannot find a stockpile, which allows bins, the contained items and has still space, will remain in the trade depot. Other items (and empty bins) in the trade depot on the other hand do respect the aforementioned stockpile settings (allthough empty bins in the trade depot can be assigned to stockpile). (Note: whether burrow settings of stockpiles in burrows can affect the assignment of bins in the trade depot to a stockpile or not has not been tested yet).

*Notes:*

- The time it takes to open the move screen is directly correlated to the amount of items in different tiles (as for each such tile a path from the tile with the item to the trade depot is computed upon opening the screen). Meaning the duration until the screen opens can be considerably speed-up by forbidding (via the stocks menu) the thousands upon thousands of loose boulders strewn about in the fortress prior to clicking the move goods to/from depot button (just don't accidently also forbid the building material of the trade depot).

- The reference, who did bring an item to the trade depot, will be saved as long as the items stays in the trade depot (and will be used, if traded, to determine, whether an export ban violation did happen). Items in bins do not get such a reference, if they are sold. Also items brought by the traders do not get a reference when bought. And items in the trade depot do not get there reference updated (or changed), if they are selected in the move goods to the trade depot menu (as they are already in the trade depot).

- Bins, which are forbidden and in the depot, while they are flagged for trading, will not have the flag (that they are traded) removed, when all the merchants have left.

- Items, which are in bins and sold in a transaction/trade (without the bins themself being sold in that trade), are added to the bottom of the trade depot in the order they did appear in the trade screen when the trade was issued (and ie. not the order of the item id or the order the items were selected for the trade).

- Items in the trade depot (as with all other buildings) are displayed in the order they were added to the building, where as items on the ground (ie. due to dumping) are ordered by item id (ie. "oldest" items are displayed first).

- Hair thread, once brought to the depot, will usually stay there until moved to a hospital or traded.

- Forbidden items in bins selected to be moved to the trade depot are dropped on the tile, where the bin is, when the bin is moved to the depot.

### Trade

This option becomes available once the caravan unloads their goods at the depot and your trader is at the depot; it begins trading. If more than one set of merchants is using the trade depot, you will be given the option of who you want to trade with.

### Requested trader

This setting determines who will perform the trade and requests a dwarf to come to the depot. To conduct trades with caravans, a trader must be present at the Trade Depot. Once requested, a job will be created for a dwarf to make their way to the depot and remain there until released with this setting, or the job is interrupted, such as by the dwarf deciding to drink, sleep, or eat. The Trade at Depot job has a fairly high priority, ie. a dwarf currently working in a workshop (without that workshop job having been set to the highest priority) will go to the trade depot at the next possible opportunity (allthough the dwarf will still finish the current sub-task of the workshop job before doing so) - still eating, drinking, sleeping and purple-colored worshipping take precedence over the trade at depot job. Also it might be a good idea to temporarily disable the animal hauling for the broker as a dwarf currently leading an animal will not abort that job to go to the depot.

If **Broker requested at depot** is active, then only the broker noble will respond to the trader request. This can become a problem when the broker is sleeping or otherwise occupied, but as the broker has usually higher "haggle skills" than the other dwarves it is harder to receive good deals (and due to the lower appraisal skill fewer goods can be accurately appraised). If **Anyone requested at depot** is selected, and someone other than the broker is currently trading, then the appraisal skill of the trading dwarf is used inside the trade screen to appraise the goods.

## Adventure mode

In adventure mode, a trade depot can be found in the surface structure of procedurally generated fortresses. It is usually filled with trade goods and people like nobles, farmers, craftsdwarves, and a broker, though in ruined fortresses there might not be any people. The player can talk to the people in the depot and then select the "Trade and settle debt" option to trade with them. Usually food, copper/iron armor, cut gems, and clothing can be purchased in large quantities in these trade depots.

## Bugs

- Purchased items stay at the Trade Depot indefinitely after the merchants have left, unless a stockpile is present AT THE SAME LEVEL as the Trade Depot itself. The simplest and quickest way to force stuck items into stockpiles on other levels is by deconstructing the Trade Depot altogether and rebuilding it after all of those items have been hauled away.Bug:12920
- Setting a meeting area over a depot, then removing it, will cause dwarves to act as though it were still a meeting area. This is irreversible.
- Merchants in a trade depot who are accosted by hostile creatures may then refuse to trade. If any merchant is unable to make it to the depot, all the other merchants will similarly refuse to trade.
- Dumping items belonging to the merchants will result in the depot thinking the merchants are gone, when they are actually hanging around.
- Forbidding a depot, or slating it for removal immediately after causing the caravan trader to be unwilling to do business with your dwarves (e.g. trading wood to the elves) will cause the caravan to leave all their items and embark on their journey, leaving you to claim the items for yourself. This is treated by the game as seizing the items and will incur diplomatic penalties on the player, unless done to a dwarven caravan (as you cannot have bad relations with your own civilization).
- The game behaves poorly when multiple trade depots are available. Merchants with wagons may path to one depot, while those with pack animals path to the other; then both groups will insist on waiting for the rest of their party to arrive. One of the wagons will scuttle upon arriving at a trade depot if there are multiple depots, causing the caravan to leave immediately. For this reason, it is recommended to build only one trade depot.
- If you slate a depot for removal while merchants are in the process of leaving, the wagons will never leave and eventually the animals and remaining traders will go mad.
