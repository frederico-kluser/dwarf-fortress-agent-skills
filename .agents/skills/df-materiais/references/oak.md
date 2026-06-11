# Oak

> Fonte: [Oak](https://dwarffortresswiki.org/index.php/Oak) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes oaks for their acorns.**
- **Biome**
- **Any Temperate Broadleaf**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** Yes
- **Density:** 700
- **Color:** auburn
- **Max trunk height:** 8
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Oak
- **Nut:** Acorn
- **Seed Properties**
- **Edible:** Yes
- **Cookable:** Yes

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **oak** is a type of above ground tree found in any temperate broadleaf forest. Like the overwhelming majority of overland trees, oak wood is brown and produces brown products. Logs can be processed in a dyer's shop into brown dye.

Oaks are notable for producing *extreme* amounts of wood logs when cut down. A fully-grown oak can produce at least 30 logs per tree, going over 40 at times, and can actually beat out the highwood for wood production. The only problems are that, only growing in temperate broadleaf forests, they are frequently crowded in by other types of trees, and that it will be hard to find a use (or stockpile space) for all the logs one produces.

Their acorns are also edible and extremely plentiful, although they are not brewable, and temperate broadleaf forests have plenty of fruit-bearing trees. You may want to harvest the oaks for wood, and keep the persimmon and cherry trees for fruits.

Some dwarves like oaks for their *acorns* and their *autumn coloration*.

|  |
|----|
| "Oak" in other / Languages / Dwarven / : / kin / Elven / : / lulo / Goblin / : / osô / Human / : / ecen |

Admired for its *acorns*.

    [PLANT:OAK]
        [NAME:oak][NAME_PLURAL:oaks][ADJ:oaken]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:oak]
            [STATE_ADJ:ALL_SOLID:oaken]
            [PREFIX:NONE]
            Based on Quercus spp.
            http://www.fpl.fs.fed.us/documnts/TechSheets/Chudnoff/TropAmerican/htmlDocs_tropamerican/Quercusspp.html
            [STATE_COLOR:ALL_SOLID:AUBURN]
            [SOLID_DENSITY:700]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [STATE_COLOR:ALL:TAN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW] certain species moreso than others
            [EDIBLE_COOKED]
        [SEED:acorn:acorns:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:8]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5] *** oak has deep roots
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:acorns]
        [PREFSTRING:autumn coloration]
        [DRY]
        [BIOME:ANY_TEMPERATE_BROADLEAF]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:oak leaf:oak leaves]
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
            [GROWTH_NAME:oak flower cluster:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:60000:99999]
            [GROWTH_PRINT:0:5:2:0:0:NONE]
        [GROWTH:NUT]
            [GROWTH_NAME:acorn:STP]
            [GROWTH_ITEM:SEEDS:NONE:LOCAL_PLANT_MAT:SEED]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:100000:250000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:0:7:6:0:0:NONE]
        [USE_MATERIAL_TEMPLATE:BARK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:oak bark dye]
            [STATE_COLOR:ALL_SOLID:BROWN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:BROWN]
            [PREFIX:NONE]
