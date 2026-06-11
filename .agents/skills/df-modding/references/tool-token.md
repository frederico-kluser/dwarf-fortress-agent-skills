# Tool token

> Fonte: [Tool token](https://dwarffortresswiki.org/index.php/Tool_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

## Tokens

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  NAME | singular / plural | Name of the tool. Required. |
|  BONE_MAT |  | Permits the tool to be made from any bone. Default jobs for bone tools can only be performed by work order. Bug:12689 |
|  CERAMIC_MAT |  | Permits the tool to be made from any material that [`[IS_CERAMIC]`](/index.php/Material_definition_token#IS_CERAMIC "Material definition token"). |
|  DESCRIPTION |  | Allows a string to describe the tool when viewed. The text box can accommodate up to 325 characters until it cuts off, but the spacing of actual sentences puts the realistic limit closer to 300. Multiple DESCRIPTION tokens can be used in the same tool definition, with each appearing on a new line. |
|  GLASS_MAT |  | Permits the tool to be made from any glass. |
|  HARD_MAT |  | Permits the tool to be made from anything with the [`[ITEMS_HARD]`](/index.php/Material_definition_token#ITEMS_HARD "Material definition token") token, such as wood, stone or metal. |
|  LEATHER_MAT |  | Permits the tool to be made from any leather. |
|  METAL_MAT |  | Permits the tool to be made from anything with the [`[IS_METAL]`](/index.php/Material_definition_token#IS_METAL "Material definition token") token. |
|  METAL_WEAPON_MAT |  | Permits the tool to be made from any metal with the [`[ITEMS_WEAPON]`](/index.php/Material_definition_token#ITEMS_WEAPON "Material definition token") token. |
|  SHEET_MAT |  | Permits the tool to be made from any sheet material, such as papyrus, paper, and parchment. Connected to the PAPER_SLURRY/PAPER_PLANT reaction classes?\[Verify\] |
|  SHELL_MAT |  | Permits the tool to be made from any shell. |
|  SILK_MAT |  | Permits the tool to be made from any silk. |
|  SOFT_MAT |  | Permits the tool to be made from any material with the [`[ITEMS_SOFT]`](/index.php/Material_definition_token#ITEMS_SOFT "Material definition token") token, such as leather or textiles. |
|  STONE_MAT |  | Permits the tool to be made from any stone. Presumably connected to the [`[IS_STONE]`](/index.php/Material_definition_token#IS_STONE "Material definition token") token. |
|  THREAD_PLANT_MAT |  | Permits the tool to be made from any plant fiber, such as pig tails. |
|  WOOD_MAT |  | Permits the tool to be made from any wood. |
|  INCOMPLETE_ITEM |  | According to Toady, "Won't be used in world gen libraries (to differentiate scrolls from quires). Also put it on bindings, rollers, instr. pieces for completeness/future use". Used on scroll rollers, book bindings, and quires. |
|  DEFAULT_IMPROVEMENT | improvement type and subtype (latter only really applicable to SPECIFIC) / tool material flag like / \[HARD_MAT\] / or / \[SILK_MAT\] | Items that appear in the wild come standard with this kind of improvement. Used on scrolls: \[DEFAULT_IMPROVEMENT:SPECIFIC:ROLLERS:HARD_MAT\] / Currently bugged, the effect is also applied to everything made in-game. This causes scrolls to have two sets of rollers, for example. |
|  UNIMPROVABLE |  | Prevents the tool from being improved. Used on honeycombs, scroll rollers, book bindings, and quires. |
|  VALUE | num | Defines the item value of the tool. Required. |
|  TILE | num | Defines the tile used to represent the tool. Required. |
|  INVERTED_TILE |  | The background of the tile will be colored, instead of the foreground. |
|  NO_DEFAULT_JOB |  | According to Toady, "only custom reactions are used to make this item". Found on scrolls and quires. |
|  TOOL_USE | tool use, see below | Defines the task performed using the tool. |
|  FURNITURE |  | Allows item to be stored in a / furniture stockpile / , and default jobs (unless disabled with / \[NO_DEFAULT_JOB\] / ) are considered / furniture / -making tasks instead of / crafts / . / The jobs for wood and stone will be done at the / carpenter's workshop / or / stoneworker's workshop / instead of the / craftsdwarf's workshop / . Likewise, the jobs for metal tools will use the / blacksmith / skill instead of / metal crafter / . |
|  SHAPE_CATEGORY | shape category | Category of shapes to choose from for the tool as defined by the CATEGORY token in descriptor_shape_standard.txt or a custom descriptor definition. |
|  USES_FACE_IMAGE_SET |  | Used on dice. |
|  ADJECTIVE | adjective | Adjective preceding the material name (e.g. "large copper dagger") |
|  SIZE /  WEIGHT | size | Volume of tool in mL or cubic centimeters. Required. |
|  CONTAINER_CAPACITY | amount | How much the item can contain. Defaults to 0. |
|  SHOOT_FORCE | value | Required for weapons. |
|  SHOOT_MAXVEL | value | Required for weapons. |
|  SKILL | Skill token | The skill to determine effectiveness in melee with this tool. Required for weapons. |
|  RANGED | Skill token / Ammo item token | Makes this tool a ranged weapon that uses the specified ammo. The specified skill determines accuracy in ranged combat. |
|  TWO_HANDED | size | Creatures under this size (in cm^3) must use the tool two-handed. Required for weapons. |
|  MINIMUM_SIZE | size | Minimum body size (in cm^3) to use the tool at all (multigrasp required until TWO_HANDED value) Required for weapons. |
|  MATERIAL_SIZE | value | Number of bar units needed for forging, as well as the amount gained from melting. Required for weapons. |
|  ATTACK | attacktype:BLUNT or EDGE / contact_area:value / penetration_size:value / verb2nd:string / verb3rd:string / noun:string / velocity_multiplier:value | You can have many ATTACK tags and one will be randomly selected for each attack, with EDGE attacks 100 times more common than BLUNT attacks. Required for weapons. |

 Valid tool uses (and the default tools used for these tasks) are as follows:

|  |  |  |  |
|----|----|----|----|
| ID | Token | Usage |  |
| 0 | LIQUID_COOKING | cauldron | adventure mode decoration / weapon |
| 1 | LIQUID_SCOOP | ladle | adventure mode decoration / weapon |
| 2 | GRIND_POWDER_RECEPTACLE | mortar | adventure mode decoration / weapon |
| 3 | GRIND_POWDER_GRINDER | pestle | adventure mode decoration / weapon |
| 4 | MEAT_CARVING | carving knife | adventure mode decoration / weapon |
| 5 | MEAT_BONING | boning knife | adventure mode decoration / weapon |
| 6 | MEAT_SLICING | slicing knife | adventure mode decoration / weapon |
| 7 | MEAT_CLEAVING | meat cleaver | adventure mode decoration / weapon |
| 8 | HOLD_MEAT_FOR_CARVING | carving fork | adventure mode decoration / weapon |
| 9 | MEAL_CONTAINER | bowl | adventure mode decoration / weapon |
| 10 | LIQUID_CONTAINER | jug | can store honey or oil |
| 11 | FOOD_STORAGE | large pot | can store beer |
| 12 | HIVE | hive | can make honey |
| 13 | NEST_BOX | nest box | for your birds to lay eggs |
| 14 | SMALL_OBJECT_STORAGE | pouch | adventure mode coin purse |
| 15 | TRACK_CART | minecart | item hauling / weapon |
| 16 | HEAVY_OBJECT_HAULING | wheelbarrow | allows hauling items faster |
| 17 | STAND_AND_WORK_ABOVE | stepladder | allows gathering fruit from trees |
| 18 | ROLL_UP_SHEET | scroll rollers |  |
| 19 | PROTECT_FOLDED_SHEETS | book binding |  |
| 20 | CONTAIN_WRITING | scroll & quire |  |
| 21 | BOOKCASE | bookcase |  |
| 22 | DISPLAY_OBJECT | pedestal & display case | for museums |
| 23 | PLACE_OFFERING | altar | for (eventually) offering sacrifices |
| 24 | DIVINATION | dice |  |
| 25 | GAMES_OF_CHANCE | dice |  |
