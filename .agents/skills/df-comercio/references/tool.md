# Tool

> Fonte: [Tool](https://dwarffortresswiki.org/index.php/Tool) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Tools** are objects used for mundane purposes by civilians and night creatures. Some tools can also be used as weapons, though it is usually much better to use, say, a sword over a carving fork. Other tools can be used by your dwarves in fortress mode.

You can select these tools as starting equipment, if your adventurer hails from a human civilisation.

## Tools Usable as Weapons

Type
Graphic
Size
Attack
Attack type
Contact Area
Penetration
Velocity
Skill Used

Carving knife

150
Slash
Edge
800
600
1.25×
Dagger

Stab
Edge
4
800
1×

Handle strike
Blunt
15
(400)
1×

Boning knife

50
Slash
Edge
500
300
1.25×
Dagger

Stab
Edge
2
400
1×

Handle strike
Blunt
10
(200)
1×

Slicing knife

150
Slash
Edge
900
700
1.25×
Dagger

Stab
Edge
3
900
1x

Handle strike
Blunt
15
(400)
1×

Meat cleaver

300
Hack
Edge
800
400
1.25×
Axe

Flat slap
Blunt
800
(400)
1.25×

Handle strike
Blunt
20
(400)
1×

Carving fork

150
Stab
Edge
1
100
1×
Dagger

Handle strike
Blunt
15
400
1×

(Stone) Axe

400
Hack
Edge
800
400
1.25×
Axe

Flat slap
Blunt
800
400
1×

Helve strike
Blunt
20
400
1×

## Other Tools

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| Type | Tile | Graphic | Size (cm³) | Material | Capacity (cm³) | Base Value | Usage |
| Cauldron | `ô` |  | 4000 | Metal 6 | 100,000 | 50 | Cooking liquids |
| Ladle | `♪` |  | 100 | Metal 1 | n/a | 10 | Liquid scoop |
| Bowl | `°` |  | 100 | Stone 1 | 3,000 | 10 | Meal container |
| Mortar | `°` |  | 100 | Stone 1 | 1,000 | 10 | Grind powder, receptacle |
| Pestle | `/` |  | 20 | Stone 1 | n/a | 10 | Grind powder, grinder |
| Nest box | `◘` |  | 1000 | Any Hard 1 | 2,000 | 10 | Contains eggs |
| Jug | `σ` |  | 300 | Any Hard 1 | 10,000 | 10 | Liquid container |
| Large pot | `Φ` |  | 5000 | Any Hard 1 | 60,000 | 10 | Food storage |
| Hive | `▬` |  | 2000 | Any Hard 1 | 5,000 | 10 | Beekeeping |
| Honeycomb | `∞` |  | 1000 | n/a 1 | n/a | 10 | n/a |
| Pouch | `¡` |  | 100 | Soft 1 | 1,000 | 10 | Small object storage |
| Minecart | `■` |  | 40,000 | Wood/Metal 6 | 500,000 | 50 | Tracked cart |
| Wheelbarrow | `Ö` |  | 30,000 | Wood/Metal 6 | 100,000 | 50 | Heavy object hauling |
| Stepladder | `₧` |  | 40,000 | Wood/Metal 6 | n/a | 50 | Fruit collection |
| Scroll rollers | `÷` |  | 100 | Any Hard 1 | n/a | 10 | Roll up sheets |
| Book binding | `÷` |  | 100 | Any Hard 1 | n/a | 10 | Protect folded sheets |
| Scroll | `∞` |  | 200 | Any Sheet 1 | n/a | 20 | Contains writing |
| Quire | `≡` |  | 100 | Any Sheet 1 | n/a | 20 | Contains writing |
| Bookcase | `≡` |  | 1000 | Any Hard 6 | 100,000 | 10 | Bookcase (Furniture) |
| Helve | `\` |  | 250 | Branch 1 | n/a | 10 | Crafting stone axes in adventure mode |
| Pedestal | `ï` |  | 500 | Any Hard 6 |  | 10 | Display furniture |
| Display case | `π` |  | 1000 | Log + Window |  | 10 | Display furniture |
| Altar | `É` |  | 500 | Any Hard 6 |  | 10 | Offering place (Furniture) |
| Die (a.k.a. dice) | `◘` |  | 5 | Any Hard 1 |  | 1 | Divination |
| Instrument component | `¢` |  | Varies | Varies |  | 10 | Constructing instruments |

Hard materials include stone, metal, wood, and glass.\
Soft materials include silk, plant fibers, leather and adamantine thread.\
Sheet materials include papyrus, paper, and parchment.

A tool needs capacity of 600 per unit of liquid to contain: a jug can hold 10,000/600 = 16 units of liquid, a submerged minecart scoops 500,000/600 = 833 units of magma or water, etc.

## See also

- Tool token

|  |
|----|
| "Tool" in other / Languages / Dwarven / : / lòr / Elven / : / wanala / Goblin / : / êngan / Human / : / shem |

    item_tool

    [OBJECT:ITEM]

    [ITEM_TOOL:ITEM_TOOL_CAULDRON]
    [NAME:cauldron:cauldrons]
    [VALUE:50]
    [METAL_MAT]
    [TOOL_USE:LIQUID_COOKING]
    [TILE:147]
    [SIZE:4000]
    [MATERIAL_SIZE:6]
    [CONTAINER_CAPACITY:100000]

    [ITEM_TOOL:ITEM_TOOL_LADLE]
    [NAME:ladle:ladles]
    [VALUE:10]
    [METAL_MAT]
    [TOOL_USE:LIQUID_SCOOP]
    [TILE:13]
    [SIZE:100]
    [MATERIAL_SIZE:1]

    [ITEM_TOOL:ITEM_TOOL_BOWL]
    [NAME:bowl:bowls]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:MEAL_CONTAINER]
    [TILE:248]
    [SIZE:100]
    [MATERIAL_SIZE:1]
    [CONTAINER_CAPACITY:3000]

    [ITEM_TOOL:ITEM_TOOL_MORTAR]
    [NAME:mortar:mortars]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:GRIND_POWDER_RECEPTACLE]
    [TILE:248]
    [SIZE:100]
    [MATERIAL_SIZE:1]
    [CONTAINER_CAPACITY:1000]

    [ITEM_TOOL:ITEM_TOOL_PESTLE]
    [NAME:pestle:pestles]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:GRIND_POWDER_GRINDER]
    [TILE:'/']
    [SIZE:20]
    [MATERIAL_SIZE:1]

    [ITEM_TOOL:ITEM_TOOL_KNIFE_CARVING]
    [NAME:carving knife:carving knives]
    [VALUE:10]
    [METAL_WEAPON_MAT]
    [TOOL_USE:MEAT_CARVING]
    [TILE:'/']
    [SIZE:150]
    [SKILL:DAGGER]
    [TWO_HANDED:22500]
    [MINIMUM_SIZE:4000]
    [MATERIAL_SIZE:1]
    [ATTACK:EDGE:800:600:slash:slashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:EDGE:4:800:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:15:400:strike:strikes:handle:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]

    [ITEM_TOOL:ITEM_TOOL_KNIFE_BONING]
    [NAME:boning knife:boning knives]
    [VALUE:10]
    [METAL_WEAPON_MAT]
    [TOOL_USE:MEAT_BONING]
    [TILE:'/']
    [SIZE:50]
    [SKILL:DAGGER]
    [TWO_HANDED:17500]
    [MINIMUM_SIZE:2000]
    [MATERIAL_SIZE:1]
    [ATTACK:EDGE:500:300:slash:slashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:EDGE:2:400:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:10:200:strike:strikes:handle:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]

    [ITEM_TOOL:ITEM_TOOL_KNIFE_SLICING]
    [NAME:slicing knife:slicing knives]
    [VALUE:10]
    [METAL_WEAPON_MAT]
    [TOOL_USE:MEAT_SLICING]
    [TILE:'/']
    [SIZE:150]
    [SKILL:DAGGER]
    [TWO_HANDED:22500]
    [MINIMUM_SIZE:4000]
    [MATERIAL_SIZE:1]
    [ATTACK:EDGE:900:700:slash:slashes:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:EDGE:3:900:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:15:400:strike:strikes:handle:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]

    [ITEM_TOOL:ITEM_TOOL_KNIFE_MEAT_CLEAVER]
    [NAME:meat cleaver:meat cleavers]
    [VALUE:10]
    [METAL_WEAPON_MAT]
    [TOOL_USE:MEAT_CLEAVING]
    [TILE:'/']
    [SIZE:300]
    [SKILL:AXE]
    [TWO_HANDED:27500]
    [MINIMUM_SIZE:5000]
    [MATERIAL_SIZE:1]
    [ATTACK:EDGE:800:400:hack:hacks:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:800:400:slap:slaps:flat:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:20:400:strike:strikes:handle:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]

    [ITEM_TOOL:ITEM_TOOL_FORK_CARVING]
    [NAME:carving fork:carving forks]
    [VALUE:10]
    [METAL_WEAPON_MAT]
    [TOOL_USE:HOLD_MEAT_FOR_CARVING]
    [TILE:'/']
    [SIZE:150]
    [SKILL:DAGGER]
    [TWO_HANDED:22500]
    [MINIMUM_SIZE:4000]
    [MATERIAL_SIZE:1]
    [ATTACK:EDGE:1:100:stab:stabs:NO_SUB:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:15:400:strike:strikes:handle:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]

    [ITEM_TOOL:ITEM_TOOL_NEST_BOX]
    [NAME:nest box:nest boxes]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:NEST_BOX]
    [TILE:8]
    [SIZE:1000]
    [MATERIAL_SIZE:1]
    [CONTAINER_CAPACITY:2000]

    [ITEM_TOOL:ITEM_TOOL_JUG]
    [NAME:jug:jugs]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:LIQUID_CONTAINER]
    [TILE:229]
    [SIZE:300]
    [MATERIAL_SIZE:1]
    [CONTAINER_CAPACITY:10000]

    [ITEM_TOOL:ITEM_TOOL_LARGE_POT]
    [NAME:pot:pots]
    [ADJECTIVE:large]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:FOOD_STORAGE]
    [TILE:232]
    [SIZE:5000]
    [MATERIAL_SIZE:1]
    [CONTAINER_CAPACITY:60000]

    [ITEM_TOOL:ITEM_TOOL_HIVE]
    [NAME:hive:hives]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:HIVE]
    [TILE:22]
    [SIZE:2000]
    [MATERIAL_SIZE:1]
    [CONTAINER_CAPACITY:5000]

    [ITEM_TOOL:ITEM_TOOL_HONEYCOMB]
    [NAME:honeycomb:honeycombs]
    [VALUE:10]
    [TILE:236]
    [SIZE:1000]
    [MATERIAL_SIZE:1]
    [UNIMPROVABLE]

    [ITEM_TOOL:ITEM_TOOL_POUCH]
    [NAME:pouch:pouches]
    [VALUE:10]
    [SOFT_MAT]
    [TOOL_USE:SMALL_OBJECT_STORAGE]
    [TILE:173]
    [SIZE:100]
    [MATERIAL_SIZE:1]
    [CONTAINER_CAPACITY:1000]

    [ITEM_TOOL:ITEM_TOOL_MINECART]
    [NAME:minecart:minecarts]
    [VALUE:50]
    [METAL_MAT]
    [WOOD_MAT]
    [TOOL_USE:TRACK_CART]
    [FURNITURE]
    [TILE:254]
    [INVERTED_TILE]
    [SIZE:40000]
    [MATERIAL_SIZE:6]
    [CONTAINER_CAPACITY:500000]

    [ITEM_TOOL:ITEM_TOOL_WHEELBARROW]
    [NAME:wheelbarrow:wheelbarrows]
    [VALUE:50]
    [METAL_MAT]
    [WOOD_MAT]
    [TOOL_USE:HEAVY_OBJECT_HAULING]
    [FURNITURE]
    [TILE:153]
    [SIZE:30000]
    [MATERIAL_SIZE:6]
    [CONTAINER_CAPACITY:100000]

    [ITEM_TOOL:ITEM_TOOL_STEPLADDER]
    [NAME:stepladder:stepladders]
    [VALUE:50]
    [METAL_MAT]
    [WOOD_MAT]
    [TOOL_USE:STAND_AND_WORK_ABOVE]
    [FURNITURE]
    [TILE:158]
    [SIZE:40000]
    [MATERIAL_SIZE:6]

    [ITEM_TOOL:ITEM_TOOL_SCROLL_ROLLERS]
    [NAME:scroll rollers:scroll rollers]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:ROLL_UP_SHEET]
    [TILE:246]
    [SIZE:100]
    [MATERIAL_SIZE:1]
    [INCOMPLETE_ITEM]
    [UNIMPROVABLE]

    [ITEM_TOOL:ITEM_TOOL_BOOK_BINDING]
    [NAME:book binding:book bindings]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:PROTECT_FOLDED_SHEETS]
    [TILE:246]
    [SIZE:100]
    [MATERIAL_SIZE:1]
    [INCOMPLETE_ITEM]
    [UNIMPROVABLE]

    [ITEM_TOOL:ITEM_TOOL_SCROLL]
    [NAME:scroll:scrolls]
    [VALUE:20]
    [SHEET_MAT]
    [TOOL_USE:CONTAIN_WRITING]
    [TILE:236]
    [SIZE:200]
    [NO_DEFAULT_JOB]
    [DEFAULT_IMPROVEMENT:SPECIFIC:ROLLERS:HARD_MAT]

    [ITEM_TOOL:ITEM_TOOL_QUIRE]
    [NAME:quire:quires]
    [VALUE:20]
    [SHEET_MAT]
    [TOOL_USE:CONTAIN_WRITING]
    [TILE:240]
    [SIZE:100]
    [NO_DEFAULT_JOB]
    [INCOMPLETE_ITEM]
    [UNIMPROVABLE]
    [NO_DEFAULT_IMPROVEMENTS]

    [ITEM_TOOL:ITEM_TOOL_BOOKCASE]
    [NAME:bookcase:bookcases]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:BOOKCASE]
    [FURNITURE]
    [TILE:240]
    [INVERTED_TILE]
    [SIZE:1000]
    [MATERIAL_SIZE:6]
    [CONTAINER_CAPACITY:100000]

    [ITEM_TOOL:ITEM_TOOL_HELVE]
    [NAME:helve:helves]
    [VALUE:10]
    [HARD_MAT]
    [TILE:'\']
    [SIZE:250]
    [NO_DEFAULT_JOB]
    [INCOMPLETE_ITEM]
    [UNIMPROVABLE]
    [NO_DEFAULT_IMPROVEMENTS]

    [ITEM_TOOL:ITEM_TOOL_STONE_AXE]
    [NAME:axe:axes]
    [VALUE:10]
    [STONE_MAT]
    [NO_DEFAULT_JOB]
    [TILE:'/']
    [SIZE:400]
    [SKILL:AXE]
    [TWO_HANDED:27500]
    [MINIMUM_SIZE:5000]
    [MATERIAL_SIZE:1]
    [ATTACK:EDGE:800:400:hack:hacks:NO_SUB:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:800:400:slap:slaps:flat:1250]
        [ATTACK_PREPARE_AND_RECOVER:3:3]
    [ATTACK:BLUNT:20:400:strike:strikes:helve:1000]
        [ATTACK_PREPARE_AND_RECOVER:3:3]

    [ITEM_TOOL:ITEM_TOOL_PEDESTAL]
    [NAME:pedestal:pedestals]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:DISPLAY_OBJECT]
    [FURNITURE]
    [TILE:139]
    [SIZE:500]
    [MATERIAL_SIZE:6]

    [ITEM_TOOL:ITEM_TOOL_DISPLAY_CASE]
    [NAME:display case:display cases]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:DISPLAY_OBJECT]
    [FURNITURE]
    [TILE:227]
    [INVERTED_TILE]
    [SIZE:1000]
    [NO_DEFAULT_JOB]

    [ITEM_TOOL:ITEM_TOOL_ALTAR]
    [NAME:altar:altars]
    [VALUE:10]
    [HARD_MAT]
    [TOOL_USE:PLACE_OFFERING]
    [FURNITURE]
    [TILE:144]
    [SIZE:500]
    [MATERIAL_SIZE:6]

    [ITEM_TOOL:ITEM_TOOL_DIE]
    [NAME:die:dice]
    [VALUE:1]
    [HARD_MAT]
    [TOOL_USE:DIVINATION]
    [TOOL_USE:GAMES_OF_CHANCE]
    [SHAPE_CATEGORY:DICE]
    [USES_FACE_IMAGE_SET]
    [TILE:8]
    [SIZE:5]
    [MATERIAL_SIZE:1]
