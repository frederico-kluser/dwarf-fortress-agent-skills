# Apple

> Fonte: [Apple](https://dwarffortresswiki.org/index.php/Apple) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes apple trees for their fruit.**
- **Biome**
- **Any Temperate**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** Yes
- **Density:** 745
- **Color:** chocolate
- **Max trunk height:** 3
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Apple wood
- **Fruit:** Apple
- **Leaf:** Apple leaf
- **Alcohol:** Apple cider
- **Leaf Properties**
- **Edible:** No
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Apple** is one of the many genera of trees found above ground. Like most trees, apple wood is brown and produces brown products.

Apple trees bear apples that can be harvested by setting up a gathering zone. They can be eaten raw, cooked, or brewed into delicious apple cider, so you may consider exploiting them, rather than chopping them down to make charcoal. They also drop leaves, which can be collected in bags. Apple leaves are not cookable or brewable, though they can be made into dye.

Logs and leaves can be processed in a dyer's shop into dyes - logs for rose and leaves for yellow.

Some dwarves like apple trees for their *fruit*.

\

Admired for its *fruit*.

|  |
|----|
| "Apple" in other / Languages / Dwarven / : / bemòng / Elven / : / fena / Goblin / : / slusna / Human / : / ramet |

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

An apple once fell on the head of a scholar, smashing his head into his body, an unrecognizable mass. Thus, the field of dwarven physics was born.

Apples were invented by two humans named Steve. A well-documented but little understood phenomenon among humans is that a preference for windows strongly correlates with an intense dislike for apples, and vice versa. Curiously, humans who like penguins tend to have a profound distaste for both.

\

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
            [STATE_COLOR:ALL:AMBER]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
            [STOCKPILE_PLANT_GROWTH]
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
        [USE_MATERIAL_TEMPLATE:BARK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:apple bark dye]
            [STATE_COLOR:ALL_SOLID:ROSE]
            [DISPLAY_COLOR:4:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:ROSE]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:apple leaf dye]
            [STATE_COLOR:ALL_SOLID:YELLOW]
            [DISPLAY_COLOR:4:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:YELLOW]
            [PREFIX:NONE]
