# Sorghum

> Fonte: [Sorghum](https://dwarffortresswiki.org/index.php/Sorghum) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sorghum for their beer.**
- **Seed**
- **/ Sorghum seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Tropical Grassland Tropical Savanna**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Sorghum beer
- **Leaf:** Sorghum leaf
- **Powder:** Sorghum flour
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Leaf Properties**
- **Edible:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Alcohol Flour**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Sorghum** is an aboveground crop found only in some tropical biomes. It is a type of grain and can either be milled into sorghum flour, brewed into sorghum beer or processed in a dyer's shop into rust dye.

Some dwarves like sorghum for its *beer*.

\

Admired for its *beer*.

    [PLANT:SORGHUM] sorghum bicolor
        [NAME:sorghum][NAME_PLURAL:sorghum][ADJ:sorghum]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [DRY][BIOME:GRASSLAND_TROPICAL][BIOME:SAVANNA_TROPICAL]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen sorghum beer]
            [STATE_NAME_ADJ:LIQUID:sorghum beer]
            [STATE_NAME_ADJ:GAS:boiling sorghum beer]
            [STATE_COLOR:ALL:AMBER]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:sorghum flour]
            [STATE_COLOR:ALL_SOLID:WHITE]
            [DISPLAY_COLOR:7:0:1]
            [MATERIAL_VALUE:20]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [MILL:LOCAL_PLANT_MAT:MILL]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:PURPLE]
            [DISPLAY_COLOR:5:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:sorghum seed:sorghum seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        *** grain can be popped
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:beer]
        [GROWTH:LEAVES]
            [GROWTH_NAME:sorghum leaf:sorghum leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:sorghum flower cluster:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:5:0:1:60000:119999:2]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:sorghum leaf dye]
            [STATE_COLOR:ALL_SOLID:RUST]
            [DISPLAY_COLOR:4:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:RUST]
            [PREFIX:NONE]
