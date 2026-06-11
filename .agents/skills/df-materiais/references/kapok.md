# Kapok

> Fonte: [Kapok](https://dwarffortresswiki.org/index.php/Kapok) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes kapoks for their buttresses.**
- **Biome**
- **Tropical Moist Broadleaf Forest**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 260
- **Color:** tan
- **Max trunk height:** 8
- **Max trunk diameter:** 2
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Kapok

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Kapoks** are a type of above ground tree, found only in tropical forests. Like the overwhelming majority of overland trees, kapok wood is brown and produces brown products.

Kapok wood is the fourth lightest in the game. Items that need to be hauled a lot, such as bins and barrels, would benefit from being made out of this wood, if the other tree types don't grow in your area.

Some dwarves like kapoks for their *buttresses*.

\

Admired for its *buttresses*.

    [PLANT:KAPOK]
        [NAME:kapok][NAME_PLURAL:kapoks][ADJ:kapok]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:kapok]
            [STATE_ADJ:ALL_SOLID:kapok]
            [PREFIX:NONE]
            Based on Cieba pentandra:
            http://www.fpl.fs.fed.us/documnts/TechSheets/Chudnoff/African/htmlDocs_africa/Ceibapentandra.html
            [SOLID_DENSITY:260]
            [STATE_COLOR:ALL_SOLID:TAN]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:WHITE]
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:1]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:226]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:8] or much much taller 70m
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:2] up to 3m w/ buttresses
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:buttresses]
        [DRY]
        [BIOME:FOREST_TROPICAL_MOIST_BROADLEAF]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:kapok leaf:kapok leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:kapok flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:50000:99999]
            [GROWTH_PRINT:5:5:7:0:1:50000:99999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:kapok fruit:kapok fruit]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:100000:300000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':7:2:0:1:100000:200000:3]
