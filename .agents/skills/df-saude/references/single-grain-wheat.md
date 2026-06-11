# Single-grain wheat

> Fonte: [Single-grain wheat](https://dwarffortresswiki.org/index.php/Single-grain_wheat) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes single-grain wheat for their beer.**
- **Seed**
- **/ Single-grain wheat seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Tropical Grassland Tropical Savanna**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Single-grain wheat beer
- **Powder:** Single-grain wheat flour
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Alcohol Flour**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Single-grain wheat** is an aboveground crop. It can either be milled into single-grain wheat flour or brewed into single-grain wheat beer.

Some dwarves like single-grain wheat for its *beer*.

Admired for its *beer*.

## Trivia

Single-grain wheat is the very first plant loaded when starting a (non-modded) game, due to being the first plant defined in the first plant raw file. Due to this, single-grain wheat occupies the 0th/first plant index of any loaded game.

    [PLANT:SINGLE-GRAIN_WHEAT] einkorn wheat
        [NAME:single-grain wheat][NAME_PLURAL:single-grain wheat][ADJ:single-grain wheat]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][BIOME:GRASSLAND_TROPICAL][BIOME:SAVANNA_TROPICAL]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen single-grain wheat beer]
            [STATE_NAME_ADJ:LIQUID:single-grain wheat beer]
            [STATE_NAME_ADJ:GAS:boiling single-grain wheat beer]
            [STATE_COLOR:ALL:AMBER]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:single-grain wheat flour]
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
        [SEED:single-grain wheat seed:single-grain wheat seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:beer]
        [GROWTH:LEAVES]
            [GROWTH_NAME:single-grain wheat leaf:single-grain wheat leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
