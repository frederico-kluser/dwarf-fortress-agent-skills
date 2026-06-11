# Purple yam

> Fonte: [Purple yam](https://dwarffortresswiki.org/index.php/Purple_yam) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes purple yam plants for their tubers.**
- **Seed**
- **/ Purple yam seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Plant Properties**
- **Edible:** No
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Purple yams** are an aboveground garden plant. They can be planted in all seasons and are edible when cooked.

Some dwarves like purple yam plants for their *tubers*.

\

Admired for its *tubers*.

    [PLANT:PURPLE_YAM] dioscorea alata
        [NAME:purple yam plant][NAME_PLURAL:purple yam plants][ADJ:purple yam plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE] the tuber, must be cooked
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:5:0:0]
        [DRY][BIOME:ANY_TROPICAL]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:WHITE]
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:purple yam seed:purple yam seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:tubers]
        [GROWTH:LEAVES]
            [GROWTH_NAME:purple yam leaf:purple yam leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:purple yam flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:7:0:1:60000:119999:2]
