# Baby toes succulent

> Fonte: [Baby toes succulent](https://dwarffortresswiki.org/index.php/Baby_toes_succulent) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Biome**
- **Any Desert**
- **Location**
- **Wet Dry**
- **Wet:** Dry

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Baby toes succulent** is a type of grass exclusive to desert environments. It can grow white flowers.

## In real life

There are various common names, such as babies' toes or window plant. Each leaf has a leaf window, a transparent window-like area, at its rounded tip, it is for these window-like structures that the genus is named (Latin: fenestra). In the wild, the plant commonly grows under sand, except for the transparent tips, which allow light into the leaves for photosynthesis. Fenestraria rhopalophylla is native to Namaqualand in southern Africa and to Namibia. The plants generally grow in sandy or calciferous soils under low \< 100 mm rainfall.

A normal plant with a strange name.

    [PLANT:BABY TOES SUCCULENT]
        Fenestraria
        [NAME:baby toes succulent][NAME_PLURAL:baby toes succulents][ADJ:baby toes succulent]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [GRASS]
        [GRASS_TILES:'.':',':'`':''']
        [GRASS_COLORS:2:0:1:2:0:0:2:0:0:6:0:0]
        [WET]
        [DRY]
        [BIOME:ANY_DESERT]
        [GROWTH:BUD]
            [GROWTH_NAME:baby toes succulent bud:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:240000:249999]
            [GROWTH_PRINT:0:7:2:0:0:240000:249999:1]
        [GROWTH:FLOWER]
            [GROWTH_NAME:baby toes succulent flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:250000:260000]
            [GROWTH_PRINT:5:5:7:0:1:250000:260000:1]
