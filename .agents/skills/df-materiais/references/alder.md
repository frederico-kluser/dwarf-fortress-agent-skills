# Alder

> Fonte: [Alder](https://dwarffortresswiki.org/index.php/Alder) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes alders for their catkins.**
- **Biome**
- **Any Temperate Broadleaf**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** Yes
- **Density:** 410
- **Color:** tan
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
- **Wood:** Alder

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Alder** is one of the many genera of trees found above ground. A deciduous tree, it sheds leaves in autumn, although this has no effect on the wood produced by chopping it down. Like the vast majority of above ground trees, alder wood is brown and produces brown products. The wood from this tree is relatively light compared to other above-ground trees, which makes it a marginally better material for hauling and a marginally worse one for crossbow melee combat and ballista ammunition. Logs can be processed in a dyer's shop into russet dye, and cones can be processed into sepia dye.

Some dwarves like alders for their *autumn coloration* and their *catkins*.

\

Admired for its *autumn coloration*.

    [PLANT:ALDER]
        [NAME:alder][NAME_PLURAL:alders][ADJ:alder]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [STOCKPILE_PLANT_GROWTH]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:alder]
            [STATE_ADJ:ALL_SOLID:alder]
            [PREFIX:NONE]
            Based on Red Alder (Alnus rubra)
            [SOLID_DENSITY:410]
            [STATE_COLOR:ALL_SOLID:TAN]
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
        [PREFSTRING:autumn coloration]
        [DRY]
        [BIOME:ANY_TEMPERATE_BROADLEAF]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:alder leaf:alder leaves]
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
            [GROWTH_NAME:alder pollen catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:'*':'*':4:0:0:30000:99999:2]
        [GROWTH:SEED_CATKINS]
            [GROWTH_NAME:alder seed catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:0:'*':6:0:0:NONE]
        [GROWTH:CONE]
            [GROWTH_NAME:alder cone:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:100000:300000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:0:'*':6:0:0:NONE]
        [USE_MATERIAL_TEMPLATE:BARK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:alder bark dye]
            [STATE_COLOR:ALL_SOLID:RUSSET]
            [DISPLAY_COLOR:4:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:RUSSET]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:CONE_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:alder cone dye]
            [STATE_COLOR:ALL_SOLID:SEPIA]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:SEPIA]
            [PREFIX:NONE]
