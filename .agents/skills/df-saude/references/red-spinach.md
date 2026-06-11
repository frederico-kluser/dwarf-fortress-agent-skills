# Red spinach

> Fonte: [Red spinach](https://dwarffortresswiki.org/index.php/Red_spinach) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes red spinach for their leaves.**
- **Seed**
- **/ Red spinach seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Leaf:** Red spinach leaf
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

**Red spinach** is an aboveground crop found in any biome except mountains, glaciers, and tundras. They are gathered and harvested as plants which can be processed at a Farmer's workshop to produce seeds and leaves or processed in a dyer's shop into fuchsia dye. Seeds can be sown in all seasons, the leaves are edible raw or cooked, and seeds when cooked.

*Some dwarves like red spinach for its leaves*.

Admired for its *leaves*.

    [PLANT:RED_SPINACH] Amaranthus dubius
        [NAME:red spinach][NAME_PLURAL:red spinach][ADJ:red spinach]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][BIOME:NOT_FREEZING]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:red spinach seed:red spinach seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:leaves]
        [GROWTH:LEAVES]
            [GROWTH_NAME:red spinach leaf:red spinach leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:red spinach inflorescence:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:2:0:1:60000:119999:2]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:red spinach leaf dye]
            [STATE_COLOR:ALL_SOLID:FUCHSIA]
            [DISPLAY_COLOR:5:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:FUCHSIA]
            [PREFIX:NONE]
