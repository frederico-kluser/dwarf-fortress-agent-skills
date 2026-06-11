# Bitter orange

> Fonte: [Bitter orange](https://dwarffortresswiki.org/index.php/Bitter_orange) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes bitter orange trees for their fruit.**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 590
- **Color:** pale taupe
- **Max trunk height:** 2
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Bitter orange wood
- **Fruit:** Bitter orange
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Bitter orange** is one of the many genera of trees found above-ground. Like the vast majority of above-ground trees, bitter orange wood is brown and produces brown products.

Bitter orange trees bear **bitter oranges** that can be harvested by setting up a gathering zone.

Some dwarves like bitter orange trees for their *fruit*.

\

Admired for its *fruit*.

|  |
|----|
| "Bitter orange" in other / Languages / Dwarven / : / räduk mostib / Elven / : / ufithe ÿare / Goblin / : / zuspu tustong / Human / : / ikash omthu |

    [PLANT:BITTER_ORANGE] poncirus trifoliata
        [NAME:bitter orange tree][NAME_PLURAL:bitter orange trees][ADJ:bitter orange tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:bitter orange wood]
            [STATE_ADJ:ALL_SOLID:bitter orange wood]
            [PREFIX:NONE]
            [SOLID_DENSITY:590] http://www.fao.org/docrep/w4095e/w4095e0c.htm Did Citrus grandis wood density - same genus but couldn't find any for Citrus aurantifolia
            [STATE_COLOR:ALL_SOLID:TAUPE_PALE] *** not yet searched
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:SEA_GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:BEIGE]
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:ORANGE]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
        [SEED:bitter orange seed:bitter orange seeds:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:2]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:fruit]
        [DRY]
        [BIOME:ANY_TROPICAL]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:bitter orange leaf:bitter orange leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:bitter orange flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:7:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:bitter orange:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':6:0:0:120000:200000:3]
            [GROWTH_HAS_SEED]
