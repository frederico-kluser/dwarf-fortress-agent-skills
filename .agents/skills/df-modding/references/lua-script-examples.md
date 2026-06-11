# Lua script examples

> Fonte: [Lua script examples](https://dwarffortresswiki.org/index.php/Lua_script_examples) — Dwarf Fortress Wiki (GFDL & MIT). Snapshot 2026-06.

\

Snippets of vanilla generation can be found in Category:Lua script pages, and all vanilla scripts can be found in data/vanilla/vanilla_procedural/scripts/.

## Helper functions

### Search by reaction class

This script returns a table of all inorganic materials with a given [`[REACTION_CLASS]`](/index.php/Material_definition_token#REACTION_CLASS "Material definition token"). The `mat` table also has `reaction_product_class`, which includes both [`[MATERIAL_REACTION_PRODUCT]`](/index.php/Material_definition_token#MATERIAL_REACTION_PRODUCT "Material definition token") and [`[ITEM_REACTION_PRODUCT]`](/index.php/Material_definition_token#ITEM_REACTION_PRODUCT "Material definition token") IDs.

    get_all_by_reaction_class()

    function

    get_all_by_reaction_class
    (
    rc
    )

    local

    valid
    =
    {}

    for

    i
    ,
    inorg

    in

    ipairs
    (
    world
    .
    inorganic
    .
    inorganic
    )

    do

    for

    _
    ,
    class

    in

    inorg
    .
    mat
    .
    reaction_class

    do

    if

    class
    ==
    rc

    then

    valid
    [
    #
    valid
    +
    1
    ]
    =
    inorg

    end

    end

    end

    return

    valid

    end

## Languages

### Identity language

This makes a language called `GEN_IDENTITY` which is like: "Abbey abbeyabbeys the abbey of abbeys" - i.e. it's the "English" language you might see occasionally. It is present in `vanilla_procedural` and can be used for [`[TRANSLATION]`](/index.php/Entity_token#TRANSLATION "Entity token") by default.

    GEN_IDENTITY

    languages
    .
    GEN_IDENTITY
    =
    function
    ()

    -- just to demonstrate the absolute most basic method of generating one of these

    -- also so that you can just mod stuff to use GEN_IDENTITY

    local

    tbl
    =
    {}

    local

    unempty

    =

    function
    (
    str1
    ,

    str2
    )

    return

    str1
    ==
    ''

    and

    str2

    or

    str1

    end

    for

    k
    ,
    v

    in

    ipairs
    (
    world
    .
    language
    .
    word
    )

    do

    local

    str
    =
    ''

    str
    =
    unempty
    (
    str
    ,
    v
    .
    NOUN_SING
    )

    str
    =
    unempty
    (
    str
    ,
    v
    .
    ADJ
    )

    str
    =
    unempty
    (
    str
    ,
    v
    .
    VERB_FIRST_PRES
    )

    str
    =
    unempty
    (
    str
    ,
    string.lower
    (
    v
    .
    token
    ))

    tbl
    [
    v
    .
    token
    ]
    =
    str

    end

    return

    tbl

    end

### Kobold language

This generates a language made of [`[UTTERANCES]`](/index.php/Creature_token#UTTERANCES "Creature token"). This is essentially a proper translation based on the kobold language. Note that the hardcoded `utterance()` function generates words independently of any existing words in the language, so you may get duplicate words.

    GEN_KOBOLD

    languages
    .
    GEN_KOBOLD
    =
    function
    ()

    local

    tbl
    =
    {}

    for

    k
    ,
    v

    in

    ipairs
    (
    world
    .
    language
    .
    word
    )

    do

    tbl
    [
    v
    .
    token
    ]
    =
    utterance
    ()

    end

    return

    tbl

    end

## Generators

### Non-random generated material

Here's an example of an object registered through the `do_once` table. There are no random elements, it is equivalent (save for being [`[GENERATED]`](/index.php/Material_token#GENERATED "Material token")) to an object defined through Material definition tokens and registered through the `raws.register_inorganics()` function. It also prints itself to the lualog for debugging purposes.

    Single material

    do_once
    .
    cobalt

    =

    function
    ()

    local

    lines

    =

    {}

    -- basic inorganic definition

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[INORGANIC:COBALT]"

    -- add [GENERATED] to save properly

    add_generated_info
    (
    lines
    )

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:ALL_SOLID:cobalt]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:LIQUID:liquid cobalt]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:GAS:boiling cobalt]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_COLOR:ALL_SOLID:COBALT]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[SPECIAL]"

    raws
    .
    register_inorganics
    (
    lines
    )

    -- show in lualog

    print_table
    (
    lines
    )

    end

