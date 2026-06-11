# String bean

> Fonte: [String bean](https://dwarffortresswiki.org/index.php/String_bean) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes string bean plants for their pods.**
- **Seed**
- **/ String beans**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Temperate**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Pod:** String bean pod
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**String beans** are an aboveground garden plant. They can be planted in all seasons. Only the seeds when cooked are edible.

Some dwarves like string bean plants for their *pods*.

Admired for its *pods*.

|  |
|----|
| "String bean" in other / Languages / Dwarven / : / birut nangês / Elven / : / nale mawada / Goblin / : / slongu dugu / Human / : / ip seto |

    [PLANT:STRING_BEAN] phaseolus vulgaris
        [NAME:string bean plant][NAME_PLURAL:string bean plants][ADJ:string bean plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:1]
        [DRY][BIOME:ANY_TEMPERATE]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:WHITE] or pink or purple
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:string bean:string beans:2:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:pods]
        [GROWTH:LEAVES]
            [GROWTH_NAME:string bean leaf:string bean leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:1:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:string bean flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:7:0:1:60000:119999:2]
        [GROWTH:POD]
            [GROWTH_NAME:string bean pod:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_PRINT:'%':'%':2:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
