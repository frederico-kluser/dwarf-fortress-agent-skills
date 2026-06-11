# Rubber tree

> Fonte: [Rubber tree](https://dwarffortresswiki.org/index.php/Rubber_tree) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rubber trees for their branch shedding.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 490
- **Color:** flax
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
- **Wood:** Rubber wood

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Rubber trees** are a type of above ground tree, found in tropical moist broadleaf forests. Rubber wood is brown (referred in the raws as "flax") and produces brown products.

As of yet, latex cannot be extracted from rubber trees.

Some dwarves like rubber trees for their *branch shedding*.

Admired for its *branch shedding*.

    [PLANT:RUBBER]
        [NAME:rubber tree][NAME_PLURAL:rubber trees][ADJ:rubber tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:rubber wood]
            [STATE_ADJ:ALL_SOLID:rubber wood]
            [PREFIX:NONE]
            Based on Hevea brasiliensis
            http://www.fpl.fs.fed.us/documnts/TechSheets/Chudnoff/TropAmerican/html_files/heveab1new.html
            [SOLID_DENSITY:490]
            [STATE_COLOR:ALL_SOLID:FLAX]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:226]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:8]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:branch shedding]
        [DRY]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:rubber leaf:rubber leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
