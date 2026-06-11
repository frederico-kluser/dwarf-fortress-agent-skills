# Mahogany

> Fonte: [Mahogany](https://dwarffortresswiki.org/index.php/Mahogany) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes mahoganies for their loose inflorescences.**
- **Biome**
- **Any Tropical Forest**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 600
- **Color:** mahogany
- **Max trunk height:** 8
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Mahogany

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Mahogany** is a type of above ground tree; only found in tropical forests. Like the overwhelming majority of overland trees, mahogany wood is brown and produces brown products. Logs can be processed in a dyer's shop into mahogany dye.

Some dwarves like mahoganies for their *loose inflorescences*.

Admired for its *loose inflorescences*.

|  |
|----|
| "Mahogany" in other / Languages / Dwarven / : / sezom / Elven / : / enefi / Goblin / : / stusmex / Human / : / quoshas |

    [PLANT:MAHOGANY]
        [NAME:mahogany][NAME_PLURAL:mahoganies][ADJ:mahogany]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:mahogany]
            [STATE_ADJ:ALL_SOLID:mahogany]
            [PREFIX:NONE]
            Based on African Mahogany (Khaya grandifoliola and K. senegalensis)
            http://www.fpl.fs.fed.us/documnts/TechSheets/Chudnoff/African/htmlDocs_africa/khayagrandi.html
            [STATE_COLOR:ALL_SOLID:MAHOGANY]
            [SOLID_DENSITY:600]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:YELLOW]
            [DISPLAY_COLOR:6:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:BROWN]
            [DISPLAY_COLOR:6:0:0]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:8]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:loose inflorescences]
        [DRY]
        [BIOME:ANY_TROPICAL_FOREST]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:mahogany leaf:mahogany leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:mahogany flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:50000:99999]
            [GROWTH_PRINT:0:5:6:0:1:NONE]
        [GROWTH:FRUIT]
            [GROWTH_NAME:mahogany fruit:mahogany fruit]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:100000:300000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:0:7:6:0:0:NONE]
        [USE_MATERIAL_TEMPLATE:BARK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:mahogany bark dye]
            [STATE_COLOR:ALL_SOLID:MAHOGANY]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:MAHOGANY]
            [PREFIX:NONE]
