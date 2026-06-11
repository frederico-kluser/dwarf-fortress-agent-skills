# Feather tree

> Fonte: [Feather tree](https://dwarffortresswiki.org/index.php/Feather_tree) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

## Dados (infobox)

- **Urist likes feather trees for their feathery leaves.**
- **Biome**
- **Any land except Mountain , Glacier , Tundra**
- **Wet Dry**
- **Wet:** Dry
- **Alignment**
- **Good**
- **Properties**
- **Deciduous:** No
- **Density:** 100
- **Color:** cream
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
- **Wood:** Feather wood

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

The **feather tree** is a special tree that grows only in good-aligned areas. Unlike other above ground trees, it yields cream-colored logs when cut down. It has feather-like "leaves", and, curiously, it yields eggs instead of fruit. Beware the unicorns that may roam around it, or simply import it from elven caravans.

Featherwood is the lightest wood in the game, so it should be used for things that get hauled around very frequently, such as bins, barrels and buckets, decreasing dwarf speed less as they carry these items, since they are carrying less weight. Featherwood shields are also very effective, since a shield's weight doesn't affect its ability to block attacks; it will make a shield's secondary bash attack less effective, though. It is extremely useless for ammunition – crossbow and ballista bolts will simply glance off enemies due to them weighing almost nothing. Since damage from falling is affected by the material of the landing zone, featherwood floors can cushion falls and prevent serious injuries.

Some dwarves like feather trees for their *feathery leaves*.

-

  The majestic Feather Tree in v50 of the game

-

  Only grows Grade-B eggs.\
  *Crudely drawn by Zippy*

|  |  |
|:--:|----|
| [](/index.php/Category:D_for_Dwarf "Category:D for Dwarf") | This article or section has been rated **D for Dwarf**. It may include witty humour, not-so-witty humour, bad humour, in-jokes, pop culture references, and references to the Bay12 forums. Don't believe everything you read, and if you miss some of the references, don't worry. It was inevitable. |

\

Observing that these so-called "trees" are covered in feathers and bear eggs instead of fruit, a growing number of dwarven naturalists are advancing the position that feather trees are more properly categorized as birds rather than plants. While not universally accepted, the proposed reclassification has gained some traction in both dwarven and human academic communities, with some recently revised bestiaries now including the species, which has been tentatively renamed the "common woody rootfowl". Elven scholars have roundly dismissed this avenue of novel scientific inquiry as a coordinated, cynically motivated effort to circumvent treaties imposing limitations on tree-felling in forests abutting traditionally elven territory.

    [PLANT:FEATHER]
        [NAME:feather tree][NAME_PLURAL:feather trees][ADJ:feather tree]
        [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
            [DISPLAY_COLOR:7:0:1]
        [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
        [USE_MATERIAL_TEMPLATE:WOOD:WOOD_TEMPLATE]
            [STATE_NAME:ALL_SOLID:feather wood]
            [STATE_ADJ:ALL_SOLID:feather wood]
            [STATE_COLOR:ALL_SOLID:CREAM]
            [PREFIX:NONE]
            [DISPLAY_COLOR:7:0:1]
            [SOLID_DENSITY:100]
        [USE_MATERIAL_TEMPLATE:FEATHER:FEATHER_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:7:0:1]
        [USE_MATERIAL_TEMPLATE:EGG:EGG_YOLK_TEMPLATE]
            [STATE_COLOR:ALL:GREEN]
            [DISPLAY_COLOR:4:0:1]
            [STOCKPILE_PLANT_GROWTH]
            *** need to go w/ all egg mats when growths support it
            *** template currently implies animal kill
        [TREE:LOCAL_PLANT_MAT:WOOD][TREE_TILE:5]
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
        [TREE_COLOR:7:0:1]
        [DEAD_TREE_COLOR:7:0:0]
        [PREFSTRING:feathery leaves]
        [DRY][GOOD]
        [BIOME:NOT_FREEZING]
        [SAPLING]
        [GROWTH:FEATHERS]
            [GROWTH_NAME:feather tree down:feather tree down]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:FEATHER]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_HOST_TILE:SAPLING]
            [GROWTH_PRINT:0:6:7:0:1:ALL:1]
        [GROWTH:EGGS]
            [GROWTH_NAME:feather tree egg:STP]
            [GROWTH_ITEM:PLANT_GROWTH:NONE:LOCAL_PLANT_MAT:EGG]
            [GROWTH_DENSITY:1000]
            [GROWTH_HOST_TILE:BRANCHES_AND_TWIGS]
            [GROWTH_TIMING:120000:200000]
            [GROWTH_DROPS_OFF_NO_CLOUD]
            [GROWTH_PRINT:'%':7:7:0:1:120000:200000:3]
