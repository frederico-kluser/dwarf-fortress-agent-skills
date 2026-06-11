# Stockpile design

> Fonte: [Stockpile design](https://dwarffortresswiki.org/index.php/Stockpile_design) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Production flowchart for most workshops**.\
Not all items are represented!\
*(Click to enlarge)*

Stockpiles can be created almost anywhere, can have almost any size, and have many different options. Choosing where to place them, how big to make them, and how to configure their settings constitutes the art of **stockpile design**. Efficient stockpile design is one of the most critical aspects of overall fortress efficiency. Stockpile and workflow design is, perhaps, the third most important thing you need to do in your fortress, after keeping dwarves fed and protected. A fortress with poor stockpile layouts will grind to an FPS death much faster than one designed with efficiency in mind.

## Avoiding hauling-caused job cancellations

One of the major problems you will face in a fortress with inefficient stockpile design is the endless "spam" of job cancellations due to items being hauled. While an item is being hauled, *or is inside a container which is tasked for hauling*, it can't be used. If a hauling job takes a month, then all the items involved in that job are unavailable for an entire month.

The solution to this issue is to minimize the amount of time a container full of items spends being hauled, either by avoiding the use of containers altogether, or by minimizing the distance a container will travel.

The classic example of this problem is the seed stockpile. Your planters need seeds to sow crops in farm plots. Seeds are stored in food stockpiles, in bags; the bags in turn will be stored in barrels or large pots if you allow it, and if enough empty barrels/pots are available. If you simply create a food stockpile next to the farm, and disable everything except seeds, the default settings will allow the use of barrels to store the seed bags. This will lead to job cancellations. Let's take a closer look at why this happens.

In the "stockpile at rest" (when no new seeds have been generated in a long time), we will most likely have 1 or 2 barrels full of seed bags, plus one empty barrel. (All barrel- and bin-using stockpiles try to keep one empty container for future use.) The barrels can hold a huge number of seed bags, so there will be a small number of very full barrels.

Now, suppose some dwarf eats a plump helmet and generates a plump helmet spawn. The stockpile will eventually realize this has occurred, and will generate a job to acquire the seed. If there is already a bag of plump helmet spawn in the stockpile, then the job will be "Store Item in Bag". Some dwarf will be assigned to take the bag of plump helmet spawn *out* of the stockpile, bring it to the dining room where the seed is, and put the seed into the bag. However, as soon as this job has been **created**, the bag is marked as being part of the hauling job. All the seeds in it are now unavailable for use -- and the dwarf hasn't even picked it up yet!

But it gets worse. Once the bag has been taken to the dining room and has acquired one (or possibly several) new seeds, the stockpile will generate another job to bring the bag back. Since there is a non-full barrel already in the stockpile, the job will be "Store Item in Barrel". Some dwarf will be assigned to take the barrel *out* of the stockpile, drag it to the dining room where the bag is, and put the bag into the barrel. As soon as this job is created, the **whole barrel full of seed bags** (which may be every seed in the entire fortress) is marked for hauling and is unavailable for any other purpose, including planting crops. The planter can't use any of those seeds until the barrel has been dragged out, and then finally dragged back to the original stockpile. And if any new seeds have been generated while that's going on, then the cycle never ends.

There are a few designs that try to mitigate this problem. The simplest design is to **disallow barrels** in the seed stockpile. Seeds will continue to be stored in bags (you cannot stop this by any means, if empty, unforbidden bags exist). You will continue to get some planting job cancellations when a bag is removed to pick up new seeds, but it is nowhere near as bad as the situation you get with barrels.

## Multiple stockpile designs

### Double stockpile

Another design that works well for seeds uses two stockpiles. The first stockpile is set to "take from anywhere", and disallows barrels. This stockpile is typically quite small, because it only holds items temporarily. The second stockpile is set to "take from links only", and is linked to take from the first stockpile (and the two stockpiles are extremely close together). This second stockpile may permit barrels. This design gives you the increased storage capacity of the stockpile with containers (for long term storage), while minimizing the amount of the time the barrels spend out of their stockpile. Rather than being dragged all the way from the seed stockpile to the dining room (or still, or farmer's workshop, etc.) the barrel only has to move a few tiles to the neighboring stockpile.

Neither of these designs will completely eliminate job cancellations, but they reduce the spam (and the time a planter spends waiting for seeds) immensely.

The double-stockpile design is also particularly good for heavy items, like armor. An armor stockpile that accepts items from anywhere and permits bins will cause dwarves to drag bins full of metal armor all the way down to the forges and back. If you're using magma forges a hundred levels down, along corridors that have to twist around caverns, such a trip can take literally weeks. The armor in that bin is unavailable for that entire time. But if you make a small "feeder" stockpile with no bins that takes from anywhere, dwarves will simply carry pieces of armor one at a time from the forge to the feeder stockpile. A larger long-term storage stockpile has bins, takes from links only, and takes from the nearby feeder stockpile. The heavy bins will only have to be moved a few tiles, and the armor in them is unavailable for a much shorter time.

### Single source distribution

This design works well for inputs that come from a single location (e.g. plants from farm plots), and are used in many other locations. Rather than simply putting a plant stockpile by each workshop that uses plants (which would mean a great deal of hauling barrels from those workshops to the farm plots to pick up new plants), place one "source" plant stockpile by the farms which disallows barrels, and takes from anywhere. All the farm crops will go there first (directly, because no barrels are involved).

Now, place a plant stockpile by each workshop that uses plants (still, farmer's workshop, etc.), set it to take from links only, and link it to take from the "source" stockpile. Ideally, each of these workshop-feeding stockpiles will take only an appropriately chosen subset of the plants (the still takes only brewable plants, while the farmer's workshop for the textile industry only takes plants that can be processed into thread, and so on). You may choose whether to allow barrels on a case by case basis, depending on how many of each plant you expect to have at once, how time-critical their processing is, etc.

If you are so inclined, you can use a quantum stockpile as the "source". This allows an infinite amount of storage in a tiny space. In the specific case of plants, this means your harvest *always* has somewhere to go, and will never wilt on the ground (unless your haulers are all busy elsewhere).

## Workshop layout for efficient hauling

It is virtually impossible to discuss stockpile design without simultaneously addressing workshop (or workflow) design. They are two sides of the same coin.

Most workshops take some items as *input* and produce other items as *output*. Consider an entire chain of workshops and products from raw materials to finished products. The closer each workshop's inputs are, the faster your dwarves can process them. When the outputs are in turn used as inputs in another workshop, it makes sense to keep those two workshops close together, to minimize the amount of distance each intermediate product has to move. In many cases, you may not even *need* a stockpile for the intermediate products; just let them sit in the first workshop until the second workshop is ready for them. (This depends on the workshop and the products.)

It's also worth mentioning that heavily congested corridors are extremely inefficient. Your most heavily traveled tunnels should be at *least* two tiles wide, and three tiles is better. When dwarves have to squeeze past each other, one of them has to stop moving to let the other go by. Worse, dwarves who are *about* to collide will run a path-finding algorithm (which takes computer time), and if an alternative route is available, they'll go out of their way - possibly a *long* way out of their way - rather than simply stop and let the other dwarf squeeze by. Try to avoid this.

### Stockpile placement

One strategy is to place the feeder stockpile immediately around the workshop. This works well for single workshops with just one input (like a mason's or mechanic's workshop).

     SSSSS   S feeder stockpile
     SWWWS   W workshop
     SWWWS
     SWWWS
     SSSSS

Another strategy is to put the workshop's stockpile above or below it. This keeps the stockpiles close to the workshops, and lets the workshops expand, even adding workshops on additional Z-levels as necessary. It works particularly well with multiple similar workshops working off the same stockpile.

              adjacent z-level
     WWW WWW      SSSSSSS
     WWWSSS
     WWW WWW      SSSSSSS

## Specific industry designs

### Farm-centric

Farms feed a wide array of workshops. Plants from farms may directly feed the kitchen, still, millstone (or quern) and farmer's workshop. The mill and farmer's workshop feed the loom and dyer which feed the clothier. Farms are in turn supplied seeds from the still, mill, farmer's workshop and dining rooms, completing the cycle of plant life.

As such, it's a good idea to design all (or at least, many) of these workshops and their stockpiles around each other. Above-ground farms can only be built in certain places, and underground farms are much *easier* to build in soil layers, so in many cases this dictates the location and layout.

### Butcher & Tanning

Because tanners are supplied directly from a butcher it's best to put them right next to each other. Designate a refuse stockpile taking Corpses for the butcher. Let the hides sit in the butcher's shop, and the tanner will take them directly to the tanner's shop with no hauling jobs required.

Consider placing a refuse stockpile somewhere behind an airlock (to keep out the miasma), to take the cartilage and other useless by-products.

- Note: When near a necromancer tower, butcher shops and refuse piles where corpses are collected should be kept within the fortress out of line of sight of any necromancer. When in an evil biome which causes the dead to reanimate, corpses should be disposed of promptly, preferably in magma.

### Kitchen

A food stockpile accepting meat/fish, raw edible plants\*†, cheese, leaves, cookable milled plants (everything but the dyes), fat†, cookable extracts (Dwarven syrup and all the milks†). If you cook booze, include that. If you want to reserve some edible plants for brewing, leave them out. Allow the maximum barrels. Remember to turn off prepared food.

*(\* plump helmet, muck root, bloated tuber, prickle berry, strawberry, rat weed, fisher berry and sun berry)*

*(† These items generally have better uses than cooking: milk for cheese, fat for tallow which is used in soap and plants for brewing as cooking will not return seeds. See kitchen for more information.)*

### Brewing

A food stockpile accepting brewable plants. Some of these have other uses, like pig tail for making thread, so you might want to disallow them if you plan on using them for something else. Remember to turn off prepared food.

Also include a barrel stockpile near your still to ensure a steady supply of empty barrels.

## Use of wheelbarrows

Wheelbarrows are tremendously useful tools, when properly applied. They allow a dwarf to move a single item at the dwarf's normal walking speed, *regardless of the item's weight*. But they have trade-offs, so they should not be used in every stockpile.

A major trade-off is that the dwarf has to walk to the stockpile first to fetch the wheelbarrow, then take the wheelbarrow to the item, and finally back to the stockpile. So, each hauling job may involve a much greater travel distance, and even though all the walking done at full speed, the total time spent may actually increase if you aren't careful.

Wheelbarrows are used by default in stone stockpiles, and for good reason -- stones are *heavy*! Dwarves, especially weak ones, will move extremely slowly when hauling a stone without a wheelbarrow or minecart. It is strongly recommend that if you have any workshops which process stones, you use a feeder stockpile near them (linked to give to the workshop, so the mason doesn't carry a stone all the way from her bedroom!), and use wheelbarrows in that stockpile. This way, the stone is only ever carried by hand for a few tiles, from the stockpile to the workshop, by the mason/mechanic/craftsdwarf doing the work.

Furniture stockpiles are another good use of wheelbarrows, as many pieces of furniture are extremely heavy (a granite statue weighs 156Γ, and a gold statue weighs 1159Γ, despite being made out of 3 gold bars that weigh 115Γ apiece -- dwarves aren't great at math).

By contrast, wheelbarrows are not a great choice for a wood stockpile. Most logs of wood weigh about 30Γ, which will not slow a dwarf of average strength. Forcing the use of wheelbarrows would just increase the time spent per log, as well as reducing the number of simultaneous log hauling jobs. (Weak or very weak dwarves *will* be slowed when hauling typical logs; you may wish to disable wood hauling on these dwarves. Ironically, very weak dwarves make great stone haulers, because they can push a wheelbarrow perfectly well.)

## See Also

- Minecart
- Quantum stockpiles
