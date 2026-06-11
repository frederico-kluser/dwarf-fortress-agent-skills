# Carambola

> Fonte: [Carambola](https://dwarffortresswiki.org/index.php/Carambola) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes carambola trees for their fruit.**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 550
- **Color:** flax
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
- **Wood:** Carambola wood
- **Fruit:** Carambola
- **Alcohol:** Carambola wine
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Carambola** (also called starfruit) is one of the many genera of trees found above ground. Like the vast majority of above ground trees, carambola wood is brown and produces brown products.

Carambola trees bear carambola fruit that can be harvested by setting up a gathering zone. They can be eaten raw, cooked, or brewed into carambola wine.

Some dwarves like carambola trees for their *fruit*.

\

Admired for its *fruit*.

    [PLANT:CARAMBOLA] Averrhoa carambola
        [NAME:carambola tree][NAME_PLURAL:carambola trees][ADJ:carambola tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:carambola wood]
            [STATE_ADJ:ALL_SOLID:carambola wood]
            [PREFIX:NONE]
            [SOLID_DENSITY:550] *** http://eol.org/pages/483574/overview
            [STATE_COLOR:ALL_SOLID:FLAX] *** surprisingly hard to find pictures
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen carambola wine]
            [STATE_NAME_ADJ:LIQUID:carambola wine]
            [STATE_NAME_ADJ:GAS:boiling carambola wine]
            [STATE_COLOR:ALL:GOLDEN_YELLOW]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:EMERALD]
            [DISPLAY_COLOR:2:0:0]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:DARK_PINK]
            [DISPLAY_COLOR:3:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:YELLOW_GREEN]
            [DISPLAY_COLOR:2:0:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
        [SEED:carambola seed:carambola seeds:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:226]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:5]
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
            [GROWTH_NAME:carambola leaf:carambola leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:carambola flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:3:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:carambola:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':2:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
