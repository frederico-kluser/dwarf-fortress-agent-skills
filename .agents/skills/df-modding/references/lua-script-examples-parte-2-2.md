# Lua script examples (parte 2/2)

    end

    end

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[STATE_COLOR:"
    ..
    kk
    ..
    ":"
    ..
    best_clp
    .
    token
    ..
    "]"

    if

    kk
    ==
    "SOLID"

    then

    solid_cl
    =
    world
    .
    descriptor
    .
    color
    [
    best_clp
    .
    color
    [
    1
    ]]

    end

    end

    local

    color_str
    =
    solid_cl
    .
    col_f
    ..
    ":0:"
    ..
    solid_cl
    .
    col_br

    l
    (
    color_str
    )

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[DISPLAY_COLOR:"
    ..
    color_str
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
    "[BUILD_COLOR:"
    ..
    color_str
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
    "[ITEMS_METAL][ITEMS_HARD][ITEMS_SCALED][ITEMS_BARRED]"

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[SPECIAL]"

    if

    v
    .
    material
    .
    flags
    .
    ITEMS_DIGGER

    then

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEMS_DIGGER]"

    end

    local

    function

    new_value
    (
    str
    )

    mat_values
    [
    str
    ]
    =
    mat_values
    [
    str
    ]

    or

    math.floor
    ((
    adamantine
    .
    material
    [
    str
    ]
    *
    wafers
    +
    v
    .
    material
    [
    str
    ]
    *
    bars
    *
    3
    )
    *
    avg_denom
    +
    0.5
    )

    l
    (
    str
    ,
    mat_values
    [
    str
    ])

    return

    mat_values
    [
    str
    ]

    end

    local

    function

    new_value_nested
    (
    str1
    ,
    str2
    )

    mat_values
    [
    str1
    ..
    str2
    ]
    =
    mat_values
    [
    str1
    ..
    str2
    ]

    or

    math.floor
    ((
    adamantine
    .
    material
    [
    str1
    ][
    str2
    ]
    *
    wafers
    +
    v
    .
    material
    [
    str1
    ][
    str2
    ]
    *
    bars
    *
    3
    )
    /
    (
    bars
    *
    3
    +
    wafers
    )
    +
    0.5
    )

    l
    (
    str1
    ..
    str2
    ,
    mat_values
    [
    str1
    ..
    str2
    ])

    return

    mat_values
    [
    str1
    ..
    str2
    ]

    end

    if

    new_value_nested
    (
    "fracture"
    ,
    "SHEAR"
    )
    >
    170000

    or

    new_value_nested
    (
    "yield"
    ,
    "IMPACT"
    )
    >
    245000

    then

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEMS_WEAPON][ITEMS_AMMO]"

    if

    new_value
    (
    "solid_density"
    )
    <
    10000

    then

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[ITEMS_WEAPON_RANGED][ITEMS_ARMOR]"

    end

    end

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MATERIAL_VALUE:"
    ..
    new_value
    (
    "base_value"
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
    "[SPEC_HEAT:"
    ..
    new_value
    (
    "temp_spec_heat"
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
    "[MELTING_POINT:"
    ..
    new_value
    (
    "temp_melting_point"
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
    "[BOILING_POINT:"
    ..
    new_value
    (
    "temp_boiling_point"
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
    "[SOLID_DENSITY:"
    ..
    new_value
    (
    "solid_density"
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
    "[LIQUID_DENSITY:"
    ..
    new_value
    (
    "liquid_density"
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
    "[MOLAR_MASS:"
    ..
    new_value
    (
    "molar_mass"
    )
    ..
    "]"

    -- i don't think this is actually correct

    for

    _
    ,
    thing

    in

    ipairs
    ({
    "yield"
    ,
    "fracture"
    })

    do

    for

    force
    ,
    _

    in

    pairs
    (
    v
    .
    material
    [
    thing
    ])

    do

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "["
    ..
    string.upper
    (
    force
    )
    ..
    "_"
    ..
    string.upper
    (
    thing
    )
    ..
    ":"
    ..
    new_value_nested
    (
    thing
    ,
    force
    )
    ..
    "]"

    end

    end

    for

    _
    ,
    force

    in

    ipairs
    (
    "IMPACT"
    ,
    "COMPRESSIVE"
    ,
    "TENSILE"
    ,
    "TORSION"
    ,
    "SHEAR"
    ,
    "BENDING"
    )

    do

    local

    modulus

    =

    v
    .
    yield
    [
    force
    ]

    /

    v
    .
    elasticity
    [
    force
    ]

    local

    average_modulus

    =

    (
    adamantine_modulus
    *
    wafers

    +

    modulus
    *
    bars
    *
    3
    )
    *
    avg_denom

    local

    strain_at_yield

    =

    math.floor
    (
    new_value_nested
    (
    "yield"
    ,
    force
    )

    /

    average_modulus

    +

    0.5
    )

    -- usually zero, but can be 1 or 2 sometimes

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "["
    ..
    string.upper
    (
    force
    )
    ..
    "_YIELD:"
    ..
    new_value_nested
    (
    "yield"
    ,
    force
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
    "["
    ..
    string.upper
    (
    force
    )
    ..
    "_FRACTURE:"
    ..
    new_value_nested
    (
    "fracture"
    ,
    force
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
    "["
    ..
    string.upper
    (
    force
    )
    ..
    "_STRAIN_AT_YIELD:"
    ..
    strain_at_yield
    ..
    "]"

    end

    lines
    [
    #
    lines
    +
    1
    ]
    =
    "[MAX_EDGE:"
    ..
    new_value
    (
    "max_edge"
    )
    ..
    "]"

    local

    reaction_token
    =
    token
    ..
    "_MAKING"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]
    =
    "[REACTION:"
    ..
    reaction_token
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
    "[NAME:make adamantine "
    ..
    v
    .
    material
    .
    name
    .
    SOLID
    ..
    " (use bars)]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]
    =
    "[BUILDING:SMELTER:NONE]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]
    =
    "[REAGENT:A:"
    ..
    tostring
    (
    150
    *
    wafers
    )
    ..
    ":BAR:NO_SUBTYPE:METAL:ADAMANTINE]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]
    =
    "[REAGENT:B:"
    ..
    tostring
    (
    150
    *
    bars
    )
    ..
    ":BAR:NO_SUBTYPE:METAL:"
    ..
    v
    .
    token
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
    "[PRODUCT:100:"
    ..
    tostring
    (
    bars
    +
    wafers
    )
    ..
    ":BAR:NO_SUBTYPE:METAL:"
    ..
    token
    ..
    "][PRODUCT_DIMENSION:150]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]
    =
    "[FORTRESS_MODE_ENABLED]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]
    =
    "[CATEGORY:ADAMANTINE_ALLOYS]"

    if

    not

    done_category

    then

    done_category
    =
    true

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]
    =
    "[CATEGORY_NAME:Adamantine alloys]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]
    =
    "[CATEGORY_DESCRIPTION:Debase adamantine with other metals to get extremely strong alloys.]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]
    =
    "[CATEGORY_KEY:CUSTOM_SHIFT_A]"

    end

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]
    =
    "[FUEL]"

    reaction_lines
    [
    #
    reaction_lines
    +
    1
    ]
    =
    "[SKILL:SMELT]"

    end

    end

    local

    entity_lines
    =
    {}

    raws
    .
    register_inorganics
    (
    lines
    )

    -- not used in vanilla right now, due to lack of instruments, but you CAN do this

    raws
    .
    register_reactions
    (
    reaction_lines
    )

    end


---
*Parte 2 de 2 de «Lua script examples». Demais partes em arquivos `...-part-{1..2}.md` na mesma pasta. Fonte: https://dwarffortresswiki.org/index.php/Lua_script_examples*
