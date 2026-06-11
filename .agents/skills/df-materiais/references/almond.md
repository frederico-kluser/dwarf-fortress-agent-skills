# Almond

> Fonte: [Almond](https://dwarffortresswiki.org/index.php/Almond) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes almond trees for their nuts.**
- **Biome**
- **Any Temperate**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** Yes
- **Density:** 795
- **Color:** copper
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
- **Wood:** Almond wood
- **Nut:** Almond
- **Seed Properties**
- **Edible:** Yes
- **Cookable:** Yes

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Almond** is one of the many trees found above ground. Like the vast majority of above ground trees, almond wood is brown and produces brown products. Their nuts can be processed in a dyer's shop into light brown dye.

Some dwarves like almond trees for their *nuts*.

\

Admired for its *nuts*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Almond trees bear delicious crunchy almonds that can be harvested by setting up a gathering zone underneath it. Almonds cannot be brewed into alcohol. Therefore, you're better off ~~exterminating each and every one of these ugly, useless potential elf retreats~~ cutting the tree or cooking the almonds into +Almond Biscuits+.

Sadly, almonds in *Dwarf Fortress* are all of the sweet variety, and of little use for giving nobles or elves a meal to die for.

    [PLANT:ALMOND] prunus dulcis
        [NAME:almond tree][NAME_PLURAL:almond trees][ADJ:almond tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:almond wood]
            [STATE_ADJ:ALL_SOLID:almond wood]
            [PREFIX:NONE]
            [SOLID_DENSITY:795] Can't find sources for almond, going for plum which is in same genus http://www.wood-database.com/plum/
            [STATE_COLOR:ALL_SOLID:COPPER] *** not yet searched
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:EMERALD]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:HELIOTROPE]
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [STATE_COLOR:ALL:BROWN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [SEED:almond:almonds:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
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
        [PREFSTRING:nuts]
        [DRY]
        [BIOME:ANY_TEMPERATE]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:almond leaf:almond leaves]
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
            [GROWTH_NAME:almond flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:7:0:1:60000:119999:2]
        [GROWTH:NUT]
            [GROWTH_NAME:almond:STP]
            [GROWTH_ITEM:SEEDS:NONE:LOCAL_PLANT_MAT:SEED]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':6:0:0:120000:200000:3]
        [USE_MATERIAL_TEMPLATE:SHELL_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:almond shell dye]
            [STATE_COLOR:ALL_SOLID:LIGHT_BROWN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:LIGHT_BROWN]
            [PREFIX:NONE]
