# Chestnut

> Fonte: [Chestnut](https://dwarffortresswiki.org/index.php/Chestnut) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes chestnuts for their smelly catkins.**
- **Biome**
- **Any Temperate Broadleaf**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** Yes
- **Density:** 430
- **Color:** dark chestnut
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
- **Wood:** Chestnut
- **Leaf:** Chestnut leaf
- **Nut:** Chestnut burr
- **Leaf Properties**
- **Edible:** No
- **Seed Properties**
- **Edible:** Yes
- **Cookable:** Yes

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Chestnuts** are a type of tree found in dry areas of temperate forests. Like the overwhelming majority of overland trees, chestnut wood is brown and produces brown products.

Chestnut trees produce **Chestnut leaves** and **Chestnut burrs**, which — together with logs — can be used in a dyer's shop to make dark brown dye.

Some dwarves like chestnuts for their *spiny pods*, their *smelly catkins*, their *chestnuts* and their *autumn coloration*. So yes, you can have a dwarf who redundantly "likes chestnuts for their chestnuts".

\

Admired for its *spiny pods*.

|  |
|----|
| "Chestnut" in other / Languages / Dwarven / : / gingik / Elven / : / bisi / Goblin / : / ukad / Human / : / cubra |

    [PLANT:CHESTNUT]
        [NAME:chestnut][NAME_PLURAL:chestnuts][ADJ:chestnut]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:chestnut]
            [STATE_ADJ:ALL_SOLID:chestnut]
            [PREFIX:NONE]
            Based on American Chestnut (Castanea dentata)
            http://www.fpl.fs.fed.us/documnts/TechSheets/HardwoodNA/htmlDocs/CASTAN.html
            [SOLID_DENSITY:430]
            [STATE_COLOR:ALL_SOLID:DARK_CHESTNUT]
        [USE_MATERIAL_TEMPLATE:LEAF:LEAF_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:2:0:0]
            [STOCKPILE_PLANT_GROWTH]
        [USE_MATERIAL_TEMPLATE:SEED:SEED_TEMPLATE]
            [STATE_COLOR:ALL:CHESTNUT]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [SEED:chestnut:chestnuts:6:0:0:LOCAL_PLANT_MAT:SEED]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
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
        [PREFSTRING:smelly catkins]
        [PREFSTRING:spiny pods]
        [PREFSTRING:chestnuts]
        [PREFSTRING:autumn coloration]
        [DRY]
        [BIOME:ANY_TEMPERATE_BROADLEAF]
        [SAPLING]
        [GROWTH:LEAVES]
            [GROWTH_NAME:chestnut leaf:chestnut leaves]
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
        [GROWTH:POLLEN_CATKINS]
            [GROWTH_NAME:chestnut pollen catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:'*':'*':7:0:1:30000:99999:3]
        [GROWTH:SEED_CATKINS]
            [GROWTH_NAME:chestnut seed catkin:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:'*':'*':7:0:1:30000:99999:2]
        [GROWTH:NUT]
            [GROWTH_NAME:chestnut burr:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:STRUCTURAL]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:100000:250000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'*':'*':2:0:0:NONE]
            [GROWTH_HAS_SEED]
            *** spiny green burr, three nuts inside
        [USE_MATERIAL_TEMPLATE:BARK_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:chestnut bark dye]
            [STATE_COLOR:ALL_SOLID:DARK_BROWN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:DARK_BROWN]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:LEAF_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:chestnut leaf dye]
            [STATE_COLOR:ALL_SOLID:DARK_BROWN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:DARK_BROWN]
            [PREFIX:NONE]
        [USE_MATERIAL_TEMPLATE:HULL_DYE:PLANT_POWDER_TEMPLATE]
            [STATE_NAME_ADJ:ALL_SOLID:chestnut hull dye]
            [STATE_COLOR:ALL_SOLID:DARK_BROWN]
            [DISPLAY_COLOR:6:0:0]
            [MATERIAL_VALUE:20]
            [POWDER_DYE:DARK_BROWN]
            [PREFIX:NONE]
