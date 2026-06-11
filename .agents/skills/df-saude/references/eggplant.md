# Eggplant

> Fonte: [Eggplant](https://dwarffortresswiki.org/index.php/Eggplant) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes eggplants for their fruit.**
- **Seed**
- **/ Eggplant seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Tropical Dry Broadleaf Forest Tropical Grassland Tropical Savanna Tropical Shrubland**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Fruit:** Eggplant
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Eggplants** are an aboveground garden plant. They can be planted in all seasons and the seeds and fruit are edible raw or cooked. Fruits also can be processed in a dyer's shop into lilac dye.

Some dwarves like eggplants for their *fruit*.

Admired for its *fruit*.

|  |
|----|
| "Eggplant" in other / Languages / Dwarven / : / acöb-erok / Elven / : / amira-mana / Goblin / : / donsmok-tusnas / Human / : / edi-ona |

    [PLANT:EGGPLANT] solanum melongena
        [NAME:eggplant][NAME_PLURAL:eggplants][ADJ:eggplant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:0]
        [DRY][BIOME:FOREST_TROPICAL_DRY_BROADLEAF][BIOME:GRASSLAND_TROPICAL][BIOME:SAVANNA_TROPICAL][BIOME:SHRUBLAND_TROPICAL]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:PURPLE]
            [DISPLAY_COLOR:5:0:0]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:EGGPLANT]
            [DISPLAY_COLOR:5:0:0]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [SEED:eggplant seed:eggplant seeds:7:0:0:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:fruit]
        [GROWTH:LEAVES]
            [GROWTH_NAME:eggplant leaf:eggplant leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:eggplant flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:5:0:0:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:eggplant:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF]
            [GROWTH_PRINT:'%':'%':5:0:0:120000:200000:3]
            [GROWTH_HAS_SEED]
        [USE_MATERIAL_TEMPLATE:FRUIT_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:eggplant dye]
            [STATE_COLOR:ALL_SOLID:LILAC]
            [DISPLAY_COLOR:5:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:LILAC]
            [PREFIX:NONE]
