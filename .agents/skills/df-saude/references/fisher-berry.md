# Fisher berry

> Fonte: [Fisher berry](https://dwarffortresswiki.org/index.php/Fisher_berry) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes fisher berries for their round shape.**
- **Seed**
- **/ Fisher berry seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Fisher berry wine
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Food Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Fisher Berries** are a type of aboveground crop. They can be found by harvesting or by trading, or be grown on a surface farm plot. They can be consumed directly, or brewed into fisher berry wine and are stored in the 'Plants' section of food stockpiles.

Some dwarves like fisher berries for their *round shape*.

Came for the berries, stayed for how round they are.

|  |
|----|
| "Fisher berry" in other / Languages / Dwarven / : / ngitkar lisig / Elven / : / nenití ada / Goblin / : / sposm smug / Human / : / edin tikbo |

    [PLANT:BERRIES_FISHER]
        [NAME:fisher berry][NAME_PLURAL:fisher berries][ADJ:fisher berry]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:58][PICKED_COLOR:7:0:0]
        [WET][BIOME:NOT_FREEZING]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen fisher berry wine]
            [STATE_NAME_ADJ:LIQUID:fisher berry wine]
            [STATE_NAME_ADJ:GAS:boiling fisher berry wine]
            [STATE_COLOR:ALL:SAFFRON]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:1]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:round shape]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:fisher berry seed:fisher berry seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
