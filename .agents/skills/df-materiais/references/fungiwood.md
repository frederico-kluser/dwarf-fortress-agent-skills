# Fungiwood

> Fonte: [Fungiwood](https://dwarffortresswiki.org/index.php/Fungiwood) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes fungiwoods for their fine grain.**
- **Biome**
- **Underground Depth: 1-2**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 600
- **Color:** lemon
- **Max trunk height:** 8
- **Max trunk diameter:** 1
- **Trunk branching:** 0
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 0
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Fungiwood

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **fungiwood** is an underground tree, likely related to the tower-cap.

It is found in underground caverns, providing lemon-colored wood, and can also grow on soil or muddied rock.

Some dwarves like fungiwoods for their *fine grain*.

|  |
|----|
| "Fungiwood" in other / Languages / Dwarven / : / muz-lolum / Elven / : / arari-ave / Goblin / : / ësmor-dôr / Human / : / meplul-pado |

    [PLANT:FUNGIWOOD]
        [NAME:fungiwood][NAME_PLURAL:fungiwoods][ADJ:fungiwood]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:6:0:1]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:fungiwood]
            [STATE_ADJ:ALL_SOLID:fungiwood]
            [PREFIX:NONE]
            [STATE_COLOR:ALL_SOLID:LEMON]
            [DISPLAY_COLOR:6:0:1]
            [SOLID_DENSITY:600]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:5]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:0]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:8]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:0]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:fine grain]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:2]
        [TREE_COLOR:6:0:1]
        [DEAD_TREE_COLOR:0:0:1]
        [SAPLING_COLOR:6:0:1]
        [DEAD_SAPLING_COLOR:0:0:1]
