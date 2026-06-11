# Pig tail

> Fonte: [Pig tail](https://dwarffortresswiki.org/index.php/Pig_tail) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes pig tails for their twisting stalks.**
- **Seed**
- **/ Pig tail seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Underground Depth: 1-3**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** Dwarven ale
- **Paper:** Pig tail paper
- **Processed to:** Thread
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Thread Alcohol Slurry**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Pig tails** are underground crops that can be gathered in the caverns and farmed only in summer and autumn. They may be brewed into dwarven ale; processed at a farmer's workshop to create pig tail thread, which can then be dyed or used to weave pig tail cloth at a loom; or mashed into slurry at a quern or millstone, which can then be pressed into paper at a screw press.

Some dwarves like pig tails for their *twisting stalks*.

## See also

- Alcohol
- Clothing industry
- Paper industry

|  |
|----|
| "Pig tail" in other / Languages / Dwarven / : / thuveg kesh / Elven / : / sano yawo / Goblin / : / dul ostusm / Human / : / pum duto |

    [PLANT:GRASS_TAIL_PIG]
        [NAME:pig tail][NAME_PLURAL:pig tails][ADJ:pig tail]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
            [MATERIAL_REACTION_PRODUCT:PRESS_PAPER_MAT:LOCAL_PLANT_MAT:THREAD]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:231][PICKED_COLOR:7:0:0]
        [GROWDUR:300][VALUE:2]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen dwarven ale]
            [STATE_NAME_ADJ:LIQUID:dwarven ale]
            [STATE_NAME_ADJ:GAS:boiling dwarven ale]
            [STATE_COLOR:ALL:PEARL]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:7:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:pig tail seed:pig tail seeds:0:0:1:LOCAL_PLANT_MAT:SEED]
        [SUMMER][AUTUMN]
        [FREQUENCY:100]
        [CLUSTERSIZE:5]
        [USE_MATERIAL_TEMPLATE:THREAD:THREAD_PLANT_TEMPLATE]
            [STATE_NAME_ADJ:SOLID:pig tail]
            [STATE_NAME_ADJ:SOLID_PASTE:pig tail slurry]
            [STATE_NAME_ADJ:SOLID_PRESSED:pig tail paper]
            [PREFIX:NONE]
            [REACTION_CLASS:PAPER_SLURRY]
            [MATERIAL_VALUE:2]
            [STOCKPILE_GLOB_PASTE]
        [THREAD:LOCAL_PLANT_MAT:THREAD]
        [PREFSTRING:twisting stalks]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:3]
        [SHRUB_TILE:58]
        [DEAD_SHRUB_TILE:58]
        [SHRUB_COLOR:7:0:0]
        [DEAD_SHRUB_COLOR:0:0:1]
