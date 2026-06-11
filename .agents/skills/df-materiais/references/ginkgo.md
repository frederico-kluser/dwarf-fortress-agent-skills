# Ginkgo

> Fonte: [Ginkgo](https://dwarffortresswiki.org/index.php/Ginkgo) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes ginkgo trees for their seeds.**
- **Biome**
- **Any Temperate**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** Yes
- **Density:** 450
- **Color:** peach
- **Max trunk height:** 8
- **Max trunk diameter:** 2
- **Trunk branching:** 0
- **Heavy branch radius:** 1
- **Branch radius:** 1
- **Root radius:** 3
- **Heavy branch density:** 0
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Ginkgo wood
- **Leaf:** Ginkgo leaf
- **Leaf Properties**
- **Edible:** No
- **Seed Properties**
- **Edible:** Yes
- **Cookable:** Yes

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Ginkgo** is one of the many *genera* of trees found above ground. Like the vast majority of above ground trees, ginkgo wood is brown and produces brown products.

Ginkgo trees frequently have 2-tile-wide trunks. Ginkgo seeds can be harvested by setting up a plant gathering zone, and can be eaten or cooked. Ginkgo leaves can be processed in a dyer's shop into lemon dye.

Some dwarves like ginkgo trees for their *seeds*.

-

  Admired for its *seeds*

-

  Ginkgo seeds

    [PLANT:GINKGO] ginkgo biloba
        [NAME:ginkgo tree][NAME_PLURAL:ginkgo trees][ADJ:ginkgo tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:ginkgo wood]
            [STATE_ADJ:ALL_SOLID:ginkgo wood]
            [PREFIX:NONE]
            [SOLID_DENSITY:450] http://eol.org/pages/1156278/overview
            [STATE_COLOR:ALL_SOLID:PEACH] *** not yet searched
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:YELLOW_GREEN]
            [DISPLAY_COLOR:2:0:0]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [STATE_COLOR:ALL:WHITE]
            [DISPLAY_COLOR:7:0:1]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW] *** not safe?
            [EDIBLE_COOKED] *** not safe?
        [SEED:ginkgo seed:ginkgo seeds:7:0:1:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:24]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:0]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:8]
        [BRANCH_RADIUS:1]
        [TRUNK_BRANCHING:0]
        [MAX_TRUNK_DIAMETER:2] up to 3-4m
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:seeds]
        [DRY]
        [BIOME:ANY_TEMPERATE]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:ginkgo leaf:ginkgo leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_TIMING:0:300000]
            [GROWTH_PRINT:0:6:2:0:0:0:209999:1]
            [GROWTH_PRINT:0:6:6:0:1:210000:300000:1] only yellow
            [GROWTH_DROPS_OFF]
        [GROWTH:POLLEN_CATKINS]
            [GROWTH_NAME:ginkgo pollen catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:'*':'*':6:0:0:30000:99999:2]
        [GROWTH:SEED]
            [GROWTH_NAME:ginkgo seed:STP]
            [GROWTH_ITEM:SEEDS:NONE:LOCAL_PLANT_MAT:SEED]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':7:0:1:120000:200000:3]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:ginkgo leaf dye]
            [STATE_COLOR:ALL_SOLID:LEMON]
            [DISPLAY_COLOR:6:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:LEMON]
            [PREFIX:NONE]
