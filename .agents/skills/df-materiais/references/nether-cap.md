# Nether-cap

> Fonte: [Nether-cap](https://dwarffortresswiki.org/index.php/Nether-cap) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes nether-caps for their coldness to the touch.**
- **Biome**
- **Underground Depth: 3**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 550
- **Color:** dark indigo
- **Max trunk height:** 4
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 2
- **Branch density:** 10
- **Root density:** 5
- **Products**
- **Wood:** Nether-cap

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Nether-caps** are a type of mushroom-like subterranean tree. Once fully grown, they can be designated for wood cutting and produce nether-cap logs. They often grow on muddied rock in the 3rd underground cavern layer and, once discovered, will begin to grow in any suitable environment within your fortress as well.

Nether-caps and their products are dark indigo, and they have the unique property of being naturally cold, having a fixed temperature of 10000 °U (the freezing point of water). Most objects made from this wood are not massive enough to change the ambient temperature around them to this point, however, so nether-cap cannot cause water to turn into ice. This fixed temperature gives nether-cap wood a strange quasi-magma-safe quality. You can use nether-cap as a substitution for metal magma-safe components (for example, in a magma pump stack), but a nether-cap minecart will not resist magma, and nether-cap items dumped into magma will be destroyed. However, a magma-safe metal minecart filled with lava can be safely carried in a nether-cap wheelbarrow. Interestingly, nether-cap logs can still be burned into ash or charcoal at a wood furnace, and nether-cap items laying on the ground can be ignited by fire-breathing/throwing creatures.

Some dwarves like nether-caps for their *coldness to the touch*.

The trunk and top of a nether-cap tree.

    [PLANT:NETHER_CAP]
        [NAME:nether-cap][NAME_PLURAL:nether-caps][ADJ:nether-cap]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:1:0:0]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:nether-cap]
            [STATE_ADJ:ALL_SOLID:nether-cap]
            [PREFIX:NONE]
            [STATE_COLOR:ALL_SOLID:DARK_INDIGO]
            [DISPLAY_COLOR:1:0:0]
            [MAT_FIXED_TEMP:10000]
            [SOLID_DENSITY:550]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
        [TREE_HAS_MUSHROOM_CAP]
        [CAP_PERIOD:40]
        [CAP_RADIUS:1]
        [TRUNK_PERIOD:40]
        [MAX_TRUNK_HEIGHT:4]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:coldness to the touch]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:3:3]
        [TREE_COLOR:1:0:0]
        [DEAD_TREE_COLOR:0:0:1]
        [SAPLING_COLOR:1:0:0]
        [DEAD_SAPLING_COLOR:0:0:1]
