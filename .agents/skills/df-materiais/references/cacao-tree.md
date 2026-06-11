# Cacao tree

> Fonte: [Cacao tree](https://dwarffortresswiki.org/index.php/Cacao_tree) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cacao trees for their flowers.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 430
- **Color:** chocolate
- **Max trunk height:** 2
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Cacao wood
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Cacao trees** are aboveground trees, found only in dry sections of tropical rainforests. Like the overwhelming majority of overland trees, cacao tree wood is brown and produces brown products.

While its seeds are the basis of the creation of chocolate in real life, they cannot be used to produce chocolate in-game, even though its trunk is, ironically, chocolate-colored. In real life, cacao fruits are also edible raw.

Some dwarves like cacao trees for their *flowers*.

Admired for its *flowers*.

\

    *** have a weird fig-like structure with flowers inside that turns into a seed

    [PLANT:CACAO]
        [NAME:cacao tree][NAME_PLURAL:cacao trees][ADJ:cacao tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:cacao wood]
            [STATE_ADJ:ALL_SOLID:cacao wood]
            [PREFIX:NONE]
            Based on Theobroma cacao
            http://acta.inpa.gov.br/fasciculos/30-4/PDF/v30n4a06.pdf
            [STATE_COLOR:ALL_SOLID:CHOCOLATE]  A delicious mix of irony and realism.
            [SOLID_DENSITY:430]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:WHITE]
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [STATE_COLOR:ALL:BROWN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:1]
            [EDIBLE_COOKED]
        [SEED:cacao bean:cacao beans:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:226]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:2]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:flowers]
        [DRY]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:cacao leaf:cacao leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:cacao flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:HEAVY_BRANCHES_AND_TRUNK]
            [GROWTH_TIMING:50000:99999]
            [GROWTH_PRINT:5:5:7:0:1:50000:99999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:cacao pod:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:HEAVY_BRANCHES_AND_TRUNK]
            [GROWTH_TIMING:100000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':7:4:0:0:100000:200000:3]
            [GROWTH_HAS_SEED]
