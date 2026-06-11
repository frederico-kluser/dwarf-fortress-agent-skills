# Graphics token

> Fonte: [Graphics token](https://dwarffortresswiki.org/index.php/Graphics_token) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

*For an explanation of how to use the various graphics types, see Graphics.*

The `[OBJECT:GRAPHICS]` token defines the use of various tile-based graphics in the game. As of version 50.01, graphics tokens have been greatly expanded to accommodate the release of the Steam & Itch premium version. These tokens, and explanations on how to use them, are listed below; the list will expand as the tokens are discovered and understood.

## Creature Graphics

Creature graphics are found within graphics_creature_x files (such as graphics_creature_domestic or graphics_creature_layered). All graphics files must begin with the file name, followed by the `[OBJECT:GRAPHICS]` type that tells the game that the file contains graphics definitions. A more detailed explanation on how to use these can be found in creature graphics.

### Types

|  |  |  |
|----|----|----|
| Type | Arguments | Description |
|  CREATURE_GRAPHICS | creature id | The simplest and most common form of creature graphics for defining one sprite for each / basic condition / . / Further conditions are required for this to function following the / creature graphics / format. Accepts / large graphics tokens / . / Additionally used to start defining a / layered graphics / set. |
|  CREATURE_CASTE_GRAPHICS | creature id / Caste ID | Nearly the same as / \[CREATURE_GRAPHICS\] / , but allows a separate sprite to be defined for each caste. / A simple alternative to / Layered Graphics / . / Requires conditions defined in / creature graphics / format. Accepts / large graphics tokens / . |
|  STATUE_CREATURE_GRAPHICS | creature id | Format for beginning a creature statue definition. Defines a 1x2 vertical rectangle to be displayed when a statue depicts one of these creatures. |
|  STATUE_CREATURE_CASTE_GRAPHICS | creature id / Caste ID | Format for beginning a creature statue definition while specifying caste. Defines a 1x2 vertical rectangle to be displayed when a statue depicts one of these creatures. |
|  TILE_GRAPHICS_RECTANGLE | creature id | Graphics for a 3x2 rectangle; for creatures, this is used exclusively for representing Forgotten Beasts based on their body parts. Uses forgotten beast graphics. It's also, however, used for interface graphics, see graphics_interface.txt. |

### Conditions

Different graphics can be defined for the same creature based on some properties about it. Below is a list of all the basic "creature texture" types that can be used as additional conditions to various basic sprites.

|  |  |
|----|----|
| Condition | Description |
|  DEFAULT | The default condition that will be displayed unless overwritten by a more specific one below. |
|  LAW_ENFORCE | Displayed if the unit is law enforcement. |
|  TAX_ESCORT | Displayed if the unit escorts a tax collector (unused). |
|  ANIMATED | Displayed if the creature is raised from the dead using an I_EFFECT:ANIMATE interaction. |
|  GHOST | Displayed if the creature is a ghost. |
|  ADVENTURER | Displayed if the creature is an adventurer. |
|  CORPSE | Displayed for corpses. |

### Basic creature sprite types

An individual sprite can be of any of the following classes. If "accepts secondary" is "yes", it can also have an extra condition tacked on at the end.

|  |  |
|----|----|
| Condition | Description |
|  Basic Condition | Any of the above conditions can be used on their own, as the default for that condition class. |
|  Unit type | Any Unit type token can be used. You may also append a basic condition as above to further specify. |
|  Position | Any Position token can be used, such as MONARCH, BROKER etc. All position tokens are raw-defined; any modded positions can have their own graphics. You may also append a basic condition as above to further specify. |
|  LIST_ICON | The default icon for this creature in lists, such as Arena mode or overall training. |
|  EGG | The sprite for a clutch of eggs. |
|  SKELETON | The sprite for a rotten corpse. |
|  SKELETON_WITH_SKULL | The sprite for a rotten corpse that can have a totem made from it. |
|  GLOWv51.01-beta26 | The creature is in the \[dark\]. Graphical replacement for [`[GLOWTILE]`](/index.php/Creature_token#GLOWTILE "Creature token"). |
|  GLOW_LEFT_GONEv51.01-beta26 | As [`[GLOW]`](/index.php/Graphics_token#GLOW "Graphics token"), but with their left eye missing. If the sprite is facing forwards, then the visually leftmost eye should remain. |
|  GLOW_RIGHT_GONEv51.01-beta26 | Counterpart of [`[GLOW_LEFT_GONE]`](/index.php/Graphics_token#GLOW_LEFT_GONE "Graphics token"). |
|  GLOW_CHILDv51.01-beta26 | A child creature is in darkness. Does not have wound states. |

### Layered Conditions

Layers aren't very useful on their own, so they come with a set of conditions to define how when they are displayed and how they interact. Unless otherwise stated, a layer will only render if all of its conditions are true.

|  |  |  |  |
|----|----|----|----|
| Token | Arguments | Type | Description |
|  LAYER_GROUP |  | General\[Verify\] | Begins a layer group. Only the first-matching layer in a group will be rendered, so list more specific items at the beginning of the layer group and more general items towards the end. |
|  LAYER_SET | condition | Creature / Graphics | Begins defining a layer set for a creature's graphics. Valid values of *condition* are DEFAULT, PORTRAITv50.13, BABY:DEFAULTv51.01-beta20, CHILD:DEFAULTv51.01-beta20, or CORPSE Valid values for basic conditions may not work.\[Verify\] |
|  LS_PALETTEv50.13 | name | Layer / Set | Begins defining a palette for the layer set. Its name can be referenced by [`[USE_PALETTE]`](/index.php/Graphics_token#USE_PALETTE "Graphics token"). Unlike the palettes used to render all descriptor color tokens, it can be of arbitrary length. |
|  LS_PALETTE_FILEv50.13 | file name | Palette | The file name of the 8bit RGBA (sometimes called 32bit) in the `/graphics/images` folder of the mod, such as `images/portraits/dwarf_portrait_body_palette.png`. |
|  LS_PALETTE_DEFAULTv50.13 | integer | Palette | Defines the default row of a layer set palette, conventionally 0. The exact color values on this row will be replaced on layer images with the colors in the same column, based on what row is passed as an argument to [`[USE_PALETTE]`](/index.php/Graphics_token#USE_PALETTE "Graphics token"). |
|  LG_CONDITION_BPv50.13 | selection criteria BY_TYPE, BY_CATEGORY, BY_TOKEN / category, type, or token | Layer / Group | Allows the entire layer group (rather than an individual layer) to be switched on and off depending on the conditions of a body part. Should accept the same tokens [`[CONDITION_BP]`](/index.php/Graphics_token#CONDITION_BP "Graphics token") does.\[Verify\] |
|  END_LAYER_GROUP |  | Layer / Group | Explicitly marks the end of a layer group, which allows layers after to not belong to any layer group. |
|  CONDITION_ITEM_WORN | BY_CATEGORY / BY_TOKEN / category / body part token / Armor type (ARMOR, GLOVES, Etc.) / Item ID(s) | Armor / Wieldables | Defines a clothing or armor graphic by the specific part it is equipped to, the / type / of armor it is, and the internal ID of that item. Additional arguments can be supplied to check for additional subtypes. Valid if any matching items are worn. / For example, a condition representing a right handed mitten or glove would be defined as: / \[CONDITION_ITEM_WORN:BY_TOKEN:RH:GLOVES:ITEM_GLOVES_MITTENS\] / Also accepts the input / ANY_HELD / or / WIELD / (e.g. / WIELD:WEAPON:ANY / ), though ANY_HELD has been bugged since v50.14. |
|  SHUT_OFF_IF_ITEM_PRESENT | BY_CATEGORY / BY_TOKEN / category / body part token / Armor type / Item ID(s) | Armor | Causes the current layer to not be rendered if the creature has one of the items worn or equipped. Also accepts the input `ANY_HELD` or `WIELD` (e.g. `WIELD:WEAPON:ANY`). Note that ANY_HELD has been bugged since v50.14. |
|  CONDITION_CASTE | caste name(s) | General | Displays this layer if the creature is this caste. Only one caste is accepted for each condition, but multiple caste conditions can be used in one layer and the layer will be displayed if any of them match. |
|  CONDITION_DYE | dye color | Armor | Represents which color the clothing is dyed. Partially-working. / v50.15 / Takes a / descriptor color / . Vanilla / dye / options: / MIDNIGHT_BLUE - ( / Dimple cup / ) / EMERALD - ( / Blade weed / ) / RED - ( / Hide root / ) / BLACK - ( / Sliver barb / ) |
|  CONDITION_NOT_DYED |  | Armor | Checks if the clothing is dyed.v50.15 |
|  CONDITION_MATERIAL_FLAG | material flag | Material | Changes graphics based on the material an equipped item is made of. Specifying multiple of this condition for a layer uses the "AND" instead of "OR" logical operator, whether placed in the same line or on separate lines. Valid material flags are similar to / reactant conditions / including: / WOVEN_ITEM / ANY_X_MATERIAL / with X being: / PLANT, SILK, YARN, LEATHER, WOOD, SHELL, BONE, STONE, GEM, TOOTH, HORN, PEARL / IS_DIVINE_MATERIAL / NOT_ARTIFACT / IS_CRAFTED_ARTIFACT / (Note that this token might not have ever worked.) / METAL_ITEM_MATERIAL / GLASS_MATERIAL / FIRE_BUILD_SAFE / MAGMA_BUILD_SAFE / GROWN_NOT_CRAFTED / v51.01-beta20 / among other, less useful ones. |
|  CONDITION_MATERIAL_TYPE | material token | Material | Changes graphics based on the material an equipped item is made of. Valid material types are `INORGANIC` or `METAL:IRON` where iron can be replaced with any weapons-grade metal. General material tokens are **not** functional. [`[CONDITION_MATERIAL_FLAG]`](/index.php/Graphics_token#CONDITION_MATERIAL_FLAG "Graphics token") is a better option for any material condition other than metal. |
| CONDITION_PROFESSION_CATEGORY / v50.01-v50.13 / Note: This condition is bugged and doesn't work since DFv50.14. | profession category token(s) | General | Checks the profession category of the creature to act as a condition. Multiple profession category tokens can be supplied as additional arguments, and will be valid for any of them. You can also use multiple of these tokens instead of listing them all in a single line, but this is functionally identical. Valid Profession tokens which are not categories will be ignored; values that do not match any existing Profession will be treated as `NONE` and thus apply to doctors, military, etc.. |
|  CONDITION_RANDOM_PART_INDEX | identifier / integer index / integer range | General | Chooses a random layer among layers with a CONDITION_RANDOM_PART_INDEX with the same identifier. Index is which option this condition is, out of Range number of options. Ex: / \[CONDITION_RANDOM_PART_INDEX:HEAD:3:4\] / is the third possible random head out of four total options. One of these random conditions each will be put into a set of four different sprites to add some random variation in the appearance of the creature's head. |
|  CONDITION_HAUL_COUNT_MIN | integer | General | Counts how many items the creature is hauling. Used for [`[PACK_ANIMAL]`](/index.php/Creature_token#PACK_ANIMAL "Creature token")s in vanilla. |
|  CONDITION_HAUL_COUNT_MAX | integer | General | Counts how many items the creature is hauling. Used for [`[PACK_ANIMAL]`](/index.php/Creature_token#PACK_ANIMAL "Creature token")s in vanilla. |
|  CONDITION_CHILD |  | General | Checks if the creature is a child or baby. |
|  CONDITION_NOT_CHILD |  | General | Checks if the creature is an adult. |
|  CONDITION_GHOST |  | General | Checks if the creature is a ghost. |
|  CONDITION_SYN_CLASS | SYN_CLASS | Syndrome | Changes graphics based on any syndromes the creature is affected by. Vanilla values include: / ZOMBIE / NECROMANCER / VAMPCURSE / RAISED_UNDEAD / DISTURBED_DEAD / GHOUL |
|  CONDITION_TISSUE_LAYER | BY_CATEGORY / body part category / or ALL / tissue layer / or ALL | Tissue | Selects a tissue layer to use for checking other conditions. Ex: / \[CONDITION_TISSUE_LAYER:BY_CATEGORY:ALL:SKIN\] |
|  TISSUE_MIN_LENGTH | integer | Tissue | Checks the current [`[CONDITION_TISSUE_LAYER]`](/index.php/Graphics_token#CONDITION_TISSUE_LAYER "Graphics token")'s LENGTH appearance modifier. Is true if the LENGTH is greater than the integer input. |
|  TISSUE_MAX_LENGTH | integer | Tissue | Checks the current [`[CONDITION_TISSUE_LAYER]`](/index.php/Graphics_token#CONDITION_TISSUE_LAYER "Graphics token")'s LENGTH appearance modifier. Is true if the LENGTH is less than the integer input. |
|  TISSUE_MAY_HAVE_COLOR | color token(s) | Tissue | Checks the selected tissue's color. Accepts multiple color tokens, and is true if the any of the colors is present in the selected tissues. |
|  TISSUE_MAY_HAVE_SHAPING | styling token | Tissue | Checks the current [`[CONDITION_TISSUE_LAYER]`](/index.php/Graphics_token#CONDITION_TISSUE_LAYER "Graphics token")'s shaping (hairstyle). Valid tokens are NEATLY_COMBED, BRAIDED, DOUBLE_BRAIDS, PONY_TAILS, CLEAN_SHAVEN and STANDARD_HAIR/BEARD/MOUSTACHE/SIDEBURNS_SHAPINGS.\[Verify\] |
|  TISSUE_NOT_SHAPED |  | Tissue | Checks the current [`[CONDITION_TISSUE_LAYER]`](/index.php/Graphics_token#CONDITION_TISSUE_LAYER "Graphics token")'s color. Accepts multiple color tokens, and is true if the any of the colors is present in the selected tissues. |
|  TISSUE_SWAP | IF_MIN_CURLY / integer / tile page id / x position / y position | Tissue | Checks if a tissue is sufficiently curly, and if so swaps to display a different image. The new image is defined by the tile page ID, x position, and y position. / This condition should be within a \[LAYER:... \] that has a similar graphic to the on in the TISSUE_SWAP. The current / \[CONDITION_TISSUE_LAYER\] / group must also include a / \[TISSUE_MIN_LENGTH\] / . |
|  ITEM_QUALITYv50.13 | integer | Armor / Wieldables | Checks the current [`[CONDITION_ITEM_WORN]`](/index.php/Graphics_token#CONDITION_ITEM_WORN "Graphics token")'s quality. 0 is base quality, 5 is masterwork. See \[CONDITION_MATERIAL_FLAG:NOT_ARTIFACT\] for non-artifact-quality items. |
|  USE_PALETTEv50.13 | layer set palette / row | General | Colors the layer using that row of either the layer-set-specific [`[LS_PALETTE]`](/index.php/Creature_token#LS_PALETTE "Creature token") or a predefined palette such as DEFAULT. |
|  USE_STANDARD_PALETTE_FROM_ITEMv50.13 |  | Armor / Wieldables | Uses the default palette to render the layer based on the color of the current [`[CONDITION_ITEM_WORN]`](/index.php/Graphics_token#CONDITION_ITEM_WORN "Graphics token"). |
|  CONDITION_BPv50.13 | selection criteria BY_TYPE, BY_CATEGORY, BY_TOKEN / category, type, or token | Body | Defines a body part graphic using standard body token selection criteria. |
|  BP_APPEARANCE_MODIFIER_RANGEv50.13 | QUALITY / minimum / maximum | Body | Checks if current [`[CONDITION_BP]`](/index.php/Graphics_token#CONDITION_BP "Graphics token")'s [`[BP_APPEARANCE_MODIFIER]`](/index.php/Creature_token#BP_APPEARANCE_MODIFIER "Creature token") falls within the chosen range. |
|  BP_PRESENTv50.13 |  | Body | Checks if the current [`[CONDITION_BP]`](/index.php/Graphics_token#CONDITION_BP "Graphics token") is present and not destroyed, pulped, or severed. Can also be applied to [`[LG_CONDITION_BP]`](/index.php/Graphics_token#LG_CONDITION_BP "Graphics token"). |
|  BP_SCARREDv50.13 |  | Body | Checks if the current [`[CONDITION_BP]`](/index.php/Graphics_token#CONDITION_BP "Graphics token") is scarred. Seems to also require [`[BP_PRESENT]`](/index.php/Graphics_token#BP_PRESENT "Graphics token") to avoid illogical results.\[Verify\] |

### Vermin Conditions

Special Conditions for [`[VERMIN]`](/index.php/Creature_token#VERMIN "Creature token") creature graphics:

|  |  |
|----|----|
| Condition | Description |
|  VERMIN | The default graphic for this vermin. |
|  VERMIN_ALT | Image cycles every 1 second. |
|  SWARM_SMALL | For swarming vermin like flies and fairies in small groups. |
|  SWARM_MEDIUM | For swarming vermin like flies and fairies in medium-sized groups. |
|  SWARM_LARGE | For swarming vermin like flies and fairies in large groups. |
|  LIGHT_VERMIN | For fireflies etc. Does not replace [`[VERMIN]`](/index.php/Graphics_token#VERMIN "Graphics token"). |
|  LIGHT_VERMIN_ALT | Like [`[VERMIN_ALT]`](/index.php/Graphics_token#VERMIN_ALT "Graphics token") for fireflies etc. |
|  LIGHT_SWARM_SMALL | Unused. |
|  LIGHT_SWARM_MEDIUM | Unused. |
|  LIGHT_SWARM_LARGE | Unused. |
|  REMAINS | Vermin corpses. |
|  HIVE | Vermin hives. |

## Item Graphics

Item graphics can also be defined, but are mostly hardcoded. This section of the wiki needs to be fleshed out. Descriptions of the token functions is provisional.

Item graphics currently do not support LARGE_IMAGE.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
|  TILE_GRAPHICS | Tile page ID / x index / y index / Item ID | Begins defining tile graphics for an item. Sets default tile graphic.\[Verify\] |
|  BOULDER_GRAPHICS | Tile page ID / x index / y index / Material ID | Defines tile graphics variants to use for BOULDER items by material; currently all boulders use material palette instead. |
|  ROUGH_GEM_GRAPHICS | Tile page ID / x index / y index / Material ID | Defines tile graphics variants to use for ROUGH (gem) items by material; currently all rough gems use material palette instead. |
|  BARS_GRAPHICS | Tile page ID / x index / y index / Material ID or item ID | Defines tile graphics variants to use for BAR items by material. |
|  FOOD_GRAPHICS | Tile page ID / x index / y index / Item ID | Defines tile graphics for FOOD items. |
|  CHEESE_GRAPHICS | Tile page ID / x index / y index / Material ID | Defines tile graphics variants to use for CHEESE items by material. Unused in vanilla raws. |
|  ARMOR_GRAPHICS | Tile page ID / x index / y index / Item ID | Defines tile graphics for ARMOR items; this is for items not being worn by a creature. |
|  GLOVES_GRAPHICS | Tile page ID / x index / y index / Item ID | Defines tile graphics for GLOVES items; this is for items not being worn by a creature. |
|  HELM_GRAPHICS | Tile page ID / x index / y index / Item ID | Defines tile graphics for HELM items; this is for items not being worn by a creature. |
|  PANTS_GRAPHICS | Tile page ID / x index / y index / Item ID | Defines tile graphics for PANTS items; this is for items not being worn by a creature. |
|  SHOES_GRAPHICS | Tile page ID / x index / y index / Item ID | Defines tile graphics for SHOES items; this is for items not being worn by a creature. |
|  SHOES_GRAPHICS_METAL | Tile page ID / x index / y index / Item ID | Defines metal material tile graphics variants for SHOES items; this is for items not being worn by a creature. |
|  SHIELD_GRAPHICS | Tile page ID / x index / y index / Item ID | Defines tile graphics for SHIELD items; this is for items not being worn by a creature. |
|  SHIELD_GRAPHICS_WOODEN | Tile page ID / x index / y index / Item ID | Defines wood material tile graphics variants for SHIELD items; this is for items not being worn by a creature. |
|  TOY_GRAPHICS | Tile page ID / x index / y index / Item ID / Material ID | Defines tile graphics for TOY items. Material ID in this case is one of STONE, WOOD, METAL, or GLASS. |
|  TRAPCOMP_GRAPHICS | Tile page ID / x index / y index / Item ID | Defines tile graphics for TRAPCOMP items. |
|  TRAPCOMP_GRAPHICS_WEAPON_TRAP | Tile page ID / x index / y index | Defines tile graphics for TRAPCOMP items when built into a weapon trap; must follow TRAPCOMP_GRAPHICS. |
|  TRAPCOMP_GRAPHICS_UPRIGHT\_#X | Tile page ID / x index / y index | Defines tile graphics for installed upright spike traps. These comprise two-tile graphics: \# is replaced with the number of spikes, 1-10; X is replaced with T (for top graphic tile) or B (bottom graphic tile). This follows the tile graphics definition of either MENACINGSPIKE or SPEAR. |
|  SIEGEAMMO_GRAPHICS | Item ID | Begins defining graphics for SIEGEAMMO items. |
|  SIEGEAMMO_GRAPHICS_STRAIGHT_DEFAULT | Tile page ID / x index / y index | Defines graphics for ballista arrows aligned orthogonally on the map; follows SEIGEAMMO_GRAPHICS. |
|  SIEGEAMMO_GRAPHICS_STRAIGHT_WOOD | Tile page ID / x index / y index | Wooden variant of above. |
|  SIEGEAMMO_GRAPHICS_DIAGONAL_DEFAULT | Tile page ID / x index / y index | Defines graphics for ballista arrows aligned diagonally on the map; follows SEIGEAMMO_GRAPHICS. |
|  SIEGEAMMO_GRAPHICS_DIAGONAL_WOOD | Tile page ID / x index / y index | Wood variant of above. |
|  AMMO_GRAPHICS | Item ID | Begins defining graphics for AMMO items. |
|  AMMO_GRAPHICS_STRAIGHT_DEFAULT | Tile page ID / x index / y index | Defines graphics for AMMO items aligned orthogonally on the map; follows AMMO_GRAPHICS. |
|  AMMO_GRAPHICS_STRAIGHT_WOOD | Tile page ID / x index / y index | Wooden variant of above. |
|  AMMO_GRAPHICS_DIAGONAL_DEFAULT | Tile page ID / x index / y index | Defines graphics for AMMO aligned diagonally on the map; follows AMMO_GRAPHICS. |
|  AMMO_GRAPHICS_DIAGONAL_WOOD | Tile page ID / x index / y index | Wood variant of above. |
|  WEAPON_GRAPHICS | Item ID | Begins defining graphics for WEAPON items. |
|  WEAPON_GRAPHICS_DEFAULT | Tile page ID / x index / y index | Defines default graphics for WEAPON item defined by WEAPON_GRAPHICS not being worn by creatures; follows WEAPON_GRAPHICS. |
|  WEAPON_GRAPHICS_MATERIAL | Tile page ID / x index / y index | Defines material palette\[Verify\] graphics for WEAPON item defined by WEAPON_GRAPHICS not being worn by creatures; follows WEAPON_GRAPHICS. |
|  WEAPON_GRAPHICS_WOOD_GROWN | Tile page ID / x index / y index | Defines graphics for grown-wood WEAPON item defined by WEAPON_GRAPHICS not being worn by creatures; follows WEAPON_GRAPHICS. |
|  WEAPON_GRAPHICS_WOOD | Tile page ID / x index / y index | Defines graphics for wooden WEAPON item defined by WEAPON_GRAPHICS not being worn by creatures; follows WEAPON_GRAPHICS. |
|  WEAPON_GRAPHICS_WEAPON_TRAP | Tile page ID / x index / y index | Defines graphics for WEAPON item defined by WEAPON_GRAPHICS as it appears installed in a weapon trap; follows WEAPON_GRAPHICS. |
|  TOOL_GRAPHICS | Tile page ID / x index / y index / Item ID | Defines default graphics for TOOL items; also begins defining variant graphics for material or container conditions when followed by tokens below. |
|  ADD_TOOL_GRAPHICS | Item ID | Adds graphics to an existing tool defined with TOOL_GRAPHICS, followed by the tool graphics material or container condition tokens below. |
|  TOOL_GRAPHICS_WOOD | Variant index / Tile page ID / x index / y index | Defines additonal variant graphics for wooden TOOL items defined by TOOL_GRAPHICS; follows TOOL_GRAPHICS or ADD_TOOL_GRAPHICS. Requires seven variants; the resulting tool graphic is selected randomly from these (they can all point to the same tile index if desired). |
|  TOOL_GRAPHICS_STONE | Variant index / Tile page ID / x index / y index | Defines additonal variant graphics for stone TOOL items defined by TOOL_GRAPHICS; follows TOOL_GRAPHICS or ADD_TOOL_GRAPHICS. Requires seven variants; the resulting tool graphic is selected randomly from these (they can all point to the same tile index if desired). |
|  TOOL_GRAPHICS_METAL | Variant index / Tile page ID / x index / y index | Defines additonal variant graphics for metal TOOL items defined by TOOL_GRAPHICS; follows TOOL_GRAPHICS or ADD_TOOL_GRAPHICS. Requires seven variants; the resulting tool graphic is selected randomly from these (they can all point to the same tile index if desired). |
|  TOOL_GRAPHICS_GLASS | Variant index / Tile page ID / x index / y index | Defines additonal variant graphics for glass TOOL items defined by TOOL_GRAPHICS; follows TOOL_GRAPHICS or ADD_TOOL_GRAPHICS. Requires seven variants; the resulting tool graphic is selected randomly from these (they can all point to the same tile index if desired). |
|  TOOL_GRAPHICS_CONTAINER_WOOD_LIQUID | Tile page ID / x index / y index | Defines graphics for wooden liquid-containing containers (empty); follows ADD_TOOL_GRAPHICS definition for container. |
|  TOOL_GRAPHICS_CONTAINER_STONE_LIQUID | Tile page ID / x index / y index | Defines graphics for stone liquid-containing containers (empty); follows ADD_TOOL_GRAPHICS definition for container. |
|  TOOL_GRAPHICS_CONTAINER_METAL_LIQUID | Tile page ID / x index / y index | Defines graphics for metal (and glass?) liquid-containing containers (empty); follows ADD_TOOL_GRAPHICS definition for container. |
|  TOOL_GRAPHICS_CONTAINER_LIQUID | Tile page ID / x index / y index | Defines graphics for the liquid filling a liquid-containing container; follows TOOL_GRAPHICS_CONTAINER\_\*\_LIQUID. |
|  TOOL_GRAPHICS_CONTAINER_WOOD_ITEM | Tile page ID / x index / y index | Defines graphics for wooden containers holding items; follows ADD_TOOL_GRAPHICS definition for container. |
|  TOOL_GRAPHICS_CONTAINER_STONE_ITEM | Tile page ID / x index / y index | Defines graphics for stone containers holding items; follows ADD_TOOL_GRAPHICS definition for container. |
|  TOOL_GRAPHICS_CONTAINER_METAL_ITEM | Tile page ID / x index / y index | Defines graphics for metal (and glass?) containers holding items; follows ADD_TOOL_GRAPHICS definition for container. |
|  TOOL_GRAPHICS_HIVE_BLD | Tile page ID / x index / y index | Defines the built item graphics for HIVE items. |
|  TOOL_GRAPHICS_HIVE_BLD_IN_USE | Tile page ID / x index / y index | Defines the built item graphics for HIVE items that have hives installed. |
|  TOOL_GRAPHICS_HIVE_PRODUCTS | Tile page ID / x index / y index | Defines the built item graphics for HIVE items that are ready to be harvested. |
|  TOOL_GRAPHICS_SHAPE | Shape ID / Tile page ID / x index / y index | Defines graphics for shaped items; currently used for dice. |

## World Map Graphics

World map graphics are defined in `Dwarf Fortress``\data\vanilla\vanilla_world_map\graphics\graphics_world_map.txt` Tokens that accept variants have 5 of them:

       [TILE_GRAPHICS:::::1]
       [TILE_GRAPHICS:::::2]
       [TILE_GRAPHICS:::::3]
       [TILE_GRAPHICS:::::4]
       [TILE_GRAPHICS:::::5]

Otherwise:

      [TILE_GRAPHICS::::]

## See Also

- Creature token
- Syndrome
- Creature examples
