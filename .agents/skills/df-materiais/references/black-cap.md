# Black-cap

> Fonte: [Black-cap](https://dwarffortresswiki.org/index.php/Black-cap) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes black-caps for their gloomy appeal.**
- **Biome**
- **Underground Depth: 2-3**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 650
- **Color:** black
- **Max trunk height:** 3
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 2
- **Branch density:** 10
- **Root density:** 5
- **Products**
- **Wood:** Black-cap

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Black-caps** are a type of underground tree found in the lower levels of caverns near the water. Unsurprisingly, they yield black logs when cut down. Due to their color, live black-caps saplings are indistinguishable from trampled ones.

Some dwarves like black-caps for their *gloomy appeal*.

    [PLANT:BLACK_CAP]
        [NAME:black-cap][NAME_PLURAL:black-caps][ADJ:black-cap]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:0:0:1]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:black-cap]
            [STATE_ADJ:ALL_SOLID:black-cap]
            [PREFIX:NONE]
            [STATE_COLOR:ALL_SOLID:BLACK]
            [DISPLAY_COLOR:0:0:1]
            [SOLID_DENSITY:650]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
        [TREE_HAS_MUSHROOM_CAP]
        [CAP_PERIOD:40]
        [CAP_RADIUS:2]
        [TRUNK_PERIOD:30]
        [MAX_TRUNK_HEIGHT:3]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:gloomy appeal]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:2:3]
        [TREE_COLOR:0:0:1]
        [DEAD_TREE_COLOR:0:0:1]
        [SAPLING_COLOR:0:0:1]
        [DEAD_SAPLING_COLOR:0:0:1]
