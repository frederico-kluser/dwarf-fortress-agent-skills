# Coffee

> Fonte: [Coffee](https://dwarffortresswiki.org/index.php/Coffee) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes coffee trees for their yummy cherries.**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 620
- **Color:** pale taupe
- **Max trunk height:** 5
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Coffee wood
- **Fruit:** Coffee cherry
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Coffee** is one of the many genera of trees found above ground. Like the vast majority of above ground trees, coffee wood is brown and produces brown products.

Coffee trees bear coffee cherry fruit. These fruits can be eaten or cooked and produce coffee beans when eaten. Coffee beans cannot be eaten or brewed into coffee, nor can their cherries be brewed into booze. ~~So feel free to cut each and every one of these useless elf houses.~~ But they can be processed in a dyer's shop into brown dye.

Some dwarves like coffee for their *yummy cherries*.

\

Admired for its *yummy cherries*.

    *** cashew apple and cashew nut that grows on the end of the apple (nut actually grows first then apple grows out)

    [PLANT:COFFEE] coffea arabica
        [NAME:coffee tree][NAME_PLURAL:coffee trees][ADJ:coffee tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:coffee wood]
            [STATE_ADJ:ALL_SOLID:coffee wood]
            [PREFIX:NONE]
            [SOLID_DENSITY:620] http://eol.org/pages/1109554/overview
            [STATE_COLOR:ALL_SOLID:TAUPE_PALE] *** not yet searched
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:FERN_GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:WHITE]
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:CHOCOLATE]
            [DISPLAY_COLOR:4:0:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:coffee bean:coffee beans:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:5]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:yummy cherries]
        [DRY]
        [BIOME:ANY_TROPICAL]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:coffee leaf:coffee leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:coffee flower cluster:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:7:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:coffee cherry:coffee cherries]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':4:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
            *** 2 beans
            *** can brew drink from roasted beans
        [USE_MATERIAL_TEMPLATE:BEAN_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:coffee bean dye]
            [STATE_COLOR:ALL_SOLID:BROWN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:BROWN]
            [PREFIX:NONE]
