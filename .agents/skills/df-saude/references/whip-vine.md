# Whip vine

> Fonte: [Whip vine](https://dwarffortresswiki.org/index.php/Whip_vine) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes whip vines for their length.**
- **Seed**
- **/ Whip vine seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Alignment**
- **Savage**
- **Products**
- **Alcohol:** Whip wine
- **Powder:** Whip vine flour
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Alcohol Flour**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Whip vines** are an above ground crop only found in savage areas, and may be planted at any time of the year, or gathered from outdoor shrubs. They cannot be eaten raw, but can be brewed or milled.

Whip wine, brewed from whip vines, is more valuable than any alcohol brewed from underground crops, and whip vine flour is the most valuable flour product available.

Some dwarves like whip vines for their *length*.

Admired for its *length*.

|  |
|----|
| "Whip vine" in other / Languages / Dwarven / : / bomrek lemis / Elven / : / baci fewetha / Goblin / : / sox alba / Human / : / uthret gili |

    [PLANT:VINE_WHIP]
        [NAME:whip vine][NAME_PLURAL:whip vines][ADJ:whip vine]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:1]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:21][PICKED_COLOR:3:0:1]
        [DRY][SAVAGE][BIOME:NOT_FREEZING]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen whip wine]
            [STATE_NAME_ADJ:LIQUID:whip wine]
            [STATE_NAME_ADJ:GAS:boiling whip wine]
            [STATE_COLOR:ALL:SKY_BLUE]
            [MATERIAL_VALUE:3]
            [DISPLAY_COLOR:3:0:1]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:whip vine flour]
            [STATE_COLOR:ALL_SOLID:AZURE]
            [DISPLAY_COLOR:3:0:1]
            [MATERIAL_VALUE:25]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [MILL:LOCAL_PLANT_MAT:MILL]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:length]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:whip vine seed:whip vine seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
