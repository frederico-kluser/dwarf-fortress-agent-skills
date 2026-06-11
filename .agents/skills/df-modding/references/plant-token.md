# Plant token

> Fonte: [Plant token](https://dwarffortresswiki.org/index.php/Plant_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\
The `[OBJECT:PLANT]` token begins the definition of a plant raw file. Following this, each new plant definition begins with the `[PLANT:plant_ID]` token, where plant_ID is a unique identifier for the plant, and that plant's properties are then defined using the tokens listed below.

\

## Basic tokens

These tokens are specified for all plants and define their most basic characteristics.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  NAME | name | The singular form of the plant's name as seen in-game. |
|  NAME_PLURAL | name | The plural form of the plant's name as seen in-game. |
|  ADJ | adjective | The word or phrase used to describe items made from this plant. |
|  ALL_NAMES | name | Sets the NAME, NAME_PLURAL, and ADJ to the specified string. |
|  PREFSTRING | reason | What dwarves can like this object for (e.g. "Urist likes plump helmets for their rounded tops.") |
|  MATERIAL | material_name | Starts defining a new local plant material with the given name. Must be followed with material definition tokens defining the material's properties. A maximum of 200 materials can be defined on any given plant. |
|  USE_MATERIAL | material_name / local_material | Starts defining a new local plant material with the given name and using the properties of another local plant material. May be followed with material definition tokens to further define its properties or change the properties imported from the local plant material. A maximum of 200 materials can be defined on any given plant. |
|  USE_MATERIAL_TEMPLATE | material_name / template_name | Starts defining a new local plant material with the name *material_name* and using the properties of the specified MATERIAL_TEMPLATE with the name *template_name*. May be followed with material definition tokens to further define its properties or change the properties imported from the template material. A maximum of 200 materials can be defined on any given plant. |
|  SELECT_MATERIALv50.13 | material_name | Selects a previously defined local plant material for subsequent modification. Unlike with creature tokens, "ALL" *cannot* be specified here. |
|  BASIC_MAT | material | Sets the basic material of the plant. This defines what is harvested when the plant itself, rather than a growth, is picked. According to Toady, you can use other materials (for instance, iron) but the game may hiccup on plants that aren't structurally plants. For crops, said material should have \[STRUCTURAL_PLANT_MAT\] to permit proper stockpiling. Generally, this should be "LOCAL_PLANT_MAT:material_name", using a material defined using MATERIAL, USE_MATERIAL, or USE_MATERIAL_TEMPLATE. The only way to remove the plant's basic material entry (e.g. "soybean plant") from every stockpile category is to remove this token, but this will cause problems with farming the plant in a farm plot and harvesting the whole wild plant if that's possible. |

## Environment tokens

These tokens, also applicable to all plants, specify where the plants grow.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  UNDERGROUND_DEPTH | minimum / maximum | Designates the highest and lowest cavern levels that the plant can appear in if its biome is subterranean. Dwarven civilizations will only export (via the embark screen or caravans) things that are available at depth 1. Defaults to 0:0 (surface only). |
|  GOOD |  | Restricts the plant to growing in Good regions. Cannot be combined with \[EVIL\]. |
|  EVIL |  | Restricts the plant to growing in Evil regions. Cannot be combined with \[GOOD\]. |
|  SAVAGE |  | Restricts the plant to growing in Savage regions (regardless of alignment). |
|  FREQUENCY | freq (0-100) | How frequently this plant is generated in a particular area. Defaults to 50. Plants with valid biome tokens and \[FREQUENCY:0\] will not grow in the wild, but will still be available for entity use and farm plots. |
|  WET |  | Restricts the plant to growing near natural water features. A plant with \[WET\] may be very common or very rare in an area, depending on how many water features that area has. Note that they will not grow next to dwarf-filled channels, since it explicitly checks the tile type (e.g. "River", "River Source", "Brook", "Murky Pool", and variants thereof). Combining this with \[DRY\] causes it to be ignored. |
|  DRY |  | Restricts the plant to growing away from natural water features. Combining this with \[WET\] causes it to be ignored. |
|  BIOME | biome | What biome this plant appears in. |

## Growth tokens

These tokens are used for all plants, and specify growths growing on a plant. Edible or otherwise usable growths should have \[STOCKPILE_PLANT_GROWTH\] in their material definitions for proper stockpiling. This also lets them be collected from plant gathering and farming jobs.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  GROWTH | name | Defines a plant growth, taking the below tokens as arguments. |
|  SELECT_GROWTHv50.13 | name | Selects a previously-defined plant growth. Any tokens which follow this will further modify the selected growth. |
|  GROWTH_NAME | singular / plural (STP for standard plural) | The name of a plant growth. |
|  GROWTH_ITEM | item token / material token | Specifies what item this growth is and what it is made of. Generally, the item type should be PLANT_GROWTH:NONE. / If multiple growths point to the same material with \[STOCKPILE_PLANT_GROWTH\] then only the first will appear correctly in the stockpile menu, with latter growths appearing as "Plant Growth (?)" |
|  GROWTH_HOST_TILE | plant part | Specifies on which part of the plant or tree the growth appears, usually for multi-tile / trees / . Valid tokens are: / TWIGS / BRANCHES_AND_TWIGS / LIGHT_BRANCHES_AND_TWIGS / BRANCHES / LIGHT_BRANCHES / ALL_BRANCHES_AND_TWIGS / HEAVY_BRANCHES / DIRECTED_BRANCHES / HEAVY_BRANCHES_AND_TRUNK / DIRECTED_BRANCHES_AND_TRUNK / TRUNK / ROOTS / CAP / SAPLING |
|  GROWTH_TRUNK_HEIGHT_PERC | start percent (0-100+) / end percent (0-100+) | Controls the height on the trunk between which the growth begins to appear. The first value is the percent of the trunk height where the growth begins appearing: 0 will cause growths to appear starting above the first tile; 100 will cause growths to appear only at the topmost trunk tile. Can be larger than 100 for trees that have growths on branches extending higher than the trunk. / A value of -1 for the second number appears to make the growths extend all the way to the top of the trunk. |
|  GROWTH_DENSITY | integer | Currently has no effect. |
|  GROWTH_TIMING | time / start:end (0-403200) | Specifies at which part of the year the growth appears. Default is all year round. / A single growth can only have one GROWTH_TIMING tag. If multiple are declared, the last one will be used. To make a growth appear multiple times during the year, you need to create a different growth for every GROWTH_TIMING interval. By using the same material for all of the duplicate growths, all of them will be stockpiled together and be eligible for the same reactions. Edible / brewable growths will have separate entries in the kitchen menu, though. / There is no known way to declare a growth timing that lasts from winter into spring. Including numbers below 0 or above 403200 in the range will make the growth available at all times, as though you hadn't defined a growth timing at all. So will including a range for which the start time is later than the end time. / This has no effect on farmed growths; all eligible growths that have \[STOCKPILE_PLANT_GROWTH\] in their materials will be harvested, regardless of if they are currently within their growth timing or not. |
|  GROWTH_PRINT | overworld tile / item tile / color / time (0-403200) start:end, ALL, or NONE / priority | Specifies the appearance of the growth. Can be specified more than once, for example for autumn leaves. Transitions between different timing periods will happen gradually over the course of 2000 ticks. / Priority seems to control what to display when there would be multiple symbols on a tile in ASCII mode. A higher number takes priority over a lower number. Example: if a LEAVES growth has a priority of 1 and a FRUIT growth has a priority of 3, the fruit growth will be the symbol shown when it is present. / The GROWTH_PRINT tile will only be displayed when the growth in question is actually present, even if its timing parameter is ALL. / In graphics mode, any growth being displayed will cause the SHRUB graphic to be used, and no growths available will display the SHRUB_PICKED graphic. |
|  GROWTH_HAS_SEED |  | The growth drops a seed if eaten raw. |
|  GROWTH_DROPS_OFF |  | Growths drop from the plant, producing a cloud of items which fall on the ground, which herbalists can collect. |
|  GROWTH_DROPS_OFF_NO_CLOUD |  | Growths drop collectable items from the plant without producing item clouds. |

## Tree tokens

These tokens are used only for trees.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  TREE | material / or NONE | Makes the plant into a tree. Cutting down the tree will yield logs made of this material. Setting the material to NONE will give no wood from this tree. |
|  TRUNK_NAME | name | What the trunk of the tree is named. |
|  MAX_TRUNK_HEIGHT | 1-8 | The maximum z-level height of a mature tree's trunk, starting from about two z-levels above ground and going up. |
|  MAX_TRUNK_DIAMETER | 1-3 | Upper limit of trunk thickness, in tiles. Counted separately for all branching trunks. Has a geometric effect on log yield. |
|  TRUNK_PERIOD | integer | The number of years the trunk takes to grow one Z-level upward.\[Verify\] |
|  TRUNK_WIDTH_PERIOD | integer | The number of years the trunk takes to grow another tile wider. |
|  LIGHT_BRANCHES_NAME | name | What thin branches of the tree are named. |
|  BRANCH_DENSITY /  LIGHT_BRANCHES_DENSITY | integer | How dense the branches grow on this tree. |
|  BRANCH_RADIUS /  LIGHT_BRANCH_RADIUS | integer | The radius to which branches can reach. Appears to never reach further than seven tiles from the centre. Does not depend on the trunk branching amount or where trunks are. The values used in the game go from 0-3. Higher values than that can cause crashes. Bug:10419 |
|  HEAVY_BRANCHES_NAME /  DIRECTED_BRANCHES_NAME | name | What thick branches of the tree are named. |
|  HEAVY_BRANCH_DENSITY /  DIRECTED_BRANCH_DENSITY | integer | Similar to BRANCH_DENSITY for thick branches. |
|  HEAVY_BRANCH_RADIUS /  DIRECTED_BRANCH_RADIUS | integer | Similar as BRANCH_DENSITY for thick branches. Values outside 0-3 can cause crashes. Bug:10419 |
|  TRUNK_BRANCHING | integer | How much the trunk branches out. 0 makes the trunk straight. |
|  ROOT_NAME /  ROOTS_NAME | name | What the roots of the tree are named. |
|  ROOT_DENSITY | integer | Density of the root growth. |
|  ROOT_RADIUS | integer | How wide the roots reach out. |
|  TWIGS_NAME | name | What the twigs of the tree are named. |
|  TWIGS_SIDE_BRANCHES | boolean (0 or 1) | Twigs appear on the side of branches. Defaults to 1. |
|  TWIGS_ABOVE_BRANCHES | boolean (0 or 1) | Twigs appear above branches. Defaults to 1. |
|  TWIGS_BELOW_BRANCHES | boolean (0 or 1) | Twigs appear below branches. Defaults to 0. |
|  TWIGS_SIDE_HEAVY_BRANCHES | boolean (0 or 1) | Twigs appear on the side of heavy branches. Defaults to 0. |
|  TWIGS_ABOVE_HEAVY_BRANCHES | boolean (0 or 1) | Twigs appear above heavy branches. Defaults to 0. |
|  TWIGS_BELOW_HEAVY_BRANCHES | boolean (0 or 1) | Twigs appear below heavy branches. Defaults to 0. |
|  TWIGS_SIDE_TRUNK | boolean (0 or 1) | Twigs appear on the side of the trunk. Defaults to 0. |
|  TWIGS_ABOVE_TRUNK | boolean (0 or 1) | Twigs appear above the trunk. Defaults to 0. |
|  TWIGS_BELOW_TRUNK | boolean (0 or 1) | Twigs appear below the trunk. Defaults to 0. |
|  TREE_HAS_MUSHROOM_CAP |  | The tree has a rounded cap-hood like a giant mushroom. This severely stunts a tree's maximum height. Bug:7313 |
|  CAP_NAME | name | What this mushroom-cap is called. Only makes sense with TREE_HAS_MUSHROOM_CAP. |
|  CAP_PERIOD | integer | Similar to the other PERIOD tags, influences the rate of the mushroom cap growth. Only makes sense with TREE_HAS_MUSHROOM_CAP. |
|  CAP_RADIUS | integer | The radius of a mushroom cap. Only makes sense with TREE_HAS_MUSHROOM_CAP. |
|  STANDARD_TILE_NAMES |  | Uses the standard names for the tree components (roots, trunk, branches, etc.) |
|  TREE_TILE | tile | The tile used for trees of this type on the world map. Defaults to 24 (↑). |
|  DEAD_TREE_TILE | tile | The tile used for (un)dead trees and deciduous trees (generally in winter) of this type. Defaults to 198 (╞). |
|  SAPLING_TILE | tile | The tile used for saplings of this tree. Defaults to 231 (τ). |
|  DEAD_SAPLING_TILE | tile | The tile used for dead saplings of this tree. Defaults to 231 (τ). |
|  TREE_COLOR | foreground / background / bright | The color of the tree on the map. Defaults to 2:0:0 (dark green). |
|  DEAD_TREE_COLOR | foreground / background / bright | The color of the tree on the map when (un)dead. Defaults to 0:0:1 (dark gray). |
|  SAPLING_COLOR | foreground / background / bright | The color of saplings of this tree. Defaults to 2:0:0 (dark green). |
|  DEAD_SAPLING_COLOR | foreground / background / bright | The color of dead saplings of this tree. Defaults to 0:0:1 (dark gray). |
|  SAPLING_DROWN_LEVEL | depth | The sapling of this tree will drown once the water on its tile reaches this level. Defaults to 4. |
|  TREE_DROWN_LEVEL | depth | The water depth at which this tree will drown. Exact behavior is unknown. Defaults to 7. |
|  SAPLING |  | Makes young versions of the tree be called "\[tree name\] sapling"; otherwise, they are called "young \[tree name\]". |

## Shrub tokens

These tokens are used for non-grass, non-tree plants.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  SPRING,  SUMMER,  AUTUMN,  WINTER |  | Allows the plant to grow in farm plots during the given season. / If the plant is a surface plant, allows it to grow in the wild during this season; wild surface plants without this token will disappear at the beginning of the season. Underground plants grow wild in all seasons, regardless of their season tokens. |
|  GROWDUR | time | How long the plant takes to grow to harvest in a farm plot. Unit hundreds of ticks, See Time. There are 1008 GROWDUR units in a season. Defaults to 300. |
|  VALUE | value | Has no known effect. Previously set the value of the harvested plant. |
|  PICKED_TILE | tile | The tile used when the plant is harvested whole, or is ready to be picked from a farm plot. May either be a cp437 tile number, or a character between single quotes. See character table. Defaults to 231 (τ). |
|  DEAD_PICKED_TILE | tile | The tile used when a plant harvested whole has wilted. Defaults to 169 (⌐). |
|  SHRUB_TILE | tile | The tile used to represent this plant when it is wild, alive, and has no growths. Defaults to 34 ("). |
|  DEAD_SHRUB_TILE | tile | The tile used to represent this plant when it is dead in the wild. Defaults to 34 ("). |
|  CLUSTERSIZE | size | The maximum stack size collected when gathered via herbalism (but *not* farm plots). Defaults to 5. CLUSTERSIZE must be greater than or equal to 1+ the number of instances of \[STOCKPILE_PLANT_GROWTH\] in the plant's raws. For plants like vanilla cabbage, clustersize of 1, which is less than 1+\[one instance\]=2, will prevent citizens from gathering the plant. Best to set all cluster sizes to 2 or higher for safety. |
|  PICKED_COLOR | foreground / background / bright | The color of the plant when it has been picked whole, or when it is ready for harvest in a farm plot. Defaults to 2:0:0 (dark green). |
|  DEAD_PICKED_COLOR | foreground / background / bright | The color of the plant when it has been picked whole, but has wilted. Defaults to 0:0:1 (dark gray). |
|  SHRUB_COLOR | foreground / background / bright | The color of the plant when it is alive, wild, and has no growths. Defaults to 2:0:0 (dark green). |
|  DEAD_SHRUB_COLOR | foreground / background / bright | The color of the plant when it is dead in the wild. Defaults to 6:0:0 (brown). |
|  SHRUB_DROWN_LEVEL | depth | The shrub will drown once the water on its tile reaches this level. Defaults to 4. |
|  DRINK | material | Names a drink made from the plant, allowing it to be used in entity resources. Previously also permitted brewing the plant into alcohol made of this material. Now, a MATERIAL_REACTION_PRODUCT of type DRINK_MAT should be used on the proper plant material. |
|  MILL | material | Permits milling the plant at a quern or millstone into a powder made of this material and allows its use in entity resources. Said material should have \[POWDER_MISC_PLANT\] to permit proper stockpiling. This token makes the whole plant harvestable regardless of which material is designated for milling. For plants with millable *growths*, use only MATERIAL_REACTION_PRODUCT or ITEM_REACTION_PRODUCT tokens to define the milling products. |
|  THREAD | material | Permits processing the plant at a farmer's workshop to yield threads made of this material and allows its use in entity resources. Said material should have \[THREAD_PLANT\] to permit proper stockpiling. |
|  SEED | name / name_plural / foreground / background / bright / material | Causes the plant to yield plantable seeds made of this material and having these properties. Said material should have \[SEED_MAT\] to permit proper stockpiling. |
|  EXTRACT_STILL_VIAL | material | Permits processing the plant into a vial at a still to yield extract made of this material. Said material should have \[EXTRACT_STORAGE:FLASK\]. |
|  EXTRACT_VIAL | material | Permits processing the plant into a vial at a farmer's workshop to yield extract made of this material. Said material should have \[EXTRACT_STORAGE:FLASK\]. |
|  EXTRACT_BARREL | material | Permits processing the plant into a barrel at a farmer's workshop to yield extract made of this material. Said material should have \[EXTRACT_STORAGE:BARREL\]. |

## Grass tokens

These tokens are used only for grasses.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  GRASS |  | Makes the plant behave as a type of grass. This allows animals to graze on it, and prevents it and its growths from being picked by herbalists. (Grass growths can still be picked in adventure mode, however.) |
|  GRASS_TILES | tile / tile / tile / tile | Specifies the 4 tiles used to represent grass of this type. If VARIED_GROUND_TILES is disabled in settings, these are ignored. Defaults to 46:44:96:39 (.,\`'). |
|  ALT_PERIOD | period / offset | How often the grass switches between its main tiles and alternate tiles. The "period" value determines how quickly (in frames) the grass animates, and the "offset" value specifies how much of that time is spent displaying the alternate tiles. If the "offset" value is greater than or equal to the "period" value, the grass will only display using the alternate tiles.\[Verify\] Defaults to 0:0. |
|  ALT_GRASS_TILES | tile / tile / tile / tile | When used with ALT_PERIOD, specifies the 4 alternate tiles used to represent grass of this type. Defaults to 46:44:96:39 (.,\`'). Dead grass does not animate. |
|  GRASS_COLORS | color 1 (fore:back:bright) / color 2 (fore:back:bright) / dry color (fore:back:bright) / dead color (fore:back:bright) | Specifies the color of this grass. Defaults to 2:0:1:2:0:0:6:0:1:6:0:0 (light green, dark green, yellow, brown). |