\
\
You can register multiple objects at the same time. This script takes a table of color tokens, and makes a metal named after each of them, with a corresponding cheaty adventure reaction.

    Chromatic metals

    do_once
    .
    chromatic_metal

    =

    function
    ()

    local

    lines

    =

    {}

    local

    reaction_lines

    =

    {}

    local

    color_tokens

    =

    {

    "AMETHYST"
    ,

    "AQUAMARINE"
    ,

    "CARDINAL"
    ,

    "COBALT"
    ,

    "EMERALD"
    ,

    "JADE"
    ,

    "MOSS_GREEN"
    ,

    "PEARL"
    ,

    "SAFFRON"
    ,

    "TURQUOISE"
    ,

    "WHITE"
    ,

    }

    -- make a metal for each color token

    for

    k
    ,
    v

    in

    pairs
    (
    color_tokens
    )

    do

    -- begin definition with ID token, [GENERATED] and template

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[INORGANIC:CHROMATICMETAL"
    ..
    v
    ..
    "]"

    add_generated_info
    (
    lines
    )

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]"

    -- look up the metal's color in the world table

    -- using string.lower(v) would result in "moss_green"

    local

    metalname

    =

    world
    .
    descriptor
    .
    color
    [
    v
    ].
    name

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:ALL_SOLID:"
    ..
    metalname
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:LIQUID:liquid "
    ..
    metalname
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:GAS:boiling "
    ..
    metalname
    ..
    "]"

    -- appearance

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_COLOR:ALL_SOLID:"
    ..
    v
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[SPECIAL]"

    -- create a corresponding reaction

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]

    =

    "[REACTION:CHROMATICMETAL"
    ..
    v
    ..
    "]"

    add_generated_info
    (
    reaction_lines
    )

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]

    =

    "[NAME:create "
    ..
    metalname
    ..
    " bars]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]

    =

    "[ADVENTURE_MODE_ENABLED]"

    -- make sure we're consistent with the inorganic ID

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]

    =

    "[PRODUCT:100:1:BAR:NONE:INORGANIC:CHROMATICMETAL"
    ..
    v
    ..
    "]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]

    =

    "[PRODUCT_DIMENSION:150]"

    end

    raws
    .
    register_inorganics
    (
    lines
    )

    raws
    .
    register_reactions
    (
    reaction_lines
    )

    end

### Random generation

Here's an example of various DF-specific randomizers in use:

- `trandom()` is used to determine how many metals generate this way.
- `utterance()` generates utterances from the Kobold language, e.g. "gorsnus", "stogodilmus", "gaylgis"
- `pick_random_no_replace()` determines the color from the table, but removes the rolled value so there's no repeats.

    Kobold metals

    do_once
    .
    kobold_metal

    =

    function
    ()

    local

    lines

    =

    {}

    local

    reaction_lines

    =

    {}

    local

    color_tokens

    =

    {

    "AMETHYST"
    ,

    "AQUAMARINE"
    ,

    "CARDINAL"
    ,

    "COBALT"
    ,

    "EMERALD"
    ,

    "JADE"
    ,

    "MOSS_GREEN"
    ,

    "PEARL"
    ,

    "SAFFRON"
    ,

    "TURQUOISE"
    ,

    "WHITE"
    ,

    }

    -- trandom() is expressed as (1dN)-1 because it uses C++ math that starts at 0

    local

    max_loops

    =

    trandom
    (
    10
    )
    +
    1

    -- create 1-10 metals

    for

    i

    =

    1
    ,
    max_loops

    do

    -- begin definition with ID token, [GENERATED] and template

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[INORGANIC:KOBOLDMETAL"
    ..
    i
    ..
    "]"

    add_generated_info
    (
    lines
    )

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]"

    -- this is the kobold name function

    local

    metalname

    =

    utterance
    ()
    ..
    "ite"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:ALL_SOLID:"
    ..
    metalname
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:LIQUID:liquid "
    ..
    metalname
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:GAS:boiling "
    ..
    metalname
    ..
    "]"

    -- no_replace removes the value from the table

    -- we don't need a fallback because there's more values than metals

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_COLOR:ALL_SOLID:"
    ..
    pick_random_no_replace
    (
    color_tokens
    )
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[SPECIAL]"

    -- create a corresponding reaction

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]

    =

    "[REACTION:KOBOLDMETAL"
    ..
    i
    ..
    "]"

    add_generated_info
    (
    reaction_lines
    )

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]

    =

    "[NAME:create "
    ..
    metalname
    ..
    " bars]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]

    =

    "[ADVENTURE_MODE_ENABLED]"

    -- make sure we're consistent with the inorganic ID

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]

    =

    "[PRODUCT:100:1:BAR:NONE:INORGANIC:KOBOLDMETAL"
    ..
    i
    ..
    "]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]

    =

    "[PRODUCT_DIMENSION:150]"

    end

    raws
    .
    register_inorganics
    (
    lines
    )

    raws
    .
    register_reactions
    (
    reaction_lines
    )

    end

### New divine metals

Many of the tables used by vanilla procedural objects are global, and thus can be added to or overwritten by mods. You can add new metal descriptions for divine metal pretty easily, for example:

    Laughing metal

    metal_by_sphere
    .
    CHILDREN
    =
    {

    name
    =
    "laughing metal"
    ,

    col
    =
    "7:0:1"
    ,

    color
    =
    "WHITE"

    }

