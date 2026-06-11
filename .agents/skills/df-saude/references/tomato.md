# Tomato

> Fonte: [Tomato](https://dwarffortresswiki.org/index.php/Tomato) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes tomato plants for their fruit.**
- **Seed**
- **/ Tomato seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Tropical Dry Broadleaf Forest**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Tomato wine
- **Fruit:** Tomato
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Food Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Tomatoes** are an aboveground garden vegetable. They can be planted in all seasons, the fruit is edible raw or cooked, (seeds when cooked), and can also be brewed into tomato wine or processed in a dyer's shop into amber dye.

Some dwarves like tomato plants for their *fruit*.

Note that this plant, along with buckwheat, is only found in worlds with poles and a Medium or Large size, since it's unique to the Tropical Dry Broadleaf forest biome which only generates under those conditions due to a bug.

Admired for its *fruit*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Tomatoes are often employed by throwing them at performers with low comedian skill who attempt to tell jokes.

    [PLANT:TOMATO] solanum lycopersicum
        [NAME:tomato plant][NAME_PLURAL:tomato plants][ADJ:tomato plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:0]
        [DRY][BIOME:FOREST_TROPICAL_DRY_BROADLEAF]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen tomato wine]
            [STATE_NAME_ADJ:LIQUID:tomato wine]
            [STATE_NAME_ADJ:GAS:boiling tomato wine]
            [STATE_COLOR:ALL:FLAX]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:4:0:1]
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
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:RED]
            [DISPLAY_COLOR:4:0:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:tomato seed:tomato seeds:7:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:fruit]
        [GROWTH:LEAVES]
            [GROWTH_NAME:tomato leaf:tomato leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:tomato flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:6:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:tomato:tomatoes]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF]
            [GROWTH_PRINT:'%':'%':4:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
        [USE_MATERIAL_TEMPLATE:SKIN_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:tomato skin dye]
            [STATE_COLOR:ALL_SOLID:AMBER]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:AMBER]
            [PREFIX:NONE]
