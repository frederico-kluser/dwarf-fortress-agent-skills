# Building token

> Fonte: [Building token](https://dwarffortresswiki.org/index.php/Building_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

**Building tokens** control the functionality of custom buildings.

All custom buildings are defined as objects of type BUILDING_WORKSHOP or BUILDING_FURNACE; workshops show up in the Build \> Workshops (bo) menu, while furnaces show up in the Build \> Workshops \> Furnaces (bou) menu.

You also must add any new custom buildings to the civilization that you want to use it.

Additionally, furnaces must be designed by an mason before being constructed (and will gain quality accordingly), though they will always use the labor(s) specified in the building definition, rather than ones based on the materials being used.

Urist asks...
Is there a WYSIWYG editor for ASCII buildings?

Custom Workshop Workshop / is a standalone program designed for this purpose. / There is also a / Building ASCII Visualizer / web app included in DFTools. Special character IDs can be found on the / Character table / .

|  |  |  |  |
|----|----|----|----|
| Token | Arguments | Description |  |
|  NAME | name | The name of the custom building. |  |
|  NAME_COLOR | fg:bg:bright | The color of the building's name when querying it. Seemingly ignored for furnaces, which are hardcoded to 4:0:1. |  |
|  DIM | width:height | The size of the custom building, in number of tiles. Defaults to 3:3. Maximum possible size is 31x31. |  |
|  WORK_LOCATION | x:y | The tile (1:1 for upper-left) in which dwarves will stand when they are performing tasks. Defaults to 3:3 (bottom-right). |  |
|  BUILD_LABOR | labor token | The labor required to construct the custom building. If multiple BUILD_LABOR tokens are specified, then any of the indicated labors can be used to construct the building; if none are specified, then no labors are required. |  |
|  BUILD_KEY | key bind | The shortcut key used in the Build menu for selecting the custom building. For example: "CUSTOM_SHIFT_S" |  |
|  BLOCK | row / tiles... | Specifies whether or not each workshop tile blocks movement. The first parameter is the row (1 = top), and each subsequent parameter is a 0 (nonblocking) or 1 (blocking) for each column, left to right. |  |
|  TILE | stage / row / tiles... | Specifies the characters used to represent the custom building. The first parameter is the building stage, varying from 0 (awaiting construction) to N (completed) where N is between 1 and 3, the 2nd parameter is the row number, and each subsequent parameter is a character number (or literal character enclosed in 'quotes'). |  |
|  COLOR | stage / row / colors... | Specifies the colors in which the custom building's tiles will be displayed. The first parameter is the building stage, the 2nd parameter is the row number, and subsequent parameters are either sets of 3 numbers (foreground:background:brightness), or the token "MAT" to use the color of the primary building material, for each tile in the row. MAT may not be available on BUILDING_FURNACEs.\[Verify\] However a color settings of 4:0:1 will translate into MAT for furnaces instead. |  |
|  BUILD_ITEM | quantity / item token / material token | Specifies one of the objects necessary to construct the custom building. Each BUILD_ITEM can be followed by zero or more modifiers. |  |
|  NEEDS_MAGMA |  | Specifies that one of the building's tiles (other than the WORK_LOCATION) must be hanging over magma in order for the building to function. Buildings with this token also ignore the \[FUEL\] token in their reactions. |  |
|  TOOLTIP | tooltip | Adds a tooltip for the building. |  |

## Item Modifiers

Building items have many of the same modifiers as reagents in custom reactions.

|  |  |
|----|----|
| Token | Meaning |
| \[ ANY_BONE_MATERIAL\] | Item material must have the \[BONE\] token. |
| \[ ANY_HORN_MATERIAL\] | Item material must have the \[HORN\] token. |
| \[ ANY_LEATHER_MATERIAL\] | Item material must have the \[LEATHER\] token. |
| \[ ANY_PEARL_MATERIAL\] | Item material must have the \[PEARL\] token. |
| \[ ANY_PLANT_MATERIAL\] | Item material must be subordinate to a PLANT object. |
| \[ ANY_SHELL_MATERIAL\] | Item material must have the \[SHELL\] token. |
| \[ ANY_SILK_MATERIAL\] | Item material must have the \[SILK\] token. |
| \[ ANY_SOAP_MATERIAL\] | Item material must have the \[SOAP\] token. |
| \[ ANY_STRAND_TISSUE\] | Item is made of a tissue having \[TISSUE_SHAPE:STRANDS\], intended for matching hair and wool. Must be used with \[USE_BODY_COMPONENT\]. |
| \[ ANY_TOOTH_MATERIAL\] | Item material must have the \[TOOTH\] token. |
| \[ ANY_YARN_MATERIAL\] | Item material must have the \[YARN\] token. |
| \[ BUILDMAT\] | Item must be a general building material - BAR, BLOCKS, BOULDER, or WOOD. |
| \[ CAN_USE_ARTIFACT\] | Item can be an Artifact. |
| \[ CONTAINS_LYE\] | Item must be a BARREL or TOOL which contains at least one item of type LIQUID_MISC made of LYE. |
| \[ EMPTY\] | If the item is a container, it must be empty. |
| \[ FIRE_BUILD_SAFE\] | Item material must be stable at temperatures below 11000. Only works with items of type BAR, BLOCKS, BOULDER, WOOD, and ANVIL - all others are considered unsafe. |
| \[ GLASS_MATERIAL\] | Item material must have the \[IS_GLASS\] token. All 3 types of glass have this token hardcoded. |
| \[ GROWN_NOT_CRAFTED\] | Item must be a GROWN wooden item, such as a "grown wooden sword" from an Elven caravan. |
| \[ HAS_MATERIAL_REACTION_PRODUCT:X\] | Item's material has a \[MATERIAL_REACTION_PRODUCT\] token with the appropriate ID. |
| \[ HAS_TOOL_USE:X\] | Item must be a tool with the specific TOOL_USE value. The item type must be TOOL:NONE for this to make any sense. |
| \[ MAGMA_BUILD_SAFE\] | Item material must be stable at temperatures below 12000. Only works with items of type BAR, BLOCKS, BOULDER, WOOD, and ANVIL - all others are considered unsafe. |
| \[ METAL_ORE:X\] | Item material must be an ore of the specified metal. |
| \[ MIN_DIMENSION:X\] | Item's dimension must be at least this large. The item type must be BAR, POWDER_MISC, LIQUID_MISC, DRINK, THREAD, or CLOTH for this to work. |
| \[ NO_EDGE_ALLOWED\] | Item must not have an edge, so must be blunt. Sharp stones (produced using knapping) and most types of weapon/ammo can not be used with this token. |
| \[ NOT_CONTAIN_BARREL_ITEM\] | If the item is a container, it must not contain lye or milk. Not necessary if specifying \[EMPTY\]. |
| \[ NOT_ENGRAVED\] | Item can not be engraved. For example, a memorial slab can not be engraved. |
| \[ NOT_WEB\] | Item must be collected (to distinguish silk thread from webs). Only makes sense for items of type THREAD. |
| \[ POTASHABLE\] (Deprecated) | Alias for \[CONTAINS_LYE\]. |
| \[ REACTION_CLASS:X\] | Item's material has a \[REACTION_CLASS\] token with the appropriate ID. |
| \[ UNROTTEN\] | Item must not be rotten, mainly for organic materials. |
| \[ USE_BODY_COMPONENT\] | Item must be a body part (CORPSE or CORPSEPIECE). |
| \[ WEB_ONLY\] | Item must be undisturbed (to distinguish silk thread from webs). Only makes sense for items of type THREAD. |
| \[ WORTHLESS_STONE_ONLY\] | Item material must be non-economic. |
