# Jute

> Fonte: [Jute](https://dwarffortresswiki.org/index.php/Jute) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes jute plants for their fibrous stems.**
- **Seed**
- **/ Jute seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Paper:** Jute paper
- **Processed to:** Thread
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Thread**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Jute** is an aboveground crop. The plant may be processed at a farmer's workshop to produce jute plant fiber thread, which can then be woven into jute cloth. It can also be mashed into a slurry and pressed to produce jute paper.

Some dwarves like jute plants for their *fibrous stems*.

Admired for its *fibrous stems*.

## In real life

Jute is grown almost exclusively in India, Bangladesh, and other countries in South and Southeast Asia, because it is dependent upon monsoon rains as part of its life cycle. However, in the current version of *DF*, it merely requires tropical climates.

The fabric most associated with jute is burlap (or hessian), and its tough but rough fibers are frequently used in burlap sacks containing common goods. It is widely used to contain cotton bales, which are used to make clothing.

    [PLANT:JUTE] Corchorus capsularis / Corchorus olitorius
        [NAME:jute plant][NAME_PLURAL:jute plants][ADJ:jute plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_REACTION_PRODUCT:PRESS_PAPER_MAT:LOCAL_PLANT_MAT:THREAD]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][BIOME:ANY_TROPICAL]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL_SOLID:YELLOW]
            [DISPLAY_COLOR:6:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:jute seed:jute seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:fibrous stems]
        [USE_MATERIAL_TEMPLATE:THREAD:THREAD_PLANT_TEMPLATE] *** stems should be retted
            [STATE_NAME_ADJ:SOLID:jute]
            [STATE_NAME_ADJ:SOLID_PASTE:jute slurry]
            [STATE_NAME_ADJ:SOLID_PRESSED:jute paper]
            [PREFIX:NONE]
            [MATERIAL_VALUE:2]
            [REACTION_CLASS:PAPER_SLURRY]
            [STOCKPILE_GLOB_PASTE]
        [THREAD:LOCAL_PLANT_MAT:THREAD]
        [GROWTH:LEAVES]
            [GROWTH_NAME:jute leaf:jute leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:jute flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:6:0:1:60000:119999:2]
