# Highwood

> Fonte: [Highwood](https://dwarffortresswiki.org/index.php/Highwood) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes highwoods for their magnificence.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Alignment**
- **Savage**
- **Properties**
- **Deciduous:** No
- **Density:** 500
- **Color:** green
- **Max trunk height:** 8
- **Max trunk diameter:** 3
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Highwood

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Highwoods** are a type of above ground tree found only in savage regions. Like the overwhelming majority of overland trees, highwood wood is brown and produces brown products. Highwoods are notable for their thick trunks, commonly measuring 2×2 or 3×3 tiles and extending upward (up to 12 z-levels) in a tangle of branches and wooden trunk. They bear pale blue flowers, but no fruit.

In spite of their much thicker trunks, they are far from guaranteed to drop more wood than other trees, especially when in a forest. Oak trees in particular seem to drop more, even though they have nearly identical stats except for the trunk diameter. Trunk diameter seems to have no effect on log production, and the thicker trunks seem to make them slower to grow and have more overlap in area with other trees. Hence, a faster-growing oak might produce 40 logs, compared to a highwood's 25, due to the highwood being crowded out.

Ironically, highwoods are more frequently found in savage deserts, due to the scarcity of tree species in these biomes, so highwoods happen in pretty much every savage desert biome that has trees.

Also, highwood height depends on your worldgen's end year, though it tends to be a problem only for very short history worlds.

Some dwarves like highwoods for their *magnificence*.

|  |
|----|
| "Highwood" in other / Languages / Dwarven / : / erlin-lolum / Elven / : / imama-ave / Goblin / : / aku-dôr / Human / : / sast-pado |

    *** need to support multi-mat egg growths, then we can use egg item instead of plant growth

    [PLANT:HIGHWOOD]
        [NAME:highwood][NAME_PLURAL:highwoods][ADJ:highwood]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:highwood]
            [STATE_ADJ:ALL_SOLID:highwood]
            [PREFIX:NONE]
            [SOLID_DENSITY:500]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:PALE_BLUE]
            [DISPLAY_COLOR:3:0:1]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:20]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:8] *** as much as supported
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:3]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:magnificence]
        [DRY][SAVAGE]
        [BIOME:NOT_FREEZING]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:highwood leaf:highwood leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:highwood flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:5:5:3:0:1:30000:99999:2]
