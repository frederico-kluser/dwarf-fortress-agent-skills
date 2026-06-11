# Bayberry

> Fonte: [Bayberry](https://dwarffortresswiki.org/index.php/Bayberry) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bayberry trees for their waxy berries.**
- **Biome**
- **Any Temperate Taiga**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 700
- **Color:** pale brown
- **Max trunk height:** 1
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Bayberry wood
- **Fruit:** Bayberry
- **Leaf:** Bayberry leaf
- **Alcohol:** Bayberry wine
- **Leaf Properties**
- **Edible:** No
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Bayberry** is one of the many genera of trees found above ground. Like the vast majority of above ground trees, bayberry wood is brown and produces brown products.

Bayberry trees bear bayberries that can be harvested by setting up a gathering zone. They can be eaten raw, cooked, or brewed into bayberry wine, so you may consider exploiting them rather than chopping them down to make charcoal.

Leaves and fruits can be processed in a dyer's shop into dye - leaves for yellow and fruits for blue.

Some dwarves like bayberry trees for their *waxy berries*.

Admired for its *waxy berries*.

    [PLANT:BAYBERRY] myrica gale/rubra
        [NAME:bayberry tree][NAME_PLURAL:bayberry trees][ADJ:bayberry tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:bayberry wood]
            [STATE_ADJ:ALL_SOLID:bayberry wood]
            [PREFIX:NONE]
            [SOLID_DENSITY:700] Has bayberry in name, close enough http://eol.org/pages/2872256/overview
            [STATE_COLOR:ALL_SOLID:PALE_BROWN] *** not yet searched
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen bayberry wine]
            [STATE_NAME_ADJ:LIQUID:bayberry wine]
            [STATE_NAME_ADJ:GAS:boiling bayberry wine]
            [STATE_COLOR:ALL:CRIMSON]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:SEA_GREEN]
            [DISPLAY_COLOR:2:0:0]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:CARDINAL]
            [DISPLAY_COLOR:5:0:0]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
            *** can be boiled for wax
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
        [SEED:bayberry seed:bayberry seeds:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:1]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:waxy berries]
        [DRY]
        [BIOME:ANY_TEMPERATE]
        [BIOME:TAIGA]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:bayberry leaf:bayberry leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:POLLEN_CATKINS]
            [GROWTH_NAME:bayberry pollen catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:'*':'*':6:0:0:30000:99999:2]
        [GROWTH:SEED_CATKINS]
            [GROWTH_NAME:bayberry seed catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:0:'*':6:0:0:NONE]
        [GROWTH:FRUIT]
            [GROWTH_NAME:bayberry:bayberries]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':5:0:0:120000:200000:3]
            [GROWTH_HAS_SEED]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:bayberry leaf dye]
            [STATE_COLOR:ALL_SOLID:YELLOW]
            [DISPLAY_COLOR:6:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:YELLOW]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:BERRY_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:bayberry dye]
            [STATE_COLOR:ALL_SOLID:BLUE]
            [DISPLAY_COLOR:1:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:BLUE]
            [PREFIX:NONE]
