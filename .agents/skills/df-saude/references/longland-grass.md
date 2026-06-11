# Longland grass

> Fonte: [Longland grass](https://dwarffortresswiki.org/index.php/Longland_grass) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes Longland grass for their sweeping stalks.**
- **Seed**
- **/ Longland grass seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Longland beer
- **Powder:** Longland flour
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Alcohol Flour**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Longland grass** is an aboveground crop. It can be milled into Longland flour or brewed into Longland beer.

It is equal in value to underground crops and is much like an aboveground version of cave wheat, though its seeds take only about 25 days to grow, rather than the 42 required for cave wheat, and they can be planted in any season.

Some dwarves like Longland grass for its *sweeping stalks*.

## Trivia

The first letter of Longland is capitalized in the raw code for Longland grass, unlike all other plant and creature names, where the name and adjective definitions are all lowercase.

|  |
|----|
| "Longland grass" in other / Languages / Dwarven / : / romek-nïr isin / Elven / : / beresi-lina enena / Goblin / : / xom-smaksmo struxe / Human / : / inid-tar kege |

    [PLANT:GRASS_LONGLAND]
        [NAME:Longland grass][NAME_PLURAL:Longland grass][ADJ:Longland grass]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
            [EDIBLE_VERMIN]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:231][PICKED_COLOR:6:0:1]
        [DRY][BIOME:NOT_FREEZING]
        [VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen Longland beer]
            [STATE_NAME_ADJ:LIQUID:Longland beer]
            [STATE_NAME_ADJ:GAS:boiling Longland beer]
            [STATE_COLOR:ALL:AMBER]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:Longland flour]
            [STATE_COLOR:ALL_SOLID:WHITE]
            [DISPLAY_COLOR:7:0:1]
            [MATERIAL_VALUE:20]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [MILL:LOCAL_PLANT_MAT:MILL]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:Longland grass seed:Longland grass seeds:6:0:0:LOCAL_PLANT_MAT:SEED]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [PREFSTRING:sweeping stalks]
