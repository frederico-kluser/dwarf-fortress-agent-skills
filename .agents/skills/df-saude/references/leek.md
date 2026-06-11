# Leek

> Fonte: [Leek](https://dwarffortresswiki.org/index.php/Leek) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes leeks for their taste.**
- **Seed**
- **/ Leek seeds**
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

**Leeks** are an aboveground garden vegetable. They can be planted in all seasons and are edible raw or cooked.

Some dwarves like leeks for their *taste*.

\

Admired for its *taste*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Some other dwarves like leeks for their *spinning*.

    [PLANT:LEEK] allium ampeloprasum
        [NAME:leek][NAME_PLURAL:leeks][ADJ:leek]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE] stem
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:0]
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
        [SEED:leek seed:leek seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:taste]
        [GROWTH:LEAVES]
            [GROWTH_NAME:leek leaf:leek leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:leek flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:5:0:1:60000:119999:2]
