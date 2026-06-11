# Modding (parte 2/2)

        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]

This defines the structure and material of the plant. It references "STRUCTURAL_PLANT_TEMPLATE" in the first line, so if you were to say, add wings to the template, the plump helmet plant would be winged. This is for the plant itself, not the end plump helmets.

After that we get our edible tokens. These say that vermin can eat the plant, and it can be eaten raw or cooked by your dwarves. So if you wanted a plant that vermin would leave alone, you'd remove the [`[EDIBLE_VERMIN]`](/index.php/Material_definition_token#EDIBLE_VERMIN "Material definition token") token.

             [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]

Next, `[``PICKED_TILE``:6]` is the character (6, or ♠) shown when the crop is harvested. See character table for a table of usable tiles. `[``PICKED_COLOR``:5:0:0]` is the color used for the crop's tile when harvested. It's in a `::` format, resulting in a purple spade: `♠`

         [PICKED_TILE:6][PICKED_COLOR:5:0:0]

`[``GROWDUR``:300]` is how long it takes for your crop to grow. There are 1008 growdur units in a season. You can calculate this value here.\
`[``VALUE``:2]` is the item value of the harvested plant (default 1).

         [GROWDUR:300][VALUE:2]

This defines the plant's alcohol states. `[``STATE_NAME_ADJ``:md]` is the frozen name, followed is the actual drink name, and then its boiling name. Drinks can evaporate and freeze in Scorching or Freezing climates, respectively.

[`[DISPLAY_COLOR]`](/index.php/Material_definition_token#DISPLAY_COLOR "Material definition token") is ASCII color, and [`[STATE_COLOR]`](/index.php/Material_definition_token#STATE_COLOR "Material definition token") is a named color linked to a graphical palette.

[`[EDIBLE_RAW]`](/index.php/Material_definition_token#EDIBLE_RAW "Material definition token") and [`[EDIBLE_COOKED]`](/index.php/Material_definition_token#EDIBLE_COOKED "Material definition token") are saying you can drink the alcohol raw or cooked.

         [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen dwarven wine]
            [STATE_NAME_ADJ:LIQUID:dwarven wine]
            [STATE_NAME_ADJ:GAS:boiling dwarven wine]
            [STATE_COLOR:ALL:AMETHYST]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:5:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]

After that we get our seed template:

         [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:plump helmet spawn:plump helmet spawn:4:0:1:LOCAL_PLANT_MAT:SEED]

And all this says is that the seeds may be eaten by vermin or cooked. Then it gives the name of our plant's seed, its plural name, its foreground, background, and brightness colors, followed by its seed material; said material should have [`[SEED_MAT]`](/index.php/Plant_token#SEED_MAT "Plant token") to permit proper stockpiling.

And finally for the last chunk we have this:

         [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:rounded tops]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:3]
        [SHRUB_TILE:58]
        [DEAD_SHRUB_TILE:58]
        [SHRUB_COLOR:5:0:0]
        [DEAD_SHRUB_COLOR:0:0:1]

