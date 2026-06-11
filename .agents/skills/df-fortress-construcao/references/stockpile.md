# Stockpile

> Fonte: [Stockpile](https://dwarffortresswiki.org/index.php/Stockpile) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

*For exploits related to stockpiling, see Quantum stockpile.*

**Stockpiles** are where dwarves store items of various types, usually in a safer, closer or more convenient place for the consumers. Dwarves with the corresponding "hauling" job will seek out items that are not already on a stockpile that accepts them and carry them to an appropriate stockpile, if available. It's important to place your stockpiles carefully to minimize the amount of time spent carrying items back-and-forth. Items in a stockpile may be stored in containers such as bags, barrels or bins (see Using bins and barrels). Seed bags, flour bags, and dye bags can go inside barrels. Empty bags, however, cannot be stacked.

## Creating and Removing Stockpiles

To create a stockpile, click the pStockpile button. At this point, you can click on any existing stockpile to inspect it, but to create a new one, you must click the button that appears immediately above the original stockpile button. When you click to create a new stockpile, you can draw a rectangle with the mouse. Clicking "Accept" in the top left pop-up finalizes the stockpile, or you can continue drawing rectangles to make the stockpile bigger. Non-contiguous regions are possible, but could be confusing to manage later for little benefit. If the chosen area has parts that cannot be made into a stockpile, like a wall, a workshop, or an already existing stockpile, a stockpile will be created but they will not be part of it. After clicking "accept", a new menu pane opens up with a list of pre-set stockpile rules, of which you must select one or else select "Custom" to define your own rules.

When creating a stockpile, any movable items (e.g. loose stone, unbuilt furniture, etc.) currently occupying the designated tiles will automatically be considered part of the stockpile, even if the stockpile settings disallow those particular items. These items also mark the tile as "full", so no new items will be stored in that tile until all the original items in the tile are moved. To handle unwanted items, you can specify that the stockpile "gives" to a workshop or stockpile that will accept those items, or use a dump command to have them carried off to a garbage zone.

To edit a stockpile, click the "Stockpile" button in the main menu, then click on the stockpile. The suite of buttons (mouse over to see their tooltips to determine what each button does) can be used to edit the name, edit its boundaries, set which stockpiles or workshops give to or receive from this stockpile, delete the stockpile, or set the amount of wheelbarrows and containers that can be used.

When you click to repaint the stockpile, note that a secondary toolbar appears at the bottom of the screen, which you can use to switch to eraser mode.

## Using stockpiles

Once a stockpile has been allocated, by default dwarves will automatically move items to the stockpile when they are available, as long as the stockpile has available space. Note that the dwarves will place the item into the empty spot that is nearest to the item, *not counting any obstructions*\[Verify\]. Dwarves will stockpile the *newest* item first, which may not necessarily be the nearest item to the stockpile. Tiles within a stockpile which contain only forbidden items are considered available space, and can accumulate another item without exploiting quantum stockpiling.

One method to ensure a workshop has raw material on hand is to place a small stockpile of its input materials next to the workshop. This will speed up production as the crafter only has to take a few steps to obtain the material, preventing them from dragging material across the entire map. Whenever a crafter picks up material from the stockpile, your hauling dwarves will automatically fetch more material to refill the stockpile. This speeds up a queue of jobs, as other dwarves perform the time-consuming distant haul whilst the crafter concentrates on actually making items.

It's not necessary to place stockpiles for all types of objects. If no storage is available for a certain item type, dwarves will seek out items wherever they might lie as mentioned earlier. This can be advantageous—if you don't have a stockpile for gems, your jeweler will go pick up fresh gems without waiting for them to be carried to a pile first. However, this also means your jeweler has to spend a lot of time fetching the gems. If you have enough haulers available, it's generally more advantageous to designate stockpiles than not. Also remember that your workshops will get cluttered and suffer production slowdowns if you let ridiculous numbers of items pile up in them, so it's important to occasionally clear out workshops if they get cluttered. This can be done either by having a stockpile available so that haulers will remove the items, by quantum stockpiling the accumulation, or by removing and rebuilding the workshop, which will empty its contents onto the ground.

## Give and/or take from a stockpile/workshop

Another feature of stockpiles allows you to tell dwarves to transfer items from or to one stockpile and/or workshop to another. The button that controls that feature is , which is on by default once a stockpile is created. When this button is activated, the stockpile will take designated items from anywhere, but if disabled, it will only give and take items from specified workshops and stockpiles. Your chosen stockpile will now list the stockpile it will take from. This will cause items in the second stockpile to be hauled to the first stockpile. The button next to the previously mentioned one is , which allows the player to select where a stockpile's items will be given to or taken from, which are chosen with  and

Each stockpile can take from any number of other stockpiles. You can't make two stockpiles feed into each other, although larger loops (e.g. three stockpiles that feed into each other in a circle) are allowed.

When having a stockpile take items from a workshop, any items produced inside the workshop become eligible to move to the stockpile. Be aware that any items produced in the workshop that *aren't* accepted by the linked stockpile will not be moved anywhere at all. They will sit inside the workshop until a linked stockpile accepts them.

Enough micromanagement will allow for effective and (relatively) streamlined supply chains. Here are some examples:

- Speeding up lumber harvesting, carpentry, *and* ash and charcoal production by putting several wood stockpiles near the various tree-felling areas, then one large "primary" stockpile near the carpenter's workshop that takes from those small ones, and then finally, a small stockpile near the wood furnace that takes from the primary one.
- A smallish plant stockpile near your farms, disallowing barrels, will allow harvesters to spend very little time stockpiling the crops they just picked. A larger stockpile near the still (this one possibly allowing barrels), taking from the smaller stockpile, lets your general-purpose haulers do most of the grunt work of getting plants in place for the brewer. The larger stockpile should be set to "take from links only", so the harvesters do not waste their time.
- A clothier's shop produces high-quality new clothing. There is currently no way to stockpile *only* new clothing, as opposed to worn clothing, except for the fact that the new clothing is sitting in its workshop. A stockpile can be set to take from the clothier's shop (and to "take from links only"), so that it only gets new clothing produced in that workshop. If another stockpile with "take from anywhere" and no links is created, that one will accept all the worn clothing - it will never take from the linked clothier's shop. This worn-clothing stockpile may be placed near the trade depot, if you plan to sell the used clothing, or near the garbage disposal, if you do not.

When giving to a stockpile, an equal and opposite "take from stockpile" is created in the other direction (and vice versa). Deleting one of these inter-stockpile links also deletes the other link.

Specifying that a workshop or furnace will only get its materials from a certain stockpile provides a way to make sure everything that the workshop produces is of a specific material. For example, setting a granite stockpile to give to a mason's workshop ensures that the workshop will only use granite as its material. This is also extremely important when the workshop's input materials are heavy (e.g. stones); linking a nearby stone stockpile to the workshop prevents the mason from hauling an enormous rock from hundreds of tiles away.

This option is quite powerful, but should be used **very** carefully as the linked workshop will now *only* take from the stockpiles set to give to that workshop. Make sure that the workshop gets *all* of the materials needed for its jobs there if you use this feature. For example, if you link your ore stockpile to a non-magma smelter, but don't also link a stockpile that includes a fuel source, then the dwarves will be unable to smelt ores at that smelter due to a lack of fuel. If you set a fuel stockpile to give that smelter, it will still be unable to melt down items marked for melting, because it only takes from the ore and fuel stockpiles. Another common mistake is setting a plant stockpile to give to a still, but forgetting to also link a furniture stockpile to the still so that it has access to barrels.

## Max bin/barrel/wheelbarrows

The *max bin*, *max barrel* and *max wheelbarrows* settings control the number of barrels, bins and wheelbarrows that are used for the organisation of items inside the stockpile. It can be useful to disallow bins and barrels from some stockpiles, for example stockpiles used to store seeds or for quantum stockpiles, by reducing this setting to 0.

Increasing these numbers is not usually needed - they are set to the number of tiles in the stockpile when it is created, which is the maximum number of bins or barrels the stockpile can hold anyway. Which of bins or barrels is turned on is determined by the item type selected when the stockpile is designated - food stockpiles allow barrels, for example, and bar stockpiles allow bins. However, these settings are not updated if the types of items allowed in the stockpile are changed. If you change the types of items allowed in the stockpile, it may also be useful to change the number of bins and barrels that are allowed in it to allow your dwarves to store those items more efficiently.

## Stockpile categories

### Ammo

This stockpile contains ammo for all forms of ammunition-requiring weaponry (except siege engines). It can use bins to consolidate stacks.

### Animal

Animals stored in cages that are not affixed to a location will be stored in these stockpiles. Traps used for capturing wild animals and empty cages are also stored here.

This type of stockpile cannot use bins or barrels.

### Armor

Armor of all types is stored here. There is no preference for specific body parts, but usable/unusable armor may be specified. All types of armor can be stored in bins.

### Bar/Block

Bars of smelted metal and blocks of cut stone and glass are kept here after being processed by the smelter, mason's workshops, and glass furnaces, before being used for other purposes. Weirdly, ashes, potash, soap, charcoal, and coke from the wood furnace, ashery, soap maker's workshop and smelter will also be stored here. As with all stockpiles, this can be changed to allow for specific blocks and bars to be stored with custom settings. Bins can be used to consolidate up to 10 bars/blocks.

Bars of fuel *(Coke and Charcoal)* are stored in **Bars: other materials-\> Coal**

### Cloth

Woven cloth and thread are stored here (plant fiber, animal hair, and silk). Bins can be used to consolidate items.

### Coins

Minted coins are kept here, several thousand of them fitting into a single bin.

### Corpses

Dead sentient beings (dwarves, goblins, trolls, etc.) and pets that have no burial location will be placed here. Other corpses are considered part of the *refuse* category.

If placed indoors, decaying bodies will generate miasma, but bones will not be removed at the end of the season. Rotting pets or friends give dwarves unhappy thoughts unless they are given a proper burial in a burial receptacle.

Corpse stockpiles are meant to be used as *morgues*, though the inclusion of invader corpses makes this slightly difficult.

### Finished Goods

Finished goods created by the craftsdwarf's workshop, as well as the clothier's shop and the leather works, are placed here before being used in trade or other uses. This type of stockpile can use bins to consolidate items, over a hundred objects can fit into a bin.

Since this stockpile can also contain supplies that the player might not want to trade away (splints, crutches, ropes, waterskins...), it is wise to make separate custom stockpiles for these goods.

While not explicitly mentioned, the Tool subcategory includes the following items:

- Scroll rollers
- Book binding
- Hive
- Honeycomb
- Quire
- Die
- Jugs
- Nestbox

### Food

As one would assume based on the name, food is stored here, in addition to a wide variety of inedible plant and animal products -- seeds, lye, giant desert scorpion venom, bags of dye, and liquid fire, to name a few. Raw fish is brought here, before being processed by a fishery and turned into edible meat. Drinks are always stored in barrels or large pots. Seeds are stored in bags (which may in turn be stored in barrels/pots); other food items can be stored in barrels or pots.

Barrels and pots can hold, at most, 60 prepared meals. Stacks larger than that (☼Dwarven Beer Roast \[200\]☼ is possible) will not fit in a barrel, but will still only take up one tile of stockpile space. To free up barrels, you may decide to have separate prepared food stockpiles that do not accept barrels - if you cook larger meals, this shouldn't be a problem.

Food will never spoil while in a stockpile, although it may attract and be eaten by vermin. Food stockpiles should, in most cases, be restricted to desired types (e.g. seed stockpiles or meat stockpiles or unprepared fish stockpiles); there are simply too many things that go in them.

Fat and tallow go in the same list and are listed by animal. To separate out just the tallow, search for "tallow" and click all/none for the column. This button only applies to displayed items. Resetting the search will show that tallow has been allowed/forbidden, but fat settings are unaffected.

Fish that have been caught but not cleaned are stored in **Unprepared fish**. Fish that have been cleaned *(via Prepare a raw fish at a* fishery) are stored in **Fish**.

Read more about the following food stockpile categories here:

- Plants
  - For edible plants, see Crops
- Seeds
- Fruit / Leaves
- Milled plant

### Furniture Storage

Completed items from the carpenter's workshop, mason's workshop, and mechanic's workshop will be stored here, along with furniture created from other shops, until placed or used in another building. Bags filled with sand can also be stored in furniture stockpiles, and in fact will appear in any furniture stockpile unless expressly forbidden, regardless of materials permitted.

Since this is a very broad category, it may be useful to create stockpiles for a specific type of item (like barrels, bags, bins, mechanisms) via the stockpile settings.

Furniture cannot be stored in barrels or bins.

If you choose to apply advanced stockpiling of furniture e.g. "make a stockpile for only Furniture\>Beds." Merely selecting "beds" under the "Type" category will not suffice. In this case one also needs to ensure the required qualities are selected! Should you want to store all quality beds, just make sure you select "all" on the categories: Core Quality as well as Total Quality.

Anvils, millstones, and querns are stored as furniture, even though they are a core component of a workshop.

Siege engine items are also stored in this stockpile:

- Ballista parts
- Bolt thrower parts
- Catapult parts
- Ballista arrow
- Ballista arrowhead

#### Other Large Tools

While not explicitly mentioned, the following items are stored in the "Other large tools" subcategory:

- Bookcase
- Pedestal
- Altar
- Stepladder
- Display case

### Gem

This stockpile stores gems and raw glass, both cut and uncut, along with gizzard stones. It can use bins to consolidate gems.

### Leather

Leather, which is produced at a tanner's shop, will be kept here. Like most stockpiles, it can use bins to consolidate items.

### Refuse

Since dwarves hate rot, because of the miasma it spreads when in an enclosed place like a cave, any garbage item that can rot will be stored in a refuse stockpile. Also, any XXdamaged itemsXX will be moved to the refuse stockpile. Many players prefer to place this stockpile outside their cavern, usually a small distance from the entrance, as rottable items on tiles that are Outside Light Above Ground do not generate miasma.

If placed on a Subterranean tile, decaying items will generate miasma, which will spread through your fortress and generate a small unhappy thought in any dwarf passing through it. For this reason, it is sensible to build doors (preferably several, separated by a few tiles to create an airlock) to all of your indoor refuse stockpiles. Miasma won't spread through a closed door, so only dwarves with business in the room will be bothered by the rot.

An alternative to this is to dig channels down from the surface, creating an area of tiles considered to be Light Above Ground, yet still located within your fortress. You can place your refuse stockpile here, and although it will be in your fort, rotten items on those tiles will not generate miasma. If you choose to cover them with walls or floors for security and/or aesthetic reasons, it will convert them to Inside, but they will remain Light Above Ground tiles, which again do not generate miasma in rotten items. (For even more creative methods to restrict the spread of foul rotting stench, see the miasma page.)

Bones, skulls, and shells are also stored here, whether from defeated enemies or raw food processing - if left in an area with high vermin levels, these will randomly disappear. Refuse stockpiles can be restricted to store only bones, skulls, shells, teeth, and horns/hooves.

Note that a refuse stockpile is not the same as a garbage dump - a garbage dump is only for things manually marked to be dumped. Additionally, refuse types specifically marked as **Dwarves Dump** *refuse type* will be hauled to the garbage dump instead of the refuse stockpile.

Be careful on evil biomes, since some can reanimate dead creatures and body parts. If your fort is located on a map where part is evil and part is not, it is best to put your refuse stockpile on the part that is not evil.

The corpses of sentient beings (goblins, trolls, etc.) are no longer stored in refuse stockpiles, but in a corpse stockpile instead. If your dwarves are not cleaning up bodies, this is probably why.

### Sheets

This stockpile stores sheets, including paper and parchment. Like most stockpiles, it can use bins to consolidate items.

### Stone

Rough stone will be stored here, as well as ore. These stockpiles cannot use bins or barrels, but the use of wheelbarrows is strongly advised. The default number of assigned wheelbarrows is 1, also if the number of assigned wheelbarrows is set to zero and the custom stockpile setting is entered, upon exiting the custom stockpile settings, the number of assigned wheelbarrows is reset to 1 (from zero), that happens even if no changes in the custom stockpile settings has been made.

Stone management is a complex topic; in the simplest terms, most stones are extremely heavy, so you want to minimize the distance they are hauled by hand (e.g. from the stone stockpile to the mason's workshop or smelter) by putting such stockpiles very close to the workshops that they feed.

### Weapons

Weapons of all types are stored here by default, including picks, trap components, and weapons too large for dwarves to use. Bins can be used to consolidate weapons of any type.

### Wood

Chopped trees are brought to the wood stockpile before being used by carpenter's workshop, a wood furnace or siege workshop. Because wood takes a long time to haul and tends to travel a long way, the stockpile should be rather close to a fortress entrance (which does not necessarily mean on the upper z-levels - moving down one z-level is only one tile), unless you have an underground tree farm. It is a good idea to position this stockpile close to your carpenter's workshop (or the other way round) since he is likely to be the main "customer". Wood stockpiles will also accept "grown" wood logs that elves bring.

This type of stockpile cannot use bins or barrels.

### None

This type of stockpile does not allow any items in the stockpile, so no items will ever be hauled to that stockpile, but all items, which are on stockpile tiles, when the stockpile is created, are automatically considered part of the stockpile. Such stockpiles can be used to ie. clear an area of non-economic stones, after the stockpile has been set to give to a stoneworker, mechanic's or craftdwarf's workshop, by turning the non-economic stones into other useful goods (like stone furniture, rock mechanisms or stone crafts and mugs), leaving the economic stones (and not allowed non-economic stones under the stone uses standing orders) behind, at which point the stockpile category should be changed (and the stockpile link should be updated) to give the rest of the stones to some other stone stockpiles. If a (none) stockpile is used for such a purpose, the workshop to process stones should be designated to build first, afterwards (before the workshop is constructed), the none stockpile can be created (around the workshop) and the link to (give to) the (yet to be completed) workshop can already be set up.

### Additional Options

The options are "Allow Plant/Animal" (organic goods) which appear as  or  and "Allow Non-Plant/Animal (non-organic goods) which appear as  or . Unlike all the other categories, the Additional Options settings apply to all other active categories. A stockpile that allows neither organic nor non-organic goods will never receive any items. Disabling "Additional Options" is a common cause of stockpile problems, and these options generally aren't useful anyway unless you want to consolidate trade goods which are safe to trade to Elven caravans.

### Custom stockpiles

With custom stockpiles, you can change which types of materials, goods, etc., can be stored in that stockpile. Any type of things can be mixed, so you could have a stockpile that will hold raw turtle, mechanisms and all stone types apart from onyx if you wanted, or only high-quality steel crossbow bolts (Ammo), all quivers (a Finished Good), and metal crossbows (a Weapon) - the combinations are endless, and can be finely tuned. Note that many sub-menus consist of several pages ( the 'other' menu of stone e.g. consists of several pages while 'metal ores' and 'economic' consist of only one ).

## Stockpile Settings

In the **Stockpile Settings**, the first column are the major categories. In the second column there may or may not be subcategories. In the third you will see the individual items. The second and third columns are only visible when a category is enabled and selected. Any option can be selected in any category by simply clicking on it. Each column has an "All" or "None" button, which will enable or disable entire categories so that the player does not have to individually click each option to enable or disable an entire list.

Be careful when selecting 'block all' on the subcategories, as it can make your stockpiles useless. For example, if you block all the furniture subcategories and then re-enable beds under types, the stockpile won't actually accept anything because it still registers all materials and all quality levels as forbidden. The correct way would be to 'forbid types' and then re-enable beds.

### Core Quality

Core quality means the quality of the *craftsdwarfship of the item*. A masterfully crafted armor (made from qualityless metal bars) has masterful core quality. A finely-crafted dress (made from an exceptional pig tail fiber cloth) has fine core quality (because the craftsdwarfship *of the item* is fine).

### Total Quality

Total quality means the highest between the craftsdwarfship of the item and the craftsdwarfship of its components (or decorations). The finely-crafted dress from our previous example has a fine core quality, but its total quality is exceptional because its component — a pig tail fiber cloth — is of exceptional quality. Likewise, a superior quality steel gauntlet, masterfully studded with copper is of masterful total quality (and superior core quality).

A more complex example: A rope reed fiber sock is superiorly decorated with pond turtle shell. Is masterfully crafted from a rope reed fiber cloth which was finely dyed with redroot dye. Core quality: masterful, Total quality: masterful. (Remember, for total quality, the best of either the item's quality, the quality of its components, or the quality of its decorations is chosen.)

See also Crafting Skills, Quality and Statistics research.

### Notes

Some categories will have a special extra type of item(s) that can be toggled.

|  |  |
|----|----|
| Categories | Item type |
| Animals | Empty cages and empty animal traps |
| Food | Prepared food |
| Weapons | Usable and unusable weapons |
| Armor | Usable and unusable armor |

If you disable an item or items that are already sitting in a stockpile, then they become loose items. Your haulers will move them to a more suitable stockpile, should one exist. All existing stockpiles (and zones) can be seen with P and viewing the "Zones" and "Stockpiles" tab.

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
- Stone carver's stone: Linking a single- or limited-type stone stockpile to a stoneworker's workshop allows you to specify exactly which stone your stone carvers will use, providing consistent output (and increased value if using economic stone). Additionally, if your stone carver has a preference for a particular stone, you can increase output quality by having him work with that stone.
- Finished goods stockpiles near a Trade Depot that includes crafts that you want to sell, but excludes ordinary clothing, backpacks, waterskins, splints and crutches that you want your dwarves to use.

## Bugs

- Gem stockpiles' material option for clay is hidden in the UI Bug:9749.
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
