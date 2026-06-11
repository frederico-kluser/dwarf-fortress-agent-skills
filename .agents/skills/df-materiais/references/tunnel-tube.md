# Tunnel tube

> Fonte: [Tunnel tube](https://dwarffortresswiki.org/index.php/Tunnel_tube) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes tunnel tubes for their curving trunk.**
- **Biome**
- **Underground Depth: 2-3**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 500
- **Color:** violet
- **Max trunk height:** 8
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 0
- **Branch density:** 0
- **Root density:** 5
- **Products**
- **Wood:** Tunnel tube

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Tunnel tubes** are a type of underground tree. They are found in deep caverns, and will grow on any muddied rock or soil once found. When cut down, they yield violet logs suitable for producing colorful furniture. (Note that, in ASCII mode, rose gold is the same color, and can also be used to create furniture other than beds, so if you are able to create it, breaching the second cavern layer may not be necessary.)

Some dwarves like tunnel tubes for their *curving trunk*.

|  |
|----|
| "Tunnel tube" in other / Languages / Dwarven / : / ód-ecem / Elven / : / thateme-cinami / Goblin / : / zutôsp-ospe / Human / : / gujeg-ilum |

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
Tunnel tubes, unlike certain other tubes, are not known to be sources of Hidden Fun Stuff. There have yet to be recordings of woodcutters stumbling upon any orange-haired nature-aligned creatures ruthlessly-protective of nature. For underground trees, the concept is silly anyway (despite what certain groups might say), since it doesn't take longer than 20 years and 10 months for an underground tree to fully grow.

    [PLANT:TUNNEL_TUBE]
        [NAME:tunnel tube][NAME_PLURAL:tunnel tubes][ADJ:tunnel tube]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:5:0:1]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:tunnel tube]
            [STATE_ADJ:ALL_SOLID:tunnel tube]
            [PREFIX:NONE]
            [STATE_COLOR:ALL_SOLID:VIOLET]
            [DISPLAY_COLOR:5:0:1]
            [SOLID_DENSITY:500]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:179]
        [TRUNK_PERIOD:7]
        [HEAVY_BRANCH_DENSITY:0]
        [BRANCH_DENSITY:0]
        [MAX_TRUNK_HEIGHT:8]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:curving trunk]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:2:3]
        [TREE_COLOR:5:0:1]
        [DEAD_TREE_COLOR:0:0:1]
        [SAPLING_COLOR:5:0:1]
        [DEAD_SAPLING_COLOR:0:0:1]
