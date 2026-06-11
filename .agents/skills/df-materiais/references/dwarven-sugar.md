# Dwarven sugar

> Fonte: [Dwarven sugar](https://dwarffortresswiki.org/index.php/Dwarven_sugar) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Dwarven Sugar** is a cookable item made by milling sweet pods. Milling plants needs one bag for every job, and one plant will be processed to make one bag of sugar. Sugar in bags or mill barrels does not wither like crops, and possesses an indefinite shelf life if kept free of vermin. It is also a very efficient use of space, since a single barrel can store up to ten bags of sugar. However, unless you have a severe shortage of barrels it is better to make dwarven syrup rather than sugar, as the two sweet pod products have the same value of 20☼ and both can be cooked, but syrup has five times the yield. On the other hand, dwarven sugar is considered a solid substrate for cooking, where syrup is not. Be warned that dwarven syrup is currently difficult to use for cooking. Bug:2393

Sugar will be used in the kitchen when 'prepare meal' tasks are queued if it is enabled in the Kitchen tab in the Status screen. Sugar is more valuable than the raw crop (20☼ per unit), and prepared meals made with sugar have a higher value. Bags and barrels of sugar are often quite valuable and suitable for export or import with caravans; a single barrel of sugar can easily be worth more than 200☼.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Sweet pods are planted in spring and summer, to be harvested, stored, and processed during the fall in preparation for the lean winter months. +Sugar roast+ is a traditional dish of Goblin Christmas, enjoyed by good little dwarves while they wait for Goblin Claus to leave his presents outside in the perimeter traps.

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
