# Workshop

> Fonte: [Workshop](https://dwarffortresswiki.org/index.php/Workshop) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

!!UNKNOWN!!  · xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Workshops** are buildings where materials are processed by dwarves into more valuable or useful items. There are a total of 31 workshops: 14 first tier, 11 second tier and 6 third tier across the game's various industries.

## Description

**Production flowchart for most workshops**.\
Not all items are represented!\
*(Click to enlarge)*

Anything that is created, refined, cooked, altered, decorated, or generally "produced" is processed at a workshop. There are many different types of workshops, for different purposes and different finished products. Just as they have specific products associated with them, they have specific labors that are required by dwarves to build them or to work there, and dwarves with more of the appropriate skill tend to produce higher quality objects\*, and/or produce them faster.

(\* *if the finished product has any quality modifiers - not all do: Processed milk is just cheese, a stone block is just a stone block, and a tanned hide is just leather, etc*.)

You can use the workshop interface to restrict the use of individual workshops to specific dwarves, called workshop Masters, to create workshop-specific work orders, and limit how individual workshops accept general work orders.

Almost all workshops measure 3 tiles square, 3×3, but a few are 5×5, or even a single tile.

### Operation

When there are items ordered at a workshop, the workshop will generate item creation jobs until it finds a suitable dwarf with appropriate labors (and skill level and so on if those are set in the workshop orders). When the dwarf is found, an A will appear next to the job in the workshop queue, and the following will happen:

1.  The dwarf finds the nearest, most suitable base raw material.

This is nearest to their current location, not the workshop.

If any stockpiles are set to give to the workshop, only linked stockpiles will be looked in.

In case of decoration jobs: the material to decorate with is fetched first (and the item to decorate with afterwards).

In case of jobs needing fuel: the fuel is fetched last.

1.  The dwarf gets that material and hauls it to the workshop.
2.  The dwarf repeats that until all the necessary ingredients are in the workshop.
3.  The dwarf labors in the workshop for a while and creates the item.
4.  The dwarf leaves the finished item in the workshop.
5.  At this point, the workshop goes to the next queued task, and starts looking for a suitable dwarf again, often the dwarf who just finished the previous.
6.  A new hauling job is (eventually) queued to take the finished item to the nearest suitable stockpile. (See \#2 for linked stockpiles)

If you have no stockpiles to put finished objects in, workshops will become cluttered. You can see the clutter by checking the contents of the workshop by clicking on it. The more items there are, the longer tasks will take.

If you have only one dwarf with the appropriate labors, and the task of fetching items takes a long time because the stockpiles are far away, then they will execute far fewer jobs before it's time for a break. If you have many dwarves, then recruitment of another one will waste time since they are far away. Therefore, in either situation, it's in your interest to put the stockpiles as close as possible to the workshop.

### Interface

A workshop's interface is accessed by clicking on it. This will open a new window showing the properties and controls of the workshop. The top section will show the name of the workshop; buttons to control its links to stockpiles, to rename it, and to deconstruct it; the tabs for Tasks, Workers, and Work orders; and the list of currently queued tasks and the button to add new tasks. The bottom section shows the current contents of the workshop, including the item that was used to construct the workshop.

The **Tasks tab** shows the current list of tasks, and is what allows you to queue up new tasks to be carried out immediately. Tasks are carried out in the order they are listed, with the current task being the topmost in the list.

To queue up a new task:

1.  Click the *Add new task* button to open up the list of valid tasks for this workshop. Tasks that can currently be queued will be in white text, while tasks that cannot be currently queued will be in orange text with red text beneath them indicating why they are not available (typically lacking a required material).
2.  Click on the task you want the workshop to perform. This will close the list and the task will be added to the bottom of the queue.

Each task will have a series of buttons beside it, allowing you to control certain aspects of how that task is carried out:

- The active task icon (a page and green check mark); this isn't a button, but indicates which task is currently being done.
- The repeat task button (two circling arrows) tells the workshop to continually repeat the task until it is either manually cancelled by the player or the workshop runs out of materials required for the task.
- The highest priority button (yellow exclamation point) which instructs the workshop to carry out the task with the highest possible priority. This is useful for emergency lever-pulling and other time-critical tasks.
- The increase priority button (orange up arrow), which moves the task higher in the task queue, to be carried out sooner.
- The details button (), which allows you to specify certain details of the task, such as choosing the material(s) to be used, the size of the resulting item (eg. clothing for difference species), or the imagery to be used in creating an artistic work.
- The pause button, which pauses the task until pressed again. A paused task does not prevent the workshop from continuing through the rest of its queue, it is simply skipped over.
- The cancel task button (red X), which deletes the task from the queue.

The **Workers tab** allows you to assign a Master to the workshop, restricting its use to that dwarf alone. Only one Master may be assigned to a given workshop. This can be useful if you want to restrict your highest-quality materials to be used by your most-skilled dwarves: by making them masters of their own workshops and controlling access to materials using stockpile links, those materials don't end up being used for lower-quality items in general workshops. By default, all workshops start as "This workshop is free for anybody to use."

To assign a workshop Master:

1.  Click on the Workers tab in the workshop interface.
2.  Click on the Add dwarf button to bring up the list of your dwarves. Beside each listed dwarf will be a button that will let you toggle them between "free to do any task" and "specialized". Dwarves set to "specialized" will only do tasks in their assigned workshops, work details, and occupations.
3.  Click on the dwarf's name to make them Master of this workshop. The list will close and return you to the Workers tab.

Once a Master is chosen, they will be listed on the Workers tab, along with the specialization toggle button. If you wish to remove them as workshop Master, click the red X button next to their name to return the workshop to general use.

If you have not assigned a workshop Master and have DFHack installed, you will be able to set a slider for the minimum and maximum skill level that a dwarf must have in order to perform tasks at the workshop. DFHack also provides a selection interface for which labors to enable for the workshop, filtering which general manager jobs the workshop will accept. These are vanilla features that the vanilla UI no longer provides an interface for.

Dwarves with strange moods seem to be able to claim a workshop, even if they do not meet the profile criteria.

The **Work orders tab** allows you to set up new work orders for the workshop, and lists all work orders specific to the workshop. These require the Manager noble position to be filled and operate identically to work orders created by a Manager (and will appear in the Manager's work order list), except that they apply only to the workshop in which they are created.

At the bottom of the Work orders tab is "General work orders allowed". This allows you to control how many general (ie. Manager-created) work orders the workshop will accept. The default value is 5. Setting this to 0 means that the workshop will not accept any general work orders, and will only perform work orders created specifically for that workshop.

## Management

As your fortress continues to grow and diversify, it becomes increasingly difficult to keep your workshops fruitfully busy without causing overproduction or underproduction or depleting your resources. Though no process can be truly automated, there are a few tricks to keeping your workshops productive.

### Standing orders

Standing orders provide a rudimentary form of automation for some specific workshops in *Dwarf Fortress*. Certain goods or materials are only useful for one thing, having no other use and requiring refinement before they can be made into something useful. Thus, standing orders automate certain tasks, queuing them up whenever input materials are available; this behavior may be configured in the "Labor" menu by pressing y or clicking the hammer icon in the bottom left toolbar, and selecting the Standing orders tab. Note that this rudimentary automation performs poorly with multiple workshops, often queuing dwarves to carry the materials to the farthest available workshop.

- **Automatically weave all thread**: This option instructs the loom to weave any thread into cloth whenever it becomes available. There are two other options: Automatically weave dyed thread, which behaves the same except it will only use dyed thread; and No automatic weaving, which disables all automatic weaving.
- **Use any cloth**: This option doesn't control any automation, instead restricting whether your clothier's shops will use any available cloth, or **Use only dyed cloth**.
- **Automatically collect webs**: This option instructs the loom to automatically queue up "Collect webs" tasks whenever spiderwebs become accessible to your dwarves. This can make your dwarves go wandering off into the caverns at some risk.
- **Slaughter any marked animal**: This option instructs the butcher's shop to queue up a "Slaughter animal" task any time an animal is marked for slaughter.
- **Automatically butcher carcasses**: This option instructs the butcher's shop to queue up a "Butcher corpse" task any time a valid, unrotten corpse becomes available nearby. Butcherable corpses have no other use, and will rot if not processed quickly.
- **Automatically clean fish**: This option instructs the fishery to queue up a "Prepare a raw fish" task any time an unrotten unprepared fish becomes available. Unprepared fish is not edible as-is and rots quickly, so leaving this on is recommended if your fort has a fishing industry.
- **Automate kitchen**: This option instructs the kitchen to queue up a "Render fat to tallow" task any time a glob of fat becomes available from butchering an animal. The resulting tallow is useful for making soap and as a low-value "solid" cooking ingredient, however you will likely end up with an overabundance of tallow. Since the original fat apparently doesn't rot, and the rendering job is slow and tends to distract your head cook when he should be cooking the quickly-expiring meat instead, it is often more convenient to disable the automatic rendering and manually queue the job (on an auxiliary kitchen) if you somehow run low on tallow.
- **Automate tannery**: This option instructs the tanner's shop to queue up a "Tan a hide" task any time an unrotten animal skin becomes available from butchering an animal. Skins will rot quickly if left untreated, so leaving this enabled can be useful; however, players processing skin into parchment will probably want to disable automatic tanning.

### Repetition

You can queue up to ten tasks in any workshop, and tell the dwarves to repeat any or all of them for as long as possible. This is most useful if you want to process all of a resource that you have into something usable (such as lye and tallow into soap), but don't know how much you have, or can't be bothered with exact numbers. If you want to keep a workshop busy, repeating a task for a period of time is the best way; most fledgling fortresses have craftdwarves making stone crafts 24/7. It is necessary to check back on your stocks every once in a while, however, as you might forget about your stone carver for a while and upon placing furniture discover that you have 99 doors but no tables. The easiest example would be gem cutting; just queue up all of the gems you've dug up on repeat, and use the cancellation messages to monitor progress through the stack. Note that if you place multiple jobs on repeat your dwarves will cycle through them, so you can have your mason make doors, cabinets, coffers, tables, and thrones (the "welcome to the fortress" package) in equally large numbers.

### Manager

Appointing a manager noble allows you to queue work orders using the job manager interface, though your manager will need time to approve work orders before production begins. Using the job manager interface has two major advantages. Firstly, it allows you to produce an exact number of items as opposed to putting a workshop on repeat, and secondly, it allows easier management of complex tasks: although you will get cancellation spam, the tasks will simply re-queue, to be fulfilled as soon as the prerequisites are in order. This makes complicated processes, such as the production of twenty steel breastplates for your military, much simpler and less time-consuming. You will be notified when your work orders are completed, so it has the advantage of timely organization as well.

### Workflow

Finally, for those who find the other automation options lacking, the dfhack "workflow" plug-in allows for automated job processing for many applications (e.g. auto process plants, auto mill plants, auto brew, auto make soap, etc.). Unfortunately, setting up the necessary rules can require some trial and error and a considerable investment of time, but the results can be well worth the trouble, at least until comprehensive automation support is added to the game itself.

## Tier system

The tier system was developed to help understand how far removed a workshop is from the basic raw materials that can be found throughout your average map. A Tier-1 workshop processes raw materials directly; a Tier-2 workshop processes the output of a Tier-1 workshop (but may also include new raw materials); and a Tier-3 workshop processes the output of a Tier-2 workshop (but may also include inputs from lower levels) Note that containers (cloth and leather bags) are considered Tier 1 materials even though they are produced at a higher tier, because these items are reusable; your dwarves will not need to create a new bag each time they want to mill some flour. In some cases, a workshop may fit into multiple tiers, (ex. Mechanic's workshop). In these cases, the workshop is listed in the lowest applicable tier for its primary purpose.

Tier 1 workshops use Tier 0 materials (animals, ore, wood, plants, bone, etc.).

Tier 2 workshops use Tier 1 materials (processed Tier 0 materials) and possibly Tier 0 materials.

Tier 3 workshops use Tier 2 materials (processed Tier 1 materials) and possibly Tier 0 and/or Tier 1 materials.

### Tier 1 workshops

- Bowyer's workshop b-o-b
  - Uses Tier 0 material: Wood
  - Can also use higher-tier material: Bone
  - Produces Tier 1 Weapon: Crossbow
- Carpenter's workshop b-o-p
  - Uses Tier 0 materials: Wood
  - Produces Tier 1 materials:
    - Armor: Buckler, Shield
    - Weapons: Training Axes, Training Swords, Training Spears
    - Containers: Barrel, Bin, Bucket, Casket
    - Building Materials: Block, Grate, Pipe section
    - Furniture: Bed, Bookcase, Chair, Table, Cabinet, Chest, Armor stand, Weapon rack
    - Furniture: Door, Floodgate, Hatch cover
    - Trap Components: Cage, Enormous corkscrew, Menacing spike, Spiked ball
    - Finished Goods: Crutch, Splint
    - Tools: Animal trap, stepladder, wheelbarrow, minecart
- Jeweler's workshop b-o-j
  - Uses Tier 0 Item: Rough gem
  - Can also use higher-tier items: Cut gems, Encrustable objects
  - Produces: Cut gem, Encrusted objects
- Stoneworker's workshop b-o-t
  - Uses Tier 0 Item: Stone
  - Produces Tier 1 Items: Armor stand, Block, Throne, Coffin, Door, Floodgate, Hatch cover, Grate, Cabinet, Coffer, Statue, Table, Weapon rack, Quern, Millstone, Slab
- Butcher's shop b-o-f-b
  - Uses Tier 0 Items: Tame animals, Corpses of untamed non-sentient animals
  - Produces Tier 1 Items: Skin, Fat, Meat, Bone, Prepared organs, Skull, Scale, Hoof, Ivory, Tooth
- Mechanic's workshop b-o-h
  - Uses Tier 0-1 Items: Stone, Table, Rope
  - Produces Tier 1 Item: Mechanism
  - Produces Tier 3 Item: Traction bench
- Farmer's workshop b-o-f-f
  - Uses Tier 0 Items: crop, Animal
  - Can use Tier 1 Reusable Items: Bags, Barrels, Vials, Buckets
  - Produces Tier 1 Items: Pig tail thread, Rope reed thread, Quarry bush leaves, Dwarven syrup, Plant extracts, Milk, Cheese
- Fishery b-o-f-y
  - Uses Tier 0 Items: Raw fish
  - Produces Tier 1 Items: Fish meat, Shells, Captured live fish
- Craftsdwarf's workshop b-o-r
  - Uses Tier 0 Items: Stone, Wood
  - Can also use higher-tier items: Bone, Shell, Ivory, Tooth, Horn, Pearl, Cloth, Leather, Slabs
  - Produces: Finished goods, Pots, Jugs, Tools, Memorials
- Siege workshop b-o-g
  - Uses Tier 0 Item: Wood
  - Can also use higher-tier item: Ballista arrowhead
  - Produces: Catapult parts, Ballista parts, Ballista arrows
- Wood furnace b-o-u-f
  - Uses Tier 0 Item: Wood
  - Produces: Fuel (Charcoal), Ash
- Magma smelter b-o-u-L (requires magma access):
  - Uses Tier 0 Items: Coal, Ore, Flux
  - Can also use higher-tier items: Fuel (Charcoal, Coke), Metal bars, scrap weapons, armor, etc.
  - Produces: Metal bars, Coke
- Magma kiln b-o-u-K (requires magma access):
  - Uses Tier 0 Items: Gypsum, Alabaster, Selenite, Satinspar, Kaolinite, Clay, Silty clay, Sandy clay, Clay loam, Fire clay, Cassiterite
  - Can also use higher-tier items: Ash, Potash
  - Produces: Pearlash, Gypsum plaster, Ceramics (Jug, Bricks, Statue, Large pot, Crafts, Hive), Glazed items
- Magma glass furnace b-o-u-G (requires magma access):
  - Uses Tier 0 Items: Sand bag, Raw rock crystal
  - Can also use higher-tier item: Pearlash
  - Produces: Raw crystal/clear/green glass, Blocks, Vials, Toys, Instruments, Goblets, Trap weapons, Windows, Furniture

### Tier 2 workshops

- Tanner's shop b-o-f-t
  - Uses Tier 1 Item: Hide
  - Produces Tier 2 Item: Leather
- Loom b-o-l-o
  - Uses Tier 1 Items: Adamantine strands, Cave spider silk thread, Giant cave spider silk thread, Phantom spider silk thread, Pig tail thread, Rope reed thread
  - Produces: Cloth
- Still b-o-f-l
  - Uses Tier 0 Item: Brewable Plant
  - Uses Tier 1 Reusable Item: Barrel
  - Produces: Drink
- Ashery b-o-y
  - Uses Tier 1 Item: Ash
  - Can use Tier 1 Reusable Item: Bucket
  - Produces Tier 2 Items: Lye, Potash
- Kitchen b-o-f-k
  - Uses Tier 1 Items: Fish, Meat, Cheese, Dwarven syrup, Milk, Prepared organs, Fat
  - Can also use lower-tier items: Plants, Seeds, Eggs
  - Can also use higher-tier items: Alcohol, Dwarven sugar, Flour, Tallow
  - Produces: Prepared meals, Tallow
- Screw press b-o-R
  - Uses Tier 1 Items: Honeycomb
  - Uses Tier 1 Reusable item: Jug
  - Can also use higher-tier item: Rock nut paste
  - Produces: Honey, Wax, Rock nut press cake, Rock nut oil
- Quern b-o-f-q
  - Uses Tier 0 Items: Blade weed, Cave wheat, Dimple cup, Hide root, Longland grass, Sliver barb, Sweet pod, Whip vine, Rock nuts
  - Uses Tier 1 Reusable Item: bag
  - Produces: Dwarven wheat flour, Dwarven sugar, Longland flour, Whip vine flour, Dimple dye, Emerald dye, Redroot dye, Sliver dye, Rock nut paste
- Millstone b-m-n (under Mechanisms instead of Workshops)
  - Requires: Mechanical Power Source (Water wheel or Windmill), and a Millstone (Constructed at Mason's workshop)
  - Uses Tier 0 Items: Blade weed, Cave wheat, Dimple cup, Hide root, Longland grass, Sliver barb, Sweet pod, Whip vine, Rock nuts
  - Uses Tier 1 Reusable Item: bag
  - Produces: Emerald dye, Dwarven wheat flour, Dimple dye, Redroot dye, Longland flour, Sliver dye, Dwarven sugar, Whip vine flour, Rock nut paste
- Smelter b-o-u-l
  - Uses Tier 1 Items: Fuel (Charcoal, Coke)
  - Uses Tier 0 Items: Coal, Ore, Flux
  - Can also use higher-tier items: Metal bars, can melt metal weapons, armor, etc.
  - Produces: Coke, Metal bars
- Kiln b-o-u-k
  - Uses Tier 0 Items: Gypsum, Alabaster, Selenite, Satinspar, Kaolinite, Clay, Silty clay, Sandy clay, Clay loam, Fire clay, Cassiterite
  - Uses Tier 1 Items: Fuel (Charcoal, Coke), Ash, Potash
  - Produces: Pearlash, Gypsum plaster, Ceramics (Jug, Bricks, Statue, Large pot, Crafts, Hive), Glazed items
- Glass furnace b-o-u-g
  - Uses Tier 0 Items: Sand bag, Raw rock crystal
  - Uses Tier 1 Items: Fuel (Charcoal, Coke)
  - Uses Tier 2 Item: Pearlash
  - Produces: Raw crystal/clear/green glass, Blocks, Vials, Toys, Instruments, Goblets, Trap weapons, Windows, Furniture

### Tier 3 workshops

- Leather works b-o-l-l
  - Uses Tier 2 Item: Leather
  - Produces: Leather Clothing, Leather Armor, Leather Shield, Leather Quiver, Leather Bag, Leather Backpack, Leather Waterskin, Leather Images (decoration)
- Dyer's shop b-o-l-y
  - Uses Tier 2 Item: Dye, Cloth
  - Can also use lower-tier item: Thread
  - Produces: Dyed Thread, Dyed Cloth
- Clothier's shop b-o-l-k
  - Uses Tier 2 Item: Cloth
  - Can also use higher-tier item: Dyed Cloth
  - Produces: Backpack, Bag, Clothing, Quiver, Rope
- Metalsmith's forge b-o-i
  - Uses Tier 1 Item: Fuel (Charcoal, Coke)
  - Uses Tier 2 Item: Metal bars
  - Produces: weapons, trap components, bolts, ballista arrowheads, armor, chains, crafts, coins, goblets, studding, anvils, blocks, furniture, animal traps and mechanisms.
- Magma forge b-o-I (requires magma access):
  - Uses Tier 2 Item: Metal bars
  - Produces: Armor, Weapon, Chain, Crafts, Furniture
- Soap maker's workshop b-o-P
  - Uses Tier 2 Items: Tallow, Lye
  - Can also use higher-tier item: Rock nut oil
  - Produces: Soap

Note that some specific products can be higher-tier than indicated above. For example, production of steel weapons requires: producing fuel, producing Iron bars, producing pig iron bars, producing steel bars, then finally forging weapons (a Tier-5 process).

## See Also

- Manager
