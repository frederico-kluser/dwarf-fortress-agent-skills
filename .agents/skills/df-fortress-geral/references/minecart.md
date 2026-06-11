# Minecart

> Fonte: [Minecart](https://dwarffortresswiki.org/index.php/Minecart) — Dwarf Fortress Wiki (GFDL/MIT)

A **minecart** is a tool intended for hauling. It can be made of wood at a carpenter's workshop or 2 bars of metal at a metalsmith's forge (using the blacksmithing labor.) Minecarts store up to five times as many items as wheelbarrows and are quite a bit faster than dwarves hauling objects by hand, but have the disadvantages of requiring a dedicated track network, a complex route planning phase, and the possibility of dwarves blundering into the path of carts filled with lead ore. Tracks may be carved into stone, or constructed; the latter allows above-ground routes, but these are more difficult to set up due to their additional material requirements.

Just like wheelbarrows, minecarts are considered items and are stored in a furniture stockpile. Despite their five-times-greater capacity, they are only 33% larger than wheelbarrows (minecarts have a size of 4000) and are identical in base value when made from the same material (the value may differ due to the item quality). Thieves or even mischievous animals can steal minecarts, even when they are moving on a track. However, minecarts moving fast enough or being ridden cannot be stolen.

Although most of the utility of minecarts is in fortress mode, an adventurer can also ride in a minecart. Adventurers can also pick up and relocate minecarts.

The invention of minecarts revolutionized the Science of Dwarfputing by enabling smaller, faster logic systems to be built.

## Basic Minecart Usage

Minecarts can be used to swiftly transport dwarves, fluids, and/or large amounts of items, but before you have a functional minecart, there are several preconditions that need to be met. First of all, you need an actual minecart, constructed either in a carpenter's workshop or metalsmith's forge. For the minecart to be able to move, you also need to carve (with ) or construct (with ) a track, which could be as simple as a straight line. Finally, you need to construct stops on your track (with ) where the minecart will start and stop.

After you have created the stops and assigned a cart to the track, you must create logic routes connecting several stops and designate starting conditions for each stop. This is done with the hauling key. The most basic conditions are how the cart's movement is initiated and in which direction the cart should start moving. Carts can be either pushed (a dwarf stands at a stop and gives the cart a single push) or guided (a dwarf continually pushes the cart forward, guiding it along the track). The hauling labor required for pushing and guiding carts is called "Push/Haul Vehicles" and is turned on by default.

To control which items are to be transported, you can add conditions specifying: (1) which kind of items are to be loaded and unloaded, (2) stockpile links to define which stockpile(s) the items should be un/loaded to and from.

### Capacity and weights

Minecarts have a size capacity of 50,000 – five times the capacity of wheelbarrows.

**Examples of the capacity of one cart**

| Item                                                      | Amount |
|-----------------------------------------------------------|--------|
| stone                                    | 5      |
| log                                         | 10     |
| block/bar                   | 83     |
| minecarts                                                 | 12     |
| prepared meals                | 500    |
| spiked balls | 500    |
| Sand bags                   | 500    |
| mace                      | 625    |
| spears                  | 1250   |
| cloth                                    | 2500   |

The weight of the loaded minecart does not affect the initial velocity received from pushing or launching from a roller. However, the load of a minecart *does* affect whether a pressure plate triggers or not, based on the pressure plate's setting.

**Weights of different carts**

| Type of cart      | Empty cart | Fully loaded (items)         |
|-------------------|------------|------------------------------|
| oaken minecart    | 28Γ        | 378Γ (10 oak logs)           |
| iron minecart     | 314Γ       | 1698Γ (83 marble blocks)     |
|                   |            |                              |
| copper minecart   | 357Γ       | 1682Γ (10 obsidian boulders) |
| platinum minecart | 856Γ       | 10482Γ (83 gold bars)        |

The weight of a minecart is one twenty-fifth (1/25) the density of its material in Urists. Because pressure plates can be set to trigger at intervals of 50 Urists, minecarts with weights just under a multiple of 50 are ideal for switching based on whether they're full or empty. The best minecart materials for full/empty switching are as follows:

| Material | Minecart weight | Content weight required to trigger | Banana roasts required to trigger (for scale) |
|----|----|----|----|
| Glumprong | 48 | 2 | 4 |
| Electrum | 596 | 4 | 7 |
| Nickel silver | 346 | 4 | 7 |
| Brass | 342 | 8 | 14 |
| Bismuth (moods only) | 391 | 9 | 15 |
| Fine pewter | 291 | 9 | 15 |
| Lay pewter | 291 | 9 | 15 |
| Tin | 291 | 9 | 15 |
| Trifle pewter | 291 | 9 | 15 |

### Creating tracks

Minecart tracks are made up of contiguous track, tracked ramp, or bridge tiles. Track tiles and tracked ramp tiles have a direction or series of directions associated with them. These directions dictate which directions a minecart on a given tile may move from that tile. For example, a Track NE (northeast) tile allows a minecart on it to move either north or east from its present position. Therefore, if you want your minecart to move east along a straight piece of track, then return west using that same track, you would need to use EW tracks so that the cart could travel east initially, then return west over the same track. Excluding designs in which the cart will "jump" tracks via a drop or other ramp, tracks must be valid end to end to work for most looped or straight-track applications. A single east only track tile in your line of east-west tracks will cause any route using the track to fail the moment it tries to go the wrong way over that tile. Minecart tracks can be built in two ways: Engraved/carved or constructed. A given minecart track need not use engraved or constructed elements exclusively, as the two methods can be used interchangeably depending on the needs of a given section of track. The way the tracks are built is slightly different between the two, as explained below.

#### Simple tracks

**Carved**

A single-tile wide strip of natural stone can be designated to be carved (with ), which will create a straight two-way track. The creation of corners, crossings, and T-junctions is as simple as designating another strip of track that overlaps an existent or newly designated track. Engraved tracks are removed by smoothing the rock they're on, which results in a smooth floor (that can be re-engraved if necessary), or by building a floor on top and subsequently removing it. Dwarves can carve corner tracks in one pass by designating the track carving twice and canceling unwanted carvings (with ). Tracks can be engraved in any natural floor tile, rough, smooth and even over engravings, providing an easy method to remove low-quality or undesired floor engravings. Once a track has been engraved, it's important to check the track directions for each tile in the route carefully to make sure no mistakes were made by yourself or the game's track engraving logic.

**Constructed**

Tracks can also be built as regular constructions (through . This method is resource-expensive, since each track tile requires one stone, bar, or block for construction. Corners, crossings, T-junctions, and ramps also have to be designated individually. However, it is usually the only way to build tracks above ground or on soil (barring the creation of obsidian). Constructed tracks are designated for removal like any regular construction; be aware that removing track ramps built on top of natural ones will also remove the original ramp, leaving a flat floor.

#### Ramps

**Carved**

The carving of natural ramps is a little more confusing: to carve a two-way track on a ramp (natural only, does not work on constructed ramps), you must designate the track **starting on the ramp and one square beyond** in the direction you want the track to go. For the side of the ramp square you want to head upward, there **must** be either a natural or constructed wall in the square next to it, otherwise the game assumes you are trying to carve it on the same level – this can result in the track being carved underneath a door or other object. If you have accidentally done this, you can correct it by smoothing the ramp and constructing a single square of wall next to it, then re-carving the ramp correctly, however, the wall must stay there permanently — removing it will disconnect the track.

**Constructed**

The track and ramp must be constructed together as a Track/Ramp from the construct track menu ( ). When constructing track ramps, the stated direction should be the same as the connected tracks. For example, a track going up from West to East would require, starting from the West, a Track (EW), a Track/Ramp (EW) and a Wall behind the ramp, underneath the section of track above it. Incorrectly placed ramps result in minecarts ignoring the ramp and crashing into the supporting wall. They will not, however, display as unusable as when the supporting wall is missing.

**Examples of ramps**

A simple ramp would look like this:

Carving track corners into ramps is rather unintuitive and complicated. Since engraving tracks always requires two tiles to connect in a straight line as input, you have to give two separate designations for a single job: a track bit from the ramp tile to the "below" direction and another one to the wall of the "upward" direction. If you wanted to change direction on a ramp from east to north:

you would need to connect the ramp on z +0 both to the west and to the north by issuing two "carve track" commands, one selecting the ramp and the track tile to the west, and another connecting the ramp tile with the wall to the north. An engraver would then carve a NW track corner into the ramp, allowing carts to pass the corner correctly both going up and down. Such track corners are perfectly serviceable for guided carts, but moving down a route of several of them by pushed or ridden cart is problematic - ramps on corners behave very counter-intuitively, resulting in loss of speed when going down and diagonal movement when going up.

Moving to and from ramps (or between ramps "pointing" in different directions) causes some non-trivial adjustments to speed and even moving along the tiles at a fixed speed *unrelated to the entry/exit velocity values*, because transitions to/from ramps are processed differently and are not to be "skipped". This affects compact track/ramp combinations (such as e.g. a simple 2x2 ramp spiral) most, and combined with bouncing often makes them work not in the way one could expect.

### Hauling route

A hauling route is a list of directions describing how and under what conditions a minecart will move. The proper setting up of routes is essential for a working rail system. Routes, stops, departure conditions and stockpile links are managed from the auling menu.

#### Route

A route defines the path a minecart will take along a track, as well as under what conditions it will move or stop moving. A route is made up of stops. Stops are precisely what they sound like, a position on the track at which you want a minecart to stop. A minecart track might use as little as a single stop for a looped track, which will serve as both a starting and stopping point for the cart, or it could contain many stops, perhaps to load supplies or wait for a bridge to be manually lowered, before reaching its destination or returning to its starting point. It is important to note that you only need to place stops on a route where you actually want the cart to stop and wait for some action to occur. They are not needed to help navigate the cart along the track beyond telling it where on the track to stop.

New routes are created with the auling key. Existing ones can be removed (without confirmation) with the key, and also icknamed. Before operating, the route must have a ehicle assigned to it (this can be done with either the route or a stop selected). Assigning a full minecart to a route may result in a slow hauling job if the contents are heavy.

#### Stops

Stops are the individual waypoints that make up a hauling route. A given stop consists of the location of a tile, as well as conditions describing when, where, and how a cart should be moved after being stopped at that tile. Stops can be created from within the auling menu, by placing the cursor over a tile and hitting while highlighting the route (or a stop within) you've already designated. A minecart will begin its route at the first stop created, and continue through each subsequent stop, being guided, pushed, or ridden from each stop to the next depending on the conditions specified. In many basic minecart applications, the cart will end up at the same stop it began at, though this is not always the case. It is important to note that hauling stop order is enforced, even if there is no track. A dwarf will drag the cart overland back to a skipped stop in the route's list if your tracks bypass it somehow, including if the minecart does not stop on the stop after it is pushed/ridden.

Once a stop has been placed, it is given a default set of conditions under which to move the minecart if it is stopped there. Each new stop gets the same default conditions regardless of the track it is placed upon (e.g. guide the cart to the north). For this reason new stops might get marked by yellow exclamation marks () due to invalid directions. One important thing to note is that as you place additional stops, the display will show paths between the stops you have defined. However, this is **not** necessarily the actual route the minecart will take once the route is in operation. For example, if a route were defined with two stops at opposite ends of a track with many twists and turns, a line will be drawn directly between those stops to show the order in which they will be visited. These route lines may crisscross all over the tracks, but so long as the track is valid end to end, the cart will follow the track from one stop to the next, even across twists, turns, and z-level changes. Route stops, which are the steps that make up a route, should not be confused with physical Track Stops, described below.

Note that setting a stop on a sloped track may cause the minecart to roll away, preventing it from being properly loaded.

##### Stockpile links

By placing the cursor on top of a stockpile and using , you can create stockpile links while defining a hauling stop. Links can also be redefined by selecting them, placing the cursor over a different stockpile, and pressing . The cart will then be filled by items present in its various linked stockpiles in preference to other items. Note that bins should be used with caution in stockpiles that are linked to minecarts. Bins cause problems when used with the "Desired Items" list in a stop's conditions. For example, if a minecart is set to accept only granite blocks, and to depart north when it is 100% full of granite blocks, it will not depart if any of those granite blocks are in bins, even if bins are also included in the desired items list. Two solutions to this problem exist as of v0.40.24. First, bins can be disallowed in stockpiles that are linked to stops. Alternatively, bins **can** be used in conjunction with minecarts provided that the minecart's departure conditions use only "any items" instead of "desired items." This option can be toggled in the advanced conditions menu for a stop, accessible via the key. The cart's contents can still be controlled by specifying what items are allowed in the linked stockpile.

##### Departure condition

Departure conditions involve setting conditions in which the minecart will leave on the route. Each condition includes:

1.  A departure mode (Guide, Ride or Push).
2.  An initial departure direction (NSEW). Note that this defines the initial direction of movement only. Even if a track includes many turns, as long as the initial movement direction is valid the cart will follow the minecart track thereafter.
3.  A timer, before which the departure condition cannot be met.
4.  Conditions on the amount of items in the cart.

Departure conditions are created with the key. A new departure condition will read: "guide north immediately when empty of desired items". This condition can be changed between basic presets with . "Advanced" mode () allows for more precise control over departure conditions: fine tuning the percentage from 0 to 100 in 25% steps ( and ), switching it being either the maximum or the minimum amount of items for the condition to be met (), and whether the cart accepts all or only a specific set of items (). Common to both screens are the departure mode (, Push, Ride or Guide), irection, and timer ( and ) options.

To have a cart only carry a specific set of items, the stop can be set to only carry "desired" items, opening the selection screen with the key while having said stop condition selected, and toggling as desired, or it can simply be linked to a stockpile and set to depart once it is full of items from its linked stockpiles, regardless of type.

### Track Stops

A Track Stop, not to be confused with a route stop, is an optional, single-tile construction which serves two purposes. First, it can be used to cancel a cart's momentum in order to slow or stop it as it passes over the Track Stop. This might be necessary if a cart were pushed down a series of ramps to its destination. Second, a Track Stop can cause a cart to automatically dump its contents as it passes over the Track Stop. Track Stops are constructed via , and must be constructed atop an existing piece of track. If a Track Stop has been set to automatically dump a cart's contents, the cart will dump its contents in the direction indicated when it passes over the Track Stop. Depending on the friction settings chosen for the Track Stop, the cart might then stop after dumping, or it might continue on its route to another destination.

Track Stops are not mandatory; in fact, their main use is in automated rail systems. However, even in basic rail systems it can be useful to set a Track Stop to dump items: this saves time that dwarves would otherwise spend in removing items from the cart, time that is better spent driving the cart back to where it's needed. Dumping will occur even with a guided cart. **Take care not to set Track Stops at a loading site to dump their contents**, or dwarves will never be able to fill the cart. It will dump any contents the moment they are loaded.

- See More on Track Stops

### Step-by-step tutorial

Let's construct a simple minecart route. This route will move stone blocks from an input stockpile to an output stockpile. We'll begin by creating the stockpiles:

The input stockpile is on the left; the output stockpile is on the right. We'll be moving blocks from left to right. Disable bins in both stockpiles, and set the input stockpile to accept only from links. Then make the stockpile take from the mason's workshop where the blocks are being produced.

Next, carve the track:

Note that the ends of the designation are uniquely shaped; this is automatic, and not anything you need to control. Now, wait for your engravers to come along and carve the track into the stone. (Your haulers will probably also fill up the input stockpile while you wait.)

In addition, while we're waiting for that to happen, we'll build an iron minecart in the forge.

When the track has been carved, it will look like the above (the track will be solid instead of flashing). Now, order a track stop to be constructed (Under "Constructions") next to the output stockpile:

|     |     |
|-----|-----|
|     |     |

You must select the dumping direction *before* placing the track stop. We want our blocks to be dumped into the output stockpile east of the track stop. Then wait for a mechanic to come along and build the track stop.

Now we'll define the actual *route*. This is done in the auling menu. Press 'Add New Route' to begin defining a route. Select 'Add a stop' then click the track next to the input stockpile:

|     |     |
|-----|-----|
|     |     |

Select 'Add a stop' again then click the stop next to the output stockpile define the second stop:

|     |     |
|-----|-----|
|     |     |

At this point, the route has been positioned, but they haven't been *defined* yet.

Click the Minecart icon for the route (not the stop) and assign a minecart to the route.

Select the minecart icon for the first stop to select what items will be hauled to the minecart. By default no items will be hauled to the minecart. As we've set the input stockpile to only take blocks from the workshop, you can either set to to accept blocks, or set it to accept all items.

Click the stockpile icon for the first stop, select the "take from" icon (middle button) and select the input stockpile.

Select the Conditions button (**\=≠**) for the first stop and check out the defaults. For the first stop, these are largely fine however you should change the direction button for all the conditions so the minecart goes the correct direction when it's ready.

Select Conditions for the second stop. These need to be changed so the minecart is returned to the start immediately. Erase the bottom two conditions, change the direction to point back to the stop, and then finally click the **\>=** button so it changes to **\B off while toggling A\B, with a corner (not a T section). Fast moving carts will tend to derail at D and rejoin the track to C. Placing a door at D will prevent the derailment, so the cart continues to B. The door is operated by mechanisms elsewhere (typically, a lever, but some fun can be had with pressure plates).

Since it depends on derailing, this switch requires a very fast cart, faster than what can be achieved with rollers alone. To gain sufficient speed, a cart must be accelerated further, usually by descending several levels or through impulse ramps. The high speed makes the cart much more dangerous and harder to control.

If carts are moving too slowly to derail at the corner, a retractable bridge may be used as a connector between A and C. The bridge must overlap the corner. Bridges behave like a track crossing, allowing carts to pass in a straight line. When retracted, the corner reappears, so the carts will continue to B. Bridges take 100 steps to react to a signal, necessitating rather long "lead times" when switching tracks via bridge.

As mentioned above, special care must be taken to make sure the bridge doesn't change state while the cart is passing over it. Retracting bridges will throw the cart, causing it to stop dead. Raising bridges can even crush the cart.

#### Controlling Speed

Minecarts can reach extremely high speeds, especially when descending multiple Z-levels. A minecart will derail at a track corner if its speed exceeds 0.5 t/st (tiles per step), **unless** the route in the direction of travel is blocked:

Will derail at \> 0.5 t/st:

Will not derail at \> 0.5 t/st:

This behavior can be used to build a "speed limiter", that will ensure that when a minecart exits it is traveling below derail speed, as illustrated in these three examples: If the minecart is traveling below derailment speed, it will not be affected; if above, will be slowed down and checked again. Granted, you could do the same just with track turns, but it may take a lot of turns and time.

Since all the derailings, bounces and ramps can impart a sideway component of speed small enough to start visible drift many tiles away (say, in the middle of a bridge), track turns have one more use: forcing the carts to move strictly along the grid directions. Carts passing a turn below derailing speed convert one component of velocity into another, thus eliminating the drift.

### Loading liquids

Water and magma can also be loaded into minecarts by submerging them to a depth of at least 6/7 while standing still or moving at speeds of at most 10000. Loading fluids onto minecarts can be difficult because the added friction provided by fluids can stop a cart in a submerged tile. Curiously, filling a minecart with magma does not injure a dwarf *riding* it. A minecart will hold enough fluid to increase the depth of a single tile by 2. This amount is listed as 833 units, which weigh 459Γ (water) or 999Γ (magma). An iron or steel cart filled with magma weighs 1313Γ, while an adamantine cart filled with magma weighs 1007Γ. Since you need a minecart above the liquid's level, possible arrangements may include pressure-activated sluices, rollers (with magma-safe chains for magma), pouring from above to "submerge" it briefly on the same level and drain excess away (dig deeper and leave a vaporizer, though if you could have power for rollers, may as well use a pump) and exploits with ramps (not necessarily impulse ramps, "same height" passing dip does it). The liquids can be dumped by a constructed track stop.

## Quirks

This little quirk concerns dwarf-managed minecarts. If a track which was previously open becomes blocked (ex. flipping a switch connected to a floodgate you've built on the track to raise it) and the conditions for departure are met, instead of refusing to ride/guide the minecart or ride/guide it until it reaches the obstacle, the dwarf will pick up the minecart off the tracks and haul it to its scheduled destination on foot. If the distance is long enough and the weight of the cart heavy enough (due to being filled with heavy items such as stones), the dwarf may drop the cart because of fatigue/hunger/thirst before reaching the destination. This will cancel that vehicle setting job and make another dwarf come by and attempt to haul the cart to the nearest appropriate stockpile where another dwarf will pick up the cart and attempt to haul it to its initial stop. If the stockpile is far enough from initial stop, this second dwarf who is attempting to place the minecart on its tracks may also drop the minecart out of fatigue/hunger/thirst creating a loop that will go on until a dwarf with enough endurance manages to place the minecart where it belongs.

In fact, it seems dwarves are more than happy to attempt to carry a minecart from one stop to another even if just waiting until the track is open again would be the more sane option.

Dwarves will also carry a minecart to its next stop if the direction specified is incorrect (or invalid). This can often occur when using the default departure settings and forgetting to set the direction of each condition.

Dwarves can admire buildings while riding mine carts. Dwarves will not fall asleep during a ride (at least not from being drowsy). If riding on a continuous powered track loop, the dwarf will die of dehydration/starvation as they can not jump off to get sustenance. Dwarves riding in submerged minecarts will gain experience in swimming.

Tracks block wagon access to trade depots, unless they're on a ramp. Bridges can also be used, as they function as tracks but do not block wagons.

## Physics

Minecart physics depend greatly on the departure mode set in the route stop conditions.

When set to "Push" or "Ride", minecarts will move according to the regular laws of momentum, gaining speed when going downhill, losing it slowly due to friction when on a flat plane, and more quickly when going uphill. In these modes, minecarts will move in a straight line until they either are brought to a stop by friction or an obstacle, or until they encounter a turn. A minecart will roll straight past "blocked" ends of T-junctions or track ends, they have no power to restrict a cart's movement. The cart's behavior is largely independent of the weight of its contents (including fluids and dwarves): heavily loaded carts gain more momentum when accelerating, but this only plays a role in collisions: a heavy cart gains just as much speed and is as easy to stop as a light one. In either case, dwarves can not push nor ride an unpowered cart up a ramp. The cart will stall and roll back towards the direction it came. At best, this is a waste of time; at worst, it will give your cart-pushing dwarf a fun surprise. To solve this, the player can either use Rollers (see below) or set the cart to be Guided.

The difference between "Push" and "Ride" is whether the dwarf will go along with the cart or not.

the dwarf will give the cart an initial push, not enough to go up a ramp, but enough to go some way along flat track. The dwarf will remain at the first stop, ready for a new job.

the dwarf will give the cart the same initial push and then hop aboard the cart riding it to the next stop.

the dwarf will steadily walk the cart to its destination while seemingly ignoring all laws of physics.

While being guided by a dwarf, minecarts will:

- Ignore the weight of any and all items inside.
- Ignore active working rollers.
- Will *not* collide with other guided carts even when a full frontal collision would be expected.
- Will ascend ramps with ease like a crundle scaling a cliff.

Because of these quirks, minecarts being guided will always move at the speed of the dwarf that is guiding them. It is thus recommended to pick the most agile of your dwarves for cart-guiding tasks. It also means for simple non-powered rail systems, "Guide" is the recommended method of transport despite it diverting a dwarf from other, potentially more important tasks.

Some samples with behavior: In the second example above, a cart "pushed" from B will go over the junction and roll off into the unknown south.

### Numbers behind the scenes

According to early research by **expwnent**:

The minecart has 3 variables for velocity. Velocity can be thought of as tiles per 100000 ticks, so a velocity of one hundred thousand means a cart travels one tile per tick. By going down a large number of ramps, a maximum velocity of 270,000 can be reached, which presents the limit for most practical applications. Short bursts of (much) higher speeds are possible through carefully planned collisions of high-speed carts. (See Perfectly Elastic Collisions.)

Every tick the cart adjusts sub-tile position units by the amount of their velocity, as well as adjusts velocity depending on current tile (speed is reduced by the "friction" of the tile, or accelerated if going "down" a ramp). On flat (non-ramp) tiles, the cart will move to the next tile when the sub-tile position goes 50000 away from the centre of the tile, denoted by the no-fraction integer value - tile 15 e.g. has its centre at the exact value 15 and its borders at co-ordinates 14.5 and 15.5.

Since most deceleration and acceleration is applied per step, with the notable exception of corners, a cart going at twice the speed of another one can travel about four times the distance before coming to a stop when going in a straight line, but only twice the distance along a winding track with very many corners.

A push will teleport a cart to the middle of the next tile in one tick with 19990 speed (10 speed is lost due to track friction), while a roller will directly give a cart the roller's set speed (minus friction) and the cart starts accumulating distance from its standing position. When a cart leaves a ramp it will emerge after one tick at the very end of the next regular tile.

Friction of tiles:

| Tile | Friction | Comment |
|----|----|----|
| Tracks | 10 |  |
| Ground/Floor | 200 |  |
| Unusable ramp | 10 |  |
| Upwards ramp | 4910 (10+4900) |  |
| Downwards ramp | -4890 (10-4900) |  |
| Roller | ±100000 (but capped by the set speed) |  |
| Corner track | 10 | Speed reduced by 1000 upon leaving the corner tile |
| Track stop (highest) | 50000 |  |
| Track stop (high) | 10000 |  |
| Track stop (medium) | 500 |  |
| Track stop (low) | 50 |  |
| Track stop (lowest) | 10 |  |
| Water 1-6 | Additional (WaterLevel - 1) \* 100 | See Skipping |
| Magma 1-6 | Additional (WaterLevel - 1) \* 500 |  |
| Empty space | 0 |  |

Water of depth 7/7 provides a friction of about 10000 per step. Maximum-depth magma causes at least as much friction, possibly more. This higher friction may not apply to very slow-moving carts.

Impulse sources:

| Feature        | Speed |
|----------------|-------|
| Push           | 20000 |
| Roller lowest  | 10000 |
| Roller low     | 20000 |
| Roller medium  | 30000 |
| Roller high    | 40000 |
| Roller Highest | 50000 |
|                |       |

Note, again, that nearly all of these values are applied *per tick*, rather than *per tile*. The exceptions are curves, which is 1k deceleration per direction change at the end of the tile, and rollers, which *set* the speed every tick. This makes rollers particularly useful in high-deceleration situations, such as underwater, but require that *nearly every tile* in such high-deceleration situations have a roller.

A cart heading up a ramp can experience deceleration on multiple ticks, (and stays on the tile more ticks the slower it is going, resulting in greater deceleration,) and as such, a cart leaving a "Highest Speed" roller with 50k velocity will not be able to climb 10 consecutive straight ramps, since they are *not* "5k deceleration each". In fact, the first ramp not on a roller will be -15k velocity, and, depending slightly upon other factors of "remainder" x position, the second may completely cancel forward momentum, and send it rolling back down, where it will bounce off the roller repeatedly. Using rollers to power carts up ramps reliably requires rollers every other un-rollered ramp. Fortunately, rollers can be built upon ramps, themselves, which allows for rollers to only need to be built every other floor. (Exploiting the checkpoint effect can allow one to bypass this requirement.)

There are two important speed values which affect carts' behaviour:

"Derailing" can happen when a cart moves at speeds in excess of 50000 - carts will ignore track corners unless forced to obey them by walls or other obstacles blocking the straight path.

The "shotgun" effect takes place when a collision changes a cart's movement speed by more than 55000: loaded carts subject to such a change eject their contents, which then keep on moving in a ballistic trajectory, in the direction and at the speed the cart had before the collision (with a small random vector added). This effect entirely rides on the amount of speed *change* - a speeding cart crashing into a wall can be subject to it just as well as a standing cart accelerated by a speedy cart smacking into it. It can even happen when two relatively slow-moving carts (down to speeds below 20000 in extreme cases) collide head-on.

### Sub-tile Positions and Velocity

Carts store six values that are unique to them. Three sub-tile position values, and three velocity values. (X, Y, and Z.)

Note that the Z position and velocity only matter when a cart is in flight. (See Falling and Cart Jumps.)

Each non-ramp tile is functionally composed of 100,000 individual minimal-length positions *within* the tile in both dimensions. When a cart has velocity, it is added or subtracted from the current position every tick, and then a friction force is applied to the cart.

In essence, every sub-tile position unit is a decimal value of a tile, 0.00001 tiles, in a game that largely prefers integer values.

The exact cart coordinates shown e.g. by a DFHack script must be rounded arithmetically (up or down to the nearest integer) to find the current tile: a cart in the centre of a tile will be at sub-tile zero in all directions, and it will cross into the next tile when subtile value is more than 50 000 higher or lower than the full number.

When carts move beyond the borders of a tile, they physically move a tile on the map, and start at the far end of the sub-tile position the next tile. (I.E., traveling West, a cart that starts a tick 15,000 X away from the border and has an X velocity of -20,000 will move -5000 X past the adjacent border of the next tile in direction -X. It will also lose 10 velocity in that tick due to friction with the track if it is on a track, or 100 velocity if it is on regular ground, or no velocity if it is airborne.)

Ramp tiles are longer, approximately 141,420 in the direction where it "slants downward", (to approximate a 45 degree slope, it is square root of two times longer,) with a centre-to-border distance of 70,710. Because of this, a cart with no velocity dropped from a hatch will land at the center of a tile, 70,710 away from the tile's borders in both directions, and will start rolling in the ramp's "downward" direction, picking up the ramp's acceleration (4890 per tick in the direction of the ramp's "downward" direction) every single tick, then moving that sub-tile amount every tick. (This results in a cart that takes 5 ticks of acceleration to leave its ramp - 6 ticks overall - and to leave the ramp with about 23k velocity, slightly more than a push.) When it enters another ramp *facing the same direction downwards*, a cart will start at the -70710 or +70710 position, and have twice as far to travel. This means that if a cart enters a ramp from the side, it will gain twice the momentum of simply starting at the midpoint of a ramp.

Note that passing from one direction of ramp to another or to flat terrain causes unintuitive behavior, "teleporting" to the end of another tile in what is called the "checkpoint effect".

Note, however, that all sub-tile positions are carried over from tile-to-tile. This separate tracking of velocity and position between X and Y can lead to problems with diagonal motion:

If a cart is passing West-to-East over this setup, the valid ramp to the South will apply "Southward" acceleration to the cart (-Y velocity) as it passes through the ramp tile. Assuming it only spends two ticks in that tile, it will have gained a lasting -5k Y velocity, which will still apply motion Southward. If the cart continues travelling over straight track for another ten steps, it will have accumulated enough Southward motion to try to move a tile South, even if all tracks are facing East-West.

A single tile spent on the ramp will not grant lasting southward motion, because the acceleration will be neutralised through the checkpoint effect when the cart leaves the ramp again, but the cart will be displaced about 5k sub-tiles southward, which can cause it to gain more or less speed than an undisplaced cart when meeting another south- or north-accelerating ramp.

**Non-curving tracks do not correct this motion**.

They don't "tip back over" without adjustments in the track. Any value of sideways motion on tracks larger than 990 will lead to a derailment. (Lower values will be nullified by friction before they are enough to lead to derailment, but there is currently no way to apply such a small amount of velocity.)

If the tile to the South is a wall at that point, it will be considered a collision with a wall that *halts all motion*. If the tile is open, the cart will simply leave the track and travel over the terrain beside it. In almost any circumstance, this is undesirable behavior.

The only way to appropriately deal with this is to either cancel out this behavior with an equal amount of acceleration in the opposite direction, or to take a curve.

Note, again, that sub-track position is saved in both directions, so when a cart approaches a curve, it will already have a shorter or longer distance past the curve when it makes the turn.

Curves are applied at the end of a tile. If a cart is moving East, and approaches a North-West track corner at 30k velocity, and friction is eliminated for the purposes of a cleaner demonstration, then when it enters the tile on the western (X coordinate) border of the tile, but in a central North-South (Y) orientation (sub-tile -50k X and 0 Y due to arithmetic rounding), it will then move 30k East (+X) the next tick, and be at -20k X sub-tile position, and 0 Y sub-tile position. Next tick, it is at +10k X sub-tile position, and 0k Y sub-tile position. Two more ticks would take it to +70k X, but that's past the tile border, so it stops at 50k, turns (and thus loses 1k velocity, but translates the rest from X-velocity to Y-velocity) and travels another 20k. It is now at 0k X sub-tile position, and -20k Y sub-tile position (i.e. it's re-set from the end to the middle of the tile with respect to the X co-ordinate). Next tick, it travels at 29k velocity North, and so moves to 0k X sub-tile position, and +9k Y sub-tile position. Then in two more turns, it leaves to the North.

In the case of diagonal motion due to having velocities in X and Y at the same time, it is critical which tile the cart actually tries to enter next. Only if the path into that tile is blocked by the corner branches will the cart take the corner and rewrite its velocity, otherwise it leaves the corner tile without changes to its motion. If the cart is redirected by the corner, all sideways velocity is lost, as forwards velocity *overwrites* sideways velocity in a curve. If, in that example in the paragraph above, the cart entered at -50k X sub-tile position with 30k X velocity, and 40k Y sub-tile position and -1k Y velocity, it would take that "curve" (or rather, redirection of velocity) on the fourth turn, while it is at 37k Y sub-tile position to start with, and then move to -53k Y sub-tile position at the end of that tick. It would then move to -26k Y sub-tile position in the following turn, and take 3 turns to clear the tile.

But, most importantly, it would be centered in the X sub-tile position, and all sideways velocity is safely removed.

There are two common ways to gain sideways velocity: Rollers facing perpendicular to the cart's travel path (which, as covered above, are almost always a bad idea, as it is easier to push *against* the travel direction of a cart into a curve, which redirects all velocity in the new direction,) and corner ramps, and require a curved track to compensate for sideways velocity within a few tiles.

### Track Direction Irrelevance

Carts that are traveling independently (that is, not guided) only care that tracks *are* on the tile, not which direction the tracks actually move. Tracks respect only curves (with two exits) and ramps.

This means, for example, that the following tracks, when a (non-guided) cart travels from West-to-East, are functionally identical in effect:

This is because so far as the cart is concerned, only valid ramps and curves with two exits where there is no exit in the path they are traveling matters.

Hence, if a minecart encounters the end of the track or a T junction with no "exit" in its movement direction, it will simply leave the track and continue on its course in a straight line until it encounters an obstacle, slows to a stop, or encounters another track even if the tile at which it joins the new track instantly sends it around a corner.

In fact, in a track designed for pushes or rides, a "║", a "╦", a "╬", and a "╥" are *only different in appearance*, and are ignored by an unguided cart, which will continue in its current direction, regardless of the track. For any purpose but guided tracks, *only curves and ramps matter at all*.

Tracks like T-junctions, however, *are* respected by dwarves guiding carts, who will lift and carry carts if they cannot find a valid track to their destination, and can choose to follow any orthogonal direction at a four-way junction in much the same way as they normally pathfind. What this functionally means is that T and four-way junctions *only guide dwarves hauling a cart, not carts, themselves*.

Carts only check for curves when they are halfway through a tile. When they get there, they look to see if their path has no exit. (That is, if it is traveling East, it checks if there is an East exit.) If there is, it ignores all other track directions, and keeps traveling. If there is not, it checks to see if there are only two exits to the track, and if one of those directions was the direction it "came from". (That is, if traveling West from the East, it checks if there is a valid exit to the West, and if not, if there is an East exit and EITHER a North or South exit.) If there is not, it ignores the track anyway, and keeps on traveling as though it were still on track.

If there is a curve the cart will respect, it checks for derailment. Carts derail if their speed is higher than 50k. Carts at this critical speed will then check for blockages of their forward path. If there is an obstacle to their path, which may be a wall or even furniture or buildings like a door, they will not derail and respect the curve, anyway. Derailing carts do not "jump" unless they hit completely untracked tile or an invalid ramp, but simply ignore the layout of the tracks entirely. With invalid ramps, this means not respecting the ramp, and likely results in collision with a wall, zeroing of all velocity, and a cart that requires manual retrieval.

If the cart is traveling at a speed that will not derail, or is forced to turn by a supporting wall, it will subtract 1000 from the "forwards" velocity of the cart, and redirect all forward velocity to the direction of the curve. This change in the direction of velocity *overwrites* any "diagonal" velocity, which can prevent diagonal velocity derailments, but any perpendicular velocity is not preserved, and is instead discarded.

### Valid and Invalid Ramps

Ramps are functionally defined for cart purposes as being a tile which exerts an acceleration force upon its "downward slope", and which allows connection to tracks a z-level above or below. This downward slope requires a cart to have at least one track branch touching a wall tile and one *and exactly one* carved exit to the tile that is the "bottom" of the ramp. Ramps accelerate carts in this "downward" direction (possibly leading to diagonal movement), and the deceleration of an "uphill" ramp is actually just the acceleration being applied against the direction of a cart's movement.

This is where players can find an exploit in the behavior of ramps - if there are *two* "downhill" exits to a ramp (such as a "T junction" on a ramp where only one exit faces a wall), then the ramp provides no acceleration *or* deceleration, allowing carts to travel up ramps without any loss of momentum except for the standard "flat track" deceleration, because as far as the cart is concerned, the track *is* flat. (A T junction is also not a curve, so the track is considered flat and straight no matter what direction the cart is traveling.)

Similar effects can be achieved when there are *no* "downhill" exits to a ramp. This may be the case if you have, for example, an East-West track with a one-tile channel with a ramp in it. The cart will travel through the "dip" with no change in velocity. It can also be the case if you abuse the Track Direction Irrelevance, and set only exits *up* the ramp, and none leading *down* the ramp. For example, if a cart is traveling from West to East up a slope, only carving East exits on each tile of ramp will make the cart travel up the ramp, and then recognize the tile it is on as being a "flat" tile, thus ignoring any deceleration from traveling uphill.

---
⚠️ Conteúdo truncado (68572 bytes = ~17143 tokens). Para o artigo completo, visite [Minecart](https://dwarffortresswiki.org/index.php/Minecart).