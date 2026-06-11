# Sweet pod

> Fonte: [Sweet pod](https://dwarffortresswiki.org/index.php/Sweet_pod) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes sweet pods for their round shape.**
- **Seed**
- **/ Sweet pod seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Underground Depth: 1-3**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Dwarven rum
- **Extract:** Dwarven syrup
- **Powder:** Dwarven sugar
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Alcohol Flour Food**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Sweet pods** are a subterranean crop grown in spring and summer. Sweet pods can be ground at a millstone or quern into dwarven sugar or processed at the farmer's workshop into barrels of dwarven syrup.

Sweet pods can also be brewed into dwarven rum.

Five units of syrup are obtained for each sweet pod, but only one unit of sugar. However, sugar can serve as a solid ingredient in cooking, while syrup cannot.

- Grow time: 50000 Game Ticks (42 days)
- Plant value: 2
- Drink value: 2
- Mill value: 20
- Extract value: 20 (×5)
- Seed value: 1
- Seasons: Spring and Summer

Some dwarves like sweet pods for their *round shape*.

    [PLANT:POD_SWEET]
        [NAME:sweet pod][NAME_PLURAL:sweet pods][ADJ:sweet pod]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:232][PICKED_COLOR:4:0:1]
        [GROWDUR:500][VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen dwarven rum]
            [STATE_NAME_ADJ:LIQUID:dwarven rum]
            [STATE_NAME_ADJ:GAS:boiling dwarven rum]
            [STATE_COLOR:ALL:HELIOTROPE]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:5:0:1]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:dwarven sugar]
            [STATE_COLOR:ALL_SOLID:WHITE]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [MILL:LOCAL_PLANT_MAT:MILL]
        [USE_MATERIAL_TEMPLATE:EXTRACT:PLANT_EXTRACT_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen dwarven syrup]
            [STATE_NAME_ADJ:LIQUID:dwarven syrup]
            [STATE_NAME_ADJ:GAS:boiling dwarven syrup]
            [MATERIAL_VALUE:20]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [EXTRACT_STORAGE:BARREL]
            [PREFIX:NONE]
        [EXTRACT_BARREL:LOCAL_PLANT_MAT:EXTRACT]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:sweet pod seed:sweet pod seeds:2:0:1:LOCAL_PLANT_MAT:SEED]
        [SPRING][SUMMER]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:round shape]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:3]
        [SHRUB_TILE:58]
        [DEAD_SHRUB_TILE:58]
        [SHRUB_COLOR:4:0:1]
        [DEAD_SHRUB_COLOR:0:0:1]
