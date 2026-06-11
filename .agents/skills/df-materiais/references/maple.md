# Maple

> Fonte: [Maple](https://dwarffortresswiki.org/index.php/Maple) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes maples for their autumn coloration.**
- **Biome**
- **Temperate Broadleaf Forest Temperate Grassland Temperate Savanna Temperate Shrubland**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** Yes
- **Density:** 540
- **Color:** rust
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
- **Wood:** Maple

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Maples** are a type of above ground tree, found in nearly any temperate region with vegetation. Like the overwhelming majority of overland trees, maple wood is brown and produces brown products. Logs can be processed in a dyer's shop into light brown dye.

Maples produce **Maple leaves** and **Maple samaras**, which cannot be stockpiled, brewed or cooked at present, nor is there any current means to extract maple syrup from maple trees. Cut them freely.

Some dwarves like maples for their *autumn coloration*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Although some attempts to pulp the tree for "syrup" have been unsuccessful, many continue trying. Only a select few human kingdoms have mastered the craft.

Admired for its *autumn coloration*.

    *** should open and show fluffy white cotton

    [PLANT:MAPLE]
        [NAME:maple][NAME_PLURAL:maples][ADJ:maple]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:maple]
            [STATE_ADJ:ALL_SOLID:maple]
            [PREFIX:NONE]
            Based on Acer spp.
            http://www.fpl.fs.fed.us/documnts/TechSheets/HardwoodNA/htmlDocs/acersp1.html
            [SOLID_DENSITY:540] Used a more average value.  Softer maples are around 400, harder ones around 600.
            [STATE_COLOR:ALL_SOLID:RUST]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:1]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:5]
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
        [PREFSTRING:autumn coloration]
        [DRY]
        [BIOME:FOREST_TEMPERATE_BROADLEAF]
        [BIOME:GRASSLAND_TEMPERATE]
        [BIOME:SAVANNA_TEMPERATE]
        [BIOME:SHRUBLAND_TEMPERATE]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:maple leaf:maple leaves]
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
            [GROWTH_NAME:maple flower cluster:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:20000:99999]
            [GROWTH_PRINT:0:5:2:0:1:NONE]
        [GROWTH:FRUIT]
            [GROWTH_NAME:maple samara:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:100000:250000]
            [GROWTH_DROPS_OFF]
            [GROWTH_PRINT:0:'%':6:0:0:NONE]
        *** dioecious
        [USE_MATERIAL_TEMPLATE:BARK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:maple bark dye]
            [STATE_COLOR:ALL_SOLID:LIGHT_BROWN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:LIGHT_BROWN]
            [PREFIX:NONE]
