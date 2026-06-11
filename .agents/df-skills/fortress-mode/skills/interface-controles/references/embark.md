# Embark

> Fonte: [Embark](https://dwarffortresswiki.org/index.php/Embark) — Dwarf Fortress Wiki (GFDL/MIT)

**Embark** is the time at the very beginning of Fortress mode before actual gameplay begins (but after generating a world), when you and your initial 7 dwarves:

1.  Choose a site.
2.  Assign starting skills to each dwarf.
3.  Select an initial load of supplies and equipment.
4.  Arrive at the site with your wagonful of supplies.

## Choosing a Site

The main considerations to keep in mind when choosing a site are: the presence of aquifers, the availability of wood, ores, and soil, the climate, and your neighbors. There is just ONE BIG RULE: when your home civilization is too small, you will recognize after the second winter that you won't get any more immigrants, which can be extremely fun. To avoid this situation, select a home civilization with *at least* two dwarven sites on the map.

The Choose Fortress Location screen shows four separate sections, with three of them being views of the land at different levels of magnification: Local, Region, and World. A section of highlighted tiles in the Local view indicates the current embark location within the region. The local view constitutes a 16×16 grid of embark area tiles (each representing 48×48 tiles when you are playing the game) that is within a single region tile. The world map cannot be directly controlled, and exists only to give you the overall view of where, relative to the rest of the features of the world, the region map is focused on.

Currently, an embark must be entirely within a tile on the "Region" view. This restriction will be removed in the future. 1

The arrow keys control the X cursor in the center "Region" view while , , , and move the embark location around within the Local view. , , , and will resize the embark location.

The size of the embark location directly affects how much data about a map the game will have to store in your computer's memory and the size of your save files. This may correspondingly make pathfinding more resource-intensive, generally slow your game down, and have a dramatic effect on the save and load times for your map. As such, smaller maps are recommended, especially for less powerful computers. Remember that each tile on your embark screen is 48×48 tiles large.

On the far right of the screen is a list of local features in the dominant biome. Individual biomes, which form at least one map-tile of your embark location, can be cycled with the -keys; for example, an area with 3 biomes present can be cycled using , and . The selected biome will be highlighted with flashing Xs on the Local Map, and the biome's information will be displayed on the right side of the screen.

### Biomes

A **biome** is a biotic area with homogeneous features, characterized by distinctive plants, animal species and climate.

In the above image, the biome is "Temperate Savanna", and the region the biome is part of is given a specific name: "The Velvety Hill", part of the continent "The Jade Horn-Land".

Biomes will also contain only one set of stone layers, though these usually expand beyond a single biome. Your dwarves will find different resources depending on which biomes they select when starting a fort.

Biomes are important when choosing a fortress location, in order to understand your surroundings. When there's more than one biome in the embark location you'll be able to press F1, F2, etc to see their specifics.

#### Climate

Climate determines the maximum temperature range of the region, which in turn impacts the severity of exposure to the outside, whether water will freeze in winter, and how quickly water evaporates.

The climate is displayed as "Temperature: Warm" in the above image.

Very hot and very cold biomes bring their own challenges, which may be further compounded with overlapping features, such as a glacier being frozen for half the year, being devoid of trees, and lacking a river. Very hot climates may see all their surface water quickly evaporate, making finding a water supply more dangerous, as underground caves filled with hostile creatures may be the only supply of water.

#### Plant Life

Seen in the above image as "Trees: Sparse" and "Other Vegetation: Moderate".

Trees are useful for the wood they provide, and wood is a basic building material, important for being the only material that can be used to create beds. Also, because creating bins and barrels from metal is an involved process involving more steps, less common resources, and fuel, wood is often preferred for making these items as well. Wood is also a source of charcoal, one possible fuel used to make metal products in standard smelters and forges and required for making steel even when you have magma forges. Wood is also useful in making potash, for soap or fertilizing farms.

Despite wood's many uses, it is entirely possible to play without any trees in your biomes. Due to the inexpensive nature of wood, it is possible to simply embark with a large quantity and rely on trade caravans from the elves, humans, and dwarves for your wood needs. Also, at a certain point, trees can be farmed in muddied underground areas regardless of how barren the surface is.

Shrubs can provide some quick food through the herbalist skill, brewable materials, and seeds for some very helpful above-ground crops which are generally only available through trading with Elves.

#### Surroundings

Surroundings affect how powerful and hostile local wildlife will be, and some forms of plants are available only in specific types of surroundings.

The surroundings of the example image are listed as "Surroundings: Wilderness".

Any biome can have any set of surroundings; for example a glacier could be haunted, wilderness or mirthful. However, a named region (which is a contiguous area of one category of biomes, such as forests or wetlands) will be either good, neutral, or evil.

There are two axis for surroundings: savagery and alignment. Calm and neutral savagery are functionally identical. Savage lands are like normal lands, except they will frequently have giant or hostile humanoid versions of normal animals. For example, you might have a Tigerman instead of "merely" a tiger in a savage jungle.

Good biomes are similar to neutral biomes, except have more fanciful (and generally benign) creatures like pixies, fluffy wamblers, or unicorns, and are generally no more dangerous than neutral biomes. Evil biomes are home to many dangerous creatures, often dead vegetation and even including undead versions of normal creatures, making for a far more hostile environment specifically for players who want to face a greater challenge to stay alive, especially early on. Trees might not grow in an evil area.

It is possible to start a fortress that overlaps multiple alignment types (for example good, evil, savage, and benign). Some players consider this desirable, as it provides diversity in your little corner of the world, but it also has its dangers in the form of more ferocious wildlife.

#### Layers

At the bottom right of the biome view, some of the main features of the site are reported. You will be told whether the biome has a layer of soil on top of it (and how thick it is), and whether that soil includes clay. Deep soil layers make underground farming extremely quick to set up, as no irrigation will be needed. If there are metal ores, *Shallow metal(s)* and/or *Deep metal(s)* are reported. Metals count as "shallow" if they are within the first two stone layers, unless the biome is a Shallow Ocean (shows "little soil") or a Sand Desert, in which case it counts the first five stone layers as "shallow". Flux is also reported if present.

The depth of the soil layers is indicated by light brown text: *Little soil*, *Some soil*, *Deep soil* or *Very deep soil*. Clay is reported as either *Shallow Clay* or *Clay*. Sand is *not* reported here; the only way to be sure you'll have sand is to embark on a Sand Desert. (Note that DFHack's \`\`embark-tools\`\` plugin can be used to add a sand indicator.)

You won't be told which kinds of metals are present. Your best bet for finding the raw materials for making steel is to look for a site with *Shallow metals* (note the plural) and *Flux*. A biome with shallow metals listed has an extremely high chance of containing iron-bearing ores in a sedimentary layer near the surface. Failing that, you're practically guaranteed to get some copper ore (tetrahedrite).

#### Aquifer

An aquifer is a layer of soil or stone saturated with water, and a biome may contain up to 3 aquifer layers (theoretically more, but such would be rare to say the least). Embarking on an aquifer brings up a warning before embark as an aquifer can significantly raise the difficulty of starting a fort. For specific tactics on working with an aquifer, see *Aquifer*.

### Changing Views

Pressing will cycle the presented information through a variety of different views and panels.

- Neighbors - other civilizations that are closest to your current location. Proximity increases the chance of interaction, though at present this largely means "nearby goblins are more likely to attack you." If any race is not represented on this page, it means that the civilization cannot reach you if you are in that location. Embarking on an island, or a location completely surrounded by mountains will make it impossible for any civilization but your own dwarven civilization to reach you, as world map travel across oceans or mountains is impossible. If not even "Dwarves" appears, it means that your home civilization is dead, and there will be no immigration waves or trade caravans from your home civilization. If this is the case, it is recommended you change to a still-existent civilization unless you want the challenge of having no support from the mountainhomes. Races that are hostile to you are represented by a series of red "-" marks or "WAR". The latter means you will get sieged by that race, while "------" stands only for diplomatic hostility (usually from baby snatching in worldgen). They'll still siege (eventually), and the first time they do will constitute a declaration of war. In vanilla DF, goblins are always hostile, but humans or elves may also be at war with particular dwarven civilizations.
- Your Civilization - indicates all dwarven civilizations in the world. and will cycle through the civilizations allowing you to choose which your settlers will be embarking from. Civilization choice will affect who is at war with you, what goods are available for trade and at embark, who your regent will be (considering one might be surprised by who turns out to be one's regent), and if there are any surviving members of your civilization left to migrate to or trade with your fort. Some of this information is only viewable in Legends Mode, but you can view accessible goods and materials after hitting mbark by looking at what items you can choose to embark with. If you don't like the options, simply to get the main menu and choose Abort Game. You will have to find the site again, but it saves you from needing to abandon the fortress.
- Relative Elevation - Shows the land height relative to the lowest point in the region.
- Cliff Indicator - Shows the severity of cliffs. With the exception of rivers that cut through mountains, even apparently very steep cliffs will still have ramps that make it perfectly accessible for any creature or even the wagons in caravans (unless you have turned erosion off).

### Reclaiming a fortress

If you reclaim the site of an abandoned fortress, upon arrival you may see goods, materials, and corpses left from the previous effort. These items will initially be forbidden and you will have to reclaim items before your dwarves will acknowledge their existence, for example to haul them to a graveyard or refuse stockpile.

## Creating Your Settlers

### Play Now!

You can forgo the process of assigning skills and supplies and instead select **Play Now!** This option will give you a selection of dwarves, with the following profiles:

- Miner: Adequate Miner
- Woodworker: Novice Carpenter, Bowyer
- Woodcutter: Novice Wood Cutter, Furnace Operator, Wood Burner, Grower, Herbalist, Brewer, Cook, Lye Maker, and Potash Maker
- Stoneworker: Novice Mason, Engraver, Building Designer, and Mechanic
- Jeweler: Novice Stone Crafter, Wood Crafter, Bone Carver, Gem Cutter, and Gem Setter
- Fisherdwarf: Novice Fisherdwarf
- Fish Cleaner: Novice Weaver, Clothier, Butcher, Tanner, Leatherworker, and Fish Cleaner

One of these will be randomly flagged as Expedition Leader at the start. The default embark value for a custom embark is 1504 embark points. Either 1104 or 1304 points are spent in pre-chosen goods (depending on if an iron or steel anvil is used), 54 points in dogs and cats, and 200 or 400 unassigned (depending on if a steel or iron anvil was given). The Play Now! embark only uses either 1158 or 1358 points. While a Play Now! embark is no more doomed than any other embark, it is always better to Prepare Carefully once you know what you're doing with the set up of an early fort.

### Prepare Carefully

Preparing allows the player to customize their embarking party and supplies by spending a pool of points which is shared between skills and equipment, with each skill rank and equipment item having a set value. The total value of embarking is set at 1,504 points, though all but 200 or 400 of these are pre-spent on an array of basic equipment (the same equipment Play Now! uses). It stands to reason that one should try to maximize the value of their embark by spending all available points. By preparing carefully it is also possible to name your fortress and your embark group.

It is possible to change the amount of available embark points when playing via advanced world generation, where presets can be created and/or customized. The maximum amount of embark points a generation setting can have is 10,000. With DFHack, the command \`\`points \[#\]\`\` (with "\[#\]" being any number) will set the amount of available embark points to the specified number.

#### Using the menu

Use to switch between selecting Skills and Items. Use the 4 directional keys or number pad to navigate to highlight the different choices/columns, and or to choose more or less of the highlighted item or skill. When viewing items, hit to go to a menu for any "new" items, that are not currently listed, including any you removed by reducing the number to 0; select the item, hit , then increase the number desired as above ( or ) in the main menu.

If you cannot buy additional skill levels, you are out of points and must return some items for additional points. Higher-priced items will automatically be removed from view when selecting new items if you do not have enough points for those selections, showing only what you can afford with your current points.

#### Skills

At embark, all seven settlers begin with no rank in all skills. Each dwarf can be assigned 10 additional ranks to be allocated however you please among the entire Dwarven skill list – including military – with the restriction that no single skill can be increased beyond 'proficient' (level 5). Therefore, you can trade off specialisation against versatility: each dwarf may be 'proficient' in two skills, or minimally skilled (rank 1, 'Novice') across 10 skills, or anything in between. Not all ranks need be allocated, and since ranks cost points there is a further trade-off to be made against other uses of embark points. The current skill rank is shown to the left of the skill (e.g. Novice), while the point cost of the next rank increment is displayed at the right; novice rank costs 5 points and each subsequent rank costs one additional point (so Adequate costs 6 points, Competent costs 7 points, and so on). Reaching 'Proficient' thus costs a total of 35 points. The most expensive allocation is granting all settlers 'proficient' in two skills; this costs a total of 490 points, which is nearly a third of the total budget. By contrast, allocating each dwarf 'novice' in 10 skills costs only 350 points.

Although this is already fairly involved, between the long skill list and the floating cost, the value of a rank is subject to further scrutiny given the early-game value, or lack thereof, of certain skills as well as the relative ease or difficulty of training ranks in a given skill. Many skills are performed just as well by a Novice (skill level 1) or even a Dabbler (level 0) as they are by a Legendary (level 15+). A Novice Furnace Operator won't produce Coke as fast as a Legendary Furnace Operator, but they will produce it fast enough to keep their neighbor smelting hematite until the cows come home. Additionally, embarking with Novice or higher skill will automatically enable the corresponding labor, avoiding manual labor assignments upon arrival.

For a more complex example, there is much overlap between what can be produced out of wood and what can be produced out of metal, but wood is plentiful in the early game (often throughout, if a tree farm is established, and caravans will bring in several pages worth of wood if you request it) while metalworking can take much longer to establish, or would take several times longer to produce a given product in the early game due to the multiple steps required. Metalworking skills also train slower than woodworking, and metal products have a longer base production time than wood products.

From one point of view, the Woodworking skills would be of more immediate use in producing quick goods of higher value in the early game, especially given the high volume needed; however furniture quality is of little concern in the early game, and the high volume of value-independent goods (such as barrels which you won't be trading away on their own or using to furnish chambers) will cause your carpenter to train his skills fairly quickly. Even on a strictly functional level, a Novice carpenter can produce beds, barrels, and bins fast enough to keep up with a fledgling base. Lastly, once metal production is up and running, it can be agonizingly slow if a Farmer or Peasant has to be reassigned to learn from scratch, thus a proficient Metalsmith stands to pay off much more in time than starting with a proficient Carpenter. Consider as well that you may receive a highly skilled Metalsmith during an immigration wave, if you care to take that chance.

#### Supplies

The default array of supplies covers a broad range of foodstuffs, seeds, drink, tools, and medical equipment, and is reasonable, though extra food and drink never hurt anyone.

:\* 2 Copper picks

:\* 2 Copper battle axes

:\* 1 Iron anvil (or steel anvil if your home civilization has no access to iron)

:\* 1 Wheelbarrow (if possible)

:\* 1 Stepladder

:\* 60 units dwarven alcohol (at least 20 each of up to 3 random types, in 12 barrels)

:\* 6 bags containing 5 seeds of each of dimple cup, cave wheat, plump helmet, sweet pod, pig tail, and quarry bush.

:\* 15 units of meat (one random type, 3 stacks of 5 units in 1 barrel)

:\* 15 units of fish (one random type, 3 stacks of 5 units in 1 barrel)

:\* 15 units of plump helmets (3 stacks of 5 units in 1 barrel)

:\* 5 pig tail fiber thread

:\* 5 pig tail fiber cloth

:\* 5 pig tail fiber bags

:\* 3 pig tail fiber ropes

:\* 3 leather quivers

:\* 3 wooden buckets

:\* 3 wooden splints

:\* 3 wooden crutches

:\* 2 female dogs†

:\* 2 female cats†

:\* 2 random of horse, yak, or water buffalo (These 2 pack animals are always given and don't cost embark points for players "preparing carefully".)

**Considering Metals**

- If your civilization lacks copper or iron (or both), the increased costs for standard-issue metal equipment can eat up the embark point advantage that Prepare Carefully has over Play Now!, but the option to customise point allocation still gives careful preparation an edge.
- Previously, if your home civilization did not have access to copper, you would start with bronze picks and battle axes instead, but there has not been evidence of this occurring since v0.44 of *Dwarf Fortress*.

**Considering Materials**

- When settling on a site with few trees, one should definitely consider bringing extra logs to cover the early demand for beds and such.
- You may also want to consider replacing the pig tail fiber items with much cheaper cave spider silk items (regular, not giant).
- Note that the types of supplies available can vary depending on what materials are available at the nearest capital of your civilization. For example, certain types of stone or bars may not be listed at all, if they are not available at your Mountainhome.

**Considering Animals**

- Do not overlook the value of bringing animals. Dogs in particular can provide an excellent early warning system, good fighters against kobolds and other thieves, and a healthy supply of meat and bones. Cats are useful for controlling the vermin population, but beware the dangers of a catsplosion.

† Cats and dogs are only included by default in the Play Now! package. To start with them when you "Prepare Carefully", you need to go into the pets list to add them.

**Those Parentheses**

- All the items (not animals or dwarves) that you are bringing with you from embark will appear with between parentheses. Example:
- Items you manufacture (or obtain by mining/farming/foraging/scavenging) will not have the parentheses.

#### Saving a starting mix

Once you have the mix of items and skills that you like, you can hit and save it to a template with a custom name. In a later game, you can pick that profile when you embark. If your selected civilization does not have some of the desired items in your template, this is announced clearly, and a different civilization can be tried as described above, or you can continue and change your mix.

If you match skills to the preferences and personalities of your dwarves, it may be an idea not to include any skills in such a template, as they will simply be applied in the original order to the current dwarves as they appear on the list.

If you find additional items that you wish to add (perhaps another type of cheap meat, or an ore not previously available), you can edit those in by hitting , overwriting your old template. You can also go into the embark_profiles.txt and edit in the SKILLS or ITEMS as you want - the syntax is fairly straightforward. Embark profile repository contains examples of different profiles you can experiment with.

## Embark Strategies

The strategies below are suggestions. They are not universal, and many are even contradictory. This is because there is no one true way to play *Dwarf Fortress*. Some may not work for you because of unstated assumptions about priority, value, fun, or procedure. However, since Losing is Fun, it's always worth it to try something out, even if it doesn't go well.

### Picking the Right Location

**Need More Dirt** - three layers of soil before the stone layers begin provides a very large area that can be used to quickly carve out efficient storage rooms, as well as easy construction of large farms and tree farms without the need to flood/muddy large areas of stone.

**Flowing Water (and its inverse)** - Flowing water (river or stream) is a must-have for the infinite power it supplies for working machinery, and because underground water supplies are too dangerous to tap into. There is no guarantee of infinite water underground, you could embark on a map with completely dry caverns. However, rainier climates will always have murky pools, which, with careful management, can be refilled from the rain. Infinite power for working machinery can be created using a limited amount of water in a perpetual motion machine, although, being limited in quantity, murky pools simply do not have the capacity to permanently flood your fortress, while a single mistake with an infinite source can easily do so.

**FPS** - often overlooked, this is perhaps the most consequential decision you will make during embark. FPS drops slowly as fortresses get more people, and create more stuff (the game has to simulate all of these people and the stuff they are making). Having a site that takes little resources to simulate can go a long way to mitigating this problem. The major FPS-eaters to look out for are trees (deciduous trees especially, as they shed their leaves annually), and flowing and/or falling water (the latter being worse on FPS). See the article on Maximizing framerate for considerations. Of all the things you can do to help with FPS, picking a new site is not one of them. Planning for this early on will save you a lot of headaches if you manage to keep a fort alive for more than a decade.

### Preparation Strategies

**Free Barrels** - many products are stored in bins, barrels, or bags and do not stack with other items even if they're in the same broad classification. Plump Helmets and Horse Meat come in separate barrels even though they're both food. Purchasing a single item of food will also produce a free barrel for it to be stored in. As barrels have a cost of 10 to buy empty, buying a single unit of cost 2 foodstuffs gets you a value of 5. Anything above cost 2 bought for the express purpose of getting barrels would be better off just buying barrels empty or raw logs. This concept can be extended to many different goods, and for any stored good you were "going to buy anyway". Alcohol will come in a new barrel after every 5th unit.

- Note that meat products from the same animal will store in the same barrel, thus 1 unit of Horse Meat and 1 unit of Horse Tripe will only get you one barrel, not two.
- Upon arrival you can build a kitchen and prepare lavish meals out of all those single units of meat. This will "compress" your food, and free up some barrels for brewing. Size of stacks of food from cooking is equal to sum of stack sizes of ingredients, so you lose nothing.

**Cheaper food** - you can bring lots of milk (worth 1 embark point each), build a farmer's workshop, and make cheese out of that milk. Combine this with the trick for free barrels, cook lavish meals out of that cheese and meat, and you will get some free barrels, and good quality food for cheap. Making milk into cheese is very fast and requires no skill, you just need to enable cheese making on your cook or brewer. Pick 1 unit of milk from each species and each one will come with a free barrel.

- To save on alcohol (you should probably still bring some of it, though) get plump helmets for 4 embark points each. Remember to disable cooking them in z -\> Kitchen menu. Build a still, and brew them all, each will make 5 units of alcohol. You can supplement this with gathering and brewing local plants.
- Cooking lavish meals out of 1 unit of meat, and full barrels of alcohol made on the spot from plump helmets (known as booze cooking) can produce even more food, but only if one knows how to do it.
- When choosing all that different food, be smart. Press "n" Go to "Meat" section, press "e", and search for one particular kind of food, "meat", for example. Press enter, rinse and repeat. This way, you can quickly add food from different animals and be sure you don't have any 2 foods from the same species. Also, it's good to make a template so you won't have to do the whole thing all over again when you start another fortress.

**Cheap Bags** - while even the cheapest bags (made from cave spider silk and low-value leather) cost 10 points each, you can instead simply bring several units of sand costing 1 point each, as each unit of sand will be stored in its own bag made from a randomly selected material (including giant cave spider silk and valuable creature leather).

**Don't Really Need That** - unless you have tailored your embark for metal production quick and early, an anvil is typically unnecessary and the 100 points you get from refunding it can be better spent on skills or additional foodstuffs (can't really have enough foodstuffs). By the time the Dwarven caravan arrives in the fall, a 100☼ iron anvil, or even a 300☼ steel anvil, should be little more than an inconvenience. This can sometimes be problematic Fun if you are unlucky and the caravan does not bring an anvil.

**REALLY Don't Need That** - For players more familiar with the game. Bring no pre-constructed goods (weapons, buckets, etc.), just the materials to make them with. This requires several (3-10, though you're likely to bring way more) logs, some fire-safe stone (ores are fine if you don't mind some micromanagement), a few nuggets of copper ore, and an anvil. Upon arrival, build a Wood Furnace and a Forge, make charcoal, then picks for the miners and an axe for wood cutters.

Medical supplies should be unnecessary to start with, because if you need them you're screwed you'll have Fun. You may want to bring some rope (or just thread) along though. You can start your fortress with just 106☼ worth of items (iron anvil - 100☼, 1 copper nuggets for 1 pick - 6☼, logs can be gathered from deconstructing the wagon and made into 1 training axe - 0☼ (training axes no longer cut trees in newer versions), fire-safe building material = ash - 0☼, everything else can be made with the raw materials you get from wood-cutting and mining.).

**Yes, I Do Need That** - DON'T EVER leave without alcohol unless you have a brewer and a way to gather plants early (untrained herbalists designated after embarking are enough) or a safe water source (preferably flowing). Be sure to bring multiple types of alcohol, as your dwarves will be happier this way, because the different types will encompass their numerous preferences.

**More Means Better... Right?** - Perhaps you once thought that the default amount of embark points aren't enough for you, and that you could give your fortress a serious leg up in getting started if you embark with *much* more animals and supplies. This can be done in a few ways: The first way is entering the "advanced world generation" screen and creating a custom world generation preset with higher embark points. Note that only a maximum of 10,000 points can be entered without cheating or hacking. The second way is to repeat the first step, but modify the world_gen.txt file found in the \[game dir\]\data\init\\ directory - modifying the \[EMBARK_POINTS:#\] line with any custom number and saving, which **can** be set above 10,000. The third way is to simply use the "points" command if using DFHack, once a world is generated.

Back to the original question, does more mean "better"? The answer: yes and no. Starting with way more supplies and animals can give you a huge starting advantage in already having the materials and then some to get your fortress going, and having the extra animals can be useful for early breeding and butchering. The extra supplies/animals can also provide a huge advantage in trading. However, having extra supplies can also hurt gameplay, as having too much of something can hamper the chance for a dwarf to make something themselves, giving them less opportunities to increase their skill levels. And having too many animals can be a pain to manage, especially once they start breeding and make this task harder. Also, bringing too many supplies with you can have dwarves putting things away from the wagon for a much longer time than normal. This can be a massive nuisance if starting out in harder embark locations where early attacks are likely, or if thieving creatures come by.

## See also

- New players may find the Quickstart guide useful.
- The Starting build article has more detailed embark strategies.

## External links

- Tutorial on how to embark

   Ru:Embark
