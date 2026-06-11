# Muskmelon

> Fonte: [Muskmelon](https://dwarffortresswiki.org/index.php/Muskmelon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes muskmelon vines for their fruit.**
- **Seed**
- **/ Muskmelon seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Temperate Tropical Dry Broadleaf Forest Tropical Grassland Tropical Savanna Tropical Shrubland**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Fruit:** Muskmelon
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

**Muskmelon** is an aboveground garden vegetable. The seeds can be planted in a farm plot in all seasons. They grow into muskmelon vines, which can be harvested and processed at a farmer's workshop into muskmelons and more seeds. The melon is edible raw or cooked.

Some dwarves like muskmelon vines for their *fruit*.

\

Admired for its *fruit*.

    [PLANT:MUSKMELON] cucumis melo (many many cultivars)
        [NAME:muskmelon vine][NAME_PLURAL:muskmelon vines][ADJ:muskmelon vine]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:0]
        [DRY][BIOME:ANY_TEMPERATE][BIOME:FOREST_TROPICAL_DRY_BROADLEAF][BIOME:GRASSLAND_TROPICAL][BIOME:SAVANNA_TROPICAL][BIOME:SHRUBLAND_TROPICAL]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:YELLOW]
            [DISPLAY_COLOR:6:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:GRAY]
            [DISPLAY_COLOR:7:0:0]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:muskmelon seed:muskmelon seeds:7:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:fruit]
        [GROWTH:LEAVES]
            [GROWTH_NAME:muskmelon leaf:muskmelon leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:muskmelon flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:6:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:muskmelon:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF]
            [GROWTH_PRINT:'%':'%':7:0:0:120000:200000:3]
            [GROWTH_HAS_SEED]
