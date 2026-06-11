# Goblin-cap

> Fonte: [Goblin-cap](https://dwarffortresswiki.org/index.php/Goblin-cap) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes goblin-caps for their stunning color.**
- **Biome**
- **Underground Depth: 2-3**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 600
- **Color:** red
- **Max trunk height:** 1
- **Max trunk diameter:** 3
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 2
- **Branch density:** 10
- **Root density:** 5
- **Products**
- **Wood:** Goblin-cap

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Goblin-caps** are a type of underground tree found in the second and third levels of the caverns near the water, bearing no relation to goblins. When cut down, they yield red logs suitable for producing colorful furniture.

Some dwarves like goblin-caps for their *stunning color*.

    [PLANT:GOBLIN_CAP]
        [NAME:goblin-cap][NAME_PLURAL:goblin-caps][ADJ:goblin-cap]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:4:0:1]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:goblin-cap]
            [STATE_ADJ:ALL_SOLID:goblin-cap]
            [PREFIX:NONE]
            [STATE_COLOR:ALL_SOLID:RED]
            [DISPLAY_COLOR:4:0:1]
            [SOLID_DENSITY:600]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
        [TREE_HAS_MUSHROOM_CAP]
        [CAP_PERIOD:30]
        [CAP_RADIUS:3]
        [TRUNK_PERIOD:20]
        [MAX_TRUNK_HEIGHT:1]
        [MAX_TRUNK_DIAMETER:3]
        [TRUNK_WIDTH_PERIOD:200]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:stunning color]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:2:3]
        [TREE_COLOR:4:0:1]
        [DEAD_TREE_COLOR:0:0:1]
        [SAPLING_COLOR:4:0:1]
        [DEAD_SAPLING_COLOR:0:0:1]
