# Passion fruit

> Fonte: [Passion fruit](https://dwarffortresswiki.org/index.php/Passion_fruit) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes passion fruit vines for their fruit.**
- **Seed**
- **/ Passion fruit seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Passion fruit wine
- **Fruit:** Passion fruit
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Passion fruits** are an aboveground garden plant. They can be planted in all seasons, are edible raw or cooked, and can also be brewed into passion fruit wine.

Passion Fruits are stockpiled in the 'Fruit/Leaves' section in food stockpiles. In the stocks menu, it's listed under 'Leaves'.

Some dwarves like passion fruit vines for their *fruit*.

Admired for its *fruit*.

|  |
|----|
| "Passion fruit" in other / Languages / Dwarven / : / ishen dozeb / Elven / : / siva ile / Goblin / : / snukang utmak / Human / : / hethre par |

    [PLANT:PASSION_FRUIT] passiflora edulis
        [NAME:passion fruit vine][NAME_PLURAL:passion fruit vines][ADJ:passion fruit vine]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:1]
        [DRY][BIOME:ANY_TROPICAL]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen passion fruit wine]
            [STATE_NAME_ADJ:LIQUID:passion fruit wine]
            [STATE_NAME_ADJ:GAS:boiling passion fruit wine]
            [STATE_COLOR:ALL:CREAM]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:PURPLE] white + purple interior
            [DISPLAY_COLOR:5:0:1]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:RED_PURPLE]
            [DISPLAY_COLOR:4:0:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:passion fruit seed:passion fruit seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:fruit]
        [GROWTH:LEAVES]
            [GROWTH_NAME:passion fruit leaf:passion fruit leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:1:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:passion fruit flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:5:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:passion fruit:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF]
            [GROWTH_PRINT:'%':'%':4:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
