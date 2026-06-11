# Cassava

> Fonte: [Cassava](https://dwarffortresswiki.org/index.php/Cassava) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes cassavas for their roots.**
- **Seed**
- **/ Cassava seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Cassava beer
- **Plant Properties**
- **Edible:** No
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Alcohol Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Cassava** is an aboveground garden plant. They can be planted in all seasons, only the plant is edible when cooked, and can also be brewed into cassava beer.

This is to reflect that in real life the raw plant contains poisonous cyanogenic glycosides, which need to be leached out of the plant before consumption.

Some dwarves like cassavas for their *roots*.

\

Admired for its *roots*.

    [PLANT:CASSAVA] manihot esculenta
        [NAME:cassava][NAME_PLURAL:cassavas][ADJ:cassava]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED] must be boiled
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:0]
        [DRY][BIOME:ANY_TROPICAL]
        [VALUE:2]
        *** mill to cassava flour
        *** squeeze extract dried as tapioca
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen cassava beer]
            [STATE_NAME_ADJ:LIQUID:cassava beer]
            [STATE_NAME_ADJ:GAS:boiling cassava beer]
            [STATE_COLOR:ALL:AMBER]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:PINK]
            [DISPLAY_COLOR:5:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:cassava seed:cassava seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:roots]
        [GROWTH:LEAVES]
            [GROWTH_NAME:cassava leaf:cassava leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:cassava flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:5:0:1:60000:119999:2]
