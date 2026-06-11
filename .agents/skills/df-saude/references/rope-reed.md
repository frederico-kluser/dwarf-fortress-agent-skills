# Rope reed

> Fonte: [Rope reed](https://dwarffortresswiki.org/index.php/Rope_reed) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes rope reeds for their precise lines.**
- **Seed**
- **/ Rope reed seeds**
- **Seasons**
- **Spring Summer Autumn Winter**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Products**
- **Alcohol:** River spirits
- **Paper:** Rope reed paper
- **Processed to:** Thread
- **Plant Properties**
- **Edible:** No
- **Cookable:** No
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes
- **Uses**
- **Alcohol Thread**

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Rope reeds** is an aboveground crop. It is useful for producing cloth and paper. They can also be brewed into river spirits, an affordably priced drink. You will likely be able to collect by gathering plants near a river or pool if you're in a temperate biome, but it may be easier if in a less hospitable enviroment to trade for the plants or seeds from a (non-dwarven) caravan, especially an elven one.

To produce rope reed cloth, the plants must be processed into threads at a farmer's workshop. Processing plants will yield both rope reed thread and seeds. Rope reed thread can then be woven into cloth at a loom. To produce paper sheets, it needs to be mashed into a slurry with a millstone or a quern and then pressed on a screw press.

Some dwarves like rope reeds for their *precise lines*.

    [PLANT:REED_ROPE]
        [NAME:rope reed][NAME_PLURAL:rope reeds][ADJ:rope reed]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [MATERIAL_VALUE:2]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
            [MATERIAL_REACTION_PRODUCT:PRESS_PAPER_MAT:LOCAL_PLANT_MAT:THREAD]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [PICKED_TILE:159][PICKED_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen river spirits]
            [STATE_NAME_ADJ:LIQUID:river spirits]
            [STATE_NAME_ADJ:GAS:boiling river spirits]
            [STATE_COLOR:ALL:YELLOW_GREEN]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:1]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [WET][BIOME:NOT_FREEZING]
        [VALUE:2]
        [SPRING][SUMMER][AUTUMN][WINTER]
        [FREQUENCY:50]
        [CLUSTERSIZE:5]
        [USE_MATERIAL_TEMPLATE:THREAD:THREAD_PLANT_TEMPLATE]
            [STATE_NAME_ADJ:SOLID:rope reed]
            [STATE_NAME_ADJ:SOLID_PASTE:rope reed slurry]
            [STATE_NAME_ADJ:SOLID_PRESSED:rope reed paper]
            [PREFIX:NONE]
            [MATERIAL_VALUE:2]
            [REACTION_CLASS:PAPER_SLURRY]
            [STOCKPILE_GLOB_PASTE]
        [THREAD:LOCAL_PLANT_MAT:THREAD]
        [PREFSTRING:precise lines]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [EDIBLE_VERMIN]
            [EDIBLE_COOKED]
        [SEED:rope reed seed:rope reed seeds:6:0:0:LOCAL_PLANT_MAT:SEED]
