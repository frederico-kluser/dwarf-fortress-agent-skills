# Candlenut

> Fonte: [Candlenut](https://dwarffortresswiki.org/index.php/Candlenut) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes candlenuts for their nuts.**
- **Biome**
- **Any Tropical Forest**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 140
- **Color:** ochre
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
- **Wood:** Candlenut
- **Nut:** Candlenut
- **Seed Properties**
- **Edible:** No
- **Cookable:** Yes

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **candlenut** is a tree only found in tropical forests. Like the overwhelming majority of overland trees, candlenut wood is brown and produces brown products. Candlenut is the third lightest wood, beaten by papayas and feather trees.

Candlenut seeds can be harvested by setting up a plant gathering zone, but as the seeds need to be cooked before they are eaten, candlenut trees may be best used as wood.

Some dwarves like candlenuts for their *nuts*.

Admired for its *nuts*.

Aleurites moluccana.

|     |
|-----|
|     |

|  |
|----|
| "Candlenut" in other / Languages / Dwarven / : / tílgil-ishlum / Elven / : / erela-apasi / Goblin / : / gunsmom-stasoz / Human / : / kofi-sas |

    [PLANT:CANDLENUT]
        [NAME:candlenut][NAME_PLURAL:candlenuts][ADJ:candlenut]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:candlenut]
            [STATE_ADJ:ALL_SOLID:candlenut]
            [PREFIX:NONE]
            Based on Aleurites moluccana
            http://www.thewoodexplorer.com/maindata/we71.html
            [SOLID_DENSITY:140]
            [STATE_COLOR:ALL_SOLID:OCHRE]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:WHITE]
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:1]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            mildly toxic if raw
            [EDIBLE_COOKED]
        [SEED:candlenut:candlenuts:2:0:1:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:226]
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
        [PREFSTRING:nuts]
        [DRY]
        [BIOME:ANY_TROPICAL_FOREST]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:candlenut leaf:candlenut leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:candlenut flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:40000:99999]
            [GROWTH_PRINT:5:5:7:0:1:40000:99999:2]
        [GROWTH:NUT]
            [GROWTH_NAME:candlenut:STP]
            [GROWTH_ITEM:SEEDS:NONE:LOCAL_PLANT_MAT:SEED]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:100000:250000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:0:7:6:0:0:NONE]
