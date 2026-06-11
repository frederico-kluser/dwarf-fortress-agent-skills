# Cedar

> Fonte: [Cedar](https://dwarffortresswiki.org/index.php/Cedar) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cedars for their majesty.**
- **Biome**
- **Temperate Coniferous Forest Tropical Coniferous Forest**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 570
- **Color:** olive
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
- **Wood:** Cedar

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **Cedar** is a type of tree found in coniferous forests at various latitudes.

Some dwarves like cedars for their *majesty*.

\

Admired for its *majesty*.

\

## Notes

The raws for the cedar mention the genus Tabebuia, a group of tropical American deciduous shrubs and trees. In contrast, the material definitions (scale-leaves and cones) imply a conifer, possibly one of the North American cupressaceae commonly called white or red cedars.

    [PLANT:CEDAR]
        [NAME:cedar][NAME_PLURAL:cedars][ADJ:cedar]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:cedar]
            [STATE_ADJ:ALL_SOLID:cedar]
            [PREFIX:NONE]
            Based on White-Cedar (Tabebuia spp.)
            http://www.fpl.fs.fed.us/documnts/TechSheets/Chudnoff/TropAmerican/htmlDocs_tropamerican/Tabebuiasppwhitecedar.html
            [STATE_COLOR:ALL_SOLID:OLIVE]
            [SOLID_DENSITY:570]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:23]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
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
        [PREFSTRING:majesty]
        [DRY]
        [BIOME:FOREST_TEMPERATE_CONIFER]
        [BIOME:FOREST_TROPICAL_CONIFER]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:cedar scale-leaf:cedar scale-leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:'*':2:0:0:ALL:1]
        *** seed drop out of cone
        [GROWTH:SEED_CONE]
            [GROWTH_NAME:cedar seed cone:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:100000:300000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:0:'*':6:0:0:NONE]
        [GROWTH:POLLEN_CONE]
            [GROWTH_NAME:cedar pollen cone:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:100000:200000]
            [GROWTH_PRINT:0:'*':5:0:0:NONE]
