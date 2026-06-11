# Banana

> Fonte: [Banana](https://dwarffortresswiki.org/index.php/Banana) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes banana trees for their fruit.**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 500
- **Color:** amber
- **Max trunk height:** 5
- **Max trunk diameter:** 1
- **Trunk branching:** 0
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 0
- **Branch density:** 0
- **Root density:** 5
- **Products**
- **Fruit:** Banana
- **Leaf:** Banana leaf
- **Alcohol:** Banana beer
- **Leaf Properties**
- **Edible:** No
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Banana trees** are one of the many genera of trees found above ground in tropical biomes. Unlike most trees, it produces no wood (*owing to the fact that this 'tree' is, in truth, an overstated shrub*), though it does produce a well-known fruit which can be eaten raw, cooked, or brewed into banana beer. As these fruits have seeds, they are likely the lesser-known wild banana. Leaves and fruits can be processed in a dyer's shop into ochre dye.

Some dwarves like banana trees for their *fruit*.

\

Admired for its *fruit*.

\

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Banana peels are especially dangerous to wagons, and are sometimes seen trailing behind them.

Some say that a banana firmly lodged in a dwarf's ear can significantly reduce stress. So far the tests to prove the claim are inconclusive, as the subjects tend to bleed out before an effect can be observed.

    [PLANT:BANANA] musa acuminata, ancestor of cultivated bananas
        [NAME:banana tree][NAME_PLURAL:banana trees][ADJ:banana tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        no wood
        [USE_MATERIAL_TEMPLATE:DRINK:PLANT_ALCOHOL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen banana beer] also wine
            [STATE_NAME_ADJ:LIQUID:banana beer]
            [STATE_NAME_ADJ:GAS:boiling banana beer]
            [STATE_COLOR:ALL:AMBER]
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
            [STATE_COLOR:ALL:MAUVE]
            [DISPLAY_COLOR:4:0:0]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:GOLDENROD]
            [DISPLAY_COLOR:6:0:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
            [MATERIAL_REACTION_PRODUCT:DRINK_MAT:LOCAL_PLANT_MAT:DRINK]
            [MATERIAL_REACTION_PRODUCT:SEED_MAT:LOCAL_PLANT_MAT:SEED]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
        [SEED:banana seed:banana seeds:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TREE:NONE:NONE][TREE_TILE:226]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:0]
        [BRANCH_DENSITY:0]
        [MAX_TRUNK_HEIGHT:5]
        [TRUNK_BRANCHING:0]
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
            [GROWTH_NAME:banana leaf:banana leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:TRUNK]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:banana flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:TRUNK]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:4:0:0:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:banana:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:TRUNK]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':6:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:banana leaf dye]
            [STATE_COLOR:ALL_SOLID:OCHRE]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:OCHRE]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:PEEL_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:banana peel dye]
            [STATE_COLOR:ALL_SOLID:OCHRE]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:OCHRE]
            [PREFIX:NONE]
