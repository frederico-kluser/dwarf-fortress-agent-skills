# Elephant-head amaranth

> Fonte: [Elephant-head amaranth](https://dwarffortresswiki.org/index.php/Elephant-head_amaranth) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes elephant-head amaranths for their leaf coloration.**
- **Seed**
- **/ Elephant-head amaranth seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Leaf:** Elephant-head amaranth leaf
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Leaf Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Elephant-head amaranth** is an aboveground crop. They can be planted in all seasons, the leaves are edible raw or cooked, and the seeds when cooked.

Some dwarves like elephant-head amaranths for their *leaf coloration*.

\

Admired for its *leaf coloration*.

    [PLANT:ELEPHANT-HEAD_AMARANTH] Amaranthus tricolor
        [NAME:elephant-head amaranth][NAME_PLURAL:elephant-head amaranths][ADJ:elephant-head amaranth]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][BIOME:ANY_TROPICAL]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:DARK_VIOLET]
            [DISPLAY_COLOR:5:0:0]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:elephant-head amaranth seed:elephant-head amaranth seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:YELLOW] red-yellow-green pattern
            [DISPLAY_COLOR:6:0:1]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:leaf coloration]
        [GROWTH:LEAVES]
            [GROWTH_NAME:elephant-head amaranth leaf:elephant-head amaranth leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:6:0:1:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:elephant-head amaranth inflorescence:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:5:0:0:60000:119999:2]
