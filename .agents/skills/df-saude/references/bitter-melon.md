# Bitter melon

> Fonte: [Bitter melon](https://dwarffortresswiki.org/index.php/Bitter_melon) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bitter melon vines for their taste.**
- **Seed**
- **/ Bitter melon seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Fruit:** Bitter melon
- **Leaf:** Bitter melon leaf
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Leaf Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Fruit Properties**
- **Edible:** No
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Bitter melons**, also known as goya, are an aboveground garden plant. They can be planted in all seasons, and grow leaves and a melon. The melon can be edible after being cooked, but the leaves are edible raw or cooked.

Some dwarves like bitter melon vines for their *taste*.

\

Admired for its *taste*.

    [PLANT:BITTER_MELON] momordica charantia, vine, can be used in place of hops in beer
        [NAME:bitter melon vine][NAME_PLURAL:bitter melon vines][ADJ:bitter melon vine]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:1]
        [DRY][BIOME:ANY_TROPICAL]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:YELLOW]
            [DISPLAY_COLOR:6:0:1]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE] leaves are edible
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE] melon
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:bitter melon seed:bitter melon seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:taste]
        [GROWTH:LEAVES]
            [GROWTH_NAME:bitter melon leaf:bitter melon leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:1:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:bitter melon flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:6:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:bitter melon:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF]
            [GROWTH_PRINT:'%':'%':2:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
