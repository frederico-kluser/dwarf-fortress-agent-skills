# Red bean

> Fonte: [Red bean](https://dwarffortresswiki.org/index.php/Red_bean) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes red bean vines for their pods.**
- **Seed**
- **/ Red beans**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Temperate**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Pod:** Red bean pod
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Red beans** are an aboveground garden plant. They can be planted in all seasons and only the seeds are edible when cooked.

Some dwarves like red bean vines for their *pods*.

Admired for its *pods*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Frozen red bean biscuits are renowned for their resilience.

|  |
|----|
| "Red bean" in other / Languages / Dwarven / : / ang nangês / Elven / : / niÿira mawada / Goblin / : / tur dugu / Human / : / kasp seto |

    [PLANT:RED_BEAN] vigna angularis
        [NAME:red bean vine][NAME_PLURAL:red bean vines][ADJ:red bean vine]
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
            [STATE_COLOR:ALL:PURPLE]
            [DISPLAY_COLOR:5:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:red bean:red beans:2:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:pods]
        [GROWTH:LEAVES]
            [GROWTH_NAME:red bean leaf:red bean leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:1:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:red bean flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:5:0:1:60000:119999:2]
        [GROWTH:POD]
            [GROWTH_NAME:red bean pod:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_PRINT:'%':'%':2:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
