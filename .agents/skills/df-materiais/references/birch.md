# Birch

> Fonte: [Birch](https://dwarffortresswiki.org/index.php/Birch) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes birches for their autumn coloration.**
- **Biome**
- **Any Temperate Broadleaf**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** Yes
- **Density:** 650
- **Color:** burnt umber
- **Max trunk height:** 8
- **Max trunk diameter:** 1
- **Trunk branching:** 0
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 0
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Birch

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Birch** is a tree found in temperate broadleaf forests. They are the second tallest tree in the game. In classic display mode, birch trees have the special quality of being the only normal tree in the game with a trunk color other than brown – specifically, white. Unfortunately, the logs that they produce are still brown (burnt umber, as described in the raws). With premium graphics, the trunks, wood, and products all use the burnt umber color. Logs can be processed in a dyer's shop into beige dye.

Some dwarves like birches for their *catkins*, *silver bark*, and *autumn coloration*.

\

Admired for its *silver bark*.

## In Real Life

Birch bark was historically used as a form of parchment and fire starter, though the former use is no longer relevant, the latter is still very true.

    [PLANT:BIRCH]
        [NAME:birch][NAME_PLURAL:birches][ADJ:birchen]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:7:0:1]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:birch]
            [STATE_ADJ:ALL_SOLID:birchen]
            [PREFIX:NONE]
            Based on American Birch (Betula spp.)
            http://www.fpl.fs.fed.us/documnts/TechSheets/HardwoodNA/htmlDocs/betula1.html
            [SOLID_DENSITY:650]
            [STATE_COLOR:ALL_SOLID:BURNT_UMBER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:5]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:0]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:8]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:0]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:catkins]
        [PREFSTRING:silver bark]
        [PREFSTRING:autumn coloration]
        [DRY]
        [BIOME:ANY_TEMPERATE_BROADLEAF]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:birch leaf:birch leaves]
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
        [GROWTH:POLLEN_CATKINS]
            [GROWTH_NAME:birch pollen catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:0:'*':6:0:0:NONE]
        [GROWTH:SEED_CATKINS]
            [GROWTH_NAME:birch seed catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:250000]
            [GROWTH_PRINT:0:'*':6:0:0:NONE]
            *** numerous seeds come out from the catkins in fall
        [USE_MATERIAL_TEMPLATE:BARK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:birch bark dye]
            [STATE_COLOR:ALL_SOLID:BEIGE]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:BEIGE]
            [PREFIX:NONE]
