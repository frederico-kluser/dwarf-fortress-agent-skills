# Cucumber

> Fonte: [Cucumber](https://dwarffortresswiki.org/index.php/Cucumber) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cucumber vines for their fruit.**
- **Seed**
- **/ Cucumber seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Tropical Dry Broadleaf Forest Tropical Grassland Tropical Savanna Tropical Shrubland**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Fruit:** Cucumber
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

**Cucumbers** are an aboveground garden plant. They can be planted in all seasons, and the fruit is edible raw or cooked.

Some dwarves like cucumber vines for their *fruit*.

\

Admired for its *fruit*.

    [PLANT:CUCUMBER] cucumis sativus, vine
        [NAME:cucumber vine][NAME_PLURAL:cucumber vines][ADJ:cucumber vine]
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
            [STATE_COLOR:ALL:YELLOW]
            [DISPLAY_COLOR:6:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:cucumber seed:cucumber seeds:7:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:fruit]
        [GROWTH:LEAVES]
            [GROWTH_NAME:cucumber leaf:cucumber leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:cucumber flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:6:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:cucumber:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF]
            [GROWTH_PRINT:'%':'%':2:0:0:120000:200000:3]
            [GROWTH_HAS_SEED]
