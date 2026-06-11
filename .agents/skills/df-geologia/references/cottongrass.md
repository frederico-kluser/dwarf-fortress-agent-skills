# Cottongrass

> Fonte: [Cottongrass](https://dwarffortresswiki.org/index.php/Cottongrass) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Biome**
- **Mountain Tundra**
- **Location**
- **Wet Dry**
- **Wet:** Dry

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Cottongrass** is a type of grass that grows exclusively in otherwise-inhospitable tundra and mountainous regions. During late spring it produces a growth, white cottongrass tufts. Unlike cotton, it cannot be used to produce thread.

|  |
|----|
| "Cottongrass" in other / Languages / Dwarven / : / îkeng-isin / Elven / : / ethe-enena / Goblin / : / ongu-struxe / Human / : / thixil-kege |

Cottongrass.

    [PLANT:COTTONGRASS]
        [ALL_NAMES:cottongrass]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [GRASS]
        [GRASS_TILES:'.':',':'`':''']
        [GRASS_COLORS:2:0:1:2:0:0:6:0:1:6:0:0]
        [WET]
        [DRY]
        [BIOME:MOUNTAIN]
        [BIOME:TUNDRA]
        [GROWTH:BUD]
            [GROWTH_NAME:cottongrass bud:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:65000:74999]
            [GROWTH_PRINT:0:7:2:0:0:65000:74999:1]
        [GROWTH:FLOWER]
            [GROWTH_NAME:cottongrass tuft:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:75000:100000]
            [GROWTH_PRINT:5:5:7:0:1:75000:100000:1]