First we define what season(s) the plant may grow in, then we define how frequently this plant is generated in a particular area, followed by how many harvested crop items may come from 1 plant. [`[PREFSTRING]`](/index.php/Plant_token#PREFSTRING "Plant token") is what your dwarves like about the plant, which in this case is the rounded tops. [`[WET]`](/index.php/Plant_token#WET "Plant token")/[`[DRY]`](/index.php/Plant_token#DRY "Plant token") are the conditions under which the plant can grow. Wet means it can grow close to water, dry means it can grow away from water. This does not mean you can grow the plant on dry stone however. It is just for natural spawning of the plant.\
[`[BIOME]`](/index.php/Plant_token#BIOME "Plant token") is what biome the plant grows in. `[``UNDERGROUND_DEPTH``:Minimum:Maximum]` is the highest and lowest cavern levels that the plant can appear in if its biome is subterranean. Dwarven civilizations will only export (via the embark screen or caravans) things that are available at depth 1. Defaults to `0:0` (surface only).\
Lastly, [`[SHRUB_TILE]`](/index.php/Plant_token#SHRUB_TILE "Plant token") is the character used for the naturally spawning shrub of this plant, [`[DEAD_SHRUB]`](/index.php/Plant_token#DEAD_SHRUB "Plant token") is the dead shrub character, [`[SHRUB_COLOR]`](/index.php/Plant_token#SHRUB_COLOR "Plant token") is the shrub's color, and [`[DEAD_SHRUB_COLOR]`](/index.php/Plant_token#DEAD_SHRUB_COLOR "Plant token") is, of course, the dead shrub's color.

Plump helmet shrubs look like `:`.

While this may or may not look like a lot of tokens, it's very easy. Just copy an existing plant and edit it to your new plant.\
For the rest of the tokens, see plant token.

#### Trees

Trees are another kind of plant that can be modded. Being plants, they use many of the same tokens as edible crops, but differ in having a few tree-specific tokens.

Below is the apple tree raw description:

      [PLANT:APPLE] malus sieversii
        [NAME:apple tree][NAME_PLURAL:apple trees][ADJ:apple tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:apple wood]
            [STATE_ADJ:ALL_SOLID:apple wood]
            [PREFIX:NONE]
            [SOLID_DENSITY:745] *** http://www.csudh.edu/oliver/chemdata/woods.htm
            [STATE_COLOR:ALL_SOLID:CHOCOLATE] *** http://www.forestryforum.com/board/index.php/topic,61009.0.html
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
                [STATE_NAME_ADJ:ALL_SOLID:frozen apple cider]
            [STATE_NAME_ADJ:LIQUID:apple cider]
            [STATE_NAME_ADJ:GAS:boiling apple cider]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
                [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:ROSE]
            [DISPLAY_COLOR:5:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:RUST]
            [DISPLAY_COLOR:4:0:0]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
        [SEED:apple seed:apple seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:5]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:3]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:fruit]
        [DRY]
        [BIOME:ANY_TEMPERATE]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:apple leaf:apple leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_TIMING:0:300000]
            [GROWTH_PRINT:0:6:2:0:0:0:209999:1]
            [GROWTH_PRINT:0:6:6:0:1:210000:239999:1] autumn color
            [GROWTH_PRINT:0:6:4:0:1:240000:269999:1]
            [GROWTH_PRINT:0:6:4:0:0:270000:300000:1]
            [GROWTH_DROPS_OFF]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:apple flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:5:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:apple:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':4:0:0:120000:200000:3]
            [GROWTH_HAS_SEED]

The first lines are the same as the ones we saw being used in the plump helmets, defining the plant object, giving it a name, and setting up the basic materials.

     [PLANT:APPLE] malus sieversii
        [NAME:apple tree][NAME_PLURAL:apple trees][ADJ:apple tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]

