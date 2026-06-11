# Willow

> Fonte: [Willow](https://dwarffortresswiki.org/index.php/Willow) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes willows for their fluffy catkins.**
- **Biome**
- **Any Temperate Any Tropical Forest Tropical Grassland Tropical Savanna Tropical Shrubland Tropical Freshwater Swamp Tropical Saltwater Swamp Tropical Freshwater Marsh Tropical Saltwater Marsh**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 390
- **Color:** tan
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
- **Wood:** Willow
- **Leaf:** Willow leaf
- **Leaf Properties**
- **Edible:** No

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **willow** is a type of above ground tree that is found in nearly any biome that has trees; but only near rivers, pools or other water. Like the overwhelming majority of overland trees, willow wood is brown and produces brown products. Logs and leaves can be processed in a dyer's shop into yellow dye.

Willow trees provide the sixth-lightest type of wood in the game, with a density of 0.390 g/cm³ (just under 2/3 of the average wood density of 0.600 g/cm³). Compared to lighter trees, willows have the benefit of growing nearly everywhere (near water), while the lighter trees are restricted to tropical climates (in the cases of papayas, candlenuts, kapoks, and custard-apples) or good surroundings (in the case of feather trees). As such, willow is the lightest indigenous wood type available to players on neutral or evil temperate embarks.

Willow trees produce **Willow fruit**, which cannot be stockpiled, brewed or cooked at present, leaving dwarves free to chop down these trees for wood, unless they particularly want a shady place to sit while fishing.

Some dwarves like willows for their *fluffy catkins* and their *sad appearance*.

Admired for its *sad appearance*.

    [PLANT:WILLOW]
        [NAME:willow][NAME_PLURAL:willows][ADJ:willow]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:willow]
            [STATE_ADJ:ALL_SOLID:willow]
            [PREFIX:NONE]
            Based on black willow (Salix nigra)
            http://www.fpl.fs.fed.us/documnts/TechSheets/HardwoodNA/htmlDocs/salixn1.html
            [SOLID_DENSITY:390]
            [STATE_COLOR:ALL_SOLID:TAN]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:BROWN]
            [DISPLAY_COLOR:6:0:0]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:244]
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
        [PREFSTRING:sad appearance]
        [PREFSTRING:fluffy catkins]
        [WET]
        [BIOME:ANY_TEMPERATE]
        [BIOME:ANY_TROPICAL_FOREST]
        [BIOME:GRASSLAND_TROPICAL]
        [BIOME:SAVANNA_TROPICAL]
        [BIOME:SHRUBLAND_TROPICAL]
        [BIOME:SWAMP_TROPICAL_FRESHWATER]
        [BIOME:SWAMP_TROPICAL_SALTWATER]
        [BIOME:MARSH_TROPICAL_FRESHWATER]
        [BIOME:MARSH_TROPICAL_SALTWATER]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:willow leaf:willow leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:POLLEN_CATKINS]
            [GROWTH_NAME:willow pollen catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:'*':'*':7:0:1:30000:99999:3]
        [GROWTH:SEED_CATKINS]
            [GROWTH_NAME:willow seed catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:'*':'*':7:0:1:30000:99999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:willow fruit:willow fruit]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:100000:250000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:0:'*':6:0:0:NONE]
            [GROWTH_HAS_SEED]
        *** dioecious
        [USE_MATERIAL_TEMPLATE:BARK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:willow bark dye]
            [STATE_COLOR:ALL_SOLID:YELLOW]
            [DISPLAY_COLOR:6:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:YELLOW]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:willow leaf dye]
            [STATE_COLOR:ALL_SOLID:YELLOW]
            [DISPLAY_COLOR:6:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:YELLOW]
            [PREFIX:NONE]
