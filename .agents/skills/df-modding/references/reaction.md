# Reaction

> Fonte: [Reaction](https://dwarffortresswiki.org/index.php/Reaction) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

\

**Reactions** are modular, editable formulas that take specific ingredients, or reagents, and use them to produce a desired item. Most manufacturing jobs are hardcoded—building beds or creating glass, for example—but a few are data-driven, and it's (sometimes) quite simple to add additional ones. There is a separate page with custom reaction examples.

## Reaction differences between modes

In fortress mode, reactions are linked to specific buildings, and must be added to a civilization's entity file to be usable by that civilization. This has the useful effect of limiting new items and materials (such as special wood or metal) to civilizations that have the requisite reaction — so that if you give your custom civilization a reaction to produce "star metal" or some other custom material, only they will be able to produce it. Exclusive non-[`[SPECIAL]`](/index.php/Inorganic_material_definition_token#SPECIAL "Inorganic material definition token") metals, such as steel, may appear on bandits and other entities with access to all materials.

In adventure mode, reactions are freely available in the x create menu, and any adventurer character can make free use of them. Reagents may be held in the hands or dropped on the ground, but cannot be used within a backpack or quiver. There are several bugs with adventure mode reactions, chief of which is the fact that you cannot select liquid reagents.\[Verify\]

## Anatomy of a reaction

Reactions are found within reaction_x files (such as reaction_smelter or reaction_other). All reaction files must begin with the file name, followed by the `[OBJECT:REACTION]` token that tells the game that the file contains reaction definitions.

The reactions themselves generally adhere to the following structure:

      [REACTION:]
         [NAME:]
         [BUILDING::]
         [REAGENT:A:150:BAR:NONE:POTASH:NONE]
         [PRODUCT:100:1:BAR:NONE:PEARLASH:NONE][PRODUCT_DIMENSION:150]
         [FUEL]
         [SKILL:]
         [MAX_MULTIPLIER:]
         [AUTOMATIC]
         [ADVENTURE_MODE_ENABLED]
         [DESCRIPTION:]

- *identifier*: The internal ID of the reaction.
- *name*: The name of the reaction, visible to the player in the Fortress mode or Adventure mode menus.
- *building*: The building ID that the reaction uses, and the relevant keyboard shortcut.
- *...reagents...*: Zero or more reagents (ingredients) that are required to be in stock for the reaction to be possible.
- *...products...*: Zero or more products that are created from the reaction.
- *fuel*: (optional) If present, the reaction requires charcoal, coke or a magma-powered workshop.
- *skill*: (optional) The skill required and trained by the reaction.
- *multiplier*: (optional) If present, the reaction will only be done the specified number of times per job; used to limit the output of reactions that accept stacks of items as reagents.
- *automatic*: (optional) If present, the reaction will automatically be enqueued whenever it can possibly be performed.
- *adventure mode enabled*: (optional) If present, the reaction can be used by the player in Adventure mode.
- *description*: (optional) If present, shows pop-up description when the reaction is selected in workshop (not working in v50).

### Reaction identifier

The REACTION token assigns a unique ID to your reaction.

       [REACTION:]

The *reaction identifier* may be anything, so long as it is unique within the raw data files. A good habit to get into is to append a short prefix or suffix to each name related to the name of your mod, to ensure nobody else is going to make an identical reaction and thereby mess up the game if their mod is run alongside yours. This is referenced in an entity definition via [`[PERMITTED_REACTION]`](/index.php/Entity_token#PERMITTED_REACTION "Entity token") to allow that entity to use the reaction.

### Reaction name

The REACTION_NAME token assigns a descriptive name to your reaction in-game.

       [REACTION_NAME:]

#### Name

This can be anything at all, and is how the reaction will appear in the job list of the building it is assigned to, and so should describe the reaction. **Tan a hide**, for example, is the name of the default leather-producing reaction. Generally this should be written as a small descriptive verb phrase, with the first letter capitalized, for consistency with the existing reactions.

### Building

The BUILDING token assigns the reaction to a building. Adding multiple BUILDING tokens will cause the reaction to be available at all of the specified buildings. Omitting the BUILDING token entirely will make the reaction unusable in Fortress mode (often used to restrict certain reactions to Adventure mode).

       [BUILDING::]

- *building name:* The ID of the building the reaction appears in.
- *building key:* The hotkey to queue up the reaction in the specified building.

#### Building name

This is the ID of the building where the reaction will be carried out. Valid building names are as follows:

- ASHERY - Ashery
- BOWYER - Bowyer's workshop
- CARPENTER - Carpenter's workshop
- CLOTHES - Clothier's shop
- CRAFTSMAN - Craftsdwarf's workshop
- DYER - Dyer's shop
- FARMER - Farmer's workshop
- GLASS - Glass furnace
- KILN - Kiln and Magma kiln
- KITCHEN - Kitchen
- LEATHER - Leather works
- MASON - Stoneworker's workshop
- METALSMITH - Metalsmith's forge
- MILLSTONE - Millstone
- QUERN - Quern
- SIEGE - Siege workshop
- SMELTER - Smelter and Magma smelter
- STILL - Still
- TANNER - Tanner's shop
- WOOD - Wood furnace
- Any custom (raw-defined) building, such as:
  - SOAP_MAKER - Soap maker's workshop
  - SCREW_PRESS - Screw press

#### Building key

This used to define the shortcut key(s) used to queue up the reaction in a workshop during gameplay. Doesn't do anything in the current version. v50.01

### Category

Categories are custom submenus for buildings' reaction menus. A reaction doesn't require a category, but if you have a lot of reactions, categories can be invaluable for organizing and presenting those reactions to players.

Categories can be nested indefinitely—you can have a category within a category within a category within a category within a category within... but as a practical matter, nesting categories more than 2 deep is not recommended.

Categories will be displayed in alphabetical order, first off the file name and then off the category name. They currently have no effect on adventure mode reactions.

#### Defining a category

Each category needs to be defined within a reaction, usually one which should appear within its menu. Categories only need to be defined once.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
| CATEGORY | Category ID | The category ID is a unique identifier for the category. It is only used in the raws, and will not appear in the game. / If you're defining multiple categories within the same reaction - for example, if you intend the reaction to be nested two deep, and haven't yet defined the super-category - the / last / CATEGORY token within the reaction definition is the one that the reaction will appear in. |
| CATEGORY_NAME | String | The name of the category as displayed in-game. |
| CATEGORY_DESCRIPTION | String | Optional. If present, when the category is highlighted in a building menu, this string will be displayed in the Helpful Hint box. |
| CATEGORY_PARENT | Category ID | Optional. If present, this category will be a submenu of the indicated category, rather than a submenu of the reaction's building. |
| CATEGORY_KEY | Hotkey token | Optional. If present, this category can be selected from its parent menu (whether a building or a parent category) using the given hotkey. Uses the same format as the BUILDING KEY described above. |

#### Adding reactions to an existing category

Just include the tag \[CATEGORY:\] within your reaction definition, and if the category exists, your reaction will be added to its menu. You can only add reactions to custom categories.

Each reaction can belong to only one category.

### Reagents

REAGENTs are a little bit complicated. They are the ingredients that the reaction will use. You can define as many as you like within a reaction.

       [REAGENT::::][...modifiers...]

- *name*: The name of the reagent, local to the reaction.
- *quantity*: The amount of the item that will be used in the reaction.
- *item token*: The type (and subtype) of the item you require.
- *material token*: The material the item should be made of.
- *...modifiers...*: Zero or more tokens which further clarify the acceptable types when the item type and material types are insufficient to distinguish them.

#### Name

The name field is a small string used to identify the reagent within the reaction, which is not visible to the player, but local to the reaction, and does not need to be unique across all of the reactions, so you can reuse the same names over and over, although each reagent within the same individual reaction must have a different name.

Most reagents are simply named **A**, **B**, and so forth in default reactions, although names such as **TOOLSTONE**, **FLUX**, or **seeds** will also work equally well. The PRODUCT may make reference to this name – for instance, if a container **B** is specified as a reagent, PRODUCT_TO_CONTAINER:B specifies that container.

#### Quantity

How many or how much of this reagent the reaction requires. For most item types this is just the number of them required. However, some other item types─specifically bars, cloth, thread, globs, liquids, powder, and sheets of paper or parchment─instead use numbers representing the size of the material within one (or more) of these items. For example, while REAGENT:A:***10***:***TOY***:NONE:NONE:NONE is ten unique, solid toy items, REAGENT:A:***10***:***THREAD***:NONE:NONE:NONE is an extremely tiny portion of a random spool of thread. One can see which items have what size quantities in the description of the PRODUCT_DIMENSION token.

If one of the reagents is in a stack, or the reaction is only using a fraction of the amount of a sized item, the reaction will consume the entire stack, or as much of the sized item as possible, and multiply the product accordingly. This behaviour can be controlled using the MAX_MULTIPLIER token.

#### Item token

Item tokens are of the form ITEM_TYPE:ITEM_SUBTYPE.

The ITEM_TYPE is the category of item you require; WEAPON, TOY or SKIN_TANNED, for example.

The ITEM_SUBTYPE is name of the exact item that you require. Examples are ITEM_WEAPON_SPEAR or ITEM_TOY_PUZZLEBOX. Some items, like quivers or backpacks, or chunks of stone or metal, have no subtype and only require the item token to be filled in; so if you're asking for those you should set the subtype to NONE. Subtypes are defined within the local raw data files and their exact names can be referenced by looking at the corresponding file.

For reagents, the item token can also be set to ANY_RAW_MATERIAL:NONE (to permit BAR, BOULDER, POWDER_MISC, or GLOB) or ANY_CRAFT:NONE (to permit FIGURINE, AMULET, SCEPTER, CROWN, RING, EARRING, or BRACELET). Internally, these special values are both converted to NONE:NONE and merely set special modifiers (similar to \[BUILDMAT\])—they cannot be used in any other context.

For backwards compatibility, reagents can also accept "METAL_ORE:metal_id" in place of both the item and material tokens—this is equivalent to using the reagent BOULDER:NONE:NONE:NONE with the modifier \[METAL_ORE:metal_id\] (see below).

When no item type is specified (as in NONE:NONE), workers will not be able to find otherwise eligible items if they are inside of barrels (at least when reagents are PLANT or PLANT_GROWTH type). This is likely a bug.

#### Material token

Material tokens come in several forms. For most reagents, this will typically be INORGANIC:MATERIAL_ID or NONE:NONE (to allow multiple materials using other modifier tokens).

Some reactions will allow the player to select specific materials after creating the job (or in some cases, armor size from the product), by clicking on  next to the job in the workshop queue. To permit this behaviour in your reaction, the reagent materials must be specified as follows:

|  |  |  |
|----|----|----|
| Item Type | Material | Notes |
| BAR / BLOCKS / BOULDER / ROUGH / SMALLGEM | INORGANIC:NONE | These all appear as "stone" in the material selection menu, and list all inorganic materials regardless of any material modifier tokens, eg. \[ITEMS_METAL\]. BAR and BLOCKS made of organic materials, and BOULDER made of clay, are excluded. |
| SKIN_TANNED or WOOD | NONE:NONE |  |
| Other Item Types | NONE:NONE | These will appear if a material modifier token other than \[ANY_LEATHER_MATERIAL\] is included. |

#### Modifiers

Reagents may also have extra tokens added on, following the REAGENT token, in order to modify their behaviour.

Generally speaking, if you set a field in a reagent to NONE, the reaction won't discriminate when it comes to that particular field. For example, if you require a BOULDER reagent but leave the material as NONE:NONE, it will grab any available BOULDER-type item regardless of material. Modifiers can then be used to restrict this to only certain broad classes of materials.

The following is a list of all known reagent modifiers:

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
| ANY_BONE_MATERIAL |  | Reagent material must have the \[BONE\] token. |
| ANY_GEM_MATERIAL |  | Reagent material must have the \[IS_GEM\] token. |
| ANY_HORN_MATERIAL |  | Reagent material must have the \[HORN\] token. |
| ANY_LEATHER_MATERIAL |  | Reagent material must have the \[LEATHER\] token. |
| ANY_PEARL_MATERIAL |  | Reagent material must have the \[PEARL\] token. |
| ANY_PLANT_MATERIAL |  | Reagent material must be subordinate to a PLANT object. |
| ANY_SHELL_MATERIAL |  | Reagent material must have the \[SHELL\] token. |
| ANY_SILK_MATERIAL |  | Reagent material must have the \[SILK\] token. |
| ANY_SOAP_MATERIAL |  | Reagent material must have the \[SOAP\] token. |
| ANY_STONE_MATERIAL |  | Reagent material must have the \[IS_STONE\] token. |
| ANY_STRAND_TISSUE |  | Reagent is made of a tissue having TISSUE_SHAPE:STRANDS, intended for matching hair and wool. Must be used with USE_BODY_COMPONENT. |
| ANY_TOOTH_MATERIAL |  | Reagent material must have the \[TOOTH\] token. |
| ANY_WOOD_MATERIAL |  | Reagent material must have the \[WOOD\] token. |
| ANY_YARN_MATERIAL |  | Reagent material must have the \[YARN\] token. |
| BUILDMAT |  | Reagent must be a general building material - BAR, BLOCKS, BOULDER, or WOOD. |
| CAN_USE_ARTIFACT |  | Reagent can be an Artifact. Using \[PRESERVE_REAGENT\] with this is strongly advised. |
| CONTAINS | Reagent name | Reagent is a container that holds the specified reagent (where *Reagent name* is the locally-defined name of the reagent). |
| CONTAINS_LYE |  | Reagent must be a BARREL or TOOL which contains at least one item of type LIQUID_MISC made of LYE. Use of this token is discouraged, as it does not work with buckets (instead, use \[CONTAINS:lye\] — note the colon — and a corresponding lye reagent \[REAGENT:lye:150:LIQUID_MISC:NONE:LYE\]). |
| DOES_NOT_ABSORB |  | Reagent material must have ABSORPTION:0 |
| DOES_NOT_DETERMINE_PRODUCT_AMOUNT |  | Reagent quantity is ignored for the purposes of producing extra outputs. Typically used for containers so that stacks of reagents will correctly produce additional outputs. |
| EMPTY |  | If the reagent is a container, it must be empty. |
| FIRE_BUILD_SAFE |  | Reagent material must be solid and stable at temperatures approaching 11000. Only works with items of type BAR, BLOCKS, BOULDER, WOOD, and ANVIL - all others are considered unsafe. |
| FOOD_STORAGE_CONTAINER |  | Reagent is either a BARREL or a TOOL with the FOOD_STORAGE use. |
| GLASS_MATERIAL |  | Reagent material must have the IS_GLASS token. All 3 types of glass have this token hardcoded. |
| HARD_ITEM_MATERIAL |  | Reagent material must have the \[ITEMS_HARD\] token. |
| HAS_EDGE |  | Reagent must have an edge. |
| HAS_ITEM_REACTION_PRODUCT | PRODUCT_ID | Reagent material must have the item reaction product specified by PRODUCT_ID - see below for more details. This can be used interchangeably with HAS_MATERIAL_REACTION_PRODUCT. |
| HAS_MATERIAL_REACTION_PRODUCT | PRODUCT_ID | Reagent material must have the material reaction product specified by PRODUCT_ID - see below for more details. |
| HAS_TOOL_USE | TOOL_USE / value | Reagent must be a tool with the specific TOOL_USE value. The reagent's item type must be TOOL:NONE for this to make any sense. |
| IS_CRAFTED_ARTIFACT\[Verify\] |  | Reagent item must be an artifact. |
| IS_DIVINE_MATERIAL |  | Reagent material must have the \[DIVINE\] token. |
| IS_SAND_MATERIAL |  | Reagent material must have the \[SOIL_SAND\] token. |
| MAGMA_BUILD_SAFE |  | Reagent material must be solid and stable at temperatures approaching 12000. Only works with items of type BAR, BLOCKS, BOULDER, WOOD, and ANVIL - all others are considered unsafe. |
| METAL_ITEM_MATERIAL |  | Reagent material must have the \[ITEMS_METAL\] token. |
| METAL_ORE | Metal ID | Reagent material must be an ore of the specified metal. |
| MIN_DIMENSION | Integer | Reagent's item size must be at least as large as *Integer*. The reagent's item type must be BAR, POWDER_MISC, LIQUID_MISC, DRINK, THREAD, CLOTH, or GLOB for this to work. See PRODUCT_DIMENSION below. |
| NO_EDGE_ALLOWED |  | Reagent must not have an edge, so must be blunt. Sharp stones (produced using knapping) and most types of weapon/ammo can not be used with this token. |
| NOT_ARTIFACT\[Verify\] |  | Reagent item must not be an artifact. |
| NOT_CONTAIN_BARREL_ITEM |  | If the reagent is a container, it must not contain lye or milk. Not necessary if specifying \[EMPTY\]. |
| NOT_ENGRAVED |  | Reagent can not be engraved. For example, a memorial slab can not be engraved. |
| NOT_IMPROVED |  | Reagent has not been decorated. |
| NOT_PRESSED |  | Reagent must not be in the SOLID_PRESSED state. |
| NOT_WEB |  | Reagent must be collected (to distinguish silk thread from webs). Only makes sense for items of type THREAD. |
| ON_GROUND |  | Reagent must be on the ground. Grabs from stockpiles. Does not grab from inventories (workshops, wagon) and causes infinite gathering for reactions in workshop. |
| POTASHABLE (Deprecated) |  | Alias for \[CONTAINS_LYE\]. |
| PRESERVE_REAGENT |  | Reagent is not destroyed, which is the normal effect, at the completion of the reaction. Typically used for containers. |
| REACTION_CLASS | CLASS_ID | Reagent material must have the reaction class specified by CLASS_ID - see below for more details. |
| UNROTTEN |  | Reagent must not be rotten, mainly for organic materials. |
| USE_BODY_COMPONENT |  | Reagent must be a body part (CORPSE or CORPSEPIECE). Must be used even if your reagent item type is CORPSE or CORPSEPIECE, otherwise it will match any item. |
| WEB_ONLY |  | Reagent must be undisturbed (to distinguish silk thread from webs). Only makes sense for items of type THREAD. |
| WORTHLESS_STONE_ONLY |  | Reagent material must be non-economic. |
| WOVEN_ITEM |  | Reagent must be a clothing item made of a woven material, ie. plant, silk, or yarn cloth. |

### Products

Products are the end product of the reaction. A reaction can have as many products as it likes.

Products are almost identical to reagents, except that they do not need to be named, can't have fields undefined, and don't use the quantity field to determine the product size. Instead, the token \[PRODUCT_DIMENSION:X\] is tacked on after the PRODUCT token, determining the size of the product.

Products can be produced directly to a container using the \[PRODUCT_TO_CONTAINER:*name*\] token, where the *name* is the name of a reagent. This requires the reagent to have the \[PRESERVE_REAGENT\] token.

Restating this in the above style, we have:

      [PRODUCT::::][...modifiers...]

#### Probability

The percentage chance the product will be produced when the reaction is completed. Must be an integer.

#### Quantity

Determines how many of the product will be produced. For the item types AMMO, REMAINS, MEAT, FISH, FISH_RAW, PLANT, PLANT_GROWTH, DRINK, CHEESE, LIQUID_MISC, COIN, and EGG, the resulting items will be created as a single stack, while all other item types will produce multiple individual items.

If a reaction can take stacks of input items, then it will attempt to perform the reaction enough times to consume as many full sets of reagents as it can—for example, if a reaction "1 piece of meat + 2 pieces of fish -\> 3 pieces of cheese" is given a stack of 5 meat and 5 fish, it will produce 6 pieces of cheese and leave 3 meat and 1 fish behind. Using the token DOES_NOT_DETERMINE_PRODUCT_AMOUNT allows a reagent to be excluded from this calculation - for example, with the reaction "1 plant + 1 barrel -\> 5 alcohol (into barrel)", using this on the barrel allows the reaction to be performed as "5 plant + 1 barrel -\> 25 alcohol" instead of "5 plant + 5 barrel -\> 25 alcohol".

#### Item token

The item token and subtype of the item you produce.

If your item has an item reaction product and you want the item type and material to be derived from one of the reagents, you can use GET_ITEM_DATA_FROM_REAGENT:reagent:REACTION_PRODUCT_ID in place of both the item token *and* the material token (see next section). You can also specify GET_ITEM_DATA_FROM_REAGENT:reagent:NONE in order to make a direct copy of the source item, though this will not work for complex items such as corpses or prepared meals.

For products, this can also be set to CRAFTS:NONE to produce up to three random craft items. This value cannot be used in any other context.

#### Material token

A material token describing what the product will be made of.

If you want the product's material to be derived from one of the reagents, you can use GET_MATERIAL_FROM_REAGENT:reagent:NONE in place of the material token in order to directly use the reagent's own material; if the reagent has a material reaction product defined, you can use GET_MATERIAL_FROM_REAGENT:reagent:REACTION_PRODUCT_ID to use that.

Similarly to choosing material types for a reagent, if the item product is armor/clothing, and has the appropriate armor token in the entity file, you will be able to choose the armor/clothing size for different creatures by clicking  of the workshop task. However, this will only work if the product material is cloth leather or certain metals, and the item is also recognized by the related vanilla workshop reaction\[Verify\].

#### Product modifiers

Zero or more tokens which further set the properties or disposition of the resulting product item.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
| FORCE_EDGE |  | Product is given a sharp edge. Used for knapping. |
| PRODUCT_PASTE |  | Product is created in the SOLID_PASTE state. |
| PRODUCT_PRESSED |  | Product is created in the SOLID_PRESSED state. |
| PRODUCT_DIMENSION | Integer | Specifies the dimension of the product for those items that use dimensions. For items of type BAR, DRINK, GLOB, LIQUID_MISC, and POWDER_MISC, one item is dimension 150; one item of CLOTH or SHEET is dimension 10000; and one item of THREAD is dimension 15000. Has no effect on any other item types. Note: this is not the actual storage volume of the product, which is hard-coded by the item token. |
| PRODUCT_TO_CONTAINER | Name | Places the product in a container; *Name* must be the name of a reagent with the \[PRESERVE_REAGENT\] token and a container item type. |
| PRODUCT_TOKEN | Name | Allows the product to be referred to by the given name for the purpose of being passed down as and argument in other tokens, in the same fashion as reagent names. |
| TRANSFER_ARTIFACT_STATUS |  | Transfers artifact status from the reagent to the product. |

### Improvements

Improvements are applied to existing reagents. A reaction can have as many improvements as it likes.

Restating this in the above style, we have:

      [IMPROVEMENT::::]

#### Probability

The percentage chance the improvement will be applied to the reagent when the reaction is completed.

#### Reagent name

The name of the reagent that will be improved. In order to be meaningful, this reagent must have \[PRESERVE_REAGENT\].

#### Improvement type

The following improvement types can be used:

|  |  |
|----|----|
| Token | Description |
| COVERED | Item is encrusted/studded/decorated with . |
| GLAZED | Item is glazed with . |
| RINGS_HANGING | Item is adorned with hanging rings of . |
| BANDS | Item is encircled with bands of . |
| SPIKES | Item menaces with spikes of . |
| PAGES | Adds pages to a book. |
| SPECIFIC | With subtype ROLLERS, adds rollers of to a scroll; with subtype HANDLE, adds a handle of to an item; with subtype TRACTION_BENCH_CHAIN or TRACTION_BENCH_ROPE adds a chain or rope of to an item. |

All other item improvement tokens (ART_IMAGE, ITEMSPECIFIC, THREAD, CLOTH, SEWN_IMAGE, and ILLUSTRATION) are ignored.

#### Material token

A material token describing what the decoration will be made of.

If you want the product's material to be derived from one of the reagents, and the reagent has a material reaction product defined, you can use GET_MATERIAL_FROM_REAGENT:reagent:REACTION_PRODUCT_ID in place of the material token. You can also specify GET_MATERIAL_FROM_REAGENT:reagent:NONE in order to directly use the reagent's own material.

### Other tokens

#### Fuel

The FUEL token means that the reaction requires coke or charcoal to be performed. Fuel is not needed when the reaction is performed at a magma workshop (a magma kiln, magma smelter, or any custom building having \[NEEDS_MAGMA\]).

#### Skill

The skill tokens determine what skill the reaction requires and trains; also how quickly skill is gained, how quickly those skill gains raise attributes, and how skill level affects the quality of the reaction product.

|  |  |  |
|----|----|----|
| Token | Arguments | Description |
| SKILL | Skill token | (Optional) This identifies the skill required to carry out the reaction and is trained when the reaction is performed. Only one skill may be specified; if multiple skill tokens are defined only the last will be used. A reaction with no product will yield no experience gain. A reaction with no SKILL token will complete in a default amount of time. |
| SKILL_IP | Integer | (Optional, requires SKILL token) This adjusts the amount of skill gained each time the reaction is carried out. The default value is 30; higher values increase the amount of skill gain. |
| ATTRIBUTE_IP | Integer | (Optional, requires SKILL token) This adjusts the amount of attribute gain that skill gain from this reaction results in. The default value is 10; higher values increase the amount of attribute gain. |
| SKILL_ROLL_RANGE | Range / Multiplier | (Optional, requires SKILL token) This changes how much skill level affects the quality of the reaction product. The default is \[SKILL_ROLL_RANGE:11:5\]. The / range / is the base "die roll" and the / multiplier / determines how much the dwarf's skill can affect the reaction; the skill roll is random(range) + random((skill level \* multipler) / 2 + 1) + random((skill level \* multipler) / 2 + 1), where random(x) gives a random number from 0 to x-1, inclusive (which also means that the minimum for the range is 1). The higher result on the roll, the better. Both numbers can be lowered to make the skill check harder. For example, with the default values a dwarf who is proficient in a skill has a skill level of 5; their roll will be random(11)+random(13)+random(13), meaning this dwarf can roll anywhere from 0 to 34; similarly, unskilled dwarves can roll 0 to 10 while legendary+0 (skill 15) dwarves can roll 0 to 84. If this is changed to \[SKILL_ROLL_RANGE:1:8\], then instead a proficient dwarf will have random(1)+random(21)+random(21), giving a roll of 0 to 40, with unskilled dwarves always rolling 0 and legendary dwarves going all the way up to 120. / As a consequence, increasing the multiplier will always make legendary dwarves more effective, even if base roll is reduced to its minimum of 1, with the default going up to 84 for default and 90 for \[SKILL_ROLL_RANGE:1:6\]. |

#### Max multiplier

The \[MAX_MULTIPLIER:\\] token specifies how many times to do the reaction. This can be used to limit stacked reagent use to the specified quantity instead of the whole stack.

#### Automatic

The AUTOMATIC token means that the reaction will be queued automatically if the reaction reagents are all present.

This token only works with jobs performed at a kiln, smelter, tanner's shop, kitchen, or custom workshop, and standing orders allow you to limit which ones trigger; custom reactions performed at a quern, millstone, still or craftsdwarf's workshop cannot be made automatic.

#### Mode enabled

Some reaction tokens enable a reaction to be used by everyone in a certain mode. These tokens are not exclusive relations; for example, you can assign an [`[ADVENTURE_MODE_ENABLED]`](/index.php/Reaction#ADVENTURE_MODE_ENABLED "Reaction") reaction with a building to an entity and their citizens can then perform it at that building in fortress mode.

|  |  |
|----|----|
| Token | Description |
| ADVENTURE_MODE_ENABLED | Available to all adventurers, regardless of origin civilization. Required for adventurers to craft anything, as they do not use the recipes available to their origin civilization. |
| FORTRESS_MODE_ENABLED | Available to all fortress mode games. Without [`[PERMITTED_REACTION]`](/index.php/Entity_token#PERMITTED_REACTION "Entity token") on a specific entity, materials produced by it will not normally be added to their civilization resources. |
| WORLDGEN_ENABLED | If possible, reaction's output will be added to all civilizations during worldgen, allowing the civilization to trade or embark with them. |

#### Description

This feature is exclusive to Classic Mode, as no description window pops up when mousing over reactions in workshops in Premium.

The \[DESCRIPTION:\] token provides a text description of the reaction when it is highlighted in the building UI. Multiple DESCRIPTION tokens can be defined in a reaction, and each will appear on a new line. The pop-up box that contains the description is limited to 325 characters total. Alternatively, this token can reference a DESCRIPTION token in an existing tool definition by replacing *string* with USE_TOOL:; or an existing instrument definition with USE_INSTRUMENT:.

## Reaction classes and products

When you're doing things like tanning hides or brewing alcohol, having separate reactions for every single possible raw material is unwieldy and terrible. However, you can let the reaction itself ask the material for details and process them all with the same reaction. There are three types of tags to dictate this behavior.

### Reaction classes

The simplest token is the reaction class. If it is tacked on a material, a reaction can limit reagents to only those materials that have the specified arbitrary \[REACTION_CLASS:whatever\] identifier.

We want a reaction that smelts iron and flux into pig iron. However, there are a half-dozen different stones that count as flux. Instead of clogging up the smelter job menu with six nearly identical reactions that all take in either dolomite or limestone or marble for the same result, we use a reaction class.

      [REACTION:PIG_IRON_MAKING]
         [NAME:make pig iron bars]
         [BUILDING:SMELTER:NONE]
         [REAGENT:A:150:BAR:NO_SUBTYPE:METAL:IRON]
         [REAGENT:B:1:BOULDER:NO_SUBTYPE:NONE:NONE][REACTION_CLASS:FLUX]
         [REAGENT:C:150:BAR:NO_SUBTYPE:COAL:NO_MATGLOSS]
         [PRODUCT:100:1:BAR:NO_SUBTYPE:METAL:PIG_IRON][PRODUCT_DIMENSION:150]
         [FUEL]
         [SKILL:SMELT]

Note how reagent B asks for "NONE:NONE" as its material. This means "boulders of any kind as long as they have the reaction class named FLUX". Stuff like calcite, here:

      [INORGANIC:CALCITE]
         [USE_MATERIAL_TEMPLATE:STONE_TEMPLATE]
         [STATE_NAME_ADJ:ALL_SOLID:calcite][DISPLAY_COLOR:7:7:1][TILE:'"']
         [REACTION_CLASS:FLUX]
         [ENVIRONMENT_SPEC:LIMESTONE:CLUSTER_SMALL:100]
         [ENVIRONMENT_SPEC:MARBLE:CLUSTER_SMALL:100]
         [MATERIAL_VALUE:2]
         [IS_STONE]
         [MELTING_POINT:12902]
         [SOLID_DENSITY:2930]

The label itself can be absolutely anything. It's only used to find a match between the material and the reaction. Note that some reaction classes have special meanings to the game itself—notably, the site finder knows that "FLUX" should be connected to the "Flux stone" filter.

### Material reaction products

But what if it's not all the same what materials the members of the reaction class put out? If a tanner starts working on a bear pelt, a horse hide, some dragon scales and a section of human skin, surely they all can't produce generic boot leather! No, the reaction must get the chance to ask the "reaction class" what the reagent should turn out as. We will declare a material reaction product.

      [REACTION:TAN_A_HIDE]
         [NAME:tan a hide]
         [BUILDING:TANNER:CUSTOM_T]
            [REAGENT:flaps of skin:1:NONE:NONE:NONE:NONE][USE_BODY_COMPONENT][UNROTTEN]
               [HAS_MATERIAL_REACTION_PRODUCT:TAN_MAT]
            [PRODUCT:100:1:SKIN_TANNED:NONE:GET_MATERIAL_FROM_REAGENT:flaps of skin:TAN_MAT]
         [SKILL:TANNER]
         [AUTOMATIC]

Where you'd usually have some fresh bodypart with the TAN_MAT reaction class produce some generic SKIN_TANNED, this goes further. Instead of declaring a material, the spool of pattern-ready tailoring leather (SKIN_TANNED) now comes out as whatever the skin flaps' material reaction product (named TAN_MAT) says in the material's definition (GET_MATERIAL_FROM_REAGENT). And what does it say?

      [MATERIAL_TEMPLATE:SKIN_TEMPLATE]
            [STATE_COLOR:ALL_SOLID:GRAY]
            [STATE_NAME:ALL_SOLID:skin]
            [STATE_ADJ:ALL_SOLID:skin]
            ...
            [ABSORPTION:100]
            [MATERIAL_REACTION_PRODUCT:TAN_MAT:LOCAL_CREATURE_MAT:LEATHER]
            [IMPLIES_ANIMAL_KILL]
            [ROTS]

It says that the caller of the TAN_MAT hook always comes out as the LEATHER of whatever creature the skin has been peeled off of (LOCAL_CREATURE_MAT). For example, skin taken from a butchered dog would be turned into dog leather. Change the SKIN_TEMPLATE MATERIAL_REACTION_PRODUCT to TAN_MAT:INORGANIC:GOLD instead and your tanner turns into Midas. Use your imagination.

If the item you're creating should be made of the *same* material as the raw material you're using (e.g. if you're carving a log into a training spear), you can specify "NONE" instead of the MATERIAL_REACTION_PRODUCT code:

      [REACTION:MAKE WOODEN TRAINING SPEAR]
         [NAME:make wooden training spear]
         [BUILDING:CARPENTER:NONE]
         [REAGENT:log:1:WOOD:NONE:NONE:NONE][ANY_PLANT_MATERIAL]
         [PRODUCT:100:1:WEAPON:ITEM_WEAPON_SPEAR_TRAINING:GET_MATERIAL_FROM_REAGENT:log:NONE]
         [SKILL:CARPENTRY]

As with reaction classes, some MATERIAL_REACTION_PRODUCT identifiers have special meanings to the game itself - notably, the site finder knows that "FIRED_MAT" should be connected to the "Clay" filter, and "CHEESE_MAT" is used when making cheese from milk.

### Item reaction products

Item reaction products are an even more powerful form of the above. Where material reaction products can only affect what type of stuff the predestined end product is made of, item reaction products can decide the entire end result ahead of time. Item AND material.

Let's assume for a moment that we're completely tired of leather earrings and hair crowns. We want a crafting reaction that takes cloth and only produces things that make sense.

         [REACTION:TAILOR_THE_BEST_THING]
               [NAME:weave something that makes sense]
               [BUILDING:CRAFTSMAN]
               [REAGENT:woven fabric:1:CLOTH:NONE:NONE:NONE]
                  [HAS_ITEM_REACTION_PRODUCT:BEST_OPTION]
               [PRODUCT:100:1:GET_ITEM_DATA_FROM_REAGENT:woven fabric:BEST_OPTION]
               [SKILL:CLOTHIER]

Now we need to come up with the counterpart tags in the materials. Hmmm... cotton is thin and soft, so it makes pretty good undergarments. An undershirt, maybe?

            [PLANT:COTTON] Gossypium hirsutum / sp.
                     [NAME:cotton plant][NAME_PLURAL:cotton plants][ADJ:cotton plant]
                     [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
                     [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
                     [DRY][BIOME:ANY_TROPICAL]
                     [VALUE:2]
                     ...
                     [USE_MATERIAL_TEMPLATE:THREAD:THREAD_PLANT_TEMPLATE]
                        [MATERIAL_VALUE:2]
                        [ITEM_REACTION_PRODUCT:BEST_OPTION:ARMOR:ITEM_ARMOR_TUNIC:LOCAL_PLANT_MAT:THREAD]
                     ...

Then jute fabric. Isn't that burlap? And what's about the only thing they make from burlap?

            [PLANT:JUTE] Corchorus capsularis / Corchorus olitorius
                     [NAME:jute plant][NAME_PLURAL:jute plants][ADJ:jute plant]
                     [USE_MATERIAL_TEMPLATE:STRUCTURAL:STRUCTURAL_PLANT_TEMPLATE]
                     [BASIC_MAT:LOCAL_PLANT_MAT:STRUCTURAL]
                     [DRY][BIOME:ANY_TROPICAL]
                     [VALUE:2]
                     ...
                     [USE_MATERIAL_TEMPLATE:THREAD:THREAD_PLANT_TEMPLATE]
                        [MATERIAL_VALUE:2]
                        [ITEM_REACTION_PRODUCT:BEST_OPTION:BAG:NONE:LOCAL_PLANT_MAT:THREAD]
                     ...

Sacks, of course! Wait, how about silk?

            [CREATURE:SPIDER_CAVE]
                     [DESCRIPTION:A tiny underground bug, sought after for its thread.]
                     [NAME:cave spider:cave spiders:cave spider]
                     ...
                     [USE_MATERIAL_TEMPLATE:SILK:SILK_TEMPLATE]
                        [ITEM_REACTION_PRODUCT:BEST_OPTION:PANTS:ITEM_PANTS_THONG:LOCAL_CREATURE_MAT:SILK]
                     ...

This goes on for as long as you let it. The ITEM_REACTION_PRODUCT declares the identifier and then the item and material with subtypes, just like a normal reaction's product line would.

Do note that MATERIAL_REACTION_PRODUCT and ITEM_REACTION_PRODUCT use the same IDs, so you cannot have both a material and item reaction product of the same name. Also, though you cannot use GET_ITEM_DATA_FROM_REAGENT with a MATERIAL_REACTION_PRODUCT (there'd be no item type information), you *can* use GET_MATERIAL_FROM_REAGENT on an ITEM_REACTION_PRODUCT (in case you want to force your own item type).

## Reactions and world generation

There are several things to keep in mind when you're adding reactions to a game that already exists.

- Most entity changes require a regen, but adding PERMITTED_REACTION tokens for reactions that existed at the time of world generation to the entity file in the save directory do not.
- Adding reactions to the raws in a save directory requires you to regen the world.
- You can alter an existing reaction in any way you like without regenning the world, so long as you don't alter the reaction identifier.

## Full token list

For the sake of convenience and readability, this is a complete compilation of the previously listed reaction tokens in alphabetical order:

|  |  |  |  |
|----|----|----|----|
| Token | Arguments | Type | Description |
|  ADVENTURE_MODE_ENABLED |  |  | This version of the reaction can be used by the wanderers of Adventure Mode without needing to also give the dwarves at home in a fortress access to it. When using this token, it will be allowed for adventurers of any race, without editing entity files. This token does not prevent Fortress Mode usage if assigned to a workshop and the civilization has access. |
|  FORTRESS_MODE_ENABLEDvLua beta |  |  | This reaction can be accessed when playing as any civilization in Fortress mode, regardless of [`[PERMITTED_REACTION]`](/index.php/Entity_token#PERMITTED_REACTION "Entity token"). Particularly useful for compatibility or Lua scripting. |
|  WORLDGEN_ENABLEDvLua beta |  |  | Adds the materials provided by the reaction to all civilizations, regardless of [`[PERMITTED_REACTION]`](/index.php/Entity_token#PERMITTED_REACTION "Entity token"). |
|  ANY_BONE_MATERIAL |  | Reagent modifier | Reagent material must have the \[BONE\] token. |
|  ANY_GEM_MATERIAL |  | Reagent modifier | Reagent material must have the \[IS_GEM\] token. |
|  ANY_HORN_MATERIAL |  | Reagent modifier | Reagent material must have the \[HORN\] token. |
|  ANY_LEATHER_MATERIAL |  | Reagent modifier | Reagent material must have the \[LEATHER\] token. |
|  ANY_PEARL_MATERIAL |  | Reagent modifier | Reagent material must have the \[PEARL\] token. |
|  ANY_PLANT_MATERIAL |  | Reagent modifier | Reagent material must be subordinate to a PLANT object. |
|  ANY_SHELL_MATERIAL |  | Reagent modifier | Reagent material must have the \[SHELL\] token. |
|  ANY_SILK_MATERIAL |  | Reagent modifier | Reagent material must have the \[SILK\] token. |
|  ANY_SOAP_MATERIAL |  | Reagent modifier | Reagent material must have the \[SOAP\] token. |
|  ANY_STONE_MATERIAL |  | Reagent modifier | Reagent material must have the \[IS_STONE\] token. |
|  ANY_STRAND_TISSUE |  | Reagent modifier | Reagent is made of a tissue having \[TISSUE_SHAPE:STRANDS\], intended for matching hair and wool. Must be used with \[USE_BODY_COMPONENT\]. |
|  ANY_TOOTH_MATERIAL |  | Reagent modifier | Reagent material must have the \[TOOTH\] token. |
|  ANY_WOOD_MATERIAL |  | Reagent modifier | Reagent material must have the \[WOOD\] token. |
|  ANY_YARN_MATERIAL |  | Reagent modifier | Reagent material must have the \[YARN\] token. |
|  ATTRIBUTE_IP | Integer | Skill modifier | Amount of attribute gain given per skill improvement. Default is 10. |
|  AUTOMATIC |  |  | The reaction will be queued automatically if the reaction reagents are all present. |
|  BAG (Deprecated) |  | Reagent modifier | Reagent has to be a bag. Intended to be used with an item type of BOX, to prevent chests, coffers, and other containers from being used instead. Deprecated as of Version 0.50.01 in favor of BAG:NONE item token. |
|  BUILDING | Building name / In-building reaction hotkey |  | Sets the building that the reaction will be performed in, and the button used to queue the reaction once that building's menu is accessed in-game. |
|  BUILDMAT |  | Reagent modifier | Reagent is able to be used to build structures (Boulders, Wood, Blocks, Bars). |
|  CAN_USE_ARTIFACT |  | Reagent modifier | Reagent can be an Artifact. Using \[PRESERVE_REAGENT\] with this is strongly advised. |
|  CAN_USE_HOSPITAL_RESERVED |  | Reagent modifier | Allows the reagent to be an item that is otherwise reserved for use by a hospital. |
|  CAN_USE_LOCATION_RESERVED |  | Reagent modifier | Allows the reagent to be an item that is otherwise reserved for use by a location. |
|  CATEGORY | Category ID |  | Puts the reaction in a category. Categories are custom submenus for reaction menus. The category ID is a unique identifier for the category. It is only used in the raws, and will not appear in the game. / If you're defining multiple categories within the same reaction - for example, if you intend the reaction to be nested two deep, and haven't yet defined the super-category - the / last / CATEGORY token within the reaction definition is the one that the reaction will appear in. |
|  CATEGORY_NAME | String | Category | The name of the category as displayed in-game. |
|  CATEGORY_DESCRIPTION | String | Category | If present, when the category is highlighted in a building menu, this string will be displayed in the Helpful Hint box. |
|  CATEGORY_PARENT | Category ID | Category | If present, this category will be a submenu of the indicated category, rather than a submenu of the reaction's building. |
|  CATEGORY_KEY | Hotkey | Category | If present, this category can be selected from its parent menu (whether a building or a parent category) using the given hotkey while playing in Classic mode. |
|  CONTAINS | Reagent name | Reagent modifier | Reagent is a container that holds the specified reagent. |
|  CONTAINS_LYE (Deprecated) |  | Reagent modifier | If the reagent is a container, it must contain LYE. No longer used - instead, use one reagent for the LYE itself and another reagent with \[CONTAINS:lye_reagent\]. |
|  DESCRIPTION | String |  | A description of the reaction that appears when it is highlighted in the building UI. *String* can also be replaced with a reference to existing DESCRIPTION tokens in tools (using USE_TOOL:) or musical instruments (using USE_TOOL:). |
|  DOES_NOT_ABSORB |  | Reagent modifier | Reagent material must have \[ABSORPTION:0\]. |
|  DOES_NOT_DETERMINE_PRODUCT_AMOUNT |  | Reagent modifier | Performing a reaction with large stacks of inputs can allow multiple sets of outputs to be produced. Setting this flag causes the reagent to be ignored in this process - for example, with the reaction "1 plant + 1 barrel -\> 5 alcohol (into barrel)", using this on the barrel allows the reaction to be performed as "5 plant + 1 barrel -\> 25 alcohol" instead of "5 plant + 5 barrel -\> 25 alcohol". |
|  EMPTY |  | Reagent modifier | If the reagent is a container, it must be empty. |
|  FIRE_BUILD_SAFE |  | Reagent modifier | Reagent must be considered fire-safe (stable temperature below 11000 °U  ) - i.e. not wood, and not coal. |
|  FORCE_EDGE |  | Product modifier | Product is given a sharp edge. Used for knapping. |
|  FOOD_STORAGE_CONTAINER |  | Reagent modifier | Reagent must be a barrel or any non-absorbing tool with \[TOOL_USE:FOOD_STORAGE\]. |
|  GROWN_NOT_CRAFTED |  | Reagent modifier | Reagent must be a GROWN wooden item, such as a "grown wooden shield" from an Elven caravan. |
|  FUEL |  |  | Requires that the reaction either use up a unit of coal or charcoal or else be performed at a magma workshop. |
|  GLASS_MATERIAL |  | Reagent modifier | Reagent material has \[IS_GLASS\]. |
|  HAS_EDGE |  | Reagent modifier | Reagent must be sharpened (used for carving). |
|  HAS_ITEM_REACTION_PRODUCT | PRODUCT_ID (custom) | Reagent modifier | Similar to HAS_MATERIAL_REACTION_PRODUCT, but requires the reagents material to have a matching ITEM_REACTION_PRODUCT entry. |
|  HAS_MATERIAL_REACTION_PRODUCT | PRODUCT_ID (custom) | Reagent modifier | Similar to REACTION_CLASS, but requires the reagents material to have a matching MATERIAL_REACTION_PRODUCT entry. Intended for reactions which transform one class of material into another, such as skin-\>leather and fat-\>tallow. |
|  HAS_TOOL_USE | TOOL_USE value | Reagent modifier | Reagent must be a tool with the specific TOOL_USE value. The reagents item type must be TOOL:NONE for this to make any sense. |
|  HAS_WRITING_IMPROVEMENT |  | Reagent modifier | Reagent must contain writing. |
|  IMPROVEMENT | Probability / Reagent name / Improvement type / Material Token |  | Applies an improvement to the named reagent. Only meaningful if said reagent has \[PRESERVE_REAGENT\]. Improvement types include BANDS, COVERED, GLAZED, PAGES, RINGS_HANGING, and SPIKES |
|  IS_CRAFTED_ARTIFACT\[Verify\] |  | Reagent modifier | Reagent item must be an artifact. |
|  IS_DIVINE_MATERIAL |  | Reagent modifier | Reagent material must have the \[DIVINE\] token. |

---
*Parte 1 de 2 de «Reaction». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Reaction*
