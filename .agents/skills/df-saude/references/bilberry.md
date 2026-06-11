# Bilberry

> Fonte: [Bilberry](https://dwarffortresswiki.org/index.php/Bilberry) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bilberry bushes for their fruit.**
- **Seed**
- **/ Bilberry seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any Temperate Tundra Taiga**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Bilberry wine
- **Fruit:** Bilberry
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Uses**
- **Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Bilberries** are an aboveground garden vegetable that highly resembles blueberries. They can be planted in all seasons, the fruit is edible raw or cooked, and can also be brewed into bilberry wine, or processed in a dyer's shop into violet dye.

When processed at a farmer's workshop, bilberry bushes produce bilberries and seeds.

They are among the very few crops that can be grown in a tundra environment.

Some dwarves like bilberry bushes for their *fruit*.

\

Admired for its *fruit*.

    [PLANT:BILBERRY] vaccinium myrtillus
        [NAME:bilberry bush][NAME_PLURAL:bilberry bushes][ADJ:bilberry bush]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:2:0:1]
        [DRY][BIOME:ANY_TEMPERATE][BIOME:TUNDRA][BIOME:TAIGA]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen bilberry wine]
            [STATE_NAME_ADJ:LIQUID:bilberry wine]
            [STATE_NAME_ADJ:GAS:boiling bilberry wine]
            [STATE_COLOR:ALL:DARK_SCARLET]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:PINK]
            [DISPLAY_COLOR:5:0:1]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:BLUE]
            [DISPLAY_COLOR:1:0:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
        [SEED:bilberry seed:bilberry seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:fruit]
        [GROWTH:LEAVES]
            [GROWTH_NAME:bilberry leaf:bilberry leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_PRINT:0:6:2:0:1:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:bilberry flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:5:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:bilberry:bilberries]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF]
            [GROWTH_PRINT:'%':'%':1:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
        [USE_MATERIAL_TEMPLATE:FRUIT_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:bilberry dye]
            [STATE_COLOR:ALL_SOLID:VIOLET]
            [DISPLAY_COLOR:5:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:VIOLET]
            [PREFIX:NONE]
