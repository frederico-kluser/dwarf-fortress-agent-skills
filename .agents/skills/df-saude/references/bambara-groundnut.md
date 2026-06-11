# Bambara groundnut

> Fonte: [Bambara groundnut](https://dwarffortresswiki.org/index.php/Bambara_groundnut) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bambara groundnut plants for their edible nuts.**
- **Seed**
- **/ Bambara groundnuts**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Tropical Dry Broadleaf Forest Tropical Grassland Tropical Savanna Tropical Shrubland**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Bambara groundnut** is an aboveground garden plant. They can be planted in all seasons. Only the cooked seeds are edible.

Some dwarves like bambara groundnut plants for their *edible nuts*.

### Bugs

Although the seed material definition marks them as being edible raw, dwarves will not eat them.

\

Admired for its *edible nuts*.

    [PLANT:BAMBARA_GROUNDNUT] vigna subterranea
        [NAME:bambara groundnut plant][NAME_PLURAL:bambara groundnut plants][ADJ:bambara groundnut plant]
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
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [SEED:bambara groundnut:bambara groundnuts:6:0:0:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:edible nuts]
        [GROWTH:LEAVES]
            [GROWTH_NAME:bambara groundnut leaf:bambara groundnut leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:bambara groundnut flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:6:0:1:60000:119999:2]
        [GROWTH:FRUIT] should bury itself in the ground (geocarpy)
            [GROWTH_NAME:bambara groundnut pod:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF]
            [GROWTH_PRINT:'%':'%':6:0:0:120000:200000:3]
            [GROWTH_HAS_SEED]
