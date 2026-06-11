# Minecart

> Fonte: [Minecart](https://dwarffortresswiki.org/index.php/Minecart) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

A **minecart** is a tool intended for hauling. It can be made of wood at a carpenter's workshop or 2 bars of metal at a metalsmith's forge (using the blacksmithing labor.) Minecarts store up to five times as many items as wheelbarrows and are quite a bit faster than dwarves hauling objects by hand, but have the disadvantages of requiring a dedicated track network, a complex route planning phase, and the possibility of dwarves blundering into the path of carts filled with lead ore. Tracks may be carved into stone, or constructed; the latter allows above-ground routes, but these are more difficult to set up due to their additional material requirements.

Just like wheelbarrows, minecarts are considered items and are stored in a furniture stockpile. Despite their five-times-greater capacity, they are only 33% larger than wheelbarrows (minecarts have a size of 40,000 cm³) and are identical in base value when made from the same material (the value may differ due to the item quality). Thieves or even mischievous animals can steal minecarts, even when they are moving on a track.[1] However, minecarts moving fast enough or being ridden cannot be stolen.

The invention of minecarts revolutionized the Science of Dwarfputing by enabling smaller, faster logic systems to be built.

## Basic Minecart Usage

Minecarts

Minecarts can be used to swiftly transport dwarves, fluids, and/or large amounts of items, but before you have a functional minecart, there are several preconditions that need to be met. First of all, you need an actual minecart, constructed either in a carpenter's workshop or metalsmith's forge. For the minecart to be able to move, you also need to carve (with vt) or construct (with bnk) a track, which could be as simple as a straight line. Finally, you need to construct stops on your track (with bnK) where the minecart will start and stop.

After you have created the stops and assigned a cart to the track, you must create logic routes connecting several stops and designate starting conditions for each stop by selecting the stops for the minecart, take note to designate the tiles where your minecart will physically stop. This is done with the h hauling key. The most basic conditions are how the cart's movement is initiated and in which direction the cart should start moving. Carts can be either pushed (a dwarf stands at a stop and gives the cart a single push) or guided (a dwarf continually pushes the cart forward, guiding it along the track). The hauling labor required for pushing and guiding carts is called "Push/Haul Vehicles" and is turned on by default.

To control which items are to be transported, you can add conditions specifying: (1) which kind of items are to be loaded and unloaded, (2) stockpile links to define which stockpile(s) the items should be un/loaded to and from.

### Capacity and weights

Minecarts have a capacity of 500,000 cm³ – five times the capacity of wheelbarrows.

**Examples\* of the capacity of one cart**

|  |  |
|----|----|
| Item | \# of / items |
| stone | 5 |
| log | 10 |
| block/bar | 83 |
| minecarts | 12 |
| prepared meals | 500 |
| spiked balls | 500 |
| Sand bags | 500 |
| mace | 625 |
| spears | 1250 |
| cloth | 2500 |

*(\* See Size#Items for a more complete list of item sizes, and use the formula {500,000 ÷ (item size)}, dropping all fractions, to determine a minecart's capacity for that item.*

*Example: A door is listed at a volume of "30,000". 500,000 ÷ 30,000 = 16.666, so a minecart can hold 16 doors, plus some smaller object(s) equal to or less than .667 (2/3) of a door, or 20,000.)*

The total weight of the loaded minecart does not affect the initial velocity received from pushing or launching from a roller.Bug:6296 However, the load of a minecart *does* affect whether a pressure plate triggers or not, based on the pressure plate's setting and the *total* weight of the 'cart.

**Weights of different carts**

|                   |            |                              |
|-------------------|------------|------------------------------|
| Type of cart      | Empty cart | Fully loaded (items)         |
| oaken minecart    | 28Γ        | 378Γ (10 oak logs)           |
| iron minecart     | 314Γ       | 1698Γ (83 marble blocks)     |
| copper minecart   | 357Γ       | 1682Γ (10 obsidian boulders) |
| platinum minecart | 856Γ       | 10482Γ (83 gold bars)        |

\
The weight of a minecart is one twenty-fifth (1/25) the density of its material in Urists. Because pressure plates can be set to trigger at intervals of 50 Urists, minecarts with weights just under a multiple of 50 are ideal for switching based on whether they're full or empty. The best minecart materials for full/empty switching are as follows:

|  |  |  |  |
|----|----|----|----|
| Material | Minecart weight | Content weight required to trigger | Banana roasts required to trigger (for scale) |
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

A dwarf riding a minecart from a higher level.

Minecart tracks are made up of contiguous track, tracked ramp, or bridge tiles. Track tiles and tracked ramp tiles have a direction or series of directions associated with them. These directions dictate which directions a minecart on a given tile may move from that tile. For example, a Track NE (northeast) tile allows a minecart on it to move either north or east from its present position. Therefore, if you want your minecart to move east along a straight piece of track, then return west using that same track, you would need to use EW tracks so that the cart could travel east initially, then return west over the same track. Excluding designs in which the cart will "jump" tracks via a drop or other ramp, tracks must be valid end to end to work for most looped or straight-track applications. A single east only track tile in your line of east-west tracks will cause any route using the track to fail the moment it tries to go the wrong way over that tile. Minecart tracks can be built in two ways: carved or constructed. A given minecart track need not use carved or constructed elements exclusively, as the two methods can be used interchangeably depending on the needs of a given section of track. The way the tracks are built is slightly different between the two, as explained below.

#### Simple tracks

**Carved**

A single-tile wide strip of natural stone can be designated to be carved (with vt), which will create a straight two-way track. The creation of corners, crossings, and T-junctions is as simple as designating another strip of track that overlaps an existent or newly designated track. Carved tracks are removed by smoothing the rock they're on, which results in a smooth floor (that can be re-carved if necessary), or by building a floor on top and subsequently removing it. Dwarves can carve corner tracks in one pass by designating the track carving twice and canceling unwanted carvings (with x). Tracks can be carved in any natural floor tile, rough, smooth and even over engravings, providing an easy method to remove low-quality or undesired floor engravings. Once a track has been carved, it's important to check the track directions for each tile in the route carefully to make sure no mistakes were made by yourself or the game's track carving logic.

**Constructed**

Tracks can also be built as regular constructions (through bnk. This method is resource-expensive, since each track tile requires one stone, bar, or block for construction. Corners, crossings, T-junctions, and ramps also have to be designated individually. However, it is usually the only way to build tracks above ground or on soil (barring the creation of obsidian). Constructed tracks are designated for removal like any regular construction; be aware that removing track ramps built on top of natural ones will also remove the original ramp, leaving a flat floor.

#### Ramps

**Carved**

The carving of natural ramps is a little more confusing: to carve a two-way track on a ramp (natural only, does not work on constructed ramps), you must designate the track **starting on the ramp and one square beyond** in the direction you want the track to go. For the side of the ramp square you want to head upward, there **must** be either a natural or constructed wall in the square next to it, otherwise the game assumes you are trying to carve it on the same level – this can result in the track being carved underneath a door or other object. If you have accidentally done this, you can correct it by smoothing the ramp and constructing a single square of wall next to it, then re-carving the ramp correctly, however, the wall must stay there permanently — removing it will disconnect the track.

**Constructed**

The track and ramp must be constructed first as a constructed Ramp, and then as a Track from the construct track menu (bnk). When constructing track ramps, the stated direction should be the same as the connected tracks. For example, a track going up from West to East would require, starting from the West, a Track (EW), a Track/Ramp (EW) and a Wall behind the ramp, underneath the section of track above it. Incorrectly placed ramps result in minecarts ignoring the ramp and crashing into the supporting wall. They will not, however, display as unusable as when the supporting wall is missing.

**Examples of ramps**

A simple ramp would look like this:

|     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     | z   |     | \+  | 0   |     |     |     | z   |     | \+  | 1   |
|     | ░   | ░   | ░   | ░   |     |     |     | ░   | ░   | ░   | ░   |
|     | ═   | ▲   | o   |     |     |     |     | ░   | ▼   | ═   |     |
|     | ░   | ░   | ░   | ░   |     |     |     | ░   | ░   | ░   | ░   |
| o   |     | :   |     | w   | a   | l   | l   |     |     |     |     |

Carving track corners into ramps is rather unintuitive and complicated. Since carving tracks always requires two tiles to connect in a straight line as input, you have to give two separate designations for a single job: a track bit from the ramp tile to the "below" direction and another one to the wall of the "upward" direction. If you wanted to change direction on a ramp from east to north:

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     | z   |     | \+  | 0   |     |     |     |     | z   |     | \+  | 1   |     |     |
|     | ░   | ░   | ░   | ░   | ░   |     |     |     | ░   | ░   | ░   | ░   | ░   |     |
|     | ░   | ░   | ░   | ░   | ░   |     |     |     | ═   | ═   | ╗   | ░   | ░   |     |
|     | ═   | ═   | ▲   | ░   | ░   |     |     |     | ░   | ░   | ▼   | ░   | ░   |     |
|     | ░   | ░   | ░   | ░   | ░   |     |     |     | ░   | ░   | ░   | ░   | ░   |     |

you would need to connect the ramp on z +0 both to the west and to the north by issuing two "carve track" commands, one selecting the ramp and the track tile to the west, and another connecting the ramp tile with the wall to the north. A stonecutter would then carve a NW track corner into the ramp, allowing carts to pass the corner correctly both going up and down. Such track corners are perfectly serviceable for guided carts, but moving down a route of several of them by pushed or ridden cart is problematic - ramps on corners behave very counter-intuitively, resulting in loss of speed when going down and diagonal movement when going up.

Moving to and from ramps (or between ramps "pointing" in different directions) causes some non-trivial adjustments to speed and even moving along the tiles at a fixed speed *unrelated to the entry/exit velocity values*, because transitions to/from ramps are processed differently and are not to be "skipped". This affects compact track/ramp combinations (such as e.g. a simple 2x2 ramp spiral) most, and combined with bouncing often makes them work not in the way one could expect. [2]

### Hauling route

A hauling route is a list of directions describing how and under what conditions a minecart will move. The proper setting up of routes is essential for a working rail system. Routes, stops, departure conditions and stockpile links are managed from the h hauling menu.

#### Route

A route defines the path a minecart will take along a track, as well as under what conditions it will move or stop moving. A route is made up of stops. Stops are precisely what they sound like, a position on the track at which you want a minecart to stop. A minecart track might use as little as a single stop for a looped track, which will serve as both a starting and stopping point for the cart, or it could contain many stops, perhaps to load supplies or wait for a bridge to be manually lowered, before reaching its destination or returning to its starting point. It is important to note that you only need to place stops on a route where you actually want the cart to stop and wait for some action to occur. They are not needed to help navigate the cart along the track beyond telling it where on the track to stop.

New routes are created with the h hauling key. Existing ones can be removed (without confirmation), and also nicknamed (). Before operating, the route must have a vehicle assigned () to it (this can be done with either the route or a stop selected). Assigning a full minecart to a route may result in a slow hauling job if the contents are heavy.

#### Stops

Stops are the individual waypoints that make up a hauling route. A given stop consists of the location of a tile, as well as conditions describing when, where, and how a cart should be moved after being stopped at that tile. Stops can be created from within the h hauling menu, by placing the cursor over a tile and hitting  while highlighting the route (or a stop within) you've already designated. A minecart will begin its route at the first stop created, and continue through each subsequent stop, being guided, pushed, or ridden from each stop to the next depending on the conditions specified. In many basic minecart applications, the cart will end up at the same stop it began at, though this is not always the case. It is important to note that hauling stop order is enforced, even if there is no track. A dwarf will drag the cart overland back to a skipped stop in the route's list if your tracks bypass it somehow, including if the minecart does not stop on the stop after it is pushed/ridden.

Once a stop has been placed, it is given a default set of conditions under which to move the minecart if it is stopped there. Each new stop gets the same default conditions regardless of the track it is placed upon (e.g. guide the cart to the north). For this reason new stops might get marked by yellow exclamation marks (!) due to invalid directions. One important thing to note is that as you place additional stops, the display will show paths between the stops you have defined. However, this is **not** necessarily the actual route the minecart will take once the route is in operation. For example, if a route were defined with two stops at opposite ends of a track with many twists and turns, a line will be drawn directly between those stops to show the order in which they will be visited. These route lines may crisscross all over the tracks, but so long as the track is valid end to end, the cart will follow the track from one stop to the next, even across twists, turns, and z-level changes. Route stops, which are the steps that make up a route, should not be confused with physical Track Stops, described below.

Note that setting a stop on a sloped track may cause the minecart to roll away, preventing it from being properly loaded.

##### Stockpile links

By placing the cursor on top of a stockpile and using s, you can create stockpile links while defining a hauling stop. Links can also be redefined by selecting them, placing the cursor over a different stockpile, and pressing p. The cart will then be filled by items present in its various linked stockpiles in preference to other items. Note that bins should be used with caution in stockpiles that are linked to minecarts. Bins cause problems when used with the "Desired Items" list in a stop's conditions. For example, if a minecart is set to accept only granite blocks, and to depart north when it is 100% full of granite blocks, it will not depart if any of those granite blocks are in bins, even if bins are also included in the desired items list. Two solutions to this problem exist as of v0.40.24. First, bins can be disallowed in stockpiles that are linked to stops. Alternatively, bins **can** be used in conjunction with minecarts provided that the minecart's departure conditions use only "any items" instead of "desired items." This option can be toggled in the advanced conditions menu for a stop, accessible via the C key. The cart's contents can still be controlled by specifying what items are allowed in the linked stockpile.

##### Departure condition

Departure conditions involve setting conditions in which the minecart will leave on the route. Each condition includes:

1.  A departure mode (Guide, Ride or Push).
2.  An initial departure direction (NSEW). Note that this defines the initial direction of movement only. Even if a track includes many turns, as long as the initial movement direction is valid the cart will follow the minecart track thereafter.
3.  A timer, before which the departure condition cannot be met.
4.  Conditions on the amount of items in the cart.

Departure conditions are created with the n key. A new departure condition will read: "guide north immediately when empty of desired items". This condition can be changed between basic presets with c. "Advanced" mode (C) allows for more precise control over departure conditions: fine tuning the percentage from 0 to 100 in 25% steps (f and F), switching it being either the maximum or the minimum amount of items for the condition to be met (m), and whether the cart accepts all or only a specific set of items (l). Common to both screens are the departure mode (p, Push, Ride or Guide), direction, and timer (t and T) options.

To have a cart only carry a specific set of items, the stop can be set to only carry "desired" items, opening the selection screen with the Enter key while having said stop condition selected, and toggling as desired, or it can simply be linked to a stockpile and set to depart once it is full of items from its linked stockpiles, regardless of type.

### Track Stops

A Track Stop, not to be confused with a route stop, is an optional, single-tile construction which serves two purposes. First, it can be used to cancel a cart's momentum in order to slow or stop it as it passes over the Track Stop. This might be necessary if a cart were pushed down a series of ramps to its destination. Second, a Track Stop can cause a cart to automatically dump its contents as it passes over the Track Stop. Track Stops are constructed via bnK, and must be constructed atop an existing piece of track. If a Track Stop has been set to automatically dump a cart's contents, the cart will dump its contents in the direction indicated when it passes over the Track Stop. Depending on the friction settings chosen for the Track Stop, the cart might then stop after dumping, or it might continue on its route to another destination.

Track Stops are not mandatory; in fact, their main use is in automated rail systems. However, even in basic rail systems it can be useful to set a Track Stop to dump items: this saves time that dwarves would otherwise spend in removing items from the cart, time that is better spent driving the cart back to where it's needed. Dumping will occur even with a guided cart. **Take care not to set Track Stops at a loading site to dump their contents**, or dwarves will never be able to fill the cart. It will dump any contents the moment they are loaded.

Track Stops are constructed using the Mechanic labor.

- See More on Track Stops

### Step-by-step tutorial

Let's construct a simple minecart route. This route will move stone blocks from an input stockpile to an output stockpile. We'll begin by creating the stockpiles:

The input stockpile is on the left; the output stockpile is on the right. We'll be moving blocks from left to right. Disable bins in both stockpiles, and set the input stockpile to accept only from links. Then make the stockpile take from the mason's workshop where the blocks are being produced.

Next, carve the track:

Note that the ends of the designation are uniquely shaped; this is automatic, and not anything you need to control. Now, wait for your stonecutters to come along and carve the track into the stone. (Your haulers will probably also fill up the input stockpile while you wait.)

In addition, while we're waiting for that to happen, we'll build an iron minecart in the forge.

When the track has been carved, it will look like the above (the track will be solid instead of flashing). Now, order a track stop to be constructed (Under "Constructions") next to the output stockpile:

|  |  |
|----|----|
|  |  |

You must select the dumping direction *before* placing the track stop. We want our blocks to be dumped into the output stockpile east of the track stop. Then wait for a mechanic to come along and build the track stop.

Now we'll define the actual *route*. This is done in the Hauling menu. Press 'Add New Route' to begin defining a route. Select 'Add a stop' then click the track next to the input stockpile:

|  |  |
|----|----|
|  |  |

Select 'Add a stop' again then click the stop next to the output stockpile define the second stop:

|  |  |
|----|----|
|  |  |

At this point, the route has been positioned, but they haven't been *defined* yet.

Click the Minecart icon for the route (not the stop) and assign a minecart to the route.

Select the minecart icon for the first stop to select what items will be hauled to the minecart. By default no items will be hauled to the minecart. As we've set the input stockpile to only take blocks from the workshop, you can either set to to accept blocks, or set it to accept all items.

Click the stockpile icon for the first stop, select the "take from" icon (middle button) and select the input stockpile.

Select the Conditions button (**\=≠**) for the first stop and check out the defaults. For the first stop, these are largely fine however you should change the direction button for all the conditions so the minecart goes the correct direction when it's ready.

Select Conditions for the second stop. These need to be changed so the minecart is returned to the start immediately. Erase the bottom two conditions, change the direction to point back to the stop, and then finally click the **\>=** button so it changes to **\<=**. This will make it so the cart is returned regardless of how full it is (which is good, as it'll always be empty!)

Once the minecart is in place, dwarves should fill it with blocks from the input stockpile, which will in turn be filled with blocks from the workshop where your mason has been toiling dutifully. When the minecart is full, the blocks will be dumped into the 1x1 stockpile on the right. Automatic quantum dumping!

If the route has any issues, you'll see a red ! on the minecart in the route screen. Be aware that this appears initially until the minecart is put in place. If your route is correctly set up, your dwarves carry items to the cart and the percentage will change on the route screen.

|                      |                                   |
|----------------------|-----------------------------------|
| Route with an issue. | Cart correctly getting filled up. |

### Troubleshooting

Because of the complexity of the system, all but the most careful and experienced minecart users will encounter issues. Most route issues can be diagnosed and fixed from the Hauling menu.

**Symptom:** ! Set dir/connect track message appears to the right of one or more stops

Possible Causes

- Game cannot find a path for *guiding* the cart without carrying. The game checks for haul route validity assuming the cart will be guided. This warning will be shown when the path crosses impassable tiles, requires a dwarf to carry the cart, or is not fully guidable.
  - If your cart path relies upon advanced tricks like deliberate falling into pits or ignoring floor types, even a path designed entirely as you intended will still trigger the yellow warning. If the route is working as intended, you can safely ignore this warning.
- Invalid departure direction in one or more conditions for the stop. Edit the stop using Enter and pressd until it is pointing in a valid direction.
- Track stop built on trackless tile. Track stops must be built on tiles where tracks already exist to be usable.
- Discontinuous track. If the route indicator seems to draw between your first and last stop, this is the cause. Make sure destinations are linked by track to both directions, and that there are no sneaky gaps in the tracks.
  - *Ramps'* are notorious for their finicky use. It is recommended to check every ramp to confirm no unintended one-way ramps remain.
  - To carve a two-way track on a (natural) ramp, you must designate the ramp *and one square beyond* in the direction you want the track to go.
  - Ramps **must** have a solid wall on the side opposite to the track ("behind" the ramp), or they will neither work nor be marked as "unusable". The wall can be natural or constructed.
- Discrepancies in desired/kept item configurations.

**Symptom:** The status **0% V** always appears to the right of one stop.

Possible Causes

- Stop not set to take from a stockpile. Edit the Stop using Enter and make sure you see a message like "Take from Stockpile \#1".
- Take conditions and stockpile contents do not overlap.
- Track stop is set to dump. A track stop set to dump cannot be filled. You must either set the stop to a time-based departure or deconstruct the track stop and rebuild it without dumping. (Alternatively, with DFHack you can modify "Dump on arrival" to "No" using the q menu without rebuilding the stop.)
- Minecart itself is designated to be dumped (such as when using mass-dump).

**Symptom:** Dwarves fill the minecart properly, but will not move it thereafter.

Possible Causes

- Minecart contains items not listed as desired on its current stop. Check minecart contents using the k and z keys and ensure that all items in the cart are desired items.
- Minecart contain desired items *in bins*. Minecarts seem to have problems realizing that they are in fact full of desired items if some of those items are in bins, even if bins are also among the desired items for that stop. **This cannot be solved by adding the appropriate bins to the stop's desired items.** Either disallow bins in stockpiles you intend to load minecarts from, or set the departure conditions to rely only on percentage of total load rather than percentage of desired items using the advanced conditions menu (C key).

**Symptom:** Dwarves repeatedly attempt to load the minecart, but no items are ever loaded into it.

Possible Causes

- Track Stop set to dump used as a loading site. Every time a dwarf places an item into a cart resting on such a track stop, the item will be immediately dumped, causing unlimited, useless cart loading jobs. Autodumping Track Stops should never be used at a loading site.

**Symptom:** A dwarf picks up the minecart and carries it to its destination.

- See Quirks

### Danger

Minecarts are not without ~~danger~~ fun. Although designating a track automatically sets the traffic designation to low, dwarves *may* still walk on them, and creatures ignore traffic designations altogether. If an unlucky dwarf or creature fails to dodge a minecart, they can be injured. Most of this danger can be avoided by setting the minecart hauling commands to guide instead of push or ride (dwarves guiding minecarts will ignore traffic restrictions), as well as by pasturing domestic animals and preventing the access of other creatures to the tracks. Note that removing the track doesn't reset that tile back to normal traffic priority, so you may wish to manually clean up traffic designation afterward. Also note that bridges that are used as tracks don't have their traffic priority changed automatically (since they're just normal bridges), which could cause dwarves to pathfind normally through dangerous minecart entrances in your fort's walls if you're not careful.

The only ~~fool~~*dwarf*-proof method is to make the tracks inaccessible. There are several ways to create a track which works for minecarts but doesn't allow creature-traversal; the simplest is perhaps building a statue on the tracks. Other options include adding single-tile holes (minecarts moving at reasonable speed will jump the gap), vertical drops, minecart-triggered doors, small pools of liquid (4/7 water or 2/7 magma), and hostile creatures overlooking the tracks. For safety, both ends of the track should be isolated, making the dangerous center sections completely inaccessible (though maintenance access can be provided by a locked door).

Danger does not always involve living victims: careless route designation can also result in minecarts careening off tracks or colliding with each other. If this occurs, the items may be scattered; this can cause even more hauling jobs than the minecart aimed to eliminate. Even ~~better~~ worse, scattered items, especially weapons, can injure passing dwarves or other creatures; in the words of Toady One the Great, "Accidental grapeshotting of the dining room should be possible now."

Of course, the danger of using minecarts means they can also be used as weapons by imaginative players.

## Advanced usage and automation

Minecart-specific effects are implemented via track stops, rollers and pressure plates with "track" condition set. Since all three are considered buildings, they can't be built on the same square (however convenient track stop + pressure plate would be) nor a simple ramp, and are removed separately.

### More on Track stop

Track stops are constructions that allow further automation of minecart systems via adjustable features such as braking by friction and automatic dumping of contents. They can be built from logs, bars and blocks through bnK; friction amount, dumping toggle and dumping direction must be set **before** construction, and these settings can be neither changed nor seen thereafter; however, track stops can be linked to pressure plates or levers to toggle friction and dumping On or Off (trigger state is inverted: switch On = track stop Off). In thoughts screen, dwarves will admire track stops as traps.

If a stockpile is placed on the tile that a track stop is set to dump to, it can act as a quantum stockpile and any items dumped from a minecart that match the storage settings of the stockpile will remain there and accumulate. Normally track stops are built on top of existing track to operate on moving minecarts, but they can also be used without tracks to create automatic quantum stockpiles (see also step-by-step tutorial). It is not always desirable to collect ALL of certain items into one quantum stockpile, such as when distributing a material to multiple separate industries. You can link your quantum stockpile to various other stockpiles, ensuring that your dwarves will keep them supplied as necessary. Because quantum stockpiles never fill up like regular stockpiles, it may be a good idea to add a switch to turn them off.

Items dumped from a minecart at a track stop (or dumped by any other means) into open space fall through z-levels until they land on a solid surface. Items falling onto a designated stockpile will automatically be considered part of that stockpile, even if the stockpile is set to disallow those items (they will, however, be automatically moved to a more appropriate stockpile, if available). Items falling on top of a minecart will **not** fall "inside" the minecart. Use with caution; dwarves have fragile skulls.Bug:5945

### Automated propulsion

#### Roller

A **roller** is a powered machine component for the automated propulsion of minecarts. They are built over the top of existing tracks with bMr, requiring a mechanic, *(length/4)+1* mechanisms and a rope. Rollers may also be placed directly on ramps to help pull carts up Z levels. Rollers are very useful to maintain a cart's momentum along long routes, to get them to climb Z-levels without dwarfpower involved, and to get them to reach speeds unattainable by guiding dwarves. These devices are variable-length (1-10), variable-direction and variable-speed (see below), all traits that can be set at construction time; a roller uses two units of power per tile it is long.

Single-tile rollers transfer power in all four cardinal directions, while other rollers generally only transfer power perpendicular to their activity direction. Longer rollers can also transfer power along their activity direction if built in the correct order, although this can be hard to accomplish and is easily broken. Rollers cannot be powered from above.

Rollers have great acceleration and capped speed. Carts going faster than the roller are unaffected. If a cart moves across an active roller in the direction the roller works and moves slower than the roller's specified speed, the cart will be set to the roller's speed. A cart going against a roller's movement direction will be sent back the way it came (once again at the roller's speed), unless it was moving extremely fast: speed increment of 100000 allows to reverse carts from the full "highest" (50000) speed roller to full "highest" speed back, but ramps can accelerate a cart beyond this. [3] A cart crossing over a roller perpendicular to its current movement direction will gain the roller's amount of speed in the perpendicular direction without directly changing its forward motion. Without an adjacent wall to constrict its movement, this will typically send a cart off the rails on a diagonal path, completely unable to follow any tracks until it collides with a wall or is otherwise brought to rest. However, if the roller is placed over a track turn and pushes *from* the direction of that turn's track, the turn affects carts *after* the roller, so they will be forced into the turn rather than derailed in a diagonal direction. [3]

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| t | r | a | c | k | s | : |  | f | u | l | l | : |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ║ |  |  |  |  |  |  |  | ║ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | ═ | ╗ | ═ |  |  |  |  |  | ═ | ╢ | ═ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ║ |  |  |  |  |  |  |  | ║ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ╢ |  | : |  | r | o | l | l | e | r |  | p | u | s | h | i | n | g |  | f | r | o | m |  | W |  | t | o |  | E |

If the roller is powered, carts from *all* directions (unless too fast) exit S, because speed imparted by the roller forces carts toward E and *then* into the turn. If not powered, carts from W and N exit S, carts from E and S exit W. Carts above derail speed will ignore the turn, of course.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  | ║ |  |  |  |  |  | ║ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ═ | ╗ | ═ |  |  |  | ═ | ╟ | ═ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | ║ |  |  |  |  |  | ║ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ╟ |  | : |  | R | o | l | l | e | r |  | p | u | s | h | i | n | g |  | f | r | o | m |  | E |  | t | o |  | W |

Carts from the E or W: exit W. Carts from N: derailed diagonally, exit SW. Carts from S: derailed diagonally, exit NW.

Rollers affects carts on a track - if placed on a floor or ramp without any tracks, they are ignored. Depowered rollers are also ignored, friction is determined by the tiles underneath.

Because of their one-way nature, rollers are unsuitable for most two-way minecart tracks (unless you set gears toggling roller A-\>B off while toggling A\[4] — this allows a one-way track to be used in both directions. In addition, unpowered rollers do not affect minecarts.

Care must be taken in glaciers and other extremely cold biomes, since rollers (and the machinery used to power them) will not operate when constructed on natural ice floors.

\

#### Impulse ramps

Carts can be given momentum without rollers or changing z-level by exploiting a design oversight in a phenomenon called "**impulse ramps**". Ramps don't actually impart any downward velocity even when making carts descend; there is no basic "rolling downhill" acceleration effect. However, a track ramp which has at least one wall/fortification and exactly one other connection will *always* accelerate a cart towards the other connection, no matter where the cart enters the tile from. If a track ramp faces three directions such as ╩, then two of those directions need to be facing walls for the cart to be accelerated towards the remaining direction. This means carts can be accelerated even if the cart doesn't actually change z-level at all.

Example of straight impulse acceleration:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |  |  |  |  |  | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ | ▒ |  |  |  |
| ═ | ▲ | ▲ | ▲ | ▲ | ▲ | ▲ | ▲ | ▲ | ▲ | ▲ | ═ |  |  |  | ═ | ╚ | ╚ | ╚ | ╚ | ╚ | ╚ | ╚ | ╚ | ╚ | ╚ | ═ |  |
| ▒ |  |  |  | : |  | W | a | l | l |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  | ═ |  | : |  | N | o | r | m | a | l |  | t | r | a | c | k |  |  |  |  |  |  |  |  |  |  |
| ▲ | / | ╚ |  | : |  | N | / | E |  | T | r | a | c | k | / | R | a | m | p |  |  |  |  |  |  |  |  |

If a cart enters from the left, it will speed up on every track/ramp and exit to the right going very very fast—more than one tile every step. If it enters from the right, then it will bounce back impulsed by the ramp if it's going slow enough.

As another oddity, carts coming from ramps will in some cases "teleport" through most of the next tile. This is called the "checkpoint effect", and is explained in detail in the Physics section, below. This negates the deceleration of the next tile if it is a ramp "angled" in a different direction.

You can just make an upward spiral alternating impulse ramps and regular upward ramps. It takes no power, is quick and cheap to build, requiring only channeling and track carving, and the cart goes up fast, but not so fast that it launches its contents.

Examples of impulse elevators:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|  | z |  | \+ | 0 |  |  |  |  | z |  | \+ | 1 |  |  |  |  | z |  | \+ | 2 |  |  |  |  | z |  | \+ | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | ░ | ╔ | ░ | ░ | ░ |  |  |  | ░ | ▼ | ╚ | ╗ | ░ |  |  |  | ░ | ░ | ▼ | ▼ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | ░ | ╝ | ░ | ░ | ░ |  |  |  | ░ | ▼ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ╔ | ░ |  |  |  | ░ | ░ | ░ | ▼ | ░ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | ░ | ▼ | ▼ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ╝ | ░ |  |  |  | ░ | ╚ | ╗ | ▼ | ░ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | z |  | \+ | 0 |  |  |  | z |  | \+ | 1 |  |  |  | z |  | \+ | 2 |  |  |  | z |  | \+ | 3 |  |  |  | z |  | \+ | 4 |  |  |  | z |  | \+ | 5 |  |  |  | z |  | \+ | 6 |  |  |  | z |  | \+ | 7 |  |  |  | z |  | \+ | 8 |  |  |  | z |  | \+ | 9 |  |
|  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |
|  | ░ | ▼ | ░ | ░ |  |  |  | ░ | ░ | ╗ | ░ |  |  |  | ░ | ╔ | ▼ | ░ |  |  |  | ░ | ▼ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ╔ | ╝ | ░ |  |  |  | ░ | ▼ | ▼ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ╗ | ░ |  |  |  | ░ | ╔ | ▼ | ░ |  |
|  | ░ | ╔ | ╝ | ░ |  |  |  | ░ | ▼ | ▼ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ╚ | ░ | ░ |  |  |  | ░ | ▼ | ╝ | ░ |  |  |  | ░ | ░ | ▼ | ░ |  |  |  | ░ | ╚ | ░ | ░ |  |  |  | ░ | ▼ | ╝ | ░ |  |  |  | ░ | ░ | ▼ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |
|  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ░ |  | : |  | W | a | l | l |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ╔ | , | ╚ | , | ╗ | , | ╝ |  | : |  | T | r | a | c | k | / | R | a | m | p |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ▼ |  | : |  | D | o | w | n |  | R | a | m | p |  | ( | e | m | p | t | y |  | s | p | a | c | e | ) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Note that these impulse elevators, due to the checkpoint effect and upward curved ramp effect, will not actually result in carts traveling straight up the ramp. They will lose speed, bounce off a ramp, then be accelerated back into the spiral after a 9-turn delay on both tiles on the floor where they are stopped. This is because the checkpoint effect allows carts to travel up the ramps in a single turn, but also prevents the impulse ramps from adding acceleration unless the cart is slowed to staying on the ramp for more than one turn. Initial acceleration will carry the cart up a variable number of floors before this effect occurs, but this bouncing back and forth will occur every 5 z-levels after the first time the cart stops. When the cart *is* traveling upwards, it will pass every tile at a rate of one tile per turn regardless of its actual speed, due to the checkpoint effect. In tracks with only a single cart, this is negligible, but when multiple carts are on the same track (such as when you place multiple carts on a magma cart lift) this can cause collisions which derail carts, or cause other unexpected or undesired behaviors.

The following impulse ramp (while larger) should alleviate these problems by using a straight ramp to go upwards, preceded by an impulse ramp to exploit the checkpoint effect and negate up ramp costs. Corners still decelerate carts, so the cart will tend towards a velocity of 72k, which is above derail speed. Derail speed breaks (see Controlling Speed, below) may be necessary at the top.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| z |  | \+ | 0 |  |  |  |  |  | z |  | \+ | 1 |  |  |  |  |  | z |  | \+ | 2 |  |  |  |  |  | z |  | \+ | 3 |  |  |  |
|  | ░ | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ | ░ |
|  | ░ | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ╔ | ╔ | ═ | ░ | ░ |  |  |  | ░ | ░ | ▼ | ▼ | ╗ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ | ░ |
|  | ░ | ║ | ░ | ░ | ░ | ░ |  |  |  | ░ | ▼ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ╗ | ░ |  |  |  | ░ | ░ | ░ | ░ | ▼ | ░ |
|  | ░ | ╚ | ░ | ░ | ░ | ░ |  |  |  | ░ | ▼ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ║ | ░ |  |  |  | ░ | ░ | ░ | ░ | ▼ | ░ |
|  | ░ | ╚ | ▼ | ▼ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ═ | ╝ | ╝ | ░ |
|  | ░ | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ | ░ |  |  |  | ░ | ░ | ░ | ░ | ░ | ░ |

---
*Parte 1 de 3 de «Minecart». Demais partes em arquivos `...-part-{1..3}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Minecart*
