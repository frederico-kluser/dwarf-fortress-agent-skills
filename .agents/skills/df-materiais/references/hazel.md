# Hazel

> Fonte: [Hazel](https://dwarffortresswiki.org/index.php/Hazel) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes hazel trees for their nuts.**
- **Biome**
- **Any Temperate**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** Yes
- **Density:** 580
- **Color:** pale taupe
- **Max trunk height:** 6
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Hazel wood
- **Leaf:** Hazel leaf
- **Nut:** Hazel nut
- **Leaf Properties**
- **Edible:** No
- **Seed Properties**
- **Edible:** Yes
- **Cookable:** Yes

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Hazel** is one of the many genera of trees found above ground. Like the vast majority of above ground trees, hazel wood is brown and produces brown products. Logs and leaves can be processed in a dyer's shop into gold dye.

Some dwarves like hazel trees for their *nuts*.

\

Admired for its *nuts*.

    [PLANT:HAZEL] corylus spp.
        [NAME:hazel tree][NAME_PLURAL:hazel trees][ADJ:hazel tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:hazel wood]
            [STATE_ADJ:ALL_SOLID:hazel wood]
            [PREFIX:NONE]
            [SOLID_DENSITY:580] Not reliable but screw it http://paleoplanet69529.yuku.com/topic/62050#.WYnsMdGQzIU
            [STATE_COLOR:ALL_SOLID:TAUPE_PALE] *** not yet searched
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:EMERALD]
            [DISPLAY_COLOR:2:0:0]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [STATE_COLOR:ALL:DARK_TAN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [SEED:hazel nut:hazel nuts:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:6]
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
            [GROWTH_NAME:hazel leaf:hazel leaves]
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
            [GROWTH_NAME:hazel pollen catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:'*':'*':6:0:1:30000:99999:2]
        [GROWTH:NUT]
            [GROWTH_NAME:hazel nut:STP]
            [GROWTH_ITEM:SEEDS:NONE:LOCAL_PLANT_MAT:SEED]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':6:0:0:120000:200000:3]
        [USE_MATERIAL_TEMPLATE:BARK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:hazel bark dye]
            [STATE_COLOR:ALL_SOLID:GOLD]
            [DISPLAY_COLOR:6:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:GOLD]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:hazel leaf dye]
            [STATE_COLOR:ALL_SOLID:GOLD]
            [DISPLAY_COLOR:6:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:GOLD]
            [PREFIX:NONE]
