# Blood thorn

> Fonte: [Blood thorn](https://dwarffortresswiki.org/index.php/Blood_thorn) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes blood thorn for their sickening appearance.**
- **Biome**
- **Underground Depth: 3**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 1250
- **Color:** crimson
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
- **Wood:** Blood thorn

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Blood thorn** are ghastly-looking trees that grow only in the deepest cavern layers. They are distinguished from their peers by being the densest tree in the game (though glumprongs come close), being approximately half as dense as most stone, and by their unique crimson color. When cut down, they produce extremely heavy crimson wood that cannot be found anywhere else, making for heavy but colorful furniture, and slightly less useless wooden ballista bolts. Curiously, trampled young blood thorn are *purple* rather than dark gray, presumably due to the plant having been "bruised" – this is in imitation of the "blood" in their name.

Among subterranean trees, blood thorn are unique in that they can grow in cavern layers that are devoid of water - when this happens, blood thorn will be the **only** plants present. This means that every so often, a fortress may happen to have a large stock of the tree in its caverns.

Some dwarves like blood thorn for their *sickening appearance*.

-

  A typical blood thorn tree in the lowest cavern levels

-

  Even elves don't care for it.\
  *Art by Naiden Petrov*

|  |
|----|
| "Blood thorn" in other / Languages / Dwarven / : / nazush kurik / Elven / : / cameda iki / Goblin / : / ogom spuspo / Human / : / cadem pik |

    [PLANT:BLOOD_THORN]
        [NAME:blood thorn][NAME_PLURAL:blood thorn][ADJ:blood thorn]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:4:0:0]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:blood thorn]
            [STATE_ADJ:ALL_SOLID:blood thorn]
            [PREFIX:NONE]
            [STATE_COLOR:ALL_SOLID:CRIMSON]
            [DISPLAY_COLOR:4:0:0]
            [SOLID_DENSITY:1250]
        [TREE:LOCAL_PLANT_MAT:WOOD]
        [TRUNK_PERIOD:10]
        [HEAVY_BRANCH_DENSITY:25]
        [BRANCH_DENSITY:50]
        [MAX_TRUNK_HEIGHT:5]
        [HEAVY_BRANCH_RADIUS:1]
        [BRANCH_RADIUS:2]
        [TRUNK_BRANCHING:2]
        [MAX_TRUNK_DIAMETER:1]
        [TRUNK_WIDTH_PERIOD:200]
        [STANDARD_TILE_NAMES]
        [TREE_TILE:181]
        [DEAD_TREE_TILE:181]
        [PREFSTRING:sickening appearance]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [BIOME:SUBTERRANEAN_CHASM]
        [UNDERGROUND_DEPTH:3:3]
        [TREE_COLOR:4:0:0]
        [DEAD_TREE_COLOR:5:0:0]
        [SAPLING_COLOR:4:0:0]
        [DEAD_SAPLING_COLOR:5:0:0]
