# Raw file

> Fonte: [Raw file](https://dwarffortresswiki.org/index.php/Raw_file) — Dwarf Fortress Wiki (GFDL/MIT)

**Raw files** are text files found in the **raw/objects/** subdirectory of *Dwarf Fortress* (used for world generation), as well as inside the saved game folder (**data/save/\/raw/objects/**) for already generated worlds. These files can be looked through to discover various specifics of game items, materials, and creatures, and can be changed to alter how the game behaves. They are sometimes referred to by players as just "the raws".

The **raw/graphics** subfolder of *Dwarf Fortress* is used to store user-customizable graphics sets. The **raw/interaction examples** folder contains examples useful for modding but completely ignored by *Dwarf Fortress*.

*Dwarf Fortress* is not currently an open-source program, so most modding of the game is limited to altering the raws or memory hacking.

Duplicating the raw files can cause strange, difficult-to-diagnose problems, and even crashes in some cases.

## Syntax of raw files

`filename`\

`[OBJECT:TYPE]`\

`[TYPE:ID] `\
``

ID is a unique identificator for your type to use (i.e. \[CREATURE:DOG\], ID=DOG or \[ITEM:ITEM_WEAPON_SWORD\], ID=ITEM_WEAPON_SWORD).

### Types of content

- BODY — body parts and structures.
- BODY_DETAIL_PLAN — similar to CREATURE_VARIATION, but used for defining tokens related to body parts (specifically materials, tissues, the assignment thereof, and body part positions, relative sizes, etc.)
- BUILDING — custom workshops and smelters.
- CREATURE — creatures.
- CREATURE_VARIATION — variations that can be applied to creatures (e.g., making them giants, or anthropomorphic). Technically a series of tokens that are added to or removed from the creature (essentially a set of templated changes).
- DESCRIPTOR_COLOR (tag is COLOR) — named colors for use with DESCRIPTOR_PATTERN objects (other purposes unknown)
- DESCRIPTOR_PATTERN (tag is COLOR_PATTERN) — patterns with color combinations for use with creatures.
- DESCRIPTOR_SHAPE (tag is SHAPE) — shapes with descriptions and variations, used for engravings.
- ENTITY — civilization types, with assigned race, language, culture, ethics, and social structure.
- GRAPHICS — graphic tiles for creatures. These are not found inside the raw/objects folder.
- INTERACTION — interaction definitions.
- INORGANIC — inorganic material definitions.
- ITEM — items ranging from ammunition to food types, has secondary types for the purposes of \[TYPE:ID\].
  - ITEM_AMMO — ammunition for ranged weapons.
  - ITEM_ARMOR — body clothing, including armor.
  - ITEM_FOOD — prepared food definitions.
  - ITEM_GLOVES — hand clothing, including armor.
  - ITEM_HELM — head clothing, including armor.
  - ITEM_INSTRUMENT — instrument definitions.
  - ITEM_PANTS — lower body clothing, including armor.
  - ITEM_SHIELD — shields.
  - ITEM_SHOES — foot clothing, including armor.
  - ITEM_SIEGEAMMO — ammunition for siege weapons that ballistae fire.
  - ITEM_TOOL — multi-purpose items that can serve as a weapon, food storage container, etc.
  - ITEM_TOY — toy definitions.
  - ITEM_TRAPCOMP — components that can be used in weapon traps (two special tags define trapcomps that can be used in other constructions: IS_SCREW and IS_SPIKE).
  - ITEM_WEAPON — weapons that are used by soldiers, as well as digging tools.
- LANGUAGE — word definitions for the languages used by ENTITY objects.
  - Entries beginning with \[SYMBOL:ID\] sort words into symbolic/poetic groups to be referenced by ENTITY preferences.
  - Entries beginning with \[WORD:ID\] define words and their alternate forms (in English).
- MATERIAL_TEMPLATE — definitions of information common to groups of materials (referenced all over the place).
- PLANT — definitions of plants, their materials, and their derivatives.
- REACTION — reactions/custom workshop jobs (turn items into other items through dwarven or adventurer effort).
- TISSUE_TEMPLATE — defines templated tissues for use with BODY_DETAIL_PLAN objects or in creatures.

Usually empty lines are used to divide different types of structures like the file name and \[OBJECT:\] or different entries, however everything which is not a token besides the 1st string (which is the filename) is understood as comments and is not considered.

The tokens are enclosed in square brackets (\[TOKEN:VALUES\]).

When a world is generated, the raw files are copied from \/raw/ to \/data/save/REGION/raw/. It is currently unknown how much these can then be changed without breaking the save.

A list of tokens can be seen at :Category:Tokens.

## Parsing

The order that *Dwarf Fortress* parses raw files in is determined by the first line of the raw file (*not* necessarily the filename). This parsing order is important for certain tags, such as \[COPY_TAGS_FROM\], but not for most other tags.

The names of raw files are completely irrelevant - when you create a new creature, you can put it in any file you want (or even in a brand-new file) and the game won't behave any differently. You can even rename all of the existing raw files and the game still won't care (as long as you generate a new world first, of course).

The load order (recorded by logging DF 0.44.09 file activity in Windows 10) follows the following pattern:

`language_*`\
`descriptor_shape_*`\
`descriptor_color_*`\
`descriptor_pattern_*`\
`material_template_*`\
`inorganic_*`\
`plant_*`\
`tissue_template_*`\
`item_*`\
`building_*`\
`b_detail_plan_*`\
`body_*`\
`c_variation_*`\
`creature_*`\
`entity_*`\
`reaction_*`\
`interaction_*`

Therefore, vanilla DF 0.44.09 loads RAW files in the following order:

`language_DWARF.txt`\
`language_ELF.txt`\
`language_GOBLIN.txt`\
`language_HUMAN.txt`\
`language_SYM.txt`\
`language_words.txt`\
`descriptor_shape_standard.txt`\
`descriptor_color_standard.txt`\
`descriptor_pattern_iris_eye.txt`\
`descriptor_pattern_pupil_eye.txt`\
`descriptor_pattern_special.txt`\
`material_template_default.txt`\
`inorganic_metal.txt`\
`inorganic_other.txt`\
`inorganic_stone_gem.txt`\
`inorganic_stone_layer.txt`\
`inorganic_stone_mineral.txt`\
`inorganic_stone_soil.txt`\
`plant_crops.txt`\
`plant_garden.txt`\
`plant_grasses.txt`\
`plant_new_trees.txt`\
`plant_standard.txt`\
`tissue_template_default.txt`\
`item_ammo.txt`\
`item_armor.txt`\
`item_food.txt`\
`item_gloves.txt`\
`item_helm.txt`\
`item_pants.txt`\
`item_shield.txt`\
`item_shoes.txt`\
`item_siegeammo.txt`\
`item_tool.txt`\
`item_toy.txt`\
`item_trapcomp.txt`\
`item_weapon.txt`\
`building_custom.txt`\
`b_detail_plan_default.txt`\
`body_default.txt`\
`body_rcp.txt`\
`c_variation_default.txt`\
`creature_amphibians.txt`\
`creature_annelids.txt`\
`creature_birds.txt`\
`creature_birds_new.txt`\
`creature_bug_slug_new.txt`\
`creature_desert_new.txt`\
`creature_domestic.txt`\
`creature_equipment.txt`\
`creature_fanciful.txt`\
`creature_insects.txt`\
`creature_large_mountain.txt`\
`creature_large_ocean.txt`\
`creature_large_riverlake.txt`\
`creature_large_temperate.txt`\
`creature_large_tropical.txt`\
`creature_large_tundra.txt`\
`creature_mountain_new.txt`\
`creature_next_underground.txt`\
`creature_ocean_new.txt`\
`creature_other.txt`\
`creature_reptiles.txt`\
`creature_riverlakepool_new.txt`\
`creature_small_mammals.txt`\
`creature_small_mammal_new.txt`\
`creature_small_ocean.txt`\
`creature_small_riverlake.txt`\
`creature_standard.txt`\
`creature_subterranean.txt`\
`creature_temperate_new.txt`\
`creature_tropical_new.txt`\
`creature_tundra_taiga_new.txt`\
`entity_default.txt`\
`reaction_adv_carpenter.txt`\
`reaction_other.txt`\
`reaction_smelter.txt`\
`interaction_standard.txt`

## Required objects

While most of the raw files are replaceable or removable, some contain raw objects that are used by procedurally generated creatures (such as FBs and experiments). Raws with the following IDs must exist, to support those creatures. The file names are where said objects exist by default, but are not important on their own, as long as the objects exist somewhere in the raws the game may use them. This list was compiled by examining the code that emits the various "Cannot generate random creatures -- missing \*" error messages.

material_template_default.txt:

`SKIN_TEMPLATE`\
`FAT_TEMPLATE`\
`MUSCLE_TEMPLATE`\
`SINEW_TEMPLATE`\
`BONE_TEMPLATE`\
`CARTILAGE_TEMPLATE`\
`HAIR_TEMPLATE`\
`FEATHER_TEMPLATE`\
`SCALE_TEMPLATE`\
`NAIL_TEMPLATE`\
`TOOTH_TEMPLATE`\
`EYE_TEMPLATE`\
`NERVE_TEMPLATE`\
`BRAIN_TEMPLATE`\
`LUNG_TEMPLATE`\
`HEART_TEMPLATE`\
`LIVER_TEMPLATE`\
`GUT_TEMPLATE`\
`STOMACH_TEMPLATE`\
`PANCREAS_TEMPLATE`\
`SPLEEN_TEMPLATE`\
`KIDNEY_TEMPLATE`\
`LEATHER_TEMPLATE`\
`HORN_TEMPLATE`\
`PEARL_TEMPLATE`\
`SILK_TEMPLATE`\
`BLOOD_TEMPLATE`\
`ICHOR_TEMPLATE`\
`GOO_TEMPLATE`\
`SLIME_TEMPLATE`\
`SHELL_TEMPLATE`\
`SOAP_TEMPLATE`\
`TALLOW_TEMPLATE`\
`CHITIN_TEMPLATE`\
`MILK_TEMPLATE`\
`CREATURE_CHEESE_TEMPLATE`\
`STRUCTURAL_PLANT_TEMPLATE`\
`SEED_TEMPLATE`\
`LEAF_TEMPLATE`\
`THREAD_PLANT_TEMPLATE`\
`PLANT_ALCOHOL_TEMPLATE`\
`PLANT_POWDER_TEMPLATE`\
`PLANT_EXTRACT_TEMPLATE`\
`CREATURE_EXTRACT_TEMPLATE`\
`FLAME_TEMPLATE`

tissue_template_default.txt:

`SKIN_TEMPLATE`\
`FAT_TEMPLATE`\
`MUSCLE_TEMPLATE`\
`BONE_TEMPLATE`\
`SHELL_TEMPLATE`\
`HORN_TEMPLATE`\
`CARTILAGE_TEMPLATE`\
`HAIR_TEMPLATE`\
`CHEEK_WHISKERS_TEMPLATE`\
`CHIN_WHISKERS_TEMPLATE`\
`MOUSTACHE_TEMPLATE`\
`SIDEBURNS_TEMPLATE`\
`EYEBROW_TEMPLATE`\
`EYELASH_TEMPLATE`\
`FEATHER_TEMPLATE`\
`SCALE_TEMPLATE`\
`NAIL_TEMPLATE`\
`CLAW_TEMPLATE`\
`TALON_TEMPLATE`\
`TOOTH_TEMPLATE`\
`EYE_TEMPLATE`\
`NERVE_TEMPLATE`\
`BRAIN_TEMPLATE`\
`LUNG_TEMPLATE`\
`HEART_TEMPLATE`\
`LIVER_TEMPLATE`\
`GUT_TEMPLATE`\
`STOMACH_TEMPLATE`\
`PANCREAS_TEMPLATE`\
`SPLEEN_TEMPLATE`\
`KIDNEY_TEMPLATE`\
`FLAME_TEMPLATE`

b_detail_plan_default.txt:

`STANDARD_MATERIALS`\
`STANDARD_TISSUES`\
`CHITIN_MATERIALS`\
`CHITIN_TISSUES`\
`FACIAL_HAIR_TISSUES`\
`HEAD_HAIR_TISSUE_LAYERS`\
`FACIAL_HAIR_TISSUE_LAYERS`\
`BODY_HAIR_TISSUE_LAYERS`\
`BODY_FEATHER_TISSUE_LAYERS`\
`VERTEBRATE_TISSUE_LAYERS`\
`EXOSKELETON_TISSUE_LAYERS`\
`STANDARD_HEAD_POSITIONS`\
`HUMANOID_HEAD_POSITIONS`\
`HUMANOID_RIBCAGE_POSITIONS`\
`SHELL_POSITIONS`\
`HUMANOID_RELSIZES`

c_variation_default.txt:

`STANDARD_BIPED_GAITS`\
`STANDARD_QUADRUPED_GAITS`\
`STANDARD_WALKING_GAITS`\
`STANDARD_CLIMBING_GAITS`\
`STANDARD_SWIMMING_GAITS`\
`STANDARD_CRAWLING_GAITS`\
`STANDARD_FLYING_GAITS`\
`STANDARD_WALK_CRAWL_GAITS`

body_rcp.txt:

`RCP_BASIC_BODY`\
`RCP_BASIC_BODY_STANCE`\
`RCP_BASIC_BODY_STANCE_WITH_HEAD_FLAG`\
`RCP_UPPER_BODY`\
`RCP_LOWER_BODY`\
`RCP_THORAX`\
`RCP_ABDOMEN`\
`RCP_CEPHALOTHORAX`\
`RCP_HEAD`\
`RCP_NECK`\
`RCP_TWO_PART_ARMS`\
`RCP_PINCERS`\
`RCP_CLAW_ARMS`\
`RCP_FIRST_SIMPLE_LEGS`\
`RCP_FIRST_SIMPLE_LEGS_GRASP`\
`RCP_SECOND_SIMPLE_LEGS`\
`RCP_THIRD_SIMPLE_LEGS`\
`RCP_FOURTH_SIMPLE_LEGS`\
`RCP_FIFTH_SIMPLE_LEGS`\
`RCP_SIMPLE_FRONT_LEGS`\
`RCP_SIMPLE_FRONT_LEGS_GRASP`\
`RCP_SIMPLE_REAR_LEGS`\
`RCP_TWO_PART_LEGS`\
`RCP_FRONT_FLIPPER`\
`RCP_REAR_FLIPPER`\
`RCP_TWO_FLIGHTLESS_WINGS`\
`RCP_TWO_WINGS`\
`RCP_TAIL`\
`RCP_2_TAILS`\
`RCP_3_TAILS`\
`RCP_TAIL_STINGER`\
`RCP_LOWER_BODY_STINGER`\
`RCP_PROBOSCIS`\
`RCP_TRUNK`\
`RCP_SHELL`\
`RCP_ANTENNAE`\
`RCP_1_HEAD_HORN`\
`RCP_2_HEAD_HORNS`\
`RCP_3_HEAD_HORNS`\
`RCP_4_HEAD_HORNS`\
`RCP_LARGE_MANDIBLES`\
`RCP_5_FINGERS`\
`RCP_4_FINGERS`\
`RCP_3_FINGERS`\
`RCP_2_FINGERS`\
`RCP_5_TOES`\
`RCP_4_TOES`\
`RCP_3_TOES`\
`RCP_2_TOES`\
`RCP_5_FRONT_TOES`\
`RCP_4_FRONT_TOES`\
`RCP_3_FRONT_TOES`\
`RCP_2_FRONT_TOES`\
`RCP_5_REAR_TOES`\
`RCP_4_REAR_TOES`\
`RCP_3_REAR_TOES`\
`RCP_2_REAR_TOES`\
`RCP_1_EYE`\
`RCP_2_EYES`\
`RCP_3_EYES`\
`RCP_BEAK`\
`RCP_NOSE`\
`RCP_CHEEKS`\
`RCP_LUNGS`\
`RCP_HEART`\
`RCP_GUTS`\
`RCP_THROAT`\
`RCP_SPINE`\
`RCP_UPPER_SPINE`\
`RCP_BRAIN`\
`RCP_SKULL`\
`RCP_MOUTH`\
`RCP_TEETH`\
`RCP_RIBS`\
`RCP_RIBS_EXTERNAL`\
`RCP_LIPS`\
`RCP_1_EYELID`\
`RCP_2_EYELIDS`\
`RCP_3_EYELIDS`\
`RCP_GLOSS_HOOF`\
`RCP_GLOSS_PAW`\
`RCP_5_FRONT_FINGERS*`\
`RCP_4_FRONT_FINGERS*`\
`RCP_3_FRONT_FINGERS*`\
`RCP_2_FRONT_FINGERS*`\
`RCP_TONGUE*`

\* - The game does not confirm the presence of these objects, but it *will* still attempt to use them (and fail if they are missing)

The objects RCP_FORKED_TONGUE, RCP_BILL, and RCP_2_HEAD_ANTLERS are currently **not** used by the game and can be safely removed.

## Examples

- Creature examples
- Interaction examples
- Reaction examples
- Syndrome examples
