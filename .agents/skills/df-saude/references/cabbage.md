# Cabbage

> Fonte: [Cabbage](https://dwarffortresswiki.org/index.php/Cabbage) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cabbages for their taste.**
- **Seed**
- **/ Cabbage seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Temperate**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Leaf:** Cabbage leaf
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Leaf Properties**
- **Edible:** No
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Cabbage** is an aboveground garden vegetable. They can be planted in all seasons and are edible raw or cooked. Leaves can be processed in a dyer's shop into pink dye.

Some dwarves like cabbages for their *taste*.

\

Admired for its *taste*.

    [PLANT:CABBAGE] brassica oleracea (many cultivars like broccoli, cauliflower, etc.)
        [NAME:cabbage][NAME_PLURAL:cabbages][ADJ:cabbage]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:1]
        [DRY][BIOME:ANY_TEMPERATE]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:YELLOW]
            [DISPLAY_COLOR:6:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:cabbage seed:cabbage seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:taste]
        [GROWTH:LEAVES]
            [GROWTH_NAME:cabbage leaf:cabbage leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:1:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:cabbage flower spike:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:6:0:1:60000:119999:2]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:cabbage leaf dye]
            [STATE_COLOR:ALL_SOLID:PINK]
            [DISPLAY_COLOR:4:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:PINK]
            [PREFIX:NONE]
