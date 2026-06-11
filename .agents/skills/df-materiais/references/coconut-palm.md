# Coconut palm

> Fonte: [Coconut palm](https://dwarffortresswiki.org/index.php/Coconut_palm) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes coconut palms for their leaves.**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 680
- **Color:** dark taupe
- **Max trunk height:** 8
- **Max trunk diameter:** 1
- **Trunk branching:** 0
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 0
- **Branch density:** 0
- **Root density:** 5
- **Products**
- **Wood:** Coconut palm
- **Fruit:** Coconut
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Coconut palms** are a type of above ground tree, that can be found in dry areas of any tropical biome. Like the overwhelming majority of overland trees, palm wood is brown and produces brown products.

Coconut palms produce coconuts that can be harvested by setting up a gathering zone. Coconuts are edible raw or cooked, but cannot be brewed. Unlike most other fruit trees, coconuts do not have seeds (technically, the edible part of the coconut is the seed and the fruit itself is inedible, but it isn't set as such in the raws, and dwarves still eat the entire fruit).

Some dwarves like coconut palms for their *leaves*.

\

Admired for its *leaves*.

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

There is often confusion over if the coconut nut is a big big nut or a coco fruit.\
Coconut palm wood is preferably used for building big houses for families.

    [PLANT:PALM]
        [NAME:coconut palm][NAME_PLURAL:coconut palms][ADJ:coconut palm]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:coconut palm]
            [STATE_ADJ:ALL_SOLID:coconut palm]
            [PREFIX:NONE]
            Based on Red Palm (Cocos nucifera)
            http://www.wood-database.com/lumber-identification/monocots/red-palm/
            [STATE_COLOR:ALL_SOLID:TAUPE_DARK]
            [SOLID_DENSITY:680]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:NUT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:BROWN]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:226]
        *** coir (from coconut husks) - fiber, from coconut
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:0]
        [BRANCH_DENSITY:0]
        [MAX_TRUNK_HEIGHT:8]
        [TRUNK_BRANCHING:0]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:leaves]
        [DRY]
        [BIOME:ANY_TROPICAL]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:coconut palm frond blade:coconut palm frond blades]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:TRUNK]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_TRUNK_HEIGHT_PERC:100:-1]
            [GROWTH_PRINT:'*':'*':2:0:0:ALL:1]
        [GROWTH:SPATHES]
            [GROWTH_NAME:coconut palm spathe:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1]
            [GROWTH_HOST_TILE:TRUNK]
            [GROWTH_TIMING:50000:99999]
            [GROWTH_TRUNK_HEIGHT_PERC:100:-1]
            [GROWTH_PRINT:5:5:2:0:0:50000:99999:2]
            *** contain flowers
        [GROWTH:FRUIT]
            [GROWTH_NAME:coconut:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:NUT]
            [GROWTH_DENSITY:1]
            [GROWTH_HOST_TILE:TRUNK]
            [GROWTH_TIMING:100000:200000]
            [GROWTH_TRUNK_HEIGHT_PERC:100:-1]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':7:6:0:0:100000:200000:3]
