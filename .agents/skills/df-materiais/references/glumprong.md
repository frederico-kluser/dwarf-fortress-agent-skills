# Glumprong

> Fonte: [Glumprong](https://dwarffortresswiki.org/index.php/Glumprong) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes glumprongs for their living shadows.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Alignment**
- **Evil**
- **Properties**
- **Deciduous:** No
- **Density:** 1200
- **Color:** purple
- **Max trunk height:** 6
- **Max trunk diameter:** 1
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 0
- **Branch density:** 0
- **Root density:** 5
- **Products**
- **Wood:** Glumprong

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Glumprongs** are a type of above ground tree found only in dry, evil regions. Glumprong trees are notable for their unique purple color, their odd structure, and for having the heaviest wood from an aboveground tree. Glumprong trees are only trunk and roots, with no branches, leaves, seeds, or fruit. However, the wood from these trees is very dense, twice that of most typical wood. This heavyweight wood is suboptimal for hauling, but can be useful for some niche weight-based applications.

If you embark in an evil-aligned area, glumprong trees may be an enticing source of wood, since they lack useful seeds and fruit. Unfortunately, glumprong wood is the second-heaviest wood in the game, behind only blood thorn, a tree-like fungus found only in the deepest caverns. The relatively high weight of glumprong logs may leave your haulers a bit more vulnerable to evil weather or hostile local creatures. Once you have the logs inside, you'll find glumprong wood's higher weight makes it somewhat less useful than other types of wood for wooden containers and other tools meant for hauling, like barrels, bins, and wheelbarrows. Wheelbarrows, ideally ones made of lighter wood, can be helpful for hauling glumprong logs.

This doesn't make glumprong wood useless, though. If you'd like purple wooden furniture, workshops, or constructions, glumprong's weight scarcely matters. Glumprong logs burn into charcoal or ash just as well as any wood. There are even a few cases where the greater weight of glumprong wood is somewhat useful, like ballista bolts, crossbows, trap components (especially blunt ones like the spiked ball), and empty minecart sorting.

Glumprong wood is only notably dense in comparison to other types of wood. It's still lighter than any non-spoiler metal, stone, ceramic, or glass. Even relatively light metals like aluminum weigh more than twice as much. If glumprong wood is the only type of wood available to you, it is still superior to using some other material for barrels, bins, buckets, cages, large pots, and wheelbarrows.

When it comes to making weapons, glumprong's weight makes it generally superior to bone or other kinds of wood, but it is still wood, and thus has very poor weapon qualities. A glumprong spiked ball or crossbow bolt will outperform one made of birch, but cannot match one made out of copper, let alone an ideal material like steel. Glumprong is slightly better as a cheap choice for mass production, but it is still vastly inferior to metal for any military application.

Some dwarves like glumprongs for their *living shadows*.

-

  Multiple z-levels of a glumprong tree.

-

  The shadows twitch when you least expect it.\
  *Crudely drawn by Zippy*

    [PLANT:GLUMPRONG]
        [NAME:glumprong][NAME_PLURAL:glumprongs][ADJ:glumprong]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:5:0:0]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:glumprong]
            [STATE_ADJ:ALL_SOLID:glumprong]
            [STATE_COLOR:ALL_SOLID:PURPLE]
            [PREFIX:NONE]
            [DISPLAY_COLOR:5:0:0]
            [SOLID_DENSITY:1200]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:180]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:0]
        [BRANCH_DENSITY:0]
        [MAX_TRUNK_HEIGHT:6]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [ROOT_DENSITY:5]
        [ROOT_RADIUS:3]
        [STANDARD_TILE_NAMES]
        [TREE_COLOR:5:0:0]
        [DEAD_TREE_COLOR:0:0:1]
        [PREFSTRING:living shadows]
        [DRY][EVIL]
        [BIOME:NOT_FREEZING]
