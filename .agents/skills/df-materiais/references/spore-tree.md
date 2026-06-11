# Spore tree

> Fonte: [Spore tree](https://dwarffortresswiki.org/index.php/Spore_tree) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes spore trees for their raining spores.**
- **Biome**
- **Underground Depth: 2-3**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 600
- **Color:** teal
- **Max trunk height:** 5
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Spore tree

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Spore trees** are a type of underground tree found in the deep caverns, and grow on muddied soil after they are found. When cut down, they yield teal logs suitable for producing colorful furniture.

Some dwarves like spore trees for their *raining spores*.

    [PLANT:SPORE_TREE]
        [NAME:spore tree][NAME_PLURAL:spore trees][ADJ:spore tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:3:0:0]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:spore tree]
            [STATE_ADJ:ALL_SOLID:spore tree]
            [PREFIX:NONE]
            [STATE_COLOR:ALL_SOLID:TEAL]
            [DISPLAY_COLOR:3:0:0]
            [SOLID_DENSITY:600]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:5]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:5]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:raining spores]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:2:3]
        [TREE_COLOR:3:0:0]
        [DEAD_TREE_COLOR:0:0:1]
        [SAPLING_COLOR:3:0:0]
        [DEAD_SAPLING_COLOR:0:0:1]
