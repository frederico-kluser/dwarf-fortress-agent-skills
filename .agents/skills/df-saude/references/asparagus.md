# Asparagus

> Fonte: [Asparagus](https://dwarffortresswiki.org/index.php/Asparagus) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes asparagus for their delicious shoots.**
- **Seed**
- **/ Asparagus seeds**
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

**Asparagus** is an aboveground garden vegetable. It can be planted in all seasons, and is edible raw or cooked.

Some dwarves like asparagus for their *delicious shoots*.

\

Admired for its *delicious shoots*.

    [PLANT:ASPARAGUS] asparagus officinalis
        [NAME:asparagus][NAME_PLURAL:asparagus][ADJ:asparagus]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE] *** should be the young shoots in spring only
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:0]
        [DRY][BIOME:ANY_TEMPERATE]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:YELLOW] greenish white to yellowish
            [DISPLAY_COLOR:6:0:1]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE] poisonous
            [STATE_COLOR:ALL:RED]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
        [SEED:asparagus seed:asparagus seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:delicious shoots]
        [GROWTH:LEAVES]
            [GROWTH_NAME:asparagus leaf:asparagus leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:asparagus flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:6:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:asparagus berry:asparagus berries]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF]
            [GROWTH_PRINT:'%':'%':4:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
