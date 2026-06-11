# Stockpile

> Fonte: [Stockpile](https://dwarffortresswiki.org/index.php/Stockpile) — Dwarf Fortress Wiki (GFDL/MIT)

**Stockpiles** are where dwarves store items of various types, usually in a safer, closer or more convenient place for the consumers. Dwarves with the corresponding "hauling" job will seek out items that are not already on a stockpile that accepts them and carry them to an appropriate stockpile, if available. It's important to place your stockpiles carefully to minimize the amount of time spent carrying items back-and-forth. Items in a stockpile may be stored in containers such as bags, barrels or bins (see Using bins and barrels). Seed bags, flour bags, and dye bags can go inside barrels. Empty bags, however, cannot be stacked.

## Allocating stockpiles

To allocate an area as a stockpile, use the menu. The right-hand menu pane will list all the stockpile categories, and the appropriate key to press to begin allocating that type. Allocating an area works exactly the same as designating an area. Press to specify the first corner of the stockpile, use the primary movement keys to move the cursor to the opposite corner, and press again. (Alternatively, it is possible to use the mouse at this stage to select individual tiles) This will create a stockpile of the chosen type that occupies the area between the two corners specified. If the chosen area has parts that cannot be made into a stockpile, like a wall, a workshop, or an already existing stockpile, a stockpile will be created but they will not be part of it.

When creating a stockpile, any movable items (e.g. loose stone, unbuilt furniture, etc.) currently occupying the designated tiles will automatically be considered part of the stockpile, even if the stockpile settings disallow those particular items. These items also mark the tile as "full", so no new items will be stored in that tile until all the original items in the tile are moved. To handle unwanted items, you can specify that the stockpile "gives" to a workshop or stockpile that will accept those items, or use a dump command to have them carried off to a garbage zone.

Removing a stockpile works exactly the same, but choose : Remove Designation. This will un-designate the specified area. It is possible to create a single stockpile with a shape other than a rectangle by using the Remove Designation tool to remove only part of the stockpile. This can be useful for cutting out sections of a stockpile in a way to carve a convenient path through them.

Stockpiles cannot be expanded once created; you must delete the pile and create a new one. DFHack provides three stockpile-related commands capable of loading, saving, and copying stockpile settings, which can make moving and resizing stockpiles much less tedious.

### Stockpile Designation Size Limits

Stockpile allocation (and removal) is limited in size: each edge of the designation area is limited to a maximum of thirty-one tiles. The limit is per-edge, so for example a stockpile that is only two tiles wide is still limited to a length of thirty-one (2x31 total size.) The largest possible stockpile is therefore a square of 961 tiles (31\*31). DF will not allow a larger area to be selected.

Note that this size limitation applies not only to creating stockpiles, but also to removing them. This means that you also cannot remove stockpiles with in areas greater than 31 long or wide - DF will limit the operation to an area of 31x31 tiles, at most.

## Using stockpiles

Once a stockpile has been allocated, by default dwarves will automatically move items to the stockpile when they are available, and as long as the stockpile has available space. Note that the dwarves will place the item into the empty spot that is nearest to the item, *not counting any obstructions*. Additional behavior also includes the fact that dwarves will stockpile the *newest* item first, which may not necessarily be the nearest item to the stockpile. You can disable automatic stockpiling by setting the stockpile to "take from links only" using . Tiles, within a stockpile, containing only forbidden items are considered available space, and can accumulate another item without exploiting quantum stockpiling.

One method to ensure a workshop has raw material on hand is to place a small stockpile next to the workshop. This will speed up production as the crafter in question only has to take a few steps to obtain the material (this also prevents the crafter from dragging material across the entire map when a new job order is issued). Whenever a crafter picks up material from the stockpile, your hauling dwarves will automatically fetch more material to refill the stockpile. This speeds up a queue of jobs, as other dwarves perform the time-consuming distant haul whilst the crafter concentrates on actually making items.

It's not necessary to place stockpiles for all types of objects. If no storage is available for a certain item type, dwarves will seek out items wherever they might lie as mentioned earlier. This can be advantageous — if you don't have a stockpile for gems, your jeweler will go pick up fresh gems without waiting for them to be carried to a pile first. However, this also means your jeweler has to spend a lot of time fetching the gems. If you have enough haulers available, it's generally more advantageous to designate stockpiles than not. Also remember that your workshops will get cluttered and suffer production slowdowns if you let ridiculous numbers of items pile up in them, so it's important to occasionally clear out workshops if they get cluttered. This can be done either by having a stockpile available so that haulers will remove the items, by quantum stockpiling the accumulation, or by removing and rebuilding the workshop, which will empty its contents onto the ground.

## Take from a stockpile/workshop

Another feature of stockpiles allows you to tell dwarves to transfer items from one stockpile to another. To specify such a flow, use the menu, and highlight the *destination* stockpile. Press , and, using the cursor, highlight another stockpile and press . Your chosen stockpile will now list the stockpile it will take from. This will cause items in the second stockpile to be hauled to the first stockpile. To stop the first stockpile from taking items from the second, use the menu on the first one, highlight the unneeded stockpile in the list using and and press **elete Selected**.

Each stockpile can take from any number of other stockpiles. You can't make two stockpiles feed into each other, although larger loops (e.g. three stockpiles that feed into each other in a circle) are allowed.

Stockpiles may also take from a workshop, using the same interface (-, then select a workshop instead of a second stockpile). In this setup, any items produced inside the workshop (visible with ) become eligible to move to the stockpile. Be aware that any items produced in the workshop that *aren't* accepted by the linked stockpile will not be moved anywhere at all. They will sit inside the workshop until a linked stockpile accepts them.

Enough micromanagement will allow for effective and (relatively) streamlined supply chains. Here are some examples:

- Speeding up lumber harvesting, carpentry, *and* ash and charcoal production by putting several wood stockpiles near the various tree-felling areas, then one large "primary" stockpile near the carpenter's workshop that takes from those small ones, and then finally, a small stockpile near the wood furnace that takes from the primary one.
- A smallish plant stockpile near your farms, disallowing barrels, will allow harvesters to spend very little time stockpiling the crops they just picked. A larger stockpile near the still (this one possibly allowing barrels), taking from the smaller stockpile, lets your general-purpose haulers do most of the grunt work of getting plants in place for the brewer. The larger stockpile should be set to "take from links only", so the harvesters do not waste their time.
- A clothier's shop produces high-quality new clothing. There is currently no way to stockpile *only* new clothing, as opposed to worn clothing, except for the fact that the new clothing is sitting in its workshop. A stockpile can be set to take from the clothier's shop (and to "take from links only"), so that it only gets new clothing produced in that workshop. If another stockpile with "take from anywhere" and no links is created, that one will accept all the worn clothing - it will never take from the linked clothier's shop. This worn-clothing stockpile may be placed near the trade depot, if you plan to sell the used clothing, or near the garbage disposal, if you do not.

## Give to a stockpile/workshop

Conversely, the key allows a pile to give items to another pile, or to a workshop. When giving to a stockpile, an equal and opposite "take from stockpile" is created in the other direction (and vice versa). Deleting one of these inter-stockpile links also deletes the other link.

Specifying that a workshop or furnace will only get its materials from a certain stockpile provides a way to make sure everything that the workshop produces is of a specific material. For example, setting a granite stockpile to give to a mason's workshop ensures that the workshop will only use granite as its material. This is also extremely important when the workshop's input materials are heavy (e.g. stones); linking a nearby stone stockpile to the workshop prevents the mason from hauling an enormous rock from hundreds of tiles away.

This option is quite powerful, but should be used **very** carefully as the linked workshop will now *only* take from the stockpiles set to give to that workshop. Make sure that the workshop gets *all* of the materials needed for its jobs there if you use this feature. For example, if you link your ore stockpile to a non-magma smelter, but don't also link a stockpile that includes a fuel source, then the dwarves will be unable to smelt ores at that smelter due to a lack of fuel. If you set a fuel stockpile to give that smelter, it will still be unable to melt down items marked for melting, because it only takes from the ore and fuel stockpiles. Another common mistake is setting a plant stockpile to give to a still, but forgetting to also link a furniture stockpile to the still so that it has access to barrels.

## Max bin/barrel

The *max bin* and *max barrel* settings control the number of barrels and bins that are used for the organisation of items inside the stockpile. It can be useful to disallow bins and barrels from some stockpiles, for example stockpiles used to store seeds or for quantum stockpiles, by reducing this setting to 0.

Increasing these numbers is not usually needed - they are set to the number of tiles in the stockpile when it is created, which is the maximum number of bins or barrels the stockpile can hold anyway. Which of bins or barrels is turned on is determined by the item type selected when the stockpile is designated - food stockpiles allow barrels, for example, and bar stockpiles allow bins. However, these settings are not updated if the types of items allowed in the stockpile are changed. If you change the types of items allowed in the stockpile, it may also be useful to change the number of bins and barrels that are allowed in it to allow your dwarves to store those items more efficiently.

## Max wheelbarrow

Another feature of the stockpile system, *max wheelbarrow* allows the player to control the number of wheelbarrows assigned to the stockpile. It can be set to 0, 1, 2, or 3.

If set to 0 (which is the default for all stockpiles other than stone stockpiles), the stockpile will generate a separate hauling job for each item that needs to be placed in it -- potentially one job per tile in the stockpile, simultaneously.

If set to non-zero, then that number of wheelbarrows will be brought to the stockpile. Once a stockpile has wheelbarrows assigned and moved to it, the number of wheelbarrows will act as a limit on the number of simultaneous hauling jobs for moving items to that stockpile. Each hauling job will be performed using a wheelbarrow, rather than by hand. You can see this as fine-tuning the speed of collection of the desired items.

Unfortunately, wheelbarrows are currently rather buggy, and may actually reduce the efficiency of your stockpiles; see Wheelbarrow for more information.

Minecarts can also be used for efficient hauling, although they require a much greater infrastructure investment.

## Will take from anywhere

A stockpile that will take from anywhere does not restrict the source of its goods. Stockpiles with "take from links only" enabled will only accept goods from their assigned workshops and linked stockpiles. You can use to toggle this setting on a stockpile.

Setting your seed stockpiles to "take from links only" will prevent your haulers from carrying your vital seeds back and forth across the map to pick up each new seed in the dining room. When your stockpiled seeds run low you can temporarily toggle to "anywhere" to collect the loose seeds in bulk.

## Stockpile categories

### Ammo

This stockpile contains ammo for all forms of ammunition-requiring weaponry (except siege engines). It can use bins to consolidate stacks.

### Animal

Animals stored in cages that are not affixed to a location will be stored in these stockpiles. Traps used for capturing wild animals and empty cages are also stored here.

This type of stockpile cannot use bins or barrels.

### Armor

Armor of all types is stored here. There is no preference for specific body parts, but usable/unusable armor may be specified. All types of armor can be stored in bins.

Note that if refuse is enabled on the stockpile, armor and clothing will wear at an accelerated rate.

### Bar/Block

Bars of smelted metal and blocks of cut stone and glass are kept here after being processed by the smelter, mason's workshops, and glass furnaces, before being used for other purposes. Weirdly, ashes, potash, soap, charcoal, and coke from the wood furnace, ashery, soap maker's workshop and smelter will also be stored here. As with all stockpiles, this can be changed to allow for specific blocks and bars to be stored with custom settings. Bins can be used to consolidate up to 10 bars/blocks.

### Cloth

Woven cloth and thread are stored here (plant fiber, animal hair, and silk). Bins can be used to consolidate items.

### Coins

Minted coins are kept here, several thousand of them fitting into a single bin.

### Corpses

Dead dwarves and pets that have no burial location will be placed here. If placed indoors, decaying bodies will generate miasma, but bones will not be removed at the end of the season. Unless they are given a proper burial in a burial receptacle, rotting pets or friends will give dwarves unhappy thoughts and may even come back to haunt you.

Corpse stockpiles are meant to be used as *morgues*, though the inclusion of invader corpses makes this slightly difficult.

### Finished Goods

Finished goods created by the craftsdwarf's workshop, as well as the clothier's shop and the leather works, are placed here before being used in trade or other uses. This type of stockpile can use bins to consolidate items, over a hundred objects can fit into a bin.

Since this stockpile can also contain supplies that the player might not want to trade away (splints, crutches, ropes, waterskins...), it is wise to make separate custom stockpiles for these goods.

Note that if refuse is enabled on the stockpile, clothes and armor will wear at an accelerated rate.

### Food

As one would assume based on the name, food is stored here, in addition to a wide variety of inedible plant and animal products -- seeds, lye, giant desert scorpion venom, bags of dye, and liquid fire, to name a few. Raw fish is brought here, before being processed by a fishery and turned into edible meat. Drinks are always stored in barrels or large pots. Seeds are stored in bags (which may in turn be stored in barrels/pots); other food items can be stored in barrels or pots.

Barrels and pots can hold, at most, 60 prepared meals. Stacks larger than that (☼Dwarven Beer Roast \[200\]☼ is possible) will not fit in a barrel, but will still only take up one tile of stockpile space. To free up barrels, you may decide to have separate prepared food stockpiles that do not accept barrels - if you cook larger meals, this shouldn't be a problem.

Food will never spoil while in a stockpile, although it may attract and be eaten by vermin. Food stockpiles should, in most cases, be restricted to desired types (e.g. seed stockpiles or meat stockpiles or unprepared fish stockpiles); there are simply too many things that go in them.

Fat and tallow go in the same list and are listed by animal, meaning that manual separation of fat and tallow takes a *long* time. Because fat will only ever enter your fortress at a butcher's shop, it is possible to link a general fat/tallow stockpile to the butchers' and have it take only from links. It may be necessary to link the butchers' to the stockpile you want the other butchery products to end up in. If you are playing with DFHack, you can use the search function to show only fat or tallow- the permit and forbid keys to toggle only those visible in the list.

### Furniture Storage

Completed items from the carpenter's workshop, mason's workshop, and mechanic's workshop will be stored here, along with furniture created from other shops, until placed or used in another building. Bags filled with sand can also be stored in furniture stockpiles, and in fact will appear in any furniture stockpile unless expressly forbidden, regardless of materials permitted.

Since this is a very broad category, it may be useful to create stockpiles for a specific type of item (like barrels, bags, bins, mechanisms) via the stockpile settings.

Furniture cannot be stored in barrels or bins.

### Gem

This stockpile stores gems and raw glass, both cut and uncut, along with gizzard stones. It can use bins to consolidate gems.

### Leather

Leather, which is produced at a tanner's shop, will be kept here. Like most stockpiles, it can use bins to consolidate items.

### Refuse

Since dwarves hate rot, because of the miasma it spreads when in an enclosed place like a cave, any garbage item that can rot will be stored in a refuse stockpile. Also, any XXdamaged itemsXX will be moved to the refuse stockpile. Many players prefer to place this stockpile outside their cavern, usually a small distance from the entrance, as rottable items on tiles that are do not generate miasma.

If placed on a tile, decaying items will generate miasma, which will spread through your fortress and generate a small unhappy thought in any dwarf passing through it. For this reason, it is sensible to build doors (preferably several, separated by a few tiles to create an airlock) to all of your indoor refuse stockpiles. Miasma won't spread through a closed door, so only dwarves with business in the room will be bothered by the rot.

An alternative to this is to dig channels down from the surface, creating an area of tiles considered to be , yet still located within your fortress. You can place your refuse stockpile here, and although it will be in your fort, rotten items on those tiles will not generate miasma. If you choose to cover them with walls or floors for security and/or aesthetic reasons, it will convert them to , but they will remain tiles, which again do not generate miasma in rotten items. (For even more creative methods to restrict the spread of foul rotting stench, see the miasma page.)

Bones, skulls, and shells are also stored here, whether from defeated enemies or raw food processing - if left in an area with high vermin levels, these will randomly disappear. Refuse stockpiles can be restricted to store only bones, skulls, shells, teeth, and horns/hooves.

Note that a refuse stockpile is not the same as a garbage dump. A garbage dump is only for things manually marked to be dumped. Additionally, refuse types specifically marked as **Dwarves Dump***refuse type* in - will be hauled to the garbage dump instead of the refuse stockpile.

Note that all armor and clothing stored in a refuse stockpile will suffer wear at an accelerated rate. This is a "feature" intended to dispose of unwanted armor.

Be careful on evil biomes, since some can reanimate dead creatures and body parts. If your fort is located on a map where part is evil and part is not, it is best to put your refuse stockpile on the part that is not evil.

The corpses of sentient beings (goblins, trolls, etc.) are no longer stored in refuse stockpiles, but in a corpse stockpile instead. If your dwarves are not cleaning up bodies, this is probably why.

### Sheets

This stockpile stores sheets, including paper and parchment. Like most stockpiles, it can use bins to consolidate items.

### Stone

Rough stone will be stored here, as well as ore. These stockpiles cannot use bins or barrels, but the use of wheelbarrows is strongly advised.

Stone management is a complex topic; in the simplest terms, most stones are extremely heavy, so you want to minimize the distance they are hauled by hand (e.g. from the stone stockpile to the mason's workshop or smelter) by putting such stockpiles very close to the workshops that they feed.

### Weapons

Weapons of all types are stored here by default, including picks, trap components, and weapons too large for dwarves to use. Bins can be used to consolidate weapons of any type.

### Wood

Chopped trees are brought to the wood stockpile before being used by carpenter's workshop, a wood furnace or siege workshop. Because wood takes a long time to haul and tends to travel a long way, the stockpile should be rather close to a fortress entrance (which does not necessarily mean on the upper z-levels - moving down one z-level is only one tile), unless you have an underground tree farm. It is a good idea to position this stockpile close to your carpenter's workshop (or the other way round) since he is likely to be the main "customer". Wood stockpiles will also accept "grown" wood logs that elves bring.

This type of stockpile cannot use bins or barrels.

### Additional Options

The options are "Allow Plant/Animal" (organic goods) and "Allow Non-Plant/Animal (non-organic goods). Unlike all the other categories, the Additional Options settings apply to all other active categories. A stockpile that allows neither organic nor non-organic goods will never receive any items. Disabling "Additional Options" is a common cause of stockpile problems, and these options generally aren't useful anyway.

### Custom stockpiles

With custom stockpiles, you can change which types of materials, goods, etc., can be stored in that stockpile. Any type of things can be mixed, so you could have a stockpile that will hold raw turtle, mechanisms and all stone types apart from onyx if you wanted, or only high-quality steel crossbow bolts (Ammo), all quivers (a Finished Good), and metal crossbows (a Weapon) - the combinations are endless, and can be finely tuned. Highlighting a stockpile with , then pressing will allow you to adjust the stockpile settings or in the menu you can press to adjust a custom stockpiles settings before placing it with . Note that many sub-menus consist of several pages ( the 'other' menu of stone e.g. consists of several pages while 'metal ores' and 'economic' consist of only one ).

Note that any custom stockpile that accepts any type of refuse will cause automatic degradation to all clothing and armor stored in that stockpile. It is highly advisable to store your shells and bones in a separate stockpile.

## Stockpile Settings

The **Stockpile Settings** screen is weird to use. In the first column are the major categories. In the second column there may or may not be subcategories. In the third you will see the individual items. The second and third columns are only visible when a category is enabled and selected.

You navigate this screen with and , and left and right on the arrow keys. and are used to enable and disable the categories. and are used to allow or disallow all the subcategories. and will permit or forbid individual subcategories. These six keys work no matter which column you have selected, though the last four will not always be available.\
will toggle individual item types.

Be careful when selecting 'block all' on the subcategories as it can make your stockpiles useless. For example, if you block all the furniture subcategories and then re-enable beds under types, the stockpile won't actually accept anything because it still registers all materials and all quality levels as forbidden. The correct way would be to 'forbid types' and then re-enable beds.

### Core Quality

Core quality means the quality of the *craftsdwarfship of the item*. A masterfully crafted armor (made from qualityless metal bars) has masterful core quality. A finely-crafted dress (made from an exceptional pig tail fiber cloth) has fine core quality (because the craftsdwarfship *of the item* is fine).

### Total Quality

Total quality means the highest between the craftsdwarfship of the item and the craftsdwarfship of its components (or decorations). The finely-crafted dress from our previous example has a fine core quality, but its total quality is exceptional because its component — a pig tail fiber cloth — is of exceptional quality. Likewise, a superior quality steel gauntlet, masterfully studded with copper is of masterful total quality (and superior core quality).

A more complex example: A rope reed fiber sock is superiorly decorated with pond turtle shell. Is masterfully crafted from a rope reed fiber cloth which was finely dyed with redroot dye. Core quality: masterful, Total quality: masterful. (Remember, for total quality, the best of either the item's quality, the quality of its components, or the quality of its decorations is chosen.)

See also Crafting Skills, Quality and Statistics research.

### Notes

Some categories will have a special extra type of item(s) that can be toggled with and sometimes .

| Categories | Item type                          |
|------------|------------------------------------|
| Animals    | Empty cages and Empty animal traps |
| Food       | Prepared food                      |
| Weapons    | Usable and unusable                |
| Armor      | Usable and unusable                |

If you disable an item or items that are already sitting in a stockpile then they become loose items and your dwarves will move them to a more suitable stockpile should one exist. All existing stockpiles (and zones) are listed under ooms.

## Custom Stockpile Uses

A custom stockpile is most useful for food, furniture, and bar/block stockpiles, to prevent your lye and venom sitting next to the kitchens, your floodgates and mechanisms near the rooms that need statues and doors, your stone blocks next to the forges, and your metal bars by the farms.

When setting up a custom stockpile to hold more than one type of raw material, it is often best to set up multiple custom stockpiles, one for each type. Otherwise your stockpile will invariably fill up with lesser-used items, rendering your custom stockpile nearly useless.

One use for this is to have an outdoor stockpile next to your gate that will accept all refuse except bones, shells, skins and skulls, and then one or more indoor pile(s) near your craftsdwarf's workshop that will **only** accept these things. If you have set the option for dwarves to gather refuse from outside, the bones will be brought in once all the meat has rotted off of any carcasses outside. This means added risk to your dwarves if they try to gather refuse that is far from your gate, and additional hauling.

Another effective use of custom stockpiles is Elven trading. Make a stockpile just for elf-safe trade goods: most categories where it is relevant have a 'materials' option. Note, however, that items with wooden decorations will **not** be excluded. Similarly, nobles who frequently mandate restricted trading can have their preferred goods stored separately, far away from the trade depot.

A highly efficient method is to have wood burning furnaces feeding into a 'charcoal only' bar/blocks stockpile, which in turn is near the smelting furnaces and forges. Bonus points if you also place a small wood stockpile near the wood furnaces.

Other good uses:

- Planter's stock: seeds and potash. If your ashery is nearby, include ashes and lye.
- Smelter stock: ores, flux and, unless you're using Magma smelter, coal.
- Sandpile: sand bags.
- Dyer's stock: a food stockpile that only includes dyes.
- Food Plus: a food stockpile that includes barrels. This spares your dwarves from carrying empty barrels to and from the furniture stores.
- Skins: a refuse stockpile limited to skins, a bit like the bone & shell stockpile above. Place near the tannery.
- Brewer's stock: brewable plants.
- Miller's stock: millable plants. (An empty bag stockpile will also speed up milling.)
- Refreshment stand: Since dwarves drink twice as often as they eat, having several small food stockpiles that only accept drinks scattered strategically through your fort can minimize smoko breaks. The usefulness of this kind of stockpile is often disputed as dwarves go to the fullest barrel first, so if you can't keep your stockpile constantly filled with new full barrels of alcohol your masons might decide to run all the way over to the alcohol stockpile you have set up for your brewers or your metalsmiths. If you can keep each stockpile constantly filled with fresh supplies of full barrels of alcohol then this can increase productivity greatly. A simple way of doing this is by keeping a brewery near each separate alcohol stockpile, or burrowing dwarves so that local stockpile is the only one they can path to.
- Artifact materials: The massive value and effectiveness of artifacts mean the materials used in them can have drastic effects, sometimes even into the *millions*. Having special stockpiles for high-value metals, stones, gems, and other such materials will make it that much easier to ensure that you will get the most out of each strange mood. (However, even with materials-specific stockpiles, it can take a fair amount of micromanagement to get a moody dwarf to use a specific material.)
- Artifact storage: Artifacts add a great deal to the created wealth of the fortress. Keep valuable artifacts safe in a special "treasure" stockpile.
- Ingredients: Store things that are cookable but not edible, like milk and quarry bush leaves, near kitchens. Also, more volatile foods (such as meat) can be stored closer to your kitchen to encourage your cooks to use them quickly.
- Mason's Stone: Linking a single- or limited-type stone stockpile to a mason's workshop allows you to specify exactly which stone your masons will use, providing consistent output (and increased value if using economic stone). Additionally, if your mason has a preference for a particular stone, you can increase output quality by having him work with that stone.
- Finished goods stockpiles near a Trade Depot that includes crafts that you want to sell, but excludes ordinary clothing, backpacks, waterskins, splints and crutches that you want your dwarves to use.

## Bugs

- Stockpile options don't work for cloth .
- Gem stockpiles' material option for clay is hidden in the UI .
- Marksdwarves may refuse to use ammo stored in bins.
- Hauling blocks access to items stored in containers; consider creating container-less "feeder" stockpiles linked to your storage stockpiles.
- Research has suggested that stockpiles are a significant cause of lag; see Quantum Stockpiles for designs that minimize stockpile tiles.
- Disabling "Additional Options" in the stockpile menu is a common source of stockpile problems.

## Troubleshooting

Getting dwarves to haul items to a stockpile is a frequent source of frustration. Here are some things to check:

- Do you have idle dwarves?
  - Do the idle dwarves have the appropriate hauling labors enabled?
  - Are the idle dwarves constantly taking and cancelling other jobs?
- Do you have a stockpile that wants this item?
  - Is there an empty spot in the stockpile?
    - Note that hidden items and wheelbarrows tie up stockpile tiles.
  - Can the idle dwarves path to the stockpile and the item?
  - Is the stockpile set to accept from anywhere, not just links?
  - Check both the item's type and its material, in stockpiles that can filter materials.
  - Check that the armor/weapon stockpile setting is "usable" and/or "unusable" as appropriate.
  - Check that "Additional Options" are set correctly to allow the desired items.
- Is the item unforbidden?
- Is the item accessible (no civilian alert, burrows, etc.)?
- Is the item not owned by any dwarf?
- Is the item not tasked for a job?
- Is the item not assigned for use in any buildings/constructions?
- Check your standing orders (o), and make sure this kind of item can be gathered.
  - For refuse, make sure dwarves are allowed to gather refuse that is "outside" (o r).
- Does the stockpile have wheelbarrows assigned? If so, are they all in use?
- If the item normally goes in a container, do you have suitable unused containers?
- Is the item claimed by a location (hospital, tavern, library, temple)?