Adding the token [`[DISPLAY_COLOR]`](/index.php/Material_definition_token#DISPLAY_COLOR "Material definition token") (ASCII) / [`[STATE_COLOR]`](/index.php/Material_definition_token#STATE_COLOR "Material definition token") (graphics) directly after [`[USE_MATERIAL_TEMPLATE]`](/index.php/Plant_token#USE_MATERIAL_TEMPLATE "Plant token") would allow us to change the color of the tree.

            [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
                [DISPLAY_COLOR:1:0:0]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]

would give us a dark blue apple tree. This method is used by the game by birches and various underground trees.

Next come the definitions of various other materials used by the tree:

            [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:apple wood]
            [STATE_ADJ:ALL_SOLID:apple wood]
            [PREFIX:NONE]
            [SOLID_DENSITY:745] *** http://www.csudh.edu/oliver/chemdata/woods.htm
            [STATE_COLOR:ALL_SOLID:CHOCOLATE] *** http://www.forestryforum.com/board/index.php/topic,61009.0.html
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
                [STATE_NAME_ADJ:ALL_SOLID:frozen apple cider]
            [STATE_NAME_ADJ:LIQUID:apple cider]
            [STATE_NAME_ADJ:GAS:boiling apple cider]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
                [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:ROSE]
            [DISPLAY_COLOR:5:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:RUST]
            [DISPLAY_COLOR:4:0:0]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
        [SEED:apple seed:apple seeds:0:0:1:LOCAL_PLANT_MAT:SEED]

\
From them, we get to know what the parts of the tree can be used for, as well as how they will appear when separated from the tree. Any alterations that can be done to materials normally can be done here, such as changing the value or adding a syndrome.

       [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:5]

[`[TREE]`](/index.php/Plant_token#TREE "Plant token") is what turns your plant object into an actual tree. The following argument describes what material the harvested logs should be made of. If `NONE`, the felled tree will give no logs. [`[TREE_TILE]`](/index.php/Plant_token#TREE_TILE "Plant token") is the tile the tree shows up as on the world map, in this case `♣`.

Note that all vanilla trees (that give logs) use the "WOOD" material defined above as the argument for [`[TREE]`](/index.php/Plant_token#TREE "Plant token"), as opposed to the "STRUCTURAL" material. Thus, any changes to the properties of the wood harvested should be done to the "WOOD" material.

The following tokens decide the dimensions of the tree, and how it grows.

        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:3]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]

\
[`[TRUNK_PERIOD]`](/index.php/Plant_token#TRUNK_PERIOD "Plant token") and [`[TRUNK_WIDTH_PERIOD]`](/index.php/Plant_token#TRUNK_WIDTH_PERIOD "Plant token") determine how long it takes for the trunk to grow one tile taller respectively wider, in years. `[``MAX_TRUNK_HEIGHT``:3]` and `[``MAX_TRUNK_DIAMETER``:1]` determine the maximum value the above can reach. [`[TRUNK_BRANCHING]`](/index.php/Plant_token#TRUNK_BRANCHING "Plant token") decides how "curvy" the tree is, with `[``TRUNK_BRANCHING``:0]` meaning the tree is entirely straight.

`[``HEAVY_BRANCH_DENSITY``:25]`, `[``HEAVY_BRANCH_RADIUS``:1]`, `[``BRANCH_DENSITY``:50]`, `[``BRANCH_RADIUS``:2]`, `[``ROOT_DENSITY``:5]`, and `[``ROOT_RADIUS``:3]` determine the density (how many are there, integer ranging 0-100) and radius (in tiles) away from the trunk, of heavy branches, normal branches and roots respectively.

[`[STANDARD_TILE_NAMES]`](/index.php/Plant_token#STANDARD_TILE_NAMES "Plant token") makes the tree use standard names for the trunk, branches etc. Otherwise custom ones can be used. (see full plant token list)

[`[SAPLING]`](/index.php/Plant_token#SAPLING "Plant token") ensures saplings of this tree are called "\[tree name\] sapling", instead of the standard "young \[tree name\]".

Lastly, we are introduced to the [`[GROWTH]`](/index.php/Plant_token#GROWTH "Plant token") token. [`[GROWTH]`](/index.php/Plant_token#GROWTH "Plant token") defines growths growing on a plant, in this case our apple tree. Apple trees have three growths: leaves, flowers and fruits.

      [GROWTH:FRUIT]
            [GROWTH_NAME:apple:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':4:0:0:120000:200000:3]
            [GROWTH_HAS_SEED]

\
First comes the name of the growth. Then, with [`[GROWTH_ITEM]`](/index.php/Plant_token#GROWTH_ITEM "Plant token"), what kind of growth it is, in this case a [`[PLANT_GROWTH]`](/index.php/Item_token#PLANT_GROWTH "Item token") made out of the local "FRUIT" material. [`[GROWTH_DENSITY]`](/index.php/Plant_token#GROWTH_DENSITY "Plant token") says how densely the growth grows, and [`[GROWTH_HOST_TILE]`](/index.php/Plant_token#GROWTH_HOST_TILE "Plant token") where on the tree it grows. [`[GROWTH_TIMING]`](/index.php/Plant_token#GROWTH_TIMING "Plant token") decides when the growth appears, in annual ticks. The growth then drops off, leaving no clouds (items to be picked up by your dwarves). [`[GROWTH_PRINT]`](/index.php/Plant_token#GROWTH_PRINT "Plant token") sets it to look like `%`, and [`[GROWTH_HAS_SEED]`](/index.php/Plant_token#GROWTH_HAS_SEED "Plant token") implies that eating this growth will leave you with a seed.

### Workshops

Workshops are raw-designed pretty differently from everything else in the game, being buildable structures rather than items or methods to gain items. However, they are fairly simple. For example, here's the raw for the soap maker's workshop:

    [BUILDING_WORKSHOP:SOAP_MAKER]
        [NAME:Soap Maker's Workshop]
        [NAME_COLOR:7:0:1]
        [DIM:3:3]
        [WORK_LOCATION:2:2]
        [BUILD_LABOR:SOAP_MAKER]
        [BUILD_KEY:CUSTOM_SHIFT_P]
        [BLOCK:1:0:0:0] workbenches no longer block
        [BLOCK:2:0:0:0]
        [BLOCK:3:0:0:0]
        [TILE:0:1:' ':' ':150]
        [TILE:0:2:' ':' ':'/']
        [TILE:0:3:'-':' ':' ']
        [COLOR:0:1:0:0:0:0:0:0:6:0:0]
        [COLOR:0:2:0:0:0:0:0:0:6:0:0]
        [COLOR:0:3:6:0:0:0:0:0:0:0:0]
        [TILE:1:1:' ':' ':'=']
        [TILE:1:2:'-':' ':8]
        [TILE:1:3:' ':' ':150]
        [COLOR:1:1:0:0:0:0:0:0:6:0:0]
        [COLOR:1:2:6:0:0:0:0:0:6:0:0]
        [COLOR:1:3:0:0:0:0:0:0:6:0:0]
        [TILE:2:1:'-':' ':8]
        [TILE:2:2:' ':' ':8]
        [TILE:2:3:' ':150:' ']
        [COLOR:2:1:6:0:0:0:0:0:6:0:0]
        [COLOR:2:2:0:0:0:0:0:0:6:0:0]
        [COLOR:2:3:0:0:0:6:0:0:0:0:0]
        [TILE:3:1:150:' ':8]
        [TILE:3:2:' ':' ':8]
        [TILE:3:3:' ':240:' ']
        [COLOR:3:1:6:0:0:0:0:0:6:7:0]
        [COLOR:3:2:0:0:0:0:0:0:6:7:0]
        [COLOR:3:3:0:0:0:7:0:1:0:0:0]
        [BUILD_ITEM:1:BUCKET:NONE:NONE:NONE][EMPTY][CAN_USE_ARTIFACT]
        [BUILD_ITEM:1:NONE:NONE:NONE:NONE][BUILDMAT][WORTHLESS_STONE_ONLY][CAN_USE_ARTIFACT]
        [TOOLTIP:Use tallow (rendered fat) or oil here with lye to make soap.]

A line-by-line breakdown:

         [NAME:Soap Maker's Workshop]
        [NAME_COLOR:7:0:1]

These define the name of the workshop (Soap Maker's Workshop) and color of the workshop's name when examined.

         [DIM:3:3]
        [WORK_LOCATION:2:2]

[`[DIM]`](/index.php/Building_token#DIM "Building token") refers to how large the workshop will be, in this case 3 wide, 3 tall. [`[WORK_LOCATION]`](/index.php/Building_token#WORK_LOCATION "Building token") tells where the creature using it (usually a dwarf) will work, numbered from the top left--in this case, `2:2`, or the middle. Multiple work locations can be defined, even outside the dim.

         [BUILD_LABOR:SOAP_MAKER]
        [BUILD_KEY:CUSTOM_SHIFT_S]

These refer to the worker required to build it (soap maker) and the key used to build it in the workshop menu (capital S).

         [BLOCK:1:0:0:0]
        ...

This is a bit more complex, and is where we get to the meaty part of workshop making--the tiles' properties. [`[BLOCK]`](/index.php/Building_token#BLOCK "Building token") refers to which tiles will be untraversable--1 means blocked, 0 means unblocked. The first number refers to row, and the next 3 refer to column, so 1:0:0:0 means that, on the first row, all tiles will be unblocked. This is the case for all vanilla workshops, as of now.

         [TILE:0:1:' ':' ':150]
        ...

The [`[TILE]`](/index.php/Building_token#TILE "Building token") token tells which tile will go where. note, however, that there are 5 entries here instead of 4. The first number, in this case, refers to build stage, numbered from 0 to 3; 3 or 1 is fully built (depending on whether there are stages), 0 is just placed, and 2 is always an intermediate stage, while 1 is usually an intermediate stage. Whether 1 is an intermediate stage or not depends on if there are a 2 and 3 stage; if 2 and 3 exist, 1 will be intermediate. The second number and beyond are similar to [`[BLOCK]`](/index.php/Building_token#BLOCK "Building token"); however, instead of 1s and 0s, you must input tiles. The tiles themselves can be given in quotes (as in ' ') or given as a number, which can be looked up here. Here, we have 150, which is û.

         [COLOR:0:1:0:0:0:0:0:0:6:0:0]
        ...

[`[COLOR]`](/index.php/Building_token#COLOR "Building token") is as [`[TILE]`](/index.php/Building_token#TILE "Building token"), but with colors instead of tiles; however, colors are made up of 3 numbers each or MAT. MAT refers to the color of the material used to make it; the 3 numbers refer to `::`, and can be looked up here. For example, `4:2:1` will give you bright red with a dark green background (☻).

For the first row (`0:1`) our colors are \[`0:0:0`, `0:0:0`, `6:0:0`\]. Combining tile and color, this is our result: ` `` `` `` ``û`

         [BUILD_ITEM:1:BUCKET:NONE:NONE:NONE][EMPTY][CAN_USE_ARTIFACT]
        [BUILD_ITEM:1:NONE:NONE:NONE:NONE][BUILDMAT][WORTHLESS_STONE_ONLY][CAN_USE_ARTIFACT]

These refer to items required to build the building. These are in the same format as reaction reagents and products: `::::`.

You'll learn more about those on the article about reactions, though. The second [`[BUILD_ITEM]`](/index.php/Building_token#BUILD_ITEM "Building token") is special— it uses modifiers exclusively to determine its requirements.

[`[BUILDMAT]`](/index.php/Building_token#BUILDMAT "Building token") refers to wood logs, wood blocks, stone boulders, and stone blocks; [`[WORTHLESS_STONE_ONLY]`](/index.php/Building_token#WORTHLESS_STONE_ONLY "Building token") means it can't use economic stone; [`[CAN_USE_ARTIFACT]`](/index.php/Building_token#CAN_USE_ARTIFACT "Building token") means that it... can use artifacts. [`[EMPTY]`](/index.php/Building_token#EMPTY "Building token"), in the bucket's case, means that the bucket must be empty.

         [TOOLTIP:Use tallow (rendered fat) or oil here with lye to make soap.]

This is the text in the tooltip shown when the building is highlighted by the mouse in the workshops list.

More can be seen at the building tokens article, including links to graphical editors for assembling workshop tile visuals.

### Reactions

Reactions are the crafting recipes used in workshops, and by the adventurer. By adding new reactions you can make new items available, or enable you to get items or materials in new ways. The reactions can also be given to entities, in which case they will make use of them during both world gen and play; making a reaction that creates steel directly from plant fibers could allow the elves to craft steel, and arrive clad in it in a siege.

Not all crafting jobs are custom reactions. Reactions are explicitly defined in raws, such as those for pottery and alloy making.

An in-depth guide for reactions is available here.

### Materials

As we've seen when talking about creatures, materials are vital. Materials can be defined in three forms: material templates, organic materials local to creatures and plants, and inorganic materials such as stone or metal.

Let's take a look at "METAL_TEMPLATE" in material_template_default.txt. It's evident that most of the basic properties of metals are already defined in the template - it goes red and melts at a high enough temperature, it's heavy, and (as noted by the very bottom token) is a metal. We already know just how useful templates can be to creatures, and the same applies to other materials.

Now let's take a look at inorganic_metal.txt. You can see that the metals here refer to the templates, and, just like we did with creatures, then modify the properties of that template and expand upon it.

Finally, let's look at inorganic_stone_mineral.txt. Here we can see that in addition to the changes made to the template, there are also [`[ENVIRONMENT]`](/index.php/Inorganic_material_definition_token#ENVIRONMENT "Inorganic material definition token") tokens - these tell the game where to place these minerals during worldgen.

Here's a list of material tokens. It should also help you out with any modifications you want to make regarding those creature modifications we were making a while back. See, it all ties together in the end. The beauty of the current materials system is that there's actually very little difference between, say, leather and iron - they're fundamentally the same thing regardless of the item type, just with different properties.

## Selecting and Cutting

As explained above, existing raws can be altered with the use of `SELECT`, and can also be culled with `CUT` for more granular control, compared to simply unloading vanilla content in the mod loader. Token behavior when multiple tokens are added depends on the individual token, such as adding to or overwriting the past value. Removing tags from an object without cutting and recreating the object in question is typically impossible, except for creature object tags removed and/or replaced with the use of creature variation tokens.

The syntax for selecting and cutting objects is as follows:

    Substitute X for the desired object. A CUT does not need a SELECT prior, this is simply a list of available options.
    Functions that apply only to local sub-objects are indented. In order to edit these, the base object must be currently being defined or have been selected prior.

    [SELECT_CREATURE:X]
    [CUT_CREATURE:X]

       [SELECT_CASTE:X]
       [SELECT_ADDITIONAL_CASTE:X]

       [SELECT_MATERIAL:X]
       [PLUS_MATERIAL:X]
       [REMOVE_MATERIAL:X]

       [SELECT_TISSUE:X]
       [REMOVE_TISSUE:X]

       [SELECT_TISSUE_LAYER:X]
       [PLUS_TISSUE_LAYER:X]

    [SELECT_ENTITY:X]
    [CUT_ENTITY:X]

    [SELECT_INTERACTION:X]
    [CUT_INTERACTION:X]

    [SELECT_ITEM:X]
    [CUT_ITEM:X]

    [SELECT_WORD:X]
    [CUT_WORD:X]

    [SELECT_TRANSLATION:X]
    [CUT_TRANSLATION:X]

    [SELECT_SYMBOL:X]
    [CUT_SYMBOL:X]

    [SELECT_INORGANIC:X]
    [CUT_INORGANIC:X]

    [SELECT_PLANT:X]
    [CUT_PLANT:X]

       [SELECT_MATERIAL:X]

       [SELECT_GROWTH:X]

    [SELECT_REACTION:X]
    [CUT_REACTION:X]

    [SELECT_MUSIC:X]
    [CUT_MUSIC:X]

    [SELECT_SOUND:X]
    [CUT_SOUND:X]

Note that the [`[SELECT_SYMBOL]`](/index.php/Entity_token#SELECT_SYMBOL "Entity token") entity token is separate from the `[SELECT_SYMBOL]` language token.

## Examples

*Main articles: Category:Modding_Examples*

The Hydling below was made by Mysteryguye (and annotated, updated and separated into blocks by Putnam), to act as an example creature.

    [CREATURE:HYDLING]
        [DESCRIPTION:A seven-headed small hairy thing, about the size of a dog. It is very loyal to its masters, and will promptly disembowel any enemy straying too close.]
        This is the description that shows up in-game when viewing the creature.

        [NAME:hydling:hydlings:hydlish] If there were a civ made of hydlings, it would appear as "hydlings" in the neighbors screen.

        [CASTE_NAME:hydling:hydlings:hydlish]

        [CREATURE_TILE:'='][COLOR:2:0:1] Will appear as a light green "=".

        [PETVALUE:40][NATURAL] Creature is known to be naturally occurring by the game. Will cost 40 embark points to buy.

        [LARGE_ROAMING] Will spawn outdoors, wandering around.

        [COMMON_DOMESTIC][TRAINABLE][PET] Can be bought on embark as a pet, war animal, or hunting animal.

        [BONECARN] Can eat meat and bones only--no vegetables.

        [PREFSTRING:loyalty] Dwarves will like it for its loyalty.

        [LARGE_PREDATOR] Will attack rather than flee.

        [BODY:BASIC_2PARTBODY:7HEADNECKS:BASIC_FRONTLEGS:BASIC_REARLEGS:TAIL:2EYES:NOSE:2LUNGS:HEART:GUTS:ORGANS:THROAT:SPINE:BRAIN:SKULL:3TOES_FQ_REG:3TOES_RQ_REG:MOUTH:TONGUE:GENERIC_TEETH_WITH_FANGS:RIBCAGE]

        Has a lower body, upper body, 4 legs, a tail, fourteen eyes, fourteen ears, seven noses, two lungs, a heart, guts, a pancreas etc., and 7 heads with all that goes with those.

        [BODYGLOSS:PAW] Feet will be called "paws"

        [BODY_DETAIL_PLAN:STANDARD_MATERIALS] Declares the standard materials that most creatures' tissues are made of.

        [BODY_DETAIL_PLAN:STANDARD_TISSUES] This declares the tissues that the creature's tissue layers are made of.

        [BODY_DETAIL_PLAN:VERTEBRATE_TISSUE_LAYERS:SKIN:FAT:MUSCLE:BONE:CARTILAGE] And this describes the tissue layers that the creature is made of.

        [BODY_DETAIL_PLAN:BODY_HAIR_TISSUE_LAYERS:HAIR] Creature will be covered with a layer of fur.

        [USE_MATERIAL_TEMPLATE:NAIL:NAIL_TEMPLATE] And it'll have nails.

        [USE_TISSUE_TEMPLATE:NAIL:NAIL_TEMPLATE]

        [TISSUE_LAYER:BY_CATEGORY:TOE:NAIL:FRONT] On the toe, specifically.

        [SELECT_TISSUE_LAYER:HEART:BY_CATEGORY:HEART]
         [PLUS_TISSUE_LAYER:SKIN:BY_CATEGORY:THROAT]
            [TL_MAJOR_ARTERIES] Heart and throat--called above--will cause heavy bleeding if ruptured.

        [BODY_DETAIL_PLAN:STANDARD_HEAD_POSITIONS] Places eyes, ears and what-have-you into their correct placement, so that you don't have people punching out eyes from behind.

        [BODY_DETAIL_PLAN:HUMANOID_RIBCAGE_POSITIONS] Sets the ribcage as being around lungs and heart.

        [USE_MATERIAL_TEMPLATE:SINEW:SINEW_TEMPLATE] Defines sinew so that...
        [TENDONS:LOCAL_CREATURE_MAT:SINEW:200] Tendons...
        [LIGAMENTS:LOCAL_CREATURE_MAT:SINEW:200] ...And ligaments can be defined.

        [HAS_NERVES] Creature has nerves, and as such can be disabled by severing them.

        [USE_MATERIAL_TEMPLATE:BLOOD:BLOOD_TEMPLATE] Defines the material BLOOD using the template BLOOD_TEMPLATE.
        [BLOOD:LOCAL_CREATURE_MAT:BLOOD:LIQUID] Defines the creature's BLOOD as being made of the above-defined BLOOD material in a LIQUID state.

        [CREATURE_CLASS:GENERAL_POISON] Creature can be affected by syndromes that affect GENERAL_POISON.

        [GETS_WOUND_INFECTIONS] Pretty much self-explanatory. Creature can get infected from wounds.
        [GETS_INFECTIONS_FROM_ROT] And from necrosis.

        [USE_MATERIAL_TEMPLATE:PUS:PUS_TEMPLATE] Defines PUS using PUS_TEMPLATE.
        [PUS:LOCAL_CREATURE_MAT:PUS:LIQUID] Defines PUS as being made of PUS.

        [BODY_SIZE:0:0:1000] Creature will be 1000 cubic centimeters at birth...
        [BODY_SIZE:1:0:12500] 12500 cubic centimeters at 1 year old...
        [BODY_SIZE:2:0:30000] and 30000 cubic centimeters at 2.

        [BODY_APPEARANCE_MODIFIER:LENGTH:90:95:98:100:102:105:110] Creature can be anywhere from 90% to 110% as long as others.
        [BODY_APPEARANCE_MODIFIER:HEIGHT:90:95:98:100:102:105:110] As above, but with height.
        [BODY_APPEARANCE_MODIFIER:BROADNESS:90:95:98:100:102:105:110] As above, but with broadness. This puts the minimum size of the creature (when fully grown) at 21870 and the maximum size at 39930.

        [MAXAGE:20:30] Creature will die of old age between the ages of 20 and 30, no later than 30, no sooner than 20.

        [CAN_DO_INTERACTION:MATERIAL_EMISSION] Creature can use the MATERIAL_EMISSION interaction.
            [CDI:ADV_NAME:Hurl fireball] In adventurer mode, the MATERIAL_EMISSION interaction will appear as "Hurl fireball".
            [CDI:USAGE_HINT:ATTACK] Creature will use MATERIAL_EMISSION when it's attacking, on creatures that it's attacking.
            [CDI:BP_REQUIRED:BY_CATEGORY:HEAD] Creature must have at least one HEAD to use MATERIAL_EMISSION.
            [CDI:FLOW:FIREBALL] The MATERIAL_EMISSION will shoot a fireball.
            [CDI:TARGET:C:LINE_OF_SIGHT] The target for the emission--a location--must be within the line of sight of the Hydling.
            [CDI:TARGET_RANGE:C:15] And must be, at most, 15 tiles away.
            [CDI:MAX_TARGET_NUMBER:C:1] The hydling can only shoot at one target at a time...
            [CDI:WAIT_PERIOD:30] and only every 30 ticks (3 tenths of a second at 100 FPS)

        [ATTACK:BITE:CHILD_BODYPART_GROUP:BY_CATEGORY:HEAD:BY_CATEGORY:TOOTH] Defines a BITE attack that uses teeth.
            [ATTACK_SKILL:BITE] Attack uses the BITE skill.
            [ATTACK_VERB:nom:noms] "The Hydling noms the Elf in the left first toe, tearing the muscle!"
            [ATTACK_CONTACT_PERC:100] Will use all of the tooth. Note that this can be more than 100.
            [ATTACK_PENETRATION_PERC:100] Will sink the tooth all the way in. This can also be more than 100.
            [ATTACK_FLAG_EDGE] Attack is an EDGE attack.
            [ATTACK_PRIORITY:MAIN] Attack is of priority MAIN. Other option is SECOND.
            [ATTACK_FLAG_CANLATCH] Attack can latch on.
                    [ATTACK_PREPARE_AND_RECOVER:3:3] Takes 3 ticks to wind up attack and 3 to recover from it.
                    [ATTACK_FLAG_INDEPENDENT_MULTIATTACK] Can use each head independently.

        [ATTACK:SCRATCH:CHILD_TISSUE_LAYER_GROUP:BY_TYPE:STANCE:BY_CATEGORY:ALL:NAIL] As above, but for nail instead of teeth.
            [ATTACK_SKILL:STANCE_STRIKE] Uses the kicking skill.
            [ATTACK_VERB:slice:slices] "You slice the Elf in the left foot and the severed part sails off in an arc!"
            [ATTACK_CONTACT_PERC:100] Uses the whole nail.
            [ATTACK_PENETRATION_PERC:100] The whole nail goes in.
            [ATTACK_FLAG_EDGE] Attack is an edge attack.
                    [ATTACK_PREPARE_AND_RECOVER:3:3]
            [ATTACK_PRIORITY:SECOND]

        [CHILD:1] Hydling will become an adult at 1 year old.

        [GENERAL_CHILD_NAME:hydie:hydies] Children will appear as "hydies".

        [DIURNAL] Is active during the daytime.

        [HOMEOTHERM:10070] Has a body temperature of 102 Fahrenheit.

        [APPLY_CREATURE_VARIATION:STANDARD_QUADRUPED_GAITS:900:730:561:351:1900:2900] Can run at 25 kph
        [APPLY_CREATURE_VARIATION:STANDARD_SWIMMING_GAITS:3512:2634:1756:878:4900:6900] Can swim at 10 kph
        [APPLY_CREATURE_VARIATION:STANDARD_CRAWLING_GAITS:6561:6115:5683:1755:7456:8567] Can crawl at 5 kph
        [SWIMS_INNATE]Swims innately.

        [CASTE:FEMALE] Defines a caste called FEMALE.
            [FEMALE] FEMALE caste is female.

        [CASTE:MALE] As above, but with male.
            [MALE] See above.

## See also

- Raw file
- Token
- Modding pitfalls
- Cheating
- Bay 12 Guide: https://bay12games.com/dwarves/modding_guide.html


---
*Parte 2 de 2 de «Modding». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Modding*
