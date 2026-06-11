# Meadowsweet

> Fonte: [Meadowsweet](https://dwarffortresswiki.org/index.php/Meadowsweet) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Biome**
- **Any Temperate Marsh Temperate Grassland**
- **Location**
- **Wet Dry**
- **Wet:** Dry

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Meadowsweet** is a type of grass that grows in temperate marshes and grasslands. It can have white flowers.

|  |
|----|
| "Meadowsweet" in other / Languages / Dwarven / : / kenis-tecàk / Elven / : / pari-tira / Goblin / : / stobux -xospo / Human / : / ethba-ciko |

Meadowsweet.

    [PLANT:MEADOWSWEET]
        [ALL_NAMES:meadowsweet]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [GRASS]
        [GRASS_TILES:'.':',':'`':''']
        [GRASS_COLORS:2:0:1:2:0:0:6:0:1:6:0:0]
        [WET]
        [DRY]
        [BIOME:ANY_TEMPERATE_MARSH]
        [BIOME:GRASSLAND_TEMPERATE]
        [GROWTH:BUD]
            [GROWTH_NAME:meadowsweet bud:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:140000:149999]
            [GROWTH_PRINT:0:7:2:0:0:140000:149999:1]
        [GROWTH:FLOWER]
            [GROWTH_NAME:meadowsweet flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:150000:250000]
            [GROWTH_PRINT:5:5:7:0:1:150000:250000:1]
