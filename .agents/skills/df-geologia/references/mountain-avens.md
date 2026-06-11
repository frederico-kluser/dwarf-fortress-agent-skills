# Mountain avens

> Fonte: [Mountain avens](https://dwarffortresswiki.org/index.php/Mountain_avens) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Biome**
- **Mountain Tundra Taiga**
- **Location**
- **Wet Dry**
- **Wet:** Dry

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Mountain avens** is a type of grass that grows exclusively in otherwise inhospitable tundra and mountainous regions, as well as taigas. During the late spring it produces a growth, identical to cottongrass.

Mountain avens.

    *** need timing

    [PLANT:MOUNTAIN AVENS]
        [ALL_NAMES:mountain avens]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [GRASS]
        [GRASS_TILES:'.':',':'`':''']
        [GRASS_COLORS:2:0:1:2:0:0:6:0:1:6:0:0]
        [WET]
        [DRY]
        [BIOME:MOUNTAIN]
        [BIOME:TUNDRA]
        [BIOME:TAIGA]
        [GROWTH:BUD]
            [GROWTH_NAME:mountain avens bud:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:65000:74999]
            [GROWTH_PRINT:0:7:2:0:0:65000:74999:1]
        [GROWTH:FLOWER]
            [GROWTH_NAME:mountain avens flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:75000:100000]
            [GROWTH_PRINT:5:5:7:0:1:75000:100000:1]
