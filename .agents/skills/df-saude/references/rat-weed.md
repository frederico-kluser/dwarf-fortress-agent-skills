# Rat weed

> Fonte: [Rat weed](https://dwarffortresswiki.org/index.php/Rat_weed) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rat weed for their hanging leaves.**
- **Seed**
- **/ Rat weed seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Sewer brew
- **Plant Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Food Alcohol**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Rat weed** is an inferior crop, on the level of muck roots and prickle berries. It can be eaten raw, cooked or made into sewer brew. However, it is not as delicious as any of the underground crops.

Rat weed is notable in that it has cookable seeds, providing both food and booze in one cheap item (although strawberries are better if they're also available), and making disposing of their seeds easier if you chose to embark on a biome where farming aboveground crops is impossible.

Some dwarves like rat weed for its *hanging leaves*.

|  |
|----|
| "Rat weed" in other / Languages / Dwarven / : / atem koshmot / Elven / : / thapa mibi / Goblin / : / spödgôz spålu / Human / : / othur thish |

    [PLANT:WEED_RAT]
        [NAME:rat weed][NAME_PLURAL:rat weed][ADJ:rat weed]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:231][PICKED_COLOR:2:0:0]
        [WET][BIOME:NOT_FREEZING]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen sewer brew]
            [STATE_NAME_ADJ:LIQUID:sewer brew]
            [STATE_NAME_ADJ:GAS:boiling sewer brew]
            [STATE_COLOR:ALL:BROWN]
            [MATERIAL_VALUE:1]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:hanging leaves]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:rat weed seed:rat weed seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
