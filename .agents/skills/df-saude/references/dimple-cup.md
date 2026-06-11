# Dimple cup

> Fonte: [Dimple cup](https://dwarffortresswiki.org/index.php/Dimple_cup) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes dimple cups for their soothing color.**
- **Seed**
- **/ Dimple cup spawn**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Underground Depth: 1-3**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Powder:** Dimple dye
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Dye**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Dimple cup** is a subterranean crop. It can be grown year-round and can be milled into blue dimple dye.

- Grow time: 500
- Plant value: 2
- Mill value: 20
- Dye color: Midnight Blue
- Seasons: All

Some dwarves like dimple cups for their *soothing color*.

## Gallery

-

  Dimple cup farm plot.

## See Also

- List of crops
- Textile industry

|  |
|----|
| "Dimple cup" in other / Languages / Dwarven / : / storlut ôfid / Elven / : / thace dima / Goblin / : / nor kux / Human / : / lapip wem |

    [PLANT:MUSHROOM_CUP_DIMPLE]
        [NAME:dimple cup][NAME_PLURAL:dimple cups][ADJ:dimple cup]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:3][PICKED_COLOR:1:0:1]
        [GROWDUR:500][VALUE:2]
        [USE_MATERIAL_TEMPLATE:MILL:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:dimple dye]
            [STATE_COLOR:ALL_SOLID:MIDNIGHT_BLUE]
            [DISPLAY_COLOR:1:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:MIDNIGHT_BLUE]
            [PREFIX:NONE]
        [MILL:LOCAL_PLANT_MAT:MILL]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:dimple cup spawn:dimple cup spawn:5:0:1:LOCAL_PLANT_MAT:SEED]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [PREFSTRING:soothing color]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:3]
        [SHRUB_TILE:58]
        [DEAD_SHRUB_TILE:58]
        [SHRUB_COLOR:1:0:1]
        [DEAD_SHRUB_COLOR:0:0:1]
