# Bloated tuber

> Fonte: [Bloated tuber](https://dwarffortresswiki.org/index.php/Bloated_tuber) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bloated tubers for their stout shape.**
- **Seed**
- **/ Bloated tuber seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Wetland**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Tuber beer
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Food Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Bloated tubers** are an aboveground plant. They can be eaten raw, cooked or brewed into ~~vodka~~ tuber beer.

Bloated tubers produce seeds and can be farmed.

- Plant value: 2
- Drink value: 2
- Seasons: All

Some dwarves like bloated tubers for their *stout shape*.

In real life, an example of a tuber is the potato.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

Bloated tubers are colloquially referred to as couch potatoes.

    [PLANT:TUBER_BLOATED]
        [NAME:bloated tuber][NAME_PLURAL:bloated tubers][ADJ:bloated tuber]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:232][PICKED_COLOR:6:0:0]
        [DRY][BIOME:ANY_WETLAND]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen tuber beer]
            [STATE_NAME_ADJ:LIQUID:tuber beer]
            [STATE_NAME_ADJ:GAS:boiling tuber beer]
            [STATE_COLOR:ALL:PEACH]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:7:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:bloated tuber seed:bloated tuber seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:stout shape]
