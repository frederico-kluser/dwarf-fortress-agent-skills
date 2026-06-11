# Long yam

> Fonte: [Long yam](https://dwarffortresswiki.org/index.php/Long_yam) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes long yam plants for their tubers.**
- **Seed**
- **/ Long yam seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Temperate**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Long yams** are an aboveground garden plant. They can be planted in all seasons and are edible raw or cooked.

Long yams are the only type of yam that can be eaten raw. However, because they cannot be brewed or otherwise processed, waiting for your dwarves to eat them is the only way to get seeds, making them a difficult crop to plan around.

Some dwarves like long yam plants for their *tubers*.

\

Admired for its *tubers*.

    [PLANT:LONG_YAM] dioscorea opposita
        [NAME:long yam plant][NAME_PLURAL:long yam plants][ADJ:long yam plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE] the tuber, does not need to be cooked
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:6:0:0]
        [DRY][BIOME:ANY_TEMPERATE]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:WHITE]
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:long yam seed:long yam seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:tubers]
        [GROWTH:LEAVES]
            [GROWTH_NAME:long yam leaf:long yam leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:long yam flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:7:0:1:60000:119999:2]
