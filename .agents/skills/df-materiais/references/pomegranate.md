# Pomegranate

> Fonte: [Pomegranate](https://dwarffortresswiki.org/index.php/Pomegranate) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes pomegranate trees for their fruit.**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** Yes
- **Density:** 770
- **Color:** peach
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
- **Wood:** Pomegranate wood
- **Fruit:** Pomegranate
- **Leaf:** Pomegranate leaf
- **Alcohol:** Pomegranate wine
- **Leaf Properties**
- **Edible:** No
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Pomegranate** is one of the many genera of trees found above ground. Like the vast majority of above ground trees, pomegranate wood is brown and produces brown products.

Pomegranate trees bear pomegranate fruit that can be harvested by setting up a gathering zone. They can be eaten raw, cooked, or brewed into pomegranate wine.

Logs, leaves and fruits can be processed in a dyer's shop into different dyes - logs for gray, leaves for yellow and fruits for green-yellow.

Some dwarves like pomegranate trees for their *fruit*.

\

Admired for its *fruit*.

    [PLANT:POMEGRANATE] punica granatum
        [NAME:pomegranate tree][NAME_PLURAL:pomegranate trees][ADJ:pomegranate tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:pomegranate wood]
            [STATE_ADJ:ALL_SOLID:pomegranate wood]
            [PREFIX:NONE]
            [SOLID_DENSITY:770] http://eol.org/pages/582971/overview
            [STATE_COLOR:ALL_SOLID:PEACH] *** not yet searched
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen pomegranate wine]
            [STATE_NAME_ADJ:LIQUID:pomegranate wine]
            [STATE_NAME_ADJ:GAS:boiling pomegranate wine]
            [STATE_COLOR:ALL:CARDINAL]
            [MATERIAL_VALUE:2]
            [DISPLAY_COLOR:6:0:0]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [PREFIX:NONE]
        [DRINK:LOCAL_PLANT_MAT:DRINK]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:EMERALD]
            [DISPLAY_COLOR:2:0:0]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:SAFFRON]
            [DISPLAY_COLOR:4:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:VERMILION]
            [DISPLAY_COLOR:4:0:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
        [SEED:pomegranate seed:pomegranate seeds:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:226]
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
            [GROWTH_NAME:pomegranate leaf:pomegranate leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_TIMING:0:300000]
            [GROWTH_PRINT:0:6:2:0:0:0:209999:1]
            [GROWTH_PRINT:0:6:6:0:1:210000:239999:1] autumn color
            [GROWTH_PRINT:0:6:4:0:1:240000:269999:1]
            [GROWTH_PRINT:0:6:4:0:0:270000:300000:1]
            [GROWTH_DROPS_OFF]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:pomegranate flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:4:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:pomegranate:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':4:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:pomegranate leaf dye]
            [STATE_COLOR:ALL_SOLID:YELLOW]
            [DISPLAY_COLOR:6:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:YELLOW]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:RIND_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:pomegranate rind dye]
            [STATE_COLOR:ALL_SOLID:GREEN-YELLOW]
            [DISPLAY_COLOR:2:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:GREEN-YELLOW]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:BARK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:pomegranate bark dye]
            [STATE_COLOR:ALL_SOLID:GRAY]
            [DISPLAY_COLOR:7:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:GRAY]
            [PREFIX:NONE]