\
\
You can also add alternatives to the default divine metal function, such as one based on the aforementioned kobold metals. Vanilla divine metal uses `metal_by_sphere` to determine its properties, and is thus valid only if the input sphere has an entry in that table. Note that even if the weights are nominally the same; because it is valid for all input spheres, it will outnumber instances of the more limited vanilla material.

    Divine kobold metal

    materials
    .
    divine
    .
    metal
    .
    kobold

    =

    function
    (
    sphere
    )

    if

    not

    foo

    then

    log
    (
    #
    metal_by_sphere
    )

    log
    (
    #
    world
    .
    spheres
    )

    foo

    =

    true

    end

    local

    lines

    =

    {}

    --generation function handles ID, registration, generated info

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]"

    --add_generated_info(lines)

    local

    metalname

    =

    utterance
    ()
    ..
    "ite"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:ALL_SOLID:"
    ..
    metalname
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:LIQUID:liquid "
    ..
    metalname
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_NAME_ADJ:GAS:boiling "
    ..
    metalname
    ..
    "]"

    local

    color_tokens

    =

    {

    "AMETHYST"
    ,

    "AQUAMARINE"
    ,

    "CARDINAL"
    ,

    "COBALT"
    ,

    "EMERALD"
    ,

    "JADE"
    ,

    "MOSS_GREEN"
    ,

    "PEARL"
    ,

    "SAFFRON"
    ,

    "TURQUOISE"
    ,

    "WHITE"
    ,

    }

    --allow for duplicate colors

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[STATE_COLOR:ALL_SOLID:"
    ..
    pick_random
    (
    color_tokens
    )
    ..
    "]"

    --add a block of tokens

    lines
    =
    split_to_lines
    (
    lines
    ,
    [[

        [MATERIAL_VALUE:200]

        [SPEC_HEAT:7500]

        [MELTING_POINT:NONE]

        [BOILING_POINT:NONE]

        [ITEMS_WEAPON][ITEMS_WEAPON_RANGED][ITEMS_AMMO][ITEMS_DIGGER][ITEMS_ARMOR][ITEMS_ANVIL]

        [ITEMS_HARD]

        [ITEMS_METAL]

        [ITEMS_BARRED]

        [ITEMS_SCALED]

        [SOLID_DENSITY:1000]

        [LIQUID_DENSITY:1000]

        [MOLAR_MASS:20000]

        [IMPACT_YIELD:1000000]

        [IMPACT_FRACTURE:2000000]

        [IMPACT_STRAIN_AT_YIELD:0]

        [COMPRESSIVE_YIELD:1000000]

        [COMPRESSIVE_FRACTURE:2000000]

        [COMPRESSIVE_STRAIN_AT_YIELD:0]

        [TENSILE_YIELD:1000000]

        [TENSILE_FRACTURE:2000000]

        [TENSILE_STRAIN_AT_YIELD:0]

        [TORSION_YIELD:1000000]

        [TORSION_FRACTURE:2000000]

        [TORSION_STRAIN_AT_YIELD:0]

        [SHEAR_YIELD:1000000]

        [SHEAR_FRACTURE:2000000]

        [SHEAR_STRAIN_AT_YIELD:0]

        [BENDING_YIELD:1000000]

        [BENDING_FRACTURE:2000000]

        [BENDING_STRAIN_AT_YIELD:0]

        [MAX_EDGE:12000]

        ]]
    )

    --sends this to get registered

    return

    {
    raws
    =
    lines
    ,
    weight
    =
    1
    }

    end

### Remove default functions

Just as easily as new functions and table entries can be added, default entries can be overwritten so that they cannot generate. This snippet removes the default forgotten beasts.

See Lua functions#Generation Tables for a list of the tables the default functions are stored in.

    creatures.fb.default=nil

### Basic generated creature

This is essentially the simplest possible creature. It has no extraordinary options (beyond an association with animals and creation), and each world generates one species from this function. It doesn't have any biome tokens or likewise, so it can only be spawned in the arena, but it is still functional.

A sample output would be "A quadruped composed of flame. It has two narrow tails and it has a regal bearing."

    do_once.basic_creature

    do_once
    .
    basic_creature

    =

    function
    ()

    local

    lines

    =

    {}

    local

    tok
    =
    "BASIC_PROCEDURAL_CREATURE"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CREATURE:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    local

    options
    =
    {

    token
    =
    tok
    ,

    spheres
    =
    {

    ANIMALS
    =
    true
    ,

    CREATION
    =
    true

    }

    }

    lines
    =
    split_to_lines
    (
    lines
    ,
    [[

            [NAME:procedural creature:procedural creatures:procedural]

            [CASTE_NAME:procedural creature:procedural creatures:procedural]

        ]]
    )

    --adds some common tokens depending on the options

    add_regular_tokens
    (
    lines
    ,
    options
    )

    --handles sphere options: fills out [SPHERE] tokens from options.spheres, and so on

    populate_sphere_info
    (
    lines
    ,
    options
    )

    --choose a creature profile to base on

    local

    rcp
    =
    get_random_creature_profile
    (
    options
    )

    --set [BODY_SIZE] and some relevant tokens

    add_body_size
    (
    lines
    ,
    rcp
    .
    min_size
    ,
    options
    )

    --add the tile from the creature profile

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CREATURE_TILE:"
    ..
    tile_string
    (
    rcp
    .
    tile
    )
    ..
    "]"

    --the Big Function determining tweaks, body, appearance, description...

    build_procgen_creature
    (
    rcp
    ,
    lines
    ,
    options
    )

    raws
    .
    register_creatures
    (
    lines
    )

    end

### Making your own rcp

You don't have to be limited to the vanilla list of random creature variants. Mods can add new kinds of random creature profiles, materials, etc that can be seamlessly integrated into how it generates creatures.

This script generates a single creature based on a eurypterid. It has a unique rcp, set in the function itself.

    do_once.local_rcp

    do_once
    .
    local_rcp

    =

    function
    ()

    local

    lines

    =

    {}

    local

    tok
    =
    "LOCAL_RCP"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CREATURE:"
    ..
    tok
    ..
    "]"

    add_generated_info
    (
    lines
    )

    local

    options
    =
    {

    token
    =
    tok
    ,

    spheres
    =
    {

    ANIMALS
    =
    true
    ,

    WATER
    =
    true

    }

    }

    add_regular_tokens
    (
    lines
    ,
    options
    )

    populate_sphere_info
    (
    lines
    ,
    options
    )

    --habitat

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[BIOME:ANY_OCEAN]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[LARGE_ROAMING]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[AQUATIC][UNDERSWIM]"

    --define a local creature profile

    local

    rcp
    =
    {

    name_string
    =
    "eurypterid"
    ,

    tile
    =
    'E'
    ,

    body_base
    =
    "SCORPION"
    ,

    c_class
    =
    "CHITIN_EXO"
    ,

    must_have_pincers
    =
    true
    ,

    must_have_tail
    =
    true
    ,

    min_size
    =
    70000
    ,

    weight
    =
    200
    ,

    }

    local

    name_str

    =

    rcp
    .
    name_string
    ..
    ":"
    ..
    rcp
    .
    name_string
    ..
    "s:"
    ..
    rcp
    .
    name_string
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[NAME:"
    ..
    name_str

    lines
    [
    #
    lines
    +
    1
    ]

    =

    "[CASTE_NAME:"
    ..
    name_str

    add_body_size
    (
    lines
    ,
    rcp
    .
    min_size
    ,
    options
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CREATURE_TILE:"
    ..
    tile_string
    (
    rcp
    .
    tile
    )
    ..
    "]"

    build_procgen_creature
    (
    rcp
    ,
    lines
    ,
    options
    )

    raws
    .
    register_creatures
    (
    lines
    )

    end

\
\
Adding a eurypterid profile to `random_creature_profiles` allows any creature to access it, if their profile is determined randomly.

This script gives it proper flippers in its body base function. It's also associated with water-based random creatures, so it can potentially generate as an aquatic forgotten beast species.

Other feature variants stored in tables, like materials, attacks, or descriptions, can be added in this way.

    Global rcp

    random_creature_types
    .
    EURYPTERID
    =
    {

    name_string
    =
    "eurypterid"
    ,

    tile
    =
    'E'
    ,

    body_base
    =
    "SCORPION_FLIPPERS"
    ,

    c_class
    =
    "CHITIN_EXO"
    ,

    must_have_pincers
    =
    true
    ,

    must_have_tail
    =
    true
    ,

    min_size
    =
    70000
    ,

    weight
    =
    200
    ,

    }

    body_base_fun
    .
    SCORPION_FLIPPERS
    =
    function
    (
    rcp
    ,
    options
    )

    options
    .
    pcg_layering_base
    =
    "BEAST_SCORPION"

    options
    .
    walk_var
    =
    "STANDARD_WALKING_GAITS"

    options
    .
    walk_speed
    =
    900

    return

    {
    "RCP_CEPHALOTHORAX"
    ,
    "RCP_ABDOMEN"
    ,
    "RCP_FIRST_SIMPLE_LEGS"
    ,
    "RCP_SECOND_SIMPLE_LEGS"
    ,
    "RCP_THIRD_SIMPLE_LEGS"
    ,
    "RCP_PINCERS"
    ,
    "RCP_FRONT_FLIPPER"
    }

    end

    water_based_random_creature
    .
    EURYPTERID
    =
    true

### Werebugs

You can make a custom function to determine what rcps are available to a given creature.

These scripts are for an arthropoid version of a werebeast.

- `arthropod_rcp` is a list of rcp keys which fit this theme (plus a few worms on there for fun), which the creature function rolls on to pick its form.
- `is_bloodsucking_by_key`, along with `rcp.must_suck_blood_through_proboscis` and `rcp.must_suck_blood_through_mouth` are checked to assign [`[BLOODSUCKER]`](/index.php/Creature_token#BLOODSUCKER "Creature token") to it, which allows certain creature types to exhibit vampiric behavior if their berserk rampage wasn't enough fun.

Otherwise, the function should work the same as vanilla werebeasts, generating an associated major curse in the same way and becoming "twisted into humanoid form" (at the expense of their additional limbs).

    arthropod_rcp

    local

    arthropod_rcp

    =

    {

    "ARACHNID_MITE"
    ,

    "ARACHNID_SCORPION"
    ,

    "ARACHNID_SPIDER"
    ,

    "ARACHNID_TARANTULA"
    ,

    "ARACHNID_TICK"
    ,

    "CRUSTACEAN_CRAB"
    ,

    "CRUSTACEAN_LOBSTER"
    ,

    "CRUSTACEAN_SHRIMP"
    ,

    "INSECT_ANT"
    ,

    "INSECT_ANTLION"
    ,

    "INSECT_APHID"
    ,

    "INSECT_BEE"
    ,

    "INSECT_BUTTERFLY"
    ,

    "INSECT_CADDISFLY"
    ,

    "INSECT_CATERPILLAR"
    ,

    "INSECT_CICADA"
    ,

    "INSECT_COCKROACH"
    ,

    "INSECT_CRICKET"
    ,

    "INSECT_DAMSELFLY"
    ,

    "INSECT_DARKLING_BEETLE"
    ,

    "INSECT_DRAGONFLY"
    ,

    "INSECT_EARWIG"
    ,

    "INSECT_FIREFLY"
    ,

    "INSECT_FLEA"
    ,

    "INSECT_FLY"
    ,

    "INSECT_GRASSHOPPER"
    ,

    "INSECT_HORNET"
    ,

    "INSECT_LACEWING"
    ,

    "INSECT_LADYBUG"
    ,

    "INSECT_LOUSE"
    ,

    "INSECT_MAGGOT"
    ,

    "INSECT_MANTIS"
    ,

    "INSECT_MAYFLY"
    ,

    "INSECT_MOSQUITO"
    ,

    "INSECT_MOTH"
    ,

    "INSECT_SILVERFISH"
    ,

    "INSECT_SCARAB_BEETLE"
    ,

    "INSECT_SCORPIONFLY"
    ,

    "INSECT_SNAKEFLY"
    ,

    "INSECT_STONEFLY"
    ,

    "INSECT_TERMITE"
    ,

    "INSECT_THRIPS"
    ,

    "INSECT_WASP"
    ,

    "INSECT_WEEVIL"
    ,

    "NEMATODE"
    ,

    "LEECH"
    ,

    }

    is_bloodsucking_by_key

    local

    is_bloodsucking_by_key

    =

    {

    ARACHNID_MITE
    =
    true
    ,

    ARACHNID_TICK
    =
    true
    ,

    INSECT_EARWIG
    =
    true
    ,
    --some are parasitic

    INSECT_FLEA
    =
    true
    ,

    INSECT_LOUSE
    =
    true
    ,

    INSECT_MAGGOT
    =
    true
    ,

    INSECT_THRIPS
    =
    true
    ,
    --no bloodsucking reported, but does bite humans

    NEMATODE
    =
    true
    ,

    }

    creatures.night_creature.werebeast.werebug

    creatures
    .
    night_creature
    .
    werebeast
    .
    werebug
    =
    function
    (
    tok
    )

    local

    lines
    =
    {}

    local

    options
    =
    {

    spheres
    =
    {

    CHAOS
    =
    true
    ,

    ANIMALS
    =
    true
    ,

    NIGHT
    =
    true
    ,

    MOON
    =
    true

    },

    always_glowing_eyes
    =
    true
    ,

    use_werebeast_pcg
    =
    true
    ,

    --use them if werebug sprites somehow exist

    animal_coloring_allowed
    =
    true
    ,

    no_tweak
    =
    true
    ,

    material_weakness
    =
    true
    ,

    humanoidable_only
    =
    true
    ,

    prioritize_bite
    =
    true
    ,

    force_ichor
    =
    true
    ,

    token
    =
    tok

    }

    options
    .
    night_creature_agile_pref
    =
    true

    night_creature_universals
    (
    lines
    ,
    options
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NIGHT_CREATURE_HUNTER]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CAN_LEARN]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CAN_SPEAK]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NO_GENDER]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[BONECARN]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CRAZED]"

    if

    options
    .
    night_creature_strength_pref

    then

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:STRENGTH:1000:1250:1500:2000:2250:2500:3000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:AGILITY:450:550:700:750:800:850:900]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:TOUGHNESS:850:900:950:1000:1050:1100:1150]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:ENDURANCE:850:900:950:1000:1050:1100:1150]"

    options
    .
    special_walk_speed
    =
    1000

    elseif

    options
    .
    night_creature_agile_pref

    then

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:STRENGTH:450:550:700:750:800:850:900]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:AGILITY:1000:1250:1500:2000:2250:2500:3000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:TOUGHNESS:850:900:950:1000:1050:1100:1150]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:ENDURANCE:850:900:950:1000:1050:1100:1150]"

    options
    .
    special_walk_speed
    =
    800
    ;

    elseif

    options
    .
    night_creature_strength_agile_pref

    then

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:STRENGTH:1000:1150:1250:1500:2000:2250:2500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:AGILITY:1000:1150:1250:1500:2000:2250:2500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:TOUGHNESS:850:900:950:1000:1050:1100:1150]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:ENDURANCE:850:900:950:1000:1050:1100:1150]"

    options
    .
    special_walk_speed
    =
    850
    ;

    end

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:RECUPERATION:450:1050:1150:1250:1350:1550:2250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PHYS_ATT_RANGE:DISEASE_RESISTANCE:700:1300:1400:1500:1600:1800:2500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MENT_ATT_RANGE:ANALYTICAL_ABILITY:1250:1500:1750:2000:2500:3000:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MENT_ATT_RANGE:FOCUS:1250:1500:1750:2000:2500:3000:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MENT_ATT_RANGE:WILLPOWER:1250:1500:1750:2000:2500:3000:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MENT_ATT_RANGE:PATIENCE:0:333:666:1000:2333:3666:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MENT_ATT_RANGE:MEMORY:1250:1500:1750:2000:2500:3000:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MENT_ATT_RANGE:LINGUISTIC_ABILITY:450:1050:1150:1250:1350:1550:2250]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MENT_ATT_RANGE:MUSICALITY:0:333:666:1000:2333:3666:5000]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MENT_ATT_RANGE:SOCIAL_AWARENESS:700:1300:1400:1500:1600:1800:2500]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:BASHFUL:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:STRESS_VULNERABILITY:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:FRIENDLINESS:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:DISDAIN_ADVICE:100:100:100]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:CHEER_PROPENSITY:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:GRATITUDE:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:TRUST:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:ALTRUISM:0:0:0]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[PERSONALITY:CRUELTY:100:100:100]"

    add_regular_tokens
    (
    lines
    ,
    options
    )

    populate_sphere_info
    (
    lines
    ,
    options
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:WRESTLING:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:BITE:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:GRASP_STRIKE:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:STANCE_STRIKE:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:MELEE_COMBAT:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:DODGING:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:SITUATIONAL_AWARENESS:6]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NATURAL_SKILL:SNEAK:20]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[DIFFICULTY:3]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[LAIR:SIMPLE_BURROW:50]"

    -- pick a random bug rcp, there's no overlap with the mammal/reptile standard werebeasts

    finalize_random_creature_types
    ()

    -- good practice to run before rolling on it

    local

    rcp_key

    =

    pick_random_no_replace
    (
    arthropod_rcp
    )

    or

    "INSECT_MANTIS"

    local

    rcp
    =
    random_creature_types
    [
    rcp_key
    ]

    local

    custom_desc_str

    =

    "it is crazed for blood and flesh"

    -- make them also vampires if they suck blood

    if

    rcp
    .
    must_suck_blood_through_proboscis

    or

    rcp
    .
    must_suck_blood_through_mouth

    or

    is_bloodsucking_by_key
    [
    rcp_key
    ]

    then

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[BLOODSUCKER]"

    custom_desc_str

    =

    "it is crazed for warm blood"

    end

    -- This sort of process should be fully generalized

    -- to all creatures you want to have bespoke associated interactions

    -- for example, you can have a blessing that allows a sort of

    -- uncrazed transformation into some sort of bespoke

    -- generated thing--at least, hopefully it's robust enough for that

    local

    choice
    =
    generate_from_list
    (
    werebeast_origin_interactions
    ,
    tok
    ,
    rcp
    .
    name_string
    ,
    options
    )

    map_merge
    (
    options
    ,
    choice
    .
    options
    )

    local

    werebeast_choice_raws
    =
    choice
    .
    interaction

    or

    choice
    .
    raws

    raws
    .
    register_interactions
    (
    werebeast_choice_raws
    )

    add_body_size
    (
    lines
    ,
    math.max
    (
    rcp
    .
    min_size
    ,
    80000
    +
    trandom
    (
    11
    )
    *
    1000
    ),
    options
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CREATURE_TILE:165]"

    --Ñ

    options
    .
    forced_color
    =
    {

    f
    =
    6
    ,

    b
    =
    0
    ,

    br
    =
    1

    }

    options
    .
    custom_desc_func
    =
    function
    (
    options
    )

    return

    custom_desc_str

    end

    build_procgen_creature
    (
    rcp
    ,
    lines
    ,
    options
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[GO_TO_START]"

    -- remove second words like " beetle", etc from the end

    local

    short_name

    =

    rcp
    .
    name_string
    :
    gsub
    (
    "%s(%w+)$"
    ,
    ""
    )

    local

    name_str
    =
    "were"
    ..
    short_name
    ..
    ":were"
    ..
    short_name
    ..
    "s:were"
    ..
    short_name
    ..
    "]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:"
    ..
    name_str

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CASTE_NAME:"
    ..
    name_str

    return

    {
    raws
    =
    lines
    ,
    weight
    =
    1
    }

    end

### New forgotten beasts

You can add new types of forgotten beasts (or more appropriately, [`[FEATURE_BEAST]`](/index.php/Creature_token#FEATURE_BEAST "Creature token")s). These generate as alternatives when populating the caverns with unique monsters. There are a number of options to interact with shared generation functions.

Unbidden spirits only appear in dry cave layers, and like "spirit" demons, are malevolent floating beings made of gas or dust.

    Unbidden spirit

    creatures
    .
    fb
    .
    unbidden
    =
    function
    (
    layer_type
    ,
    tok
    )

    if

    layer_type
    ==
    0

    then

    return

    nil

    end

    -- land only

    local

    tbl
    =
    {}

    local

    options
    =
    {

    strong_attack_tweak
    =
    true
    ,

    always_make_uniform
    =
    true
    ,

    always_insubstantial
    =
    true
    ,

    intangible_flier
    =
    true
    ,

    spheres
    =
    {
    CAVERNS
    =
    true
    },

    is_evil
    =
    true
    ,

    sickness_name
    =
    "beast sickness"
    ,

    token
    =
    tok

    }

    tbl
    =
    split_to_lines
    (
    tbl
    ,
    [[

        [FEATURE_BEAST]

        [ATTACK_TRIGGER:0:0:2]

        [NAME:unbidden spirit:unbidden spirit:unbidden spirit]

        [CASTE_NAME:unbidden spirit:unbidden spirit:unbidden spirit]

        [NO_GENDER]

        [CARNIVORE]

        [DIFFICULTY:10]

        [NATURAL_SKILL:WRESTLING:6]

        [NATURAL_SKILL:BITE:6]

        [NATURAL_SKILL:GRASP_STRIKE:6]

        [NATURAL_SKILL:STANCE_STRIKE:6]

        [NATURAL_SKILL:MELEE_COMBAT:6]

        [NATURAL_SKILL:DODGING:6]

        [NATURAL_SKILL:SITUATIONAL_AWARENESS:6]

        [LARGE_PREDATOR]

        ]]
    )

    add_regular_tokens
    (
    tbl
    ,
    options
    )

    tbl
    [
    #
    tbl
    +
    1
    ]
    =
    layer_type
    ==
    0

    and

    "[BIOME:SUBTERRANEAN_WATER]"

    or

    "[BIOME:SUBTERRANEAN_CHASM]"

    if

    layer_type
    ==
    0

    then

    options
    .
    spheres
    .
    WATER
    =
    true

    end

    options
    .
    spheres
    [
    pick_random
    (
    evil_spheres
    )]
    =
    true

    options
    .
    do_water
    =
    layer_type
    ==
    0

    populate_sphere_info
    (
    tbl
    ,
    options
    )

    local

    rcp
    =
    get_random_creature_profile
    (
    options
    )

    add_body_size
    (
    tbl
    ,
    math.max
    (
    10000000
    ,
    rcp
    .
    min_size
    ),
    options
    )

    tbl
    [
    #
    tbl
    +
    1
    ]
    =
    "[CREATURE_TILE:"
    ..
    tile_string
    (
    rcp
    .
    tile
    )
    ..
    "]"

    build_procgen_creature
    (
    rcp
    ,
    tbl
    ,
    options
    )

    -- Weight is a float; all vanilla objects have weight 1

    return

    {
    creature
    =
    tbl
    ,
    weight
    =
    0.5
    }

    end

\
\
Elementals are defined by the material they're made of, using a table of options to set the right properties. In a dry chasm layer, they'll roll on the `fb_elements` table, while in a water layer, they'll be a water elemental. Should they ever carry a syndrome, they would inflict dyskrasia.

The most important feature is setting `options.sphere_rcm` to a key in `random_creature_materials`, so fire elementals are made of "FLAME" and earth elementals are made of "ANY_MINERAL".

    Elemental

    fb_elements

    =

    {

    {

    name
    =
    "fire"
    ,

    rcm
    =
    "FLAME"
    ,

    spheres
    =
    {

    FIRE
    =
    true

    },

    options
    =
    {

    fire_immune
    =
    true

    }

    },

    {

    name
    =
    "earth"
    ,

    rcm
    =
    "ANY_MINERAL"
    ,

    rcp_options
    =
    {

    always_flightless
    =
    true

    },

    spheres
    =
    {

    EARTH
    =
    true
    ,

    MINERALS
    =
    true

    }

    },

    {

    name
    =
    "air"
    ,

    rcm
    =
    "STEAM"
    ,

    spheres
    =
    {

    WIND
    =
    true
    ,

    SKY
    =
    true

    },

    options
    =
    {

    always_insubstantial
    =
    true
    ,

    intangible_flier
    =
    true

    }

    }

    }

    creatures
    .
    fb
    .
    elemental
    =
    function
    (
    layer_type
    ,
    tok
    )

    local

    lines
    =
    {}

    local

    options
    =
    {

    strong_attack_tweak
    =
    true
    ,

    always_make_uniform
    =
    true
    ,

    --irrelevant due to sphere_rcm

    spheres
    =
    {},

    sickness_name
    =
    "dyskrasia"
    ,

    token
    =
    tok

    }

    lines
    =
    split_to_lines
    (
    lines
    ,
    [[

            [FEATURE_BEAST]

            [ATTACK_TRIGGER:0:0:2]

            [NO_GENDER]

            [NO_EAT][NO_DRINK]

            [DIFFICULTY:10]

            [NATURAL_SKILL:WRESTLING:6]

            [NATURAL_SKILL:BITE:6]

            [NATURAL_SKILL:GRASP_STRIKE:6]

            [NATURAL_SKILL:STANCE_STRIKE:6]

            [NATURAL_SKILL:MELEE_COMBAT:6]

            [NATURAL_SKILL:DODGING:6]

            [NATURAL_SKILL:SITUATIONAL_AWARENESS:6]

            [LARGE_PREDATOR]

        ]]
    )

    -- Create a water elemental in water layers, otherwise use another type

    local

    water_elemental

    =

    {

    name
    =
    "water"
    ,

    rcm
    =
    "WATER"
    ,

    spheres
    =
    {
    WATER
    =
    true
    },

    options
    =
    {
    do_water
    =
    true
    }

    }

    local

    my_element

    =

    layer_type
    ==
    1

    and

    pick_random
    (
    fb_elements
    )

    or

    water_elemental

    -- Assign propertes from chosen element

    map_merge
    (
    options
    .
    spheres
    ,
    my_element
    .
    spheres
    )

    if

    my_element
    .
    options

    then

    map_merge
    (
    options
    ,
    my_element
    .
    options
    )

    end

    add_regular_tokens
    (
    lines
    ,
    options
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    layer_type
    ==
    0

    and

    "[BIOME:SUBTERRANEAN_WATER]"

    or

    "[BIOME:SUBTERRANEAN_CHASM]"

    populate_sphere_info
    (
    lines
    ,
    options
    )

    -- Set custom material

    options
    .
    sphere_rcm
    =
    my_element
    .
    rcm

    -- Build body

    local

    rcp
    =
    get_random_creature_profile
    (
    options
    )

    -- Set more options on the RCP

    if

    my_element
    .
    rcp_options

    then

    map_merge
    (
    rcp
    .
    options
    ,
    my_element
    .
    rcp_options
    )

    end

    add_body_size
    (
    lines
    ,
    math.max
    (
    10000000
    ,
    rcp
    .
    min_size
    ),
    options
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CREATURE_TILE:'E']"

    build_procgen_creature
    (
    rcp
    ,
    lines
    ,
    options
    )

    -- Generate name

    local

    element_name

    =

    my_element
    .
    name

    or

    "glitchstuff"

    local

    name_str

    =

    element_name
    ..
    " elemental:"
    ..
    element_name
    ..
    " elemental:"
    ..
    element_name
    ..
    "-elemental]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[GO_TO_START]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[NAME:"
    ..
    name_str

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[CASTE_NAME:"
    ..
    name_str

    return

    {
    raws
    =
    lines
    ,
    weight
    =
    1.5
    }

    end

### Tweaking creatures

Common Lua features allow you to extend functions by mirroring the original function and then overwriting it, akin to the `SELECT` tags. This function extends `add_regular_tokens()` to add [`[GENERAL_MATERIAL_FORCE_MULTIPLIER]`](/index.php/Creature_token#GENERAL_MATERIAL_FORCE_MULTIPLIER "Creature token") to all generated creatures.

    add_regular_tokens (extension)

    old_add_regular_tokens
    =
    add_regular_tokens

    function

    add_regular_tokens
    (
    lines
    ,
    options
    )

    old_add_regular_tokens
    (
    lines
    ,
    options
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[GENERAL_MATERIAL_FORCE_MULTIPLIER:1:2]"

    end

\
\
This function is run in `build_body_from_rcp()` right before tweaks are determined (See Lua functions#Creature patching). If a generated creature's size is greater than 500,000 Γ (about as much as an elephant), this patch adds [`[POWER]`](/index.php/Creature_token#POWER "Creature token") and the like to make forgotten beasts, titans, etc capable of impersonating deities and ruling civilizations.

    btc1_tweaks.titan_worship

    -- make all large creatures into powers

    btc1_tweaks
    .
    titan_worship
    =
    function
    (
    lines
    ,
    options
    ,
    add_to_body
    ,
    add_to_body_unique
    ,
    add_tweak_candidate
    )

    if

    options
    .
    body_size
    >=
    500000

    then

    -- described as "very large", graphics size cutoff

    options
    .
    can_learn
    =
    true

    -- for flavor text

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[INTELLIGENT]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SUPERNATURAL]"

    -- knows secrets according to their spheres

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[POWER]"

    -- impersonates deities

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SPREAD_EVIL_SPHERES_IF_RULER]"

    end

    end

### Adamantine alloys

You can add your own arbitrary generated objects, though as of right now there's no way to make settings for them. This allows for some *truly* wild stuff; here's a fun example: adamantine-metal alloys for every single non-special metal, giving you an average of the properties of them.

    Adamantine alloys

    preprocess
    .
    adamantine_alloys
    =
    function
    ()

    if

    not

    random_object_parameters
    .
    main_world_randoms

    then

    return

    end

    local

    l
    =
    get_debug_logger
    (
    2
    )

    local

    lines
    =
    {}

    local

    reaction_lines
    =
    {}

    local

    reaction_names
    =
    {}

    local

    adamantine
    =
    world
    .
    inorganic
    .
    inorganic
    .
    ADAMANTINE

    if

    not

    adamantine

    then

    return

    end

    local

    adamantine_color
    =
    world
    .
    descriptor
    .
    color
    [
    world
    .
    descriptor
    .
    color_pattern
    [
    adamantine
    .
    material
    .
    color_pattern
    .
    SOLID
    ].
    color
    [
    1
    ]]

    local

    adamantine_modulus

    =

    2500000

    --mildly arbitrary, just below the theoretical limit

    l
    (
    "Starting"
    )

    local

    done_category
    =
    false

    for

    k
    ,
    v

    in

    ipairs
    (
    world
    .
    inorganic
    .
    inorganic
    )

    do

    if

    not

    v
    .
    flags
    .
    SPECIAL

    and

    v
    .
    material
    .
    flags
    .
    IS_METAL

    then

    l
    (
    v
    .
    token
    )

    local

    token
    =
    "GEN_ADAMANTINE_"
    ..
    v
    .
    token

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[INORGANIC:"
    ..
    token
    ..
    "]"

    add_generated_info
    (
    lines
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[USE_MATERIAL_TEMPLATE:METAL_TEMPLATE]"

    for

    kk
    ,
    vv

    in

    pairs
    (
    v
    .
    material
    .
    adj
    )

    do

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STATE_ADJ:"
    ..
    kk
    ..
    ":adamantine "
    ..
    vv
    ..
    "]"

    --"adamantine molten steel"? it's fine

    end

    for

    kk
    ,
    vv

    in

    pairs
    (
    v
    .
    material
    .
    name
    )

    do

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STATE_NAME:"
    ..
    kk
    ..
    ":adamantine "
    ..
    vv
    ..
    "]"

    end

    l
    (
    2
    )

    local

    mat_values
    =
    {}

    -- Find the ratio for which you get closest to (but not below) 2000000 in the material's worst property

    local

    worst
    =
    math.min
    (
    v
    .
    material
    .
    yield
    .
    IMPACT
    ,
    v
    .
    material
    .
    fracture
    .
    SHEAR
    )

    local

    wafers
    =
    1

    local

    bars
    =
    1

    if

    worst

    <

    2000000

    then

    local

    ratio

    =

    (
    2000000
    -
    3
    *
    worst
    )
    /
    1000000

    local

    best_diff
    =
    1

    for

    i
    =
    1
    ,
    10

    do

    local

    wafer_amt
    =
    i
    *
    ratio

    if

    wafer_amt
    >
    1

    and

    wafer_amt
    <
    20

    and

    math.ceil
    (
    wafer_amt
    )
    -
    wafer_amt
    <
    best_diff

    then

    best_diff
    =
    math.ceil
    (
    wafer_amt
    )
    -
    wafer_amt

    wafers
    =
    math.ceil
    (
    wafer_amt
    )

    bars
    =
    i

    end

    end

    end

    local

    avg_denom
    =
    1
    /
    (
    bars
    *
    3
    +
    wafers
    )

    -- Multiplication just a bit faster than division, we're rounding at the end anyway

    local

    solid_cl
    =
    nil

    for

    kk
    ,
    vv

    in

    pairs
    (
    v
    .
    material
    .
    color_pattern
    )

    do

    -- time to get silly

    local

    this_color
    =
    world
    .
    descriptor
    .
    color
    [
    world
    .
    descriptor
    .
    color_pattern
    [
    vv
    ].
    color
    [
    1
    ]]

    local

    wanted_color
    =
    {

    r
    =
    (
    this_color
    .
    r
    *
    bars
    *
    3
    +
    adamantine_color
    .
    r
    *
    wafers
    )
    *
    avg_denom
    ,

    g
    =
    (
    this_color
    .
    g
    *
    bars
    *
    3
    +
    adamantine_color
    .
    g
    *
    wafers
    )
    *
    avg_denom
    ,

    b
    =
    (
    this_color
    .
    b
    *
    bars
    *
    3
    +
    adamantine_color
    .
    b
    *
    wafers
    )
    *
    avg_denom
    ,

    }

    local

    best_total_diff
    =
    1000000000

    local

    best_clp
    =
    nil

    for

    _
    ,
    clp

    in

    ipairs
    (
    world
    .
    descriptor
    .
    color_pattern
    )

    do

    if

    clp
    .
    pattern
    ==
    "MONOTONE"

    then

    local

    cl
    =
    world
    .
    descriptor
    .
    color
    [
    clp
    .
    color
    [
    1
    ]]

    local

    diff
    =
    math.abs
    (
    wanted_color
    .
    r
    -
    cl
    .
    r
    )
    +
    math.abs
    (
    wanted_color
    .
    b
    -
    cl
    .
    b
    )
    +
    math.abs
    (
    wanted_color
    .
    g
    -
    cl
    .
    g
    )

    if

    diff
    <
    best_total_diff

    then

    best_clp
    =
    clp

    best_total_diff
    =
    diff

    end


---
*Parte 1 de 2 de «Lua script examples». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Lua_script_examples*
