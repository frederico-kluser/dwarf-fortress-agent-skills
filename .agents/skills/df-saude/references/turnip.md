# Turnip

> Fonte: [Turnip](https://dwarffortresswiki.org/index.php/Turnip) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes turnip plants for their edible roots.**
- **Seed**
- **/ Turnip seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Temperate**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Turnip wine
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Alcohol Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Turnips** are an aboveground garden vegetable. They can be planted in all seasons, are edible raw or cooked, and can also be brewed into turnip wine or processed in a dyer's shop into beige dye.

Some dwarves like turnip plants for their *edible roots*.

\

Admired for its *edible roots*.

    [PLANT:TURNIP] brassica rapa
        [NAME:turnip plant][NAME_PLURAL:turnip plants][ADJ:turnip plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE] the root
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:5:0:1]
        [DRY][BIOME:ANY_TEMPERATE]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen turnip wine]
            [STATE_NAME_ADJ:LIQUID:turnip wine]
            [STATE_NAME_ADJ:GAS:boiling turnip wine]
            [STATE_COLOR:ALL:MAROON]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:5:0:1]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:YELLOW]
            [DISPLAY_COLOR:6:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:turnip seed:turnip seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:edible roots]
        [GROWTH:LEAVES]
            [GROWTH_NAME:turnip leaf:turnip leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:turnip flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:6:0:1:60000:119999:2]
        [USE_MATERIAL_TEMPLATE:SKIN_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:turnip skin dye]
            [STATE_COLOR:ALL_SOLID:BEIGE]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:BEIGE]
            [PREFIX:NONE]
