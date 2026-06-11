# Cloudberry

> Fonte: [Cloudberry](https://dwarffortresswiki.org/index.php/Cloudberry) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Biome**
- **Mountain Tundra Taiga**
- **Location**
- **Wet Dry**
- **Wet:** Dry

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Cloudberry** is a type of grass that grows exclusively in otherwise inhospitable tundra and mountainous regions, as well as taigas. It has white flowers, but, unlike its real-life counterpart, does not produce edible berries.

|  |
|----|
| "Cloudberry" in other / Languages / Dwarven / : / lun-lisig / Elven / : / atera-ada / Goblin / : / ëstraz-smug / Human / : / atal-tikbo |

Cloudberry.

    [PLANT:CLOUDBERRY]
        [NAME:cloudberry][NAME_PLURAL:cloudberries][ADJ:cloudberry]
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
            [GROWTH_NAME:cloudberry bud:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:240000:249999]
            [GROWTH_PRINT:0:7:2:0:0:240000:249999:1]
        [GROWTH:FLOWER]
            [GROWTH_NAME:cloudberry flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:250000:300000]
            [GROWTH_PRINT:5:5:7:0:1:250000:300000:1]
