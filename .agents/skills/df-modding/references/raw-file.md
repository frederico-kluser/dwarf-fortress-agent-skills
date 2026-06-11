# Raw file

> Fonte: [Raw file](https://dwarffortresswiki.org/index.php/Raw_file) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

xTATTEREDx  · +FINE+  · \*SUPERIOR\*  · ≡EXCEPTIONAL≡  · ☼MASTERWORK☼

**Raw files** are text files found in the `\data\vanilla\` subdirectory of *Dwarf Fortress* (used for world generation), as well as inside the saved game folder for already generated worlds. These files can be looked through to discover various specifics of game items, materials, and creatures, and can be changed to alter how the game behaves. They are sometimes referred to by players as just "the raws".

The `data\vanilla\*_graphics` subfolders are used to store user-customizable graphics sets. The `data\vanilla\``interaction examples` folder contains examples useful for modding but completely ignored by *Dwarf Fortress*.

*Dwarf Fortress* is not currently an open-source program, so most modding of the game is limited to altering the raws or memory hacking.

Duplicating the raw files can cause strange, difficult-to-diagnose problems, and even crashes in some cases.

## Syntax of raw files

    filename

    [OBJECT:TYPE]

    [TYPE:ID]

*filename* is a copy of the raw file name, minus the .txt extension; every raw must begin with this. It must begin with a certain prefix depending on the TYPE (see below).

*TYPE* is a keyword that instructs the game what sort of objects are being defined in the raw (see below). An individual raw file can (and must) have only one OBJECT:TYPE.

*ID* is a unique identificator for your type to use (i.e. \[CREATURE:DOG\], ID=DOG or \[ITEM:ITEM_WEAPON_SWORD\], ID=ITEM_WEAPON_SWORD).

### Types of content

- BODY — body parts and structures; filename prefix `body_`.
- BODY_DETAIL_PLAN — similar to CREATURE_VARIATION, but used for defining tokens related to body parts (specifically materials, tissues, the assignment thereof, and body part positions, relative sizes, etc.); filename prefix `b_detail_plan_`.
- BUILDING — custom workshops and smelters; filename prefix `building_`.
- CREATURE — creatures; filename prefix `creature_`.
- CREATURE_VARIATION — variations that can be applied to creatures (e.g., making them giants, or anthropomorphic). Technically a series of tokens that are added to or removed from the creature (essentially a set of templated changes); filename prefix `c_variation_`.
- DESCRIPTOR_COLOR (tag is COLOR) — named colors for use with DESCRIPTOR_PATTERN objects (other purposes unknown); filename prefix `descriptor_color_`.
- DESCRIPTOR_PATTERN (tag is COLOR_PATTERN) — patterns with color combinations for use with creatures; filename prefix `descriptor_pattern_`.
- DESCRIPTOR_SHAPE (tag is SHAPE) — shapes with descriptions and variations, used for engravings; filename prefix `descriptor_shape_`.
- ENTITY — civilization types, with assigned race, language, culture, ethics, and social structure; filename prefix `entity_`.
- GRAPHICS — graphic tiles for creatures. These are not found inside the raw/objects folder; filename prefix `graphics_`.
- INTERACTION — interaction definitions; filename prefix `interaction_`.
- INORGANIC — inorganic material definitions; filename prefix `inorganic_`.
- ITEM — items ranging from ammunition to food types, has secondary types for the purposes of \[TYPE:ID\]; filename prefix `item_`.
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
- LANGUAGE — word definitions for the languages used by ENTITY objects; filename prefix `language_`.
  - Entries beginning with \[SYMBOL:ID\] sort words into symbolic/poetic groups to be referenced by ENTITY preferences.
  - Entries beginning with \[WORD:ID\] define words and their alternate forms (in English).
- MATERIAL_TEMPLATE — definitions of information common to groups of materials (referenced all over the place); filename prefix `material_template_`.
- MUSIC — assigns music files to background and event music cues, modding currently very limited; filename prefix `music_`.
- PALETTE — defines a color palette and associates those colors to an image file containing color swatches; filename prefix `palette_`.
- PLANT — definitions of plants, their materials, and their derivatives; filename prefix `plant_`.
- REACTION — reactions/custom workshop jobs (turn items into other items through dwarven or adventurer effort); filename prefix `reaction_`.
- SOUND — associates sound files with in-game event cues; filename prefix `sound_`.
- TEXT_SET — conversation text, mostly used in Adventure mode; ; filename prefix `text_`. Example: text_dwarf.txt
- TILE_PAGE — assigns IDs to image files and establishes their parameters for use in GRAPHICS raws; filename prefix `tile_page_`.
- TISSUE_TEMPLATE — defines templated tissues for use with BODY_DETAIL_PLAN objects or in creatures; filename prefix `tissue_template_`.

Usually empty lines are used to divide different types of structures like the file name and \[OBJECT:\] or different entries, however everything which is not a token besides the 1st string (which is the filename) is understood as comments and is not considered.

The tokens are enclosed in square brackets (\[TOKEN:VALUES\]).

A list of tokens can be seen at Category:Tokens.

## Parsing

The order that *Dwarf Fortress* parses raw files in is determined by the first line of the raw file (*not* necessarily the filename). This parsing order is important for certain tags, such as \[COPY_TAGS_FROM\], but not for most other tags.

The names of raw files are completely irrelevant - when you create a new creature, you can put it in any file you want (or even in a brand-new file) and the game won't behave any differently. You can even rename all of the existing raw files and the game still won't care (as long as you generate a new world first, of course).

## Required objects

While most of the raw files are replaceable or removable, some contain raw objects that are used by procedurally generated creatures (such as FBs and experiments). Raws with the following IDs must exist, to support those creatures. The file names are where said objects exist by default, but are not important on their own, as long as the objects exist somewhere in the raws the game may use them. This list was compiled by examining the code that emits the various "Cannot generate random creatures -- missing \*" error messages.

material_template_default.txt:

    SKIN_TEMPLATE
    FAT_TEMPLATE
    MUSCLE_TEMPLATE
    SINEW_TEMPLATE
    BONE_TEMPLATE
    CARTILAGE_TEMPLATE
    HAIR_TEMPLATE
    FEATHER_TEMPLATE
    SCALE_TEMPLATE
    NAIL_TEMPLATE
    TOOTH_TEMPLATE
    EYE_TEMPLATE
    NERVE_TEMPLATE
    BRAIN_TEMPLATE
    LUNG_TEMPLATE
    HEART_TEMPLATE
    LIVER_TEMPLATE
    GUT_TEMPLATE
    STOMACH_TEMPLATE
    PANCREAS_TEMPLATE
    SPLEEN_TEMPLATE
    KIDNEY_TEMPLATE
    LEATHER_TEMPLATE
    HORN_TEMPLATE
    PEARL_TEMPLATE
    SILK_TEMPLATE
    BLOOD_TEMPLATE
    ICHOR_TEMPLATE
    GOO_TEMPLATE
    SLIME_TEMPLATE
    SHELL_TEMPLATE
    SOAP_TEMPLATE
    TALLOW_TEMPLATE
    CHITIN_TEMPLATE
    MILK_TEMPLATE
    CREATURE_CHEESE_TEMPLATE
    STRUCTURAL_PLANT_TEMPLATE
    SEED_TEMPLATE
    LEAF_TEMPLATE
    THREAD_PLANT_TEMPLATE
    PLANT_ALCOHOL_TEMPLATE
    PLANT_POWDER_TEMPLATE
    PLANT_EXTRACT_TEMPLATE
    CREATURE_EXTRACT_TEMPLATE
    FLAME_TEMPLATE

tissue_template_default.txt:

    SKIN_TEMPLATE
    FAT_TEMPLATE
    MUSCLE_TEMPLATE
    BONE_TEMPLATE
    SHELL_TEMPLATE
    HORN_TEMPLATE
    CARTILAGE_TEMPLATE
    HAIR_TEMPLATE
    CHEEK_WHISKERS_TEMPLATE
    CHIN_WHISKERS_TEMPLATE
    MOUSTACHE_TEMPLATE
    SIDEBURNS_TEMPLATE
    EYEBROW_TEMPLATE
    EYELASH_TEMPLATE
    FEATHER_TEMPLATE
    SCALE_TEMPLATE
    NAIL_TEMPLATE
    CLAW_TEMPLATE
    TALON_TEMPLATE
    TOOTH_TEMPLATE
    EYE_TEMPLATE
    NERVE_TEMPLATE
    BRAIN_TEMPLATE
    LUNG_TEMPLATE
    HEART_TEMPLATE
    LIVER_TEMPLATE
    GUT_TEMPLATE
    STOMACH_TEMPLATE
    PANCREAS_TEMPLATE
    SPLEEN_TEMPLATE
    KIDNEY_TEMPLATE
    FLAME_TEMPLATE

b_detail_plan_default.txt:

    STANDARD_MATERIALS
    STANDARD_TISSUES
    CHITIN_MATERIALS
    CHITIN_TISSUES
    FACIAL_HAIR_TISSUES
    HEAD_HAIR_TISSUE_LAYERS
    FACIAL_HAIR_TISSUE_LAYERS
    BODY_HAIR_TISSUE_LAYERS
    BODY_FEATHER_TISSUE_LAYERS
    VERTEBRATE_TISSUE_LAYERS
    EXOSKELETON_TISSUE_LAYERS
    STANDARD_HEAD_POSITIONS
    HUMANOID_HEAD_POSITIONS
    HUMANOID_RIBCAGE_POSITIONS
    SHELL_POSITIONS
    HUMANOID_RELSIZES

c_variation_default.txt:

    STANDARD_BIPED_GAITS
    STANDARD_QUADRUPED_GAITS
    STANDARD_WALKING_GAITS
    STANDARD_CLIMBING_GAITS
    STANDARD_SWIMMING_GAITS
    STANDARD_CRAWLING_GAITS
    STANDARD_FLYING_GAITS
    STANDARD_WALK_CRAWL_GAITS

body_rcp.txt:

    RCP_BASIC_BODY
    RCP_BASIC_BODY_STANCE
    RCP_BASIC_BODY_STANCE_WITH_HEAD_FLAG
    RCP_UPPER_BODY
    RCP_LOWER_BODY
    RCP_THORAX
    RCP_ABDOMEN
    RCP_CEPHALOTHORAX
    RCP_HEAD
    RCP_NECK
    RCP_TWO_PART_ARMS
    RCP_PINCERS
    RCP_CLAW_ARMS
    RCP_FIRST_SIMPLE_LEGS
    RCP_FIRST_SIMPLE_LEGS_GRASP
    RCP_SECOND_SIMPLE_LEGS
    RCP_THIRD_SIMPLE_LEGS
    RCP_FOURTH_SIMPLE_LEGS
    RCP_FIFTH_SIMPLE_LEGS
    RCP_SIMPLE_FRONT_LEGS
    RCP_SIMPLE_FRONT_LEGS_GRASP
    RCP_SIMPLE_REAR_LEGS
    RCP_TWO_PART_LEGS
    RCP_FRONT_FLIPPER
    RCP_REAR_FLIPPER
    RCP_TWO_FLIGHTLESS_WINGS
    RCP_TWO_WINGS
    RCP_TAIL
    RCP_2_TAILS
    RCP_3_TAILS
    RCP_TAIL_STINGER
    RCP_LOWER_BODY_STINGER
    RCP_PROBOSCIS
    RCP_TRUNK
    RCP_SHELL
    RCP_ANTENNAE
    RCP_1_HEAD_HORN
    RCP_2_HEAD_HORNS
    RCP_3_HEAD_HORNS
    RCP_4_HEAD_HORNS
    RCP_LARGE_MANDIBLES
    RCP_5_FINGERS
    RCP_4_FINGERS
    RCP_3_FINGERS
    RCP_2_FINGERS
    RCP_5_TOES
    RCP_4_TOES
    RCP_3_TOES
    RCP_2_TOES
    RCP_5_FRONT_TOES
    RCP_4_FRONT_TOES
    RCP_3_FRONT_TOES
    RCP_2_FRONT_TOES
    RCP_5_REAR_TOES
    RCP_4_REAR_TOES
    RCP_3_REAR_TOES
    RCP_2_REAR_TOES
    RCP_1_EYE
    RCP_2_EYES
    RCP_3_EYES
    RCP_BEAK
    RCP_NOSE
    RCP_CHEEKS
    RCP_LUNGS
    RCP_HEART
    RCP_GUTS
    RCP_THROAT
    RCP_SPINE
    RCP_UPPER_SPINE
    RCP_BRAIN
    RCP_SKULL
    RCP_MOUTH
    RCP_TEETH
    RCP_RIBS
    RCP_RIBS_EXTERNAL
    RCP_LIPS
    RCP_1_EYELID
    RCP_2_EYELIDS
    RCP_3_EYELIDS
    RCP_GLOSS_HOOF
    RCP_GLOSS_PAW
    RCP_5_FRONT_FINGERS*
    RCP_4_FRONT_FINGERS*
    RCP_3_FRONT_FINGERS*
    RCP_2_FRONT_FINGERS*
    RCP_TONGUE*

\* - The game does not confirm the presence of these objects, but it *will* still attempt to use them (and fail if they are missing)

The objects RCP_FORKED_TONGUE, RCP_BILL, and RCP_2_HEAD_ANTLERS are currently **not** used by the game and can be safely removed.

## Examples

- Creature examples
- Interaction examples
- Reaction examples
- Syndrome examples
