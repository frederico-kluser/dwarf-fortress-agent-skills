# Olive

> Fonte: [Olive](https://dwarffortresswiki.org/index.php/Olive) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes olive trees for their oil-giving fruit.**
- **Biome**
- **Any Tropical**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 990
- **Color:** pale brown
- **Max trunk height:** 3
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 25
- **Branch density:** 50
- **Root density:** 5
- **Products**
- **Wood:** Olive wood
- **Fruit:** Olive
- **Leaf:** Olive leaf
- **Oil:** Olive oil
- **Leaf Properties**
- **Edible:** No
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes
- **Seed Properties**
- **Edible:** No

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Olive** is one of the many genera of trees found above ground. Like the vast majority of above ground trees, olive wood is brown and produces brown products. Logs and leaves can be processed in a dyer's shop into woodland green dye.

Olive trees possess the third densest wood and the densest wood that isn't restricted to evil biomes or the deep caverns. This density makes olive wood a less optimal choice as a material for bins and other goods that need to be hauled regularly. Elves armed with olive wood arrows and weapons are slightly more dangerous to civilian dwarves than those made from other types of wood.

Olive fruit can be eaten raw, or can be pressed into olive oil and a unit of olive pomace at a screw press. Olives can be harvested by setting up a gathering zone.

Olive oil is much easier to produce than seed oils, as not only do olives not need to be milled first, but a stack of them can also be pressed in a single job, occupying only one jug. On the other hand, compared to seeds, there's less value increase, and your supply of olives is limited to whatever you can gather or import, whereas seeds are an often plentiful byproduct of farming, which is infinitely scalable.

Some dwarves like olive trees for their *oil-giving fruit*.

\

Admired for its *oil-giving fruit*.

|  |
|----|
| "Olive" in other / Languages / Dwarven / : / losush / Elven / : / naye / Goblin / : / dum / Human / : / lunda |

    [PLANT:OLIVE] olea europaea
        [NAME:olive tree][NAME_PLURAL:olive trees][ADJ:olive tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:OIL:PLANT_OIL_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:frozen olive oil]
            [STATE_NAME_ADJ:LIQUID:olive oil]
            [STATE_NAME_ADJ:GAS:boiling olive oil]
            [PREFIX:NONE]
            [MATERIAL_VALUE:5]
            [EDIBLE_COOKED]
        [USE_MATERIAL_TEMPLATE:SOAP:PLANT_SOAP_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:olive oil soap]
            [STATE_NAME_ADJ:LIQUID:melted olive oil soap]
            [STATE_NAME_ADJ:GAS:n/a]
            [PREFIX:NONE]
            [MATERIAL_VALUE:5]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:olive wood]
            [STATE_ADJ:ALL_SOLID:olive wood]
            [PREFIX:NONE]
            [SOLID_DENSITY:990] http://www.wood-database.com/olive/
            [STATE_COLOR:ALL_SOLID:PALE_BROWN] *** not yet searched
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:FERN_GREEN]
            [DISPLAY_COLOR:2:0:0]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:BEIGE]
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:FERN_GREEN]
            [DISPLAY_COLOR:0:0:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
            [STATE_NAME_ADJ:ALL_SOLID:olive fruit]
            [STATE_NAME_ADJ:SOLID_PRESSED:olive pomace]
            [PREFIX:NONE]
            [MATERIAL_REACTION_PRODUCT:PRESS_LIQUID_MAT:LOCAL_PLANT_MAT:OIL]
            [STOCKPILE_GLOB_PRESSED]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
        [SEED:olive pit:olive pits:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:3]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:oil-giving fruit]
        [DRY]
        [BIOME:ANY_TROPICAL]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:olive leaf:olive leaves]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:LEAF]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:2:0:0:ALL:1]
        [GROWTH:FLOWERS]
            [GROWTH_NAME:olive raceme:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:60000:119999]
            [GROWTH_PRINT:5:5:7:0:1:60000:119999:2]
        [GROWTH:FRUIT]
            [GROWTH_NAME:olive:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':'%':0:0:1:120000:200000:3]
            [GROWTH_HAS_SEED]
        [USE_MATERIAL_TEMPLATE:BARK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:olive bark dye]
            [STATE_COLOR:ALL_SOLID:WOODLAND_GREEN]
            [DISPLAY_COLOR:2:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:WOODLAND_GREEN]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:olive leaf dye]
            [STATE_COLOR:ALL_SOLID:WOODLAND_GREEN]
            [DISPLAY_COLOR:2:0:1]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:WOODLAND_GREEN]
            [PREFIX:NONE]
