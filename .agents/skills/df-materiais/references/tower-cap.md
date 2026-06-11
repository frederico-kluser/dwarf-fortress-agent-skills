# Tower-cap

> Fonte: [Tower-cap](https://dwarffortresswiki.org/index.php/Tower-cap) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes tower-caps for their great size.**
- **Biome**
- **Underground Depth: 1-2**
- **Wet Dry**
- **Wet:** Dry
- **Properties**
- **Deciduous:** No
- **Density:** 600
- **Color:** white
- **Max trunk height:** 5
- **Max trunk diameter:** 3
- **Trunk branching:** 2
- **Heavy branch radius:** 1
- **Branch radius:** 2
- **Root radius:** 3
- **Heavy branch density:** 2
- **Branch density:** 10
- **Root density:** 5
- **Products**
- **Wood:** Tower-cap

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Tower-caps** are a type of mushroom-like subterranean tree. Once fully grown, they can be designated for wood cutting and produce tower-cap logs. Tower-caps will grow on thick subterranean soil or muddied rock. They may be found already growing on muddied rock in an underground cavern. Tower-caps are white and produce white logs, and the resulting products are white or light grey - as a result, they are sometimes used in combination with other white stones to create entirely white areas. Tower-caps produce large amounts of logs per tree due to them having a solid circular cap instead of branches, each tile of which can drop a log.

Tower-caps will not start growing in muddied soil until you have discovered the 1st underground cavern.

Some dwarves like tower-caps for their *great size*.

## Energy source?

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\
There is much controversy about the energy source that tower-caps use to grow. Although it is clear that, like any fungus, they gain energy by breaking down organic compounds in soil and mud, it's equally clear that they are able to do this underground, without access to sunlight. Without any obvious way to regenerate the organic matter that they sprout in, it's unclear how they can survive for thousands of years without sunlight. Thus, useless immigrant dwarven botanists have wasted entirely too much spare time trying to find their energy source.

The leading theory is that underground soil may contain perpetual motion machines, composed of molecular-scale screw pumps and water wheels. As every dwarven engineer knows, a perpetual motion machine must be given water to start up, after which, it will run indefinitely without any extra water required. Molecular-scale screw pumps and water wheels would, similarly, not provide energy until they become muddied, and, similarly, would remain functional indefinitely. The concept of things smaller than a monarch butterfly, however, has led to enormous controversy. Although, obviously, it would be hard to see something smaller than a butterfly, it should be possible to show that it exists because, just like butterflies, it would sometimes get stuck in doors and prevent them from closing. So far, there is no evidence that doors have been held stuck by imperceptibly tiny objects, so the theory remains unsubstantiated.

Alternative theorists have proposed that energy is initially harvested from magma by vermin in the magma sea, and it steadily rises through biological interactions between other vermin, cavern inhabitants, and cave moss. While it is well-documented that vermin reside pretty much everywhere, this theory implies that it should be possible for a dwarf to subsist off of a diet consisting solely of vermin fresh from the magma sea. ~~Un~~fortunately, all attempts to test this theory have been ~~disastrous~~ fun for the test subjects, leading one to conclude this theory is even more foolish than the first.

    [PLANT:TOWER_CAP]
        [NAME:tower-cap][NAME_PLURAL:tower-caps][ADJ:tower-cap]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:7:0:1]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:tower-cap]
            [STATE_ADJ:ALL_SOLID:tower-cap]
            [PREFIX:NONE]
            [STATE_COLOR:ALL_SOLID:WHITE]
            [DISPLAY_COLOR:7:0:1]
            [SOLID_DENSITY:600]
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:6]
        [TREE_HAS_MUSHROOM_CAP]
        [CAP_PERIOD:20]
        [CAP_RADIUS:3]
        [TRUNK_PERIOD:10]
        [MAX_TRUNK_HEIGHT:5]
        [MAX_TRUNK_DIAMETER:3]
        [TRUNK_WIDTH_PERIOD:200]
        [STANDARD_TILE_NAMES]
        [PREFSTRING:great size]
        [WET][DRY]
        [BIOME:SUBTERRANEAN_WATER]
        [UNDERGROUND_DEPTH:1:2]
        [TREE_COLOR:7:0:1]
        [DEAD_TREE_COLOR:0:0:1]
        [SAPLING_COLOR:7:0:1]
        [DEAD_SAPLING_COLOR:0:0:1]
