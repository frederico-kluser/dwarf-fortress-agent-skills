# Two-grain wheat

> Fonte: [Two-grain wheat](https://dwarffortresswiki.org/index.php/Two-grain_wheat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes two-grain wheat for their beer.**
- **Seed**
- **/ Two-grain wheat seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Tropical Grassland Tropical Savanna**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Two-grain wheat beer
- **Powder:** Two-grain wheat flour
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Alcohol Flour**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Two-grain wheat** is an aboveground crop. It can either be milled into two-grain wheat flour or brewed into two-grain wheat beer.

Some dwarves like two-grain wheat for its *beer*.

\

Admired for its *beer*.

    [PLANT:TWO-GRAIN_WHEAT] emmer wheat
        [NAME:two-grain wheat][NAME_PLURAL:two-grain wheat][ADJ:two-grain wheat]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][BIOME:GRASSLAND_TROPICAL][BIOME:SAVANNA_TROPICAL]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen two-grain wheat beer]
            [STATE_NAME_ADJ:LIQUID:two-grain wheat beer]
            [STATE_NAME_ADJ:GAS:boiling two-grain wheat beer]
            [STATE_COLOR:ALL:AMBER]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:two-grain wheat flour]
            [STATE_COLOR:ALL_SOLID:WHITE]
            [DISPLAY_COLOR:7:0:1]
            [MATERIAL_VALUE:20]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [MILL:LOCAL_PLANT_MAT:MILL] *** ear is threshed to spikelets, milled down to flour
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:two-grain wheat seed:two-grain wheat seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:beer]
        [GROWTH:LEAVES]
            [GROWTH_NAME:two-grain wheat leaf:two-grain wheat leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
