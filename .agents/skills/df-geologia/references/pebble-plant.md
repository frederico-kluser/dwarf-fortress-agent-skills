# Pebble plant

> Fonte: [Pebble plant](https://dwarffortresswiki.org/index.php/Pebble_plant) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Biome**
- **Any Desert**
- **Location**
- **Wet Dry**
- **Wet:** Dry

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Pebble plant** is a type of grass that grows exclusively in deserts. It can have yellow flowers.

|  |
|----|
| "Pebble plant" in other / Languages / Dwarven / : / ib erok / Elven / : / ata mana / Goblin / : / aba tusnas / Human / : / reb ona |

Pebble plants.

    [PLANT:PEBBLE PLANTS]
        Lithops
        [NAME:pebble plant][NAME_PLURAL:pebble plants][ADJ:pebble plant]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [GRASS]
        [GRASS_TILES:'.':',':'`':''']
        [GRASS_COLORS:2:0:1:2:0:0:2:0:0:6:0:0]
        [WET]
        [DRY]
        [BIOME:ANY_DESERT]
        [GROWTH:BUD]
            [GROWTH_NAME:pebble plant bud:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:240000:249999]
            [GROWTH_PRINT:0:7:2:0:0:240000:249999:1]
        [GROWTH:FLOWER]
            [GROWTH_NAME:pebble plant flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_TIMING:250000:260000]
            [GROWTH_PRINT:5:5:6:0:1:250000:260000:1]
