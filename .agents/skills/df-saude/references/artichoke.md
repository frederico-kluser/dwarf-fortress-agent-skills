# Artichoke

> Fonte: [Artichoke](https://dwarffortresswiki.org/index.php/Artichoke) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes artichokes for their yummy hearts.**
- **Seed**
- **/ Artichoke seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Temperate Grassland**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Artichoke wine
- **Heart:** Artichoke heart
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Heart Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Food Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Artichokes** are an aboveground garden vegetable. They can be planted in all seasons and grow a purple flower, leaves, and an artichoke heart. The artichoke heart is edible raw or cooked, and can also be brewed into artichoke wine. Seeds can only retrieved from brewing, not from eating raw hearts.

Some dwarves like artichokes for their *yummy hearts*.

\

Admired for their *yummy hearts*.

    [PLANT:ARTICHOKE] cynara cardunculus
        [NAME:artichoke][NAME_PLURAL:artichokes][ADJ:artichoke]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:0]
        [DRY][BIOME:GRASSLAND_TEMPERATE]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen artichoke wine]
            [STATE_NAME_ADJ:LIQUID:artichoke wine]
            [STATE_NAME_ADJ:GAS:boiling artichoke wine]
            [STATE_COLOR:ALL:FLAX]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:HEART:FRUIT_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:PURPLE]
            [DISPLAY_COLOR:5:0:0]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
        [SEED:artichoke seed:artichoke seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:yummy hearts]
        [GROWTH:LEAVES]
            [GROWTH_NAME:artichoke leaf:artichoke leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:HEART]
            [GROWTH_NAME:artichoke heart:STP] bud not fruit
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:HEART]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:0:59999]
            [GROWTH_PRINT:'%':'%':4:0:1:0:59999:3]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:artichoke flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:5:0:1:60000:119999:2]
