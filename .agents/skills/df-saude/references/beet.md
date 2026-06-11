# Beet

> Fonte: [Beet](https://dwarffortresswiki.org/index.php/Beet) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes beet plants for their edible roots.**
- **Seed**
- **/ Beet seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Temperate Grassland**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Beetroot wine
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Food Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Beets** are an aboveground garden vegetable. They can be planted in all seasons, is edible raw or cooked, and can also be brewed into beetroot wine.

Some dwarves like beet plants for their *edible roots*.

\

Admired for its *edible roots*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

A human doctor is known to sell highly coveted beets. Most dwarves don't understand the demand for beets by Dr. Dre.

    [PLANT:BEET] beta vulgaris
        [NAME:beet plant][NAME_PLURAL:beet plants][ADJ:beet plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE] the root and leaves
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:4:0:1]
        [DRY][BIOME:GRASSLAND_TEMPERATE]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen beetroot wine]
            [STATE_NAME_ADJ:LIQUID:beetroot wine]
            [STATE_NAME_ADJ:GAS:boiling beetroot wine]
            [STATE_COLOR:ALL:CARMINE]
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
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:beet seed:beet seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:edible roots]
        [GROWTH:LEAVES]
            [GROWTH_NAME:beet leaf:beet leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:beet flower spike:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:2:0:0:60000:119999:2]
