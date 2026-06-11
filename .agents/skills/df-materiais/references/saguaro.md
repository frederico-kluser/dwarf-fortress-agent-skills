# Saguaro

> Fonte: [Saguaro](https://dwarffortresswiki.org/index.php/Saguaro) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes saguaros for their amazing arms.**
- **Biome**
- **Any Desert**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 430
- **Color:** ecru
- **Max trunk height:** 8
- **Max trunk diameter:** 1
- **Trunk branching:** 0
- **Heavy branch radius:** 3
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 50
- **Branch density:** 0
- **Root density:** 5
- **Products**
- **Wood:** Saguaro rib wood
- **Fruit:** Saguaro fruit
- **Fruit Properties**
- **Edible:** Yes
- **Cookable:** Yes

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Saguaros** are a type of above ground tree. They are a cactus, and grow in deserts. Like the overwhelming majority of overland trees, saguaro rib wood logs are brown and produce brown products.

Saguaros are one of the least productive trees for wood. Cutting a saguaro generally does not give much wood, 2-3 logs on average.

Saguaros bear fruit for a relatively long period of time. This can be very useful in adventurer mode, as the saguaro fruit can still be plucked and eaten long after other shrubs and trees have lost their fruits. In fortress mode, the fruit can be cooked, but not brewed.

Some dwarves like saguaros for their *amazing arms*.

\

Admired for its *amazing arms*.

## Trivia

- Its solid density was determined empirically by DF players, as evidenced in the raws. There was no other public, online source of that information prior to *Dwarf Fortress*. Toady One received a "Birthday Artifact" in 2012 made out of Saguaro rib wood.

    [PLANT:SAGUARO]
        [NAME:saguaro][NAME_PLURAL:saguaros][ADJ:saguaro]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:2:0:0]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:saguaro rib wood]
            [STATE_ADJ:ALL_SOLID:saguaro rib]
            [PREFIX:NONE]
                 Density was determined experimentally.  Contact Uristocrat for a sample if you want to verify this yourself.
                 A 6g (+/- 0.1g) piece of dry Saguaro wood had a volume of approximately 14 cm^3 (+/- 1 cm^3)
            [SOLID_DENSITY:430]
            [STATE_COLOR:ALL_SOLID:ECRU]
        [USE_MATERIAL_TEMPLATE:FLOWER:FLOWER_TEMPLATE]
            [STATE_COLOR:ALL:WHITE]
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:FRUIT:FRUIT_TEMPLATE]
            [STATE_COLOR:ALL:RED]
            [DISPLAY_COLOR:4:0:1]
            [EDIBLE_VERMIN]
            [EDIBLE_RAW]
            [EDIBLE_COOKED]
            [STOCKPILE_PLANT_GROWTH]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:198]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:50]
        [BRANCH_DENSITY:0]
        [MAX_TRUNK_HEIGHT:8]
        [HEAVY_BRANCH_RADIUS:3]
        [TRUNK_BRANCHING:0]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [TWIGS_SIDE_BRANCHES:0]
        [TWIGS_ABOVE_BRANCHES:0]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:amazing arms]
        [DRY]
        [BIOME:ANY_DESERT]
        *** night blooming
        [GROWTH:FLOWERS]
            [GROWTH_NAME:saguaro flower:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FLOWER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:TRUNK]
            [GROWTH_TIMING:30000:99999]
            [GROWTH_PRINT:5:5:7:0:1:50000:119999:1]
        [GROWTH:FRUIT]
            [GROWTH_NAME:saguaro fruit:saguaro fruit]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FRUIT]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:TRUNK]
            [GROWTH_TIMING:100000:300000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:0:7:4:0:1:NONE]
            [GROWTH_HAS_SEED]
